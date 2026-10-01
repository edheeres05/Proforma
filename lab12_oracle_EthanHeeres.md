# Lab 12 - Pro-Forma Sensitivity: Present and Review Your Full Analysis

**Ethan D. Heeres | FIN 439 | October 1, 2026**  
**My company:** Oracle Corporation (ORCL)  
**Learning partner:** Nicole Yu  
**Partner company reviewed:** Target Corporation (TGT)

## Existing analysis and output

These are the existing files I used during the presentation. Lab 12 did not require a new model or a new slide deck.

- [Oracle DCF analysis](oracle_lab06.md)
- [Oracle DCF code](dcf.py)
- [Oracle peer comparison](lab08_oracle.md)
- [Oracle pro-forma analysis](lab10_oracle.md)
- [Oracle pro-forma code](orcl_proforma.py)
- [Oracle Lab 11 sensitivity analysis](lab11_oracle_EthanHeeres_COMPLETE1.md)
- [Oracle Lab 11 sensitivity code](orcl_lab11_EthanHeeres.py)
- [Oracle Lab 11 output](lab11_oracle_output.txt)

## My Oracle conclusion

My analysis does not support treating one valuation number as certain. My Week 3 DCF produced a base value of **$151.01 per share** on the September 10, 2026 comparison date, with a sensitivity range of **$112.42-$213.77**. My peer comparison produced a range of **$159.94-$181.63**, with a median of **$170.78**, compared with Oracle's **$152.94** September 10 market price.

The later Lab 10 pro-forma produced a much lower conditional value of **$74.80 per current common share** versus a **$139.52** September 24, 2026 market price. I do not average these methods because they use different models and assumptions. The large difference in the pro-forma is mainly tied to Oracle's heavy capital-spending and financing requirements.

Lab 11 showed that **revenue growth was the larger operating driver over the usable tested comparisons**. The higher-growth case increased FY2031 operating profit by **$7,345.1 million** and signed FCFE by **$5,320.1 million** versus the base case. The lower-capex case increased operating profit by **$1,931.9 million** and signed FCFE by **$3,413.1 million**. The lower-growth and higher-capex endpoints failed the model's funding constraints, so I do not treat those failed cases as valid valuation evidence.

My main conclusion is conditional: Oracle has meaningful cloud and AI growth opportunities, but the value depends heavily on whether that growth converts into cash flow fast enough to support the required infrastructure spending and financing.

## As presenter - questions Nicole asked me about Oracle

### 1. Why is Oracle's current stock price significantly higher than its estimated DCF value?

I explained that the market may be expecting stronger cloud and AI growth than the pro-forma DCF assumes. The difference could also come from conservative cash-flow forecasts, the discount rate, terminal-growth assumptions, and investor optimism. The gap means the market is pricing in a stronger future than the lower pro-forma valuation assumes.

### 2. Which economic, market, and business factors might the DCF model fail to capture?

I explained that a basic DCF cannot fully capture future economic conditions, changes in customer technology spending, input costs, competition, investor sentiment, or the strategic value of Oracle's cloud infrastructure. It may also fail to capture how quickly AI demand could change Oracle's future revenue and margins.

### 3. How could cloud and AI demand affect Oracle's future performance?

I said higher demand could increase cloud revenue, improve data-center utilization, and create more recurring cash flow. The tradeoff is that Oracle has to spend heavily on infrastructure first, and competition could reduce prices or margins.

### 4. Will Oracle need debt financing for its mega-projects?

I said Oracle may need debt financing if capital expenditures substantially exceed operating cash flow. Debt can help fund expansion without issuing additional common shares, but it also increases interest expense, refinancing risk, and financial pressure if the expected growth does not occur.

### 5. What factors could support buying Oracle despite the low pro-forma DCF estimate?

I said the argument would be Oracle's recurring revenue, established customer base, cloud expansion, and long-term AI opportunities. At the same time, the gap between the **$74.80** pro-forma estimate and the **$139.52** September 24 market price leaves less room for error because a significant amount of future growth is already reflected in the market price.

## What I will keep, revise, and investigate after Nicole's feedback

- **Keep:** I will keep the core view that Oracle's cloud and AI growth can create substantial long-term revenue and cash-flow opportunities, but I will continue to present the valuation as conditional rather than as one certain fair-value number.
- **Revise:** I will make the difference between the Week 3 DCF, peer valuation, and later pro-forma clearer. The methods use different forecast structures, valuation dates, and assumptions, so the results should be shown side by side rather than blended together.
- **Investigate:** I would research Oracle's capital-spending path and financing needs first, especially whether annual capex can realistically fall from roughly **$92.5 billion in FY2027 to $40 billion by FY2030-FY2031** while Oracle still supports the cloud growth assumed in the model. I would also keep researching whether cloud demand converts into operating cash flow as quickly as the higher-growth scenario assumes.

