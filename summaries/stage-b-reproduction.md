# Stage B: reproduction of published 2025–26 figures

Generated 2026-10-29 by `money/tools/reproduce.py`. No sector judgment is made here (that is Stage C). The tool's rules are in its docstring. TEC rows with `infoOnlyFlag=Y` (superseded) are dropped. Schedules A1 (monetary) and A2 (in-kind) both count. Windows are on contribution date. Donors are matched by a name regex keyed to the name the outlet printed, and the row ids behind each hit are listed at the bottom.

**Command** (run from `writing/gop-deserves-to-lose-texas/money/tools/`):

```bash
cd "/Users/saulelbein/Documents/Claude Code/writing/gop-deserves-to-lose-texas/money/tools" && python3 -I reproduce.py --rows
```

**Inputs (sha256)**

| Input | Path | sha256 |
|---|---|---|
| TEC Abbott slice (ids 00051153, 00019652) | `/Volumes/Elements/reference-data/tec-cf-bulk/2026-10-29/slices/tec_abbott.csv` | `59946843f2b5f8a81913fa583969141323e19f9d317aef93e0d840ad0e675cd2` |
| TEC Patrick slice (ids 00064090, 00057897) | `money/raw/tec_patrick.csv` | `5a1685ad319d03d7f4d921316cbe9335d020169bba27375f8d8fdae9d78465e4` |
| FEC Ken Paxton for Senate | `/Volumes/Elements/reference-data/fec-efiling/2026-10-29/fec_C00901918.jsonl` | `bd67a207c4cc9c0b6a9ba7b20ecada93194129434456a33db86c520857bd71dc` |
| FEC Paxton Victory | `money/raw/fec_C00952218.jsonl` | `ca5b7a7915b8b74ba86753a647320ecfc4602858a0a5a48eb26ffc45c223a3b4` |
| FEC Lone Star Liberty PAC | `money/raw/fec_C00901223.jsonl` | `96dc9f2b5a3369af781c9e171912837e4802bbf041301c915b1596b6c42275e2` |
| FEC totals receipt | `money/raw/fec_totals.json` | `5a72ed754271eafb0237a0024497c975c5501671f010f2bf95d26251ae36a64b` |
| Tool | `money/tools/reproduce.py` | `dafef4fb190a313a73b56e95b634eb838348df480bbaaf07a756171dbedef4ff` |

Bulk source: TEC_CF_CSV.zip, 1,080,659,684 bytes, sha256 `3d4fb840ab2ffe8af07a89152853a6c9bf9d9caf24494239719a12928ed6d578` (registry D-79). Tolerance is $10,000 for the Chronicle and $1 for everything else, per the brief. The "At printed precision" column rounds our figure to the unit the outlet printed ($117.6M is printed to $0.1M, so we round to $0.1M) and compares.

## Table (tool output, verbatim)

