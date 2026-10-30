"""Stage A: convert raw FEC electronic filings (.fec, format 8.x, FS=0x1c) into one jsonl
per committee. Acquisition only. Every line of every file becomes one row, unchanged (lines split on newline only;
str.splitlines() would also split on the 0x1c field separator):
`raw` is the line as filed; `fields` is the same line split on FS with surrounding quotes
stripped; `named` maps FEC 8.5 Schedule A positions to names for SA* records only.
Nothing is deduped, netted or dropped (WinRed earmarks, memo rows, refunds stay as filed).

usage: python3 -I fec_to_jsonl.py <committee_id> <out.jsonl> <receipts.json> <file.fec> [...]
"""
import hashlib, json, os, sys
from decimal import Decimal

SA_NAMES = ['form_type','filer_committee_id','transaction_id','back_reference_tran_id','back_reference_sched_name',
 'entity_type','contributor_organization_name','contributor_last_name','contributor_first_name','contributor_middle_name',
 'contributor_prefix','contributor_suffix','contributor_street_1','contributor_street_2','contributor_city','contributor_state',
 'contributor_zip','election_code','election_other_description','contribution_date','contribution_amount','contribution_aggregate',
 'contribution_purpose_descrip','contributor_employer','contributor_occupation','donor_committee_fec_id','donor_committee_name',
 'donor_candidate_fec_id','donor_candidate_last_name','donor_candidate_first_name','donor_candidate_middle_name','donor_candidate_prefix',
 'donor_candidate_suffix','donor_candidate_office','donor_candidate_state','donor_candidate_district','conduit_name','conduit_street1',
 'conduit_street2','conduit_city','conduit_state','conduit_zip','memo_code','memo_text_description','reference_code']

def unq(s):
    return s[1:-1] if len(s) >= 2 and s[0] == '"' and s[-1] == '"' else s

def main():
    cid, out, rec = sys.argv[1], sys.argv[2], sys.argv[3]
    files = sys.argv[4:]
    receipts = {'tool': 'money/tools/fec_to_jsonl.py', 'committee_id': cid, 'source': 'https://docquery.fec.gov/dcdev/posted/<file_number>.fec', 'files': [], 'output': out}
    n_total = 0
    with open(out, 'w', encoding='utf-8') as o:
        for p in files:
            b = open(p, 'rb').read()
            fn = os.path.basename(p).split('.')[0]
            counts, sa_sum, sa_sum_nonmemo, hdr = {}, Decimal('0'), Decimal('0'), None
            for ln, line in enumerate(b.decode('latin-1').replace('\r\n', '\n').rstrip('\n').split('\n'), 1):
                f = [unq(x) for x in line.split('\x1c')]
                rt = f[0]
                counts[rt] = counts.get(rt, 0) + 1
                row = {'committee_id': cid, 'file_number': fn, 'line_no': ln, 'record_type': rt, 'raw': line, 'fields': f}
                if rt.startswith('SA'):
                    row['named'] = dict(zip(SA_NAMES, f))
                    amt = Decimal(f[20] or '0')
                    sa_sum += amt
                    if (f[42] if len(f) > 42 else '') != 'X':
                        sa_sum_nonmemo += amt
                elif rt.startswith('F3') or rt.startswith('F6') or rt.startswith('F24') or rt.startswith('F5'):
                    hdr = f[:25]
                o.write(json.dumps(row, ensure_ascii=False) + '\n')
                n_total += 1
            receipts['files'].append({'file_number': fn, 'url': f'https://docquery.fec.gov/dcdev/posted/{fn}.fec', 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest(),
                                      'record_counts': counts, 'sa_amount_all_rows': str(sa_sum), 'sa_amount_non_memo': str(sa_sum_nonmemo), 'form_header_first_fields': hdr})
    ob = open(out, 'rb').read()
    receipts.update({'output_rows': n_total, 'output_bytes': len(ob), 'output_sha256': hashlib.sha256(ob).hexdigest()})
    json.dump(receipts, open(rec, 'w'), indent=2)
    print(cid, 'files', len(files), 'rows', n_total, 'bytes', len(ob))

main()
