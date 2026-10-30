"""Stage C: read the Stage A slices by sector (oil and gas) for Abbott, Patrick and Paxton, 2025-26.
Analysis stage. Reads raw/ and Elements, never writes to them. Writes views/donors_<official>.csv
and views/summary.md. Stdlib only, no paid calls.

usage:
  python3 -I sector_read.py [--rulings PATH] [--out-dir DIR] [--list-unresolved N] [--official NAME]
  (input paths default to the Stage B paths; override with --tec-abbott, --tec-patrick,
   --fec-elements, --fec-repo-dir, --fec-totals)

Method (the plan's Stage C, oil-money-plan.md):
  Unit of analysis is the donor. Three passes, each writing its own columns; a later pass never
  overwrites an earlier one's columns. The final tier is resolved by precedence hand > entity > keyword.
    1. keyword pass on employer, occupation, job title and organization name -> kw_tier, kw_term
         strict terms: oil, gas, petrol*, drilling, exploration, E&P, midstream, pipeline, frac*,
                       oilfield, royalt*, mineral*, permian, refin*, crude, LNG, oilman, wildcat
         broad terms:  energy, electric*, utilit*, power, generation
         weak terms (hand check required): operating, resources, midland, production
         'not': a stated employer or occupation with no term (placeholders such as self, retired,
                investor, homemaker, 'information requested' do not count as stated); for an entity
                row with no employer, a PAC, association, union, law-firm or party name counts as
                stated (the name says who sponsors it), while a bare LLC, trust or company does not
    2. entity pass on contributor name and employer against ENTITIES below -> ent_tier, ent_canonical,
         ent_basis. Also merges aliases into one donor (Fairly's two vehicles, Musk's two trust
         spellings, Perot Jr.'s two spellings).
    3. hand pass from the rulings CSV (official, donor_key, tier, basis) -> hand_tier, hand_basis.
  Tiers: strict = TPJ-comparable (producers, oilfield services, midstream, refiners, royalty owners,
         their executives and families, their PACs and trade groups); broad = strict plus electric
         utilities, power generators and 'energy' investors; not = classified as something else;
         unclassified = no pass reached a verdict.
TEC rules (as in Stage B): infoOnlyFlag=Y rows dropped; campaign committee id only; schedules A1 and A2;
  window Jan 1 2025 - Oct 24 2026 on contributionDt.
FEC rules: newest filing per coverage period (superseded filings dropped); Schedule A rows with
  memo_code != X are the money (WinRed conduit rollups and redesignations are memo rows). A transfer
  from a joint fundraising committee (SA12) is replaced by its memo attribution rows so the underlying
  donors are read; when the memo rows do not sum to the transfer (the JFC nets its costs), each memo
  amount is scaled by transfer/memo-sum and the scale is recorded in the donor's `via` column. Memo
  rows filed without a back reference are attributed to the filing's transfer when it is the only one.
  A transfer with no memo rows stays one unclassified row. The
  non-memo SA11AI sum per filing is checked against the form's itemized-individual line.
Donor key: contributor name (organization, else 'LAST, FIRST'), upper-cased, punctuation stripped,
  plus zip5. The Chronicle's key adds city, occupation and employer; Stage B showed that key splits
  one donor who filed two employer spellings (Perot Jr.), so the key here is looser and the entity
  pass merges known aliases.
"""
import argparse, csv, hashlib, json, os, re, sys
from collections import defaultdict
from decimal import Decimal as D

csv.field_size_limit(10 ** 9)
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

TEC = {'abbott': ('00051153', 'Texans for Greg Abbott'), 'patrick': ('00064090', 'Texans for Dan Patrick'),
       'paxton_state': ('00051407', 'Ken Paxton, candidate/officeholder account (TEC)')}
CYCLE = ('20250101', '20261024')
FEC = {'paxton_senate': ('C00901918', 'Ken Paxton for Senate'),
       'paxton_victory': ('C00952218', 'Paxton Victory (joint fundraising committee)'),
       'lone_star_liberty': ('C00901223', 'Lone Star Liberty PAC (super PAC)')}

# ---------- keyword pass
STRICT = [r'\boil\b', r'\bgas\b', r'petrol', r'drilling', r'exploration', r'\bE ?& ?P\b', r'midstream', r'pipeline',
          r'\bfrac', r'oil ?field', r'royalt', r'mineral', r'permian', r'refin', r'\bcrude\b', r'\bLNG\b', r'oilman', r'wildcat',
          r'\bupstream\b', r'\bdownstream\b', r'landman', r'\bwell service', r'\bsaltwater disposal']
BROAD = [r'\benergy\b', r'electric', r'utilit', r'\bpower\b', r'\bgeneration\b']
WEAK = [r'\boperating\b', r'\bresources\b', r'\bmidland\b', r'\bproduction\b']
PLACEHOLDER = re.compile(r'^(self|self[- ]?employed|retired|none|n/?a|not employed|unemployed|homemaker|housewife|'
                         r'information requested.*|best efforts.*|requested|investor|investments?|private investor|'
                         r'business ?(owner|man|woman)?|entrepreneur|executive|owner|president|ceo|chairman|consultant|'
                         r'philanthropist|various|individual|private|personal|family|trust|founder|partner|manager|'
                         r'management|principal|rancher|ranching|farmer)[.\s]*$', re.I)


ORG_STATED = re.compile(r'\bPAC\b|POLITICAL ACTION|COMMITTEE|ASSOCIATION|\bASSN\b|\bUNION\b|\bLLP\b|\bPLLC\b|\bLAW\b|CAMPAIGN|\bPARTY\b|\bSOCIETY\b|\bFEDERATION\b|\bCOUNCIL\b|\bCOALITION\b', re.I)


