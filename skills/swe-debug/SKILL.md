---
name: swe-debug
description: "Find and fix a defect following the swe-docs debugging rules. Use when fixing a bug, a failing test, a regression or unexpected behavior."
---

# Debug with swe-docs

Uses `docs/guidelines` from swe-docs (<https://github.com/cs-clarence/swe-docs>). If it is missing, say so and stop; do not invent rules. Repo overrides win (`docs/guidelines/core/precedence.md`). If a skill named below is not installed, follow the guideline files it covers.

1. Read `docs/guidelines/authoring/debugging-and-bug-fixing.md` and follow it from reproducing the defect to confirming the fix.
2. Write the test that fails without the fix, using `authoring/testing/testing.md`. If a regression test is impractical, say why and how else the fix was verified. For unreliable tests read `authoring/testing/flaky-tests.md`.
3. If the fix touches a contract, data or concurrency, read the matching file from the "Which files apply" table in `docs/guidelines/README.md`.
4. If the cause turns out bigger than expected, stop and follow `core/when-to-ask.md`.
5. Finish with `swe-self-review` and check `core/definition-of-done.md`.
