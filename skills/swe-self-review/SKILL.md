---
name: swe-self-review
description: "Self-review your own change before asking for review or declaring work done, using swe-docs. Use after implementing and before handing back."
---

# Self-review with swe-docs

Uses `docs/guidelines` from swe-docs (<https://github.com/cs-clarence/swe-docs>). If it is missing, say so and stop; do not invent rules. Repo overrides win (`docs/guidelines/core/precedence.md`). If a skill named below is not installed, follow the guideline files it covers.

1. Read `docs/guidelines/authoring/self-review.md` and `core/definition-of-done.md`.
2. Walk the diff against them; for risky areas read the matching `reviewing/checks/` file.
3. Run only the checks the change can affect while working. For work split between agents, run the broad checks once after the parts are combined (`planning/agents.md#run-the-broad-checks-once-at-integration`), and for a delegated part report which checks you ran and which you did not.
4. Fix issues found, then report what was checked and anything left open.
