# Lab 10 — Pro-Forma: Oracle (ORCL)

**Ethan D. Heeres | FIN 439 | September 24, 2026**


All dollar amounts are **USD millions**, except per-share amounts. Share counts are in millions. Oracle's fiscal year ends May 31. FY2024–FY2026 are history; FY2027–FY2031 are projections.

## Reopen and rerun

The existing `proforma.py` was run and matched the Lab 09 ABG known answer: value per share **$291.75**, FY2026 cash **101.8**, FY2030 cash **719.8**, and zero balance-sheet gaps in all five years. Its break test refused valuation with the required FY2026 gap of **−61.4**. These are computational checks performed for this draft, not a claim about a partner's computer.

Save `orcl_proforma.py` and this Markdown file in the Course/Work Folder. Keep the original ABG file.

```bash
python proforma.py
python orcl_proforma.py
```

## D — the question, the same for everyone

**What are five years of your company's statements worth, built from assumptions you can defend?**

My company is **Oracle Corporation (NYSE: ORCL)**.

**The line that makes Oracle different:** Oracle's AI cloud expansion requires substantial data-center capital spending before the related revenue is fully earned, so my model connects that investment to PP&E, depreciation, customer prepayments, and borrowing.

ABG's inventory floor-plan financing does not fit Oracle. My replacement is **data-center investment and customer funding**. PP&E rises with capital spending and falls with depreciation; customer advances create deferred revenue rather than immediate profit. New term debt and the revolver fund remaining cash needs.

Initial partner question about this line: **[Record the actual question after discussing it.]**

## R — the history, then the assumptions

### Sources and how to find the numbers

| ID | Filing or source | Locations used |
| --- | --- | --- |
| [F24][F24] | Oracle FY2024 10-K; filed June 20, 2024 | Balance sheet p. 65; operations p. 66; cash flows p. 69; Item 7 MD&A |
| [F25][F25] | Oracle FY2025 10-K; filed June 18, 2025 | Balance sheet p. 64; operations p. 65; cash flows p. 68; Item 7 MD&A |
| [F26][F26] | Oracle FY2026 10-K; filed June 22, 2026 | Balance sheet p. 64; operations p. 65; cash flows p. 68; Notes 1, 4, 5, 6, 8, 9, 10; Item 7 MD&A |
| [Q27][Q27] | Quarter ended August 31, 2026; filed September 11, 2026 | Cover share count as of September 7; common-stock note and equity statement for ATM proceeds |
| [G27][G27] | Oracle Q1 FY2027 results, September 10, 2026 | Full-year revenue guidance; Q1 capital spending; completed stock offering |
| [P][PROVIDER] | Stock Analysis annual cash-flow table, accessed September 24, 2026 | Capital Expenditures field; quote dated September 24, 4:00 PM EDT |

BS = consolidated balance sheet; IS = consolidated statement of operations; CF = consolidated statement of cash flows. Each historical cell below identifies its own filing. FY2026's comparative IS and CF also corroborate FY2024 and FY2025.

### Three-year history grid

| Item | FY2024 | FY2025 | FY2026 |
| --- | --- | --- | --- |
| Revenue | 52,961 ([F24][F24], IS) | 57,399 ([F25][F25], IS) | 67,357 ([F26][F26], IS) |
| Direct operating costs used below | 15,143 ([F24][F24], IS; calculation) | 16,927 ([F25][F25], IS; calculation) | 23,021 ([F26][F26], IS; calculation) |
| Gross profit, constructed | 37,818 ([F24][F24], IS; calculation) | 40,472 ([F25][F25], IS; calculation) | 44,336 ([F26][F26], IS; calculation) |
| SG&A, constructed | 9,822 ([F24][F24], IS; calculation) | 10,253 ([F25][F25], IS; calculation) | 9,949 ([F26][F26], IS; calculation) |
| Net income | 10,467 ([F24][F24], IS) | 12,443 ([F25][F25], IS) | 17,087 ([F26][F26], IS) |
| Inventory, standalone balance | Not separately disclosed; unresolved ([F24][F24], BS/notes reviewed) | Not separately disclosed; unresolved ([F25][F25], BS/notes reviewed) | Not separately disclosed; unresolved ([F26][F26], BS/notes reviewed) |
| PP&E, net | 21,536 ([F24][F24], BS) | 43,522 ([F25][F25], BS) | 99,957 ([F26][F26], BS) |
| Oracle parent shareholders’ equity | 8,704 ([F24][F24], BS) | 20,451 ([F25][F25], BS) | 42,508 ([F26][F26], BS) |
| Total consolidated equity, including NCI | 9,239 ([F24][F24], BS) | 20,969 ([F25][F25], BS) | 43,056 ([F26][F26], BS) |
| Depreciation | 3,129 ([F24][F24], CF) | 3,867 ([F25][F25], CF) | 7,623 ([F26][F26], CF) |
| Capital expenditures, cash outflow magnitude | 6,866 ([F24][F24], CF) | 21,215 ([F25][F25], CF) | 55,663 ([F26][F26], CF) |
| Pretax income | 11,741 ([F24][F24], IS) | 14,160 ([F25][F25], IS) | 19,554 ([F26][F26], IS) |
| Income-tax provision | 1,274 ([F24][F24], IS) | 1,717 ([F25][F25], IS) | 2,467 ([F26][F26], IS) |
| Operating cash flow | 18,673 ([F24][F24], CF) | 20,821 ([F25][F25], CF) | 31,977 ([F26][F26], CF) |

