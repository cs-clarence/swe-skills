---
name: swe-plan
description: "Plan a change before building: choose an approach, size it, break down work. Use when starting a fix, feature, large change, migration or new project, or when work turns out bigger than expected."
---

# Plan with swe-docs

Uses `docs/guidelines` from swe-docs (<https://github.com/cs-clarence/swe-docs>). If it is missing, say so and stop; do not invent rules. Repo overrides win (`docs/guidelines/core/precedence.md`). If a skill named below is not installed, follow the guideline files it covers. Scale effort to risk (`core/risk-tiers.md`).

1. Use the `swe-assess` assessment if there is one; otherwise assess first (`planning/approaches/choose-the-approach.md` and `core/risk-tiers.md`; state the same points every time, as that file lists). Read the matching file in `docs/guidelines/planning/approaches/`.
2. Read `planning/plan-a-change.md`, `planning/break-down-work.md` and `planning/change-size.md`. For migrations or replacements add `planning/large-changes.md`; for design docs, `planning/design-docs.md`.
3. Check the plan against `planning/ready-to-build.md` before starting.
4. If the work is bigger than expected or differs from the design, stop and follow `core/when-to-ask.md`.
5. Agents: also read `planning/agents.md`.
6. If the assessment says to split work between agents:
   - Give each part a self-contained brief: goal, scope, inputs, what not to touch, how the result is checked (`planning/agents.md#give-delegated-work-a-self-contained-brief`).
   - Name in each brief only the checks its change can affect. Widen them for contracts, shared state, shared configuration, dependencies or unreliable checks, and for callers at High risk (`planning/agents.md#scope-each-parts-checks-to-its-change`).
   - Keep integration and final verification with one agent, and plan the broad checks to run once after integration (`planning/agents.md#run-the-broad-checks-once-at-integration`). Verify the combined result yourself.
   - If those headings are missing, tell the user to update swe-docs and do not split.
