# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-impl-rereview2-3

**🤖 → 👤 Handoff to supervisor · Run report at 20:03 BST · last mark 20:03 BST**

---

## Done

Verdict: CHANGES NEEDED

Reviewed `d6df59d9^..7eb0f017` on local `main` at `7eb0f017`; no repository file changed. Typecheck passed, 93 test files and 1,823 tests passed, and the 100 % coverage gate passed, all in a scratch clone at `7eb0f017` under `/var/folders/6b/b4c73j8s6w12g2k9_yl652_h0000gn/T/ki-agents/ways-of-working/wow-day-impl-rereview2-3/tools-ki`. Probe tests and logs are kept under `/var/folders/6b/b4c73j8s6w12g2k9_yl652_h0000gn/T/ki-agents/ways-of-working/wow-day-impl-rereview2-3` (`probe.log` at `7eb0f017`, `probe-old.log` at `166f0cbc`); nothing was committed.

### New findings in `7eb0f017`

- **Blocking 1 — `src/core/agent/controls.ts:52-53`.** The `event()` helper dereferences `.seq` on a journal entry that is absent when `recordEvent` leaves the publication pending; `src/core/agent/events.ts:176-186` now swallows a busy `events.lock` for every kind, so a confirmed stop crashes with an uncaught `TypeError` after `stopped`/`stoppedBy` is persisted (`controls.ts:255-257`) and before `finishOperation`: no receipt, no `ki: error:` line, no recovery route, exit by unhandled exception. The same path covers `dequeued` after the entry is cancelled (`controls.ts:352-356`), `stop-requested` and every `blocked` outcome. At `166f0cbc` the identical scenario was a documented `events-transaction-busy` refusal (exit 1). Reproduced by `probe-a` and `probe-a2`; the attempt state is correct afterwards and a `--request` retry rebuilds the receipt, but the operation's outcome is misreported and its receipt is lost until manual retry.
- **Blocking 2 — `src/core/agent/events.ts:249-258`.** `publicationSeen` no longer marks a `dequeued` publication as ended (`166f0cbc` did, old `events.ts:119-120`). When the held supervisor later fences the cancelled entry and sets the attempt `failed` (`src/core/agent/runs.ts:874-877`), `agentChanges` (`events.ts:404-409`) emits a second terminal event, `worker failed: attempt failed`, for an attempt whose status is `dequeued`. `wait --next` reports a deliberate cancellation as a failure; at `166f0cbc` the second wait returned `ALL FINISHED`. The regression at `src/tests/cli/agent-control.test.ts:1050` counts only `dequeued` events and misses it. Reproduced by `probe-b`.
- **Advisory 3 — `src/core/agent/runs.ts:1397-1407`.** The dispatch catch calls `loadControl` before classifying the error, so a fail-closed evidence refusal there replaces the original error, and the cast at line 1407 would throw on an undefined store. Low likelihood after a queue exists.
- **Advisory 4 — `src/core/agent/processes.ts:97-131`, `src/context.ts:79-92`.** Host signal cleanup and the display interrupt handler are v8-ignored and exercised only through the injected port (`agent-control.test.ts:3014`); the real ordering of lock release before the display handler re-delivers SIGINT is untested.
- **Advisory 5 — `src/core/agent/control-store.ts:382-397`.** After the 120-second bound a held supervisor exits with the refusal and its attempt stays `held` with a dead PID, shown as "held; launch acknowledgement unavailable" (`runs.ts:207`) until an explicit stop marks it failed. Consistent with the no-takeover rule; worth a sentence in the guide.

### Earlier blocking findings, each confirmed fixed

- review-1 unreadable projection: `control-store.ts:73` (ENOENT-only read), `control-store.ts:215-271` (missing projection refused beside journal or receipts); tests `agent-control.test.ts:2542`, `2561`.
- review-1 stale held authority: `runs.ts:409-411` revalidates before and after worktree preparation; test `2813`.
- review-1 duplicate stopped events on retry: `events.ts:217-236` dedupes by publication and operation/kind, `events.ts:498` derives from `stoppedBy` only; tests `604`, `1432`, `2594`.
- review-1 lock age takeover: `locking.ts:14-42` has no age or PID branch; tests `1134`, `2668`.
- review-2 busy lock kills hold/dispatch: `control-store.ts:382-397`; test `2714`.
- review-2 leftover lock: `locking.ts:36-41` names the holder and the manual route; guide section "Recover an abandoned lock"; test `2749`.
- review-2 refusal after claim: `runs.ts:820-834` restores the reserved attempt only when no spawn intent exists; test `2628`.
- rereview-1 catch-all event readers: `events.ts:78-101` fail closed with `events-evidence-unverified`; tests `2916`, `2941`, `2956`, `agent-control-faults.test.ts:103-123`.
- rereview-2 busy publication after spawn: `events.ts:149-193` pending publications, `runs.ts:1397-1401` started entry reported as launched; tests `2968`, `agent-control-faults.test.ts:125`.
- rereview-2 interrupted observer wedges `events.lock`: `locking.ts:44-62` synchronous token-matched release registered through `onExit`; tests `3014`, `3084`.
- rereview-3 advisories 1–4: release on interrupt (same lines); bounded control wait `control-store.ts:382-397` with test `3153`; busy refusal names the holder `locking.ts:36-41` with tests `3153`, `3269`; watch and wait stay pending `runs.ts:1076-1085` with test `3132`.

### Contract properties across the range

Immutable identity, journal-before-effect, idempotent `--request` retries, fail-closed control and event reads, no lock takeover, token-matched release, bounded control waits and the `ALL FINISHED` rule hold. Two properties are broken by `7eb0f017`: exit-code and receipt truthfulness for stop, dequeue and blocked outcomes under a busy event lock (Blocking 1), and no duplicate terminal events for one attempt (Blocking 2).

## In Progress

None.

## Queries

None.

### 🤖 → 👤 Handoff to supervisor · since 20:03 BST

🤖 0 running · 👤 1 you · ⛔ 0 blocked

- [you] decide whether `7eb0f017` returns for a third fix of the two regressions · supervisor · since 20:03 BST
