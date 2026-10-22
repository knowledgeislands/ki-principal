# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-impl-rereview2-2

**🤖 → 👤 Handoff to supervisor · Run report at 20:02 BST · last mark 19:18 BST**

---

## Done

Verdict: CHANGES NEEDED

I re-reviewed d6df59d9^..7eb0f017 in tools-ki, checking it against the accepted contract (blob at ki-principal 03954f4c) and every earlier report. Each new finding is backed by a probe test that runs against both 7eb0f017 and 166f0cbc. The probe source and its logs are in [the evidence folder](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview2-2.evidence/).

### Findings

1. **Blocking: a worker's `blocked:` or `failed:` status line now loses its terminal event** (`src/core/agent/events.ts:249-255`, `:373`, `:433-441`).
   - Cause: `readSnapshot` now replays the whole journal through `publicationSeen` on every read. `publicationSeen` ends the attempt on any `failed` event, and on any `blocked` event without an operation, and the progress-protocol status forms produce exactly those events.
   - Probes P1a to P1c:
     - After a `blocked:` line, DONE with a report produces no `done` event.
     - After a `blocked:` line, an exit without DONE produces no `failed: exited without DONE` event.
     - After a `failed:` line, DONE produces no `done` event.
   - On 166f0cbc, all three produce their events.
   - Effect: terminal evidence is lost, `wait --next` never returns the finish, and gates miss the outcome.
2. **Blocking: the 120 s `pendingControl` bound turns a busy control lock into a held attempt reported as failed** (`src/core/agent/runs.ts:861`, `:1318`; `src/core/agent/control-store.ts:393`).
   - Cause: in `holdAgent`, the bound is uncaught, so the hold process exits 1.
   - Probe P2: status then reports `failed: exited without DONE (… held until …)`, the control attempt stays `held`, and dependants' gates close. The dispatcher dies in the same way.
   - This is realistic: worktree preparation, which includes the node_modules copy in `worktrees.ts:38-70`, holds the control lock for about 50 s on this machine. The 1 s retry is not fair to waiters.
3. **Blocking: stop and dequeue crash with a raw TypeError after their effect when `events.lock` is busy** (`src/core/agent/controls.ts:34-53`).
   - Cause: `event()` assumes that `recordEvent` published synchronously. Since 7eb0f017, `recordEvent` leaves a busy-lock event pending, so `.find(...).seq` throws `Cannot read properties of undefined (reading 'seq')`.
   - Probe P3: the dequeue entry is `cancelled`, but no receipt is written and the command dies instead of returning `cancelled-before-start` with exit 0. A retry after the lock is released does succeed, with one `dequeued` event.
   - Probe P4: stop saves `stop-requested` and then crashes. The `stopped` path at `controls.ts:262` would crash in the same way after the scope has emptied, leaving no receipt.
   - 166f0cbc gave a typed busy refusal here, so this is a regression.
4. **Advisory: `pendingObservation` waits forever and silently** (`src/core/agent/runs.ts:1076-1085`, used at `:1237` and `:1462`).
   - An abandoned `events.lock` spins `watch` and `wait` forever, with no status line and no reference to the recovery route.
   - `watch` and `wait` have no overall timeout of their own, so nothing else bounds them.
   - This could be argued as blocking under the brief's "bounded waiting in watch and wait"; see the first query.
5. **Advisory: pending publications are ordered by random UUID rather than creation order** (`src/core/agent/events.ts:207`). Probe P5 published `held` before `launch` for the same attempt in 3 of 8 runs.
6. **Advisory: `publicationSeen` does not handle `dequeued`** (`src/core/agent/events.ts:249-260`). This is harmless today, but it is inconsistent with `stopped`.
7. **Advisory: after a post-spawn error, a legacy queue entry with no `entry` id is still dropped as `failed`** (`src/core/agent/runs.ts:1405-1418`). This is the residual of RR2 B1.
8. **Advisory: real signal-driven lock release is untested on the host.**
   - The release code in `src/core/agent/processes.ts:96-130` is inside the v8-ignore block at `:65-133`.
   - The tests inject `onExit` instead (`src/tests/cli/agent-control.test.ts:3015`, `:3084`), so no test sends a real SIGINT or SIGTERM under Bun.
9. **Advisory: in `withRunLock`, a release error raised in `finally` can mask the action's own error** (`src/core/agent/locking.ts`).

### Earlier blocking findings

