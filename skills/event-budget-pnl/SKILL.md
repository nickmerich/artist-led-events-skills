---
name: event-budget-pnl
description: Builds an artist-led athletic event budget, break-even point, contribution target, and profit split using deterministic math from a CSV, not model estimates. Use for "what will this cost", "build the budget", "how many tickets to break even", "can partners fund it free", "what's the profit split", or checking whether a plan's numbers add up. Labels every line as quoted, estimated, or committed.
metadata:
  library: artist-led-athletic-events
  version: "1.0"
---

# Event Budget and P&L

Do the arithmetic in code. Your job is to get the right lines in the sheet and label how sure each number is.

## Step 1: Fill the budget

Copy `assets/budget-template.csv`. Columns:

- `type`: `cost` or `revenue`
- `category`: see categories below
- `item`, `qty`, `unit_amount`
- `basis`: `fixed` (once) or `per_participant` (qty is ignored; multiplied by headcount)
- `status`: `committed` (signed or paid), `quoted` (written quote), `estimate`
- `source`: link or note

Cost categories that get forgotten: insurance add-ons and additional insured fees, permit fees and deposits, music licensing, restrooms, cleanup and trash, medical staffing, radios, signage, payment processing fees, platform fees, volunteer food and shirts, photographer and editor, contingency.

Always include a **contingency** line: 10% of costs is a reasonable starting assumption for a first event.

## Step 2: Run the numbers

```bash
python3 scripts/pnl.py path/to/budget.csv --headcount 100 --split 0.5
```

The script reports: total costs, total revenue, profit, break-even headcount for paid entry, partner revenue as a share of costs, split amounts, and how much of the budget is only an estimate.

## Step 3: Pick the funding shape

| Shape | Rule of thumb |
|-------|---------------|
| **Free, partner-funded** | Committed partner revenue covers 100% of committed and quoted costs before announcing free entry. |
| **Paid entry** | Price so break-even sits at or below a conservative show/sell assumption, not at capacity. |
| **Hybrid** | Partners cover fixed costs; entry covers per-person costs. |
| **Self-funded pilot** | Cap the loss in advance and write it down. |

A **contribution target** (for example, 25% margin after costs) is a goal, not a forecast. Label it.

## Step 4: Sanity checks before sharing

- More than 40% of costs still `estimate` two weeks before announcing? Get quotes.
- Any revenue line `estimate`? It isn't money. Show the plan with and without it.
- Profit split math uses profit **after** the agreed cost categories in the artist term sheet.
- Fiscal sponsor or nonprofit fees, if money passes through one, are a cost line.

## Output

The filled CSV, the script output, and a three-line summary: what it costs, who's paying, what's still a guess.
