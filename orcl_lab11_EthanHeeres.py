"""FIN 439 Lab 11 -- Oracle sensitivity, Ethan D. Heeres.

Run: python orcl_lab11_EthanHeeres.py
Only the Python standard library is needed; there are no input-file dependencies.
Prints the run and saves lab11_oracle_output.txt beside this script.
Keep your completed Markdown report as the written interpretation.

The original Lab 10 inputs and calculation functions are included unchanged.
The old Lab 10 command-line entry point is replaced by the sensitivity run.
The agreed ranges and a copy of the prediction from the supplied report are
embedded below. This is a reproduction of an existing analysis, not a new
pre-run prediction. It does not modify the supplied Markdown report.

Exit 1 means at least one scenario failed the reported model constraints;
the completed output is still saved. Exit 2 means the analysis could not run.
"""

import argparse
import copy
import math

YEARS = [2027, 2028, 2029, 2030, 2031]
TOLERANCE = 1e-6
SOURCES = {
    "F24": "https://www.sec.gov/Archives/edgar/data/1341439/000095017024075605/orcl-20240531.htm",
    "F25": "https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/orcl-20250531.htm",
    "F26": "https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm",
    "Q27": "https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm",
    "G27": "https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx",
    "PROVIDER": "https://stockanalysis.com/stocks/orcl/financials/cash-flow-statement/",
}

# Reported history; gross profit and SG&A are constructed consistently below.
HISTORY = {
    2024: dict(revenue=52961, direct_cost=9427+891+4825, sga=8274+1548,
               net_income=10467, inventory=None, ppe=21536, parent_equity=8704,
               total_equity=9239, depreciation=3129, capex=6866,
               tax=1274, pretax=11741, prior_revenue=49954, cfo=18673,
               constant_currency_growth=0.06, source="F24"),
    2025: dict(revenue=57399, direct_cost=11569+782+4576, sga=8651+1602,
               net_income=12443, inventory=None, ppe=43522, parent_equity=20451,
               total_equity=20969, depreciation=3867, capex=21215,
               tax=1717, pretax=14160, prior_revenue=52961, cfo=20821,
               constant_currency_growth=0.09, source="F25"),
    2026: dict(revenue=67357, direct_cost=17597+868+4556, sga=8331+1618,
               net_income=17087, inventory=None, ppe=99957, parent_equity=42508,
               total_equity=43056, depreciation=7623, capex=55663,
               tax=2467, pretax=19554, prior_revenue=57399, cfo=31977,
               constant_currency_growth=0.16, source="F26"),
}

# FY2026 opening balances. All groupings reconcile to the consolidated 10-K.
OPENING = {
    "revenue": 67357.0,
    "cash": 31289.0,
    "receivables": 10385.0,
    "prepaid": 4288.0,
    "ppe": 99957.0,
    "intangibles": 3229.0,
    "other_assets": 261759.0-31289-10385-4288-99957-3229,
    "debt": 7199.0+122342+7701,  # Includes finance-lease liabilities.
    "revolver": 0.0,
    "deferred_revenue": 9916.0+5479,
    "other_liabilities": 218703.0-(7199+122342+7701)-(9916+5479),
    "equity": 43056.0,
    "preferred_equity": 4954.0,
    "nci": 548.0,
}