| # | Official | Source | Check | Window | Published | Ours | Delta | Tolerance | Result | At printed precision | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Abbott | Chronicle | total raised, Texans for Greg Abbott only | 2025-01-01..2026-10-24 | $117,600,000.00 | $117,553,355.26 | $-46,644.74 | $10,000.00 | FAIL | PASS (ours rounds to $117,600,000.00) | printed as $117.6M (nearest $0.1M); the plan says the Chronicle rounds totals to $10K |
| 2 | Abbott | Chronicle | total raised, SPAC + officeholder id | 2025-01-01..2026-10-24 | $117,600,000.00 | $122,319,355.26 | $4,719,355.26 | $10,000.00 | FAIL | FAIL (ours rounds to $122,300,000.00) | officeholder id 00019652 received $4,000,000 from Texans for Greg Abbott on 2026-09-23: a transfer, so summing both ids double-counts it |
| 3 | Abbott | Chronicle | donation count, SPAC (~129,000) | 2025-01-01..2026-10-24 | 129,000 | 129,421 | 421 | 500 | PASS |  | published to the nearest thousand; tolerance 500 rows |
| 4 | Abbott | Chronicle | Anwar, monetary + in-kind ($4.37M) | 2025-01-01..2026-10-24 | $4,370,000.00 | $4,372,086.00 | $2,086.00 | $10,000.00 | PASS |  |  |
| 5 | Abbott | Chronicle | Anwar in-kind only (>$100K) | 2025-01-01..2026-10-24 | $100,000.00 | $122,086.00 | $22,086.00 | must exceed | PASS |  |  |
| 6 | Abbott | Chronicle | Musk ($5.5M) | 2025-01-01..2026-10-24 | $5,500,000.00 | $5,500,000.00 | $0.00 | $10,000.00 | PASS |  |  |
| 7 | Abbott | Chronicle | Fisher ($4.1M) | 2025-01-01..2026-10-24 | $4,100,000.00 | $4,100,000.00 | $0.00 | $10,000.00 | PASS |  |  |
| 8 | Abbott | Chronicle | Fairly, by name ($3.5M) | 2025-01-01..2026-10-24 | $3,500,000.00 | $175.00 | $-3,499,825.00 | $10,000.00 | FAIL |  | only row named Fairly is Hugh Fairly of Frisco, $25 gifts |
| 9 | Abbott | Chronicle | Fairly as Texas Republican Leadership Fund + DealOn LLC ($3.5M) | 2025-01-01..2026-10-24 | $3,500,000.00 | $3,500,000.00 | $0.00 | $10,000.00 | PASS |  | both Amarillo entities; the filed Tribune text (asset TXTRIB_2026-10-06_GREG_ABBOTT_BURNS_THROUGH_WAR_CHEST_IN_TEXAS_05F17, line 57) names Alex Fairly as giving through DealOn LLC and Texas Republican Leadership Fund |
| 10 | Abbott | Chronicle | RGA ($3M) | 2025-01-01..2026-10-24 | $3,000,000.00 | $3,000,000.00 | $0.00 | $10,000.00 | PASS |  | filed as "RGA Right Direction PAC", 2026-10-20 |
| 11 | Abbott | Tribune | total raised (>$20M) | 2026-07-01..2026-09-24 | $20,000,000.00 | $20,304,875.73 | $304,875.73 | must exceed | PASS |  |  |
| 12 | Abbott | Tribune | Anwar ($750K) | 2026-07-01..2026-09-24 | $750,000.00 | $750,000.00 | $0.00 | $1.00 | PASS |  |  |
| 13 | Abbott | Tribune | Rowling ($500K) | 2026-07-01..2026-09-24 | $500,000.00 | $500,000.00 | $0.00 | $1.00 | PASS |  |  |
| 14 | Abbott | Tribune | Campbell ($500K) | 2026-07-01..2026-09-24 | $500,000.00 | $260,000.00 | $-240,000.00 | $1.00 | FAIL |  |  |
| 15 | Abbott | Tribune | Fairly via DealOn LLC + Texas Republican Leadership Fund ($1.5M) | 2026-07-01..2026-09-24 | $1,500,000.00 | $1,500,000.00 | $0.00 | $1.00 | PASS |  | Tribune text line 57 |
| 16 | Abbott | Tribune | Dunn via TUCM ($100K) | 2026-07-01..2026-09-24 | $100,000.00 | $100,000.00 | $0.00 | $1.00 | PASS |  |  |
| 17 | Abbott | Hinojosa | six-figure gifts in the 30-day report: count (52) | 2026-07-01..2026-09-24 | 52 | 54 | 2 | 0 | FAIL |  | rows of $100,000 or more; "one filing" assumed = the 30-day report |
| 18 | Abbott | Hinojosa | six-figure gifts in the 30-day report: distinct donors (52) | 2026-07-01..2026-09-24 | 52 | 52 | 0 | 0 | PASS |  | diagnostic: distinct contributor names among those rows (Anwar filed three $250,000 rows) |
| 19 | Abbott | Hinojosa | six-figure gifts in the 30-day report: dollars ($14M) | 2026-07-01..2026-09-24 | $14,000,000.00 | $14,450,000.00 | $450,000.00 | $1.00 | FAIL | PASS (ours rounds to $14,000,000.00) |  |
| 20 | Abbott | E&E | Anwar ($1.25M) | 2026-02-22..2026-06-30 | $1,250,000.00 | $1,250,000.00 | $0.00 | $1.00 | PASS |  | window ASSUMED = Abbott SEMIJUL period; article text not read (E&E 403 to plain fetch; full-text-fetch run blocked by permission classifier) |
| 21 | Abbott | E&E | Campbell ($300K) | 2026-02-22..2026-06-30 | $300,000.00 | $300,000.00 | $0.00 | $1.00 | PASS |  | window ASSUMED = Abbott SEMIJUL period; article text not read (E&E 403 to plain fetch; full-text-fetch run blocked by permission classifier) |
| 22 | Abbott | E&E | Sellers ($250K) | 2026-02-22..2026-06-30 | $250,000.00 | $250,000.00 | $0.00 | $1.00 | PASS |  | window ASSUMED = Abbott SEMIJUL period; article text not read (E&E 403 to plain fetch; full-text-fetch run blocked by permission classifier) |
| 23 | Abbott | E&E | Oncor PAC ($100K) | 2026-02-22..2026-06-30 | $100,000.00 | $100,000.00 | $0.00 | $1.00 | PASS |  | window ASSUMED = Abbott SEMIJUL period; article text not read (E&E 403 to plain fetch; full-text-fetch run blocked by permission classifier) |
| 24 | Abbott | E&E | Nye ($170K) | 2026-02-22..2026-06-30 | $170,000.00 | $170,000.00 | $0.00 | $1.00 | PASS |  | window ASSUMED = Abbott SEMIJUL period; article text not read (E&E 403 to plain fetch; full-text-fetch run blocked by permission classifier); Erle Nye only (other Nyes gave $431.25) |
| 25 | Abbott | E&E | TXOGA PAC gave (no amount) | 2026-02-22..2026-06-30 | $0.00 | $27,920.12 | $27,920.12 | must exceed | PASS |  | window ASSUMED = Abbott SEMIJUL period; article text not read (E&E 403 to plain fetch; full-text-fetch run blocked by permission classifier) |
| 26 | Abbott | E&E | Chevron PAC gave (no amount) | 2026-02-22..2026-06-30 | $0.00 | $15,000.00 | $15,000.00 | must exceed | PASS |  | window ASSUMED = Abbott SEMIJUL period; article text not read (E&E 403 to plain fetch; full-text-fetch run blocked by permission classifier) |
| 27 | Abbott | Hinojosa | ENTITY rows, all ($5.2M + $2.6M = $7.8M) | 2026-02-22..2026-09-24 | $7,800,000.00 | $6,683,716.74 | $-1,116,283.26 | $1.00 | FAIL | FAIL (ours rounds to $6,700,000.00) | contributorPersentTypeCd = ENTITY; published figures rounded to $0.1M |
| 28 | Abbott | Hinojosa | business entities: ENTITY and not PAC ($5.2M) | 2026-02-22..2026-09-24 | $5,200,000.00 | $3,105,230.96 | $-2,094,769.04 | $1.00 | FAIL | FAIL (ours rounds to $3,100,000.00) | PAC rule: see is_pac() |
| 29 | Abbott | Hinojosa | PACs: ENTITY and PAC ($2.6M) | 2026-02-22..2026-09-24 | $2,600,000.00 | $3,578,485.78 | $978,485.78 | $1.00 | FAIL | FAIL (ours rounds to $3,600,000.00) | PAC rule: see is_pac() |
| 30 | Abbott | Hinojosa | ENTITY rows, all (plan window variant) | 2026-01-01..2026-09-24 | $7,800,000.00 | $7,552,884.65 | $-247,115.35 | $1.00 | FAIL | FAIL (ours rounds to $7,600,000.00) | diagnostic: the plan glosses the window as about Jan 1-Sep 24 2026 (four reports, not two) |
| 31 | Abbott | Hinojosa | business entities: ENTITY and not PAC (plan window variant) | 2026-01-01..2026-09-24 | $5,200,000.00 | $3,285,043.94 | $-1,914,956.06 | $1.00 | FAIL | FAIL (ours rounds to $3,300,000.00) | diagnostic: the plan glosses the window as about Jan 1-Sep 24 2026 (four reports, not two) |
| 32 | Abbott | Hinojosa | PACs: ENTITY and PAC (plan window variant) | 2026-01-01..2026-09-24 | $2,600,000.00 | $4,267,840.71 | $1,667,840.71 | $1.00 | FAIL | FAIL (ours rounds to $4,300,000.00) | diagnostic: the plan glosses the window as about Jan 1-Sep 24 2026 (four reports, not two) |
| 33 | Abbott | Hinojosa | Warren + Long ($600K) | 2026-02-22..2026-09-24 | $600,000.00 | $600,000.00 | $0.00 | $1.00 | PASS |  |  |
| 34 | Abbott | Tackett | TUCM ($100K) | 2026-09-25..2026-10-24 | $100,000.00 | $100,000.00 | $0.00 | $1.00 | PASS |  |  |
| 35 | Patrick | Chronicle | total raised, Texans for Dan Patrick only ($21M) | 2025-01-01..2026-10-24 | $21,000,000.00 | $26,523,733.01 | $5,523,733.01 | $10,000.00 | FAIL | FAIL (ours rounds to $27,000,000.00) |  |
| 36 | Patrick | Chronicle | total raised, SPAC + officeholder id | 2025-01-01..2026-10-24 | $21,000,000.00 | $27,223,733.01 | $6,223,733.01 | $10,000.00 | FAIL | FAIL (ours rounds to $27,000,000.00) | officeholder id 00057897 received $700,000 from Texans for Dan Patrick (transfers) |
| 37 | Patrick | Chronicle | total raised, SPAC, ending at the 30-day report (2026-09-24) | 2025-01-01..2026-09-24 | $21,000,000.00 | $20,983,853.07 | $-16,146.93 | $10,000.00 | FAIL | PASS (ours rounds to $21,000,000.00) | diagnostic: tests whether the Chronicle figure predates the 8-day report |
| 38 | Patrick | Chronicle | donation count (>10,000) | 2025-01-01..2026-10-24 | 10,000 | 12,512 | 2,512 | must exceed | PASS |  |  |
| 39 | Patrick | Chronicle | Yass ($1M) | 2025-01-01..2026-10-24 | $1,000,000.00 | $1,000,000.00 | $0.00 | $10,000.00 | PASS |  |  |
| 40 | Patrick | Chronicle | Perot Jr. ($500K) | 2025-01-01..2026-10-24 | $500,000.00 | $750,000.00 | $250,000.00 | $10,000.00 | FAIL |  | all spellings: "Perot Jr., H. Ross" (2 rows, $500,000) and "Perot Jr, H. Ross" (1 row, $250,000, 8-day) |
| 41 | Patrick | Chronicle | Perot Jr. under the spelling "PEROT JR., H. ROSS" only | 2025-01-01..2026-10-24 | $500,000.00 | $500,000.00 | $0.00 | $10,000.00 | PASS |  | diagnostic: a name-keyed dedupe splits the two spellings into two donors |
| 42 | Patrick | Tribune | total raised ($6.3M) | 2026-07-01..2026-09-24 | $6,300,000.00 | $6,254,530.36 | $-45,469.64 | $1.00 | FAIL | PASS (ours rounds to $6,300,000.00) |  |
| 43 | Patrick | E&E | Nye ($150K) | 2026-02-22..2026-06-30 | $150,000.00 | $150,000.00 | $0.00 | $1.00 | PASS |  | window ASSUMED = Abbott SEMIJUL period; article text not read (E&E 403 to plain fetch; full-text-fetch run blocked by permission classifier) |
| 44 | Patrick | E&E | Musk ($500K) | 2026-02-22..2026-06-30 | $500,000.00 | $500,000.00 | $0.00 | $1.00 | PASS |  | window ASSUMED = Abbott SEMIJUL period; article text not read (E&E 403 to plain fetch; full-text-fetch run blocked by permission classifier); filed as "Elon Musk Recovable Trust" (sic) |
| 45 | Patrick | Tackett | Campbell ($200K) | 2026-09-25..2026-10-24 | $200,000.00 | $200,000.00 | $0.00 | $1.00 | PASS |  |  |
| 46 | Paxton | FEC/Capital & Main | Ken Paxton for Senate C00901918 total receipts vs /totals/ | 2026 cycle | $22,319,359.05 | $22,319,359.05 | $0.00 | $1.00 | PASS |  | sum of period receipts over 9 reports; superseded skipped: none; target from api.open.fec.gov/v1/committee/C00901918/totals/?cycle=2026 (DEMO_KEY), values as printed in session |
| 47 | Paxton | FEC/Capital & Main | Paxton Victory C00952218 total receipts vs /totals/ | 2026 cycle | $12,047,495.63 | $12,047,495.63 | $0.00 | $1.00 | PASS |  | sum of period receipts over 3 reports; superseded skipped: none; target from https://www.fec.gov/data/committee/C00952218/?cycle=2026&tab=filings (browser) |
| 48 | Paxton | FEC/Capital & Main | Lone Star Liberty PAC C00901223 total receipts vs /totals/ | 2026 cycle | $29,696,321.83 | $29,696,321.83 | $0.00 | $1.00 | PASS |  | sum of period receipts over 8 reports; superseded skipped: 1901692; target from https://www.fec.gov/data/committee/C00901223/?cycle=2026&tab=filings (browser) |
| 49 | Paxton | FEC/Capital & Main | Wilks $250K to Paxton Victory on 2026-08-13 | 2026 cycle | $250,000.00 | $250,000.00 | $0.00 | $1.00 | PASS |  |  |
| 50 | Paxton | FEC/Capital & Main | Chevron PAC $200K to Lone Star Liberty PAC | 2026 cycle | $200,000.00 | $200,000.00 | $0.00 | $1.00 | PASS |  |  |
| 51 | Paxton | FEC/Capital & Main | Gordy $250K to Lone Star Liberty PAC | 2026 cycle | $250,000.00 | $250,000.00 | $0.00 | $1.00 | PASS |  |  |
| 52 | Paxton | FEC/Capital & Main | Molleston $100K to Lone Star Liberty PAC | 2026 cycle | $100,000.00 | $100,000.00 | $0.00 | $1.00 | PASS |  |  |

