"""Stage A slicer: copy every contribution row for the given filer ids out of the TEC
bulk contribs_*.csv files, unchanged (same header, same field bytes via csv round-trip).
Acquisition only: no filtering beyond filerIdent membership.

usage: python3 -I slice_tec.py <extracted_dir> <out_dir> <label>=<id,id,...> [...]
writes <out_dir>/tec_<label>.csv and <out_dir>/receipts_tec.json
"""
import csv, glob, hashlib, json, os, sys
from decimal import Decimal

csv.field_size_limit(10**9)

def main():
    src, out = sys.argv[1], sys.argv[2]
    groups = {}
    for a in sys.argv[3:]:
        label, ids = a.split('=')
        groups[label] = set(ids.split(','))
    id2label = {i: l for l, s in groups.items() for i in s}
    files = sorted(glob.glob(os.path.join(src, 'contribs_*.csv')))
    writers, handles, header = {}, {}, None
    stats = {}  # label -> id -> file -> {rows, amount}
    for path in files:
        with open(path, newline='', encoding='utf-8', errors='strict') as f:
            r = csv.reader(f)
            h = next(r)
            if header is None:
                header = h
                for l in groups:
                    fh = open(os.path.join(out, f'tec_{l}.csv'), 'w', newline='', encoding='utf-8')
                    handles[l] = fh
                    writers[l] = csv.writer(fh, quoting=csv.QUOTE_MINIMAL)
                    writers[l].writerow(h)
            assert h == header, f'header mismatch in {path}'
            fi = h.index('filerIdent'); ai = h.index('contributionAmount')
            for row in r:
                fid = row[fi]
                l = id2label.get(fid)
                if l is None:
                    continue
                writers[l].writerow(row)
                s = stats.setdefault(l, {}).setdefault(fid, {}).setdefault(os.path.basename(path), {'rows': 0, 'amount': Decimal('0')})
                s['rows'] += 1
                s['amount'] += Decimal(row[ai] or '0')
    for fh in handles.values():
        fh.close()
    receipts = {'tool': 'money/tools/slice_tec.py', 'source_dir': src, 'source_files': [os.path.basename(p) for p in files], 'filer_groups': {l: sorted(s) for l, s in groups.items()}, 'outputs': {}}
    for l in groups:
        p = os.path.join(out, f'tec_{l}.csv')
        hsh = hashlib.sha256(open(p, 'rb').read()).hexdigest()
        per = {}
        for fid, byf in stats.get(l, {}).items():
            per[fid] = {'rows': sum(v['rows'] for v in byf.values()), 'amount_all_rows': str(sum(v['amount'] for v in byf.values())), 'by_source_file': {k: {'rows': v['rows'], 'amount': str(v['amount'])} for k, v in sorted(byf.items())}}
        receipts['outputs'][l] = {'path': p, 'bytes': os.path.getsize(p), 'sha256': hsh, 'data_rows': sum(v['rows'] for v in per.values()), 'per_filer_id': per,
                                  'note': 'amount_all_rows sums every row as filed, including superseded (infoOnlyFlag=Y) rows, all schedules and all years.'}
    json.dump(receipts, open(os.path.join(out, 'receipts_tec.json'), 'w'), indent=2)
    print(json.dumps({l: {'rows': v['data_rows'], 'bytes': v['bytes']} for l, v in receipts['outputs'].items()}))

main()
