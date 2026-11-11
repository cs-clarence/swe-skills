---
name: swe-release
description: "Prepare to ship a change and be able to undo it, following the swe-docs release rules. Use before releasing, deploying, migrating data or changing a published interface."
---

# Release with swe-docs

Uses `docs/guidelines` from swe-docs (<https://github.com/cs-clarence/swe-docs>). If it is missing, say so and stop; do not invent rules. Repo overrides win (`docs/guidelines/core/precedence.md`). If a skill named below is not installed, follow the guideline files it covers.

1. Read `docs/guidelines/authoring/releases-and-rollback.md`. State the rollback path, or why the change cannot be undone and what applies instead.
2. Changing an API, format or other published interface: `authoring/interfaces-and-compatibility.md`.
3. Changing schemas, migrations or persistent data: `authoring/database/data-and-state.md`, which sets the order of compatible rollout steps.
4. Large migrations or replacements: `planning/large-changes.md`. New settings or flags: `authoring/configuration.md`.
5. Report the rollout order, the rollback path and any risk left over.
