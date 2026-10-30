"""How much of each oil-and-gas share rests on calls a reader could weigh differently.

For each group, from the donor views: oil and gas dollars, the part decided only by a keyword in the filed employer or
occupation, the part a reporter flagged as a judgment call (family tie, company line of business), and the share with
every flagged call dropped. Group totals are the published totals in views/industry_ranking_*.csv (FEC totals include
unitemized money the donor views do not list).
Writes views/sensitivity.csv.  python3 -I sensitivity.py
"""
import csv, os

HERE = os.path.dirname(os.path.abspath(__file__)); V = os.path.join(os.path.dirname(HERE), 'views')
GROUPS = [
    ('career', 'abbott', ['abbott_career']), ('career', 'patrick', ['patrick_career']),
    ('career', 'paxton_career_own', ['paxton_state_career', 'paxton_senate', 'paxton_victory']),
    ('career', 'paxton_career', ['paxton_state_career', 'paxton_senate', 'paxton_victory', 'lone_star_liberty']),
    ('2025-26', 'abbott', ['abbott']), ('2025-26', 'patrick', ['patrick']),
    ('2025-26', 'paxton_senate', ['paxton_senate']), ('2025-26', 'paxton_victory', ['paxton_victory']),
    ('2025-26', 'lone_star_liberty', ['lone_star_liberty']),
    ('2025-26', 'paxton_combined', ['paxton_senate', 'paxton_victory', 'lone_star_liberty']),
]
totals = {}
for win in ('career', '2025-26'):
    for r in csv.DictReader(open(os.path.join(V, f'industry_ranking_{win}.csv'))):
        totals[(win, r['group'])] = float(r['group_total'])
out = []
for win, g, files in GROUPS:
    oil = kw = flag = 0.0; nflag = 0
    for fk in files:
        for r in csv.DictReader(open(os.path.join(V, f'donors_{fk}.csv'))):
            if r['tier'] != 'strict':
                continue
            t = float(r['total']); oil += t
            if r['decided_by'] == 'keyword':
                kw += t
            if r['hand_flag'] == 'Y':
                flag += t; nflag += 1
    tot = totals[(win, g)]
    out.append(dict(window=win, group=g, group_total=f'{tot:.2f}', oil_gas=f'{oil:.2f}', oil_share=f'{oil / tot:.6f}',
                    keyword_only=f'{kw:.2f}', flagged_judgment_calls=f'{flag:.2f}', flagged_donors=nflag,
                    share_without_flagged=f'{(oil - flag) / tot:.6f}'))
with open(os.path.join(V, 'sensitivity.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
for r in out:
    print(r['window'], r['group'].ljust(18), f"{float(r['oil_share']):.1%}", '->', f"{float(r['share_without_flagged']):.1%}", f"({r['flagged_donors']} flagged)")
