# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-impl-rereview-3

**🤖 → 👤 Handoff to supervisor · Run report at 19:13 BST · last mark 14:35 BST**

---

## Done

Verdict: ACCEPT

- Reviewer 1, blocking 1 (unreadable `control.json` silently replaced): fixed. `controlRead` fails closed on any non-ENOENT error and `loadControl` refuses a missing projection when a journal, receipts, temporary projection or launch identity exists (`src/core/agent/control-store.ts:73-80`, `215-242`). Regression `review-1: unreadable control projection fails closed without queue mutation` and `review-1: missing projection with existing journal cannot initialise fresh state` exercise both routes.
- Reviewer 1, blocking 2 (held work starts with stale authority): fixed. `startRuntime` runs the frozen selection through `validated` before and again after worktree preparation, so authority, evidence and acceptance digests are rechecked at spawn (`src/core/agent/runs.ts:324-347`, `399-482`). Regressions `review-1: held role rechecks authority|evidence when its gate opens` and `review-1: held acceptance revalidates record digests after waiting`.
- Reviewer 1, blocking 3 (duplicate `stopped` events): fixed. `stoppedBy` is persisted on the attempt and `deriveEvents` emits `stopped` only for that operation; replay restores it from receipts for older projections (`src/core/agent/controls.ts:161-169`, `256`; `src/core/agent/control-store.ts:171-174`). Regressions `review-1: a different stop request and replay cannot duplicate a terminal event` and `stopped receipts restore terminal ownership when an older projection lacks it`.
- Reviewer 1, blocking 4 (`events.lock` deleted by age): fixed. Both locks go through `withRunLock`, which records machine, pid, birth and token, retries boundedly, refuses with the recovery route and releases only when the lock bytes are unchanged; there is no age or PID takeover (`src/core/agent/locking.ts`). Regression `review-1: an observer cannot take a live lock after thirty seconds` expects the contender to refuse and one `done` event.
- Reviewer 2, blocking 1 (busy lock kills hold and dispatch): fixed. Hold and dispatch use `pendingControl`, which retries on `control-transaction-busy` with an injected 1 s sleep (`src/core/agent/control-store.ts:376-389`; `src/core/agent/runs.ts:862`, `1309`). Regression `review-2: a busy transaction keeps the hold|dispatch loop pending`.
- Reviewer 2, blocking 2 (leftover lock wedges the run with no recovery route): fixed as a documented manual route rather than release on interrupt. The refusal cites the guide section, lock bytes carry holder identity, and the guide requires verified holder exit before renaming, never deletion. Regression `review-2: leftover locks refuse with a documented offline recovery route and retain evidence`. The interrupt residue is advisory 1 below.
- Reviewer 2, blocking 3 (refusal after claim wedges the queue as `unconfirmed`): fixed. `dispatchRun` no longer pre-claims; a definite refusal before any spawn intent leaves a role entry queued, and `launchAgent` restores the prior attempt when nothing was spawned (`src/core/agent/runs.ts:821-838`, `1302-1414`). Regressions `review-2: a definite role refusal leaves its queue entry queued without a spawn intent` and `a known worktree preparation refusal leaves a role queue retryable without an effect intent`, the latter asserting zero operations.
- Reviewer 2 advisories 4-9 and reviewer 3 advisories 1-4 and 6 each have the change and the named test the fix report lists; I read each and found them as described. Reviewer 3 advisory 5 needed no change.

New findings, all advisory. None breaks a contract property.

1. `src/context.ts:79-91` with `src/core/agent/locking.ts:36-46`, advisory. The interrupt handler removes its listener and re-raises SIGINT, so the `finally` release in `withRunLock` does not run. A foreground `ki agent stop` interrupted during its grace wait (`src/core/agent/controls.ts:84`, `227`) leaves `control.lock` with the holder identity recorded. Safe, but reviewer 2 asked for release on interrupt and the stop section of the guide does not say Ctrl-C leaves a lock. Fix: release the held lock inside the interrupt handler before re-raising, under the same unchanged-bytes check, or state in the stop guidance that an interrupted grace wait needs the recovery route.
2. `src/core/agent/control-store.ts:376-389`, advisory. `pendingControl` is unbounded and silent. A hold or dispatcher loop facing an abandoned lock waits at 1 s intervals for ever and its status line does not change, so the only signal is a foreground command's busy refusal. Fix: after a bounded number of retries, write one waiting line naming the lock holder to the run's status or events, or refuse with the recovery route; keep no takeover.
3. `src/core/agent/locking.ts:20-33`, advisory. Foreground `launch`, `queue`, `stop` and `dequeue` refuse after about 2 s of contention, while a stop holds `control.lock` for up to 120 s of grace. The refusal says "retry after holder finishes" but does not name the holder, so an operator cannot tell a live stop from an abandoned lock without opening the file. Fix: include the lock's machine, pid and birth in the busy refusal text and JSON.
4. `src/core/agent/events.ts:291-292` with `src/core/agent/runs.ts:1074-1075`, `1225-1229`, `1440`, advisory. Observers derive events under `events.lock` and end with `events-transaction-busy` exit 1 after about 2 s of contention; the regression test confirms this for a single-shot observer, and `watch` and `wait` call the same path with no retry. A long-running `watch` therefore exits when it collides with another observer or a stop. Fix: have `watch` and `wait` sleep and retry on the busy refusal, as they hold no effect intent.

Checks, in a scratch copy of `166f0cbc` under the temp directory:

- Agent test files (control, control faults, compatibility, events, agent): 362 passed.
- Full suite: 93 files, 1,780 tests passed, exit 0.
- Compatibility goldens executed against a scratch copy of baseline `d6df59d9^`: 7 passed, so role-free `--rules` tiers and `reconcile` receipts are byte-identical to the pre-feature baseline apart from the documented additive selection line.
- Contract conformance re-read: unproved capabilities refuse (`containment-unverified`, `profile-dormant`, `model-evidence-unavailable`, `acceptance-contract-unavailable`); no lock is taken on age or PID; no silent fallback; `recover` and `reconcile` stay distinct; wake absent.
- Test helper diff against baseline is additive only. No checkout was edited, committed or pushed.

## In Progress

Nothing. The scratch copies and the full-suite log remain under `/var/folders/6b/b4c73j8s6w12g2k9_yl652_h0000gn/T/ki-agents/ways-of-working/wow-day-impl-rereview-3/`.

## Queries

**Context** Advisory 1 is the one point where the fix departs from reviewer 2's stated remedy: it documents a manual recovery route instead of releasing the lock on interrupt, and the fix report records this as a deliberate choice. The lock cannot be stolen and the holder is recorded, so the contract holds either way. **Query** Is the documented manual route accepted for the first stage, or should the implementer add interrupt-time release before publication? **Options** a) (recommended, confidence high - the contract forbids release while an effect may be live and the manual route is verified by test) Accept the manual route now and carry advisories 1-4 into the second build stage. b) Commission a small follow-up on the same branch for advisories 1 and 3 before publication, since both touch only refusal text and the interrupt handler. c) Require all four advisories fixed before publication.

### 🤖 → 👤 Handoff to supervisor · since 19:13 BST

🤖 0 running · 👤 1 you · ⛔ 0 blocked

- [with you] Disposition of the ACCEPT verdict and advisories 1-4 for `166f0cbc` · supervisor · since 19:13 BST
