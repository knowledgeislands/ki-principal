# Brief - wave1-review

Blind query review for KI > Foundations > Baseline rollout (`ki.baseline-rollout`), under the `ki-coordination` standard's Query review section. You are reviewing one query before it reaches Kris. Read only what you need to check it directly; write nothing in any repository.

## The query

**Context:** No baseline-rollout work has started. The proposed first wave only reads and writes nothing in any repository: `ki territory audit` across six territories (humans-not-robots, legal, personal, equal-remedy, valle-armonia, techmedix), whose repositories are listed in the local `ki` registry; a roadmap conformance sweep looking for retired theme slugs in each repository's `.ki.toml` area map, the issue-ledger form and missing size declarations; and a status check on the harness items KI-HARNESS-GOV-205, KI-HARNESS-GOV-221 and COORD-1 in `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`. Registration and every write wait for Kris's go, repository by repository. Each territory's Capital keeps ownership; ki-trades is on hold until its review on 2026-10-21.

**Query:** Shall the worker launch wave 1 as proposed, read-only, through `ki agent` in run `baseline-rollout`?

**Options:**

- Launch wave 1 as proposed and bring the findings back before any registration or write.
- Launch it with a scope Kris names instead.
- Hold it until after the trades review on 2026-10-21.

## What to check

1. Whether `ki territory audit` and the conformance sweep are truly read-only: check `ki territory audit --help`, `man ki` or the tools-ki source at `/Users/krisbrown/workspaces/knowledge-islands/tools-ki` for any write, registration or network side effect. Do not run anything that could write.
2. Whether anything makes the wave premature, such as the state of KI-HARNESS-GOV-205, KI-HARNESS-GOV-221 or COORD-1, or the trades hold.

## Report

Return a run report in the `ki-coordination` run-report form with one query, WAVE-1, carrying your own recommended option first as `a) (recommended, confidence <high|medium|low> - <one-line reason>)`, the other options beneath, and under Done one line per check with what you verified directly.

Authority: read-only across all repositories; no commits, no pushes, no writes outside the run's state folder.
