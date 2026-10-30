"""Build the fact-check package for texas-oil-money-data from this repo. Consumer only: it copies views, rulings and
scripts, and selects the filed contribution rows behind every oil-and-gas call. It reclassifies nothing.

Usage: python3 -I factcheck_export.py <target_dir>
Writes into <target_dir>: README.md, MANIFEST.json, contributions/, donors/, checks/, rulings/, summaries/, scripts/,
spot_check.csv. Raw TEC slices stay out (229 MB for Abbott); README tells a checker how to rebuild them.
"""
import csv, hashlib, json, os, random, shutil, subprocess, sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
V = os.path.join(ROOT, 'views'); RAW = os.path.join(ROOT, 'raw')
sys.path.insert(0, HERE)
import sector_read as sr
from public_text import clean

ELEM = '/Volumes/Elements/reference-data/tec-cf-bulk/2026-10-29'
TEC = {'00051153': (f'{ELEM}/slices/tec_abbott.csv', 'abbott_career'),
       '00064090': (os.path.join(RAW, 'tec_patrick.csv'), 'patrick_career'),
       '00051407': (f'{ELEM}/slices/tec_paxton.csv', 'paxton_state_career')}
FEC = {'C00901918': ('/Volumes/Elements/reference-data/fec-efiling/2026-10-29/fec_C00901918.jsonl', 'paxton_senate'),
       'C00952218': (os.path.join(RAW, 'fec_C00952218.jsonl'), 'paxton_victory'),
       'C00901223': (os.path.join(RAW, 'fec_C00901223.jsonl'), 'lone_star_liberty')}
DONOR_VIEWS = ['abbott_career', 'patrick_career', 'paxton_state_career', 'abbott', 'patrick', 'paxton_senate', 'paxton_victory', 'lone_star_liberty']
CHECKS = ['report_check_tec.csv', 'report_check_fec.csv', 'sensitivity.csv', 'oil_definition_check_career.csv',
          'oil_definition_check_2025-26.csv', 'industry_ranking_career.csv', 'industry_ranking_2025-26.csv']
SUMMARIES = ['summary.md', 'summary_career.md', 'industries_2025-26.md', 'industries_career.md', 'stage-b-reproduction.md']
SCRIPTS = ['slice_tec.py', 'fec_to_jsonl.py', 'sector_read.py', 'industry_rank.py', 'reconcile_reports.py', 'sensitivity.py',
           'public_text.py', 'factcheck_export.py']
csv.field_size_limit(10 ** 9)
target = os.path.abspath(sys.argv[1])
TIER = {'strict': 'oil and gas', 'broad': 'other energy (utilities, power, diversified energy fortunes)'}
HOW = {'hand': 'reporter review', 'entity': 'known company, executive or family', 'keyword': 'filed employer or occupation'}


def sub(*p):
    d = os.path.join(target, *p); os.makedirs(d, exist_ok=True); return d


def classified(view):
    """row id -> classification of its donor, for every oil-and-gas or other-energy donor in a donor view."""
    m = {}
    for r in csv.DictReader(open(os.path.join(V, f'donors_{view}.csv'), encoding='utf-8')):
        if r['tier'] not in TIER:
            continue
        info = dict(donor=r['donor'], tier=TIER[r['tier']], decided_by=HOW.get(r['decided_by'], r['decided_by']),
                    why=clean(r['hand_basis'] or r['ent_basis'] or (f"keyword '{r['kw_term']}'" if r['kw_term'] else '')),
                    judgment_call='yes' if r['hand_flag'] == 'Y' else '')
        for rid in r['row_ids'].split():
            m[rid] = info
    return m


def contributions():
    out = []
    for fid, (path, view) in TEC.items():
        cls = classified(view)
        with open(path, newline='', encoding='utf-8') as f:
            for r in csv.DictReader(f):
                c = cls.get(r['contributionInfoId'])
                if not c or r['filerIdent'] != fid or r['infoOnlyFlag'] == 'Y':
                    continue
                out.append(dict(source='TEC', filer_or_committee=fid, report_or_filing=r['reportInfoIdent'], contribution_id=r['contributionInfoId'],
                                date=r['contributionDt'], amount=r['contributionAmount'], schedule=r['schedFormTypeCd'],
                                name_as_filed=r['contributorNameOrganization'] or f"{r['contributorNameLast']}, {r['contributorNameFirst']}",
                                city=r['contributorStreetCity'], state=r['contributorStreetStateCd'], zip=r['contributorStreetPostalCode'][:5],
                                employer_as_filed=r['contributorEmployer'], occupation_as_filed=r['contributorOccupation'],
                                in_2025_26='yes' if '20250101' <= r['contributionDt'] <= '20261024' else '', note='', **c))
    for cid, (path, view) in FEC.items():
        cls = classified(view)
        rows, _, _, _ = sr.fec_load(path, cid)
        for r in rows:
            c = cls.get(r['row_id'])
            if not c:
                continue
            out.append(dict(source='FEC', filer_or_committee=cid, report_or_filing='', contribution_id=r['row_id'],
                            date=r['date'], amount=f"{r['amt']}", schedule=r.get('kind', ''), name_as_filed=r['name'],
                            city=r.get('city', ''), state='', zip=r.get('zip5', ''), employer_as_filed=r.get('employer', ''),
                            occupation_as_filed=r.get('occupation', ''), in_2025_26='yes', note=r.get('via', ''), **c))
    return out