# Each input is labelled and explained in the accompanying assumption table.
ASSUMPTIONS = {
    "growth": [90000/67357-1, 0.25, 0.20, 0.15, 0.10],
    "gross_margin_before_depreciation": [0.75]*5,
    "sga_to_gross_profit": [0.22, 0.21, 0.20, 0.20, 0.20],
    "rd_to_revenue": [0.12, 0.115, 0.11, 0.105, 0.10],
    "depreciation_to_opening_ppe": 0.12,
    "amortization": [731.0, 694.0, 620.0, 582.0, 377.0],
    "restructuring": [1500.0, 750.0, 500.0, 0.0, 0.0],
    "capex": [92500.0, 70000.0, 50000.0, 40000.0, 40000.0],
    "tax_rate": 0.18,
    "receivables_to_revenue": 10385/67357,
    "prepaid_to_revenue": 4288/67357,
    "net_customer_cash_advances": [20000.0, 15000.0, 5000.0, -5000.0, 0.0],
    "ordinary_deferred_revenue_baseline": 10733.0,
    "customer_financing_rate": 0.05,
    "new_debt": [20000.0, 25000.0, 0.0, 0.0, 0.0],
    "debt_repayment": [7210+620, 10145+600, 5500+600, 7250+600, 9750+600],
    "debt_rate": 0.045,
    "revolver_rate": 0.065,
    "minimum_cash": 10000.0,
    "revolver_limit": 10000.0,
    "common_equity_proceeds": [19909.0, 0.0, 0.0, 0.0, 0.0],
    "current_common_shares": 3023.736,  # 10-Q cover, September 7, 2026.
    "preferred_conversion_shares": 0.05*624.7657,
    "preferred_dividends": [325.0, 325.0, 325*7.5/12, 0.0, 0.0],
    "annual_common_dividend_per_share": 2.0,
    "cost_of_equity": 0.12,
    "terminal_growth": 0.03,
    "market_price": 139.52,
    "market_price_date": "2026-09-24, 4:00 PM EDT close (Stock Analysis)",
}


def total_assets(r):
    return sum(r[k] for k in ("cash", "receivables", "prepaid", "ppe",
                             "intangibles", "other_assets"))


def total_liabilities(r):
    return sum(r[k] for k in ("debt", "revolver", "deferred_revenue", "other_liabilities"))


def balance_gap(r):
    return total_assets(r)-total_liabilities(r)-r["equity"]


def require_zero(year, label, gap):
    if not math.isfinite(gap) or abs(gap) > TOLERANCE:
        raise ValueError(f"FY{year}: {label} gap = {gap:,.6f} million")


def project(opening=OPENING, a=ASSUMPTIONS):
    """Income statement -> noncash balances -> cash flows -> financing -> cash."""
    require_zero(2026, "opening balance sheet", balance_gap(opening))
    prev = opening.copy()
    rows = []
    for i, year in enumerate(YEARS):
        r = {"year": year}
        r["revenue"] = prev["revenue"]*(1+a["growth"][i])
        r["depreciation"] = prev["ppe"]*a["depreciation_to_opening_ppe"]
        r["direct_cost_ex_depreciation"] = r["revenue"]*(1-a["gross_margin_before_depreciation"][i])
        r["gross_profit_before_depreciation"] = r["revenue"]-r["direct_cost_ex_depreciation"]
        # All modeled PP&E depreciation is allocated to direct costs ONCE.
        r["direct_cost"] = r["direct_cost_ex_depreciation"]+r["depreciation"]
        r["gross_profit"] = r["revenue"]-r["direct_cost"]
        r["sga"] = r["gross_profit"]*a["sga_to_gross_profit"][i]
        r["rd"] = r["revenue"]*a["rd_to_revenue"][i]
        r["amortization"] = a["amortization"][i]
        r["restructuring"] = a["restructuring"][i]
        r["operating_income"] = r["gross_profit"]-r["sga"]-r["rd"]-r["amortization"]-r["restructuring"]
        # Opening balances, as in Lab 09. No circular average-balance interest.
        r["interest"] = prev["debt"]*a["debt_rate"]+prev["revolver"]*a["revolver_rate"]
        r["customer_interest"] = max(0, prev["deferred_revenue"]-a["ordinary_deferred_revenue_baseline"])*a["customer_financing_rate"]
        r["pretax"] = r["operating_income"]-r["interest"]-r["customer_interest"]
        r["tax"] = max(0, r["pretax"])*a["tax_rate"]
        r["net_income"] = r["pretax"]-r["tax"]

        r["receivables"] = r["revenue"]*a["receivables_to_revenue"]
        r["prepaid"] = r["revenue"]*a["prepaid_to_revenue"]
        r["change_working_assets"] = r["receivables"]+r["prepaid"]-prev["receivables"]-prev["prepaid"]
        r["capex"] = a["capex"][i]
        r["ppe"] = prev["ppe"]+r["capex"]-r["depreciation"]
        r["intangibles"] = prev["intangibles"]-r["amortization"]
        r["other_assets"] = prev["other_assets"]
        r["net_customer_cash_advances"] = a["net_customer_cash_advances"][i]
        # Cash advances and noncash financing accretion both increase the liability.
        r["deferred_revenue"] = prev["deferred_revenue"]+r["net_customer_cash_advances"]+r["customer_interest"]
        r["new_debt"] = a["new_debt"][i]
        r["debt_repayment"] = a["debt_repayment"][i]
        r["debt"] = prev["debt"]+r["new_debt"]-r["debt_repayment"]
        r["other_liabilities"] = prev["other_liabilities"]
        r["preferred_equity"] = opening["preferred_equity"] if year < 2029 else 0.0
        r["nci"] = opening["nci"]
        r["shares"] = a["current_common_shares"]+(a["preferred_conversion_shares"] if year >= 2029 else 0)
        r["preferred_dividends"] = a["preferred_dividends"][i]
        r["common_dividends"] = r["shares"]*a["annual_common_dividend_per_share"]
        r["equity_proceeds"] = a["common_equity_proceeds"][i]
        r["equity"] = prev["equity"]+r["net_income"]+r["equity_proceeds"]-r["common_dividends"]-r["preferred_dividends"]

        # Compensation is modeled as cash compensation; no SBC add-back/dilution.
        r["cfo"] = (r["net_income"]+r["depreciation"]+r["amortization"]
                    +r["customer_interest"]-r["change_working_assets"]
                    +r["net_customer_cash_advances"])
        r["cfi"] = -r["capex"]
        r["fcfe_before_new_borrowing"] = r["cfo"]-r["capex"]-r["debt_repayment"]-r["preferred_dividends"]
        # Include planned new term debt; exclude the discretionary liquidity revolver.
        r["fcfe"] = r["fcfe_before_new_borrowing"]+r["new_debt"]
        cash_before_revolver = prev["cash"]+r["fcfe"]+r["equity_proceeds"]-r["common_dividends"]
        if cash_before_revolver < a["minimum_cash"]:
            r["change_revolver"] = min(a["minimum_cash"]-cash_before_revolver,
                                        max(0, a["revolver_limit"]-prev["revolver"]))
        else:
            r["change_revolver"] = -min(prev["revolver"], cash_before_revolver-a["minimum_cash"])
        r["revolver"] = prev["revolver"]+r["change_revolver"]
        r["cff"] = (r["new_debt"]-r["debt_repayment"]+r["change_revolver"]
                    +r["equity_proceeds"]-r["common_dividends"]-r["preferred_dividends"])
        r["opening_cash"] = prev["cash"]
        r["change_cash"] = r["cfo"]+r["cfi"]+r["cff"]
        r["cash"] = prev["cash"]+r["change_cash"]
        r["cash_from_funding_schedule"] = cash_before_revolver+r["change_revolver"]
        r["fcfe_after_revolver"] = r["fcfe"]+r["change_revolver"]
        rows.append(r)
        prev = r
    return rows