The review did **not** make me replace my valuation conclusion with a new number. It changed my research priority by making the capital-spending, financing, and cloud-to-cash-flow assumptions the main items I would investigate next.

## As reviewer - Nicole Yu's Target analysis

I reviewed Nicole's Target analysis after presenting Oracle. I used the answers she gave during the **Part R full-analysis route** to form the questions below and explain her analysis back to her.

### 1. Selection and evidence

**Question I asked Nicole:** You explained that Target has a recognizable brand, a large store network, and an omnichannel retail model. Why does that make Target a useful company to analyze, and what evidence supports that view?

**Answer from Nicole's Part R discussion:** Target is useful to analyze because its business model is easy to connect to operating results: it sells a broad mix of merchandise through stores and digital channels, and its results depend on customer traffic, spending, product mix, margins, inventory, and operating efficiency. Its size and long public history also give enough financial information to compare recent performance with prior years.

**Evidence check:** We used Target's annual-report information as the evidence behind the business and recent-performance discussion. Target describes itself as a single retail segment in which customers can buy differentiated merchandise and everyday essentials through stores and digital channels. Its 2025 annual report shows net sales of **$104.780 billion**, compared with **$106.566 billion in 2024**, so the recent weakness Nicole discussed is visible in the reported results.

### 2. Model and valuation

**Question I asked Nicole:** Since Target's recent sales have been weaker, what has to improve in the forecast for the valuation to work, and why?

**Answer from Nicole's Part R discussion:** The forecast depends on Target getting back to sales growth while protecting profitability. If traffic, discretionary spending, or margins stay weak, the cash flows used in the valuation would also be weaker. If Target can improve the shopping experience, merchandising, digital fulfillment, and operating efficiency, then revenue and profit can recover and support a higher value.

I also asked how management's outlook fits into that assumption. Nicole explained that management is trying to return Target to growth rather than assuming the recent weak results continue forever. Target's 2025 annual report supports that point: management said its focus is getting Target back to growth and identified merchandising, guest experience, technology, and the team as major priorities for 2026.

### 3. Sensitivity and interpretation

**Question I asked Nicole:** What could most easily make your Target conclusion wrong?

**Answer from Nicole's Part R discussion:** The biggest issue is whether Target can actually improve sales and margins. Consumers have been cautious, especially with discretionary spending, and Target also faces strong retail competition. If those pressures continue, a more optimistic growth or margin assumption would be too high. On the other hand, stronger traffic, better merchandising, and improved execution could make the forecast more achievable.

**Follow-up:** Does that mean the driver ranking is certain?

**Answer:** No. The sensitivity results only show which assumptions mattered most **over the ranges she tested**. They do not prove which future outcome is most likely.

### Source/calculation checked

We checked the recent-performance claim against Target's 2025 annual report:

- 2024 net sales: **$106.566 billion**
- 2025 net sales: **$104.780 billion**
- Change: approximately **-1.7%**
- 2024 operating income: **$5.566 billion**
- 2025 operating income: **$5.117 billion**
- Change: approximately **-8.1%**

This supported Nicole's Part R explanation that Target entered the forecast from a period of weaker recent performance rather than from unusually strong current growth.

Official source used for the check:  
https://corporate.target.com/investors/annual/2025-annual-report/financials/financial-performance

### My explanation back to Nicole

I explained Nicole's analysis back as follows: **her Target conclusion depends on a recovery in sales and profitability rather than simply extending the recent decline. The main operating driver is whether Target can turn its brand, stores, merchandise, and omnichannel capabilities into stronger customer traffic and spending while maintaining margins. The biggest limitation is that consumer demand and competitive pressure are outside Target's control, so a forecasted recovery is still an assumption rather than a guaranteed outcome.**

Nicole's Part R discussion also made the difference between a business strength and a valuation assumption clear. Target's brand, store network, and omnichannel capabilities are real advantages, but those advantages still have to translate into higher revenue, margins, and cash flow for the valuation to improve.

### Feedback I gave Nicole

**Evidence-backed strength:** Nicole connected Target's recent operating performance and management outlook to the assumptions in her forecast instead of treating the forecast as disconnected from the company's history.

**Specific improvement:** I would make the sales-growth and margin-recovery assumptions even more explicit by showing exactly how much improvement is required relative to 2025 results. That would make it easier to see how much of the valuation depends on Target successfully returning to growth versus simply maintaining its current performance.
## Reflection

The question that made me reconsider my analysis most was why Oracle might need substantial debt financing for its expansion. It reinforced that strong revenue growth does not automatically mean the company generates enough cash to fund the infrastructure required to produce that growth. I now understand more clearly that Oracle's growth forecast, capital-spending path, and financing assumptions have to be evaluated together rather than independently.
