# Contributing

The best contributions come from events that actually happened.

## Add a sport

1. Copy `skills/sport-format-design/references/sports/_new-sport-template.md` to `<sport>.md`.
2. Fill in every section. If you don't know something (staffing ratio, permit authority), write `UNKNOWN: ask <who>` instead of guessing.
3. Add the sport to the list in `README.md` and in `skills/sport-format-design/SKILL.md`.
4. Run `python3 scripts/validate_skills.py`.

## Improve a skill

- Keep each `SKILL.md` under 500 lines. Move detail into `references/` or `assets/`.
- `name` must match the folder name: lowercase, numbers, single hyphens.
- `description` says what it does **and when to use it**, in under 1,024 characters.
- Write plainly. No em dashes, no hype words, no invented numbers.

## Share a lesson

Open an issue titled `Lesson: <what happened>` with: the format, headcount (verified or estimated, say which), what broke, what you'd change. Lessons that hold up get folded into the relevant skill.

## Never commit

Participant names, emails, phone numbers, waivers, medical info, emergency contacts, unpublished photos, contracts, or sponsor pricing someone asked you to keep private.
