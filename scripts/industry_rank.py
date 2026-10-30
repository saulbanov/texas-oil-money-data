"""Rank donor industries for each official's 2025-26 money, so oil and gas can be compared with other industries.

Analysis stage downstream of sector_read.py. Reads the persisted donor views (views/donors_<official>.csv) verbatim
and adds one column: industry. It never changes the oil-and-gas tier: strict donors are Oil & Gas, broad donors are
"Energy, other". Every other donor gets an industry from, in order:
  1. a hand ruling in tools/industry_rulings.csv (official,donor_key,industry,basis), donor_key = NAME|zip5 or NAME|*
  2. keyword rules over the filed employer, occupation and donor name
  3. keyword rules over the stated basis text of the oil-tier rulings (hand_basis, ent_basis), which often name a
     business line ("auto dealer", "law firm PAC")
  4. Retired or homemaker, employer not given  /  Not identified
Unitemized FEC money is its own row.

Scheme: OpenSecrets sectors and industries (labels as reproduced in published tables; OpenSecrets' own site refused
our fetch on 2026-10-30, so the labels were not checked against its page). Oil & Gas and "Energy, other" sit in the
Energy/Natural Resources sector. Candidate and party committees are split out of Ideology/Single-Issue.

Writes views/industry_<official>.csv and views/industries_2025-26.md (input sha256s, per-official ranking, coverage).
python3 -I industry_rank.py
"""
import csv, hashlib, os, re, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); VIEWS = os.path.join(ROOT, 'views')
sys.path.insert(0, HERE)
from sector_read import norm  # same normalizer as the donor key

OFFICIALS = [('abbott', 'Texans for Greg Abbott'), ('patrick', 'Texans for Dan Patrick'),
             ('paxton_senate', 'Ken Paxton for Senate'), ('paxton_victory', 'Paxton Victory (joint committee)'),
             ('lone_star_liberty', 'Lone Star Liberty PAC (super PAC)')]
PAXTON = ['paxton_senate', 'paxton_victory', 'lone_star_liberty']

# Our industry -> the OpenSecrets industries it spans (checked 2026-10-30 against raw/opensecrets_industries_by_sector_2026-10-30.txt)
OS_MAP = {
    'Oil & Gas': 'Oil & Gas + Natural Gas Pipelines; also chemical makers (OpenSecrets: Misc Business, Chemical & Related Manufacturing) and fuel distribution, by Saul\'s 2026-10-29 ruling',
    'Energy, other': 'Electric Utilities; Alternative Energy Production & Services; diversified energy fortunes (no OpenSecrets equivalent)',
    'Real Estate': 'Real Estate', 'Securities & Investment': 'Securities & Investment; Venture Capital; Hedge Funds; Private Equity & Investment Firms',
    'Banking & Finance': 'Commercial Banks; Credit Unions; Finance / Credit Companies; Mortgage Bankers & Brokers', 'Insurance': 'Insurance',
    'Home Builders': 'Home Builders', 'Construction & Contractors': 'General Contractors; Special Trade Contractors; Construction Services; Architectural Services; Building Materials & Equipment',
    'Hospitals & Nursing Homes': 'Hospitals & Nursing Homes', 'Health Professionals': 'Health Professionals; Dentists; Nurses; Chiropractors',
    'Health Services & Pharmaceuticals': 'Health Services/HMOs; Pharmaceuticals / Health Products; Medical Supplies',
    'Lawyers / Law Firms': 'Lawyers / Law Firms', 'Lobbyists & Consultants': 'Lobbyists; political consultants (OpenSecrets may file some under Business Services)',
    'Tech & Internet': 'Computer Software; Internet; Electronics Manufacturing & Equipment', 'Telecom & Media': 'Telephone Utilities; Telecom Services & Equipment; TV / Movies / Music; Printing & Publishing',
    'Car Dealers': 'Car Dealers; Automotive', 'Transportation & Rail': 'Air Transport; Trucking; Railroads; Sea Transport',
    'Retail, Food & Beverage': 'Food & Beverage; Restaurants & Drinking Establishments; Beer, Wine & Liquor; Retail Sales; Food Stores; Clothing Manufacturing (Phil Knight)',
    'Manufacturing & Industry': 'Steel Production; Misc Manufacturing & Distributing; Chemical & Related Manufacturing (non-petrochemical)',
    'Casinos / Gambling': 'Casinos / Gambling; Indian Gaming', 'Business Services & Associations': 'Business Associations; Business Services; Miscellaneous Services; Advertising/Public Relations; For-profit Prisons',
    'Recreation / Live Entertainment': 'Recreation / Live Entertainment; Professional Sports, Sports Arenas & Related Equipment & Services',
    'Ranching & Agriculture': 'Livestock; Farm Bureaus; Crop Production & Basic Processing; Forestry & Forest Products',
    'Ideological & Single-Issue Groups': 'Republican/Conservative and the other issue industries', 'Candidate & Party Committees': 'Candidate Committees; Leadership PACs (party committees have no OpenSecrets industry)',
    'Labor': 'all union industries', 'Education & Nonprofits': 'Education; Non-profits, Foundations & Philanthropists; For-profit Education; Clergy',
}

