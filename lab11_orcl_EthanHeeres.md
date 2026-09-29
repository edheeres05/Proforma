# Lab 11 — Oracle pro-forma sensitivity

Ethan D. Heeres | FIN 439

Run timestamp (UTC): 2026-09-29T20:55:11.082433+00:00


## Question

Which assumptions drive Oracle's forecast and value, and what explains their effects?

## Model and comparison

Source: the unchanged Lab 10 `orcl_proforma.py`. Both drivers affect FY2027–FY2031. Growth uses a constant percentage-point shift to each annual growth rate; capital spending uses a constant percentage change to each year's spending amount. The range widths and reasons are student inputs, not chosen by this program.

Outputs: FY2031 operating profit and signed FCFE, both in USD millions. FCFE = CFO − capex + planned new term debt − principal repayments − preferred dividends. It excludes common dividends, new common-equity proceeds, and discretionary revolver movements.

Value per share: Unavailable. Lab 10's primary valuation discards negative forecast FCFE; Lab 11 retains signed FCFE. Its terminal refinancing and replacement-spending assumptions have not been resolved into a defensible normalized terminal year. No new terminal value or discount-rate assumption is introduced.

## Verified base

| Output (USD millions) | FY2027 | FY2028 | FY2029 | FY2030 | FY2031 |
|---|---:|---:|---:|---:|---:|
| Operating profit | 30,263.0248 | 35,166.9372 | 43,064.5567 | 52,137.1599 | 59,936.4607 |
| Signed FCFE | -33,068.2862 | -74.2828 | 1,300.8723 | 10,383.1330 | 21,777.5260 |
| Cash | 12,082.2418 | 10,000.0000 | 10,000.0000 | 10,000.0000 | 21,092.1725 |
| Revolver | 0.0000 | 4,039.5130 | 8,848.5893 | 4,575.4049 | 0.0000 |

All original independent assumptions and full statements are retained in the JSON evidence and text output.

## Input ranges and results

| Driver / case | Actual FY2027–FY2031 input path | Units | FY2031 operating profit | Change from base | FY2031 signed FCFE | Change from base | Status |
|---|---|---|---:|---:|---:|---:|---|
| growth / lower | 31.616402%, 23.000000%, 18.000000%, 13.000000%, 8.000000% | Annual growth % | 53,063.8591 | -6,872.6016 | 16,700.9456 | -5,076.5804 | INVALID; diagnostic only |
| growth / base | 33.616402%, 25.000000%, 20.000000%, 15.000000%, 10.000000% | Annual growth % | 59,936.4607 | +0.0000 | 21,777.5260 | +0.0000 | PASS |
| growth / higher | 35.616402%, 27.000000%, 22.000000%, 17.000000%, 12.000000% | Annual growth % | 67,281.5518 | +7,345.0911 | 27,097.5816 | +5,320.0556 | PASS |
| capex / lower | 83,250.00, 63,000.00, 45,000.00, 36,000.00, 36,000.00 | USD millions | 61,868.4047 | +1,931.9439 | 25,190.6592 | +3,413.1332 | PASS |
| capex / base | 92,500.00, 70,000.00, 50,000.00, 40,000.00, 40,000.00 | USD millions | 59,936.4607 | +0.0000 | 21,777.5260 | +0.0000 | PASS |
| capex / higher | 101,750.00, 77,000.00, 55,000.00, 44,000.00, 44,000.00 | USD millions | 58,004.5168 | -1,931.9439 | 18,319.1310 | -3,458.3950 | INVALID; diagnostic only |

Range reason for growth: Judgment: a sustained two-percentage-point annual deviation tests a modest difference in cloud demand and the timing of converting contracts into revenue while preserving the slowing-growth pattern. This is a chosen scenario range, not company guidance or a probability interval.

Range reason for capex: Judgment: a ten-percent change tests uncertainty in data-center build costs, replacement needs, and the investment required to support the forecast, while preserving the original spending pattern. This is a chosen scenario range, not company guidance or a probability interval.

