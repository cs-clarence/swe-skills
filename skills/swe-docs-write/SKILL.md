---
name: swe-docs-write
description: "Write or update user and developer documents: tutorials, how-to guides, reference, explanation, README, release notes. Use when asked to write docs, or invoke it manually for documentation-only work."
---

# Write docs with swe-docs

Uses `docs/guidelines` from swe-docs (<https://github.com/cs-clarence/swe-docs>). If it is missing, say so and stop; do not invent rules. Repo overrides win (`docs/guidelines/core/precedence.md`).

`swe-author` already covers documents (its step 5). This skill is a shortcut for invoking that by hand on documentation-only work, without the code workflow.

1. Find where the repo keeps its user docs (the Artifacts section of the instruction file, see `swe-init`); if unrecorded, look for the existing docs folder and ask.
2. Read `docs/guidelines/authoring/documentation/documentation.md` and `authoring/documentation/choosing-a-type.md`.
3. Read the file for the chosen type in `authoring/documentation/`: `tutorials`, `how-to-guides`, `reference`, `explanation`, `project-readme` or `release-notes`. For documents for people changing the code, read `authoring/documentation/developer-docs.md`.
4. Check the result against the matching file in `reviewing/checks/documentation/`.
