# Artist-Led Athletic Events: Agent Skills

A skills library for producing athletic events led by artists: runs, walks, rides, pickup games, carries, pull-up challenges, and whatever sport comes next. Each skill teaches an AI agent (or a human producer) how to do one part of the job well: pick the right concept, design the format, fund it with brand partners, keep people safe, run the day, and report honestly afterward.

Built by [GRYT Run Club](https://grytrunclub.com) from producing weekly community runs and artist-led events in Pittsburgh. The standard we hold ourselves to: **the artist brings the reason to show up, the producer makes it safe and easy, partners pay for something useful, and nobody gets left behind.**

## Who this is for

- **Artists and their teams** who want to do something physical with their fans that isn't a meet-and-greet.
- **Producers and run/ride/sport clubs** who handle the operations.
- **Brand partners** who want to fund real participation instead of a logo on a banner.
- **Agents** (Claude, Codex, Perplexity, Cursor, anything that reads `SKILL.md`) doing the planning, drafting, and checking.

## The skills

| # | Skill | Use it to |
|---|-------|-----------|
| 0 | [`event-producer`](skills/event-producer/SKILL.md) | Run the whole production. Routes to every other skill and enforces the go/no-go gates. Start here. |
| 1 | [`artist-fit-and-concept`](skills/artist-fit-and-concept/SKILL.md) | Decide if an artist and a concept belong together, using a five-question evidence scorecard. |
| 2 | [`sport-format-design`](skills/sport-format-design/SKILL.md) | Turn "let's do a basketball thing" into a format with capacity, staffing, scoring, and adaptations. Ships with seven sport references and a template for any new sport. |
| 3 | [`artist-deal-terms`](skills/artist-deal-terms/SKILL.md) | Write the artist side: role, time ask, money, name and likeness approvals, content rights, conflicts. |
| 4 | [`event-budget-pnl`](skills/event-budget-pnl/SKILL.md) | Build the budget, break-even, and profit split with deterministic math (`scripts/pnl.py`). |
| 5 | [`sponsor-inventory-and-pricing`](skills/sponsor-inventory-and-pricing/SKILL.md) | Package what partners actually get, price it, and check category conflicts. |
| 6 | [`sponsor-outreach-and-close`](skills/sponsor-outreach-and-close/SKILL.md) | Find, pitch, and close partners without overpromising. |
| 7 | [`permits-insurance-and-risk`](skills/permits-insurance-and-risk/SKILL.md) | Permits, insurance, waivers, medical, weather calls (lightning, heat, cold), and the risk register. |
| 8 | [`registration-and-capacity`](skills/registration-and-capacity/SKILL.md) | Free or paid, numbered tickets, waitlists, consent, check-in, and honest counts. |
| 9 | [`launch-campaign`](skills/launch-campaign/SKILL.md) | A six-week, artist-audience-first launch with claim rules. |
| 10 | [`run-of-show-and-staffing`](skills/run-of-show-and-staffing/SKILL.md) | Roles, ratios, volunteer briefs, minute-by-minute run of show, radio plan. |
| 11 | [`content-capture-and-rights`](skills/content-capture-and-rights/SKILL.md) | Shot list, releases, music rights in video, minors, approvals. |
| 12 | [`recap-and-sponsor-report`](skills/recap-and-sponsor-report/SKILL.md) | Verified recap, sponsor report, renewal ask, and the return-rate follow-up. |
| 13 | [`press-and-media`](skills/press-and-media/SKILL.md) | Earn press and podcast coverage: proof table, cleared quotes, one angle per outlet type, stated pitch routes, replies tracked instead of sends. |

## Sports covered

Each lives in [`skills/sport-format-design/references/sports/`](skills/sport-format-design/references/sports/):

- [Running](skills/sport-format-design/references/sports/running.md): community 5K, artist 5K, shakeout, conference morning run
- [Walking and rucking](skills/sport-format-design/references/sports/walking-rucking.md): city walks, ruck marches, walk/roll formats
- [Cycling](skills/sport-format-design/references/sports/cycling.md): no-drop social rides, gravel, indoor ride sets
- [Basketball](skills/sport-format-design/references/sports/basketball.md): 3x3 runs, shootarounds, skills challenges
- [Soccer](skills/sport-format-design/references/sports/soccer.md): small-sided pickup, futsal, juggling challenges
- [Weighted carries](skills/sport-format-design/references/sports/weighted-carries.md): farmer's walks, sandbag and ruck carries
- [Pull-ups](skills/sport-format-design/references/sports/pull-ups.md): group-total challenges like 500 pull-ups, scaled for every level
- [Any other sport](skills/sport-format-design/references/sports/_new-sport-template.md): the template. Fill it in and the rest of the skills work unchanged.

## Workflows and examples

- [12-week production timeline](workflows/12-week-production-timeline.md)
- [Go/no-go gates](workflows/go-no-go-gates.md)
- [Day-of command checklist](workflows/day-of-command.md)
- [Press activation by market](workflows/press-activation-by-market.md): home market, event markets, national layer
- [Worked example: a hypothetical artist 5K, start to finish](examples/hypothetical-artist-5k.md)
- [Evidence rules](docs/evidence-rules.md): how every skill separates facts, assumptions, and asks

## Install

Skills follow the open [Agent Skills format](https://agentskills.io/specification): a folder with a `SKILL.md` that has `name` and `description` frontmatter.

**Claude Code, one command:**

```
/plugin marketplace add nickmerich/artist-led-events-skills
/plugin install artist-led-events-skills@artist-led-events-skills
```

**Any agent that reads `SKILL.md`** (Claude apps, Codex, Cursor, Gemini CLI, Copilot, Perplexity):

```bash
git clone https://github.com/nickmerich/artist-led-events-skills
# Copy or symlink skills into your skills directory
cp -r skills/* ~/.claude/skills/
# Any other agent: point it at the skills/ folder, or paste a SKILL.md into context
```

Validate after editing (every skill also passes `skills-ref validate` from the [Agent Skills reference library](https://github.com/agentskills/agentskills)):

```bash
python3 scripts/validate_skills.py
python3 skills/event-budget-pnl/scripts/pnl.py examples/hypothetical-budget.csv --headcount 125
```

## Ground rules every skill follows

1. **Shared effort over spectacle.** No VIP pens, no fastest-finisher worship, no event that only works if you got a selfie with the artist. The line: "We won. Together."
2. **The doorway stays open.** Every format has a walk, scaled, or no-equipment version. Pace and skill are never the price of entry.
3. **Facts, assumptions, and asks stay separate.** RSVPs are not attendance. Followers are not fans who'll show up. Pipeline is not revenue. A sent email is not a yes.
4. **Safety decisions are written down before the day,** with a named person who makes the call.
5. **Names, likeness, music, and member content need permission in writing** before public use.
6. **Math happens outside the model.** Budgets, splits, and counts run through scripts or spreadsheets, not vibes.
7. **Humans approve anything that sends, publishes, spends, signs, or commits.**

## Not legal, medical, or insurance advice

These skills tell you what to ask and who to ask. Permit authorities, your insurance broker, local EMS, a licensed medical lead, and a lawyer make the actual calls for your event.

## Contributing

Add a sport, fix a skill, share what broke on your event day. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