Output changes are changed output minus the first base, calculated before rounding. Invalid rows are retained for diagnosis and excluded from spans and rankings. Value/share and its change are unavailable in every run.

| Driver | Usable scenarios | Operating-profit span ($m) | Signed-FCFE span ($m) |
|---|---:|---:|---:|
| growth | 2/3 | 7,345.0911 | 5,320.0556 |
| capex | 2/3 | 1,931.9439 | 3,413.1332 |

Full-range ranking withheld: at least one scenario is invalid. Partial spans above cover only usable results and cannot establish the requested full-range ranking.

## Base check

Restored base after changed runs: PASS
Maximum absolute difference across all statement cells: 0 USD millions (tolerance 1e-06).
Same input set: True. Original model inputs unchanged: True.

## Checks for every run

| Run | Usable | Largest absolute accounting gap ($m) | Issues |
|---|---|---:|---|
| Base before analysis | PASS | 7.27595761418e-11 | None |
| growth / lower | INVALID | 8.73114913702e-11 | FY2029: cash floor failed; FY2030: cash floor failed; FY2029: cash floor gap = -1,939.552296 million; financing unavailable |
| growth / base | PASS | 7.27595761418e-11 | None |
| growth / higher | PASS | 8.73114913702e-11 | None |
| capex / lower | PASS | 4.0017766878e-11 | None |
| capex / base | PASS | 7.27595761418e-11 | None |
| capex / higher | INVALID | 8.73114913702e-11 | FY2028: cash floor failed; FY2029: cash floor failed; FY2030: cash floor failed; FY2031: cash floor failed; FY2028: cash floor gap = -10,280.612504 million; financing unavailable |
| Restored base | PASS | 7.27595761418e-11 | None |

The text output lists every year and every accounting gap, cash floor, and revolver limit. The JSON retains each run's independent inputs, all statement lines, and all checks.

## Locked prediction and reconciliation

The following higher-growth prediction was recorded before the changed-input sensitivity run and was not revised after seeing the results.

Recorded at: 2026-09-29T16:53:07.498015-04:00
Driver: growth
Case: higher
Old values: FY2027–FY2031 annual growth = 33.61640216%, 25.00000000%, 20.00000000%, 15.00000000%, 10.00000000%.
New values: FY2027–FY2031 annual growth = 35.61640216%, 27.00000000%, 22.00000000%, 17.00000000%, 12.00000000%; +2 percentage points in every year. Capex and all other independent assumptions stay at base.
Expected direction: Higher FY2031 operating profit and higher signed FCFE.
Rough size: Operating profit +10.408080% versus original FY2031 base; FCFE +21.665290% versus original FY2031 base. These implement the original estimates as discussed: 1.02^5 - 1 and 1.04^5 - 1, not new growth inputs in the model. Predicted profit = 66,174.6957 USD million (base 59,936.4607); predicted FCFE = 26,495.6902 USD million (base 21,777.5260).
Reason: Ethan expects continued cloud adoption and Oracle's position in cloud services to support higher revenue and profits. The comparison isolates higher revenue growth while all other independent assumptions remain at base. This is a pre-run judgment, not a model result.
Range and unit check used in the completed analysis: revenue growth changes are measured in percentage points, capex changes are measured as percent changes to spending, outputs are in USD millions, and the comparison covers FY2027–FY2031.

The later 7% profit / 13% FCFE estimate was withdrawn; Ethan asked to use the original estimates. The original Lab 10 forecast remains unchanged. Reconcile the actual result in the analysis report after running; do not rewrite the prediction after seeing results.


Saved prediction SHA-256: `9057466cef65443ce394b5952238d56e175e9939864fba4ff58351fa87787f5a`

Selected actual result: growth / higher; usable. Operating-profit change: +7,345.0911 million. Signed-FCFE change: +5,320.0556 million.

