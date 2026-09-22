"""FIN 439 Lab 09: ABG three-statement projection and FCFE valuation.

All dollar amounts are USD millions, except value per share.
Run: python proforma.py
Demonstrate the required failure: python proforma.py --break-check
Uses the supplied lab assumptions, not independently verified company data.
"""

import argparse
import math


YEARS = [2026, 2027, 2028, 2029, 2030]
TOLERANCE = 0.000001  # Ignore tiny floating-point differences in USD millions.

OPENING = {
    "revenue": 17999.0,
    "inventory": 2135.8,
    "ppe": 3070.4,
    "other_assets": 6371.6,
    "cash": 40.4,
    "floor_plan": 2027.0,
    "debt": 3572.0,
    "revolver": 0.0,
    "other_liabilities": 2127.5,
    "equity": 3891.7,
}

ASSUMPTIONS = {
    "growth": 0.018,
    "gross_margin": 0.1705,
    "sga_ratios": [0.665, 0.655, 0.645, 0.645, 0.645],
    "depreciation_ratio": 82.4 / 3070.4,
    "impairment": 120.0,
    "capex": 250.0,
    "tax_rate": 0.255,
    "inventory_days": 2135.8 / (17999.0 - 3071.7) * 365,
    "floor_plan_ratio": 2027.0 / 2135.8,
    "other_wc_ratio": 0.008,
    "minimum_cash": 25.0,
    "revolver_limit": 850.0,
    "revolver_rate": 0.06,
    "repayment": 150.0,
    "buyback": 150.0,
    "floor_plan_rate": 0.0467,
    "debt_rate": 0.0544,
    "cost_of_equity": 0.10,
    "terminal_growth": 0.025,
    "shares": 17.951349,  # Millions of shares, held fixed for this lab.
}


def total_assets(row):
    return row["cash"] + row["inventory"] + row["ppe"] + row["other_assets"]


def total_liabilities(row):
    return (row["floor_plan"] + row["debt"] + row["revolver"]
            + row["other_liabilities"])


def balance_gap(row):
    # Recompute from the balances so changing cash cannot bypass the check.
    return total_assets(row) - total_liabilities(row) - row["equity"]


def project(opening, assumptions):
    """Build each year's statements in the order specified by the lab."""
    a = assumptions
    prior = opening.copy()
    projections = []

    for index, year in enumerate(YEARS):
        # 1. Income statement. Interest uses OPENING financing balances.
        revenue = prior["revenue"] * (1 + a["growth"])
        gross_profit = revenue * a["gross_margin"]
        cost_of_sales = revenue - gross_profit
        sga = gross_profit * a["sga_ratios"][index]
        depreciation = prior["ppe"] * a["depreciation_ratio"]
        impairment = a["impairment"]
        operating_income = gross_profit - sga - depreciation - impairment
        interest = (prior["floor_plan"] * a["floor_plan_rate"]
                    + prior["debt"] * a["debt_rate"]
                    + prior["revolver"] * a["revolver_rate"])
        pretax_income = operating_income - interest
        tax = max(0.0, pretax_income) * a["tax_rate"]
        net_income = pretax_income - tax

        # 2. Balance sheet, leaving cash until the cash flows are known.
        inventory = cost_of_sales * a["inventory_days"] / 365
        floor_plan = inventory * a["floor_plan_ratio"]
        ppe = prior["ppe"] + a["capex"] - depreciation
        change_other_wc = a["other_wc_ratio"] * (revenue - prior["revenue"])
        other_assets = prior["other_assets"] + change_other_wc - impairment
        debt = prior["debt"] - a["repayment"]
        other_liabilities = prior["other_liabilities"]
        equity = prior["equity"] + net_income - a["buyback"]

        # 3. Cash flow. Floor-plan borrowing is operating for this lab.
        change_inventory = inventory - prior["inventory"]
        change_floor_plan = floor_plan - prior["floor_plan"]
        operating_cash_flow = (net_income + depreciation + impairment
                               - change_inventory - change_other_wc
                               + change_floor_plan)
        fcfe = operating_cash_flow - a["capex"] - a["repayment"]
        cash = prior["cash"] + fcfe - a["buyback"]

        # Draw only what is needed; use surplus cash to repay the revolver.
        revolver = prior["revolver"]
        if cash < a["minimum_cash"]:
            draw = min(a["minimum_cash"] - cash,
                       max(0.0, a["revolver_limit"] - revolver))
            revolver += draw
            cash += draw
        elif cash > a["minimum_cash"]:
            repayment = min(revolver, cash - a["minimum_cash"])
            revolver -= repayment
            cash -= repayment

        change_revolver = revolver - prior["revolver"]
        investing_cash_flow = -a["capex"]
        financing_cash_flow = -a["repayment"] - a["buyback"] + change_revolver
        change_cash = operating_cash_flow + investing_cash_flow + financing_cash_flow

        row = {
            "year": year, "revenue": revenue, "cost_of_sales": cost_of_sales,
            "gross_profit": gross_profit, "sga": sga,
            "depreciation": depreciation, "impairment": impairment,
            "operating_income": operating_income, "interest": interest,
            "pretax_income": pretax_income, "tax": tax, "net_income": net_income,
            "inventory": inventory, "floor_plan": floor_plan, "ppe": ppe,
            "other_assets": other_assets, "debt": debt,
            "other_liabilities": other_liabilities, "equity": equity,
            "opening_cash": prior["cash"], "cash": cash, "revolver": revolver,
            "change_inventory": change_inventory, "change_other_wc": change_other_wc,
            "change_floor_plan": change_floor_plan, "change_revolver": change_revolver,
            "operating_cash_flow": operating_cash_flow,
            "investing_cash_flow": investing_cash_flow,
            "financing_cash_flow": financing_cash_flow, "change_cash": change_cash,
            "capex": a["capex"], "repayment": a["repayment"],
            "buyback": a["buyback"], "fcfe": fcfe,
        }
        # Calculate both required checks immediately after each year.
        row["balance_gap"] = balance_gap(row)
        row["cash_above_minimum"] = cash - a["minimum_cash"]
        projections.append(row)
        prior = row

    return projections


