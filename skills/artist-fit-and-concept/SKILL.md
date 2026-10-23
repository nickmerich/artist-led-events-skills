---
name: artist-fit-and-concept
description: Evaluates whether an artist and an athletic event concept belong together before anyone spends money, using eligibility checks and a five-question evidence scorecard with routing rules. Use for "should we do an event with [artist]", "score this artist", "which artist should we pitch", "is this concept authentic", or ranking a list of artist prospects. Produces a scored evidence packet and a next stage, never a launch approval.
metadata:
  library: artist-led-athletic-events
  version: "1.0"
---

# Artist Fit and Concept

The best artist-led events feel like the artist was going to do this anyway and invited you. The worst feel like a brand deal with a finish line. This skill tells them apart with evidence.

## Step 1: Eligibility (pass/fail, before scoring)

For a produced public event (not a small private pilot), the artist should show:

1. **Current activity:** releasing, touring, or actively building an audience now.
2. **A real practice:** recent public evidence they do the activity or something hard and physical regularly. Posts, interviews, race results, gym clips.
3. **Local pull:** evidence they can bring people in person in this city. Past show attendance, local fan groups, a hometown story. Set the bar to the format: for a produced 5K, aim for evidence of at least 50 people who'd come because of the artist.
4. **A reachable decision-maker:** artist, manager, or agent who can say yes.

If an item fails, the right move is usually a smaller format (a private run with the artist and 15 club members, a one-week fan challenge), not lowering the bar. Say so.

## Step 2: Build the evidence packet

Use `assets/evidence-packet.md`. Every claim gets a source link or a label (VERIFIED, REPORTED, ASSUMPTION, UNKNOWN).

## Step 3: Score five questions

Each question is scored independently: **Supported (2), Partial (1), Not Met (0), Unknown (unscored)**. Unknown is never treated as a pass.

| # | Question | Supported looks like |
|---|----------|----------------------|
| Q1 | **Authenticity:** Does evidence show this reflects the artist's current practice or a real personal goal? | Multiple recent, unprompted posts or statements about the activity. |
| Q2 | **Shared participation:** Can fans take part alongside the artist, at their own level, and meet each other? | Format has scaled/walk/no-equipment options and a reason fans talk to each other, not just watch. |
| Q3 | **Artist commitment:** Has the artist or their team agreed to a specific role in writing? | Email or message from the decision-maker naming date, role, and time. |
| Q4 | **Demand evidence:** Does observed demand support the headcount target? | Waitlist signups, poll responses, past event turnout, or a soft RSVP test at 1.5x the target. |
| Q5 | **Production readiness:** Is there an operating plan and budget a producer would sign off on? | Format brief, budget with break-even, venue path, insurance path, owner named. |

## Step 4: Route

Apply in order. First match wins.

1. Any **Not Met** → **Hold / Redesign.** Name the failing question and the redesign that could fix it.
2. Q1 **Unknown** → **Research.** Find authenticity evidence before contacting anyone.
3. Q1 **Partial** or Q3 **Unknown** → **Discovery.** A short call or message with the artist team.
4. Q2 not Supported, Q3 Partial, or Q5 not Supported → **Pilot Design.** Work the format, deal, or plan.
5. Q1, Q2, Q3, Q5 Supported and Q4 Partial/Unknown → **Demand Validation.** Run a soft RSVP or waitlist test.
6. All five Supported → **Final Review** by the human decision-maker. This is not launch approval.

The routing is deterministic. If you have a script environment, compute it in code rather than by judgment.

## Step 5: Concept line

Write the concept in one sentence a fan would repeat: **[Artist] is [doing the hard thing] with [who], in [place], because [true reason].** If the "because" isn't true and sourced, go back to Q1.

## Discovery call questions (Q1, Q3)

- What do you actually do to stay moving right now? How often?
- Have you ever done something like this with fans? What did you like or hate about it?
- What would make this feel like yours and not a brand activation?
- How much time can you give on the day? Before the day?
- Any brand deals, exclusivities, or sensitivities we need to know? (Feeds the conflict check.)
- Who signs off on announcements and your name and likeness?

## Red flags

- The artist's only connection to the sport is a sponsor's request.
- The plan only works if the artist does a meet-and-greet line.
- The headcount target came from follower count.
- "We'll figure out the venue after we announce."

## Output

A packet with: eligibility results, the five scores with evidence, the route, the concept line, and one next action with an owner.