Student explanation of prediction error or agreement: **My prediction had the right direction but slightly understated the size of the change. I predicted FY2031 operating profit of $66,174.6957 million and FCFE of $26,495.6902 million. The actual higher-growth case produced operating profit of $67,281.5518 million and FCFE of $27,097.5816 million. That means operating profit was $1,106.8561 million above my prediction and FCFE was $601.8914 million above my prediction. The actual increases versus the base were 12.2548% for operating profit and 24.4291% for FCFE, compared with my predicted increases of 10.4081% and 21.6653%. My estimate was close, but the linked model produced a somewhat larger benefit from the higher revenue path than I expected.**

## Student interpretation and partner exchanges

- Main driver for operating profit and FCFE **over these ranges**, with actual numbers and a statement-by-statement explanation: **The full lower-to-higher ranking cannot be completed because the lower-growth case and higher-capex case fail the model's funding constraints, so I do not treat those endpoints as usable full-range results. Looking at the usable base-to-endpoint comparisons, revenue growth has the larger effect on both FY2031 operating profit and FCFE. The higher-growth case raises revenue by $14,690.1822 million, which increases gross profit by $11,017.6367 million. SG&A rises by $2,203.5273 million and R&D rises by $1,469.0182 million, but operating profit still increases by $7,345.0911 million. Pretax income rises by $7,642.4924 million, taxes rise by $1,375.6486 million, and net income rises by $6,266.8438 million. On the cash-flow statement, CFO rises by $5,320.0556 million while capex stays at $40,000 million, so signed FCFE also rises by $5,320.0556 million. By comparison, the valid lower-capex case raises operating profit by $1,931.9439 million and FCFE by $3,413.1332 million. Lower capex reduces depreciation, which raises gross profit and operating income, and it directly reduces investing cash outflow. This shows that growth is more influential in the usable comparisons, but the failed endpoints also show that funding capacity matters when growth is weaker or spending is higher.**
- Effect on valuation conclusion or research priority, including a reason if unchanged: **This sensitivity does not create a new value-per-share conclusion because the Lab 11 model does not use a defensible terminal-year valuation after keeping signed FCFE. It does change what I would research first. Revenue growth is the most important operating assumption in the usable comparisons, so I would focus on Oracle's cloud demand, backlog/contract conversion into revenue, and whether the high growth path can actually continue. I would also pay close attention to capital spending and financing capacity because the higher-capex case reaches the revolver limit and still falls below the cash floor.**
- Exchange 1: **Aidan Murrin; September 29, 2026. Aidan asked, “Which input do you expect to matter most?” I answered, “I expect growth to have a strong effect on operating profit because the revenue differences compound over five years. Capital spending could matter more for cash flow because it directly uses cash. I need the results before deciding which has the larger effect over these ranges.” After running the sensitivity, the usable comparisons showed that growth had the larger effect on both FY2031 operating profit and FCFE.**
- Exchange 2: **I checked Aidan's model by focusing on his revenue-growth assumption. I asked him why he chose 4% annual growth. He said he chose 4% as a moderate assumption and was not assuming that the company would continue growing at 8%. This helped show the difference between our models: his growth assumption was more moderate, while my Oracle sensitivity tests whether a higher cloud-driven revenue path could continue over the five-year forecast.**
- Exchange 3: **Aidan asked, “Do you think Oracle could realistically sustain the higher-growth scenario through 2031?” I said yes because more and more customers are using cloud products, so I expect Oracle's cloud business to continue expanding. That continued cloud adoption could support the higher revenue-growth path through 2031. I would still treat the higher-growth case as a sensitivity scenario rather than a guarantee. Compared with Aidan's model, Oracle's mechanism is more dependent on continued cloud expansion and the large capital spending needed to support that growth, while his revenue-growth assumption was intentionally more moderate.**
- Reflection: which result surprised me and why: **The result that surprised me most was that the higher-capex case became invalid even though FY2031 operating profit only fell by about $1.932 billion from the base. The bigger issue was financing and liquidity: the revolver reached its $10 billion limit and the model still fell below the minimum cash requirement. That showed me that an assumption can look manageable on the income statement but still create a major problem on the cash-flow statement and balance sheet. I was also surprised that the higher-growth case beat my original prediction by about $1.107 billion of operating profit and $0.602 billion of FCFE.**