**Gross profit definition:** Oracle does not show a consolidated gross-profit subtotal. I calculate revenue less the cloud/software direct expense, hardware expense, and services expense lines. This follows Oracle's presentation of intangible amortization separately below those direct expenses; it is not necessarily a data provider's standardized gross profit. The arithmetic is:

- FY2024: 52,961 − (9,427 + 891 + 4,825) = **37,818**.
- FY2025: 57,399 − (11,569 + 782 + 4,576) = **40,472**.
- FY2026: 67,357 − (17,597 + 868 + 4,556) = **44,336**.

SG&A = sales and marketing + general and administrative. **R&D is separate**, not hidden in SG&A. Oracle changed its revenue presentation in FY2026; these consolidated direct-cost totals remain comparable.

Inventory is not zero just because it is not a standalone balance-sheet line. Its separate amount and inventory days remain unresolved. The model leaves any inventory embedded in prepaid/other current assets; it does not invent a balance or use ABG's inventory turnover.

### Two checks I must do myself

- [ ] Open **F26, p. 65, Total revenues**. Expected FY2026 value: **67,357 million**. My observed value: **[fill in]**. Date/initials: **[fill in]**.
- [ ] Open **F26, p. 68, Capital expenditures**. Expected FY2026 cash-flow entry: **(55,663) million**, meaning a cash outflow. My observed value: **[fill in]**. Date/initials: **[fill in]**.

These values were checked against the retrieved filing while preparing the model, but the boxes stay unchecked until I personally open the filing.

### Three-year ratio table

| Ratio | FY2024 [F24] | FY2025 [F25] | FY2026 [F26] | Formula / basis |
| --- | --- | --- | --- | --- |
| Gross margin | 71.41% | 70.51% | 65.82% | GP / revenue |
| SG&A / gross profit | 25.97% | 25.33% | 22.44% | (sales & marketing + G&A) / GP |
| Depreciation / year-end net PP&E | 14.53% | 8.89% | 7.63% | CF depreciation / BS net PP&E |
| Effective tax rate | 10.85% | 12.13% | 12.62% | tax provision / pretax income |
| Reported revenue growth | 6.02% | 8.38% | 17.35% | revenue / prior-year revenue − 1 |
| Constant-currency growth, as disclosed | 6.00% | 9.00% | 16.00% | MD&A; rounded by Oracle |
| Cash capex / revenue | 12.96% | 36.96% | 82.64% | cash capex magnitude / revenue |
| Inventory days | Unresolved | Unresolved | Unresolved | Would be inventory / direct costs × 365; standalone inventory unavailable |
| Organic / same-store growth | Not separately disclosed | Not separately disclosed | Not separately disclosed | Constant currency is not an acquisition-adjusted organic-growth measure |

The depreciation ratio uses **year-end** PP&E for historical calibration, matching the video's convention. In the forecast, the chosen forward rate applies to **opening** PP&E. They are different denominators and should not be silently interchanged.

### Filing capital spending beside the provider field

| Fiscal year | Filing CF, signed cash outflow | Stock Analysis “Capital Expenditures,” signed | Difference after matching units and sign |
| --- | ---: | ---: | ---: |
| 2024 | −6,866 [F24] | −6,866 [P] | 0 |
| 2025 | −21,215 [F25] | −21,215 [P] | 0 |
| 2026 | −55,663 [F26] | −55,663 [P] | 0 |

Both columns are USD millions. The model stores capex as a positive spending amount and subtracts it in investing cash flow. These are **annual** columns, not the provider's TTM column. Cash capex is not the full change in PP&E: unpaid purchases, finance leases, depreciation, and other noncash changes can cause differences. Future unpaid purchases and new finance leases are held flat in this simplified purchased-capacity scenario.

Historical operating cash flow minus capex was **11,807** in FY2024, **−394** in FY2025, and **−23,686** in FY2026. That is reported-style FCF, not the model's FCFE after debt flows and preferred dividends.

### Labelled assumption set

Each row below has the requested three columns: **value, label, reason**. The assumption name is included in the value cell. Every projected policy, including a decision to hold something constant or at zero, is a judgment unless explicitly identified otherwise.

