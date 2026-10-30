# Texas oil money: the data

This repository holds the data behind Saul Elbein's count of the oil and gas money given to Gov. Greg Abbott, Lt. Gov. Dan Patrick and Attorney General Ken Paxton. It is built from their campaign filings with the Texas Ethics Commission and, for Paxton's 2026 U.S. Senate run, the Federal Election Commission. Every dollar in every figure below can be traced to a filed contribution in `contributions/oil_and_energy_contributions.csv`, and every contribution can be looked up on the commission's site by its report id and contribution id.

## The findings

Whole careers:

| Who | Period | Raised | From oil and gas | Share | Next industry | Share with judgment calls dropped |
|---|---|---|---|---|---|---|
| Greg Abbott | June 2001 to Oct. 24, 2026 (Texans for Greg Abbott) | $507.8 million | $82.8 million | 16.3% | Securities & Investment, $48.5 million | 14.0% |
| Dan Patrick | 2008 to Oct. 24, 2026 (Texans for Dan Patrick) | $129.4 million | $18.8 million | 14.6% | Real Estate, $12.0 million | 13.6% |
| Ken Paxton, his own committees | 2002 to Oct. 2026 (state account 2002-2024; Ken Paxton for Senate and Paxton Victory, 2026 cycle) | $79.8 million | $10.8 million | 13.5% | Securities & Investment, $5.6 million | 12.2% |
| Ken Paxton, with the super PAC | same as above, plus Lone Star Liberty PAC, 2026 cycle | $109.5 million | $13.7 million | 12.5% | Tech & Internet, $12.8 million | 11.2% |

This election cycle:

| Who | Period | Raised | From oil and gas | Share | Next industry | Share with judgment calls dropped |
|---|---|---|---|---|---|---|
| Greg Abbott | Jan. 1, 2025 to Oct. 24, 2026 | $117.6 million | $19.7 million | 16.8% | Securities & Investment, $11.1 million | 14.1% |
| Dan Patrick | Jan. 1, 2025 to Oct. 24, 2026 | $26.5 million | $4.7 million | 17.8% | Real Estate, $2.8 million | 16.8% |
| Ken Paxton, joint committee | 2026 cycle (Paxton Victory) | $12.0 million | $2.9 million | 23.9% | Securities & Investment, $1.2 million | 19.2% |
| Ken Paxton, three committees | 2026 cycle (Senate campaign, joint committee, super PAC) | $64.1 million | $6.3 million | 9.8% | Tech & Internet, $12.1 million | 8.4% |

"Next industry" is the largest industry other than oil and gas. Industries follow OpenSecrets' categories. Money from donors with no employer listed, and small unitemized federal gifts, has no industry but counts in each total.

## How to check a figure

1. **Sum the contributions.** In `contributions/oil_and_energy_contributions.csv`, keep the rows whose `tier` is `oil and gas` and whose `filer_or_committee` is the committee you are checking (Abbott `00051153`, Patrick `00064090`, Paxton's state account `00051407`, Paxton's federal committees `C00901918`, `C00952218`, `C00901223`). For this election cycle, also keep `in_2025_26 = yes`. The amounts add up to the oil and gas figures above.
2. **Look up any contribution.** For a state row, search the filer id at https://www.ethics.state.tx.us/search/cf/, open the report named in `report_or_filing` and find the `contribution_id`. For a federal row, the committee's filings are on fec.gov and `contribution_id` is the schedule line and transaction id.
3. **See why a donor counts.** Each row carries `why`, `decided_by` and `judgment_call`. Every ruling, with its written basis, is in `rulings/`.
4. **Check the totals.** `checks/report_check_tec.csv` sets each report's own filed contribution total, minus its unitemized money, against the sum of the rows used here. The rows match 77 of 77 of Abbott's reports, 66 of 66 of Patrick's and 71 of 78 of Paxton's, to the cent. `checks/report_check_fec.csv` does the same for each federal filing: 20 of 20 match their own summary line.
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

- Five of Paxton's 2001-2002 state reports, together $109,670 in itemized gifts, have no contribution rows in the commission's export, so his state total is short by that much.
- His two 2010 reports as a candidate for House speaker file no contribution total to check against.
- Abbott's judicial campaigns of the 1990s and his separate officeholder account are not included.
- Transfers between a man's own committees are not counted twice.
- Industries other than oil and gas were assigned from filed employers and, for the largest donors, by review. Committees that pass money along are counted as committees, not traced to their own donors.

Analysis by Saul Elbein.
