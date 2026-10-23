#!/usr/bin/env python3
"""Deterministic P&L for an artist-led event budget CSV.

Usage: python3 pnl.py budget.csv [--headcount N] [--split 0.5]

CSV columns: type,category,item,qty,unit_amount,basis,status,source
  type: cost | revenue
  basis: fixed | per_participant (qty ignored, multiplied by headcount)
  status: committed | quoted | estimate
"""
import argparse
import csv
import math
import sys


def load(path):
    try:
        with open(path, newline="") as f:
            rows = list(csv.DictReader(f))
    except FileNotFoundError:
        sys.exit(f"Budget file not found: {path}")
    required = {"type", "category", "item", "qty", "unit_amount", "basis", "status"}
    if not rows or not required.issubset(rows[0].keys()):
        sys.exit(f"CSV must have columns: {', '.join(sorted(required))}")
    return rows


def num(value, field, row_no):
    try:
        return float(value or 0)
    except ValueError:
        sys.exit(f"Row {row_no}: '{field}' must be a number, got '{value}'")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--headcount", type=int, default=100, help="planned participants")
    ap.add_argument("--split", type=float, default=0.5, help="producer share of profit (0-1)")
    a = ap.parse_args()
    if not 0 <= a.split <= 1:
        sys.exit("--split must be between 0 and 1")

    rows = load(a.csv)
    totals = {"cost": 0.0, "revenue": 0.0}
    fixed_cost = var_cost = fixed_rev = 0.0
    entry_per_person = 0.0
    estimate_cost = 0.0
    partner_committed = 0.0
    by_status = {}

    for i, r in enumerate(rows, start=2):
        t = r["type"].strip().lower()
        if t not in totals:
            sys.exit(f"Row {i}: type must be cost or revenue")
        basis = r["basis"].strip().lower()
        unit = num(r["unit_amount"], "unit_amount", i)
        qty = num(r["qty"], "qty", i)
        status = r["status"].strip().lower()
        amount = unit * a.headcount if basis == "per_participant" else unit * qty
        totals[t] += amount
        by_status.setdefault((t, status), 0.0)
        by_status[(t, status)] += amount
        if t == "cost":
            if basis == "per_participant":
                var_cost += unit
            else:
                fixed_cost += amount
            if status == "estimate":
                estimate_cost += amount
        else:
            if basis == "per_participant" and r["category"].strip().lower() == "entry":
                entry_per_person += unit
            else:
                fixed_rev += amount
            if r["category"].strip().lower() == "partner" and status == "committed":
                partner_committed += amount

    profit = totals["revenue"] - totals["cost"]
    print(f"Headcount assumed: {a.headcount}")
    print(f"Total costs:       ${totals['cost']:,.2f}")
    print(f"Total revenue:     ${totals['revenue']:,.2f}")
    print(f"Profit (loss):     ${profit:,.2f}")
    if totals["cost"]:
        print(f"Costs still estimates: {estimate_cost / totals['cost']:.0%}")
        print(f"Committed partner revenue covers: {partner_committed / totals['cost']:.0%} of costs")
    margin = entry_per_person - var_cost
    if entry_per_person > 0:
        if margin <= 0:
            print("Break-even: never. Entry price is at or below per-person cost.")
        else:
            need = max(0.0, fixed_cost - fixed_rev)
            print(f"Break-even paid headcount: {math.ceil(need / margin)}")
    if profit > 0:
        print(f"Producer share ({a.split:.0%}): ${profit * a.split:,.2f}")
        print(f"Partner/artist share ({1 - a.split:.0%}): ${profit * (1 - a.split):,.2f}")
    print("\nBy status:")
    for (t, s), v in sorted(by_status.items()):
        print(f"  {t:8} {s:10} ${v:,.2f}")
    rev_est = by_status.get(("revenue", "estimate"), 0.0)
    if rev_est:
        print(f"\nWarning: ${rev_est:,.2f} of revenue is an estimate. Without it, profit is ${profit - rev_est:,.2f}.")


if __name__ == "__main__":
    main()