| Value / assumption | Label | Reason |
| --- | --- | --- |
| Opening balances: FY2026; see reconciliation below | history | I start from the last completed fiscal year rather than substituting ABG balances. [F26] |
| FY2027 revenue: 90,000; growth 33.6164% | guidance | Oracle guides to at least $90 billion; I use the stated lower bound, not a promise that the outcome is certain. [G27] |
| FY2028–FY2031 revenue growth: 25%, 20%, 15%, 10% | judgment | I expect cloud capacity to support strong growth initially, but I step it down as the revenue base gets larger. Slower contract conversion would make me lower this path. |
| Gross contribution before PP&E depreciation: 75% of revenue each year | judgment | The FY2026 constructed GP plus total depreciation is about 77.14% of revenue. I use 75% to allow for a lower-margin cloud mix; this is a modeling approximation because not all historical depreciation necessarily sits in direct costs. |
| Allocate modeled PP&E depreciation entirely to direct costs | judgment | Data-center equipment is central to delivery costs. I subtract its depreciation once before calculating SG&A, rather than subtracting it again from an already depreciated margin. |
| SG&A / gross profit after depreciation: 22%, 21%, 20%, 20%, 20% | judgment | FY2026 was 22.44%. I allow modest operating leverage, but stop the improvement at 20% because selling and administrative work will not disappear. |
| R&D / revenue: 12%, 11.5%, 11%, 10.5%, 10% | judgment | R&D was 10,272 / 67,357 = 15.25% in FY2026. I assume revenue initially grows faster than R&D, while the dollars spent on development still grow; weak product demand would challenge this. |
| Depreciation / opening net PP&E: 12% | judgment | FY2026’s 7.63% ratio is depressed by a rapidly expanding year-end asset base. I move toward FY2024’s 14.53% as more installed equipment enters service; this is not a disclosed useful-life estimate. |
| Intangible amortization: 731, 694, 620, 582, 377 | guidance | These are management’s estimated future amortization expenses in the FY2026 intangible-assets note. No new acquired intangibles are assumed. [F26, Note 5] |
| Cash restructuring expense: 1,500, 750, 500, 0, 0; impairment: 0 | judgment | I let the FY2026 restructuring burden wind down over three years. I assume the forecast charges are cash expenses, so I do not add them back as impairment. |
| Gross cash capex: 92,500, 70,000, 50,000, 40,000, 40,000 | judgment | Q1 FY2027 cash capex was 28,499, versus 55,663 for all FY2026. I assume an intense first year followed by slower additions as capacity comes online; the exact path is my scenario, not a five-year company forecast. It must fall only if demand can be served with less new investment. [Q27; F26] |
| Tax rate: 18%; no tax benefit on a pretax loss | judgment | This is above the 10.85%–12.62% annual historical effective rates. I do not assume all recent tax benefits repeat as profits grow; cash and book tax are equal in this simplified forecast. |
| Receivables / revenue: 10,385 / 67,357; prepaid/other current assets / revenue: 4,288 / 67,357 | history | I use the exact FY2026 ratios, 15.42% and 6.37%, as the historical calibration. [F26, BS] |
| Apply those two operating-asset ratios unchanged to future revenue | judgment | I assume collection timing and prepaid-asset intensity remain stable. A shift in billing or collections would require changing them. |
| Inventory / floor plan: no separate modeled inventory or inventory loan | judgment | Oracle’s filings do not support an ABG-style inventory-loan ratio. Any inventory remains inside the reported asset grouping; the absence of a separate row does not establish zero inventory. |
| Net customer cash advances less revenue recognition: +20,000, +15,000, +5,000, −5,000, 0 | judgment | Large prepaid cloud contracts help fund capacity. I assume receipts exceed recognition at first, then recognition catches up; I stop the net runoff by FY2031 rather than extending a finite liability runoff forever. This is a net movement, not total collections or immediate revenue. |
| Ordinary deferred-revenue baseline: 10,733 | history | This was total deferred revenue at FY2025 year-end. [F26, Note 8, comparative column] |
| Keep that baseline fixed; accrue 5% on opening deferred revenue above it | judgment | I use the excess over the FY2025 base as a rough proxy for customer financing and charge for its time value. This proxy is not Oracle’s disclosed financed balance or contract-level interest schedule; the historical financing component was immaterial. [F26, Note 1] |
| New term borrowing: 20,000, 25,000, 0, 0, 0 | judgment | The data-center build cannot be funded by modeled operations alone. My original 15,000 FY2028 borrowing case failed the cash floor, so this case explicitly assumes 10,000 more term funding; it depends on lender access and is not committed borrowing. |
| Existing note/other-borrowing principal: 7,210, 10,145, 5,500, 7,250, 9,750 | history | These are the disclosed five-year principal maturities. They are applied to the opening debt balance, not copied from ABG. [F26, Note 6] |
| Finance-lease principal: 620, 600, 600, 600, 600; total modeled repayments: 7,830, 10,745, 6,100, 7,850, 10,350 | judgment | 620 is the FY2026 current finance-lease liability; the later 600 amounts are rounded approximations. I assume new term borrowing matures after FY2031. Finance-lease and note principal are kept distinct when forming the total. [F26, Note 9] |
| Debt interest: 4.5%; revolver interest: 6.5%; opening balances | judgment | These are blended scenario rates, not quoted coupons. I give short-term credit a higher rate and use opening balances to preserve the course engine’s noncircular order; in-year borrowing interest is simplified. |
| Cash floor: 10,000 | judgment | I want a liquidity reserve close to Oracle’s FY2024–FY2025 cash balances. This is a chosen operating buffer, not a covenant. |
| Revolver limit: 10,000; opening draw: 0 | history | The FY2026 filing discloses a $10 billion facility and no outstanding borrowings. [F26, Note 6] |
| Revolver policy: borrow only for cash shortfall; repay surplus first; assume covenant access | judgment | I do not increase the facility to make the model pass. I assume any FY2031 repayment occurs before its March 6 maturity; this annual model does not verify monthly liquidity or the contractual EBITDA covenant. |
| Completed common equity proceeds in FY2027: 19,909 | history | This is the completed ATM issuance net of costs in Q1 FY2027. The new money increases cash and equity, never revenue. [Q27, equity statement] |
| Further common equity offerings after the completed ATM: 0 | judgment | I assume no further offering is needed beyond the completed program and the stated debt funding. If funding access weakens, another offering and additional dilution would need to be modeled. |
| Current common shares: 3,023.736 million | history | Use the September 7, 2026 10-Q cover count, which includes the recent offering; do not use FY2026 weighted-average shares. [Q27] |
| Preferred conversion: add 31.238285 million common shares in FY2029 | judgment | I assume the disclosed maximum conversion rate, 624.7657 shares times 0.05 million preferred shares, on January 15, 2029. That makes later shares 3,054.974285 million and conservatively allows for dilution; actual conversion depends on the contract and future price. [F26, Note 10] |
| Preferred cash dividends: 325, 325, 203.125, 0, 0 | judgment | The 6.5% rate on $5,000 million liquidation preference is historical. I assume cash payment and approximate FY2029 as 7.5 months before conversion; no preferred dividend remains in the terminal period. [F26, Note 10] |
| Common dividends: $2.00 per share per year; share repurchases: 0 | judgment | I hold the current $0.50 quarterly rate constant and stop discretionary buybacks while funding the build. I use each year-end modeled share count for the whole-year cash dividend as a conservative timing simplification. [Q27] |
| Treat employee compensation as a cash-equivalent expense; no SBC add-back or future employee dilution | judgment | I avoid treating share compensation as free cash while also holding employee-related shares fixed. This is a simplified economic replacement-cost treatment, not a forecast of reported GAAP stock compensation. |
| Other assets 112,611; other liabilities 66,066: held flat; no acquisitions, disposals, OCI, new leases, or investment gains; NCI earnings/distributions 0 | judgment | I isolate the investment driver and operating-asset changes rather than invent detailed schedules. Existing operating-lease rent stays inside operating cost assumptions; existing lease balances stay in the other groupings. Oracle’s nonrecurring FY2026 investment gain is not repeated. These simplifications limit precision. |
| Cost of equity: 12%; terminal growth: 3% | judgment | I require a return above the ABG example’s 10% because this scenario carries funding and execution risk. I use 3% long-run cash-flow growth rather than continuing double-digit near-term growth; 12% exceeds 3%. |
| Terminal debt principal is refinanced; FY2031 repayment is added back before perpetuity | judgment | This follows Lab 09’s terminal convention. It assumes continued refinancing with interest expense retained, not debt forgiveness; it is a reduced-form steady-state cash-flow assumption rather than a full perpetual balance sheet. |
| Exclude negative annual FCFE from the primary PV; show signed alternative | judgment | I follow the explicit Lab 10 classroom instruction, but retain funding deficits in the statements and disclose that excluding them raises the indicated value. |
| Annual end-of-year discounting, t = 1 to 5 from May 31, 2026; no separate opening-cash addition | judgment | I preserve the annual course convention. The September quote comparison is a classroom comparison, not an exact-date valuation with a completed-quarter/stub-period bridge. |
| Market price: $139.52, September 24, 2026, 4:00 PM EDT close | history | This is the dated quote shown by the cited provider, not a forecast or an unlabeled live price. [P] |

