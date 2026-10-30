# Donor industries, whole careers

Written by `tools/industry_rank.py` from the donor views that `tools/sector_read.py` writes. The oil-and-gas column is the
final 2025-26 strict tier, unchanged. Every other donor carries one OpenSecrets-style industry, decided by a hand ruling
(`tools/industry_rulings.csv`), a keyword over the filed employer, occupation or name, or a keyword over the stated
basis of an oil-tier ruling. Each donor row in `views/industry_<official>.csv` names how it was decided and its raw row ids.

## Inputs (sha256)

| Input | Path | sha256 |
|---|---|---|
| rulings | `/Users/saulelbein/Documents/Claude Code/tx-campaign-money/tools/industry_rulings.csv` | `2334611f826ec77338722a7c37c21f561ff15ad8515adbf250e24aedac0bdd61` |
| tool | `/Users/saulelbein/Documents/Claude Code/tx-campaign-money/tools/industry_rank.py` | `d8f9c3b8aa147e48bdc50aff419dfd3ad5bdf8592b03f0e5a6f8bf79218db68c` |
| summary | `/Users/saulelbein/Documents/Claude Code/tx-campaign-money/views/summary.md` | `67205e72494f7eb44bcfff33b6c3aed918f6af7ebdfd70f49a557888887ff097` |
| donors_paxton_senate | `/Users/saulelbein/Documents/Claude Code/tx-campaign-money/views/donors_paxton_senate.csv` | `fcadbdf74000634c16fddb1a65345c602ef28644c9f75cf7dca7f06bc9f05fdc` |
| donors_paxton_victory | `/Users/saulelbein/Documents/Claude Code/tx-campaign-money/views/donors_paxton_victory.csv` | `a331bff87e86c8a6b73d54efcfa5e1270d0a97b54360ad63d95478e8f79af529` |
| donors_lone_star_liberty | `/Users/saulelbein/Documents/Claude Code/tx-campaign-money/views/donors_lone_star_liberty.csv` | `6b23da29c2410442d208f74d31918eda0c3cfca7224d2ad6f4ee7a65daef1dc0` |
| donors_abbott_career | `/Users/saulelbein/Documents/Claude Code/tx-campaign-money/views/donors_abbott_career.csv` | `2a97b8464e4fe82f12dbf539254ae06ec6288ba2bbcc1abef9405856776444a6` |
| donors_patrick_career | `/Users/saulelbein/Documents/Claude Code/tx-campaign-money/views/donors_patrick_career.csv` | `7cf04f164403b3d6e20a16c9fde7b5c7dfee18d67b700315e6c89fdec11c783e` |
| donors_paxton_state_career | `/Users/saulelbein/Documents/Claude Code/tx-campaign-money/views/donors_paxton_state_career.csv` | `07441be0b49570e232f073dbd6481e44dcdb0570e6681c31ffc9d1a99ab2632b` |

## Industry ranking by official

### abbott: Texans for Greg Abbott, June 2001 to Oct. 24, 2026

Total $507,770,402. Industry identified for 77.2% of dollars.

