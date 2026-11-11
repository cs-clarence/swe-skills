---
name: swe-author
description: "Write or change code following the swe-docs authoring rules. Use for any implementation work: features, bug fixes, refactors, tests, dependencies, interfaces, database, security-sensitive code."
---

# Author with swe-docs

Guidelines live in `docs/guidelines` of the current repository (installed from <https://github.com/cs-clarence/swe-docs>). If that folder is missing, tell the user and point them to the swe-docs README install section; do not invent rules. Repository overrides take precedence per `docs/guidelines/core/precedence.md`. Scale effort to risk using `docs/guidelines/core/risk-tiers.md`.

1. For anything beyond a trivial edit, assess it first with the `swe-assess` skill if installed, otherwise with `planning/approaches/choose-the-approach.md` and `core/risk-tiers.md`. New projects, medium and large work, and any High-risk work need a plan first (a short written plan for medium): use the `swe-plan` skill if installed, otherwise follow `planning/plan-a-change.md` and `planning/write-the-plan.md`, and for High risk wait for approval before building (`planning/agents.md`).
2. Always read `docs/guidelines/core/principles.md`, `authoring/approach.md` and `authoring/agents.md`.
3. Open `docs/guidelines/README.md` and use the "Which files apply" table to read only the topic files that match the change (testing, error handling, security, database, structure, style, and so on).
4. Bug fixes: `authoring/debugging-and-bug-fixing.md`. Refactors: `authoring/structure/refactoring.md`.
5. Finish with the `swe-self-review` skill if installed, otherwise follow `authoring/self-review.md`, and check `core/definition-of-done.md`.
