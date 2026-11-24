---
name: swe-change-description
description: "Write or revise a commit body, pull request description or other explanation of a change, using swe-docs. Use when asked to write a PR description or commit message body, or before opening a PR."
---

# Write a change description with swe-docs

Uses `docs/guidelines` from swe-docs (<https://github.com/cs-clarence/swe-docs>). If it is missing, say so and stop; do not invent rules. Repo overrides win (`docs/guidelines/core/precedence.md`). If a skill named below is not installed, follow the guideline files it covers.

1. Read the change itself (diff, plan, linked issue), not only the request. Find its risk tier (`swe-assess`, or `docs/guidelines/core/risk-tiers.md`).
2. Read `docs/guidelines/authoring/change-description.md`. Match detail to the tier: a Low-risk change in one place needs only the summary plus anything not done or uncertain.
3. Open with what changed and why, and link the request, issue or plan. Add verification and what was not verified, the riskiest part, alternatives rejected (Medium and above), how to undo (High), and a design section when the change reaches wide.
4. If you are missing context needed for any of this, ask the requester or author; do not guess.
5. Word it with the `unslop` skill from pstack: concrete, active prose, plain words, and a precise contrast ("before X, now Y, so Z") over a list of edits. If it is not installed, install it (see below) or apply the same principles by hand.
6. Leave out the work log: conversations, agent names, review iterations, routine validation. Keep a detail only if it explains a remaining constraint.
7. Check the result against `docs/guidelines/reviewing/checks/change-description.md`. Reread it against the final diff if the diff changed after review.

## unslop

`unslop` is the pstack skill that removes AI writing patterns. Check whether it is already installed (for example `.agents/skills/unslop` or `~/.agents/skills/unslop`). If not, point the user to it and install only with their approval:

- Source: <https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md>
- Mirror: <https://github.com/backnotprop/pstack>
- Install: `npx skills add https://github.com/cursor/plugins --skill unslop`