| Rank | Industry | Sector | Dollars | Share of total | Donors | Largest donors |
|---|---|---|---|---|---|---|
| 1 | **Oil & Gas** | Energy & Natural Resources | $82,782,773 | 16.3% | 1035 | ANWAR, S JAVAID $16,135,679; WARREN, KELCY $4,509,000; GRAHAM, JAY (Spur Energy Partners) $3,442,198 |
| 2 | Securities & Investment | Finance, Insurance & Real Estate | $48,530,637 | 9.6% | 1110 | FISHER, KENNETH $5,600,000; TROUTT, KENNY $4,810,000; PORTER, MICHAEL & MARY $3,100,000 |
| 3 | Real Estate | Finance, Insurance & Real Estate | $34,051,462 | 6.7% | 1101 | ROSKI, EDWARD $5,945,000; PEROT JR., H. ROSS (Hillwood) $4,020,143; HARRIS, WILLIAM $1,300,000 |
| 4 | Retail, Food & Beverage | Misc Business | $28,815,784 | 5.7% | 287 | COX, BOBBY $4,219,445; NAU III, JOHN (Silver Eagle Distri $3,596,217; KNIGHT, PHILIP $2,500,000 |
| 5 | Construction & Contractors | Construction | $27,338,137 | 5.4% | 504 | PITCOCK, JAMES $4,311,050; DOGGETT, WILLIAM (Doggett Equipmen $3,137,554; WEISMAN, JOHN $2,021,000 |
| 6 | Energy, other | Energy & Natural Resources | $17,130,770 | 3.4% | 489 | STEDMAN, STUART $3,200,311; ROWLING, ROBERT $2,802,100; NYE JR., ERLE (Oncor; incl. EN Con $1,152,000 |
| 7 | Lawyers / Law Firms | Lawyers & Lobbyists | $15,458,992 | 3.0% | 1692 | ROSENZWEIG, ROBIN $550,000; VINSON & ELKINS TEXAS PAC $503,160; ANDREWS & KURTH TEXAS PAC $437,500 |
| 8 | Tech & Internet | Communications/Electronics | $14,261,702 | 2.8% | 130 | MUSK, ELON (incl. Elon Musk Revoca $5,510,000; GEBBIA, JOE $2,500,100; WOOD, ANTHONY $1,000,000 |
| 9 | Car Dealers | Transportation | $12,895,228 | 2.5% | 347 | GULF STATES TOYOTA INC STATE PAC $1,400,000; AGRESTI, JOSEPH $942,500; FRIEDKIN, T DAN $875,247 |
| 10 | Business Services & Associations | Misc Business | $12,331,843 | 2.4% | 316 | RYAN TEXAS PAC $1,335,000; BELLINGER, JOHN $1,260,000; BELLINGER, JOHN $1,175,025 |
| 11 | Candidate & Party Committees | Ideological/Single-Issue | $12,208,554 | 2.4% | 246 | RGA RIGHT DIRECTION PAC $7,000,000; GREG ABBOTT CAMPAIGN $3,156,765; ORGANIZING FOR TEXAS SENIORS PAC $507,221 |
| 12 | Health Professionals | Health | $11,604,696 | 2.3% | 1130 | BORDER HEALTH PAC $1,444,259; RAY, JAY $474,058; RAY, RICHIE $352,410 |
| 13 | Ranching & Agriculture | Agribusiness | $8,802,771 | 1.7% | 580 | SANTA ROSA RANCHES $1,015,000; TRAYLOR, RICHARD $775,000; HOLT, PETER $695,000 |
| 14 | Insurance | Finance, Insurance & Real Estate | $7,873,536 | 1.6% | 255 | FAIRLY, ALEX (via Texas Republican $4,000,000; POLITICAL ACTION COMMITTEE OF THE  $652,999; BOENKER, AL $472,500 |
| 15 | Banking & Finance | Finance, Insurance & Real Estate | $7,310,190 | 1.4% | 526 | DWYER, JOHN (Capital Funding Group $1,667,500; STEELE, BRANDON $591,136; PERKINS, JAMES $353,500 |
| 16 | Casinos / Gambling | Misc Business | $6,808,000 | 1.3% | 19 | ADELSON, MIRIAM $2,500,000; THE CHICKASAW NATION $1,725,000; TEXAS SANDS PAC $700,000 |
| 17 | Health Services & Pharmaceuticals | Health | $6,082,343 | 1.2% | 325 | STAI, DIAN $849,700; ZAFFIRINI, CARLOS $812,320; HALBERT, DAVID $525,325 |
| 18 | Manufacturing & Industry | Misc Business | $5,842,624 | 1.2% | 163 | SIMMONS, HAROLD $1,870,000; ANSARY, HUSHANG $1,188,500; CHEN, FELIX $415,000 |
| 19 | Recreation / Live Entertainment | Misc Business | $5,146,929 | 1.0% | 73 | JONES, JERRAL $1,524,574; MCNAIR, ROBERT $851,000; HEAVIN, H GARY $468,792 |
| 20 | Lobbyists & Consultants | Lawyers & Lobbyists | $5,119,815 | 1.0% | 525 | HILLCO PAC $1,371,383; KELLEY, RUSSELL $337,393; BLACKRIDGE ASSOCIATES $215,000 |
| 21 | Education & Nonprofits | Other | $4,329,404 | 0.9% | 221 | PRICE, MACKENZIE $1,000,000; PRICE, MACKENZIE $550,000; PYLE, DAVID $535,000 |
| 22 | Transportation & Rail | Transportation | $4,118,859 | 0.8% | 108 | RICHARD R SCOTT 1991 TRUST $1,080,000; SCOTT, RICHARD $397,941; SCOTT, WILLIAM $390,925 |
| 23 | Home Builders | Construction | $4,026,210 | 0.8% | 114 | PERRY, BOB $910,265; PERRY, DOYLENE $520,000; HOMEPAC OF THE TEXAS ASSN OF BUILD $405,000 |
| 24 | Ideological & Single-Issue Groups | Ideological/Single-Issue | $3,095,117 | 0.6% | 109 | TEXANS FOR LAWSUIT REFORM PAC $1,261,704; TEXANS FOR LAWSUIT REFORM PAC $265,000; TEXANS FOR RESPONSIBLE GOVERNMENT  $200,000 |
| 25 | Telecom & Media | Communications/Electronics | $2,886,461 | 0.6% | 144 | FOLLETT, BRIAN $516,000; AT&T INC TEXAS POLITICAL ACTION CO $472,878; FIGGERS, FREDDIE $285,000 |
| 26 | Hospitals & Nursing Homes | Health | $2,544,465 | 0.5% | 152 | BLAKE, GARY $614,536; NORTH CYPRESS MEDICAL CENTER OPERA $430,908; BLAKE, GARY $303,125 |
| 27 | Labor | Labor | $568,479 | 0.1% | 32 | UNION PACIFIC CORP FUND FOR EFFECT $172,500; HOUSTON POLICE OFFICERS UNION PAC $75,500; TEXAS CORNERSTONE CREDIT UNION LEA $55,000 |
| - | Retired or Homemaker (employer not given) | Not identified | $55,989,654 | 11.0% | 279280 | |
| - | Not identified | Not identified | $59,814,969 | 11.8% | 9587 | |

By sector: Not identified 22.8%; Energy & Natural Resources 19.7%; Finance, Insurance & Real Estate 19.3%; Misc Business 11.6%; Construction 6.2%; Lawyers & Lobbyists 4.1%; Health 4.0%; Communications/Electronics 3.4%; Transportation 3.4%; Ideological/Single-Issue 3.0%; Agribusiness 1.7%; Other 0.9%; Labor 0.1%

### patrick: Texans for Dan Patrick, 2008 to Oct. 24, 2026

Total $129,441,204. Industry identified for 84.6% of dollars.

| Rank | Industry | Sector | Dollars | Share of total | Donors | Largest donors |
|---|---|---|---|---|---|---|
| 1 | **Oil & Gas** | Energy & Natural Resources | $18,845,479 | 14.6% | 483 | SCHARBAUER, DOUGLAS (Midland; oil  $1,485,000; DUNCAN, JAN (widow of Enterprise P $905,000; HUNT, RAY (Hunt Consolidated; incl $900,000 |
| 2 | Real Estate | Finance, Insurance & Real Estate | $12,014,158 | 9.3% | 509 | PEROT JR., H. ROSS (Hillwood) $1,225,200; HUNT, WOODY $1,043,928; ALVIS, STEVEN $818,584 |
| 3 | Securities & Investment | Finance, Insurance & Real Estate | $10,548,197 | 8.1% | 354 | YASS, JEFF $1,350,000; TROUTT, KENNY $785,000; FISHER, KENNETH $650,000 |
| 4 | Retail, Food & Beverage | Misc Business | $9,238,104 | 7.1% | 135 | MCLANE JR., DRAYTON (McLane Group) $1,762,000; FERTITTA, TILMAN $1,092,281; APLIN, ARCH $1,011,483 |
| 5 | Construction & Contractors | Construction | $6,891,913 | 5.3% | 238 | WEISMAN, JOHN $1,225,000; PITCOCK, JAMES $805,000; LANHAM, ROBERT $780,000 |
| 6 | Car Dealers | Transportation | $6,264,719 | 4.8% | 190 | GULF STATES TOYOTA INC STATE PAC $962,256; HERNANDEZ, MICHAEL $445,400; ELSWICK, ROGER $340,000 |
| 7 | Business Services & Associations | Misc Business | $4,989,561 | 3.9% | 246 | RYAN TEXAS PAC $1,485,000; SARVADI, PAUL $317,500; SWINBANK, JOSEPH $276,000 |
| 8 | Lawyers / Law Firms | Lawyers & Lobbyists | $4,946,828 | 3.8% | 576 | ALLEN BOONE HUMPHRIES ROBINSON LLP $372,823; PATTERSON, CARY $254,571; STANTON, JAMES $250,000 |
| 9 | Energy, other | Energy & Natural Resources | $4,901,426 | 3.8% | 343 | ROWLING, ROBERT $1,250,000; NYE JR., ERLE (Oncor; incl. EN Con $505,000; NYE JR , ERLE $190,000 |
| 10 | Ideological & Single-Issue Groups | Ideological/Single-Issue | $4,348,789 | 3.4% | 79 | DEFEND TEXAS LIBERTY PAC $1,000,000; TEXANS FOR LAWSUIT REFORM PAC $610,996; EMPOWER TEXANS PAC $518,100 |
| 11 | Health Professionals | Health | $3,878,183 | 3.0% | 353 | BORDER HEALTH PAC $1,985,000; TEXAS DENTAL ASSOCIATION PAC $275,000; TEXAS OPTOMETRIC PAC $150,000 |
| 12 | Banking & Finance | Finance, Insurance & Real Estate | $2,466,467 | 1.9% | 239 | PERKINS, JAMES $796,697; TBA BANK PAC STATE $211,000; AHLBERG, TREVOR $205,000 |
| 13 | Health Services & Pharmaceuticals | Health | $2,188,673 | 1.7% | 176 | STAI, DIAN $480,000; LEININGER, JAMES $95,000; BROWN, DEDE $88,000 |
| 14 | Lobbyists & Consultants | Lawyers & Lobbyists | $2,067,840 | 1.6% | 338 | HILLCO PAC $839,736; BLACKRIDGE $338,538; KELLEY, RUSSELL $115,000 |
| 15 | Insurance | Finance, Insurance & Real Estate | $1,811,271 | 1.4% | 162 | BOENKER, ALVIN $325,000; BOENKER, AL $285,297; FARMERS EMPLOYEE AND AGENT PAC OF  $202,500 |
| 16 | Tech & Internet | Communications/Electronics | $1,688,359 | 1.3% | 84 | MUSK, ELON (incl. Elon Musk Revoca $1,010,000; COLLINS, RICHARD $165,000; FROST, HOLLOWAY $151,038 |
| 17 | Ranching & Agriculture | Agribusiness | $1,633,278 | 1.3% | 191 | SRR RANCHES LLC $275,000; TEXAS FARM BUREAU AGFUND $101,718; NCHA S TEXAS EVENTS PAC $83,500 |
| 18 | Manufacturing & Industry | Misc Business | $1,628,217 | 1.3% | 72 | LEDWELL, STEVE $289,638; MORIAN, REED $255,000; ANSARY, HUSHANG $150,000 |
| 19 | Transportation & Rail | Transportation | $1,361,028 | 1.1% | 60 | SCOTT, RICHARD $348,550; SCOTT, RICHARD $175,000; GARIBAY, RUBEN $160,000 |
| 20 | Education & Nonprofits | Other | $1,315,699 | 1.0% | 256 | FRIENDS OF THE TTU SYSTEM PAC $150,000; CEQELSKI, ELIZABETH $100,000; MABEE, JOHN $85,000 |
| 21 | Casinos / Gambling | Misc Business | $1,312,558 | 1.0% | 9 | TEXAS SANDS PAC $425,000; KICKAPOO TRADITIONAL TRIBE OF TEXA $225,000; THE CHICKASAW NATION $210,000 |
| 22 | Candidate & Party Committees | Ideological/Single-Issue | $1,118,347 | 0.9% | 78 | ORGANIZING FOR TEXAS SENIORS $350,000; DAN PATRICK CAMPAIGN $140,000; DAN PATRICK CAMPAIGN $123,125 |
| 23 | Hospitals & Nursing Homes | Health | $1,055,946 | 0.8% | 83 | BLAKE, GARY $466,341; FISHER, NEAL $57,000; HCA TEXAS GOOD GOVERNMENT FUND $55,000 |
| 24 | Home Builders | Construction | $937,375 | 0.7% | 55 | HOMEPAC OF TEXAS $285,000; BOWLING, ROBERT $97,500; AUSTIN, DUSTIN $75,000 |
| 25 | Recreation / Live Entertainment | Misc Business | $803,774 | 0.6% | 32 | JONES, JERRAL $200,000; HEAVIN, H GARY $130,000; MITCHELL, LEE $95,000 |
| 26 | Telecom & Media | Communications/Electronics | $706,274 | 0.5% | 52 | AT&T TEXAS PAC $399,858; CHARTER COMMUNICATIONS INC TEXAS P $60,000; TX FRIENDS OF TIME WARNER CABLE PA $53,000 |
| 27 | Labor | Labor | $582,200 | 0.4% | 43 | UNION PACIFIC CORPORATION FUND FOR $95,000; HOUSTON POLICE OFFICERS UNION PAC $90,000; TEXAS CORNERSTONE CREDIT UNION LEA $60,000 |
| - | Retired or Homemaker (employer not given) | Not identified | $2,432,815 | 1.9% | 10954 | |
| - | Not identified | Not identified | $17,463,725 | 13.5% | 3864 | |

By sector: Finance, Insurance & Real Estate 20.7%; Energy & Natural Resources 18.3%; Not identified 15.4%; Misc Business 13.9%; Construction 6.0%; Transportation 5.9%; Health 5.5%; Lawyers & Lobbyists 5.4%; Ideological/Single-Issue 4.2%; Communications/Electronics 1.8%; Agribusiness 1.3%; Other 1.0%; Labor 0.4%

### paxton_state: Ken Paxton's state account (TEC 00051407), 2002 to 2024

Total $45,407,773. Industry identified for 76.2% of dollars.

| Rank | Industry | Sector | Dollars | Share of total | Donors | Largest donors |
|---|---|---|---|---|---|---|
| 1 | **Oil & Gas** | Energy & Natural Resources | $7,400,241 | 16.3% | 319 | DUNN, TIMOTHY $820,000; WILKS, FARRIS $675,000; STALLINGS, KYLE (Desert Royalty; i $507,500 |
| 2 | Securities & Investment | Finance, Insurance & Real Estate | $3,848,661 | 8.5% | 262 | TROUTT, KENNY $650,000; PORTER, MICHAEL $420,000; DEASON, DARWIN $330,000 |
| 3 | Ideological & Single-Issue Groups | Ideological/Single-Issue | $2,661,932 | 5.9% | 44 | TEXANS FOR LAWSUIT REFORM PAC $1,419,226; DEFEND TEXAS LIBERTY PAC $500,000; EMPOWER TEXANS PAC $350,000 |
| 4 | Real Estate | Finance, Insurance & Real Estate | $2,347,761 | 5.2% | 430 | MOAYEDI, MEHRDAD (Centurion Americ $320,400; BENNETT, MONTY $155,000; TREPAC TEXAS ASSOCIATION OF REALTO $125,240 |
| 5 | Business Services & Associations | Misc Business | $2,332,924 | 5.1% | 163 | REPUBLICAN ATTORNEYS GENERAL ASSOC $931,500; REPUBLICAN ATTORNEYS GENERAL ASSOC $258,026; RYAN TEXAS PAC $200,000 |
| 6 | Retail, Food & Beverage | Misc Business | $1,851,404 | 4.1% | 88 | MCLANE, JR , DRAYTON $205,000; HORNER, TIMOTHY $165,000; WASEK, DONALD $150,000 |
| 7 | Lawyers / Law Firms | Lawyers & Lobbyists | $1,825,896 | 4.0% | 661 | HS LAW PAC $111,000; ALLEN BOONE HUMPHRIES ROBINSON LLP $90,869; ANDREWS & KURTH TEXAS PAC $78,000 |
| 8 | Recreation / Live Entertainment | Misc Business | $1,450,280 | 3.2% | 19 | HEAVIN, GARY $1,165,000; MITCHELL, LEE ROY $214,683; HEAVIN, GARY $30,000 |
| 9 | Health Professionals | Health | $1,385,397 | 3.1% | 284 | BORDER HEALTH PAC $360,000; FISHER, NEAL $78,000; AHMED, ANOSH $75,000 |
| 10 | Car Dealers | Transportation | $1,212,700 | 2.7% | 88 | EAGLE, JOHN $125,000; ORR, KEITH $104,500; ELSWICK, ROGER $90,500 |
| 11 | Lobbyists & Consultants | Lawyers & Lobbyists | $1,051,802 | 2.3% | 300 | HILLCO PAC $279,152; BLACKRIDGE $79,606; FRINZI, JIM $50,000 |
| 12 | Health Services & Pharmaceuticals | Health | $1,038,048 | 2.3% | 133 | WEBB, JAMES $235,000; JAMES H WEBB, JR LIVING TRUST $100,000; LACORE, TERRY $87,198 |
| 13 | Energy, other | Energy & Natural Resources | $856,924 | 1.9% | 148 | NYE JR., ERLE (Oncor; incl. EN Con $78,500; BURCIAGA, GILBERT $70,000; BRYAN, JP $65,000 |
| 14 | Insurance | Finance, Insurance & Real Estate | $697,422 | 1.5% | 80 | FAIRLY, ALEX (via Texas Republican $300,000; BOENKER, AL $106,007; FARMERS EMPLOYEE & AGENT PAC OF TE $100,000 |
| 15 | Banking & Finance | Finance, Insurance & Real Estate | $681,206 | 1.5% | 234 | HARPER, ALAN $114,300; AHLBERG, TREVOR $113,000; MARLING, ROBERT $70,000 |
| 16 | Tech & Internet | Communications/Electronics | $673,049 | 1.5% | 95 | FROST, HOLLY $295,000; FROST, HOLLOWAY $85,000; FROST, HOLLY $75,000 |
| 17 | Candidate & Party Committees | Ideological/Single-Issue | $659,668 | 1.5% | 66 | TEXANS FOR GREG ABBOTT $351,750; DAN PATRICK CAMPAIGN $125,000; GARDERE WYNNE SEWELL LLP CAMPAIGN  $26,668 |
| 18 | Construction & Contractors | Construction | $608,379 | 1.3% | 177 | COOK, BRAD $100,000; DANNENBAUM, JAMES $65,000; PEINADO, FRANK $45,000 |
| 19 | Manufacturing & Industry | Misc Business | $421,157 | 0.9% | 42 | EWING, ANTHONY $151,000; SAULSBURY, C R $50,000; ANSARY, HUSHANG $45,000 |
| 20 | Home Builders | Construction | $302,577 | 0.7% | 53 | HOMEPAC OF TEXAS $58,300; PERRY, BOB J $52,000; HUGHES, LEE $28,500 |
| 21 | Ranching & Agriculture | Agribusiness | $287,854 | 0.6% | 88 | TEXAS FARM BUREAU AGFUND $47,500; MARION, ANNE $25,000; LODGE, IV, JOHN $25,000 |
| 22 | Education & Nonprofits | Other | $245,970 | 0.5% | 173 | PHILLIPS, GENE $71,164; SANDEFER, JEFF D $43,696; UNIVERSITY OF HOUSTON PAC $13,750 |
| 23 | Telecom & Media | Communications/Electronics | $219,035 | 0.5% | 53 | AT&T TEXAS PAC $118,922; TX FRIENDS OF TIME WARNER CABLE PA $30,000; CHARTER COMMUNICATIONS, INC, TEXAS $15,000 |
| 24 | Casinos / Gambling | Misc Business | $168,525 | 0.4% | 8 | THE CHICKASAW NATION $55,000; KICKAPOO TRADITIONAL TRIBE OF TEXA $40,000; KICKAPOO TRADITIONAL TRIBE OF TEXA $35,000 |
| 25 | Labor | Labor | $166,565 | 0.4% | 18 | TEXAS CORNERSTONE CREDIT UNION LEA $35,000; HOUSTON POLICE OFFICERS UNION PAC $27,500; TEXAS CORNERSTONE CREDIT UNION LEA $20,000 |
| 26 | Hospitals & Nursing Homes | Health | $166,319 | 0.4% | 60 | BLAKE, GARY $62,500; THOMASON, JOE $15,796; NORTH CYPRESS MEDICAL CENTER $15,000 |
| 27 | Transportation & Rail | Transportation | $57,502 | 0.1% | 46 | SCOTT, WILLIAM $13,000; WILLIS, ROY $10,000; BNSF RAILPAC $10,000 |
| - | Retired or Homemaker (employer not given) | Not identified | $3,180,138 | 7.0% | 18218 | |
| - | Not identified | Not identified | $7,608,437 | 16.8% | 3209 | |

By sector: Not identified 23.8%; Energy & Natural Resources 18.2%; Finance, Insurance & Real Estate 16.7%; Misc Business 13.7%; Ideological/Single-Issue 7.3%; Lawyers & Lobbyists 6.3%; Health 5.7%; Transportation 2.8%; Construction 2.0%; Communications/Electronics 2.0%; Agribusiness 0.6%; Other 0.5%; Labor 0.4%

### paxton_career: Paxton career: state account 2002-2024 plus his three federal committees 2025-26, including the super PAC (not netted for the $21,257 transfer)

Total $109,470,949. Industry identified for 70.4% of dollars.

| Rank | Industry | Sector | Dollars | Share of total | Donors | Largest donors |
|---|---|---|---|---|---|---|
| 1 | **Oil & Gas** | Energy & Natural Resources | $13,653,060 | 12.5% | 564 | SCHARBAUER, DOUGLAS (Midland; oil  $1,225,700; DUNN, TIMOTHY $820,000; WILKS, FARRIS $675,000 |
| 2 | Tech & Internet | Communications/Electronics | $12,777,195 | 11.7% | 222 | MUSK, ELON (incl. Elon Musk Revoca $10,000,000; GEBBIA, JOSEPH $1,000,000; FROST, HOLLY $295,000 |
| 3 | Securities & Investment | Finance, Insurance & Real Estate | $6,245,357 | 5.7% | 499 | TROUTT, KENNY $650,000; PORTER, MICHAEL $420,000; DEASON, DARWIN $330,000 |
| 4 | Candidate & Party Committees | Ideological/Single-Issue | $6,043,636 | 5.5% | 84 | SLF PAC $5,000,000; TEXANS FOR GREG ABBOTT $351,750; BUCKEYE VICTORY ACTION INC $250,000 |
| 5 | Lawyers / Law Firms | Lawyers & Lobbyists | $5,062,550 | 4.6% | 1075 | THOMAS J HENRY LAW PLLC $646,107; AZIZ, MUHAMMAD $293,000; AZIZ, MUHAMMAD $265,800 |
| 6 | Ideological & Single-Issue Groups | Ideological/Single-Issue | $4,159,393 | 3.8% | 63 | TEXANS FOR LAWSUIT REFORM PAC $1,419,226; MAHA ACTION PAC $1,000,000; DEFEND TEXAS LIBERTY PAC $500,000 |
| 7 | Real Estate | Finance, Insurance & Real Estate | $3,651,967 | 3.3% | 809 | MOAYEDI, MEHRDAD (Centurion Americ $320,400; BENNETT, MONTY $155,000; TREPAC TEXAS ASSOCIATION OF REALTO $125,240 |
| 8 | Business Services & Associations | Misc Business | $3,306,304 | 3.0% | 262 | REPUBLICAN ATTORNEYS GENERAL ASSOC $931,500; REPUBLICAN ATTORNEYS GENERAL ASSOC $258,026; RYAN, GEORGE $234,400 |
| 9 | Recreation / Live Entertainment | Misc Business | $2,942,046 | 2.7% | 37 | HEAVIN, GARY $1,165,000; HEAVIN, GARY $500,000; JONES, JERRAL $350,000 |
| 10 | Health Services & Pharmaceuticals | Health | $2,578,019 | 2.4% | 236 | KNUTZ, JONATHAN $1,100,000; WEBB, JAMES $235,000; LACORE, TERRY $100,000 |
| 11 | Retail, Food & Beverage | Misc Business | $2,214,204 | 2.0% | 134 | MCLANE, JR , DRAYTON $205,000; HORNER, TIMOTHY $165,000; WASEK, DONALD $150,000 |
| 12 | Health Professionals | Health | $1,943,626 | 1.8% | 614 | BORDER HEALTH PAC $360,000; FISHER, NEAL $78,000; U S ANESTHESIA PARTNERS, INC PAC D $75,000 |
| 13 | Lobbyists & Consultants | Lawyers & Lobbyists | $1,612,588 | 1.5% | 570 | HILLCO PAC $279,152; VARMA, SAMIT $97,740; BLACKRIDGE $79,606 |
| 14 | Car Dealers | Transportation | $1,437,387 | 1.3% | 139 | EAGLE, JOHN $125,000; ORR, KEITH $104,500; LOBB, LAWRENCE $100,000 |
| 15 | Banking & Finance | Finance, Insurance & Real Estate | $1,331,545 | 1.2% | 388 | MARLING, ROBERT $225,000; MARLING, ROBERT $150,000; HARPER, ALAN $114,300 |
| 16 | Construction & Contractors | Construction | $1,318,055 | 1.2% | 341 | PAUL MCLAREN REVOCABLE TRUST $250,000; DACUS, TAYLOR $100,000; COOK, BRAD $100,000 |
| 17 | Energy, other | Energy & Natural Resources | $1,209,068 | 1.1% | 254 | SAGO ENERGY LP $100,000; ROWLING, ROBERT $100,000; NYE JR., ERLE (Oncor; incl. EN Con $78,500 |
| 18 | Insurance | Finance, Insurance & Real Estate | $1,037,722 | 0.9% | 160 | FAIRLY, ALEX (via Texas Republican $300,000; FAIRLY, ALEX (via Texas Republican $274,300; BOENKER, AL $106,007 |
| 19 | Manufacturing & Industry | Misc Business | $999,445 | 0.9% | 104 | MCCORVEY, TONY $270,800; EWING, ANTHONY $151,000; SORKIN, FELIX $150,000 |
| 20 | Transportation & Rail | Transportation | $735,539 | 0.7% | 101 | MILTON, CHELSEY $500,000; MILTON, TREVOR $100,000; SCOTT, WILLIAM $13,000 |
| 21 | Hospitals & Nursing Homes | Health | $729,082 | 0.7% | 100 | BLAKE, GARY $274,000; CARROLLTON REGIONAL MEDICAL CENTER $150,000; BLAKE, GARY $100,000 |
| 22 | Ranching & Agriculture | Agribusiness | $592,013 | 0.5% | 304 | BANKS, KENNETH $50,000; TEXAS FARM BUREAU AGFUND $47,500; MARION, ANNE $25,000 |
| 23 | Home Builders | Construction | $467,877 | 0.4% | 80 | HOMEPAC OF TEXAS $58,300; PERRY, BOB J $52,000; BOWLING, RANDALL $50,000 |
| 24 | Education & Nonprofits | Other | $377,988 | 0.3% | 294 | PHILLIPS, GENE $71,164; SANDEFER, JEFF D $43,696; SUTTON, JOSEPH $25,000 |
| 25 | Casinos / Gambling | Misc Business | $269,113 | 0.2% | 12 | TRIBE OF TEXAS $100,000; THE CHICKASAW NATION $55,000; KICKAPOO TRADITIONAL TRIBE OF TEXA $40,000 |
| 26 | Telecom & Media | Communications/Electronics | $251,857 | 0.2% | 72 | AT&T TEXAS PAC $118,922; TX FRIENDS OF TIME WARNER CABLE PA $30,000; CHARTER COMMUNICATIONS, INC, TEXAS $15,000 |
| 27 | Labor | Labor | $167,954 | 0.2% | 21 | TEXAS CORNERSTONE CREDIT UNION LEA $35,000; HOUSTON POLICE OFFICERS UNION PAC $27,500; TEXAS CORNERSTONE CREDIT UNION LEA $20,000 |
| - | Unitemized (FEC) | Not identified | $6,075,477 | 5.5% | 3 | |
| - | Retired or Homemaker (employer not given) | Not identified | $10,843,800 | 9.9% | 29118 | |
| - | Not identified | Not identified | $15,437,084 | 14.1% | 6476 | |

By sector: Not identified 29.6%; Energy & Natural Resources 13.6%; Communications/Electronics 11.9%; Finance, Insurance & Real Estate 11.2%; Ideological/Single-Issue 9.3%; Misc Business 8.9%; Lawyers & Lobbyists 6.1%; Health 4.8%; Transportation 2.0%; Construction 1.6%; Agribusiness 0.5%; Other 0.3%; Labor 0.2%

### paxton_career_own: Paxton career without the super PAC: state account 2002-2024 plus Ken Paxton for Senate and Paxton Victory 2025-26

Total $79,774,627. Industry identified for 62.8% of dollars.

| Rank | Industry | Sector | Dollars | Share of total | Donors | Largest donors |
|---|---|---|---|---|---|---|
| 1 | **Oil & Gas** | Energy & Natural Resources | $10,809,102 | 13.5% | 542 | DUNN, TIMOTHY $820,000; WILKS, FARRIS $675,000; STALLINGS, KYLE (Desert Royalty; i $507,500 |
| 2 | Securities & Investment | Finance, Insurance & Real Estate | $5,595,065 | 7.0% | 472 | TROUTT, KENNY $650,000; PORTER, MICHAEL $420,000; DEASON, DARWIN $330,000 |
| 3 | Lawyers / Law Firms | Lawyers & Lobbyists | $3,449,766 | 4.3% | 1054 | AZIZ, MUHAMMAD $265,800; STOGNER, BRANT $200,000; BENNY AGOSTO JR PC $150,000 |
| 4 | Real Estate | Finance, Insurance & Real Estate | $3,105,603 | 3.9% | 788 | MOAYEDI, MEHRDAD (Centurion Americ $320,400; BENNETT, MONTY $155,000; TREPAC TEXAS ASSOCIATION OF REALTO $125,240 |
| 5 | Business Services & Associations | Misc Business | $3,091,304 | 3.9% | 259 | REPUBLICAN ATTORNEYS GENERAL ASSOC $931,500; REPUBLICAN ATTORNEYS GENERAL ASSOC $258,026; RYAN, GEORGE $234,400 |
| 6 | Ideological & Single-Issue Groups | Ideological/Single-Issue | $3,059,393 | 3.8% | 61 | TEXANS FOR LAWSUIT REFORM PAC $1,419,226; DEFEND TEXAS LIBERTY PAC $500,000; EMPOWER TEXANS PAC $350,000 |
| 7 | Recreation / Live Entertainment | Misc Business | $2,392,046 | 3.0% | 35 | HEAVIN, GARY $1,165,000; JONES, JERRAL $350,000; JONES, JOHN $272,000 |
| 8 | Retail, Food & Beverage | Misc Business | $2,060,615 | 2.6% | 129 | MCLANE, JR , DRAYTON $205,000; HORNER, TIMOTHY $165,000; WASEK, DONALD $150,000 |
| 9 | Health Professionals | Health | $1,835,758 | 2.3% | 606 | BORDER HEALTH PAC $360,000; FISHER, NEAL $78,000; AHMED, ANOSH $75,000 |
| 10 | Tech & Internet | Communications/Electronics | $1,773,896 | 2.2% | 219 | FROST, HOLLY $295,000; GEBBIA, JOSEPH $274,300; WINN, STEPHEN $150,000 |
| 11 | Lobbyists & Consultants | Lawyers & Lobbyists | $1,605,588 | 2.0% | 569 | HILLCO PAC $279,152; VARMA, SAMIT $97,740; BLACKRIDGE $79,606 |
| 12 | Car Dealers | Transportation | $1,424,189 | 1.8% | 135 | EAGLE, JOHN $125,000; ORR, KEITH $104,500; LOBB, LAWRENCE $100,000 |
| 13 | Energy, other | Energy & Natural Resources | $1,201,969 | 1.5% | 251 | SAGO ENERGY LP $100,000; ROWLING, ROBERT $100,000; NYE JR., ERLE (Oncor; incl. EN Con $78,500 |
| 14 | Health Services & Pharmaceuticals | Health | $1,175,920 | 1.5% | 228 | WEBB, JAMES $235,000; JAMES H WEBB, JR LIVING TRUST $100,000; LACORE, TERRY $87,198 |
| 15 | Banking & Finance | Finance, Insurance & Real Estate | $1,102,256 | 1.4% | 385 | MARLING, ROBERT $150,000; HARPER, ALAN $114,300; AHLBERG, TREVOR $113,000 |
| 16 | Insurance | Finance, Insurance & Real Estate | $1,036,722 | 1.3% | 159 | FAIRLY, ALEX (via Texas Republican $300,000; FAIRLY, ALEX (via Texas Republican $274,300; BOENKER, AL $106,007 |
| 17 | Construction & Contractors | Construction | $950,466 | 1.2% | 334 | DACUS, TAYLOR $100,000; COOK, BRAD $100,000; DANNENBAUM, JAMES $65,000 |
| 18 | Manufacturing & Industry | Misc Business | $840,156 | 1.1% | 101 | MCCORVEY, TONY $270,800; EWING, ANTHONY $151,000; SAULSBURY, C R $50,000 |
| 19 | Candidate & Party Committees | Ideological/Single-Issue | $770,337 | 1.0% | 80 | TEXANS FOR GREG ABBOTT $351,750; DAN PATRICK CAMPAIGN $125,000; NRSC $62,000 |
| 20 | Hospitals & Nursing Homes | Health | $627,092 | 0.8% | 97 | BLAKE, GARY $274,000; CARROLLTON REGIONAL MEDICAL CENTER $150,000; BLAKE, GARY $62,500 |
| 21 | Ranching & Agriculture | Agribusiness | $588,714 | 0.7% | 303 | BANKS, KENNETH $50,000; TEXAS FARM BUREAU AGFUND $47,500; MARION, ANNE $25,000 |
| 22 | Home Builders | Construction | $414,877 | 0.5% | 77 | HOMEPAC OF TEXAS $58,300; PERRY, BOB J $52,000; BOWLING, RANDALL $50,000 |
| 23 | Education & Nonprofits | Other | $351,998 | 0.4% | 292 | PHILLIPS, GENE $71,164; SANDEFER, JEFF D $43,696; UNIVERSITY OF HOUSTON PAC $13,750 |
| 24 | Casinos / Gambling | Misc Business | $269,113 | 0.3% | 12 | TRIBE OF TEXAS $100,000; THE CHICKASAW NATION $55,000; KICKAPOO TRADITIONAL TRIBE OF TEXA $40,000 |
| 25 | Telecom & Media | Communications/Electronics | $251,857 | 0.3% | 72 | AT&T TEXAS PAC $118,922; TX FRIENDS OF TIME WARNER CABLE PA $30,000; CHARTER COMMUNICATIONS, INC, TEXAS $15,000 |
| 26 | Labor | Labor | $167,954 | 0.2% | 21 | TEXAS CORNERSTONE CREDIT UNION LEA $35,000; HOUSTON POLICE OFFICERS UNION PAC $27,500; TEXAS CORNERSTONE CREDIT UNION LEA $20,000 |
| 27 | Transportation & Rail | Transportation | $131,225 | 0.2% | 97 | SCOTT, WILLIAM $13,000; WILLIS, ROY $10,500; WILLIS, ROY $10,000 |
| - | Unitemized (FEC) | Not identified | $6,073,116 | 7.6% | 2 | |
| - | Retired or Homemaker (employer not given) | Not identified | $10,230,976 | 12.8% | 29075 | |
| - | Not identified | Not identified | $13,387,552 | 16.8% | 6407 | |

By sector: Not identified 37.2%; Energy & Natural Resources 15.1%; Finance, Insurance & Real Estate 13.6%; Misc Business 10.8%; Lawyers & Lobbyists 6.3%; Ideological/Single-Issue 4.8%; Health 4.6%; Communications/Electronics 2.5%; Transportation 1.9%; Construction 1.7%; Agribusiness 0.7%; Other 0.4%; Labor 0.2%

## Caveats

- The industry of a donor is the industry of the money's source as best stated: a family office or trust takes the industry of the fortune behind it when a hand ruling says so; otherwise its filed employer.
- Keyword calls (`decided_by` keyword or basis) were not hand-checked donor by donor. Hand rulings cite their basis.
- Committees that pass money through (PACs, joint committees, other candidates) are ranked as their own kind, not traced to their donors, except where a hand ruling names the funder.
- Oil & Gas here is the final strict tier. "Energy, other" is the broad tier minus strict: utilities, power and diversified energy fortunes.
- Labels checked on 2026-10-30 against OpenSecrets' Industries by Sector page (https://www.opensecrets.org/industries/slist), saved as `raw/opensecrets_industries_by_sector_2026-10-30.txt`. Our sectors are theirs; candidate committees sit in Ideological/Single-Issue as OpenSecrets files them. Where one of our industries spans several of theirs, the table below says which.

| Our industry | OpenSecrets industries it spans |
|---|---|
| Oil & Gas | Oil & Gas + Natural Gas Pipelines; also chemical makers (OpenSecrets: Misc Business, Chemical & Related Manufacturing) and fuel distribution, by Saul's 2026-10-29 ruling |
| Energy, other | Electric Utilities; Alternative Energy Production & Services; diversified energy fortunes (no OpenSecrets equivalent) |
| Real Estate | Real Estate |
| Securities & Investment | Securities & Investment; Venture Capital; Hedge Funds; Private Equity & Investment Firms |
| Banking & Finance | Commercial Banks; Credit Unions; Finance / Credit Companies; Mortgage Bankers & Brokers |
| Insurance | Insurance |
| Home Builders | Home Builders |
| Construction & Contractors | General Contractors; Special Trade Contractors; Construction Services; Architectural Services; Building Materials & Equipment |
| Hospitals & Nursing Homes | Hospitals & Nursing Homes |
| Health Professionals | Health Professionals; Dentists; Nurses; Chiropractors |
| Health Services & Pharmaceuticals | Health Services/HMOs; Pharmaceuticals / Health Products; Medical Supplies |
| Lawyers / Law Firms | Lawyers / Law Firms |
| Lobbyists & Consultants | Lobbyists; political consultants (OpenSecrets may file some under Business Services) |
| Tech & Internet | Computer Software; Internet; Electronics Manufacturing & Equipment |
| Telecom & Media | Telephone Utilities; Telecom Services & Equipment; TV / Movies / Music; Printing & Publishing |
| Car Dealers | Car Dealers; Automotive |
| Transportation & Rail | Air Transport; Trucking; Railroads; Sea Transport |
| Retail, Food & Beverage | Food & Beverage; Restaurants & Drinking Establishments; Beer, Wine & Liquor; Retail Sales; Food Stores; Clothing Manufacturing (Phil Knight) |
| Manufacturing & Industry | Steel Production; Misc Manufacturing & Distributing; Chemical & Related Manufacturing (non-petrochemical) |
| Casinos / Gambling | Casinos / Gambling; Indian Gaming |
| Business Services & Associations | Business Associations; Business Services; Miscellaneous Services; Advertising/Public Relations; For-profit Prisons |
| Recreation / Live Entertainment | Recreation / Live Entertainment; Professional Sports, Sports Arenas & Related Equipment & Services |
| Ranching & Agriculture | Livestock; Farm Bureaus; Crop Production & Basic Processing; Forestry & Forest Products |
| Ideological & Single-Issue Groups | Republican/Conservative and the other issue industries |
| Candidate & Party Committees | Candidate Committees; Leadership PACs (party committees have no OpenSecrets industry) |
| Labor | all union industries |
| Education & Nonprofits | Education; Non-profits, Foundations & Philanthropists; For-profit Education; Clergy |

- Our Oil & Gas is broader than OpenSecrets' Oil & Gas industry (pipelines, and by Saul's ruling petrochemicals and fuel distribution). The narrow-definition share was estimated for 2025-26 only (see `industries_2025-26.md`).
- Career oil tiers come from `hand_rulings.csv` plus `hand_rulings_career.csv` as applied in the career donor views; career coverage is lower for older years.
