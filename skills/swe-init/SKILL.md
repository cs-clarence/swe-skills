---
name: swe-init
description: "Set up swe-docs and these skills in a new or existing repository, choosing the structure that fits. Use when the user asks to install, adopt or configure swe-docs, or when docs/guidelines is missing."
---

# Set up swe-docs in a repository

Optional. Run this only when asked, or when `docs/guidelines` is missing and the user wants it. Ask before every change and show each file you would create or edit. Never overwrite; append to existing files and stop on collisions. Rules come from swe-docs (<https://github.com/cs-clarence/swe-docs>); read its README install section and `docs/guidelines/core/precedence.md` instead of restating them.

1. Inspect without changing anything: new or existing repo, monorepo or not, instruction files (`AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`), existing docs folders, any existing `docs/guidelines`, an omni workspace (`workspace.omni.yaml`), and where plans, decisions and design docs live today (issues, a decisions folder, a wiki), and the check commands: test, lint, type-check and build, read from build files, scripts and CI config. Note too any existing contributor rules that clash with swe-docs.
2. Recommend an install method and let the user choose. Omni projection if there is or will be a workspace, with `rev` pinned to a tag or commit. Otherwise copy or symlink `docs/guidelines`. Offer a subset by dropping areas from the top down: reviewing, then authoring, then planning; `core` always stays.
3. Install only the skills whose guideline areas are present: `swe-review` needs `reviewing`; `swe-debug`, `swe-release`, `swe-author` and `swe-self-review` need `authoring`; `swe-plan` and `swe-assess` need `planning`. Install them the same way: omni projection from <https://github.com/cs-clarence/swe-skills>, or copy each `skills/<name>` folder.
4. Agree where artifacts live: assessments, plans, design docs, decision records. Use what the repo already does; if nothing, propose the default below and ask. Record the answer in an Artifacts section of the instruction file.
   - Default layout, under the repo's existing docs folder (`docs/` if none; reuse `doc/` or similar if that is what exists): `plans/` for plans, `design/` for design docs, `decisions/` for decision records. Check the names are free first; if any collide, pick another and say so.
   - Create a folder only when its first artifact is written, with no placeholder files.
   - Name files `<short-slug>.md`, with no sequence numbers, so parallel branches do not collide. Supersede a decision record with a new one that links to the old; do not edit it.
   - Plans are temporary. Delete a plan when the work ends, after moving what lasts to a decision record, code comment or doc, as `planning/write-the-plan.md` describes.
   - An assessment is not a separate file. Put it at the top of the plan, or in the change description for small work.
   - Keep the default if the user does not choose; never move or rename existing docs to fit it.
5. Record the repo's checks in a Checks section of the instruction file, so agents need not guess them: each command, which area it covers, whether it is slow, and whether only CI runs it. This is what `planning/agents.md#scope-each-parts-checks-to-its-change` and `planning/agents.md#run-the-broad-checks-once-at-integration` rely on. Record what you detected, ask only where detection is unclear, and never invent a command.
6. Ask whether any area is always High risk, such as payments, authentication or migrations. Write each as an override per `docs/guidelines/core/precedence.md`, in the repo's own files, naming the rule, action, reason and effective rule. Do the same for any clash found in step 1, proposing the override and letting the user decide.
7. Add one line to the instruction file: follow the guidelines in `docs/guidelines`. Create `AGENTS.md` only if no instruction file exists.
8. Overrides are optional beyond those in step 6. Any other rule change goes in the repo's own files, never in the installed folder.
9. Report what was done and what remains. Suggest the `swe-assess` skill for the next task.
10. When rerun, change nothing unless asked; report the current state and any drift.
