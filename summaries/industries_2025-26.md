# Donor industries, 2025-26

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
| donors_abbott | `/Users/saulelbein/Documents/Claude Code/tx-campaign-money/views/donors_abbott.csv` | `c6a77de1fabef008e44ae6e62ced441901acedd369705d868252d0f17f9f3def` |
| donors_patrick | `/Users/saulelbein/Documents/Claude Code/tx-campaign-money/views/donors_patrick.csv` | `7e4e1c5620cf7be5ac675ca75d22ff160ebaf7e08844b1137bad829159ef34cc` |
| donors_paxton_senate | `/Users/saulelbein/Documents/Claude Code/tx-campaign-money/views/donors_paxton_senate.csv` | `fcadbdf74000634c16fddb1a65345c602ef28644c9f75cf7dca7f06bc9f05fdc` |
| donors_paxton_victory | `/Users/saulelbein/Documents/Claude Code/tx-campaign-money/views/donors_paxton_victory.csv` | `a331bff87e86c8a6b73d54efcfa5e1270d0a97b54360ad63d95478e8f79af529` |
| donors_lone_star_liberty | `/Users/saulelbein/Documents/Claude Code/tx-campaign-money/views/donors_lone_star_liberty.csv` | `6b23da29c2410442d208f74d31918eda0c3cfca7224d2ad6f4ee7a65daef1dc0` |

## Industry ranking by official

### abbott: Texans for Greg Abbott

Total $117,553,355. Industry identified for 86.4% of dollars.