**Practice attack:** “Why does capex fall from $92.5 billion to $40 billion while revenue grows to $170.8 billion, and what evidence would make you keep spending higher?”

**Two-sentence answer:** I assume the large early build creates capacity that later revenue can use, so capital spending can slow even as revenue continues to grow. I would keep capex higher or reduce revenue if capacity utilization, equipment replacement needs, or Oracle’s spending updates showed that the projected revenue required more new infrastructure.

### Opening balance sheet and mapping

Every balance comes from F26, with the note-based reclassifications shown. No plug is added to make the opening balance sheet work.

| Opening FY2026 balance | Amount | Source / reconciliation |
| --- | --- | --- |
| Cash | 31,289 | BS |
| Trade receivables | 10,385 | BS |
| Prepaid/other current assets | 4,288 | BS |
| PP&E, net | 99,957 | BS |
| Intangibles, net | 3,229 | Note 5; separated from other noncurrent assets |
| Other assets | 112,611 | 261,759 − 31,289 − 10,385 − 4,288 − 99,957 − 3,229 |
| TOTAL ASSETS | 261,759 | BS |
| Debt including finance leases | 137,242 | 7,199 current notes + 122,342 noncurrent notes + 7,701 finance leases |
| Revolver | 0 | Note 6 |
| Deferred revenue / customer funding | 15,395 | 9,916 current + 5,479 noncurrent, Note 8 |
| Other liabilities | 66,066 | 218,703 total liabilities − 137,242 debt/leases − 15,395 deferred revenue |
| TOTAL LIABILITIES | 218,703 | 41,764 current + 176,939 noncurrent |
| Common parent equity | 37,554 | 42,508 parent equity − 4,954 preferred |
| Preferred equity | 4,954 | BS; issue costs make carrying value differ from 5,000 liquidation preference |
| Noncontrolling interests | 548 | BS |
| TOTAL EQUITY | 43,056 | BS |
| TOTAL LIABILITIES + EQUITY | 261,759 | 218,703 + 43,056 |

