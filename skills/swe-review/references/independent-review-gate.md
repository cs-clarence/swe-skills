# Independent review gate

Required for changes at Medium risk and above, including solo work. Self-review and passing automated checks do not replace independent review.

Adapted in part from Bun's Zig-to-Rust rewrite (<https://bun.com/blog/bun-in-rust>): separate roles, adversarial reviewers, and fixing the process that produces bad code.

## Roles

- **Implementer** writes the change and wants it accepted, which biases it toward shipping early. It never reviews its own work for the gate.
- **Reviewer** has one job: find bugs and reasons the change does not work. It does not implement or edit the change.
- **Fixer** applies accepted findings. It may be the implementer, but never a reviewer. A fixer's change is a new revision that goes back through the gate.
- Each role runs in its own context window. Reviewers do not see each other's findings until all have reported, so their conclusions stay independent.

## Reviewers by tier

- **Medium:** one independent reviewer.
- **High:** two or more independent reviewers, each with a different angle (for example correctness against the spec, and failure, rollback and security paths). Use a different model for at least one when available. Every reviewer must PASS.
- Raise the count for large or cross-cutting changes. Never lower it to save time.

### Reviewer strength

Rank the models the harness offers as fast, mid or strong, using only what it lists; if you cannot tell, ask or use `.agents/agent-choices.local.md`. Compare the reviewer to the author, not to a model name.

- **Medium:** at least mid-tier, and at least as strong as the author for non-trivial changes. Prefer a different model from the author.
- **High:** every reviewer at least as strong as the author, and at least one from a different model, ideally a different family.
- **Author is the strongest available:** use a different model of the same tier, or two reviewers from the strongest.
- **Hard design, cross-cutting or debugging work:** review it with a strong model; cheap review here gives false confidence.
- **Shortfall:** if no available model meets the rule, the gate is BLOCKED. Report it and ask; do not silently downgrade.
- A weaker reviewer counts only if it states what it tried to break. Every report names the model it ran on.

## Prepare

1. Finish the intended change, self-review it, and run the relevant checks before requesting review.
2. Identify the exact revision under review: a commit SHA, or a captured diff including relevant untracked files if the work is uncommitted. Record the scope and risk tier.
3. Choose reviewers other than the author, with fresh context and read-only access. Give them the task or approved plan, acceptance criteria, the revision and scope, relevant guidelines, and check results and omissions. Do not give them only the author's summary; they must inspect the actual change.
4. Brief them adversarially: assume the change is wrong and try to prove it. Ask them to check the change against a reference where one exists (the spec, the old behavior, the approved plan, or the guidelines) and to name each file and line they relied on.
5. Give reviewers the rejection rules that apply, plus these defaults:
   - Reject stubs, placeholders, `TODO`s, and code that was made to compile or pass by removing or bypassing the behavior.
   - Reject skipped, deleted, weakened, or conditionally disabled tests, and assertions that cannot fail.
   - Reject a paragraph-long comment used to justify a workaround; the code is wrong, so fix the code.
   - Reject behavior that differs between build modes or environments, such as side effects inside assertions or debug-only code.
   - Reject changes that go beyond the stated scope.
6. For split work, require independent review of every agent-authored part and of the integrated result. The orchestrator's own review counts as independent only for parts it did not author; an orchestrator who authored integration changes cannot independently approve those changes.

## Decide

The reviewer runs `swe-review` and returns:

- The revision and scope inspected.
- Findings, separated into blocking issues and non-blocking suggestions, with reasons and file references.
- Checks run, checks not run, and any resulting verification gaps.
- An explicit verdict: **PASS** or **BLOCKED**.

**PASS** means the reviewer found no unresolved blocking issues and has enough evidence to judge the scope. A reviewer who finds nothing must say what they tried to break; a bare "looks good" is not a pass. **BLOCKED** means there is a blocking finding, insufficient evidence, incomplete coverage, or no available independent reviewer. Silence, a missing report, and an author's assertion are not a pass. Suggestions alone do not block.

## Verify the evidence

- Confirm that the checks the gate relies on actually ran: tests executed rather than skipped, counts did not drop, and nothing was deleted or disabled to get green. A green result with fewer tests than before is BLOCKED until explained.
- Treat review reports as claims. The orchestrator spot-checks a sample of findings and passes against the diff, so a reviewer that approves without catching known problems is noticed.
- When a reviewer misses something, or an implementer repeats a mistake, fix the process: tighten the brief, add a rejection rule, or add a check. Do not only patch the change.

## Resolve and re-review

- The implementer or fixer addresses blocking findings and reruns affected checks. Reviewers do not edit the change being reviewed.
- Request independent re-review of the new revision, supplying the previous findings and their disposition. Re-review may focus on the fixes and their affected areas, but must confirm all previous blockers are resolved and no new blockers were introduced.
- Any change after a pass invalidates that pass for the affected scope. Review the new revision and its effects before restoring the pass; do not reuse an approval for a stale diff.
- If a finding is disputed, record the reasoning and ask the reviewer to reassess. The author cannot dismiss a blocker or approve their own fix. If unresolved, stop and ask the user.
- If the same blocker returns after two rounds, stop looping: re-brief the implementer, change the approach, or ask the user.

## Enforce and report

- Do not declare the change complete or ready, or proceed to shipping, deployment or merge, while the gate is blocked.
- If the reviewer is unavailable or the gate cannot pass, report the blocker and ask the user how to proceed. Do not silently waive or lower the risk tier to bypass it.
- When agents run in parallel, keep their write scopes separate and forbid commands that affect shared state, such as `git stash`, `git reset`, or whole-tree checkouts; agents commit only their own files.
- Keep the gate result in the existing plan or review record when one exists; otherwise include it in the handback. Record reviewer identity, reviewed revision and scope, verdict, findings and resolutions, and remaining checks or risks.
- A pass satisfies only the independent-review gate; required approval, automated checks and release gates still apply.
