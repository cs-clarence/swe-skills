---
name: swe-self-review
description: "Self-review your own change before asking for review or declaring work done, using swe-docs. Use after implementing and before handing back."
---

# Self-review with swe-docs

Guidelines live in `docs/guidelines` of the current repository (installed from <https://github.com/cs-clarence/swe-docs>). If that folder is missing, tell the user and point them to the swe-docs README install section; do not invent rules. Repository overrides take precedence per `docs/guidelines/core/precedence.md`. Scale effort to risk using `docs/guidelines/core/risk-tiers.md`.

1. Read `docs/guidelines/authoring/self-review.md` and `core/definition-of-done.md`.
2. Walk the diff against them; for risky areas read the matching `reviewing/checks/` file.
3. Fix issues found, then report what was checked and anything left open.
