# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-ci-check

**🤖 → 👤 Handoff to supervisor · Run report at 22:12 BST · last mark not supplied in the brief**

---

## Done

- Harness CI on `main` is green at its head: the latest `CI` run (job `build`) passed on e8f1da6e, which is also `origin/main`; read-only, no edits or commits.
- 1b8ab57b, 979e075a and 9c17df3c are all ancestors of e8f1da6e (`git merge-base --is-ancestor`), so `build` has run green on and after all three.
- There is no workflow named `build`: `build` is the single job in the `CI` workflow, and the brief's check is answered against that job.

| Workflow | Latest run | Commit | Result |
| --- | --- | --- | --- |
| CI (job `build`) | 2026-10-20 09:11 UTC, push | e8f1da6e | success |
| Update ki pin | 2026-10-20 12:07 UTC, schedule | - | success |

Red runs in the last 15, all superseded by later green runs:

| Run | Commit | Failing job and step | First error |
| --- | --- | --- | --- |
| 39340974158, 39349567954, 39351248673 (19 Oct 23:20 to 20 Oct 01:03 UTC) | 95d36f86, 871e98ea, c49a40b3 | `build` / Test | `(fail) a failing Husky gate still refuses the commit through the stub`, with three more hook tests (`expect(received).toBe(expected)`, `Command failed: /bin/sh .husky/pre-commit`) |
| 39354134595 (20 Oct 01:33 UTC) | 30cbbd1d | `build` / Audit | `ki-work-roadmap` FAIL=7, first `fail [item body shape (ITEM-3)] docs/roadmap/KI-HARNESS-GOV-200-thread-folder-closed-list.md - body must contain Goal → Context → ...` |
| 39340524075, 39368942825 (cancelled) | 185624b0, ba4055ef | `build` / Test | no error line: the Test step hung until the 6-hour job limit and the run was cancelled, with orphan `bun` processes terminated at clean-up |

- Hook-test failures: pre-existing and fixed. They started with the Husky/Knip hook changes on 19 Oct, and runs have been green since `fix(hooks): refuse the commit when bun is not on PATH` (01:46 UTC).
- Roadmap ITEM-3 audit failure: one run only, fixed by the next push, which was green.
- Six-hour Test hangs: not new and still intermittent. They happened at 23:16 UTC on 19 Oct and again at 04:19 UTC on 20 Oct, on ba4055ef, after the hook fix. Green runs came before and after both, so the hang is unresolved but does not block anything.

## In Progress

Nothing is running.

Outstanding - no action requested now: the intermittent 6-hour Test hang (two of the last 15 runs) has no known cause. Each one burns six hours of runner time before it is cancelled. A job `timeout-minutes` or a bounded test timeout would make it fail fast. That is a candidate record for the harness owner, not part of this run.

## Queries

No outstanding queries
