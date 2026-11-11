---
name: swe-review
description: Review a change, diff or pull request using the swe-docs reviewing checks. Use when asked to review code, a plan, or agent output.
---

# Review with swe-docs

Guidelines live in `docs/guidelines` of the current repository (installed from https://github.com/cs-clarence/swe-docs). If that folder is missing, tell the user and point them to the swe-docs README install section; do not invent rules. Repository overrides take precedence per `docs/guidelines/core/precedence.md`. Scale effort to risk using `docs/guidelines/core/risk-tiers.md`.

1. Read `docs/guidelines/reviewing/process.md` and `reviewing/feedback.md`.
2. Use `reviewing/by-tier.md` to pick checks for the change's risk tier, then read the matching files in `reviewing/checks/`.
3. High-risk security changes: `reviewing/checks/threat-review.md`. Plans: `reviewing/checks/planning/`.
4. Reviewing agent output: `reviewing/agents.md`.
5. Report findings in the format from `reviewing/feedback.md`.