Finance-lease liabilities are reclassified out of other current/noncurrent liabilities into debt. Deferred revenue includes its current and noncurrent portions. Operating lease ROU assets and related liabilities remain inside the other-asset and other-liability groupings. These are reclassifications, not additional assets or liabilities.

## I — your company through the engine

The new file uses only Python's standard library. Calculation order remains the course order: income statement, noncash balance-sheet balances, cash flows, financing, then cash. The main adaptations are R&D, intangible amortization, explicit cloud investment, customer funding, preferred dividends/conversion, and the completed common-stock issue.

Gross profit is computed **after one depreciation charge**. Cash is computed from operating, investing, and financing cash flows, never typed to balance the balance sheet. Net customer advances increase deferred revenue; they do not increase net income by themselves. Noncash customer financing interest reduces earnings, is added back to CFO, and increases deferred revenue.

The forecast starts with FY2026 audited balances. Q1 FY2027 is used for the known equity raise, shares and updated guidance, but is not reconstructed as a separate actual quarter; FY2027 remains a full-year classroom forecast.

### Income Statement

| USD millions | FY2027E | FY2028E | FY2029E | FY2030E | FY2031E |
| --- | --- | --- | --- | --- | --- |
| Revenue | 90,000.0 | 112,500.0 | 135,000.0 | 155,250.0 | 170,775.0 |
| Direct costs excluding depreciation | 22,500.0 | 28,125.0 | 33,750.0 | 38,812.5 | 42,693.8 |
| Gross profit before depreciation | 67,500.0 | 84,375.0 | 101,250.0 | 116,437.5 | 128,081.2 |
| Depreciation in direct costs | 11,994.8 | 21,655.5 | 27,456.8 | 30,162.0 | 31,342.5 |
| Gross profit after depreciation | 55,505.2 | 62,719.5 | 73,793.2 | 86,275.5 | 96,738.7 |
| SG&A | 12,211.1 | 13,171.1 | 14,758.6 | 17,255.1 | 19,347.7 |
| Research and development | 10,800.0 | 12,937.5 | 14,850.0 | 16,301.2 | 17,077.5 |
| Intangible amortization | 731.0 | 694.0 | 620.0 | 582.0 | 377.0 |
| Restructuring (cash expense) | 1,500.0 | 750.0 | 500.0 | 0.0 | 0.0 |
| Operating income | 30,263.0 | 35,166.9 | 43,064.6 | 52,137.2 | 59,936.5 |
| Debt and revolver interest | 6,175.9 | 6,723.5 | 7,627.6 | 7,665.7 | 7,034.7 |
| Customer financing accretion | 233.1 | 1,244.8 | 2,057.0 | 2,409.8 | 2,280.3 |
| Pretax income | 23,854.0 | 27,198.6 | 33,380.0 | 42,061.6 | 50,621.5 |
| Income tax | 4,293.7 | 4,895.8 | 6,008.4 | 7,571.1 | 9,111.9 |
| Net income | 19,560.3 | 22,302.9 | 27,371.6 | 34,490.5 | 41,509.6 |

