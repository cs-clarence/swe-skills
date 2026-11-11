---
name: swe-review
description: "Review a change, diff or pull request using the swe-docs reviewing checks. Use when asked to review code, a plan, or agent output."
---

# Review with swe-docs

Guidelines live in `docs/guidelines` of the current repository (installed from <https://github.com/cs-clarence/swe-docs>). If that folder is missing, tell the user and point them to the swe-docs README install section; do not invent rules. Repository overrides take precedence per `docs/guidelines/core/precedence.md`. Scale effort to risk using `docs/guidelines/core/risk-tiers.md`.

1. Read `docs/guidelines/reviewing/process.md` and `reviewing/feedback.md`.
2. Use `reviewing/by-tier.md` to pick checks for the change's risk tier, then read the matching files in `reviewing/checks/`.
3. High-risk security changes: `reviewing/checks/threat-review.md`. Plans: `reviewing/checks/planning/`.
4. If you are an agent doing the review, read `reviewing/agents.md` whatever the author was; it also covers reviewing agent output.
5. If work was split between agents, check it against `reviewing/checks/planning/agents.md`. At High risk, confirm every agent-authored part was checked by someone other than its author.
6. Report findings in the format from `reviewing/feedback.md`.