35 of 52 pass
#4 rows: 150447103 150450626 150458278 150463966 150472317 153322756 153322757 153322758 155553834 146069471 147533168 147533183 147533184 147727816 147737810 147745168 147754979 147759185 147768117 149059463
#5 rows: 147533168 147533183 147533184
#6 rows: 150461520 155553868
#7 rows: 153310368 155553835 155562164 146071495 147752668
#8 rows: 150449418 150456370 147752091 147758842 147768247 148738944 149067115
#9 rows: 150472309 153322293 153322367 147768180
#10 rows: 155564311
#12 rows: 153322756 153322757 153322758
#13 rows: 153311872
#14 rows: 153313891 153313892
#15 rows: 153322293 153322367
#16 rows: 153318404
#20 rows: 150447103 150450626 150458278 150463966 150472317
#21 rows: 150451827 150470876
#22 rows: 150473243
#23 rows: 150472099
#24 rows: 150472103
#25 rows: 150457471 150458623 150462375
#26 rows: 150457462
#33 rows: 150473261 153311997
#34 rows: 155562085
#39 rows: 152861171
#40 rows: 151001889 155063473 146088563
#41 rows: 151001889 146088563
#43 rows: 151001814
#44 rows: 151001888
#45 rows: 155063469
#49 rows: SA11A.30924440
#50 rows: SA11C.4919
#51 rows: SA11AI.5008
#52 rows: SA11AI.4970

