---
name: swe-init
description: "Set up swe-docs and these skills in a new or existing repository, choosing the structure that fits. Use when the user asks to install, adopt or configure swe-docs, or when docs/guidelines is missing."
---

# Set up swe-docs in a repository

Optional. Run this only when asked, or when `docs/guidelines` is missing and the user wants it. Ask before every change and show each file you would create or edit. Never overwrite; append to existing files and stop on collisions. Rules come from swe-docs (<https://github.com/cs-clarence/swe-docs>); read its README install section and `docs/guidelines/core/precedence.md` instead of restating them.

1. Inspect without changing anything: new or existing repo, monorepo or not, instruction files (`AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`), existing docs folders, any existing `docs/guidelines`, an omni workspace (`workspace.omni.yaml`), and where plans, decisions and design docs live today (issues, a decisions folder, a wiki).
2. Recommend an install method and let the user choose. Omni projection if there is or will be a workspace, with `rev` pinned to a tag or commit. Otherwise copy or symlink `docs/guidelines`. Offer a subset by dropping areas from the top down: reviewing, then authoring, then planning; `core` always stays.
3. Install these skills the same way: omni projection from <https://github.com/cs-clarence/swe-skills>, or copy each `skills/<name>` folder.
4. Agree where artifacts live: assessments, plans, design docs, decision records. Use what the repo already does; if nothing, propose a location and ask. Record the answer in an Artifacts section of the instruction file.
5. Add one line to the instruction file: follow the guidelines in `docs/guidelines`. Create `AGENTS.md` only if no instruction file exists.
6. Overrides are optional. If the user wants to change a rule, write it as an override per `docs/guidelines/core/precedence.md` in the repo's own files, never in the installed folder.
7. Report what was done and what remains. Suggest the `swe-assess` skill for the next task.
8. When rerun, change nothing unless asked; report the current state and any drift.