### Balance Sheet

| USD millions | FY2027E | FY2028E | FY2029E | FY2030E | FY2031E |
| --- | --- | --- | --- | --- | --- |
| Cash | 12,082.2 | 10,000.0 | 10,000.0 | 10,000.0 | 21,092.2 |
| Trade receivables | 13,876.1 | 17,345.1 | 20,814.1 | 23,936.2 | 26,329.8 |
| Prepaid / other current assets | 5,729.5 | 7,161.8 | 8,594.2 | 9,883.3 | 10,871.7 |
| PP&E, net | 180,462.2 | 228,806.7 | 251,349.9 | 261,187.9 | 269,845.4 |
| Intangibles, net | 2,498.0 | 1,804.0 | 1,184.0 | 602.0 | 225.0 |
| Other assets | 112,611.0 | 112,611.0 | 112,611.0 | 112,611.0 | 112,611.0 |
| Total assets | 327,258.9 | 377,728.6 | 404,553.2 | 418,220.5 | 440,975.0 |
| Debt, including finance leases | 149,412.0 | 163,667.0 | 157,567.0 | 149,717.0 | 139,367.0 |
| Revolver | 0.0 | 4,039.5 | 8,848.6 | 4,575.4 | 0.0 |
| Deferred revenue / customer funding | 35,628.1 | 51,872.9 | 58,929.8 | 56,339.7 | 58,620.0 |
| Other liabilities | 66,066.0 | 66,066.0 | 66,066.0 | 66,066.0 | 66,066.0 |
| Total liabilities | 251,106.1 | 285,645.4 | 291,411.4 | 276,698.1 | 264,053.0 |
| Common parent equity | 70,650.8 | 86,581.3 | 112,593.8 | 140,974.4 | 176,374.0 |
| Preferred equity | 4,954.0 | 4,954.0 | 0.0 | 0.0 | 0.0 |
| Noncontrolling interests | 548.0 | 548.0 | 548.0 | 548.0 | 548.0 |
| Total equity | 76,152.8 | 92,083.3 | 113,141.8 | 141,522.4 | 176,922.0 |
| Total liabilities and equity | 327,258.9 | 377,728.6 | 404,553.2 | 418,220.5 | 440,975.0 |

### Cash Flow Statement

| USD millions | FY2027E | FY2028E | FY2029E | FY2030E | FY2031E |
| --- | --- | --- | --- | --- | --- |
| Net income | 19,560.3 | 22,302.9 | 27,371.6 | 34,490.5 | 41,509.6 |
| + Depreciation | 11,994.8 | 21,655.5 | 27,456.8 | 30,162.0 | 31,342.5 |
| + Intangible amortization | 731.0 | 694.0 | 620.0 | 582.0 | 377.0 |
| + Noncash customer financing interest | 233.1 | 1,244.8 | 2,057.0 | 2,409.8 | 2,280.3 |
| - Change in operating assets | -4,932.5 | -4,901.4 | -4,901.4 | -4,411.2 | -3,382.0 |
| Net cash advances / (recognition) | 20,000.0 | 15,000.0 | 5,000.0 | -5,000.0 | 0.0 |
| Cash from operations | 47,586.7 | 55,995.7 | 57,604.0 | 58,233.1 | 72,127.5 |
| Investing cash flow: gross capex | -92,500.0 | -70,000.0 | -50,000.0 | -40,000.0 | -40,000.0 |
| New term debt | 20,000.0 | 25,000.0 | 0.0 | 0.0 | 0.0 |
| Debt / finance lease principal | -7,830.0 | -10,745.0 | -6,100.0 | -7,850.0 | -10,350.0 |
| Common equity proceeds | 19,909.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Common dividends | -6,047.5 | -6,047.5 | -6,109.9 | -6,109.9 | -6,109.9 |
| Preferred dividends | -325.0 | -325.0 | -203.1 | 0.0 | 0.0 |
| Revolver draw / (repayment) | 0.0 | 4,039.5 | 4,809.1 | -4,273.2 | -4,575.4 |
| Cash from financing | 25,706.5 | 11,922.0 | -7,604.0 | -18,233.1 | -21,035.4 |
| Change in cash | -19,206.8 | -2,082.2 | 0.0 | 0.0 | 11,092.2 |
| Opening cash | 31,289.0 | 12,082.2 | 10,000.0 | 10,000.0 | 10,000.0 |
| Closing cash | 12,082.2 | 10,000.0 | 10,000.0 | 10,000.0 | 21,092.2 |
| FCFE before any new debt | -53,068.3 | -25,074.3 | 1,300.9 | 10,383.1 | 21,777.5 |
| FCFE incl. term debt; before revolver | -33,068.3 | -74.3 | 1,300.9 | 10,383.1 | 21,777.5 |
| FCFE including revolver | -33,068.3 | 3,965.2 | 6,109.9 | 6,109.9 | 17,202.1 |