def norm(s):
    s = (s or '').upper()
    s = re.sub(r'[^A-Z0-9 ,&]', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def stated(x):
    x = (x or '').strip()
    return bool(x) and not PLACEHOLDER.match(x)


def keyword_pass(employer, occupation, jobtitle, orgname):
    text = ' | '.join(x or '' for x in (employer, occupation, jobtitle, orgname))
    for t in STRICT:
        m = re.search(t, text, re.I)
        if m:
            return 'strict', m.group(0)
    for t in BROAD:
        m = re.search(t, text, re.I)
        if m:
            return 'broad', m.group(0)
    for t in WEAK:
        m = re.search(t, text, re.I)
        if m:
            return 'weak', m.group(0)
    if stated(employer) or stated(occupation) or stated(jobtitle):
        return 'not', 'stated employer/occupation, no term'
    if orgname and ORG_STATED.search(orgname):
        return 'not', 'PAC/association/firm name states its sponsor, no term'
    return '', ''


# ---------- entity pass
# (pattern on normalized name OR employer, tier, canonical donor name or None to keep the filed name, basis)
REG = 'knowledge-wiki/entities/'
ENTITIES = [
    # trade groups and company PACs (strict)
    (r'TEXAS OIL (AND|&) GAS ASSOCIATION|\bTXOGA\b', 'strict', None, f'{REG}orgs.csv O-00076/O-00313/O-02228 (industry)'),
    (r'TEXAS INDEPENDENT PRODUCERS|\bTIPRO\b', 'strict', None, f'{REG}orgs.csv O-00304 (industry)'),
    (r'PERMIAN BASIN PETROLEUM', 'strict', None, f'{REG}orgs.csv O-00224 (industry)'),
    (r'\bCHEVRON\b', 'strict', None, f'{REG}orgs.csv O-00103; producer'),
    (r'ENERGY TRANSFER', 'strict', None, f'{REG}people.csv E-0000158 Kelcy Warren, Executive Chairman; midstream'),
    (r'\bPIONEER NATURAL', 'strict', None, f'{REG}orgs.csv O-00226; producer'),
    (r'DIAMONDBACK', 'strict', None, f'{REG}orgs.csv O-00128; producer'),
    (r'DOUBLE EAGLE', 'strict', None, 'plan ruling: Campbell and Sellers (Double Eagle, Permian producer) strict'),
    (r'\bENDEAVOR ENERGY', 'strict', None, 'Endeavor Energy Resources, Midland producer (acquired by Diamondback 2024)'),
    (r'HUNT CONSOLIDATED|\bHUNT OIL\b', 'strict', None, 'Hunt Oil / Hunt Consolidated (Ray L. Hunt), producer'),
    (r'CROWNQUEST|CROWN ?ROCK', 'strict', None, f'{REG}orgs.csv O-02223 CrownQuest; people.csv E-0000221 Tim Dunn'),
    (r'TEXANS UNITED FOR A CONSERVATIVE MAJORITY|\bTUCM\b', 'strict', None, 'plan ruling: Dunn PAC (TUCM) strict; Tackett 2026-10-28'),
    (r'JEFFERSON RISING', 'strict', None, 'plan ruling: Dunn PAC (Jefferson Rising) strict; Mediaite 2026-09-02'),
    (r'WILKS BROTHERS|\bWILKS, (FARRIS|DAN|JO ?ANN|STACI)', 'strict', None, f'{REG}people.csv E-0000102/E-0000119 Dan and Farris Wilks; plan ruling (shale fortune)'),
    (r'MIDLAND ENERGY', 'strict', None, f'{REG}people.csv E-0407688 S. Javaid Anwar, Midland Energy Inc CEO; plan ruling'),
    (r'HILCORP', 'strict', None, 'Hilcorp Energy, producer (Jeffery Hildebrand)'),
    (r'GEOSOUTHERN', 'strict', None, 'plan ruling: Molleston (GeoSouthern) strict; GeoSouthern Energy, producer'),
    (r'\bFASKEN\b', 'strict', None, 'Fasken Oil and Ranch, Midland producer'),
    (r'DESERT ROYALTY', 'strict', None, f'{REG}people.csv E-0000165 Kyle L. Stallings; royalty owner'),
    (r'WESTERN REFINING|\bDELEK\b|VALERO|MARATHON PETROLEUM|PHILLIPS 66|\bCITGO\b|MOTIVA', 'strict', None, 'refiner'),
    (r'CONOCOPHILLIPS|EXXON ?MOBIL|OCCIDENTAL PETROLEUM|\bOXY\b|\bEOG\b|\bAPACHE CORP|\bDEVON ENERGY|OVINTIV|COTERRA|PERMIAN RESOURCES|MATADOR RESOURCES|CONCHO RESOURCES|HENRY RESOURCES|\bPARSLEY ENERGY|\bCALLON\b|\bSM ENERGY\b|\bMURPHY OIL|\bRANGE RESOURCES|\bCOMSTOCK RESOURCES|SILVERBOW|\bTUG HILL', 'strict', None, 'producer (public filings)'),
    (r'ENTERPRISE PRODUCTS|KINDER MORGAN|\bTARGA\b|\bPLAINS ALL AMERICAN|\bENLINK\b|WESTERN MIDSTREAM|\bONEOK\b|\bCHENIERE\b|\bNEXTDECADE\b|\bFREEPORT LNG|\bHOWARD ENERGY|\bWHITEWATER MIDSTREAM', 'strict', None, 'midstream / LNG'),
    (r'\bNGL ENERGY|\bNGL TEXAS PAC\b', 'strict', None, 'NGL Energy Partners (natural gas liquids midstream)'),
    (r'\bHALLIBURTON\b|SCHLUMBERGER|\bSLB\b|BAKER HUGHES|\bNABORS\b|PATTERSON.UTI|\bHELMERICH|\bPROPETRO\b|\bLIBERTY ENERGY|\bSELECT WATER|\bCACTUS WELLHEAD', 'strict', None, 'oilfield services'),
    (r'TEXAS PACIFIC LAND', 'strict', None, 'royalty and surface owner, Permian'),
    # broad entities
    (r'\bONCOR\b', 'broad', None, 'plan ruling: Oncor and its executives broad only (electric utility)'),
    (r'CENTERPOINT', 'broad', None, 'electric and gas utility (plan entity list)'),
    (r'\bVISTRA\b|\bTXU\b|LUMINANT', 'broad', None, 'power generator (plan entity list)'),
    (r'\bNRG\b', 'broad', None, 'power generator (plan entity list)'),
    (r'\bAEP\b|AMERICAN ELECTRIC POWER|\bENTERGY\b|\bCPS ENERGY\b|\bAUSTIN ENERGY\b|CONSTELLATION ENERGY|\bCALPINE\b|\bATMOS ENERGY', 'broad', None, 'electric or gas utility / generator'),
    # alias merges, ruled not oil and gas
    (r'^TEXAS REPUBLICAN LEADERSHIP FUND$|^DEALON LLC$', 'not', 'FAIRLY, ALEX (via Texas Republican Leadership Fund + DealOn LLC)',
     'Tribune 2026-10-06 (asset TXTRIB_2026-10-06_GREG_ABBOTT_BURNS_THROUGH_WAR_CHEST_IN_TEXAS_05F17 line 57) names Alex Fairly, insurance, as the giver through both; plan ruling: not oil and gas'),
    (r'^ELON MUSK RE[CV]O[CV]ABLE TRUST$|^MUSK, ELON$', 'not', 'MUSK, ELON (incl. Elon Musk Revocable Trust)', 'plan ruling: Musk not oil and gas; Patrick filing spells the trust two ways'),
    (r'^PEROT JR ?,? H ROSS$|^PEROT, H ROSS$', 'not', 'PEROT JR., H. ROSS (Hillwood)', 'plan ruling: Perot Jr. real estate, not oil and gas; filed under two spellings'),
    (r'^FISHER, KENNETH$', 'not', None, 'plan ruling: Fisher Investments, not oil and gas'),
    (r'^YASS, JEFF', 'not', None, 'plan ruling: Yass (Susquehanna), not oil and gas'),
    (r'^RGA RIGHT DIRECTION', 'not', None, 'Republican Governors Association PAC'),
]
MERGES = [
    # (pattern on normalized name, tier, canonical donor, basis, zips) -- same person or household filed under several names
    (r'^DUNCAN, JAN(ET)?( E)?$', 'strict', 'DUNCAN, JAN (widow of Enterprise Products founder Dan Duncan)', "Jan Duncan, widow of Dan Duncan, founder of Enterprise Products Partners (midstream; registry O-00140); family member; filed retired under two spellings", {'77019'}),
    (r'^MC ?CLANE JR ?, DRAYTON$|^MCLANE, DRAYTON$', 'not', 'MCLANE JR., DRAYTON (McLane Group)', 'McLane Group (distribution) per filed employer; two spellings', {'76503'}),
    (r'^NAU( III)?, JOHN$|^JLN III HOLDINGS,? LLC$', 'not', 'NAU III, JOHN (Silver Eagle Distributors; incl. JLN III Holdings)', 'Silver Eagle Distributors (beer) per filed employer; JLN III Holdings files from the same Houston zip', {'77019', '77219'}),
    (r'^(SSC INC|BALONEY FEATHERS LTD|TWO TOADS HOLDINGS,? LTD|CHARLENE MCDONALD, JOHNNY|MC ?DONALD, JOHNNY|MCDONALD, TIMMIE)$', 'strict', 'MCDONALD, JOHNNY (Lubbock oil producer; incl. SSC Inc, Baloney Feathers Ltd, Two Toads Holdings, spouse Timmie)', "Johnny McDonald filed occupation OIL PRODUCER to Paxton Victory; SSC Inc, Baloney Feathers Ltd, Two Toads Holdings and 'Charlene McDonald, Johnny' all file from his P.O. Box 1586, Lubbock 79408 (FEC street field)", {'79408'}),
    (r'^GORDY, (RUSSELL|GLENDA)$', 'strict', 'GORDY, RUSSELL (SG Interests; incl. Glenda Gordy)', 'Russell Gordy, SG Interests founder (plan ruling, flagged); Glenda Gordy files from the same Houston address (32 Crestwood Dr)', {'77007'}),
    (r'^NYE( JR)?, ERLE$', 'broad', 'NYE JR., ERLE (Oncor; incl. EN Consulting)', 'plan ruling: Oncor executives broad only; filed as Oncor general counsel and as EN Consulting', {'75225'}),
    (r'^STALLINGS, (KYLE|JAMIE)$', 'strict', 'STALLINGS, KYLE (Desert Royalty; incl. Jamie Stallings)', 'Desert Royalty / Permian Basin Acquisition Fund (filed employers); registry E-0000165; spouse files from the same zip', {'79701', '79702'}),
    (r'^HILDEBRAND, (JEFFERY|MELINDA)$', 'strict', 'HILDEBRAND, JEFFERY (Hilcorp; incl. Melinda Hildebrand)', 'Hilcorp Energy (filed employer); Melinda Hildebrand (ambassador) is his spouse, same zip', {'77251'}),
    (r'^HUNT, (RAY|NANCY ANN)$', 'strict', 'HUNT, RAY (Hunt Consolidated; incl. Nancy Ann Hunt)', 'Hunt Consolidated / Hunt Oil (filed employer); Nancy Ann Hunt is his spouse, same zip', {'75201'}),
    (r'^MONCRIEF, (RICHARD|GLORIA)$', 'strict', 'MONCRIEF, RICHARD (Moncrief Oil; incl. Gloria Moncrief)', 'Moncrief Oil International (filed employer); Gloria Moncrief is his spouse, same zip', {'76102'}),
    (r'^CAMPBELL, (CODY|TARA)$', 'strict', 'CAMPBELL, CODY (Double Eagle; incl. Tara Campbell)', 'plan ruling: Double Eagle strict; Cody Campbell files under two Fort Worth zips; Tara Campbell is his spouse', {'76107', '76109'}),
    (r'^DOGGETT, WILLIAM$', 'not', 'DOGGETT, WILLIAM (Doggett Equipment)', 'Doggett Equipment Services Group per filed employer; two zips', {'77019', '77037'}),
    (r'^DWYER, JOHN$', 'not', 'DWYER, JOHN (Capital Funding Group)', 'Capital Funding Group per filed employer; two zips', {'32951', '21209'}),
    (r'^GRAHAM, JAY$', 'strict', 'GRAHAM, JAY (Spur Energy Partners)', 'Spur Energy Partners (filed employer): Permian producer; two zips', {'77802', '77024'}),
    (r'^SCHARBAUER, DOUGLAS$', 'strict', 'SCHARBAUER, DOUGLAS (Midland; oil consultant, mineral owner)', "filed occupation 'Oil Consultant' to Patrick; Scharbauer family mineral rights; P.O. Box 2888 Midland on every committee", {'79702'}),
    (r'^SPARKS, (DON|GWYN|CHRISTOPHER)$', 'strict', 'SPARKS, DON (Discovery Operating; incl. Gwyn and Christopher Sparks)', 'Discovery Operating (filed employer), Midland oil and gas operator; household files from one zip', {'79705'}),
    (r'^BROOKS, (RANDY|J RANDAL)$', 'strict', 'BROOKS, RANDY (BNB Ventures)', "BNB Ventures, 'Fuel Sales and investing'; fuel distribution counted as oil industry (Saul's ruling 2026-10-29); two spellings", {'76903', '76904'}),
    (r'^DAVIS, RAY$', 'strict', 'DAVIS, RAY (Avatar Investments; Energy Transfer co-founder)', 'Avatar Investments (filed employer); co-founded Energy Transfer Partners, co-CEO to 2007', {'75225'}),
    (r'^SAULSBURY, (CHARLES|BUBBA)$', 'strict', 'SAULSBURY, CHARLES (Saulsbury Industries)', 'Saulsbury Industries (filed employer), Odessa midstream EPC contractor', {'79768', '79762'}),
    (r'^(MOAYEDI, MEHRDAD|MEHRDAD, MOAYEDI)$', 'not', 'MOAYEDI, MEHRDAD (Centurion American)', 'Centurion American (real estate) per filed employer; name fields reversed on one row', {'75234'}),
    (r'^SINCLAIR, DONALD$', 'strict', 'SINCLAIR, DONALD (Western Gas; WTX Pumping Services)', 'Western Gas CEO (Abbott filing); WTX Pumping Services chairman (Patrick filing)', {'77005'}),
]
ENT_RX = [(re.compile(p), t, c, b, None) for p, t, c, b in ENTITIES] + [(re.compile(p), t, c, b, z) for p, t, c, b, z in MERGES]


def entity_pass(name_n, employer_n, zip5=''):
    for rx, tier, canon, basis, zips in ENT_RX:
        if rx.search(name_n) and (zips is None or zip5 in zips):
            return tier, (canon or name_n), basis, 'name'
    for rx, tier, canon, basis, zips in ENT_RX:
        if zips is None and tier in ('strict', 'broad') and employer_n and rx.search(employer_n):
            return tier, name_n, basis, 'employer'
    return '', '', '', ''


# ---------- loaders
def tec_load(path, filer_id):
    out = []
    with open(path, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            if r['infoOnlyFlag'] == 'Y' or r['filerIdent'] != filer_id:
                continue
            if not (CYCLE[0] <= r['contributionDt'] <= CYCLE[1]):
                continue
            name = r['contributorNameOrganization'] or f"{r['contributorNameLast']}, {r['contributorNameFirst']}"
            out.append(dict(row_id=r['contributionInfoId'], amt=D(r['contributionAmount'] or '0'), date=r['contributionDt'],
                            name=name, zip5=(r['contributorStreetPostalCode'] or '')[:5], city=r['contributorStreetCity'],
                            employer=r['contributorEmployer'], occupation=r['contributorOccupation'], jobtitle=r['contributorJobTitle'],
                            orgname=r['contributorNameOrganization'], kind=r['schedFormTypeCd'], ptype=r['contributorPersentTypeCd'],
                            via=''))
    return out


def fec_load(path, cid):
    rows = [json.loads(l) for l in open(path, encoding='utf-8')]
    reps = {}
    for r in rows:
        rt, f = r['record_type'], r['fields']
        if rt in ('F3N', 'F3A'):
            reps.setdefault((f[15], f[16]), []).append((int(r['file_number']), D(f[32] or '0')))
        elif rt in ('F3XN', 'F3XA'):
            reps.setdefault((f[13], f[14]), []).append((int(r['file_number']), D(f[29] or '0')))
    keep, superseded, line11ai = set(), set(), {}
    for cov, lst in reps.items():
        lst.sort()
        keep.add(str(lst[-1][0])); line11ai[str(lst[-1][0])] = lst[-1][1]
        superseded |= {str(x[0]) for x in lst[:-1]}
    sa = [r for r in rows if r['record_type'].startswith('SA') and r['file_number'] in keep]
    # check: non-memo SA11AI per filing == form line 11(a)(i)
    checks = []
    per = defaultdict(D)
    for r in sa:
        n = r['named']
        if r['record_type'] == 'SA11AI' and n.get('memo_code') != 'X':
            per[r['file_number']] += D(n['contribution_amount'] or '0')
    for fn in sorted(keep):
        checks.append((fn, per[fn], line11ai[fn], per[fn] == line11ai[fn]))
    # memo attribution rows keyed by the transaction they attribute
    memos = defaultdict(list)
    orphan = defaultdict(list)   # SA12 memo rows with no back reference, by filing
    n_transfers = defaultdict(int)
    for r in sa:
        n = r['named']
        if n.get('memo_code') == 'X' and n['back_reference_tran_id']:
            memos[n['back_reference_tran_id']].append(r)
        elif n.get('memo_code') == 'X' and r['record_type'] == 'SA12':
            orphan[r['file_number']].append(r)
        elif r['record_type'] == 'SA12':
            n_transfers[r['file_number']] += 1
    out, transfers = [], []
    for r in sa:
        n = r['named']
        if n.get('memo_code') == 'X':
            continue
        rid = n['transaction_id'] if n['transaction_id'].startswith(r['record_type']) else f"{r['record_type']}.{n['transaction_id']}"
        base = dict(amt=D(n['contribution_amount'] or '0'), date=n['contribution_date'], kind=r['record_type'], city=n['contributor_city'],
                    ptype=n['entity_type'], via='')
        if r['record_type'] == 'SA12':
            att = memos.get(n['transaction_id'], [])
            if not att and orphan.get(r['file_number']) and n_transfers[r['file_number']] == 1:
                att = orphan[r['file_number']]   # the filing's JFC memo rows carry no back reference; one transfer in the filing, so they attribute it
            att_sum = sum((D(m['named']['contribution_amount'] or '0') for m in att), D(0))
            src = n['contributor_organization_name'] or n['donor_committee_name'] or n['memo_text_description']
            transfers.append((rid, src, base['amt'], len(att), att_sum))
            if att and att_sum > 0:
                scale = base['amt'] / att_sum
                how = 'by attribution' if scale == 1 else f'pro rata (memo rows sum {att_sum} against transfer {base["amt"]}; each memo amount x {scale:.6f})'
                for m in att:
                    mn = m['named']
                    out.append(dict(row_id=mn['transaction_id'] if mn['transaction_id'].startswith(m['record_type']) else f"{m['record_type']}.{mn['transaction_id']}", amt=(D(mn['contribution_amount'] or '0') * scale).quantize(D('0.01')), date=mn['contribution_date'],
                                    name=mn['contributor_organization_name'] or f"{mn['contributor_last_name']}, {mn['contributor_first_name']}",
                                    zip5=(mn['contributor_zip'] or '')[:5], city=mn['contributor_city'], employer=mn['contributor_employer'],
                                    occupation=mn['contributor_occupation'], jobtitle='', orgname=mn['contributor_organization_name'],
                                    kind=m['record_type'], ptype=mn['entity_type'], via=f'JFC transfer {rid} from {src}, read {how}'))
                continue
            out.append(dict(base, row_id=rid, name=f'TRANSFER FROM {src}'.strip(), zip5=(n['contributor_zip'] or '')[:5], employer='', occupation='',
                            jobtitle='', orgname=src, via='unattributed transfer'))
            continue
        out.append(dict(base, row_id=rid, name=n['contributor_organization_name'] or f"{n['contributor_last_name']}, {n['contributor_first_name']}",
                        zip5=(n['contributor_zip'] or '')[:5], employer=n['contributor_employer'], occupation=n['contributor_occupation'],
                        jobtitle='', orgname=n['contributor_organization_name']))
    return out, checks, sorted(superseded), transfers


# ---------- rulings
def load_rulings(path):
    out = {}
    if not path or not os.path.exists(path):
        return out
    with open(path, encoding='utf-8') as f:
        for r in csv.DictReader(l for l in f if not l.startswith('#')):
            if not (r.get('donor_key') or '').strip():
                continue
            key = (r['official'].strip(), norm(r['donor_key'].split('|')[0]), r['donor_key'].split('|')[1].strip() if '|' in r['donor_key'] else '*')
            out[key] = (r['tier'].strip(), r['basis'].strip(), (r.get('flag') or '').strip().upper())
    return out


def hand_lookup(rulings, official, name_n, zip5):
    for off in (official, '*'):
        for z in (zip5, '*'):
            v = rulings.get((off, name_n, z))
            if v:
                return v
    return None


# ---------- classify
def classify(official, rows, rulings):
    donors = {}
    for r in rows:
        name_n, emp_n = norm(r['name']), norm(r['employer'])
        kw_tier, kw_term = keyword_pass(r['employer'], r['occupation'], r['jobtitle'], r['orgname'])
        ent_tier, canon, ent_basis, ent_how = entity_pass(name_n, emp_n, r['zip5'])
        key = (canon if (ent_tier and canon != name_n) else name_n, r['zip5'] if not (ent_tier and canon != name_n) else '*')
        d = donors.get(key)
        if d is None:
            d = donors[key] = dict(donor=key[0], zip5=key[1], total=D(0), n_rows=0, row_ids=[], names=set(), employers=set(),
                                   occupations=set(), kw=set(), ent=set(), via=set(), kinds=set(), first=r['date'], last=r['date'])
        d['total'] += r['amt']; d['n_rows'] += 1; d['row_ids'].append(r['row_id'])
        d['names'].add(r['name']); d['kinds'].add(r['kind'])
        if r['employer'].strip(): d['employers'].add(r['employer'].strip())
        if r['occupation'].strip(): d['occupations'].add(r['occupation'].strip())
        if r['jobtitle'].strip(): d['occupations'].add(r['jobtitle'].strip())
        if kw_tier: d['kw'].add((kw_tier, kw_term))
        if ent_tier: d['ent'].add((ent_tier, ent_basis, ent_how))
        if r['via']: d['via'].add(r['via'])
        d['first'], d['last'] = min(d['first'], r['date']), max(d['last'], r['date'])
    out = []
    RANK = {'strict': 4, 'broad': 3, 'weak': 2, 'not': 1, '': 0}
    for key, d in donors.items():
        # keyword column: the strongest verdict among the donor's rows
        kw_tier, kw_term = max(d['kw'], key=lambda x: RANK[x[0]]) if d['kw'] else ('', '')
        ent_tier, ent_basis = ('', '')
        if d['ent']:
            e = max(d['ent'], key=lambda x: RANK[x[0]])
            ent_tier, ent_basis = e[0], f'{e[1]} [matched on {e[2]}]'
        hand = hand_lookup(rulings, official, norm(d['donor']), d['zip5'])
        if not hand:
            for nm in sorted(d['names']):
                hand = hand_lookup(rulings, official, norm(nm), d['zip5'])
                if hand: break
        hand_tier, hand_basis, hand_flag = hand if hand else ('', '', '')
        if hand_tier:
            tier, decided = hand_tier, 'hand'
        elif ent_tier:
            tier, decided = ent_tier, 'entity'
        elif kw_tier in ('strict', 'broad', 'not'):
            tier, decided = kw_tier, 'keyword'
        else:
            tier, decided = 'unclassified', ''
        out.append(dict(official=official, donor=d['donor'], zip5=d['zip5'], total=d['total'], n_rows=d['n_rows'], first=d['first'], last=d['last'],
                        tier=tier, decided_by=decided, kw_tier=kw_tier, kw_term=kw_term, ent_tier=ent_tier, ent_basis=ent_basis,
                        hand_tier=hand_tier, hand_basis=hand_basis, hand_flag=hand_flag, names=' ; '.join(sorted(d['names'])), employers=' ; '.join(sorted(d['employers'])),
                        occupations=' ; '.join(sorted(d['occupations'])), kinds=' '.join(sorted(d['kinds'])), via=' ; '.join(sorted(d['via'])),
                        row_ids=' '.join(d['row_ids'])))
    out.sort(key=lambda x: (-x['total'], x['donor']))
    return out


def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def money(x):
    return f'${x:,.2f}'


def pct(a, b):
    return f'{(a / b * 100):.1f}%' if b else 'n/a'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tec-abbott', default='/Volumes/Elements/reference-data/tec-cf-bulk/2026-10-29/slices/tec_abbott.csv')
    ap.add_argument('--tec-patrick', default=os.path.join(ROOT, 'raw', 'tec_patrick.csv'))
    ap.add_argument('--tec-paxton', default='/Volumes/Elements/reference-data/tec-cf-bulk/2026-10-29/slices/tec_paxton.csv')
    ap.add_argument('--with-paxton-state', action='store_true', help='also read Paxton\'s TEC officeholder account 00051407 (state career; off by default so the 2025-26 views stay as published)')
    ap.add_argument('--fec-elements', default='/Volumes/Elements/reference-data/fec-efiling/2026-10-29/fec_C00901918.jsonl')
    ap.add_argument('--fec-repo-dir', default=os.path.join(ROOT, 'raw'))
    ap.add_argument('--fec-totals', default=os.path.join(ROOT, 'raw', 'fec_totals.json'))
    ap.add_argument('--rulings', default=os.path.join(HERE, 'hand_rulings.csv'))
    ap.add_argument('--rulings-extra', default='', help='second rulings file loaded after --rulings (its keys win); used for the career window')
    ap.add_argument('--out-dir', default=os.path.join(ROOT, 'views'))
    ap.add_argument('--list-unresolved', type=int, default=0, help='print the N largest donors per official that still need a hand call, then exit')
    ap.add_argument('--official', default='', help='restrict to one official key')
    ap.add_argument('--window', default='', help='TEC window as YYYYMMDD:YYYYMMDD (default Jan 1 2025 - Oct 24 2026); FEC committees are skipped when set')
    ap.add_argument('--suffix', default='', help='suffix for output file names, e.g. _2017-2020')
    ap.add_argument('--list-top', type=int, default=0, help='print the N largest donors per official with current verdicts, then exit')
    ap.add_argument('--min', type=float, default=0, help='with --list-top: only donors at or above this total')
    a = ap.parse_args()
    global CYCLE
    if a.window:
        CYCLE = tuple(a.window.split(':'))
    rulings = load_rulings(a.rulings)
    if a.rulings_extra:
        rulings.update(load_rulings(a.rulings_extra))
    inputs = {'tec_abbott': a.tec_abbott, 'tec_patrick': a.tec_patrick, 'fec_C00901918': a.fec_elements,
              'fec_C00952218': os.path.join(a.fec_repo_dir, 'fec_C00952218.jsonl'), 'fec_C00901223': os.path.join(a.fec_repo_dir, 'fec_C00901223.jsonl'),
              'fec_totals': a.fec_totals, 'rulings': a.rulings, 'tool': os.path.abspath(__file__)}
    if a.rulings_extra:
        inputs['rulings_extra'] = a.rulings_extra
    if a.with_paxton_state or a.official == 'paxton_state':
        inputs['tec_paxton'] = a.tec_paxton
    fec_totals = json.load(open(a.fec_totals))

    officials = {}
    if not a.official or a.official == 'abbott':
        officials['abbott'] = dict(rows=tec_load(a.tec_abbott, TEC['abbott'][0]), label=TEC['abbott'][1], source='TEC', checks=[], superseded=[], transfers=[])
    if not a.official or a.official == 'patrick':
        officials['patrick'] = dict(rows=tec_load(a.tec_patrick, TEC['patrick'][0]), label=TEC['patrick'][1], source='TEC', checks=[], superseded=[], transfers=[])
    if (a.with_paxton_state and not a.official) or a.official == 'paxton_state':
        officials['paxton_state'] = dict(rows=tec_load(a.tec_paxton, TEC['paxton_state'][0]), label=TEC['paxton_state'][1], source='TEC', checks=[], superseded=[], transfers=[])
    for key, (cid, label) in FEC.items():
        if (a.official and a.official != key) or a.window:
            continue
        rows, checks, sup, transfers = fec_load(inputs[f'fec_{cid}'], cid)
        officials[key] = dict(rows=rows, label=label, source='FEC', checks=checks, superseded=sup, transfers=transfers, cid=cid)

    results = {}
    for key, o in officials.items():
        results[key] = classify(key, o['rows'], rulings)

    if a.list_top:
        for key, donors in results.items():
            print(f"\n=== {key}")
            for d in donors[:a.list_top]:
                if d['total'] < D(str(a.min)): break
                print(f"{d['total']:>13,.0f} | {d['donor']}|{d['zip5']} | {d['tier']}/{d['decided_by']} kw={d['kw_tier']}:{d['kw_term']} | emp={d['employers'][:55]} | occ={d['occupations'][:40]} | {d['via'][:30]}")
        return
    if a.list_unresolved:
        for key, donors in results.items():
            tot = sum(d['total'] for d in donors)
            print(f"\n=== {key}: {len(donors)} donors, itemized {money(tot)}")
            n = 0
            for d in donors:
                needs = d['tier'] == 'unclassified' or d['kw_tier'] == 'weak' or (d['decided_by'] == 'keyword' and d['kw_tier'] == 'broad')
                if not needs:
                    continue
                n += 1
                if n > a.list_unresolved:
                    break
                print(f"{d['total']:>14,.2f} | {d['donor']}|{d['zip5']} | kw={d['kw_tier']}:{d['kw_term']} | emp={d['employers'][:60]} | occ={d['occupations'][:50]} | {d['city'] if 'city' in d else ''}{d['via'][:40]}")
        return

    os.makedirs(a.out_dir, exist_ok=True)
    cols = ['official', 'donor', 'zip5', 'total', 'n_rows', 'first', 'last', 'tier', 'decided_by', 'kw_tier', 'kw_term', 'ent_tier', 'ent_basis',
            'hand_tier', 'hand_basis', 'hand_flag', 'names', 'employers', 'occupations', 'kinds', 'via', 'row_ids']
    W = f'{CYCLE[0][:4]}-{CYCLE[0][4:6]}-{CYCLE[0][6:]} to {CYCLE[1][:4]}-{CYCLE[1][4:6]}-{CYCLE[1][6:]}'
    lines = [f'# Stage C: oil-and-gas share of money to Abbott, Patrick and Paxton, {W} (TEC window; FEC: 2026 cycle)', '',
             f'Generated by `tools/sector_read.py`. Method in the tool docstring and in `../writing/gop-deserves-to-lose-texas/oil-money-plan.md` (Stage C). '
             'Consumers read this view and `donors_<official>.csv`; nobody re-derives it. Every donor row lists the raw row ids behind it '
             '(TEC `contributionInfoId`; FEC `<schedule>.<transaction_id>`).', '',
             '**Command** (from `tx-campaign-money/tools/`):', '', '```bash',
             'cd "/Users/saulelbein/Documents/Claude Code/tx-campaign-money/tools" && python3 -I sector_read.py' + (f' --official abbott --window {CYCLE[0]}:{CYCLE[1]} --suffix {a.suffix}' if a.window else ''), '```', '',
             '## Inputs (sha256)', '', '| Input | Path | sha256 |', '|---|---|---|']
    for k, p in inputs.items():
        lines.append(f'| {k} | `{p}` | `{sha(p) if os.path.exists(p) else "missing"}` |')
    lines += ['', '## Summary table', '',
              '| Official | Committee | Total raised | Strict oil & gas | Share of total | Strict share of classified $ | Broad (strict + utilities, power, energy) | Share of total | Classified not oil & gas | Unclassified (incl. unitemized) | Share | Classified coverage |',
              '|---|---|---|---|---|---|---|---|---|---|---|---|']
    detail = []
    for key, donors in results.items():
        o = officials[key]
        itemized = sum(d['total'] for d in donors)
        if o['source'] == 'TEC':
            total = itemized; unitemized = D(0); total_note = 'sum of every A1/A2 row in the window (TEC itemizes everything for these filers)'
        else:
            total = D(str(fec_totals[o['cid']]['total_receipts'])) if o['cid'] in fec_totals and 'total_receipts' in fec_totals[o['cid']] else None
            if total is None:
                total = D(str(fec_totals.get(o['cid'], {}).get('receipts', '0')))
            unitemized = total - itemized; total_note = 'FEC total receipts for the 2026 cycle (Stage B check passed); itemized Schedule A rows are read, the rest is unitemized or other receipts and stays unclassified'
        by = defaultdict(D); n_by = defaultdict(int)
        for d in donors:
            by[d['tier']] += d['total']; n_by[d['tier']] += 1
        strict, broad_only, not_ = by['strict'], by['broad'], by['not']
        broad = strict + broad_only
        uncl = by['unclassified'] + unitemized
        classified = strict + broad_only + not_
        lines.append(f"| {key} | {o['label']} | {money(total)} | {money(strict)} | {pct(strict, total)} | {pct(strict, classified)} | {money(broad)} | {pct(broad, total)} | {money(not_)} | {money(uncl)} | {pct(uncl, total)} | {pct(classified, total)} |")
        detail += ['', f"## {key}: {o['label']}", '', f'- Total raised: {money(total)} ({total_note}).',
                   f"- Itemized rows read: {len(o['rows'])}; distinct donors after dedupe: {len(donors)}.",
                   f"- Strict: {money(strict)} from {n_by['strict']} donors ({pct(strict, total)}). Broad-only additions (utilities, power, 'energy' not promoted to strict): {money(broad_only)} from {n_by['broad']} donors. Broad total: {money(broad)} ({pct(broad, total)}).",
                   f"- Classified not oil and gas: {money(not_)} from {n_by['not']} donors. Unclassified: {money(by['unclassified'])} itemized from {n_by['unclassified']} donors" + (f' plus {money(unitemized)} unitemized/other' if unitemized else '') + f'. Classified coverage: {pct(classified, total)} of dollars.',
                   f"- Decided by: " + ', '.join(f"{p} {money(sum(d['total'] for d in donors if d['decided_by'] == p))}" for p in ('hand', 'entity', 'keyword')) + '.']
        if o['source'] == 'FEC':
            bad = [c for c in o['checks'] if not c[3]]
            detail.append(f"- Dedupe check (non-memo SA11AI per filing == form line 11(a)(i)): {len(o['checks']) - len(bad)} of {len(o['checks'])} filings match" + (f"; mismatches: {[(c[0], str(c[1]), str(c[2])) for c in bad]}" if bad else '') + f". Superseded filings dropped: {o['superseded'] or 'none'}.")
            if o['transfers']:
                detail.append('- Transfers (SA12): ' + '; '.join(f"{rid} from {src or '?'} {money(amt)} ({n} memo rows summing {money(s)}{', read by attribution' if n and s == amt else (', read pro rata' if n else ', kept as one unattributed row')})" for rid, src, amt, n, s in o['transfers']) + '.')
        detail += ['', '**Top ten strict donors**', '', '| # | Donor | Total | Decided by | Basis | Rows |', '|---|---|---|---|---|---|']
        top = [d for d in donors if d['tier'] == 'strict'][:10]
        for i, d in enumerate(top, 1):
            basis = d['hand_basis'] if d['decided_by'] == 'hand' else (d['ent_basis'] if d['decided_by'] == 'entity' else f"keyword '{d['kw_term']}' in employer/occupation: {d['employers']} / {d['occupations']}")
            detail.append(f"| {i} | {d['donor']} ({d['employers'][:60] or d['occupations'][:60] or 'entity'}) | {money(d['total'])} | {d['decided_by']} | {basis[:160]} | {d['row_ids'][:200]} |")
        detail += ['', '**Largest broad-only donors (not in strict)**', '']
        for d in [d for d in donors if d['tier'] == 'broad'][:5]:
            detail.append(f"- {d['donor']}: {money(d['total'])} ({d['employers'][:50] or d['occupations'][:50]}); {d['decided_by']}")
        detail += ['', '**Largest unclassified donors**', '']
        for d in [d for d in donors if d['tier'] == 'unclassified'][:8]:
            detail.append(f"- {d['donor']}: {money(d['total'])} (employer: {d['employers'][:40] or 'blank'}; occupation: {d['occupations'][:40] or 'blank'}; {d['via'][:50]})")
        with open(os.path.join(a.out_dir, f'donors_{key}{a.suffix}.csv'), 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            for d in donors:
                w.writerow({c: (str(d[c]) if c == 'total' else d[c]) for c in cols})
    if all(k in results for k in ('paxton_senate', 'paxton_victory', 'lone_star_liberty')):
        tot = D(0); by = defaultdict(D); netted = D(0)
        for k in ('paxton_senate', 'paxton_victory', 'lone_star_liberty'):
            o = officials[k]
            t = D(str(fec_totals[o['cid']]['total_receipts'])) if 'total_receipts' in fec_totals[o['cid']] else D(str(fec_totals[o['cid']].get('receipts', '0')))
            tot += t
            item = D(0)
            for d in results[k]:
                if k == 'paxton_senate' and 'from PAXTON VICTORY' in d['via']:
                    netted += d['total']; continue
                by[d['tier']] += d['total']; item += d['total']
            by['unclassified'] += t - item - (netted if k == 'paxton_senate' else D(0))
        tot -= netted
        strict, broad = by['strict'], by['strict'] + by['broad']; classified = by['strict'] + by['broad'] + by['not']; uncl = by['unclassified']
        lines.append(f"| paxton_combined | three committees, net of Paxton Victory transfers into the campaign ({money(netted)}) | {money(tot)} | {money(strict)} | {pct(strict, tot)} | {pct(strict, classified)} | {money(broad)} | {pct(broad, tot)} | {money(by['not'])} | {money(uncl)} | {pct(uncl, tot)} | {pct(classified, tot)} |")
        lines.append('')
        lines.append('The combined Paxton row adds the campaign, the joint fundraising committee and the super PAC. Only transfers from Paxton Victory into the campaign are netted; Team Paxton (a separate joint committee not pulled) and other committees transfer money into these three and are read through their memo attributions. The super PAC is independent spending, not the campaign, so quote the rows separately where the distinction matters.')
    lines += detail
    lines += ['', '## Judgment calls flagged for Saul (hand_flag=Y)', '', '| Official | Donor | Total | Tier | Basis |', '|---|---|---|---|---|']
    for key, donors in results.items():
        for d in donors:
            if d['hand_flag'] == 'Y':
                lines.append(f"| {key} | {d['donor']} | {money(d['total'])} | {d['tier']} | {d['hand_basis'][:220]} |")
    lines += ['', '## Rulings applied by hand', '', f"{len(rulings)} rulings in `{os.path.relpath(a.rulings, ROOT)}`; each names its basis in the donor CSV's `hand_basis` column.", '',
              '## Caveats', '',
              '- Keyword verdicts rest on what the donor filed as employer and occupation. A producer whose employer field names no oil-and-gas term and who is below the hand pass stays `not` or `unclassified`; the hand pass covers the largest donors, so the error is in the small-dollar tail.',
              "- `broad` by keyword means the word 'energy', 'electric', 'utility' or 'power' and nothing stronger; where the hand pass found the company is an oil-and-gas company it is promoted to strict.",
              "- Strict includes petrochemicals, fuel wholesale and distribution, and fuel hauling (Saul's ruling 2026-10-29). Retail convenience stores (Buc-ee's) stay out and are flagged.",
              '- In-kind (TEC A2) counts, as the Chronicle counts it. Loans are not in the slices. TEC itemizes every contribution for these filers, so there is no unitemized remainder on the TEC rows; FEC unitemized money is in the unclassified column.',
              '- Paxton Victory distributes to Ken Paxton for Senate and other participants; its money and the campaign\'s overlap by the transfers listed above. Do not add the three Paxton rows without netting them.']
    with open(os.path.join(a.out_dir, f'summary{a.suffix}.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print('\n'.join(lines[lines.index('## Summary table'):lines.index('## Summary table') + 4 + len(results)]))
    for key, o in officials.items():
        if o['source'] == 'FEC':
            bad = [c for c in o['checks'] if not c[3]]
            print(key, 'form-line check', 'PASS' if not bad else f'FAIL {bad}')


if __name__ == '__main__':
    main()
