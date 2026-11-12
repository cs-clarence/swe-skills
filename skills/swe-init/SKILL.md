---
name: swe-init
description: "Set up swe-docs and these skills in a new or existing repository, and write the repo's contributor docs and agent context: checks, tooling, patterns, git workflow and artifact locations, inferred from the code or proposed as safe defaults when the repo is new. Use when the user asks to install, adopt or configure swe-docs, onboard a repo for agents, document its conventions, or when docs/guidelines is missing."
---

# Set up swe-docs and repo context

Optional: run only when asked, or when `docs/guidelines` is missing and the user wants it. Rules come from swe-docs (<https://github.com/cs-clarence/swe-docs>); read its README install section and `docs/guidelines/core/precedence.md` instead of restating them. Details for the steps are in `references/artifacts-and-checks.md`.

## Ground rules

- Ask before every change and show each file you would create or edit. Never overwrite; append to existing files and stop on collisions.
- Infer from the repo by detection, never invent. Where the repo is mixed or unclear, ask. Where it is new or has no convention, propose a safe default marked as proposed, and write it only after the user agrees.
- Write repo knowledge (checks, tooling, patterns, git workflow) as human-facing docs any contributor can read, in the repo's existing contributor docs or the places the reference proposes. Keep agent-specific content in the instruction file (`AGENTS.md` or the agent's own file): the guidelines line, pointers to those docs, the Artifacts section, and rules that only matter to agents. Never duplicate a fact between them; the instruction file links.
- Each doc you write carries a short "keep this up to date" note, and the instruction file gets a matching agent rule (see "Keep the docs current" in the reference).
- Personal choices (agents, models, per-user tools) go in a git-ignored local file, never a committed one.
- Never install tools or change existing hooks, protections, docs or history to fit a default.

## Steps

1. Inspect without changing anything:
   - new or existing repo, monorepo or not;
   - instruction files (`AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`), docs folders, any existing `docs/guidelines`, an omni workspace (`workspace.omni.yaml`);
   - where plans, decisions and design docs live today (issues, a decisions folder, a wiki);
   - check commands (test, lint, type-check, build), read from build files, scripts and CI config;
   - tooling: runtimes, package manager, task runners, code generators, migration and dev tools, containers, CLIs on the machine;
   - patterns: the libraries and approaches the code uses for recurring problems;
   - git workflow: default branch, branch and commit style, merge method, CI, hooks, PR template;
   - existing contributor rules that clash with swe-docs.
2. Recommend an install method and let the user choose: omni projection if there is or will be a workspace, with `rev` pinned to a tag or commit; otherwise copy or symlink `docs/guidelines`. Offer a subset by dropping areas from the top down: reviewing, then authoring, then planning; `core` always stays.
3. Install only skills whose guideline areas are present: `swe-review` needs `reviewing`; `swe-debug`, `swe-release` and `swe-author` need `authoring`; `swe-docs-write` and `swe-self-review` need `authoring` and `reviewing`, because they read `reviewing/checks/`; `swe-plan` and `swe-assess` need `planning`; `swe-execute` needs all three and `swe-orchestrate` (hidden, loaded by `swe-execute`) needs `planning`. Install them the same way (copy whole skill folders), from <https://github.com/cs-clarence/swe-skills>.
4. Agree where artifacts live (assessments, plans, design docs, decision records) and where user docs live (tutorials, guides, reference, release notes). Use what the repo already does; if nothing, propose the default in the reference and ask. Record the answer in an Artifacts section of the instruction file, which stays there because other skills look it up.
5. Record the repo's checks in a Checks section of the contributor docs: each command, its area, whether it is slow, whether only CI runs it.
6. Record the tooling in a Tooling section: toolchain, quality tools, environment, CLIs confirmed on the machine, and dev tools worth knowing such as task runners and code generators, each with how to run it.
7. Record the patterns in `docs/patterns/` with a `README.md` index (or a Patterns section of an existing conventions doc): the approach this repo uses for recurring problems and libraries, with example paths. Show the findings and let the user accept, edit or drop each before writing. If the repo is new or the patterns are not established, propose defaults for its stack, marked as proposed.
8. Record the git workflow in a Git section: branching, commit messages, PR and merge rules, protections, hooks. If the repo is new or has no clear convention, propose the safe default, and list admin settings (branch protection, required reviews) as suggestions for the user to set, never applied.
9. Ask whether the user wants to pick agents or models for kinds of work, such as exploring, bounded edits, hard design, review. Offer to infer it from what the harness lists, as `swe-orchestrate` would, and show the result for the user to accept or edit before writing it to the git-ignored local file. Otherwise let them choose, or skip, and `swe-orchestrate` chooses from what the harness offers. Offer only agents and models the harness lists; never invent a name.
10. Ask whether any area is always High risk, such as payments, authentication or migrations. Write each as an override per `docs/guidelines/core/precedence.md`, in the repo's own files, naming the rule, action, reason and effective rule. Do the same for any clash found in step 1, letting the user decide.
11. Update the instruction file with approval: one line to follow the guidelines in `docs/guidelines`, pointers to the docs written above, the Artifacts section, and the agent-only rules (for example, git actions only when asked; update the docs in the same change). `CONTRIBUTING.md` alone is not an instruction file, since many agents do not load it. Ask which agent the user runs, then update the file that agent loads, creating `AGENTS.md` or the agent's own file (such as `CLAUDE.md`) if none exists. Any other rule change goes in the repo's own files, never in the installed folder.
12. Report what was done, what is only proposed, and what remains. Suggest `swe-assess` for the next task.
13. When rerun, change nothing unless asked; report the current state and any drift: missing paths, tools or agents, stale docs, patterns still only proposed.