SECTOR = {
    'Oil & Gas': 'Energy & Natural Resources', 'Energy, other': 'Energy & Natural Resources',
    'Real Estate': 'Finance, Insurance & Real Estate', 'Securities & Investment': 'Finance, Insurance & Real Estate',
    'Banking & Finance': 'Finance, Insurance & Real Estate', 'Insurance': 'Finance, Insurance & Real Estate',
    'Home Builders': 'Construction', 'Construction & Contractors': 'Construction',
    'Hospitals & Nursing Homes': 'Health', 'Health Professionals': 'Health',
    'Health Services & Pharmaceuticals': 'Health',
    'Lawyers / Law Firms': 'Lawyers & Lobbyists', 'Lobbyists & Consultants': 'Lawyers & Lobbyists',
    'Tech & Internet': 'Communications/Electronics', 'Telecom & Media': 'Communications/Electronics',
    'Car Dealers': 'Transportation', 'Transportation & Rail': 'Transportation',
    'Retail, Food & Beverage': 'Misc Business', 'Manufacturing & Industry': 'Misc Business',
    'Casinos / Gambling': 'Misc Business', 'Business Services & Associations': 'Misc Business',
    'Recreation / Live Entertainment': 'Misc Business',
    'Ranching & Agriculture': 'Agribusiness',
    'Ideological & Single-Issue Groups': 'Ideological/Single-Issue', 'Candidate & Party Committees': 'Ideological/Single-Issue',
    'Labor': 'Labor', 'Education & Nonprofits': 'Other',
    'Retired or Homemaker (employer not given)': 'Not identified', 'Not identified': 'Not identified',
    'Unitemized (FEC)': 'Not identified',
}

