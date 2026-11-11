# Artifacts and checks

Details for `swe-init` steps 4, 5 and 6.

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

Record in a Checks section of the instruction file, so agents need not guess:

- Each command: test, lint, type-check, build.
- The area it covers.
- Whether it is slow.
- Whether only CI runs it.

`planning/agents.md#scope-each-parts-checks-to-its-change` and `planning/agents.md#run-the-broad-checks-once-at-integration` rely on this. Record what you detected, ask only where detection is unclear, and never invent a command.

## Agents file

Optional and personal: each user has different agents and models, so keep it out of version control.

- Write it to `.agents/agent-choices.local.md`, or the path the user prefers. Add that exact path to the repo's `.gitignore` (create the file if missing, append, never overwrite), show the change, and confirm the file is ignored with `git check-ignore`. If the path is already tracked, stop and choose another.
- Do not add it to the instruction file. `swe-orchestrate` reads this path directly.
- One line per kind of work: explore, research, bounded edit, hard design or debugging, independent review.
- Name the agent or model exactly as the harness does, with an optional override condition, such as High risk.
- Leave a kind out to keep the default.
- To infer it, read what the harness offers and use the table in `swe-orchestrate`. Mark each line as inferred, give a one-line reason, and write nothing until the user accepts or edits it. If the harness lists too little to infer a kind, leave it out.
- Ask which agent the user runs and list only what it offers. Never record an agent you could not confirm exists.
- On rerun, check the file still lists agents that exist; models change.
- A team-wide rule belongs in the committed instruction file, only if the whole team shares those agents.
