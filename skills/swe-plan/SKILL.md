---
name: swe-plan
description: "Plan a change before building: choose an approach, size it, break down work. Use when starting a fix, feature, large change, migration or new project, or when work turns out bigger than expected."
---

# Plan with swe-docs

Guidelines live in `docs/guidelines` of the current repository (installed from <https://github.com/cs-clarence/swe-docs>). If that folder is missing, tell the user and point them to the swe-docs README install section; do not invent rules. Repository overrides take precedence per `docs/guidelines/core/precedence.md`. Scale effort to risk using `docs/guidelines/core/risk-tiers.md`.

1. Read `docs/guidelines/planning/approaches/choose-the-approach.md` and the matching approach file.
2. Read `planning/plan-a-change.md`, `planning/break-down-work.md` and `planning/change-size.md`.
3. For migrations or replacements read `planning/large-changes.md`; for design docs read `planning/design-docs.md`.
4. Check the plan against `planning/ready-to-build.md` before starting.
5. If the work is bigger than expected or differs from the design, stop and follow `core/when-to-ask.md`.
6. Agents: also read `planning/agents.md`.
