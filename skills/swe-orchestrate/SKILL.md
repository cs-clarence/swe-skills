---
name: swe-orchestrate
description: "Pick which agent handles each slice of a split task, brief it, and integrate the results. Use when swe-execute or swe-plan has decided to split work between agents."
user-invocable: false
---

# Orchestrate agents with swe-docs

Uses `docs/guidelines` from swe-docs (<https://github.com/cs-clarence/swe-docs>). If it is missing, say so and stop; do not invent rules. Repo overrides win (`docs/guidelines/core/precedence.md`). If a skill named below is not installed, follow the guideline files it covers.

Not user-invoked; `swe-execute` loads it. swe-docs owns whether to split, the brief, per-part checks and integration (`planning/agents.md`). This skill only adds how to choose the agent for each slice. If `planning/agents.md` or its headings are missing, tell the user to update swe-docs and work solo.

1. Confirm the split is worth it (`planning/agents.md#split-work-between-agents-only-when-it-pays`). Slices must be independent, bounded and checkable on their own, with contracts agreed first for large work (`planning/approaches/large-work.md#agree-ownership-and-interfaces-up-front`).
2. List the agents the harness offers, with their model, tools and permissions. Use only what exists; never assume a name. If only one kind exists, the choice below reduces to read-only versus write.
3. Read `.agents/agent-choices.local.md` if it exists (a personal, git-ignored file from `swe-init`). A choice recorded there for a kind of work wins over the table, unless that agent is no longer offered; then say so and fall back. For the rest, pick the agent with the table. Take the cheapest agent that can do the slice reliably.
4. Brief each one (`planning/agents.md#give-delegated-work-a-self-contained-brief`) with the checks its change can affect (`planning/agents.md#scope-each-parts-checks-to-its-change`). Ask for a report (see Agent reports).
5. Integrate and run the broad checks once, yourself (`planning/agents.md#run-the-broad-checks-once-at-integration`).

## Choosing the agent for a slice

| Slice | Agent | Why |
| --- | --- | --- |
| Find files, trace usage, answer "where/how does X work" | Read-only explorer, fast and cheap model | No writes needed; breadth over depth |
| Research outside the repo (docs, APIs, versions) | Agent with web access, read-only | Keeps untrusted content away from write access |
| Bounded edit with a settled interface and clear tests | General-purpose writer, mid-tier model | Well specified, so cost matters more than depth |
| Ambiguous design, cross-cutting change, hard debugging | Strongest available model, or do it yourself | Briefing costs more than doing; errors compound |
| Independent review or verification of a part | A different agent from the author, fresh context, read-only | Required at High risk (`planning/agents.md#split-work-between-agents-only-when-it-pays`); shared context shares blind spots |
| Integration and final checks | The orchestrator | One agent owns the combined result |

Adjust by these traits, in order:

1. **Writes or not.** If the slice needs no edits, use a read-only agent. Grant the least permission that works.
2. **Risk tier.** At High risk use a stronger model and a separate reviewer. At Low, prefer cheap.
3. **Ambiguity.** If the slice needs judgement the brief cannot settle, do not delegate it. Settle the decision, then delegate the rest.
4. **Context needed.** If the slice depends on most of what you know, do it yourself. Delegate when a short brief is enough.
5. **Parallel or serial.** Run slices in parallel only when they touch different files or modules and need no output from each other. Otherwise run them in order.
6. **Isolation.** Slices that write to overlapping files need separate checkouts or must be serialized. Never let two writers share files.

## Agent reports

Ask each agent to end with a short report: what it changed or found, which checks it ran and which it did not, open questions, and anything the brief did not anticipate. The report is a claim; the diff and your own check runs are the evidence.

Use a file instead only when the result is too big for a message, several later slices need the same output, or you need to keep bulk out of your context. Have the agent write it to the temp directory or a git-ignored path, and return a short summary plus the path. Delete it after integration. Progress that must outlive the session goes in the plan (`planning/agents.md#leave-a-plan-another-agent-can-resume`), not in a handoff file.

## While agents run

- Do not duplicate a delegated slice yourself. Work on integration prep or an unrelated slice.
- Treat reports as claims. Read the diff and re-run the checks (`planning/agents.md#give-delegated-work-a-self-contained-brief`).
- If an agent fails or returns something off-brief, fix the brief once and retry. If it fails again, take the slice over or stop and ask (`core/when-to-ask.md`). Do not escalate to a bigger model without a reason you can state.
- If a slice grows or the plan changes, stop and re-plan (`planning/agents.md#stop-and-re-plan-when-work-diverges`).

## Report

State, per slice: the agent chosen, why, what it returned, and what you verified. Name checks left to CI.