def check_gaps(r, prev):
    return {
        "balance sheet": balance_gap(r),
        "cash-flow link": r["cash"]-prev["cash"]-r["cfo"]-r["cfi"]-r["cff"],
        "cash movement": r["change_cash"]-r["cfo"]-r["cfi"]-r["cff"],
        "funding cash link": r["cash"]-r["cash_from_funding_schedule"],
        "PP&E roll-forward": r["ppe"]-prev["ppe"]-r["capex"]+r["depreciation"],
        "intangible roll-forward": r["intangibles"]-prev["intangibles"]+r["amortization"],
        "debt roll-forward": r["debt"]-prev["debt"]-r["new_debt"]+r["debt_repayment"],
        "deferred revenue roll-forward": r["deferred_revenue"]-prev["deferred_revenue"]-r["net_customer_cash_advances"]-r["customer_interest"],
        "equity roll-forward": r["equity"]-prev["equity"]-r["net_income"]-r["equity_proceeds"]+r["common_dividends"]+r["preferred_dividends"],
        "FCFE link": r["fcfe"]-r["cfo"]+r["capex"]-r["new_debt"]+r["debt_repayment"]+r["preferred_dividends"],
    }


def assert_balanced(rows, a=ASSUMPTIONS, opening=OPENING):
    """Refuse valuation on broken accounting, nonfinite values, or unavailable cash."""
    require_zero(2026, "opening balance sheet", balance_gap(opening))
    prev = opening
    for r in rows:
        year = r["year"]
        for key, value in r.items():
            if not math.isfinite(value):
                raise ValueError(f"FY{year}: {key} is nonfinite")
        for label, gap in check_gaps(r, prev).items():
            require_zero(year, label, gap)
        if r["cash"] < a["minimum_cash"]-TOLERANCE:
            raise ValueError(f"FY{year}: cash floor gap = {r['cash']-a['minimum_cash']:,.6f} million; financing unavailable")
        if r["revolver"] < -TOLERANCE or r["revolver"] > a["revolver_limit"]+TOLERANCE:
            raise ValueError(f"FY{year}: revolver outside limit")
        for key in ("ppe", "intangibles", "debt", "deferred_revenue"):
            if r[key] < -TOLERANCE:
                raise ValueError(f"FY{year}: negative {key} = {r[key]:,.6f} million")
        prev = r


