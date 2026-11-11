---
name: swe-author
description: "Write or change code following the swe-docs authoring rules. Use for any implementation work: features, bug fixes, refactors, tests, dependencies, interfaces, database, security-sensitive code."
---

# Author with swe-docs

Uses `docs/guidelines` from swe-docs (<https://github.com/cs-clarence/swe-docs>). If it is missing, say so and stop; do not invent rules. Repo overrides win (`docs/guidelines/core/precedence.md`). If a skill named below is not installed, follow the guideline files it covers. Scale effort to risk (`core/risk-tiers.md`).

1. For anything beyond a trivial edit, assess it first with `swe-assess` (or read `planning/approaches/choose-the-approach.md` and `core/risk-tiers.md`).
2. New projects, medium and large work, and any High-risk work need a plan first (short and written for medium) with `swe-plan` (or follow `planning/plan-a-change.md`, `planning/write-the-plan.md` and `planning/ready-to-build.md`). At High risk, wait for approval before building (`planning/agents.md`).
3. Always read `docs/guidelines/core/principles.md`, `authoring/approach.md` and `authoring/agents.md`.
4. Use the "Which files apply" table in `docs/guidelines/README.md` and read only the topic files that match the change.
5. Bug fixes: `authoring/debugging-and-bug-fixing.md`. Refactors: `authoring/structure/refactoring.md`.
6. Finish with `swe-self-review` and check `core/definition-of-done.md`.
