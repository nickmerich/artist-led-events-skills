---
name: sponsor-inventory-and-pricing
description: Packages brand partner inventory for an artist-led athletic event (title, presenting, activation, product, content, access, and series deals), prices it from costs and delivered value instead of follower counts, and checks category conflicts with the artist. Use for "what can we sell sponsors", "build sponsor tiers", "price this partnership", "what should we ask [brand] for", or turning an event plan into a partner menu.
metadata:
  library: artist-led-athletic-events
  version: "1.0"
---

# Sponsor Inventory and Pricing

Partners don't buy "exposure." They buy a specific useful thing at a specific moment for specific people. Sell that.

## Step 1: List the real inventory

Go through the format brief and run of show. Every moment where a partner could be **useful** is inventory.

| Inventory type | Examples | Useful version |
|----------------|----------|----------------|
| **Title** | "[Brand] presents [Artist]'s [Event]" | One per event. Needs artist approval. |
| **Activation** | Coffee table, hydration station, recovery tent, shakeout warm-up | They solve a real need at the event. |
| **Product** | Product in hand, sampling, gear for leaders | Something people use that day. |
| **Access** | Funds free entry for N people ("100 free spots, covered by [Brand]") | Strongest story: the partner opened the door. |
| **Content** | Named segment in the recap video, behind-the-scenes series | Delivered assets with clear usage rights. |
| **Data and follow-up** | Opt-in offer to participants who check a box | Only with explicit, separate consent. Never hand over the list. |
| **Series** | Same partner across a season or multiple cities | Discounted per event, longer commitment. |
| **Community** | Presenting partner of the recurring weekly run or club | Builds year-round value beyond one day. |

Cut anything that makes the experience worse: forced booths in the start corral, mandatory stops, logos on everything.

## Step 2: Price it

Price from two floors and one ceiling:

1. **Cost floor:** what the inventory costs you to deliver (staff time, product handling, space, content editing) plus your margin.
2. **Funding floor:** the share of the budget this partner needs to cover. If the event is free, partners together need to cover the full budget (see `event-budget-pnl`).
3. **Value ceiling:** what the delivered outcome is worth to the brand: verified people reached in person, sampled product, content assets with usage rights, local relevance. Use verified or conservatively assumed numbers only.

Price inside that range. Round to clean numbers. Write a tier menu with 3 to 5 options and one custom option.

**Never price from follower counts.** In-person participants, product in hand, and usable content are the value.

## Step 3: Conflict check (required)

For every prospect:
- Against the artist's existing deals and exclusivities (from `artist-deal-terms`).
- Against other partners in the same event (one per category unless agreed).
- Against venue rules (some venues have pouring rights or ban sampling; trails may ban sales and giveaways).
- Against the audience: no alcohol or age-restricted products in all-ages or athletic portions; nothing that undercuts the safety message.

If a conflict appears, swap the category, don't stall.

## Step 4: Write the menu

Use `assets/inventory-menu.md`. Each item states: what the partner gets, what they provide (cash, product, both), the exact deliverables, approvals required, and any limits.

## Fiscal sponsorship note

If an event runs through a nonprofit or fiscal sponsor, some contributions may be tax-deductible for the partner. Only say so when the fiscal sponsor relationship is approved and the specific contribution qualifies. Keep commercial benefits (logos, sampling, ads) and charitable gifts separate; ask the fiscal sponsor how they want it structured.

## Output

A filled inventory menu, the price logic for each line, and the conflict check results.