def assert_balanced(projections, assumptions):
    """Refuse valuation if any year fails the accounting or liquidity checks."""
    for row in projections:
        year = row["year"]
        gap = balance_gap(row)
        if not math.isfinite(gap) or abs(gap) > TOLERANCE:
            raise ValueError(f"FY{year}E: balance sheet gap = {gap:,.1f} million")
        cash_gap = row["cash"] - assumptions["minimum_cash"]
        if not math.isfinite(cash_gap) or cash_gap < -TOLERANCE:
            raise ValueError(f"FY{year}E: cash below minimum; gap = {cash_gap:,.1f} million")
        revolver = row["revolver"]
        if (not math.isfinite(revolver) or revolver < -TOLERANCE
                or revolver > assumptions["revolver_limit"] + TOLERANCE):
            raise ValueError(f"FY{year}E: revolver outside permitted range: {revolver:,.1f}")


def print_table(title, projections, lines):
    """Print years across columns; round for display only."""
    print(f"\n{title} (USD millions)")
    print(f"{'':<35}" + "".join(f"{'FY' + str(r['year']) + 'E':>14}" for r in projections))
    for label, calculation in lines:
        values = [calculation(row) for row in projections]
        values = [0.0 if abs(value) < TOLERANCE else value for value in values]
        print(f"{label:<35}" + "".join(f"{value:>14,.1f}" for value in values))