def write_csv(path, rows):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)


def money(x):
    x = float(x)
    return f'${x / 1e6:.1f} million' if x >= 1e6 else f'${x:,.0f}'


def readme():
    """README text with every figure read from the views at build time."""
    F = {r['key']: r for r in csv.DictReader(open(os.path.join(ROOT, 'public', 'findings.csv'), encoding='utf-8'))}
    S = {(r['window'], r['group']): r for r in csv.DictReader(open(os.path.join(V, 'sensitivity.csv'), encoding='utf-8'))}
    tec = list(csv.DictReader(open(os.path.join(V, 'report_check_tec.csv'), encoding='utf-8')))
    fec = list(csv.DictReader(open(os.path.join(V, 'report_check_fec.csv'), encoding='utf-8')))
    live = [r for r in tec if not r['superseded']]
    ok = {fid: (sum(r['match'] == 'yes' for r in live if r['filer_id'] == fid), sum(1 for r in live if r['filer_id'] == fid)) for fid in TEC}
    norows = [r for r in live if r['match'] == 'no rows in slice']
    gap = sum(float(r['filed_total_contributions']) - float(r['filed_unitemized']) for r in norows)
    fec_ok = sum(r['match'] == 'yes' for r in fec); fec_live = sum(r['match'] in ('yes', 'NO') for r in fec)
    pct = lambda x: f'{float(x):.1%}'

    def table(win):
        L = ['| Who | Period | Raised | From oil and gas | Share | Next industry | Share with judgment calls dropped |', '|---|---|---|---|---|---|---|']
        for k, r in F.items():
            if r['window'] != win:
                continue
            s = S.get((win, k.split(':')[1]))
            L.append(f"| {r['who']} | {r['period']} | {money(r['raised'])} | {money(r['oil_gas'])} | {pct(r['oil_share'])} | "
                     f"{r['next_industry']}, {money(r['next_dollars'])} | {pct(s['share_without_flagged']) if s else ''} |")
        return '\n'.join(L)

    return f"""# Texas oil money: the data

This repository holds the data behind Saul Elbein's count of the oil and gas money given to Gov. Greg Abbott, Lt. Gov. Dan Patrick and Attorney General Ken Paxton. It is built from their campaign filings with the Texas Ethics Commission and, for Paxton's 2026 U.S. Senate run, the Federal Election Commission. Every dollar in every figure below can be traced to a filed contribution in `contributions/oil_and_energy_contributions.csv`, and every contribution can be looked up on the commission's site by its report id and contribution id.

## The findings

Whole careers:

{table('career')}

This election cycle:

{table('2025-26')}

"Next industry" is the largest industry other than oil and gas. Industries follow OpenSecrets' categories. Money from donors with no employer listed, and small unitemized federal gifts, has no industry but counts in each total.

## How to check a figure

1. **Sum the contributions.** In `contributions/oil_and_energy_contributions.csv`, keep the rows whose `tier` is `oil and gas` and whose `filer_or_committee` is the committee you are checking (Abbott `00051153`, Patrick `00064090`, Paxton's state account `00051407`, Paxton's federal committees `C00901918`, `C00952218`, `C00901223`). For this election cycle, also keep `in_2025_26 = yes`. The amounts add up to the oil and gas figures above.
2. **Look up any contribution.** For a state row, search the filer id at https://www.ethics.state.tx.us/search/cf/, open the report named in `report_or_filing` and find the `contribution_id`. For a federal row, the committee's filings are on fec.gov and `contribution_id` is the schedule line and transaction id.
3. **See why a donor counts.** Each row carries `why`, `decided_by` and `judgment_call`. Every ruling, with its written basis, is in `rulings/`.
4. **Check the totals.** `checks/report_check_tec.csv` sets each report's own filed contribution total, minus its unitemized money, against the sum of the rows used here. The rows match {ok['00051153'][0]} of {ok['00051153'][1]} of Abbott's reports, {ok['00064090'][0]} of {ok['00064090'][1]} of Patrick's and {ok['00051407'][0]} of {ok['00051407'][1]} of Paxton's, to the cent. `checks/report_check_fec.csv` does the same for each federal filing: {fec_ok} of {fec_live} match their own summary line.
5. **Start with a sample.** `spot_check.csv` lists 25 oil and gas contributions drawn at random, with the report id for each.

## What counts as oil and gas

Producers, oilfield service companies, royalty and mineral owners, refiners, pipelines, petrochemical makers, fuel wholesalers and haulers, their trade groups and political committees, and the families and investment vehicles that hold oil fortunes. Retail convenience stores are not counted. Utilities, power generators and diversified fortunes with an oil arm are kept apart as "other energy" and are not in the oil and gas figures.

OpenSecrets' own oil and gas industry is narrower: it leaves out pipelines, petrochemical makers and fuel distributors. `checks/oil_definition_check_career.csv` and `checks/oil_definition_check_2025-26.csv` recount every figure on that definition. Oil and gas stays the largest industry for Abbott, Patrick and Paxton's own committees.

## How much rests on judgment calls

Some donors were counted as oil and gas because of a family tie or a company's line of business that a reader could weigh differently. They carry `judgment_call = yes`. The last column of each table above drops all of them. `checks/sensitivity.csv` has the dollars behind each.

## Files

| Path | What it holds |
|---|---|
| `contributions/oil_and_energy_contributions.csv` | every filed contribution from an oil and gas or other-energy donor, with the classification |
| `donors/donors_<who>.csv` | every donor to each committee, with all three classification passes kept separate (`kw_*` keyword, `ent_*` known entity, `hand_*` review), the final `tier` and the contribution ids |
| `donors/industry_<who>.csv` | the same donors with an OpenSecrets-style industry |
| `checks/` | report-by-report totals, the narrower-definition test, the sensitivity table, industry rankings, filer ids, FEC totals and the OpenSecrets category list as read on 2026-10-30 |
| `rulings/` | every reviewed donor, with the written basis |
| `summaries/` | the full summary tables as the analysis wrote them |
| `scripts/` | the code that built every file here |
| `MANIFEST.json` | the size and sha256 of every file, and the source commit |

Files ending `_career` cover whole careers; the others cover Jan. 1, 2025 through Oct. 24, 2026, or for the federal committees the 2026 cycle. The two largest tables are gzipped.

## Rebuilding from the public filings

1. Download the commission's bulk export, https://prd.tecprd.ethicsefile.com/public/cf/public/TEC_CF_CSV.zip. The copy used here was downloaded 2026-10-29; its sha256 is in `MANIFEST.json`. The commission regenerates the file, so a later copy carries later reports. Match by contribution id and report id.
2. `scripts/slice_tec.py` pulls the rows for a filer id out of the unzipped export without changing them.
3. `scripts/fec_to_jsonl.py` reads the federal `.fec` filings listed in `checks/report_check_fec.csv`.
4. `scripts/sector_read.py` classifies donors, `scripts/industry_rank.py` assigns industries, `scripts/reconcile_reports.py` checks totals, and `scripts/sensitivity.py` writes the judgment-call table. Each script's header names its inputs. The scripts were written for the analysis repository's folder layout, so paths may need adjusting.

## Using this data

Federal law bars using the names and addresses of individual contributors taken from FEC reports to solicit contributions or for any commercial purpose (52 U.S.C. 30111(a)(4); 11 CFR 104.15). Use this data for reporting, research and checking, not for fundraising or marketing. These files carry no street addresses or phone numbers.

Federal committees may "salt" their reports with up to ten fictitious contributor names to detect misuse, so a federal row here could be a decoy the committee planted.

The data and text in this repository are licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY-NC-SA 4.0), the same terms OpenSecrets uses for its data. Credit "Saul Elbein, Future Heist." The scripts in `scripts/` are under the MIT License. See `LICENSE`.

## Known limits

- Five of Paxton's 2001-2002 state reports, together {money(gap)} in itemized gifts, have no contribution rows in the commission's export, so his state total is short by that much.
- His two 2010 reports as a candidate for House speaker file no contribution total to check against.
- Abbott's judicial campaigns of the 1990s and his separate officeholder account are not included.
- Transfers between a man's own committees are not counted twice.
- Industries other than oil and gas were assigned from filed employers and, for the largest donors, by review. Committees that pass money along are counted as committees, not traced to their own donors.

Analysis by Saul Elbein.
"""


