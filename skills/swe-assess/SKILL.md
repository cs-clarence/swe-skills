---
name: swe-assess
description: "Assess a change before planning or building: decide its kind (small, medium, large, new project) and risk tier. Use when starting any task beyond a trivial edit, or when work grows beyond what was assessed."
---

# Assess with swe-docs

Guidelines live in `docs/guidelines` of the current repository (installed from <https://github.com/cs-clarence/swe-docs>). If that folder is missing, tell the user and point them to the swe-docs README install section; do not invent rules. Repository overrides take precedence per `docs/guidelines/core/precedence.md`.

1. Read `docs/guidelines/planning/approaches/choose-the-approach.md` and `core/risk-tiers.md`.
2. Answer the four questions: how much changes, how much is unknown, how hard it is to undo, and how many people and how much time it needs.
3. If unknowns dominate, run a short, bounded experiment on the riskiest one, then assess again.
4. Pick the lightest kind that fits. When unsure between two kinds or two tiers, take the larger or higher one.
5. State the assessment with the same points every time: kind, risk tier, answers to the four questions, main unknowns, next step, and what would move the work up a kind.
6. Take the plan's shape from the kind and the rigor from the tier. Next step: read the matching file in `planning/approaches/`. Then plan with the `swe-plan` skill for new projects, medium or large work, and any High-risk work whatever its size. Small work that is neither a new project nor High risk goes to `swe-author`. If the next skill is not installed, follow the same guideline files directly (`planning/plan-a-change.md`, `planning/ready-to-build.md`, `authoring/approach.md`) or tell the user which skill to install.
7. Choose the execution shape from `planning/agents.md#split-work-between-agents-only-when-it-pays`: solo for small work; independent, bounded parts for medium; split along ownership boundaries for large once contracts are agreed. At High risk, no agent is the only checker of its own part. Include the shape in the assessment.
8. Reassess when the work grows. If it outgrows the assessment, follow `core/when-to-ask.md`.
9. Put the assessment where the plan belongs, found as `planning/write-the-plan.md` describes.
