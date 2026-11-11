---
name: swe-review
description: "Review a change, diff or pull request using the swe-docs reviewing checks. Use when asked to review code, a plan, or agent output."
---

# Review with swe-docs

Uses `docs/guidelines` from swe-docs (<https://github.com/cs-clarence/swe-docs>). If it is missing, say so and stop; do not invent rules. Repo overrides win (`docs/guidelines/core/precedence.md`). If a skill named below is not installed, follow the guideline files it covers.

1. Read `docs/guidelines/reviewing/process.md` and `reviewing/feedback.md`.
2. Use `reviewing/by-tier.md` to pick checks for the change's risk tier, then read the matching files in `reviewing/checks/`.
3. High-risk security changes: `reviewing/checks/threat-review.md`. Plans: `reviewing/checks/planning/`.
4. If you are an agent doing the review, read `reviewing/agents.md` whatever the author was; it also covers reviewing agent output.
5. If work was split between agents, check it against `reviewing/checks/planning/agents.md`. At High risk, confirm every agent-authored part was checked by someone other than its author.
6. Report findings in the format from `reviewing/feedback.md`.