# (industry, regex). Order matters: first hit wins. Applied to employer/occupation/name, then to basis text.
RULES = [
    ('Candidate & Party Committees', r"\b(FOR (CONGRESS|SENATE|TEXAS|GOVERNOR|STATE)|CAMPAIGN|COMMITTEE TO ELECT|FRIENDS OF (SENATOR|REP|JUDGE)|REPUBLICAN (PARTY|NATIONAL)|VICTORY|RNC|NRSC|GOP|CANDIDATE|STATE REPRESENTATIVE|STATE SENATOR)\b|^TEXANS FOR [A-Z]+ [A-Z]+$"),
    ('Casinos / Gambling', r'\b(TRIBE|TRIBAL|NATION OF|CHOCTAW|CHICKASAW|KICKAPOO|CASINO|GAMING|GAMBLING)\b'),
    ('Labor', r'\b(UNION|BROTHERHOOD|TEAMSTERS|AFL|IBEW|FIREFIGHTERS|POLICE ASSOCIATION|OPERATING ENGINEERS)\b'),
    ('Lawyers / Law Firms', r'\b(LAW FIRM|LAWYER|ATTORNEY|LLP|PLLC|L L P|LEGAL|COUNSEL|BAKER BOTTS|BRACEWELL|JACKSON WALKER|VINSON|AKIN|LANIER|TRIAL)\b|^LAW\b| LAW$'),
    ('Lobbyists & Consultants', r'\b(LOBBY|LOBBYIST|GOVERNMENT(AL)? (AFFAIRS|RELATIONS)|PUBLIC AFFAIRS|POLITICAL CONSULT|STRATEG(Y|IES|IST)|BLACKRIDGE|CONSULTING|CONSULTANT|PUBLIC BLUEPRINT)\b'),
    ('Ideological & Single-Issue Groups', r'\b(LAWSUIT REFORM|SCHOOL CHOICE|CLUB FOR GROWTH|FREEDOM|LIBERTY|CONSERVATIVE|RESPONSIBLE GOVERNMENT|TRUTH|PRO[- ]LIFE|ACTION FUND|GOPAC|MAJORITY|ALLIANCE|ORGANIZING)\b'),
    ('Hospitals & Nursing Homes', r'\b(HOSPITAL|MEDICAL CENTER|HEALTH SYSTEM|HOSPAC|NURSING|LONG[- ]TERM CARE|SENIOR LIVING|HCA|BAYLOR SCOTT|TEXAS HEALTH CARE ASSOC|THCAPAC)\b'),
    ('Health Professionals', r'\b(PHYSICIAN|M ?D\b|MD|DOCTOR|SURGEON|SURGERY|ANESTHES|CARDIO|DENTAL|DENTIST|DENPAC|ORTHOPED|RADIOLOG|DERMATOLOG|ONCOLOG|PEDIATR|MEDICAL GROUP|NURSE|OPTOMETR|CHIROPRACT|VETERINAR|PHARMACIST)\b'),
    ('Health Services & Pharmaceuticals', r'\b(HEALTH|MEDICAL|PHARMA|PHARMAC|HEALTHCARE|IMAGING|LAB(ORATOR(Y|IES))?|BIOTECH|MCKESSON|DIAGNOSTIC|HOME HEALTH|MEDICAID|DENTAL BENEFIT)\b'),
    ('Home Builders', r'\b(HOMEBUILD|HOME BUILD|HOMES\b|PERRY HOMES|WEEKLEY|BUILDERS)\b'),
    ('Real Estate', r'\b(REAL ESTATE|REALTOR|REALTY|PROPERT(Y|IES)|DEVELOP(ER|MENT)|LAND COMPANY|TREPAC|APARTMENT|MULTIFAMILY|HOTEL|CROW HOLDINGS|COMMERCIAL REAL)\b'),
    ('Securities & Investment', r'\b(INVESTMENT|INVESTMENTS|INVESTOR|CAPITAL|PRIVATE EQUITY|HEDGE|ASSET MANAGEMENT|FUND MANAGER|SECURITIES|TRADING|VENTURE|FAMILY OFFICE|PARTNERS LP|HOLDINGS|WEALTH|SUSQUEHANNA|FINANCIAL ADVIS)\b'),
    ('Banking & Finance', r'\b(BANK|BANKER|BANKING|BANCSHARES|CREDIT UNION|LENDING|LOAN|MORTGAGE|FINANCIAL|FINANCE|CAPITAL ONE)\b'),
    ('Insurance', r'\b(INSURANCE|INSURER|UNDERWRIT|REINSUR|ANNUIT)\b'),
    ('Tech & Internet', r'\b(TECH|TECHNOLOG|SOFTWARE|COMPUTER|SEMICONDUCTOR|DATA|INTERNET|CLOUD|TESLA|SPACEX|AIRBNB|ORACLE|DELL|STARLINK|AI\b|CYBER)\b'),
    ('Telecom & Media', r'\b(TELECOM|WIRELESS|VERIZON|AT ?& ?T|CABLE|BROADCAST|MEDIA|TELEVISION|RADIO|NEWSPAPER|CLEAR CHANNEL|TIME WARNER|COMMUNICATIONS)\b'),
    ('Car Dealers', r'\b(AUTO|AUTOMOTIVE|MOTORS|DEALERSHIP|CAR DEALER|AUTO DEALER|FORD|TOYOTA|CHEVROLET|HONDA|NISSAN|LEASING)\b'),
    ('Transportation & Rail', r'\b(RAIL|RAILROAD|RAILWAY|TRUCKING|FREIGHT|LOGISTICS|AVIATION|AIRLINE|SHIPPING|MARINE TERMINAL|UPS|UPSPAC|BNSF)\b'),
    ('Construction & Contractors', r'\b(CONSTRUCTION|CONTRACTOR|CONTRACTING|ENGINEERING|PAVING|CONCRETE|STEEL|ELECTRIC CO|PLUMBING|ROOFING|BUILDING MATERIALS|AGGREGATES|CEMENT|ARCHITECT)\b'),
    ('Recreation / Live Entertainment', r'\b(SPORTS|COWBOYS|SPURS|ROCKETS|ASTROS|RANGERS|STADIUM|RACING|RACETRACK|CIRCUIT OF THE AMERICAS|ENTERTAINMENT|FITNESS|CAMP)\b'),
    ('Retail, Food & Beverage', r"\b(RETAIL|STORE|STORES|GROCER|H ?E ?B|BUC ?EE|RESTAURANT|FOOD|BEVERAGE|BEER|DISTRIBUT(ING|OR)|WINE|SPIRITS|TEQUILA|POULTRY|PILGRIM|CONVENIENCE|BLUE BELL)\b"),
    ('Ranching & Agriculture', r'\b(RANCH|RANCHER|RANCHING|RANCHES|CATTLE|FARM|FARMER|FARMING|AGRICULTUR|AGFUND|FARM BUREAU|CATTLE RAISERS|COTTON|DAIRY|TIMBER|LUMBER)\b'),
    ('Manufacturing & Industry', r'\b(MANUFACTUR|INDUSTRIES|INDUSTRIAL|CHEMICAL|METAL|RECYCLING|PLASTICS|AEROSPACE|DEFENSE)\b'),
    ('Business Services & Associations', r'\b(ASSOCIATION|CHAMBER|BUSINESS PAC|ACCOUNTING|CPA|STAFFING|MARKETING|ADVERTISING|SECURITY SERVICES|INVESTIGATION)\b'),
    ('Education & Nonprofits', r'\b(UNIVERSITY|COLLEGE|SCHOOL|ISD|TEACHER|PROFESSOR|EDUCATION|FOUNDATION|NONPROFIT|CHURCH|PASTOR|MINISTRY)\b'),
]
RX = [(ind, re.compile(rx)) for ind, rx in RULES]
BASIS_SKIP = {'Candidate & Party Committees', 'Ideological & Single-Issue Groups', 'Casinos / Gambling', 'Lobbyists & Consultants', 'Labor'}
RETIRED = re.compile(r'^(RETIRED|HOMEMAKER|HOUSEWIFE|NOT EMPLOYED|NONE|UNEMPLOYED|N A|NA|BEST EFFORTS|INFORMATION REQUESTED|REQUESTED|SELF|SELF EMPLOYED|)$')


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def load_rulings(path):
    out = {}
    if not os.path.exists(path):
        return out
    with open(path, encoding='utf-8') as f:
        for r in csv.DictReader(l for l in f if not l.startswith('#')):
            name, _, z = r['donor_key'].rpartition('|')
            if r['industry'] not in SECTOR:
                raise SystemExit(f"industry_rulings.csv: unknown industry {r['industry']!r} for {r['donor_key']}")
            out[(r['official'].strip(), norm(name), z.strip() or '*')] = (r['industry'], r['basis'].strip())
    return out


