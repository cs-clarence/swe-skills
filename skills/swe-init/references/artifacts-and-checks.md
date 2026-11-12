# Artifacts and checks

Details for `swe-init` steps 4 to 9 and 11.

## Keep the docs current

Docs that drift stop being trusted, so every doc written by `swe-init` (Checks, Tooling, Patterns, Git, and each index) carries a short note, written for humans:

- Place it at the top or bottom, as a one- or two-line "Keeping this up to date" note: these docs describe how the repo works today; change them in the same PR as the change that makes them wrong (a new library, command, generator or convention); fix or delete stale entries rather than leave them.
- For patterns, also say: when a pattern changes, update its example paths and the `README.md` index.
- Do not add dates or version stamps; they rot. Reuse the repo's own wording if it already has such a note, and never add a second one.
- The instruction file gets the agent-only counterpart, one line: update these docs in the same change when you alter the tooling, a pattern or the git workflow they describe.

## Where it is written

- Human docs: Artifacts, Checks, Tooling, Patterns and Git sections below are written for any contributor, in plain prose or short lists, with no agent instructions. Place them in the repo's existing contributor docs; if none, propose `CONTRIBUTING.md` for Checks and Git, a `docs/` page for Tooling, and `docs/patterns/` (with a `README.md` index) for Patterns, and ask. Keep them apart from `docs/guidelines`.
- Instruction file: only a pointer to each doc, the guidelines line, and agent-only rules (for example: commit, push and open PRs only when asked; never edit generated files; run checks with the non-interactive commands). The git default's agent rules (last bullets) go here; the rest of it goes in the human doc.
- Never duplicate a fact in both; link from the instruction file instead. The personal agents file stays separate and git-ignored.

## Default artifact layout

Use when the repo has no convention, and only after the user agrees.

- Put these under the repo's existing docs folder (`docs/` if none; reuse `doc/` or similar if that is what exists): `plans/`, `design/` and `decisions/`. Check the names are free first; if any collide, pick another and say so.
- Create a folder only when its first artifact is written, with no placeholder files.
- Name files `<short-slug>.md`, with no sequence numbers, so parallel branches do not collide.
- Supersede a decision record with a new one that links to the old; do not edit it.
- Delete a plan when the work ends, after moving what lasts to a decision record, code comment or doc (`planning/write-the-plan.md`).
- An assessment is not a separate file. Put it at the top of the plan, or in the change description for small work.
- Keep the default if the user does not choose. Never move or rename existing docs to fit it.

## User docs location

Ask where the repo keeps user docs, and record the path in the Artifacts section so `swe-author` and `swe-docs-write` know where to write. Reuse the existing folder or site. If there is none, propose `docs/` and ask; keep it apart from `docs/guidelines`. Never move existing docs. How to write them is in `authoring/documentation/`.

## Checks section

Record in a Checks section of the contributor docs, with a pointer from the instruction file, so contributors and agents need not guess:

- Each command: test, lint, type-check, build.
- The area it covers.
- Whether it is slow.
- Whether only CI runs it.

`planning/agents.md#scope-each-parts-checks-to-its-change` and `planning/agents.md#run-the-broad-checks-once-at-integration` rely on this. Record what you detected, ask only where detection is unclear, and never invent a command.

## Patterns section

Record in a Patterns section of the contributor docs the approaches this repo already uses, so contributors and agents follow them instead of inventing new ones:

- Where it goes: if the repo already has an architecture, conventions or dev-guide doc, add a Patterns section there; never create a parallel doc. Otherwise propose `docs/patterns/` (kept apart from `docs/guidelines`) and ask. Use one file per pattern or concern (`error-handling.md`, `data-access.md`), named `<short-slug>.md`, and a `docs/patterns/README.md` index that links each file with a one-line description. Create the folder and files only when the first pattern is accepted, and update the index whenever a file is added, renamed or removed. In a monorepo, a package with different approaches may have its own `patterns/` folder, linked from the root index. The instruction file only links to the index.
- Find them by reading the code, dependency manifests and existing docs: which library handles each concern (HTTP, ORM or queries, validation, state, forms, testing, logging, config, dates) and how the repo uses it.
- One line per pattern: the problem, the approach or library, and one or two example file paths. Add "avoid: X" only when the repo clearly rejects an alternative.
- Record only what is consistent across the code. If the repo is mixed, say so and ask which one is preferred; never pick silently.
- Do not restate general guidelines or what the code makes obvious. Keep it short and link to examples rather than copying code.
- Never invent a pattern from a single occurrence or from what the repo might want.

If the repo is new or the patterns are not established (few files, mixed approaches, no clear choice), suggest defaults instead:

- Base them on the language, framework and libraries already in the manifests, and on those tools' own documented, mainstream approach. Prefer what is already installed over adding a dependency.
- Propose one approach per concern, with a one-line reason, only for concerns the project actually has or is about to have. Skip the rest.
- Mark each line "proposed" and write nothing until the user accepts or edits it. Mixed repos: ask which approach wins.
- Replace "proposed" with example paths once real code follows the pattern; on rerun, report patterns that are still only proposed.
- On rerun, check the listed paths still exist and report drift; change nothing unasked.

## Git section

Record in a Git section of the contributor docs how the repo works with git, so everyone follows it (agent-only rules go in the instruction file):

- Detect first: default branch, branch naming (`git branch -a`), commit message style (`git log`), merge method (merge commits, squash, rebase), CI and required checks, hook files (`.husky`, `lefthook`, `.pre-commit-config.yaml`, `.git/hooks`), `.gitignore`, `CODEOWNERS`, PR template.
- Record what you found, one line each. Where the repo is mixed or unclear, ask; never invent.

Safe default, proposed only when the repo is new or has no convention, and written only after the user agrees:

- Never commit to the default branch directly; work on short-lived branches named `<type>/<short-slug>`.
- Small, focused commits in imperative mood with a short subject; follow Conventional Commits only if the repo already does.
- Open a PR for every change; squash-merge to keep history linear; delete the branch after merge.
- Require passing checks (from the Checks section) and one review before merge.
- Never force-push shared branches, rewrite published history, skip hooks (`--no-verify`) or commit secrets; use `--force-with-lease` only on your own branch.
- Agents commit, push or open PRs only when asked, and never change branch protections, remotes or git config.
- Keep `.gitignore` covering build output, dependencies, env files and local agent files.
- Suggest, never apply, repo admin settings (branch protection, required reviews, secret scanning) as a list for the user to set.

Never change existing hooks, protections or history to match the default.

## Tooling section

Record in a Tooling section of the contributor docs what is available here, inferred by detection:

- Where it goes: if the repo has a development or setup guide (`CONTRIBUTING.md`, a README "Development" section, `docs/development.md`), add a Tooling section there. Otherwise propose a single `docs/tooling.md` and ask. If it grows long (many generators or services), propose splitting into `docs/tooling/` with one file per area (`task-runners.md`, `code-generation.md`, `environment.md`) and a `README.md` index linking each with a one-line description, as for patterns. Create it only when the first entry is accepted, and keep the index current. The instruction file only links to it.

- Toolchain: language runtimes and versions (`.tool-versions`, `mise.toml`, `.nvmrc`, `rust-toolchain`, `go.mod`), package manager (from lockfiles), task runners (`Makefile`, `justfile`, `package.json` scripts, omni).
- Quality tools: formatter, linter, type checker, test runner, from config files.
- Environment: containers or dev environments (`Dockerfile`, `compose`, `devcontainer`), required services, env var templates (`.env.example`; never read or record real secrets).
- CLIs on the machine that the repo relies on (`gh`, `docker`, database or cloud CLIs): confirm with `command -v`; list only what you confirmed.
- Agent tooling: MCP servers and skills the harness offers, only if you can list them; they are personal, so put per-user ones in `.agents/agent-choices.local.md`, not the committed file.
- Dev tools worth knowing: task runners and their key tasks (list the tasks, not just the runner), code generators (schema, ORM, API client, GraphQL, protobuf, scaffolding or template tools), migration tools, mock or seed scripts, and similar helpers. Find them in scripts, config files, `codegen` or `generate` targets and generator config. For each, record the command, what it generates or does, where the output goes, and whether generated files are committed or must not be hand-edited.
- One line each: tool, what it is for, how to run it. Mark anything detected in config but not found on the machine as "not installed". Never invent a tool or command; ask only where detection is unclear.
- On rerun, report tools that are missing or newly added.

## Agents file

Optional and personal: each user has different agents and models, so keep it out of version control.

- Write it to `.agents/agent-choices.local.md`; `swe-orchestrate` reads only this path, so do not use another. Add that path to the repo's `.gitignore` (create the file if missing, append, never overwrite), show the change, and confirm the file is ignored with `git check-ignore`. If the path is already tracked, offer to untrack it (`git rm --cached`) with the user's approval; otherwise skip personal choices, since no other path is read.
- Do not add it to the instruction file. `swe-orchestrate` reads this path directly.
- One line per kind of work: explore, research, bounded edit, hard design or debugging, independent review.
- Name the agent or model exactly as the harness does, with an optional override condition, such as High risk.
- Leave a kind out to keep the default.
- To infer it, read what the harness offers and use the table in `swe-orchestrate`. Mark each line as inferred, give a one-line reason, and write nothing until the user accepts or edits it. If the harness lists too little to infer a kind, leave it out.
- Ask which agent the user runs and list only what it offers. Never record an agent you could not confirm exists.
- On rerun, check the file still lists agents that exist; models change.
- A team-wide rule belongs in the committed instruction file, only if the whole team shares those agents.
