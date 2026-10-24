# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-impl-rereview-2

**🤖 → 👤 Handoff to supervisor · Run report at 19:12 BST · last mark 14:35 BST**

---

## Done

Verdict: CHANGES NEEDED

First-round blocking findings:

- Review 1, blocking 1 (unreadable control state): fixed. `controlRead` fails closed on anything except ENOENT, and a missing projection beside a journal, receipts, temporary projections or identity-bearing launch evidence is refused. The regression fails on `cb165c20` and passes on `166f0cbc`.
- Review 1, blocking 2 (stale authority on held work): fixed. `startRuntime` revalidates the frozen selection before and after worktree preparation, inside the spawn transaction. Authority, evidence and acceptance-digest regressions fail on `cb165c20` and pass on the fix.
- Review 1, blocking 3 (duplicate terminal stop events): fixed. `stoppedBy` binds the one stopping operation, and replay, stop and `deriveEvents` all honour it. The regression fails on `cb165c20` and passes on the fix.
- Review 1, blocking 4 (events lock stolen by age): fixed. The age takeover is gone, and the regression fails on `cb165c20` and passes on the fix. However, the replacement introduces new findings 1 and 2.
- Review 2, blocking 1 (busy lock kills hold and dispatch): fixed for hold and dispatch through `pendingControl`, with regressions that fail on `cb165c20` and pass on the fix. Foreground role-free `launch` and `queue` still refuse after about 2 s (advisory 3).
- Review 2, blocking 2 (leftover lock wedges a run): fixed as far as the fix went. Locks now record holder identity and a documented offline recovery route, with a regression that fails on `cb165c20`. The reviewer's request to release the lock on interrupt was not implemented, and the same wedge now also reaches `events.lock` (new finding 2).
- Review 2, blocking 3 (refusal after claim wedges the queue): fixed. Known refusals now pass before any claim or spawn intent, and definite preparation failures leave the entry queued. The role-refusal regression fails on `cb165c20`. The worktree-preparation case also passes on `cb165c20`, so the role-refusal test is the real regression.

New findings:

1. **Blocking - event publication after a spawn can now refuse, so a started worker is reported as failed.** The `withRunLock` bounded refusal ([locking.ts:20](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/locking.ts:20), used by [events.ts:61](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:61)) makes `recordEvent` throw `events-transaction-busy` after about 2 s of contention. The old observer waited instead. Three paths call it after the external effect: direct launch ([runs.ts:777-779](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:777)), the hold loop ([runs.ts:900-901](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:900)) and dispatch, whose role-free catch sends the error to `drop` ([runs.ts:1395-1396](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:1395)). I reproduced this through the CLI seam on the host-like unmanaged fixture:
   - A role-free dispatch with an observer holding `events.lock` for 2.5 s spawned the worker, then printed `could not launch worker: events-transaction-busy`, appended a `failed` event and rewrote the `started` entry to `cancelled`/`failed`. The dependants' gates now close as "was failed" while the worker runs.
   - A role-free `launch` spawned its worker and exited 1.
   - On `cb165c20`, the same dispatch probe reports `launched worker` with the entry `started`.

   This breaks unchanged role-free behaviour, the contract's rule never to infer an entry's fate from an error, and truthful outcomes. Spawn-failure reporting at [runs.ts:455](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:455) has the same exposure: the busy error replaces the `claim-unconfirmed` recovery message, although the state stays correctly fenced. **Fix:**
   - Never let event publication after an effect fail the operation. Keep it pending through a busy events lock, as `pendingControl` does, or leave the event to journal-driven derivation.
   - In `dispatchRun`, never `drop` an entry whose control state is `started` or that has a spawn operation for its token.
   - Add busy-events-lock regressions for launch, hold and dispatch, asserting exit 0, `started`, one `launch` event and no `failed` event.
2. **Blocking - an interrupted observer now wedges every role-free run until an owner-cited offline recovery.** Before this range, a leftover `events.lock` cleared itself after 30 s (`d6df59d9^:src/core/agent/events.ts:59`). Now nothing releases it:
   - `withRunLock` releases only in `finally`.
   - Ctrl-C re-raises SIGINT ([context.ts:81-88](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/context.ts:81)).
   - A tool-timeout kill of `ki agent wait --next` also skips `finally`.

   An interrupt during derivation therefore leaves the lock behind. With a leftover holder, I reproduced exit 1 `events-transaction-busy` for `status` and `wait --next` (even with the clock 120 s on), and a role-free `launch` that spawned its worker and then exited 1. The guide's route ([background-agents.md:72-80](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/guides/user/background-agents.md:72)) needs a cited owner decision and supervisor exit proof for what is a routine interrupt of an effect-free observer. **Fix:**
   - Have the holder release its own unchanged lock on SIGINT and SIGTERM for the events critical section. That section has no external effect, and releasing your own lock is not a takeover.
   - Keep `wait` and `watch` pending on a busy events lock instead of exiting.
   - Keep the rule that no lock is taken over on age or PID.
   - Add a regression that interrupts an observer mid-derivation, then checks that `status`, `wait` and `launch` still succeed.
3. **Advisory - foreground role-free `launch` and `queue` still refuse after about 2 s while another launch holds the control lock through worktree preparation** ([runs.ts:411](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:411), inside the transaction from [runs.ts:664](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:664) and [runs.ts:961](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:961)). The refusal is explicit and retryable, and the contract allows holding through spawn, but before this range these commands never failed this way. **Fix:** prepare the worktree before taking the transaction and revalidate inside it, or let foreground commands wait for a longer bounded time with a visible message.

Whole-range judgement, apart from the findings above:

- First-stage conformance holds: wake is absent, role profiles are dormant, accept refuses with `acceptance-contract-unavailable`, and native stop refuses with `containment-unverified` without signalling.
- No lock is taken over on age or PID.
- `ki agent reconcile` and role-free `--rules` are unchanged apart from the documented additive selection line. The parent-baseline goldens pass.
- The new unused-declaration and footer-ceiling refusals sit only on role paths.

Checks:

- Review regressions on the old code: 19 of the fix's new review regressions fail and 2 pass when run against `cb165c20` ([log](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview-2.evidence/review-regressions-on-cb165c20.log)).
- Focused agent suites on `166f0cbc`: 362 of 362 passed.
- Full suite with the coverage gate on a clean `166f0cbc` copy: 1,780 tests across 93 files passed, thresholds met.
- Typecheck: passed.
- Probes for new findings 1 and 2: reproduced on `166f0cbc` and absent for finding 1 on `cb165c20` ([probe source](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview-2.evidence/probes.test-fragment.ts), [evidence folder](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview-2.evidence)).
- Read-only boundary: no repository edits, commits, pushes, installs, live workers or remote calls; tools-ki remains clean at `166f0cbc`.

## In Progress

Nothing is running. The scratch copies remain in `/var/folders/6b/b4c73j8s6w12g2k9_yl652_h0000gn/T/ki-agents/ways-of-working/wow-day-impl-rereview-2/`, because the brief forbids deletion. The supervisor needs to clear them before `ki agent close`. The evidence worth keeping is already in the `.evidence` folder beside this report.

## Queries

No outstanding queries.