- **R1 B1, control evidence read fail-closed:** fixed (`control-store.ts`, `controlRead`/`loadControl`).
- **R1 B2, runtime revalidation at start:** fixed (`runs.ts` ~399-410).
- **R1 B3, `stoppedBy` recorded on stop:** fixed (`controls.ts:161-169`, `:256-262`).
- **R1 B4, no age-based lock takeover:** fixed (`locking.ts`). The lock is taken by an exclusive create and released only when the token matches.
- **R2 B1, waiting on a busy lock in hold and dispatch:** fixed, but the new 120 s bound regresses into finding 2.
- **R2 B2, holder identity and manual recovery route:** fixed. A busy refusal names the holder and cites `background-agents.md#recover-an-abandoned-lock`.
- **R2 B3, refusals before claim:** fixed.
- **RR1 B8, evidence reads fail closed, with only ENOENT treated as absence:** fixed (`events.ts` ~78-95).
- **RR2 B1, busy publication after spawn is not reported as failure:** fixed for launch, hold and dispatch (`agent-control.test.ts:2969`). The legacy-entry residual is finding 7.
- **RR2 B2, lock release on SIGINT, SIGTERM and exit:** implemented with token-matched synchronous release; host coverage is the gap in finding 8.

### Checks

- **Suite and coverage gate in scratch at 7eb0f017:** passed. 93 files and 1,823 tests passed, with 100% coverage of statements, branches, functions and lines.
- **Fail-closed evidence reads:** hold.
- **Spawned worker never reported as failed or not started:** broken by finding 2 (a held attempt is reported failed) and finding 1 (DONE is lost after a status line).
- **Pending-event reconciliation, exactly once:** no duplicates were seen, but terminal events are lost (finding 1) and ordering is not preserved (finding 5).
- **Lock acquisition, token-matched release and manual recovery with no age or PID takeover:** hold in code; real-signal coverage is missing (finding 8).
- **Bounded waiting:**
  - Launch and queue are bounded.
  - Hold and dispatch are bounded but misreport the outcome (finding 2).
  - Watch and wait are unbounded and silent (finding 4).
- **Tests genuinely exercise the paths:** partly. No test covers a status-form line followed by DONE or exit, busy `events.lock` during stop or dequeue, hold beyond the bound, or event ordering.
- **Contract properties across the range:**
  - Contract §Events ("receipt retries and event derivation cannot emit duplicate terminal events"; acceptance 5) holds for duplicates but fails for lost terminal events.
  - Stop and dequeue receipts fail under a busy events lock (finding 3).
  - All other properties reviewed hold.
- **Primary checkouts:** tools-ki stayed clean on `main` at 7eb0f017. Nothing was edited, committed or pushed, and no remote call was made.
- **Scratch:** the evidence is homed and the temp folder is empty.

## In Progress

Nothing. The three blocking findings need a fix run, followed by another re-review.

## Queries

### WAIT-BOUND - How should watch and wait behave on a busy events lock?

**Context:** Hold and dispatch now give up after 120 s, which is finding 2. Watch and wait retry for ever without saying anything, which is finding 4. The brief asks for bounded waiting in all of them, but if any of them gives up, a live run can end up misreported.

**Query:** What should hold, dispatch, watch and wait each do when the lock stays busy?

**Options:** a) (recommended, confidence high - this stops a busy lock misreporting a run, and still shows the owner a stuck lock) All four keep waiting. Every 60 s each one prints a status line naming the lock holder and the recovery route. Only launch, queue and the one-shot control commands stop after the 120 s bound, with a typed busy refusal. b) All four stop at 120 s with a typed busy refusal, and status shows a stopped hold as "hold-interrupted", not as failed. c) Keep the current behaviour and accept that a slow worktree preparation can make a hold look failed.

### CONTRACT-PATH - Which copy of the contract counts as current?

**Context:** `design/agent-control-contract.md` is missing from the ki-principal working tree, and that checkout's HEAD is detached. The contract is still in commit 03954f4c on `main`, and I reviewed against that copy.

**Query:** Was the contract moved or pruned on purpose, and is the 03954f4c copy still the accepted one?

**Options:** a) (recommended, confidence medium - it is the accepted commit, and nothing later in the history replaces it) Treat 03954f4c as the accepted contract, and have the coordinator check the ki-principal checkout's detached HEAD. b) Point me to the contract's new location, and I will re-check the property list against it.