def print_statements(rows, a):
    print_table("INCOME STATEMENT", rows, [
        ("Revenue", lambda r: r["revenue"]),
        ("Cost of sales", lambda r: r["cost_of_sales"]),
        ("Gross profit", lambda r: r["gross_profit"]),
        ("SG&A", lambda r: r["sga"]),
        ("Depreciation", lambda r: r["depreciation"]),
        ("Impairment", lambda r: r["impairment"]),
        ("Operating income", lambda r: r["operating_income"]),
        ("Interest expense", lambda r: r["interest"]),
        ("Pretax income", lambda r: r["pretax_income"]),
        ("Tax expense", lambda r: r["tax"]),
        ("Net income", lambda r: r["net_income"]),
    ])
    print_table("BALANCE SHEET", rows, [
        ("Cash", lambda r: r["cash"]),
        ("Inventory", lambda r: r["inventory"]),
        ("PP&E", lambda r: r["ppe"]),
        ("Other assets", lambda r: r["other_assets"]),
        ("Total assets", total_assets),
        ("Floor plan (inventory loans)", lambda r: r["floor_plan"]),
        ("Term debt", lambda r: r["debt"]),
        ("Revolver", lambda r: r["revolver"]),
        ("Other liabilities", lambda r: r["other_liabilities"]),
        ("Total liabilities", total_liabilities),
        ("Equity", lambda r: r["equity"]),
        ("Total liabilities + equity", lambda r: total_liabilities(r) + r["equity"]),
    ])
    print_table("CASH FLOW STATEMENT", rows, [
        ("Net income", lambda r: r["net_income"]),
        ("+ Depreciation", lambda r: r["depreciation"]),
        ("+ Impairment", lambda r: r["impairment"]),
        ("- Change in inventory", lambda r: -r["change_inventory"]),
        ("- Change in other working capital", lambda r: -r["change_other_wc"]),
        ("+ Change in floor plan", lambda r: r["change_floor_plan"]),
        ("Operating cash flow", lambda r: r["operating_cash_flow"]),
        ("Investing cash flow (capex)", lambda r: r["investing_cash_flow"]),
        ("Term debt repayment", lambda r: -r["repayment"]),
        ("Share buybacks", lambda r: -r["buyback"]),
        ("Revolver draw / (repayment)", lambda r: r["change_revolver"]),
        ("Financing cash flow", lambda r: r["financing_cash_flow"]),
        ("Change in cash", lambda r: r["change_cash"]),
        ("Opening cash", lambda r: r["opening_cash"]),
        ("Closing cash", lambda r: r["cash"]),
        ("FCFE (before buybacks/revolver)", lambda r: r["fcfe"]),
    ])
    print_table("CHECKS", rows, [
        ("Assets - liabilities - equity", balance_gap),
        ("Cash", lambda r: r["cash"]),
        ("Cash above minimum", lambda r: r["cash"] - a["minimum_cash"]),
    ])
    for row in rows:
        balanced = abs(balance_gap(row)) <= TOLERANCE
        cash_ok = row["cash"] >= a["minimum_cash"] - TOLERANCE
        print(f"FY{row['year']}E: balance {'PASS' if balanced else 'FAIL'}; "
              f"minimum cash {'PASS' if cash_ok else 'FAIL'}")


def value_equity(rows, assumptions):
    """Discount FCFE and the lab's repayment-adjusted terminal value."""
    # Enforce checks even when this function is called outside main().
    assert_balanced(rows, assumptions)
    cost_of_equity = assumptions["cost_of_equity"]
    terminal_growth = assumptions["terminal_growth"]
    if cost_of_equity <= terminal_growth:
        raise ValueError("Cost of equity must exceed terminal growth.")
    pv_fcfe = sum(row["fcfe"] / (1 + cost_of_equity) ** year
                  for year, row in enumerate(rows, start=1))
    terminal_fcfe = (rows[-1]["fcfe"] + rows[-1]["repayment"]) * (1 + terminal_growth)
    terminal_value = terminal_fcfe / (cost_of_equity - terminal_growth)
    pv_terminal = terminal_value / (1 + cost_of_equity) ** len(rows)
    equity_value = pv_fcfe + pv_terminal
    return equity_value, pv_terminal / equity_value, equity_value / assumptions["shares"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--break-check", action="store_true",
                        help="Set FY2026E cash to 40.4; expect a -61.4 gap and refusal.")
    args = parser.parse_args()
    rows = project(OPENING, ASSUMPTIONS)
    if args.break_check:
        rows[0]["cash"] = OPENING["cash"]
        print("BREAK TEST: FY2026E cash changed to the opening 40.4.")

    print_statements(rows, ASSUMPTIONS)
    assert_balanced(rows, ASSUMPTIONS)
    equity_value, terminal_share, value_per_share = value_equity(rows, ASSUMPTIONS)
    print("\nVALUATION")
    print(f"Equity value (USD millions): ${equity_value:,.2f}")
    print(f"Share of value after 2030: {terminal_share:.2%}")
    print(f"Value per share: ${value_per_share:,.2f}")


if __name__ == "__main__":
    main()
