---
name: swe-plan
description: "Plan a change before building: choose an approach, size it, break down work. Use when starting a fix, feature, large change, migration or new project, or when work turns out bigger than expected."
---

# Plan with swe-docs

Guidelines live in `docs/guidelines` of the current repository (installed from <https://github.com/cs-clarence/swe-docs>). If that folder is missing, tell the user and point them to the swe-docs README install section; do not invent rules. Repository overrides take precedence per `docs/guidelines/core/precedence.md`. Scale effort to risk using `docs/guidelines/core/risk-tiers.md`.

1. Use the assessment from the `swe-assess` skill if there is one. Otherwise do it first with that skill if installed, or by reading `planning/approaches/choose-the-approach.md` and `core/risk-tiers.md` yourself. Read the matching approach file in `docs/guidelines/planning/approaches/`.
2. Read `planning/plan-a-change.md`, `planning/break-down-work.md` and `planning/change-size.md`.
3. For migrations or replacements read `planning/large-changes.md`; for design docs read `planning/design-docs.md`.
4. Check the plan against `planning/ready-to-build.md` before starting.
5. If the work is bigger than expected or differs from the design, stop and follow `core/when-to-ask.md`.
6. Agents: also read `planning/agents.md`.
7. If the assessment says to split work between agents, give each part a self-contained brief (goal, scope, inputs, what not to touch, how the result is checked) per `planning/agents.md#give-delegated-work-a-self-contained-brief`. Keep integration and final verification with one agent and verify the combined result yourself. Name in each brief only the checks its change can affect, widening them for contracts, shared state, shared configuration, dependencies or unreliable checks, and for callers at High risk (`planning/agents.md#scope-each-parts-checks-to-its-change`). Plan the broad checks to run once after integration (`planning/agents.md#run-the-broad-checks-once-at-integration`). If that heading is missing, tell the user to update swe-docs and do not split.
