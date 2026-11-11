---
name: swe-execute
description: "Carry out a task or an approved plan end to end, delegating slices to agents when it pays. Use when asked to implement, build or execute a task, plan or plan artifacts."
---

# Execute with swe-docs

Uses `docs/guidelines` from swe-docs (<https://github.com/cs-clarence/swe-docs>). If it is missing, say so and stop; do not invent rules. Repo overrides win (`docs/guidelines/core/precedence.md`). If a skill named below is not installed, follow the guideline files it covers. Scale effort to risk (`core/risk-tiers.md`).

1. Find the input: the task as given, or plan artifacts (the plan, design doc or decision records, where the repo keeps them; see `planning/write-the-plan.md`). If there is neither, ask the user what to execute. Do not invent a task.
2. If the input is only a task, assess it with `swe-assess`. Medium, large, new-project and High-risk work needs a plan first (`swe-plan`). At High risk, wait for approval before building (`planning/agents.md`).
3. If the input is a plan, check it against `planning/ready-to-build.md`. If it is not ready, or work differs from it, stop and follow `core/when-to-ask.md`.
4. Decide solo or split from the assessment and plan (`planning/agents.md#split-work-between-agents-only-when-it-pays`). Small work is solo. If splitting, say so in one line and load `swe-orchestrate` to choose agents and integrate. Otherwise continue solo.
5. Build with `swe-author`, or `swe-debug` for a defect. Follow the plan's steps in order and report revisions instead of absorbing them (`planning/agents.md#stop-and-re-plan-when-work-diverges`).
6. Finish with `swe-self-review` and `core/definition-of-done.md`. For work that ships or is hard to undo, also use `swe-release`.
7. Record progress where the next reader will find it if the work is not finished (`planning/agents.md#leave-a-plan-another-agent-can-resume`).

Hand back with what was done, what was verified and how, what was left to CI, and any open questions.