def value_equity(rows, a=ASSUMPTIONS):
    assert_balanced(rows, a)
    k, g = a["cost_of_equity"], a["terminal_growth"]
    if not (math.isfinite(k) and math.isfinite(g) and k > g >= 0):
        raise ValueError("Require finite cost of equity > terminal growth >= 0.")
    if a["current_common_shares"] <= 0 or any(r["shares"] <= 0 for r in rows):
        raise ValueError("Share counts must be positive.")
    # Terminal cash must already be positive; do not rescue a negative year.
    if rows[-1]["fcfe"] <= 0:
        raise ValueError("FY2031: negative/zero FCFE; no positive perpetual terminal value is supported.")
    # Lab 09 convention: refinance principal after year 5; debt is NOT forgiven.
    terminal_fcfe = (rows[-1]["fcfe"]+rows[-1]["debt_repayment"])*(1+g)
    terminal_value = terminal_fcfe/(k-g)
    pv_positive_per_share = sum(max(0,r["fcfe"])/r["shares"]/(1+k)**t
                                for t,r in enumerate(rows,1))
    pv_signed_per_share = sum(r["fcfe"]/r["shares"]/(1+k)**t
                              for t,r in enumerate(rows,1))
    pv_terminal_per_share = terminal_value/rows[-1]["shares"]/(1+k)**len(rows)
    value_per_share = pv_positive_per_share+pv_terminal_per_share
    return {
        "value_per_share": value_per_share,
        "equity_value_current_share_basis": value_per_share*a["current_common_shares"],
        "terminal_fcfe": terminal_fcfe,
        "terminal_value": terminal_value,
        "terminal_share": pv_terminal_per_share/value_per_share,
        "signed_fcfe_comparison": pv_signed_per_share+pv_terminal_per_share,
        "pv_positive_per_share": pv_positive_per_share,
        "pv_terminal_per_share": pv_terminal_per_share,
    }


STATEMENT_LINES = {
    "INCOME STATEMENT": [
        ("Revenue","revenue"), ("Direct costs excluding depreciation","direct_cost_ex_depreciation"),
        ("Gross profit before depreciation","gross_profit_before_depreciation"),
        ("Depreciation in direct costs","depreciation"), ("Gross profit after depreciation","gross_profit"),
        ("SG&A","sga"), ("Research and development","rd"), ("Intangible amortization","amortization"),
        ("Restructuring (cash expense)","restructuring"), ("Operating income","operating_income"),
        ("Debt and revolver interest","interest"), ("Customer financing accretion","customer_interest"),
        ("Pretax income","pretax"), ("Income tax","tax"), ("Net income","net_income")],
    "BALANCE SHEET": [
        ("Cash","cash"), ("Trade receivables","receivables"), ("Prepaid / other current assets","prepaid"),
        ("PP&E, net","ppe"), ("Intangibles, net","intangibles"), ("Other assets","other_assets"),
        ("Total assets",total_assets), ("Debt, including finance leases","debt"), ("Revolver","revolver"),
        ("Deferred revenue / customer funding","deferred_revenue"), ("Other liabilities","other_liabilities"),
        ("Total liabilities",total_liabilities),
        ("Common parent equity",lambda r:r["equity"]-r["preferred_equity"]-r["nci"]),
        ("Preferred equity","preferred_equity"), ("Noncontrolling interests","nci"), ("Total equity","equity"),
        ("Total liabilities and equity",lambda r:total_liabilities(r)+r["equity"])],
    "CASH FLOW STATEMENT": [
        ("Net income","net_income"), ("+ Depreciation","depreciation"), ("+ Intangible amortization","amortization"),
        ("+ Noncash customer financing interest","customer_interest"),
        ("- Change in operating assets",lambda r:-r["change_working_assets"]),
        ("Net cash advances / (recognition)","net_customer_cash_advances"), ("Cash from operations","cfo"),
        ("Investing cash flow: gross capex","cfi"), ("New term debt","new_debt"),
        ("Debt / finance lease principal",lambda r:-r["debt_repayment"]),
        ("Common equity proceeds","equity_proceeds"), ("Common dividends",lambda r:-r["common_dividends"]),
        ("Preferred dividends",lambda r:-r["preferred_dividends"]),
        ("Revolver draw / (repayment)","change_revolver"), ("Cash from financing","cff"),
        ("Change in cash","change_cash"), ("Opening cash","opening_cash"), ("Closing cash","cash"),
        ("FCFE before any new debt","fcfe_before_new_borrowing"),
        ("FCFE incl. term debt; before revolver","fcfe"),
        ("FCFE including revolver","fcfe_after_revolver")],
}


