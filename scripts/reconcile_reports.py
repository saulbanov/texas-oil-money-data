"""Report-by-report check of our contribution rows against each report's own filed totals, for a fact-checker.

TEC: for every campaign finance report filed under the three filer ids (cover.csv in the 2026-10-29 bulk export),
the report's own totalContribAmount minus its unitemizedContribAmount against the sum of the itemized rows in our slice
for that report id (A1 cash + A2 in-kind + other schedules; the filed total includes in-kind gifts). Superseded reports (infoOnlyFlag=Y) are listed and
marked; their rows are not in the shares.
FEC: per filing, the itemized individual contributions on Schedule A line 11(a)(i) against the filing's own summary
line, as sector_read.fec_load computes it.

Reads raw slices and the extracted cover.csv on Elements; writes views/report_check_tec.csv and views/report_check_fec.csv.
python3 -I reconcile_reports.py
"""
import csv, os, sys
from collections import defaultdict
from decimal import Decimal as D

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import sector_read as sr

ELEM = '/Volumes/Elements/reference-data/tec-cf-bulk/2026-10-29'
SLICES = {'00051153': (f'{ELEM}/slices/tec_abbott.csv', 'Texans for Greg Abbott'),
          '00064090': (os.path.join(ROOT, 'raw', 'tec_patrick.csv'), 'Texans for Dan Patrick'),
          '00051407': (f'{ELEM}/slices/tec_paxton.csv', 'Ken Paxton (candidate/officeholder account)')}
csv.field_size_limit(10 ** 9)


def tec():
    sums = defaultdict(lambda: defaultdict(D)); counts = defaultdict(int)
    for fid, (path, _) in SLICES.items():
        with open(path, newline='', encoding='utf-8') as f:
            for r in csv.DictReader(f):
                if r['filerIdent'] != fid:
                    continue
                key = (fid, r['reportInfoIdent'])
                kind = r['schedFormTypeCd'] if r['schedFormTypeCd'] in ('A1', 'A2') else 'other'
                sums[key][kind] += D(r['contributionAmount'] or '0'); counts[key] += 1
                sums[key]['_info'] = D(1) if r['infoOnlyFlag'] == 'Y' else sums[key]['_info']
    out = []
    with open(f'{ELEM}/extracted/cover.csv', newline='', encoding='utf-8') as f:
        for c in csv.DictReader(f):
            fid = c['filerIdent']
            if fid not in SLICES:
                continue
            key = (fid, c['reportInfoIdent']); s = sums.get(key, {})
            total = D(c['totalContribAmount'] or '0'); unit = D(c['unitemizedContribAmount'] or '0')
            a1, a2, oth = s.get('A1', D(0)), s.get('A2', D(0)), s.get('other', D(0))
            out.append(dict(filer_id=fid, committee=SLICES[fid][1], report_id=c['reportInfoIdent'], form=c['formTypeCd'],
                            period_start=c['periodStartDt'], period_end=c['periodEndDt'], received=c['receivedDt'],
                            superseded='yes' if c['infoOnlyFlag'] == 'Y' else '',
                            filed_total_contributions=f'{total:.2f}', filed_unitemized=f'{unit:.2f}',
                            our_itemized_cash_A1=f'{a1:.2f}', our_inkind_A2=f'{a2:.2f}', our_other_schedules=f'{oth:.2f}',
                            our_rows=counts.get(key, 0),
                            difference=f'{total - unit - a1 - a2 - oth:.2f}',
                            match='yes' if abs(total - unit - a1 - a2 - oth) < D('0.01') else ('no rows in slice' if not counts.get(key) else 'NO')))
    out.sort(key=lambda r: (r['filer_id'], r['period_end'], r['report_id']))
    return out


def fec():
    out = []
    for cid, label in (('C00901918', 'Ken Paxton for Senate'), ('C00952218', 'Paxton Victory'), ('C00901223', 'Lone Star Liberty PAC')):
        path = '/Volumes/Elements/reference-data/fec-efiling/2026-10-29/fec_C00901918.jsonl' if cid == 'C00901918' else os.path.join(ROOT, 'raw', f'fec_{cid}.jsonl')
        _, checks, superseded, _ = sr.fec_load(path, cid)
        for fn, ours, line, ok in checks:
            out.append(dict(committee_id=cid, committee=label, filing_id=fn, our_itemized_individual_11ai=f'{D(ours):.2f}',
                            filed_line_11ai=f'{D(line):.2f}', match='yes' if ok else 'NO'))
        for fn in sorted(superseded):
            out.append(dict(committee_id=cid, committee=label, filing_id=fn, our_itemized_individual_11ai='',
                            filed_line_11ai='', match='superseded by a later amendment; not counted'))
    return out


for name, rows in (('report_check_tec.csv', tec()), ('report_check_fec.csv', fec())):
    with open(os.path.join(ROOT, 'views', name), 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print(name, len(rows))