### FCFE definition and negative years

`FCFE = CFO − gross cash capex + planned new term debt − principal repayments − preferred dividends`.

This is before common dividends, new common-equity proceeds, and discretionary revolver movements. The output also prints FCFE before all new borrowing and FCFE after revolver movements. Borrowing is a financing flow, not operating revenue. The primary convention excludes the revolver from valuation, following the course engine's liquidity treatment.

| Year | FCFE before revolver | Treatment in primary PV |
| --- | --- | --- |
| FY2027 | -33,068.3 | **Negative FCFE** — zero valued |
| FY2028 | -74.3 | **Negative FCFE** — zero valued |
| FY2029 | 1,300.9 | Positive FCFE — discounted |
| FY2030 | 10,383.1 | Positive FCFE — discounted |
| FY2031 | 21,777.5 | Positive FCFE — discounted |

A terminal value based on a perpetually negative cash flow is not a meaningful positive going-concern value: the company would need a supported path to positive distributable cash first. The code refuses a terminal valuation if the final modeled FCFE is zero or negative.

## V — the check block, and the price

### Accounting and liquidity checks

| Check, USD millions | FY2027 | FY2028 | FY2029 | FY2030 | FY2031 |
| --- | --- | --- | --- | --- | --- |
| balance sheet | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| cash-flow link | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| cash movement | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| funding cash link | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| PP&E roll-forward | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| intangible roll-forward | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| debt roll-forward | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| deferred revenue roll-forward | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| equity roll-forward | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| FCFE link | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |

| USD millions | FY2027E | FY2028E | FY2029E | FY2030E | FY2031E |
| --- | --- | --- | --- | --- | --- |
| Cash | 12,082.2 | 10,000.0 | 10,000.0 | 10,000.0 | 21,092.2 |
| Cash floor | 10,000.0 | 10,000.0 | 10,000.0 | 10,000.0 | 10,000.0 |
| Cash above floor | 2,082.2 | 0.0 | 0.0 | 0.0 | 11,092.2 |
| Revolver outstanding | 0.0 | 4,039.5 | 8,848.6 | 4,575.4 | 0.0 |
| Revolver draw / (repayment) | 0.0 | 4,039.5 | 4,809.1 | -4,273.2 | -4,575.4 |

The accounting check block is zero in every year; **cash above the floor is an inequality, not a gap that must equal zero**. FY2028 draws **4,039.5** and FY2029 draws **4,809.1** because investment, principal repayments and dividends exceed cash available after planned financing. The balance peaks at **8,848.6**, below the actual **10,000** limit, and is repaid by FY2031.

The earlier scenario with only 15,000 of FY2028 term borrowing failed the floor by **4,039.5 even after using the whole revolver**. The model was not made to ignore that failure: the final table explicitly assumes 25,000 of FY2028 term borrowing. That dependence is a material judgment to challenge.

### Refusal tests actually run

| Command / case | Expected and observed result |
| --- | --- |
| `python orcl_proforma.py` | Five balanced years; all cash floors pass; valuation prints |
| `python orcl_proforma.py --break-check` | Exit 1; refuses FY2027 balance-sheet gap −1,000 |
| `python orcl_proforma.py --break-cash-flow` | Exit 1; refuses FY2027 cash-flow-link gap −1,000 even though the BS itself is unchanged |
| `python orcl_proforma.py --funding-stress` | Exit 1; refuses FY2027 cash-floor shortfall after the credit limit is exhausted |
| Cost of equity set below terminal growth | Refuses valuation |
| Final-year capex increased enough to make FCFE negative, with explicit equity funding to preserve liquidity | Refuses terminal valuation |

The switches make temporary in-memory changes; the base file remains unchanged. `assert_balanced` runs inside `value_equity`, so calling the valuation function directly cannot skip the checks.

### Value and market comparison

The lab-convention value is **$74.80 per current common share**, or **$226,177.57 million** on **3,023.736000 million current common shares**. The share of indicated value after FY2031 is **91.30%**.

After assumed preferred conversion, FY2029–FY2031 cash flows are divided by **3,054.974285 million** shares. The existing holder's per-share cash-flow PV is then multiplied by the **current** share count only to state a current-common-equity equivalent. I do not divide the model by a diluted future count and compare its market capitalization against an unrelated count.

Following the course convention:

`Terminal FCFE = (21,777.5260 + 10,350) × 1.03 = 33,091.3518`

`Terminal value at FY2031 = 33,091.3518 / (0.12 − 0.03) = 367,681.6863`