def print_table(title, rows, lines):
    print(f"\n{title} (USD millions; shares in millions)")
    print(f"{'':<42}"+"".join(f"{'FY'+str(r['year'])+'E':>15}" for r in rows))
    for label, field in lines:
        values = [field(r) if callable(field) else r[field] for r in rows]
        print(f"{label:<42}"+"".join(f"{0.0 if abs(v)<TOLERANCE else v:>15,.1f}" for v in values))


# LAB 11: frozen base inputs and selected sensitivity assumptions.
import hashlib
import io
import json
from contextlib import redirect_stdout
from datetime import datetime, timezone
from pathlib import Path

BASE_INPUTS = copy.deepcopy(ASSUMPTIONS)
BASE_OPENING = copy.deepcopy(OPENING)
VALUE_NOTE = (
    "Unavailable. The Lab 10 positive-FCFE-only valuation is not used in Lab 11. "
    "Signed FCFE is retained, and normalized terminal financing and replacement "
    "spending remain unresolved."
)

ORIGINAL_MODEL_SHA256 = '7845874854dcacf3fe3d17162966328346d82587079a03e2b02d3a8f848cf0e5'
RANGES = {'years': [2027, 2028, 2029, 2030, 2031], 'drivers': [{'key': 'growth', 'change_units': 'percentage_points', 'lower_change': -2, 'higher_change': 2, 'range_reason': 'Judgment: a sustained two-percentage-point annual deviation tests a modest difference in cloud demand and the timing of converting contracts into revenue while preserving the slowing-growth pattern. This is a chosen scenario range, not company guidance or a probability interval.'}, {'key': 'capex', 'change_units': 'percent_change', 'lower_change': -10, 'higher_change': 10, 'range_reason': 'Judgment: a ten-percent change tests uncertainty in data-center build costs, replacement needs, and the investment required to support the forecast, while preserving the original spending pattern. This is a chosen scenario range, not company guidance or a probability interval.'}]}
PREDICTION_TEXT = "The following higher-growth prediction was recorded before the changed-input sensitivity run and was not revised after seeing the results.\n\nRecorded at: 2026-09-29T16:53:07.498015-04:00\nDriver: growth\nCase: higher\nOld values: FY2027–FY2031 annual growth = 33.61640216%, 25.00000000%, 20.00000000%, 15.00000000%, 10.00000000%.\nNew values: FY2027–FY2031 annual growth = 35.61640216%, 27.00000000%, 22.00000000%, 17.00000000%, 12.00000000%; +2 percentage points in every year. Capex and all other independent assumptions stay at base.\nExpected direction: Higher FY2031 operating profit and higher signed FCFE.\nRough size: Operating profit +10.408080% versus original FY2031 base; FCFE +21.665290% versus original FY2031 base. These implement the original estimates as discussed: 1.02^5 - 1 and 1.04^5 - 1, not new growth inputs in the model. Predicted profit = 66,174.6957 USD million (base 59,936.4607); predicted FCFE = 26,495.6902 USD million (base 21,777.5260).\nReason: Ethan expects continued cloud adoption and Oracle's position in cloud services to support higher revenue and profits. The comparison isolates higher revenue growth while all other independent assumptions remain at base. This is a pre-run judgment, not a model result.\nRange and unit check used in the completed analysis: revenue growth changes are measured in percentage points, capex changes are measured as percent changes to spending, outputs are in USD millions, and the comparison covers FY2027–FY2031.\n\nThe later 7% profit / 13% FCFE estimate was withdrawn; Ethan asked to use the original estimates. The original Lab 10 forecast remains unchanged. Reconcile the actual result in the analysis report after running; do not rewrite the prediction after seeing results."
ORIGINAL_RECORDED_PREDICTION_SHA256 = '9057466cef65443ce394b5952238d56e175e9939864fba4ff58351fa87787f5a'
ORIGINAL_REPORT_NAME = 'lab11_oracle_EthanHeeres_COMPLETE1.md'
ORIGINAL_REPORT_SHA256 = 'b616cb84612d39d7fb547a6ffb216b357909464e3bba88a9f09974a928681fd5'