def lookup(rulings, official, names, zip5):
    for nm in names:
        n = norm(nm)
        for k in ((official, n, zip5), (official, n, '*'), ('*', n, zip5), ('*', n, '*')):
            if k in rulings:
                return rulings[k]
    return None


def classify(official, r, rulings):
    if r['tier'] == 'strict':
        return 'Oil & Gas', 'tier', 'strict oil-and-gas tier from sector_read.py'
    if r['tier'] == 'broad':
        return 'Energy, other', 'tier', 'broad energy tier from sector_read.py'
    names = [r['donor']] + [x for x in r['names'].split(' ; ') if x]
    hit = lookup(rulings, official, names, r['zip5'])
    if hit:
        return hit[0], 'hand', hit[1]
    is_person = ',' in r['donor'] and not re.search(r'\b(LLC|LP|LTD|INC|TRUST|PAC|FUND|COMPANY|CORP|PARTNERS|PC|PA|LLP|PLLC)\b', norm(r['donor']))
    filed = ' | '.join(norm(x) for x in (r['employers'], r['occupations'], '' if is_person else r['donor']))
    for ind, rx in RX:
        m = rx.search(filed)
        if m:
            return ind, 'keyword', f'filed employer/occupation/name matched {m.group(0).strip()!r}'
    basis = norm(r['hand_basis'] + ' ' + r['ent_basis'])
    for ind, rx in RX:
        if ind in BASIS_SKIP:
            continue
        m = rx.search(basis)
        if m:
            return ind, 'basis', f'oil-tier ruling basis names {m.group(0).strip()!r}'
    emps = [norm(e) for e in (r['employers'] + ' ; ' + r['occupations']).split(' ; ')]
    if is_person and all(RETIRED.match(e) for e in emps):
        return 'Retired or Homemaker (employer not given)', 'filed', 'filed employer and occupation are placeholders'
    return 'Not identified', 'none', 'no rule matched'