`Value/share = Σ[max(FCFE_t, 0) / shares_t / 1.12^t] + terminal value / FY2031 shares / 1.12^5`.

PV from positive forecast cash flows is **$6.51/share**, and PV from the terminal value is **$68.29/share**.

**Required comparison sentence:** The model says **$74.80 per share** and the market says **$139.52 at the September 24, 2026, 4:00 PM EDT close**, using **3,023.736 million current common shares** as the common-equity comparison basis—what stronger growth, margins, or lower investment burden would explain the difference? [P]

At that same share count, price × shares is **$421,871.65 million**. This deliberately does not copy a provider market-cap figure that might use a different share count.

**Material interpretation limits:** The comparison uses the lab's annual FY2026-year-end discount convention; it is not a September 24 stub-period valuation. Excluding negative FCFE raises the number: including the signed forecast FCFE, with the same terminal assumptions, gives **$65.02/share**. The signed calculation is a diagnostic, not a second recommendation. The lab figure is conditional on obtaining the planned funding, the capex taper, and the terminal refinancing assumption. It is not an investable fair-value conclusion or a buy/sell recommendation.

The terminal calculation is a reduced-form cash-flow assumption: it does not prove that every PP&E, lease, tax, or customer-contract balance can grow at 3% forever. Net customer cash runoff stops before terminal valuation, but the future replacement-spending burden and financing economics still deserve a separate normalized terminal-year build in next week's sensitivity work.

## E — fresh eyes


- Partner name and date: **Aidan Murrin, 9/24/26**.
- Judgment my partner attacked: **Oracle’s annual capital spending decreasing from $92.5 billion in FY2027 to $40 billion in FY2031 while revenue continues growing.**
- Their actual attack, including “why that number, and what would change it?”: **Proposed wording to confirm with Aidan: Why did you choose $40 billion for Oracle’s later capital spending, and what would make you increase that number?**
- My answer, sentence 1: **I assumed Oracle’s large investments in the first few years would create capacity that could support future revenue, allowing annual spending to decrease as those facilities become operational.**
- My answer, sentence 2: **I would increase capital spending or lower projected revenue if Oracle’s updates showed that equipment replacement and additional data centers required more investment than I assumed.**
- The specific judgment I attacked in their model: **eBay’s assumed annual revenue growth rate of 4%.**
- My actual question: **Why did you choose 4% annual revenue growth for eBay?**
- Their answer: **Aidan said he chose 4% as a moderate assumption rather than assuming eBay would continue growing at its reported 2025 rate of 8%.**

**Question prepared for my attack, if it fits their model:** “Your revenue grows while your capital spending stays fixed; how does your PP&E schedule support that extra capacity after depreciation, and what happens to your cash and terminal value if replacement spending rises?” Replace it if their actual model does not make those assumptions. For a services company, ask instead about the staffing or R&D investment needed to support its revenue growth.

## Organic growth — Learn on your own

**1. What is it?** Organic growth is growth from the existing business, excluding the effect of acquisitions and divestitures; the exact company definition can also exclude currency and other items. Same-store growth is a retailer/dealer version that compares qualifying locations open in both periods.

**2. How does Oracle disclose it?** In the reviewed MD&A, Oracle presents reported growth and constant-currency growth. I did not find a separate consolidated organic or same-store series for these years. Its constant-currency growth was **6%, 9%, and 16%** for FY2024–FY2026; this removes currency effects but does not by itself exclude acquisitions. Oracle cloud growth is a business-line measure, not an organic-growth substitute.

**3. Why does the ABG video carry 1.8% rather than reported 4.7%?** The video's historical FY2025 same-store growth is **1.2%**, while reported growth is **4.7%** and includes acquired dealerships. The forward **1.8% is a judgment**, between that 1.2% history and low-single-digit growth; it is not the reported same-store rate. Applying 4.7% indefinitely without modeling acquisitions and the money required to buy them would give the model growth without the associated investment. Oracle's forward growth path is therefore labelled guidance/judgment, not presented as disclosed organic-growth history. See [Part 1 slides][SLIDES], slides 5 and 8.

## Reflect

**Which label would I defend longest, and why? — I would defend labelling the capital-spending decline a judgment. The filings show the spending that already occurred, but they do not prove Oracle can lower future investment while producing the revenue I projected; calling that decline history or guidance would overstate the evidence.

**What number surprised me? — Oracle reported 17,087 of net income in FY2026 but spent 55,663 on capital expenditures, compared with 31,977 of operating cash flow. The resulting 23,686 free-cash-flow deficit showed me why growth in accounting profit does not automatically mean cash is available to shareholders.

**Why cash comes last? — Cash is the result of operations, investment, and financing. Typing a cash balance first could hide a missing borrowing need or a broken statement link, which is why the program computes it last and checks it separately.