def changed_keys(a, b):
    return sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))

def evaluate(label, inputs, driver=None, case="base"):
    """Fresh independent assumptions and opening balances for every full run."""
    a = copy.deepcopy(inputs)
    opening = copy.deepcopy(BASE_OPENING)
    saved_inputs = copy.deepcopy(a)
    changes = changed_keys(a, BASE_INPUTS)
    expected = [] if case == "base" else [driver]
    if changes != expected:
        raise ValueError(f"{label}: expected changed keys {expected}, got {changes}")
    rows = project(opening, a)
    if a != saved_inputs or opening != BASE_OPENING:
        raise ValueError("Model mutated independent inputs or opening balances.")
    checks, errors = [], []
    prev = opening
    for row in rows:
        gaps = check_gaps(row, prev)
        accounting_ok = all(math.isfinite(v) and abs(v) <= TOLERANCE for v in gaps.values())
        finite = all(math.isfinite(v) for v in row.values())
        cash_ok = row["cash"] >= a["minimum_cash"] - TOLERANCE
        credit_ok = -TOLERANCE <= row["revolver"] <= a["revolver_limit"] + TOLERANCE
        balances_ok = all(row[k] >= -TOLERANCE for k in ("ppe", "intangibles", "debt", "deferred_revenue"))
        checks.append(dict(year=row["year"], gaps=gaps, accounting_pass=accounting_ok,
                           finite_pass=finite, cash_floor_pass=cash_ok,
                           credit_limit_pass=credit_ok, balances_pass=balances_ok,
                           cash=row["cash"], cash_floor=a["minimum_cash"],
                           revolver=row["revolver"], revolver_limit=a["revolver_limit"]))
        for test, passed in (("accounting", accounting_ok), ("finite values", finite),
                             ("cash floor", cash_ok), ("credit limit", credit_ok),
                             ("nonnegative balances", balances_ok)):
            if not passed:
                errors.append(f"FY{row['year']}: {test} failed")
        prev = row
    try:
        assert_balanced(rows, a, opening)
    except ValueError as exc:
        errors.append(str(exc))
    return dict(label=label, driver=driver, case=case, inputs=saved_inputs,
                changed_independent_keys=changes, rows=rows, checks=checks,
                valid=not errors, errors=errors,
                operating_profit=rows[-1]["operating_income"], fcfe=rows[-1]["fcfe"],
                value_per_share=None, value_note=VALUE_NOTE)

def prepare_ranges(config):
    if config.get("years") != YEARS:
        raise ValueError(f"The agreed comparison covers all five years: {YEARS}.")
    drivers = config.get("drivers", [])
    if len(drivers) != 2 or {d.get("key") for d in drivers} != {"growth", "capex"}:
        raise ValueError("Specify the two operating drivers growth and capex.")
    specs = []
    for d in drivers:
        key = d["key"]
        mode = "percentage_points" if key == "growth" else "percent_change"
        if d.get("change_units") != mode:
            raise ValueError(f"{key}: use {mode}.")
        lo, hi = d.get("lower_change"), d.get("higher_change")
        if any(isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x) for x in (lo, hi)):
            raise ValueError(f"Choose lower_change and higher_change for {key}; no ranges have been assumed.")
        if not lo < 0 < hi:
            raise ValueError(f"{key}: lower_change must be negative, higher_change positive.")
        if not str(d.get("range_reason", "")).strip():
            raise ValueError(f"Record why you chose the {key} range (history or labelled judgment).")
        for case, shift in (("lower", lo), ("base", 0.0), ("higher", hi)):
            a = copy.deepcopy(BASE_INPUTS)
            if case != "base":
                a[key] = ([x + shift / 100 for x in BASE_INPUTS[key]] if key == "growth"
                          else [x * (1 + shift / 100) for x in BASE_INPUTS[key]])
            if key == "growth" and any(x <= -1 for x in a[key]):
                raise ValueError("Growth must remain above -100% in every year.")
            if key == "capex" and any(x < 0 for x in a[key]):
                raise ValueError("Capital spending cannot be negative.")
            specs.append(dict(driver=key, case=case, shift=shift, inputs=a,
                              change_units=mode, range_reason=d["range_reason"]))
    return specs