| Rank | Industry | Sector | Dollars | Share of total | Donors | Largest donors |
|---|---|---|---|---|---|---|
| 1 | **Oil & Gas** | Energy & Natural Resources | $19,739,495 | 16.8% | 121 | ANWAR, S JAVAID $4,372,086; WARREN, KELCY $1,506,300; CAMPBELL, CODY (Double Eagle; incl $840,000 |
| 2 | Securities & Investment | Finance, Insurance & Real Estate | $11,125,862 | 9.5% | 118 | FISHER, KENNETH $4,100,000; YASS, JEFF $1,000,000; ANDRESEN, MATTHEW $700,000 |
| 3 | Tech & Internet | Communications/Electronics | $10,131,050 | 8.6% | 21 | MUSK, ELON (incl. Elon Musk Revoca $5,500,000; GEBBIA, JOE $2,500,000; WOOD, ANTHONY $1,000,000 |
| 4 | Retail, Food & Beverage | Misc Business | $8,461,378 | 7.2% | 41 | KNIGHT, PHILIP $2,500,000; NAU III, JOHN (Silver Eagle Distri $1,524,811; COX, BOBBY $1,246,600 |
| 5 | Real Estate | Finance, Insurance & Real Estate | $7,787,219 | 6.6% | 124 | ROSKI, EDWARD $2,000,000; PEROT JR., H. ROSS (Hillwood) $1,097,489; CROW, HARLAN $575,000 |
| 6 | Construction & Contractors | Construction | $7,512,378 | 6.4% | 58 | DOGGETT, WILLIAM (Doggett Equipmen $1,604,946; ACOSTA, ARCILIA $925,000; WEISMAN, JOHN $810,000 |
| 7 | Energy, other | Energy & Natural Resources | $5,302,862 | 4.5% | 57 | STEDMAN, STUART $1,514,107; ROWLING, ROBERT $850,000; BLACK MOUNTAIN POWER LLC $500,000 |
| 8 | Insurance | Finance, Insurance & Real Estate | $3,746,116 | 3.2% | 14 | FAIRLY, ALEX (via Texas Republican $3,500,000; POLITICAL ACTION COMMITTEE OF THE  $100,000; ADAMS, PHILLIP $100,000 |
| 9 | Casinos / Gambling | Misc Business | $3,100,000 | 2.6% | 5 | ADELSON, MIRIAM $1,500,000; THE CHICKASAW NATION $1,000,000; TEXAS SANDS PAC $300,000 |
| 10 | Candidate & Party Committees | Ideological/Single-Issue | $3,051,034 | 2.6% | 25 | RGA RIGHT DIRECTION PAC $3,000,000; WOOD, GRANT $15,000; FOLEY & LARDNER LLP TEXAS CAMPAIGN $10,000 |
| 11 | Car Dealers | Transportation | $2,838,056 | 2.4% | 35 | SEWELL, CARL $500,000; HERNANDEZ, MICHAEL $459,490; CLAY COOLEY INVESTMENTS $300,000 |
| 12 | Business Services & Associations | Misc Business | $2,821,812 | 2.4% | 33 | BELLINGER, JOHN $800,000; SWINBANK, JOSEPH $500,000; FORD, CURTIS $241,062 |
| 13 | Banking & Finance | Finance, Insurance & Real Estate | $2,490,771 | 2.1% | 33 | DWYER, JOHN (Capital Funding Group $1,515,000; HENDERSON, GEORGE $250,000; BEAL, ANDREW $250,000 |
| 14 | Lawyers / Law Firms | Lawyers & Lobbyists | $1,855,258 | 1.6% | 96 | ROSENZWEIG, ROBIN $500,000; ALLEN BOONE HUMPHRIES ROBINSON, LL $121,055; STODGHILL, STEVEN $108,021 |
| 15 | Education & Nonprofits | Other | $1,854,211 | 1.6% | 18 | PRICE, MACKENZIE $1,000,000; PYLE, DAVID $300,000; PRICE, MACKENZIE $100,000 |
| 16 | Ranching & Agriculture | Agribusiness | $1,784,340 | 1.5% | 47 | SRR RANCHES LLC $525,000; TRAYLOR, RICHARD $250,000; THE JASPERRUTH RANCH LLC $150,000 |
| 17 | Recreation / Live Entertainment | Misc Business | $1,677,080 | 1.4% | 13 | JONES, JERRAL $1,000,000; EPSTEIN, ROBERT $300,000; TORN, SUSAN AND SAM $250,000 |
| 18 | Health Professionals | Health | $1,211,257 | 1.0% | 66 | BORDER HEALTH PAC $263,598; PEREZ, NOLAN $117,000; RAY, JAY $100,000 |
| 19 | Transportation & Rail | Transportation | $1,191,511 | 1.0% | 15 | JAFFE, JORDAN $264,000; SCOTT, RICHARD $209,800; SPAMER, JOAQUIN $110,300 |
| 20 | Health Services & Pharmaceuticals | Health | $844,000 | 0.7% | 26 | TURNER, FREDERICK $250,000; HALBERT, DAVID $200,000; LEININGER, JAMES $100,000 |
| 21 | Ideological & Single-Issue Groups | Ideological/Single-Issue | $759,000 | 0.6% | 13 | TEXANS FOR LAWSUIT REFORM PAC $416,000; TEXANS FOR TRUTH & LIBERTY PAC $100,000; TEXANS FOR RESPONSIBLE GOVERNMENT  $100,000 |
| 22 | Lobbyists & Consultants | Lawyers & Lobbyists | $727,801 | 0.6% | 52 | HILLCO PAC $125,000; MANAGEMENT AND GOVERNANCE CONSULTI $100,000; CABRERA, CYNTHIA $57,500 |
| 23 | Hospitals & Nursing Homes | Health | $623,970 | 0.5% | 10 | BLAKE, GARY $462,000; BLAKE, GARY $45,470; HCA TEXAS GOOD GOVERNMENT FUND $35,000 |
| 24 | Manufacturing & Industry | Misc Business | $353,100 | 0.3% | 11 | GUPTA, SATISH $103,000; WHITE, MARTHA & WALTER $100,000; CHEN, FELIX $100,000 |
| 25 | Home Builders | Construction | $293,121 | 0.2% | 11 | BOWLING, ROBERT $60,000; BOWLING, RANDALL $60,000; HOMEPAC OF THE TEXAS ASSN OF BUILD $47,500 |
| 26 | Telecom & Media | Communications/Electronics | $201,604 | 0.2% | 10 | WELLS, RICHARD $50,000; AT&T INC TEXAS POLITICAL ACTION CO $50,000; CHARTER COMMUNICATIONS, INC TEXAS  $30,000 |
| 27 | Labor | Labor | $85,569 | 0.1% | 5 | UNION PACIFIC CORP FUND FOR EFFECT $35,000; PLUMBERS LOCAL UNION NO 68 PAC $25,000; HOUSTON POLICE OFFICERS UNION PAC $20,000 |
| - | Retired or Homemaker (employer not given) | Not identified | $7,407,398 | 6.3% | 38734 | |
| - | Not identified | Not identified | $8,576,102 | 7.3% | 549 | |

By sector: Finance, Insurance & Real Estate 21.4%; Energy & Natural Resources 21.3%; Misc Business 14.0%; Not identified 13.6%; Communications/Electronics 8.8%; Construction 6.6%; Transportation 3.4%; Ideological/Single-Issue 3.2%; Health 2.3%; Lawyers & Lobbyists 2.2%; Other 1.6%; Agribusiness 1.5%; Labor 0.1%

### patrick: Texans for Dan Patrick

Total $26,523,733. Industry identified for 88.5% of dollars.

| Rank | Industry | Sector | Dollars | Share of total | Donors | Largest donors |
|---|---|---|---|---|---|---|
| 1 | **Oil & Gas** | Energy & Natural Resources | $4,710,510 | 17.8% | 65 | CAMPBELL, CODY (Double Eagle; incl $450,000; DUNCAN, JAN (widow of Enterprise P $400,000; TEXANS UNITED FOR A CONSERVATIVE M $350,000 |
| 2 | Real Estate | Finance, Insurance & Real Estate | $2,778,461 | 10.5% | 68 | PEROT JR., H. ROSS (Hillwood) $750,000; CROW, HARLAN $325,000; HUNT, WOODY $300,000 |
| 3 | Securities & Investment | Finance, Insurance & Real Estate | $2,722,016 | 10.3% | 53 | YASS, JEFF $1,000,000; FISHER, KENNETH $650,000; SEAY, GEORGE $200,000 |
| 4 | Retail, Food & Beverage | Misc Business | $1,950,188 | 7.4% | 33 | MCLANE JR., DRAYTON (McLane Group) $500,000; APLIN, ARCH $450,000; NAU III, JOHN (Silver Eagle Distri $425,000 |
| 5 | Construction & Contractors | Construction | $1,384,291 | 5.2% | 44 | WEISMAN, JOHN $325,000; AGC OF TEXAS PAC ACCOUNT $250,750; LANHAM, ROBERT $200,000 |
| 6 | Business Services & Associations | Misc Business | $1,217,059 | 4.6% | 27 | RYAN TEXAS PAC $450,000; RYAN LLC PAC $250,000; SWINBANK, JOSEPH $100,000 |
| 7 | Energy, other | Energy & Natural Resources | $1,211,849 | 4.6% | 58 | ROWLING, ROBERT $250,000; NYE JR., ERLE (Oncor; incl. EN Con $150,000; NYE JR , ERLE $150,000 |
| 8 | Tech & Internet | Communications/Electronics | $1,135,332 | 4.3% | 14 | MUSK, ELON (incl. Elon Musk Revoca $1,000,000; FROST, HOLLOWAY $56,038; BARSKIY, MAXIM $50,000 |
| 9 | Car Dealers | Transportation | $951,980 | 3.6% | 38 | GULF STATES TOYOTA INC STATE PAC $350,000; HERNANDEZ, MICHAEL $115,000; CLAY COOLEY INVESTMENTS $60,000 |
| 10 | Lawyers / Law Firms | Lawyers & Lobbyists | $819,799 | 3.1% | 65 | STANTON, JAMES $150,000; PATTERSON, CHARLES $100,000; ALLEN BOONE HUMPHRIES ROBINSON LLP $70,000 |
| 11 | Banking & Finance | Finance, Insurance & Real Estate | $690,739 | 2.6% | 19 | PERKINS, JAMES $350,000; CANTU, ALONZO $142,876; TBA BANK PAC STATE $100,000 |
| 12 | Health Professionals | Health | $635,298 | 2.4% | 39 | BORDER HEALTH PAC $450,000; TEXAS DENTAL ASSOCIATION PAC $50,000; TEXAS DENTAL ASSOCIATION POLITICAL $25,000 |
| 13 | Ranching & Agriculture | Agribusiness | $438,902 | 1.7% | 33 | SRR RANCHES LLC $200,000; TEXAS FARM BUREAU AGFUND $75,200; HOUSTON SAN JACINTO RANCH LLC $50,000 |
| 14 | Ideological & Single-Issue Groups | Ideological/Single-Issue | $411,250 | 1.6% | 9 | TEXANS FOR LAWSUIT REFORM PAC $200,000; TEXANS FOR LAWSUIT REFORM PAC $100,000; THE BEER ALLIANCE OF TEXAS PAC $30,000 |
| 15 | Health Services & Pharmaceuticals | Health | $381,677 | 1.4% | 25 | STAI, DIAN $125,000; TEXPAC STATEWIDE TEXAS MEDICAL ASS $40,000; CVS HEALTH PAC $40,000 |
| 16 | Transportation & Rail | Transportation | $337,710 | 1.3% | 16 | GARIBAY, RUBEN $150,000; SCOTT, WILLIAM $75,000; GONSOULIN, AL $50,000 |
| 17 | Education & Nonprofits | Other | $316,644 | 1.2% | 50 | FRIENDS OF THE TTU SYSTEM PAC $100,000; PRICE, MACKENZIE $50,000; FRIENDS OF THE UNIVERSITY OF TEXAS $50,000 |
| 18 | Hospitals & Nursing Homes | Health | $244,185 | 0.9% | 7 | BLAKE, GARY $212,947; HCA TEXAS GOOD GOVERNMENT FUND $30,000; HAMON, ERIC $1,000 |
| 19 | Lobbyists & Consultants | Lawyers & Lobbyists | $242,364 | 0.9% | 42 | HILLCO PAC $150,000; BLACKRIDGE $20,000; TEXAS LOBBY STRATEGIES $10,000 |
| 20 | Manufacturing & Industry | Misc Business | $240,019 | 0.9% | 6 | LEDWELL, STEVE $100,000; EWING, ANTHONY $65,000; MCCORVEY SR , ANTHONY $50,000 |
| 21 | Home Builders | Construction | $224,525 | 0.8% | 9 | BOWLING, RANDALL $75,000; BOWLING, ROBERT $50,000; HOMEPAC OF TEXAS $45,000 |
| 22 | Insurance | Finance, Insurance & Real Estate | $145,251 | 0.5% | 18 | FAIRLY, ALEX (via Texas Republican $100,000; POLITICAL ACTION COMMITTEE OF THE  $25,000; ALLSTATE INSURANCE COMPANY PAC $9,000 |
| 23 | Casinos / Gambling | Misc Business | $125,058 | 0.5% | 4 | KICKAPOO TRADITIONAL TRIBE OF TEXA $100,000; THE CHICKASAW NATION $25,000; HARPER, DANIEL $52 |
| 24 | Labor | Labor | $80,010 | 0.3% | 6 | UNION PACIFIC CORPORATION FUND FOR $27,500; HOUSTON POLICE OFFICERS UNION PAC $20,000; UNION PACIFIC CORPORATION FUND FOR $12,500 |
| 25 | Candidate & Party Committees | Ideological/Single-Issue | $45,385 | 0.2% | 5 | ROBERT NICHOLS SENATE CAMPAIGN $25,000; FOLEY & LARDNER LLP TEXAS CAMPAIGN $10,000; BRIAN BIRDWELL CAMPAIGN $10,000 |
| 26 | Recreation / Live Entertainment | Misc Business | $34,708 | 0.1% | 3 | TORN, RONALD $25,000; HEAVIN, GARY $9,500; GAYNOR, GLORIA $208 |
| 27 | Telecom & Media | Communications/Electronics | $3,050 | 0.0% | 4 | TOOLEY, BRADLEY $1,000; JONES, SHANNA $1,000; DELISI COMMUNICATIONS PAC $1,000 |
| - | Retired or Homemaker (employer not given) | Not identified | $785,533 | 3.0% | 4530 | |
| - | Not identified | Not identified | $2,259,938 | 8.5% | 596 | |

By sector: Finance, Insurance & Real Estate 23.9%; Energy & Natural Resources 22.3%; Misc Business 13.4%; Not identified 11.5%; Construction 6.1%; Transportation 4.9%; Health 4.8%; Communications/Electronics 4.3%; Lawyers & Lobbyists 4.0%; Ideological/Single-Issue 1.7%; Agribusiness 1.7%; Other 1.2%; Labor 0.3%

### paxton_senate: Ken Paxton for Senate

Total $22,319,359. Industry identified for 23.1% of dollars.

| Rank | Industry | Sector | Dollars | Share of total | Donors | Largest donors |
|---|---|---|---|---|---|---|
| 1 | Lawyers / Law Firms | Lawyers & Lobbyists | $620,070 | 2.8% | 382 | SHIELDS, JOHN $40,000; STEWART, SCOTT $14,650; NEIMAN, JOHN $14,000 |
| 2 | Real Estate | Finance, Insurance & Real Estate | $615,842 | 2.8% | 350 | WOLFE, STEVEN $16,318; HUFFINES, PHILLIP $16,318; ALVIS, STEVEN $16,318 |
| 3 | Securities & Investment | Finance, Insurance & Real Estate | $575,004 | 2.6% | 195 | THALER, JOHN $14,000; SAWYER, JOHN $14,000; RUSSELL, BEEBEN $14,000 |
| 4 | **Oil & Gas** | Energy & Natural Resources | $532,461 | 2.4% | 203 | NEWKUMET, WAYNE $16,318; NEWKUMET, TRAVIS $16,318; BURCIAGA, GILBERT $16,318 |
| 5 | Lobbyists & Consultants | Lawyers & Lobbyists | $411,046 | 1.8% | 265 | FRINZI, JAMES $14,000; BARLEY, MICHAEL $10,500; ANDRO, RICHARD $10,000 |
| 6 | Health Professionals | Health | $397,861 | 1.8% | 320 | LEHMANN, ROBERT $15,000; BECK, HOWARD $14,078; STEVENS, D $14,000 |
| 7 | Ranching & Agriculture | Agribusiness | $235,360 | 1.1% | 210 | LODGE, JOHN $11,000; FIGUEROA, TIM $10,000; SKOV, ROBERT $7,500 |
| 8 | Banking & Finance | Finance, Insurance & Real Estate | $231,050 | 1.0% | 146 | SINGLETON, MARK $14,000; SIINO, SPENCER $14,000; AUSTIN, JEFF $9,318 |
| 9 | Construction & Contractors | Construction | $172,087 | 0.8% | 154 | MECKES, DONOVAN $14,000; LANHAM, ROBERT $14,000; POGUE, BEN $7,000 |
| 10 | Tech & Internet | Communications/Electronics | $151,547 | 0.7% | 117 | BLAIR, ALAN $20,400; BROWN, MATT $14,000; AQUILA, ANTHONY $14,000 |
| 11 | Energy, other | Energy & Natural Resources | $142,045 | 0.6% | 99 | CASH, CLAY $14,000; SYMANK, AARON $7,000; QUEZADA, DOUG $7,000 |
| 12 | Health Services & Pharmaceuticals | Health | $127,623 | 0.6% | 92 | KNUTZ, JONATHAN $14,000; HAMMOND, STEVAN $12,000; ST LEGER, JOHN $10,500 |
| 13 | Candidate & Party Committees | Ideological/Single-Issue | $110,668 | 0.5% | 14 | NRSC $62,000; WINRED TECHNICAL SERVICES, LLC $20,726; SBA PRO LIFE AMERICA CANDIDATE FUN $5,000 |
| 14 | Business Services & Associations | Misc Business | $109,379 | 0.5% | 91 | SMITH, GREGORY $7,000; RIDGELY, GERALD $7,000; REAGAN, WILLIAM $7,000 |
| 15 | Manufacturing & Industry | Misc Business | $104,999 | 0.5% | 54 | LEDWELL, STEVE $31,500; PIZER, VIRGIL $14,000; LYDECKER, JEFFREY $7,000 |
| 16 | Education & Nonprofits | Other | $102,528 | 0.5% | 118 | ELDRED, KEN $8,000; CURRAN, ISABEL $7,000; AUSTIN, REBECCA $7,000 |
| 17 | Retail, Food & Beverage | Misc Business | $101,711 | 0.5% | 37 | DYER, DON $14,000; AUNG, KATIE $14,000; COX, BOBBY $12,318 |
| 18 | Car Dealers | Transportation | $101,489 | 0.5% | 45 | DURANT, JERRY $14,100; LOBB, LAWRENCE $14,000; HERNANDEZ, MICHAEL $9,318 |
| 19 | Transportation & Rail | Transportation | $73,723 | 0.3% | 51 | WILLIS, ROY $10,500; GARIBAY, RUBEN $9,330; WILSON, STEPHEN $7,000 |
| 20 | Home Builders | Construction | $62,300 | 0.3% | 23 | HUGHES, LEE $15,000; HUGHES, LEE $14,000; ELLISON, BILL $7,000 |
| 21 | Insurance | Finance, Insurance & Real Estate | $58,501 | 0.3% | 77 | PHILLIPS, BRADFORD $10,000; INDEPENDENT INSURANCE AGENTS & BRO $5,000; TILLEY, AARON $3,500 |
| 22 | Recreation / Live Entertainment | Misc Business | $29,766 | 0.1% | 11 | HEAVIN, GARY $14,000; MITCHELL, LEE $7,000; DE JESUS, DAVID $7,000 |
| 23 | Ideological & Single-Issue Groups | Ideological/Single-Issue | $28,662 | 0.1% | 14 | PICK, JACKI $7,000; REPUBLICAN MAJORITY FUND $5,000; JOBS, FREEDOM & SECURITY PAC $5,000 |
| 24 | Hospitals & Nursing Homes | Health | $26,773 | 0.1% | 34 | BLAKE, GARY $7,000; BOX, BARRY $3,500; ASHTON, ANDY $2,318 |
| 25 | Telecom & Media | Communications/Electronics | $22,462 | 0.1% | 18 | BOWLING, PATTY $7,000; CHRISTENSON, MICHAEL $3,500; NEXSTAR MEDIA GROUP, INC PAC $3,311 |
| 26 | Labor | Labor | $1,389 | 0.0% | 3 | CHOAT, CHRISTOPHER $1,041; MCCREIGHT, ANDREW $208; FUNK, LOUIS $140 |
| 27 | Casinos / Gambling | Misc Business | $588 | 0.0% | 3 | LAWSON, ARTHUR $260; PYDO, BARBARA $250; STONE, NATHAN $78 |
| - | Unitemized (FEC) | Not identified | $6,070,928 | 27.2% | 1 | |
| - | Retired or Homemaker (employer not given) | Not identified | $6,854,338 | 30.7% | 10838 | |
| - | Not identified | Not identified | $4,247,157 | 19.0% | 3135 | |

By sector: Not identified 76.9%; Finance, Insurance & Real Estate 6.6%; Lawyers & Lobbyists 4.6%; Energy & Natural Resources 3.0%; Health 2.5%; Misc Business 1.6%; Agribusiness 1.1%; Construction 1.1%; Transportation 0.8%; Communications/Electronics 0.8%; Ideological/Single-Issue 0.6%; Other 0.5%; Labor 0.0%

### paxton_victory: Paxton Victory (joint committee)

Total $12,047,496. Industry identified for 85.6% of dollars.

| Rank | Industry | Sector | Dollars | Share of total | Donors | Largest donors |
|---|---|---|---|---|---|---|
| 1 | **Oil & Gas** | Energy & Natural Resources | $2,876,400 | 23.9% | 20 | GORDY, RUSSELL (SG Interests; incl $350,000; MCDONALD, JOHNNY (Lubbock oil prod $300,000; CAMPBELL, CODY (Double Eagle; incl $299,300 |
| 2 | Securities & Investment | Finance, Insurance & Real Estate | $1,171,400 | 9.7% | 15 | TROUTT, LISA $265,800; TROUTT, KENNY $265,800; DEASON, DOUGLAS $265,800 |
| 3 | Lawyers / Law Firms | Lawyers & Lobbyists | $1,003,800 | 8.3% | 11 | AZIZ, MUHAMMAD $265,800; STOGNER, BRANT $200,000; BENNY AGOSTO JR PC $150,000 |
| 4 | Tech & Internet | Communications/Electronics | $949,300 | 7.9% | 7 | GEBBIA, JOSEPH $274,300; WINN, STEPHEN $150,000; DAVIS, LINDSAY $125,000 |
| 5 | Recreation / Live Entertainment | Misc Business | $912,000 | 7.6% | 5 | JONES, JERRAL $350,000; JONES, JOHN $272,000; HEAVIN, H $250,000 |
| 6 | Business Services & Associations | Misc Business | $649,000 | 5.4% | 5 | RYAN, GEORGE $234,400; FRANKLIN, LARRY $188,600; RALSTON, SHANNON $125,000 |
| 7 | Hospitals & Nursing Homes | Health | $434,000 | 3.6% | 3 | BLAKE, GARY $274,000; CARROLLTON REGIONAL MEDICAL CENTER $150,000; TEXAS SPINE AND JOINT HOSPITAL LTD $10,000 |
| 8 | Ideological & Single-Issue Groups | Ideological/Single-Issue | $368,800 | 3.1% | 3 | PICK, JACKI $265,800; TZEDEK PAC $100,000; AMERICA FIRST MAJORITY PAC $3,000 |
| 9 | Manufacturing & Industry | Misc Business | $314,000 | 2.6% | 5 | MCCORVEY, TONY $270,800; MCCORVEY, MITZY $29,200; LEDWELL, STEVE $7,000 |
| 10 | Insurance | Finance, Insurance & Real Estate | $280,800 | 2.3% | 2 | FAIRLY, ALEX (via Texas Republican $274,300; STERLING, DAVID $6,500 |
| 11 | Energy, other | Energy & Natural Resources | $203,000 | 1.7% | 4 | SAGO ENERGY LP $100,000; ROWLING, ROBERT $100,000; SHKOZA, KLODIAN $2,500 |
| 12 | Banking & Finance | Finance, Insurance & Real Estate | $190,000 | 1.6% | 5 | MARLING, ROBERT $150,000; SINGLETON, MARVIN $15,000; SIINO, SPENCER $10,000 |
| 13 | Construction & Contractors | Construction | $170,000 | 1.4% | 3 | DACUS, TAYLOR $100,000; MCLAREN, PAUL $50,000; MJERASHAJ, GENTJAN $20,000 |
| 14 | Lobbyists & Consultants | Lawyers & Lobbyists | $142,740 | 1.2% | 4 | VARMA, SAMIT $97,740; LINDSEY, RUSSELL $25,000; YARBROUGH, STACY $10,000 |
| 15 | Real Estate | Finance, Insurance & Real Estate | $142,000 | 1.2% | 8 | MOAYEDI, MEHRDAD (Centurion Americ $50,000; BOWLING, ROBERT $50,000; SHADDOCK, WILLIAM $20,000 |
| 16 | Car Dealers | Transportation | $110,000 | 0.9% | 2 | LOBB, LAWRENCE $100,000; WISCHNEWSKY, DARRYL $10,000 |
| 17 | Retail, Food & Beverage | Misc Business | $107,500 | 0.9% | 4 | DYER, DON $75,000; COX, BOBBY $25,000; MORRISON, SHAWN $5,000 |
| 18 | Casinos / Gambling | Misc Business | $100,000 | 0.8% | 1 | TRIBE OF TEXAS $100,000 |
| 19 | Ranching & Agriculture | Agribusiness | $65,500 | 0.5% | 5 | BANKS, KENNETH $50,000; GEORGE, PATRICIA $5,000; PAULY, SCOTT $3,500 |
| 20 | Health Professionals | Health | $52,500 | 0.4% | 2 | THOMAS, SUCHMOR $50,000; ZARRABI, SAAM $2,500 |
| 21 | Home Builders | Construction | $50,000 | 0.4% | 1 | BOWLING, RANDALL $50,000 |
| 22 | Telecom & Media | Communications/Electronics | $10,360 | 0.1% | 1 | GALICOT, GREGORIO $10,360 |
| 23 | Health Services & Pharmaceuticals | Health | $10,250 | 0.1% | 3 | HAMMONDS, STEVAN $9,000; HAMMOND, STEVAN $1,000; BLAYLOCK, KAREN $250 |
| 24 | Education & Nonprofits | Other | $3,500 | 0.0% | 1 | ELDRED, KEN $3,500 |
| - | Unitemized (FEC) | Not identified | $2,188 | 0.0% | 1 | |
| - | Retired or Homemaker (employer not given) | Not identified | $196,500 | 1.6% | 19 | |
| - | Not identified | Not identified | $1,531,958 | 12.7% | 63 | |

By sector: Energy & Natural Resources 25.6%; Misc Business 17.3%; Finance, Insurance & Real Estate 14.8%; Not identified 14.4%; Lawyers & Lobbyists 9.5%; Communications/Electronics 8.0%; Health 4.1%; Ideological/Single-Issue 3.1%; Construction 1.8%; Transportation 0.9%; Agribusiness 0.5%; Other 0.0%

### lone_star_liberty: Lone Star Liberty PAC (super PAC)

Total $29,696,322. Industry identified for 91.0% of dollars.

| Rank | Industry | Sector | Dollars | Share of total | Donors | Largest donors |
|---|---|---|---|---|---|---|
| 1 | Tech & Internet | Communications/Electronics | $11,003,299 | 37.1% | 3 | MUSK, ELON (incl. Elon Musk Revoca $10,000,000; GEBBIA, JOSEPH $1,000,000; JUNCOSA, MARK $3,299 |
| 2 | Candidate & Party Committees | Ideological/Single-Issue | $5,273,299 | 17.8% | 4 | SLF PAC $5,000,000; BUCKEYE VICTORY ACTION INC $250,000; TOM RAMSEY CAMPAIGN $20,000 |
| 3 | **Oil & Gas** | Energy & Natural Resources | $2,843,958 | 9.6% | 22 | SCHARBAUER, DOUGLAS (Midland; oil  $1,225,700; MCDONALD, JOHNNY (Lubbock oil prod $510,000; GORDY, RUSSELL (SG Interests; incl $250,000 |
| 4 | Lawyers / Law Firms | Lawyers & Lobbyists | $1,612,784 | 5.4% | 21 | THOMAS J HENRY LAW PLLC $646,107; AZIZ, MUHAMMAD $293,000; STOGNER, BRANT $200,000 |
| 5 | Health Services & Pharmaceuticals | Health | $1,402,099 | 4.7% | 8 | KNUTZ, JONATHAN $1,100,000; LACORE, TERRY $100,000; EVEXIAS MANAGEMENT $100,000 |
| 6 | Ideological & Single-Issue Groups | Ideological/Single-Issue | $1,100,000 | 3.7% | 2 | MAHA ACTION PAC $1,000,000; TEXANS FOR TRUTH AND LIBERTY PAC $100,000 |
| 7 | Securities & Investment | Finance, Insurance & Real Estate | $650,292 | 2.2% | 27 | DEASON, DARWIN $210,000; DONDERO, JAMES $100,000; ABRAHAM, SALEM $75,000 |
| 8 | Transportation & Rail | Transportation | $604,314 | 2.0% | 4 | MILTON, CHELSEY $500,000; MILTON, TREVOR $100,000; SCOTT, WILLIAM $3,299 |
| 9 | Recreation / Live Entertainment | Misc Business | $550,000 | 1.9% | 2 | HEAVIN, GARY $500,000; JONES, JERRAL $50,000 |
| 10 | Real Estate | Finance, Insurance & Real Estate | $546,364 | 1.8% | 21 | GABBAY, MAYA $120,000; MOAYEDI, MEHRDAD (Centurion Americ $100,000; ABBOTT, LAUREN $100,000 |
| 11 | Construction & Contractors | Construction | $367,588 | 1.2% | 7 | PAUL MCLAREN REVOCABLE TRUST $250,000; BYLER, BILL $50,000; BELL, PETER $35,000 |
| 12 | Banking & Finance | Finance, Insurance & Real Estate | $229,289 | 0.8% | 3 | MARLING, ROBERT $225,000; MONK, MICHAEL $3,299; HUTCHINSON, BRAD $990 |
| 13 | Business Services & Associations | Misc Business | $215,000 | 0.7% | 3 | GEO REENTRY SERVICES, LLC $200,000; FRANKLIN, LARRY $10,000; JAIN, UMESH $5,000 |
| 14 | Manufacturing & Industry | Misc Business | $159,289 | 0.5% | 3 | SORKIN, FELIX $150,000; CRENSHAW, WILL $8,299; WILMETH, STEVE $990 |
| 15 | Retail, Food & Beverage | Misc Business | $153,588 | 0.5% | 5 | DYER, DON $75,000; AUNG, KATIE $71,000; WASEK, DONALD $3,299 |
| 16 | Health Professionals | Health | $107,867 | 0.4% | 8 | U S ANESTHESIA PARTNERS, INC PAC D $75,000; NOSNIK, PEDRO $20,000; PEREZ, NOLAN $3,299 |
| 17 | Hospitals & Nursing Homes | Health | $101,990 | 0.3% | 3 | BLAKE, GARY $100,000; RUFF, MARK $1,000; ASHTON, ANDY $990 |
| 18 | Home Builders | Construction | $53,000 | 0.2% | 3 | BOWLING, ROBERT $25,000; BOWLING, RANDALL $25,000; ADDISON HOMES LLC $3,000 |
| 19 | Education & Nonprofits | Other | $25,990 | 0.1% | 2 | SUTTON, JOSEPH $25,000; WILKINSON, SUSANNE $990 |
| 20 | Car Dealers | Transportation | $13,197 | 0.0% | 4 | HERNANDEZ, MICHAEL $3,299; EWING, FINLEY $3,299; ELSWICK, ROGER $3,299 |
| 21 | Energy, other | Energy & Natural Resources | $7,099 | 0.0% | 3 | GILLIAM, FROSTY $3,299; BURCIAGA, GILBERT $3,299; ABS ELECTRIC $500 |
| 22 | Lobbyists & Consultants | Lawyers & Lobbyists | $7,000 | 0.0% | 1 | BOUNDARY CONSULTING LLC $7,000 |
| 23 | Ranching & Agriculture | Agribusiness | $3,299 | 0.0% | 1 | BROWN, ROB $3,299 |
| 24 | Insurance | Finance, Insurance & Real Estate | $1,000 | 0.0% | 1 | LOONAM, TIMOTHY $1,000 |
| - | Unitemized (FEC) | Not identified | $2,361 | 0.0% | 1 | |
| - | Retired or Homemaker (employer not given) | Not identified | $612,823 | 2.1% | 43 | |
| - | Not identified | Not identified | $2,049,532 | 6.9% | 69 | |

By sector: Communications/Electronics 37.1%; Ideological/Single-Issue 21.5%; Energy & Natural Resources 9.6%; Not identified 9.0%; Lawyers & Lobbyists 5.5%; Health 5.4%; Finance, Insurance & Real Estate 4.8%; Misc Business 3.6%; Transportation 2.1%; Construction 1.4%; Other 0.1%; Agribusiness 0.0%

### paxton_combined: Paxton, three committees (not netted for the $21,257 Paxton Victory transferred to the campaign)

Total $64,063,177. Industry identified for 66.3% of dollars.

| Rank | Industry | Sector | Dollars | Share of total | Donors | Largest donors |
|---|---|---|---|---|---|---|
| 1 | Tech & Internet | Communications/Electronics | $12,104,146 | 18.9% | 127 | MUSK, ELON (incl. Elon Musk Revoca $10,000,000; GEBBIA, JOSEPH $1,000,000; GEBBIA, JOSEPH $274,300 |
| 2 | **Oil & Gas** | Energy & Natural Resources | $6,252,819 | 9.8% | 245 | SCHARBAUER, DOUGLAS (Midland; oil  $1,225,700; MCDONALD, JOHNNY (Lubbock oil prod $510,000; GORDY, RUSSELL (SG Interests; incl $350,000 |
| 3 | Candidate & Party Committees | Ideological/Single-Issue | $5,383,967 | 8.4% | 18 | SLF PAC $5,000,000; BUCKEYE VICTORY ACTION INC $250,000; NRSC $62,000 |
| 4 | Lawyers / Law Firms | Lawyers & Lobbyists | $3,236,654 | 5.1% | 414 | THOMAS J HENRY LAW PLLC $646,107; AZIZ, MUHAMMAD $293,000; AZIZ, MUHAMMAD $265,800 |
| 5 | Securities & Investment | Finance, Insurance & Real Estate | $2,396,696 | 3.7% | 237 | TROUTT, LISA $265,800; TROUTT, KENNY $265,800; DEASON, DOUGLAS $265,800 |
| 6 | Health Services & Pharmaceuticals | Health | $1,539,971 | 2.4% | 103 | KNUTZ, JONATHAN $1,100,000; LACORE, TERRY $100,000; EVEXIAS MANAGEMENT $100,000 |
| 7 | Ideological & Single-Issue Groups | Ideological/Single-Issue | $1,497,462 | 2.3% | 19 | MAHA ACTION PAC $1,000,000; PICK, JACKI $265,800; TZEDEK PAC $100,000 |
| 8 | Recreation / Live Entertainment | Misc Business | $1,491,766 | 2.3% | 18 | HEAVIN, GARY $500,000; JONES, JERRAL $350,000; JONES, JOHN $272,000 |
| 9 | Real Estate | Finance, Insurance & Real Estate | $1,304,206 | 2.0% | 379 | GABBAY, MAYA $120,000; MOAYEDI, MEHRDAD (Centurion Americ $100,000; ABBOTT, LAUREN $100,000 |
| 10 | Business Services & Associations | Misc Business | $973,379 | 1.5% | 99 | RYAN, GEORGE $234,400; GEO REENTRY SERVICES, LLC $200,000; FRANKLIN, LARRY $188,600 |
| 11 | Construction & Contractors | Construction | $709,676 | 1.1% | 164 | PAUL MCLAREN REVOCABLE TRUST $250,000; DACUS, TAYLOR $100,000; MCLAREN, PAUL $50,000 |
| 12 | Transportation & Rail | Transportation | $678,037 | 1.1% | 55 | MILTON, CHELSEY $500,000; MILTON, TREVOR $100,000; WILLIS, ROY $10,500 |
| 13 | Banking & Finance | Finance, Insurance & Real Estate | $650,340 | 1.0% | 154 | MARLING, ROBERT $225,000; MARLING, ROBERT $150,000; SINGLETON, MARVIN $15,000 |
| 14 | Manufacturing & Industry | Misc Business | $578,288 | 0.9% | 62 | MCCORVEY, TONY $270,800; SORKIN, FELIX $150,000; LEDWELL, STEVE $31,500 |
| 15 | Hospitals & Nursing Homes | Health | $562,763 | 0.9% | 40 | BLAKE, GARY $274,000; CARROLLTON REGIONAL MEDICAL CENTER $150,000; BLAKE, GARY $100,000 |
| 16 | Lobbyists & Consultants | Lawyers & Lobbyists | $560,786 | 0.9% | 270 | VARMA, SAMIT $97,740; LINDSEY, RUSSELL $25,000; FRINZI, JAMES $14,000 |
| 17 | Health Professionals | Health | $558,229 | 0.9% | 330 | U S ANESTHESIA PARTNERS, INC PAC D $75,000; THOMAS, SUCHMOR $50,000; NOSNIK, PEDRO $20,000 |
| 18 | Retail, Food & Beverage | Misc Business | $362,800 | 0.6% | 46 | DYER, DON $75,000; DYER, DON $75,000; AUNG, KATIE $71,000 |
| 19 | Energy, other | Energy & Natural Resources | $352,144 | 0.5% | 106 | SAGO ENERGY LP $100,000; ROWLING, ROBERT $100,000; CASH, CLAY $14,000 |
| 20 | Insurance | Finance, Insurance & Real Estate | $340,301 | 0.5% | 80 | FAIRLY, ALEX (via Texas Republican $274,300; PHILLIPS, BRADFORD $10,000; STERLING, DAVID $6,500 |
| 21 | Ranching & Agriculture | Agribusiness | $304,159 | 0.5% | 216 | BANKS, KENNETH $50,000; LODGE, JOHN $11,000; FIGUEROA, TIM $10,000 |
| 22 | Car Dealers | Transportation | $224,687 | 0.4% | 51 | LOBB, LAWRENCE $100,000; DURANT, JERRY $14,100; LOBB, LAWRENCE $14,000 |
| 23 | Home Builders | Construction | $165,300 | 0.3% | 27 | BOWLING, RANDALL $50,000; BOWLING, ROBERT $25,000; BOWLING, RANDALL $25,000 |
| 24 | Education & Nonprofits | Other | $132,018 | 0.2% | 121 | SUTTON, JOSEPH $25,000; ELDRED, KEN $8,000; CURRAN, ISABEL $7,000 |
| 25 | Casinos / Gambling | Misc Business | $100,588 | 0.2% | 4 | TRIBE OF TEXAS $100,000; LAWSON, ARTHUR $260; PYDO, BARBARA $250 |
| 26 | Telecom & Media | Communications/Electronics | $32,822 | 0.1% | 19 | GALICOT, GREGORIO $10,360; BOWLING, PATTY $7,000; CHRISTENSON, MICHAEL $3,500 |
| 27 | Labor | Labor | $1,389 | 0.0% | 3 | CHOAT, CHRISTOPHER $1,041; MCCREIGHT, ANDREW $208; FUNK, LOUIS $140 |
| - | Unitemized (FEC) | Not identified | $6,075,477 | 9.5% | 3 | |
| - | Retired or Homemaker (employer not given) | Not identified | $7,663,661 | 12.0% | 10900 | |
| - | Not identified | Not identified | $7,828,646 | 12.2% | 3267 | |

By sector: Not identified 33.7%; Communications/Electronics 18.9%; Ideological/Single-Issue 10.7%; Energy & Natural Resources 10.3%; Finance, Insurance & Real Estate 7.3%; Lawyers & Lobbyists 5.9%; Misc Business 5.5%; Health 4.2%; Transportation 1.4%; Construction 1.4%; Agribusiness 0.5%; Other 0.2%; Labor 0.0%

## Caveats

- The industry of a donor is the industry of the money's source as best stated: a family office or trust takes the industry of the fortune behind it when a hand ruling says so; otherwise its filed employer.
- Keyword calls (`decided_by` keyword or basis) were not hand-checked donor by donor. Hand rulings cite their basis.
- Committees that pass money through (PACs, joint committees, other candidates) are ranked as their own kind, not traced to their donors, except where a hand ruling names the funder.
- Oil & Gas here is the final strict tier. "Energy, other" is the broad tier minus strict: utilities, power and diversified energy fortunes.
- Labels checked on 2026-10-30 against OpenSecrets' Industries by Sector page (https://www.opensecrets.org/industries/slist), saved as `raw/opensecrets_industries_by_sector_2026-10-30.txt`. Our sectors are theirs; candidate committees sit in Ideological/Single-Issue as OpenSecrets files them. Where one of our industries spans several of theirs, the table below says which.
- Our Oil & Gas is broader than OpenSecrets' Oil & Gas industry: it adds natural-gas pipelines (a separate OpenSecrets industry) and, by Saul's 2026-10-29 ruling, petrochemical makers and fuel distribution. Narrowed to OpenSecrets' definition, Abbott's oil share falls from 16.8% to roughly 11.5-12.7% (midstream donors Kelcy Warren, Jan Duncan, Nancy Kinder), still above Securities & Investment at 9.5%. Patrick falls to roughly 14.3%, still first. The range reflects donors whose OpenSecrets code was not checked one by one.

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
