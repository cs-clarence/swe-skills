---
name: swe-assess
description: "Assess a change before planning or building: decide its kind (small, medium, large, new project) and risk tier. Use when starting any task beyond a trivial edit, or when work grows beyond what was assessed."
---

# Assess with swe-docs

Uses `docs/guidelines` from swe-docs (<https://github.com/cs-clarence/swe-docs>). If it is missing, say so and stop; do not invent rules. Repo overrides win (`docs/guidelines/core/precedence.md`). If a skill named below is not installed, follow the guideline files it covers.

1. Read `docs/guidelines/planning/approaches/choose-the-approach.md` and `core/risk-tiers.md`.
2. Answer the four questions: how much changes, how much is unknown, how hard it is to undo, how many people and how much time. If unknowns dominate, run a short, bounded experiment on the riskiest one, then assess again.
3. Pick the lightest kind that fits. When unsure between two kinds or tiers, take the larger or higher.
4. State the assessment with the same points every time: kind, risk tier, answers to the four questions, main unknowns, execution shape, checks, next step, and what would move the work up a kind.
5. Take the shape, checks and next step from the table. The kind sets the shape and the tier sets the rigor.

| Kind | Execution shape | Checks | Next |
| --- | --- | --- | --- |
| Small | Solo | Relevant checks locally; CI as backstop | `swe-author` |
| Medium | Independent bounded parts, if worth it | Relevant checks per part and for the combined change | `swe-plan` |
| Large | Split along ownership boundaries once contracts are agreed | Full set locally, once, at integration | `swe-plan` |
| New project | As its approach file says | Automated from the start | `swe-plan` |

- Split only when it saves more than it costs in briefing, coordination and checking; otherwise work solo (`planning/agents.md#split-work-between-agents-only-when-it-pays`). If that heading is missing, the installed swe-docs is older than these skills expect: tell the user to update it and work solo meanwhile.
- High risk goes to `swe-plan` whatever the size. No agent is the only checker of its own part.
- At Low risk, CI on the integrated change may stand in for a local run of small or medium work (`planning/agents.md#run-the-broad-checks-once-at-integration`).
- Read the matching file in `planning/approaches/` before handing off.

Reassess when the work grows; if it outgrows the assessment, follow `core/when-to-ask.md`. Put the assessment where the plan belongs (`planning/write-the-plan.md`).