def compare_bases(first, last):
    max_difference = max(abs(x[k] - y[k]) for x, y in zip(first["rows"], last["rows"]) for k in x)
    same_inputs = first["inputs"] == last["inputs"] == BASE_INPUTS
    untouched = ASSUMPTIONS == BASE_INPUTS and OPENING == BASE_OPENING
    return dict(passed=first["valid"] and last["valid"] and same_inputs and untouched
                and max_difference <= TOLERANCE,
                same_inputs=same_inputs, original_model_unchanged=untouched,
                maximum_statement_difference=max_difference, tolerance=TOLERANCE)

def compute_spans(runs):
    spans = []
    for key in ("growth", "capex"):
        group = [r for r in runs if r["driver"] == key]
        valid = [r for r in group if r["valid"]]
        if not group:
            continue
        item = dict(driver=key, valid_count=len(valid), tested_count=len(group),
                    full_range_valid=len(valid) == 3)
        for metric in ("operating_profit", "fcfe"):
            values = [r[metric] for r in valid]
            item[metric] = max(values) - min(values) if len(values) >= 2 else None
        spans.append(item)
    return spans

def number(x, signed=False):
    if x is None:
        return "Unavailable"
    return format(x, "+,.4f" if signed else ",.4f")

def input_path(run):
    key = run["driver"]
    return ", ".join(f"{x*100:.6f}%" if key == "growth" else f"{x:,.2f}" for x in run["inputs"][key])


def build_analysis():
    """Reproduce the agreed one-at-a-time cases with independent deep copies."""
    base = evaluate("Base before analysis", BASE_INPUTS)
    if not base["valid"]:
        raise ValueError("Base is invalid: " + "; ".join(base["errors"]))
    specs = prepare_ranges(RANGES)
    runs = []
    for spec in specs:
        run = evaluate(f"{spec['driver']} / {spec['case']}", spec["inputs"],
                       spec["driver"], spec["case"])
        run["change_operating_profit"] = run["operating_profit"] - base["operating_profit"]
        run["change_fcfe"] = run["fcfe"] - base["fcfe"]
        runs.append(run)
    restored = evaluate("Restored base", BASE_INPUTS)
    return dict(
        run_timestamp_utc=datetime.now(timezone.utc).isoformat(),
        source_original_model_sha256=ORIGINAL_MODEL_SHA256,
        supplied_report_name=ORIGINAL_REPORT_NAME,
        supplied_report_sha256=ORIGINAL_REPORT_SHA256,
        opening=copy.deepcopy(BASE_OPENING), ranges=copy.deepcopy(RANGES),
        base=base, runs=runs, restored_base=restored,
        base_check=compare_bases(base, restored), spans=compute_spans(runs),
        prediction_copy_from_report=PREDICTION_TEXT,
        original_prediction_hash_as_recorded_in_report=ORIGINAL_RECORDED_PREDICTION_SHA256,
        value_note=VALUE_NOTE,
    )


