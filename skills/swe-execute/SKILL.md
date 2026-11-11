---
name: swe-execute
description: "Decide how to carry out a task or an approved plan and route it to the right skill, delegating slices to agents when it pays. Use when asked to implement, build, fix or execute a task, plan or plan artifacts and the path is not already clear."
---

# Execute with swe-docs

Uses `docs/guidelines` from swe-docs (<https://github.com/cs-clarence/swe-docs>). If it is missing, say so and stop; do not invent rules. Repo overrides win (`docs/guidelines/core/precedence.md`). If a skill named below is not installed, follow the guideline files it covers. Scale effort to risk (`core/risk-tiers.md`).

This skill decides what to do and in what order. It does not write code itself; the skills below do the work.

1. Find the input: the task as given, or plan artifacts (plan, design doc, decision records, where the repo keeps them; see `planning/write-the-plan.md`). If there is neither, ask the user what to execute. Do not invent a task.
2. Gate. Skip what is already done and pass it on, so no skill repeats it:
   - Task only: assess with `swe-assess`. Medium, large, new-project and High-risk work needs `swe-plan` first, and High risk waits for approval (`planning/agents.md`).
   - Plan given: find its risk tier and check it against `planning/ready-to-build.md`. If it is not ready or work differs from it, stop and follow `core/when-to-ask.md`. At High risk, confirm explicit approval before delegating or building; if it is missing, stop and ask, unless the user explicitly told you to proceed (`planning/agents.md`).
3. Route by kind of work:

   | The work is | Use |
   | --- | --- |
   | Writing or changing code, tests, interfaces, dependencies | `swe-author` |
   | A defect, failing test or regression | `swe-debug` |
   | Documents only | `swe-docs-write` |
   | Shipping, deploying, data migration, published interface | `swe-release`, after the change is built |
   | Reviewing a change, plan or agent output | `swe-review` |
   | Mixed | Order the parts above in the plan, one skill per part |

4. Decide solo or split (`planning/agents.md#split-work-between-agents-only-when-it-pays`). Small work is solo. To split, say so in one line and load `swe-orchestrate` to choose an agent per slice; each agent runs the routed skill for its slice. Integration and final checks stay with you.
5. Run the routed skills in plan order. Report revisions instead of absorbing them (`planning/agents.md#stop-and-re-plan-when-work-diverges`). `swe-author` and `swe-debug` end with `swe-self-review`; for other solo work that produced a change, such as documents only, run it yourself before handing back. Review-only work (`swe-review`) produces no change, so skip it and do not edit what you reviewed unless asked. For split work, review the combined result yourself.
6. If unfinished, record progress where the next reader will find it (`planning/agents.md#leave-a-plan-another-agent-can-resume`). Check `core/definition-of-done.md` before handing back.

Hand back with what was done, what was verified and how, what was left to CI, and open questions.
