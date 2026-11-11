---
name: swe-init
description: "Set up swe-docs and these skills in a new or existing repository, choosing the structure that fits. Use when the user asks to install, adopt or configure swe-docs, or when docs/guidelines is missing."
---

# Set up swe-docs in a repository

Optional: run only when asked, or when `docs/guidelines` is missing and the user wants it. Ask before every change and show each file you would create or edit. Never overwrite; append to existing files and stop on collisions. Rules come from swe-docs (<https://github.com/cs-clarence/swe-docs>); read its README install section and `docs/guidelines/core/precedence.md` instead of restating them.

1. Inspect without changing anything:
   - new or existing repo, monorepo or not;
   - instruction files (`AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`), docs folders, any existing `docs/guidelines`, an omni workspace (`workspace.omni.yaml`);
   - where plans, decisions and design docs live today (issues, a decisions folder, a wiki);
   - check commands (test, lint, type-check, build), read from build files, scripts and CI config;
   - existing contributor rules that clash with swe-docs.
2. Recommend an install method and let the user choose: omni projection if there is or will be a workspace, with `rev` pinned to a tag or commit; otherwise copy or symlink `docs/guidelines`. Offer a subset by dropping areas from the top down: reviewing, then authoring, then planning; `core` always stays.
3. Install only skills whose guideline areas are present: `swe-review` needs `reviewing`; `swe-debug`, `swe-release` and `swe-author` need `authoring`; `swe-docs-write` and `swe-self-review` need `authoring` and `reviewing`, because they read `reviewing/checks/`; `swe-plan` and `swe-assess` need `planning`; `swe-execute` needs all three and `swe-orchestrate` (hidden, loaded by `swe-execute`) needs `planning`. Install them the same way (copy whole skill folders), from <https://github.com/cs-clarence/swe-skills>.
4. Agree where artifacts live (assessments, plans, design docs, decision records) and where user docs live (tutorials, guides, reference, release notes). Use what the repo already does; if nothing, propose the default in `references/artifacts-and-checks.md` and ask. Record the answer in an Artifacts section of the instruction file.
5. Record the repo's checks in a Checks section of the instruction file (see `references/artifacts-and-checks.md`).
6. Ask whether the user wants to pick agents or models for kinds of work, such as exploring, bounded edits, hard design, review. Available agents differ per user, so this is personal: write it to a git-ignored local file, never to a committed one (see `references/artifacts-and-checks.md`). Offer to infer it: list what the harness offers, map each kind of work to an agent by its model, tools and permissions as `swe-orchestrate` would, and show the result for the user to accept or edit before writing. Otherwise let them choose, or skip, and `swe-orchestrate` then chooses from what the harness offers. Offer only agents and models the harness lists; never invent a name.
7. Ask whether any area is always High risk, such as payments, authentication or migrations. Write each as an override per `docs/guidelines/core/precedence.md`, in the repo's own files, naming the rule, action, reason and effective rule. Do the same for any clash found in step 1, letting the user decide.
8. Add one line to the instruction file: follow the guidelines in `docs/guidelines`. `CONTRIBUTING.md` alone is not an instruction file, since many agents do not load it. Ask which agent the user runs, then update the file that agent loads, creating `AGENTS.md` or the agent's own file (such as `CLAUDE.md`) if none exists, with approval. Any other rule change goes in the repo's own files, never in the installed folder.
9. Report what was done and what remains. Suggest `swe-assess` for the next task.
10. When rerun, change nothing unless asked; report the current state and any drift.
