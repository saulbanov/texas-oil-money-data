# TEC filer ids for Abbott and Patrick

Resolved 2026-10-29 from `filers.csv` in the TEC bulk export (D-79, zip sha256 `3d4fb840ab2ffe8a…`), by a search for "Abbott" with "Greg"/"Governor", "Dan Patrick", "Texans for Dan", and last name Patrick with first name Dan. Each id was then confirmed in the TEC Simple Search (`https://www.ethics.state.tx.us/search/cf/`, By Filer ID, built-in browser, 2026-10-29).

## Taken

| Official | Filer id | Type | Name in filers.csv | Status | Simple Search |
|---|---|---|---|---|---|
| Abbott | 00051153 | SPAC | Texans for Greg Abbott | ACTIVE, eff. 2001-06-07; treasurer John L. Nau III | one row, SPAC, Austin TX, "Related COH(s)" |
| Abbott | 00019652 | COH | Abbott, Greg (The Honorable) | CURRENT_OFFICEHOLDER, Governor, eff. 2015-01-01; treasurer Cecilia P. Abbott | two rows, COH and JCOH |
| Patrick | 00064090 | SPAC | Texans for Dan Patrick | ACTIVE, eff. 2008-06-17; treasurer Robert Wells | one row, SPAC, Houston TX |
| Patrick | 00057897 | COH | Patrick, Dan (The Honorable) | CURRENT_OFFICEHOLDER, Lt. Governor, eff. 2015-01-01; treasurer Robert Wells | one row, COH |

The 00019652 id also carries a JCOH row (Supreme Court Justice, Place 3, 1996-01-02 to 2001-06-06). It is the same filer id, so the slice includes any rows filed under it; none fall in 2025–26.

## Rejected (near misses)

| Filer id | Type | Name | Why rejected |
|---|---|---|---|
| 00031088 | JSPC | Judge Abbott Committee (DISSOLVED) | Abbott's 1995–2011 judicial committee, TERMINATED 2011-07-12 |
| 00070352 | SPAC | Republicans for Greg Abbott (DISSOLVED) | Los Angeles committee, Darrell Walker appointor, active 2014-09-11 to 2014-09-23 only; not Abbott's |
| 00086561 | GPAC | Mothers Against Greg Abbott | opposition PAC |
| 00089101 | COH | Bills, James E. (Mr.) | governor candidate whose city is Abbott, TX |
| 00015704 | SPAC | Texans for Dan Kubiak Committee (DISSOLVED) | different Dan |
| 00062488 | SPAC | Texans for Dan Branch | different Dan |
| 00064966 | SPAC | Texans for Dan Gattis, Inc. (DISSOLVED) | different Dan |
| 00066845 | SPAC | Texans for Dan Neil (DISSOLVED) | different Dan |

## Reports in the 2025–26 windows (from cover.csv; the eight newest confirmed in Simple Search)

| Filer | Report # | Type | Period | Total political contributions | Superseded? |
|---|---|---|---|---|---|
| 00051153 | 101011609 (corrects 101006444) | SEMIJUL | 2025-01-01 to 2025-06-30 | $20,188,882.21 | 101006444 has infoOnlyFlag=Y |
| 00051153 | 101029815 | SEMIJAN | 2025-07-01 to 2025-12-31 | $22,710,294.06 | |
| 00051153 | 101035305 | E30DAYBEF | 2026-01-01 to 2026-01-22 | $670,576.80 | |
| 00051153 | 101040213 | E08DAYBEF | 2026-01-23 to 2026-02-21 | $2,138,999.56 | |
| 00051153 | 101055764 | SEMIJUL | 2026-02-22 to 2026-06-30 | $25,505,117.82 | |
| 00051153 | 101067772 | E30DAYBEF | 2026-07-01 to 2026-09-24 | $20,304,875.73 | Simple Search: same |
| 00051153 | 101072179 | E08DAYBEF | 2026-09-25 to 2026-10-24 | $26,034,609.08 | Simple Search: same |
| 00019652 | 101042498 | SEMIJUL | 2026-02-22 to 2026-06-30 | $16,000.00 | |
| 00019652 | 101068173 | E30DAYBEF | 2026-07-01 to 2026-09-24 | $4,750,000.00 | Simple Search: same |
| 00019652 | 101072160 | E08DAYBEF | 2026-09-25 to 2026-10-24 | blank (no contributions) | Simple Search: same |
| 00064090 | 101012309 (corrects 101009073) | SEMIJUL | 2025-01-01 to 2025-06-30 | $5,034,350.00 | 101009073 infoOnlyFlag=Y |
| 00064090 | 101020066 | E08DAYBEF | 2025-07-01 to 2025-10-25 | $1,895,277.59 | |
| 00064090 | 101024127 | SEMIJAN | 2025-10-26 to 2025-12-31 | $1,799,374.21 | |
| 00064090 | 101035206 | E30DAYBEF | 2026-01-01 to 2026-01-22 | $188,852.56 | |
| 00064090 | 101039838 | E08DAYBEF | 2026-01-23 to 2026-02-21 | $736,158.00 | |
| 00064090 | 101064425 (corrects 101055635) | SEMIJUL | 2026-02-22 to 2026-06-30 | $5,075,310.35 | 101055635 infoOnlyFlag=Y |
| 00064090 | 101068411 | E30DAYBEF | 2026-07-01 to 2026-09-24 | $6,254,530.36 | Simple Search: same |
| 00064090 | 101071302 | E08DAYBEF | 2026-09-25 to 2026-10-24 | $5,539,879.94 | Simple Search: same |
| 00057897 | 101036480 | E30DAYBEF | 2026-01-01 to 2026-01-22 | $150,000.00 | |
| 00057897 | 101040569 | E08DAYBEF | 2026-01-23 to 2026-02-21 | $150,000.00 | |
| 00057897 | 101070184 | E30DAYBEF | 2026-07-01 to 2026-09-24 | blank | Simple Search: same |
| 00057897 | 101072774 | E08DAYBEF | 2026-09-25 to 2026-10-24 | $400,000.00 | Simple Search: same |

Other 00057897 reports in 2025 (101011257 SEMIJUL, 101033723 SEMIJAN) and 00019652's (101006439, 101028842, 101035303, 101040189) print a blank total. Daily reports (DAILYCPAC) filed after Oct 24 fall outside every window and carry no totals on the listing.

**Bulk vs per-report:** the eight newest reports' `noadd.csv` files match the bulk slice row for row (same contribution ids, same amounts, zero rows unique to either side; `crosscheck_per_report.json`). The bulk zip of 2026-10-29 carries the 8-day reports, so it is the pull for the Sep 25–Oct 24 window too.