## Diagnosis of every failed check

Marked **observed** where the filing rows show it, **guess** where they do not.

1. **#1 Abbott total, Texans for Greg Abbott only, −$46,645.** Observed: our sum is $117,553,355.26 over 129,421 rows, and it equals the sum of the seven 2025–26 cover-sheet totals. It rounds to the printed $117.6M. Guess: the Chronicle printed to $0.1M, so the $10,000 tolerance is tighter than the figure. If the Chronicle's own unrounded number is $117.55M, we match.
2. **#2 Abbott, both ids, +$4.7M.** Observed: the officeholder id 00019652 received $750,000 (Aug 11) and $4,000,000 (Sep 23) from Texans for Greg Abbott, plus $16,000 in-kind airplane use. Those are transfers between Abbott's own accounts, so adding the second id double-counts. The Chronicle's figure is the committee alone.
3. **#8 "Fairly" by name.** Observed: no Fairly row is larger than $25. The money is filed under Texas Republican Leadership Fund ($2.5M) and DealOn LLC ($1M), both Amarillo, which sum to exactly $3.5M (check #9 passes). The filed Tribune text, line 57, names Alex Fairly as giving through both entities, so the attribution is sourced. By-name matching is the wrong key for this donor.
4. **#14 Tribune Campbell, $260,000 against $500,000.** Observed: Cody Campbell has two rows in the 30-day report, $250,000 on Sep 9 and $10,000 on Sep 23, and no pledge or other record type in that report names him. **Unexplained.** Guess: the Tribune may have folded in Campbell's $250,000 of Jun 17 (in the previous report) or a gift through an entity. Mayfair Investments of Benbrook gave $250,000 in the window, but nothing in the filing ties it to Campbell. Ask the Tribune or leave the Tribune's Campbell figure unused.
5. **#17 six-figure gifts, 54 rows against 52.** Observed: Anwar filed three $250,000 rows, so the 54 rows are 52 distinct donors (#18 passes). Hinojosa counted donors, not rows. Dollars: $14.45M against "$14M", which passes at printed precision.
6. **#26–#31 Hinojosa entity and PAC split: not reproduced.** Observed: TEC's `contributorPersentTypeCd` has only two codes, INDIVIDUAL and ENTITY, with no PAC code. The tool's PAC test is an ENTITY whose name matches PAC, political action, committee, fund, campaign or party, or which carries `contributorPacFein` or `contributorOosPacFlag=Y`. The two-period window, Feb 22–Sep 24, gives ENTITY $6.68M, split $3.11M business and $3.58M PAC. The plan's Jan 1–Sep 24 gloss gives $7.55M, split $3.29M and $4.27M. Both miss on total and split. Guess: Hinojosa's "business entities" includes contributors coded INDIVIDUAL who give through a company named in the employer field, and the PAC bucket is narrower than ours. One more guess: the 30-day report alone plus the $4.75M officeholder transfers sums to $7.78M, close to $7.8M, which would be a misread of the transfers. Either way the $5.2M and $2.6M do not come out of the contributor-type field, so **their $6.9M energy-and-utility figure should not be used as a Stage C target.**
7. **#34–#35 Patrick total, $26.5M against $21M.** Observed: Texans for Dan Patrick took $26,523,733.01 from Jan 1 2025 to Oct 24 2026, and $5,539,879.94 of it is in the 8-day report. Through Sep 24 the sum is $20,983,853.07 (#36), which rounds to $21M. Guess: the Chronicle's Patrick figure was computed before the 8-day reports were filed Oct 26, or its window ends Sep 24. The Chronicle's Patrick page should be read for its window before this figure rides.
8. **#39 Perot Jr., $750,000 against $500,000.** Observed: Patrick filed three $250,000 rows: 2025-06-27 ("Perot Jr., H. Ross", employer "Hillwood Development Corp."), 2026-06-25 ("Perot Jr., H. Ross", "Hillwood"), and 2026-09-25 in the 8-day report ("Perot Jr, H. Ross", zip 75219-6268, "Hillwood"). The two rows before Sep 25 sum to exactly $500,000. Guess: this is the same cause as item 7, a Chronicle figure computed before the 8-day report. A name-spelling dedupe split (#40) also yields $500,000, but a full Chronicle key would split all three rows on the employer text, so the timing explanation fits better. Both Patrick misses point the same way.
9. **#41 Tribune Patrick $6.3M, −$45,470.** Observed: $6,254,530.36, which rounds to the printed $6.3M. This fails only the $1 tolerance.

**Fixed in the tool, not a data problem:** E&E's Nye check first matched every Nye, adding $431.25 from William and Mark Nye. It now matches Erle Nye only ($170,000, passes).

## Caveats that ride with every number above

- **E&E window is assumed, not read.** The article returned HTTP 403 to a plain fetch, and the full-text-fetch run was blocked by this session's permission classifier. The checks use Feb 22–Jun 30 2026, the period of Abbott's July semiannual report, as the "four months to Jun 30." All seven E&E checks pass on that window, which supports the assumption but does not replace reading the article.
- **FEC totals for Paxton Victory and Lone Star Liberty PAC** came from the fec.gov committee pages, because the DEMO_KEY API ran out after one /totals/ call. Ken Paxton for Senate's came from the API. All three equal the sum of the filed reports' period receipts to the cent.
- **Paxton donor checks** use rows with memo code not X, as filed. WinRed earmark memos, reattributions and redesignations are kept in raw and not netted. Dedupe is Stage C's job.