CAREER = [('abbott', 'abbott_career', 'Texans for Greg Abbott, June 2001 to Oct. 24, 2026'),
          ('patrick', 'patrick_career', 'Texans for Dan Patrick, 2008 to Oct. 24, 2026'),
          ('paxton_state', 'paxton_state_career', "Ken Paxton's state account (TEC 00051407), 2002 to 2024")]


def build(key, file_key, label, rulings, inputs, published=None):
    p = os.path.join(VIEWS, f'donors_{file_key}.csv'); inputs[f'donors_{file_key}'] = p
    rows = list(csv.DictReader(open(p, encoding='utf-8')))
    out = []
    for r in rows:
        ind, how, basis = classify(key, r, rulings)
        out.append(dict(official=key, donor=r['donor'], zip5=r['zip5'], total=r['total'], tier=r['tier'], industry=ind,
                        sector=SECTOR[ind], decided_by=how, industry_basis=basis, employers=r['employers'],
                        occupations=r['occupations'], oil_basis=(r['hand_basis'] or r['ent_basis'] or (f"keyword {r['kw_term']!r}" if r['kw_term'] else '')) if r['tier'] in ('strict', 'broad') else '',
                        oil_decided_by=r['decided_by'] if r['tier'] in ('strict', 'broad') else '', row_ids=r['row_ids']))
    itemized = sum(float(o['total']) for o in out)
    if published is None:
        published = itemized  # TEC itemizes every contribution for these filers
    unitem = round(published - itemized, 2)
    if unitem > 1:
        out.append(dict(official=key, donor='(unitemized and other receipts)', zip5='', total=f'{unitem:.2f}', tier='unclassified',
                        industry='Unitemized (FEC)', sector=SECTOR['Unitemized (FEC)'], decided_by='total',
                        industry_basis='published committee total minus itemized donor rows', employers='', occupations='', oil_basis='', oil_decided_by='', row_ids=''))
    with open(os.path.join(VIEWS, f'industry_{file_key}.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader()
        for o in sorted(out, key=lambda o: -float(o['total'])):
            w.writerow(o)
    return (label, published, out)


def main():
    career = '--career' in sys.argv
    rulings_path = os.path.join(HERE, 'industry_rulings.csv')
    rulings = load_rulings(rulings_path)
    summary_md = open(os.path.join(VIEWS, 'summary.md'), encoding='utf-8').read()
    inputs = {'rulings': rulings_path, 'tool': os.path.abspath(__file__), 'summary': os.path.join(VIEWS, 'summary.md')}
    fed = {}
    for key, label in OFFICIALS:
        m = re.search(rf'^\| {key} \| [^|]*\| \$([\d,\.]+) ', summary_md, re.M)
        if career and key not in PAXTON:
            continue
        fed[key] = build(key, key, label, rulings, inputs, float(m.group(1).replace(',', '')))
    if not career:
        groups = [(k, *fed[k]) for k, _ in OFFICIALS]
        pax_out = [o for k in PAXTON for o in fed[k][2]]
        groups.append(('paxton_combined', 'Paxton, three committees (not netted for the $21,257 Paxton Victory transferred to the campaign)', sum(fed[k][1] for k in PAXTON), pax_out))
        write_md(groups, inputs, '2025-26', 'industries_2025-26.md')
        return
    res = {k: build(k, fk, label, rulings, inputs) for k, fk, label in CAREER}
    groups = [(k, *res[k]) for k, _, _ in CAREER]
    pax_out = res['paxton_state'][2] + [o for k in PAXTON for o in fed[k][2]]
    pax_pub = res['paxton_state'][1] + sum(fed[k][1] for k in PAXTON)
    groups.append(('paxton_career', 'Paxton career: state account 2002-2024 plus his three federal committees 2025-26, including the super PAC (not netted for the $21,257 transfer)', pax_pub, pax_out))
    pax_out2 = res['paxton_state'][2] + [o for k in ('paxton_senate', 'paxton_victory') for o in fed[k][2]]
    pax_pub2 = res['paxton_state'][1] + sum(fed[k][1] for k in ('paxton_senate', 'paxton_victory'))
    groups.append(('paxton_career_own', 'Paxton career without the super PAC: state account 2002-2024 plus Ken Paxton for Senate and Paxton Victory 2025-26', pax_pub2, pax_out2))
    write_md(groups, inputs, 'whole careers', 'industries_career.md')


NARROW_OUT = re.compile(r'midstream|pipeline|petrochem|chemical|lyondell|distribut|hauling|terminal|energy transfer|kinder|nustar|enterprise products|duncan', re.I)
NARROW_KEEP = re.compile(r'FOSTER, PAUL|BAGGETT')


def narrow_oil(out):
    total = sum(float(o['total']) for o in out if o['industry'] == 'Oil & Gas')
    moved = sum(float(o['total']) for o in out if o['industry'] == 'Oil & Gas'
                and NARROW_OUT.search(' '.join((o['oil_basis'], o['employers'], o['donor']))) and not NARROW_KEEP.search(o['donor']))
    return total, moved


def rank(out, published):
    by = defaultdict(float); n = defaultdict(int); top = defaultdict(list)
    for o in out:
        t = float(o['total']); by[o['industry']] += t; n[o['industry']] += 1; top[o['industry']].append((t, o['donor']))
    return by, n, top


def write_md(groups, inputs, window, outname):
    money = lambda x: f'${x:,.0f}'
    L = [f'# Donor industries, {window}', '',
         'Written by `tools/industry_rank.py` from the donor views that `tools/sector_read.py` writes. The oil-and-gas column is the',
         'final 2025-26 strict tier, unchanged. Every other donor carries one OpenSecrets-style industry, decided by a hand ruling',
         '(`tools/industry_rulings.csv`), a keyword over the filed employer, occupation or name, or a keyword over the stated',
         'basis of an oil-tier ruling. Each donor row in `views/industry_<official>.csv` names how it was decided and its raw row ids.', '',
         '## Inputs (sha256)', '', '| Input | Path | sha256 |', '|---|---|---|']
    for k, p in inputs.items():
        L.append(f'| {k} | `{p}` | `{sha(p)}` |')
    L += ['', '## Industry ranking by official', '']
    tag = 'career' if window != '2025-26' else '2025-26'
    rank_rows, narrow_rows = [], []
    for key, label, published, out in groups:
        by, n, top = rank(out, published)
        ranked_all = sorted(((k, v) for k, v in by.items() if SECTOR[k] != 'Not identified'), key=lambda x: -x[1])
        for i, (k, v) in enumerate(ranked_all, 1):
            rank_rows.append(dict(window=tag, group=key, group_label=label, group_total=f'{published:.2f}', rank=i, industry=k, sector=SECTOR[k],
                                  dollars=f'{v:.2f}', share=f'{v / published:.6f}', donors=n[k],
                                  largest_donors='; '.join(f'{d} ({t:.0f})' for t, d in sorted(top[k], reverse=True)[:3])))
        for k in ('Unitemized (FEC)', 'Retired or Homemaker (employer not given)', 'Not identified'):
            if by.get(k):
                rank_rows.append(dict(window=tag, group=key, group_label=label, group_total=f'{published:.2f}', rank='', industry=k, sector=SECTOR[k],
                                      dollars=f'{by[k]:.2f}', share=f'{by[k] / published:.6f}', donors=n[k], largest_donors=''))
        oil, moved = narrow_oil(out)
        nxt = next(((k, v) for k, v in ranked_all if k != 'Oil & Gas'), ('', 0))
        narrow_rows.append(dict(window=tag, group=key, group_total=f'{published:.2f}', oil_dollars=f'{oil:.2f}', moved_out_dollars=f'{moved:.2f}',
                                narrow_oil_dollars=f'{oil - moved:.2f}', narrow_share=f'{(oil - moved) / published:.6f}',
                                next_industry=nxt[0], next_dollars=f'{nxt[1]:.2f}', narrow_still_first='yes' if oil - moved > nxt[1] else 'no',
                                rule='pipelines, petrochemicals and fuel distribution moved out by keyword over the oil ruling basis, employer and name; refiner Paul Foster and energy consultancy Opportune (David Baggett) kept in'))
        ident = sum(v for k, v in by.items() if SECTOR[k] != 'Not identified')
        L += [f'### {key}: {label}', '', f'Total {money(published)}. Industry identified for {ident / published * 100:.1f}% of dollars.', '',
              '| Rank | Industry | Sector | Dollars | Share of total | Donors | Largest donors |', '|---|---|---|---|---|---|---|']
        ranked = sorted(((k, v) for k, v in by.items() if SECTOR[k] != 'Not identified'), key=lambda x: -x[1])
        for i, (k, v) in enumerate(ranked, 1):
            tops = '; '.join(f'{d[:34]} {money(t)}' for t, d in sorted(top[k], reverse=True)[:3])
            mark = '**' if k == 'Oil & Gas' else ''
            L.append(f'| {i} | {mark}{k}{mark} | {SECTOR[k]} | {money(v)} | {v / published * 100:.1f}% | {n[k]} | {tops} |')
        for k in ('Unitemized (FEC)', 'Retired or Homemaker (employer not given)', 'Not identified'):
            if by.get(k):
                L.append(f'| - | {k} | Not identified | {money(by[k])} | {by[k] / published * 100:.1f}% | {n[k]} | |')
        secs = defaultdict(float)
        for k, v in by.items():
            secs[SECTOR[k]] += v
        L += ['', 'By sector: ' + '; '.join(f'{s} {v / published * 100:.1f}%' for s, v in sorted(secs.items(), key=lambda x: -x[1])), '']
    L += ['## Caveats', '',
          '- The industry of a donor is the industry of the money\'s source as best stated: a family office or trust takes the industry of the fortune behind it when a hand ruling says so; otherwise its filed employer.',
          '- Keyword calls (`decided_by` keyword or basis) were not hand-checked donor by donor. Hand rulings cite their basis.',
          '- Committees that pass money through (PACs, joint committees, other candidates) are ranked as their own kind, not traced to their donors, except where a hand ruling names the funder.',
          '- Oil & Gas here is the final strict tier. "Energy, other" is the broad tier minus strict: utilities, power and diversified energy fortunes.',
          '- Labels checked on 2026-10-30 against OpenSecrets\' Industries by Sector page (https://www.opensecrets.org/industries/slist), saved as `raw/opensecrets_industries_by_sector_2026-10-30.txt`. Our sectors are theirs; candidate committees sit in Ideological/Single-Issue as OpenSecrets files them. Where one of our industries spans several of theirs, the table below says which.',
          '- Our Oil & Gas is broader than OpenSecrets\' Oil & Gas industry: it adds natural-gas pipelines (a separate OpenSecrets industry) and, by Saul\'s 2026-10-29 ruling, petrochemical makers and fuel distribution. Narrowed to OpenSecrets\' definition, Abbott\'s oil share falls from 16.8% to roughly 11.5-12.7% (midstream donors Kelcy Warren, Jan Duncan, Nancy Kinder), still above Securities & Investment at 9.5%. Patrick falls to roughly 14.3%, still first. The range reflects donors whose OpenSecrets code was not checked one by one.',
          '', '| Our industry | OpenSecrets industries it spans |', '|---|---|'] + [f'| {k} | {v} |' for k, v in OS_MAP.items()]
    if window != '2025-26':
        L = [l for l in L if not l.startswith("- Our Oil & Gas is broader")] + ['', '- Our Oil & Gas is broader than OpenSecrets\' Oil & Gas industry (pipelines, and by Saul\'s ruling petrochemicals and fuel distribution). The narrow-definition share was estimated for 2025-26 only (see `industries_2025-26.md`).',
              '- Career oil tiers come from `hand_rulings.csv` plus `hand_rulings_career.csv` as applied in the career donor views; career coverage is lower for older years.']
    open(os.path.join(VIEWS, outname), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    for name, rows_ in ((f'industry_ranking_{tag}.csv', rank_rows), (f'oil_definition_check_{tag}.csv', narrow_rows)):
        with open(os.path.join(VIEWS, name), 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=list(rows_[0].keys())); w.writeheader(); w.writerows(rows_)
    print(f'wrote views/{outname}')


if __name__ == '__main__':
    main()
