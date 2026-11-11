---
name: swe-debug
description: "Find and fix a defect following the swe-docs debugging rules. Use when fixing a bug, a failing test, a regression or unexpected behavior."
---

# Debug with swe-docs

Guidelines live in `docs/guidelines` of the current repository (installed from <https://github.com/cs-clarence/swe-docs>). If that folder is missing, tell the user and point them to the swe-docs README install section; do not invent rules. Repository overrides take precedence per `docs/guidelines/core/precedence.md`. Scale effort to risk using `docs/guidelines/core/risk-tiers.md`.

1. Read `docs/guidelines/authoring/debugging-and-bug-fixing.md` and follow it from reproducing the defect to confirming the fix.
2. Write the test that fails without the fix, using `authoring/testing/testing.md`. If a regression test is impractical, say why and how else the fix was verified. For unreliable tests read `authoring/testing/flaky-tests.md`.
3. If the fix touches a contract, data or concurrency, read the matching file from the "Which files apply" table in `docs/guidelines/README.md`.
4. If the cause turns out bigger than expected, stop and follow `core/when-to-ask.md`.
5. Finish with the `swe-self-review` skill if installed, otherwise follow `authoring/self-review.md` and check `core/definition-of-done.md`.