def print_results(bundle):
    print("LAB 11 -- ORACLE SENSITIVITY | ETHAN D. HEERES | FIN 439")
    print("Reproduction run (UTC):", bundle["run_timestamp_utc"])
    print("All monetary outputs are USD millions. Negative FCFE is retained.")
    print("The original Lab 10 model and selected ranges are included in the Python file.")
    print("Written interpretation and partner exchanges: supplied completed Markdown.")
    print("JSON evidence is embedded at the end of this output; no separate JSON file is needed.")
    print("Value per share:", VALUE_NOTE)
    print("\nSENSITIVITY RESULTS -- FY2031")
    print("| Case | Actual FY2027-FY2031 input path | Operating profit | Change | Signed FCFE | Change | Status |")
    print("|---|---|---:|---:|---:|---:|---|")
    for r in bundle["runs"]:
        print(f"| {r['label']} | {input_path(r)} | {number(r['operating_profit'])} | "
              f"{number(r['change_operating_profit'], True)} | {number(r['fcfe'])} | "
              f"{number(r['change_fcfe'], True)} | {'PASS' if r['valid'] else 'INVALID; diagnostic only'} |")
    for driver in RANGES["drivers"]:
        print(f"\n{driver['key']}: {driver['lower_change']:+g} / {driver['higher_change']:+g} "
              f"{driver['change_units']}; applied to every forecast year.")
        print("Reason:", driver["range_reason"])
    print("\nVALID-SCENARIO SPANS (exclude invalid endpoints)")
    for s in bundle["spans"]:
        print(f"{s['driver']}: {s['valid_count']}/{s['tested_count']} usable; "
              f"operating-profit span {number(s['operating_profit'])}; FCFE span {number(s['fcfe'])}")
    if not all(s["full_range_valid"] for s in bundle["spans"]):
        print("Full-range ranking withheld: at least one endpoint fails funding constraints.")
    check = bundle["base_check"]
    print("\nRESTORED BASE:", "PASS" if check["passed"] else "FAIL")
    print("Maximum absolute difference across all statement cells:", check["maximum_statement_difference"])
    print("Same inputs:", check["same_inputs"])
    print("Original model inputs unchanged:", check["original_model_unchanged"])
    print("\nPRIOR PREDICTION -- copied from the supplied completed report")
    print(PREDICTION_TEXT)
    print("Original prediction SHA-256 as recorded in that report:", ORIGINAL_RECORDED_PREDICTION_SHA256)
    print("This reproduces the report's prior record; the original separate prediction file is not re-created or re-timestamped.")
    higher = next(r for r in bundle["runs"] if r["driver"] == "growth" and r["case"] == "higher")
    for metric, expected_rate in (("operating_profit", 1.02**5-1), ("fcfe", 1.04**5-1)):
        predicted = bundle["base"][metric] * (1+expected_rate)
        actual = higher[metric]
        change = (actual / bundle["base"][metric]-1)*100
        print(f"{metric}: predicted {predicted:,.4f}; actual {actual:,.4f}; "
              f"actual minus predicted {actual-predicted:+,.4f}; actual change from base {change:.4f}%")
    for run in [bundle["base"]] + bundle["runs"] + [bundle["restored_base"]]:
        print("\nRUN:", run["label"], "PASS" if run["valid"] else "INVALID; diagnostic only")
        print("Independent inputs:", json.dumps(run["inputs"], indent=2))
        print("Changed independent keys:", run["changed_independent_keys"])
        for title, lines in STATEMENT_LINES.items():
            print_table(title, run["rows"], lines)
        print("\nACCOUNTING AND FUNDING CHECKS (USD millions)")
        for c in run["checks"]:
            print(f"FY{c['year']}: " + "; ".join(f"{k}={v:.12g}" for k,v in c["gaps"].items()))
            print(f"  Cash {c['cash']:,.6f} / floor {c['cash_floor']:,.6f}; "
                  f"revolver {c['revolver']:,.6f} / limit {c['revolver_limit']:,.6f}")
        for error in run["errors"]:
            print("INVALID:", error)
    print("\nFULL-PRECISION JSON EVIDENCE")
    print(json.dumps(bundle, indent=2, allow_nan=False))
    print("\nAnalysis complete. Funding-invalid scenarios are reported as findings and excluded from usable spans.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().with_name("lab11_oracle_output.txt"))
    args = parser.parse_args()
    try:
        bundle = build_analysis()
        stream = io.StringIO()
        with redirect_stdout(stream):
            print_results(bundle)
        text = stream.getvalue()
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
        print(text, end="")
        return int(not bundle["base_check"]["passed"] or any(not r["valid"] for r in bundle["runs"]))
    except (ValueError, OSError, KeyError) as exc:
        parser.exit(2, f"Analysis could not run: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
