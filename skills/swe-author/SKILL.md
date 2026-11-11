---
name: swe-author
description: "Write or change code following the swe-docs authoring rules. Use for any implementation work: features, bug fixes, refactors, tests, dependencies, interfaces, database, security-sensitive code."
---

# Author with swe-docs

Uses `docs/guidelines` from swe-docs (<https://github.com/cs-clarence/swe-docs>). If it is missing, say so and stop; do not invent rules. Repo overrides win (`docs/guidelines/core/precedence.md`). If a skill named below is not installed, follow the guideline files it covers. Scale effort to risk (`core/risk-tiers.md`).

1. For anything beyond a trivial edit, assess it first with `swe-assess` (or read `planning/approaches/choose-the-approach.md` and `core/risk-tiers.md`). If `swe-execute` or the user already supplied an assessment or plan, use it; do not redo an existing assessment. If a plan is supplied without an assessment and does not establish the work kind and risk tier, assess the work first.
2. New projects, medium and large work, and any High-risk work need a plan first (short and written for medium) with `swe-plan` (or follow `planning/plan-a-change.md`, `planning/write-the-plan.md` and `planning/ready-to-build.md`). At High risk, wait for approval before building (`planning/agents.md`).
3. Always read `docs/guidelines/core/principles.md`, `authoring/approach.md` and `authoring/agents.md`.
4. Use the "Which files apply" table in `docs/guidelines/README.md` and read only the topic files that match the change.
5. Documents (tutorials, how-to guides, reference, explanation, README, release notes, developer docs): read `authoring/documentation/documentation.md` and `authoring/documentation/choosing-a-type.md`, then the file for the chosen type. Update affected docs in the same change as the behavior.
6. Bug fixes: `authoring/debugging-and-bug-fixing.md`. Refactors: `authoring/structure/refactoring.md`.
7. Finish with `swe-self-review` and check `core/definition-of-done.md`.