def main():
    rows = contributions()
    open(os.path.join(target, 'README.md'), 'w', encoding='utf-8').write(readme())
    shutil.copyfile(os.path.join(ROOT, 'public', 'LICENSE'), os.path.join(target, 'LICENSE'))
    write_csv(os.path.join(sub('contributions'), 'oil_and_energy_contributions.csv'), rows)
    import gzip
    for v in DONOR_VIEWS:
        for kind in ('donors', 'industry'):
            src = os.path.join(V, f'{kind}_{v}.csv'); dst = os.path.join(sub('donors'), f'{kind}_{v}.csv')
            for old in (dst, dst + '.gz'):
                if os.path.exists(old):
                    os.remove(old)
            if os.path.getsize(src) > 40_000_000:  # GitHub warns at 50 MB; ship large tables gzipped
                with open(src, 'rb') as fi, gzip.GzipFile(dst + '.gz', 'wb', mtime=0) as fo:
                    shutil.copyfileobj(fi, fo)
            else:
                shutil.copyfile(src, dst)
    for c in CHECKS:
        shutil.copyfile(os.path.join(V, c), os.path.join(sub('checks'), c))
    for s in SUMMARIES:
        shutil.copyfile(os.path.join(V, s), os.path.join(sub('summaries'), s))
    for r in ('hand_rulings.csv', 'hand_rulings_career.csv', 'industry_rulings.csv'):
        shutil.copyfile(os.path.join(HERE, r), os.path.join(sub('rulings'), r))
    for s in SCRIPTS:
        shutil.copyfile(os.path.join(HERE, s), os.path.join(sub('scripts'), s))
    shutil.copyfile(os.path.join(RAW, 'filer_ids.md'), os.path.join(sub('checks'), 'filer_ids.md'))
    shutil.copyfile(os.path.join(RAW, 'fec_totals.json'), os.path.join(sub('checks'), 'fec_totals.json'))
    shutil.copyfile(os.path.join(RAW, 'opensecrets_industries_by_sector_2026-10-30.txt'), os.path.join(sub('checks'), 'opensecrets_industries_by_sector_2026-10-30.txt'))
    # spot check: 25 oil-and-gas contributions drawn at random (seed fixed so the draw can be repeated)
    oil = [r for r in rows if r['tier'] == 'oil and gas' and r['source'] == 'TEC']
    rnd = random.Random(20261030)
    pick = sorted(rnd.sample(oil, 25), key=lambda r: (r['filer_or_committee'], r['date']))
    write_csv(os.path.join(target, 'spot_check.csv'), [dict(filer=r['filer_or_committee'], report_id=r['report_or_filing'], contribution_id=r['contribution_id'],
              date=r['date'], amount=r['amount'], name_as_filed=r['name_as_filed'], employer_as_filed=r['employer_as_filed'], why=r['why'],
              look_up='https://www.ethics.state.tx.us/search/cf/ (search by filer id, open the report id)') for r in pick])
    head = subprocess.run(['git', '-C', ROOT, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
    dirty = bool(subprocess.run(['git', '-C', ROOT, 'status', '--porcelain'], capture_output=True, text=True).stdout.strip())
    files = {}
    for dp, _, fns in os.walk(target):
        if '.git' in dp:
            continue
        for fn in fns:
            p = os.path.join(dp, fn); rel = os.path.relpath(p, target)
            if rel in ('MANIFEST.json',):
                continue
            files[rel] = {'bytes': os.path.getsize(p), 'sha256': hashlib.sha256(open(p, 'rb').read()).hexdigest()}
    json.dump({'built': date.today().isoformat(), 'built_by': 'scripts/factcheck_export.py', 'source_repo': 'saulbanov/tx-campaign-money (private)',
               'source_commit': head, 'source_had_uncommitted_changes': dirty,
               'tec_bulk_export': {'url': 'https://prd.tecprd.ethicsefile.com/public/cf/public/TEC_CF_CSV.zip', 'downloaded': '2026-10-29',
                                   'zip_sha256': json.load(open(os.path.join(RAW, 'receipts.json')))['tec']['bulk_source']['zip_sha256']},
               'files': dict(sorted(files.items()))}, open(os.path.join(target, 'MANIFEST.json'), 'w'), indent=1)
    print('contribution rows', len(rows), '| oil and gas', sum(r['tier'] == 'oil and gas' for r in rows), '| files', len(files))


main()
