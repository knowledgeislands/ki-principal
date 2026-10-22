# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-impl-rereview4-2

**🤖 → 👤 Handoff to supervisor · Run report at 00:01 BST · last mark 19:18 BST**

---

## Done

Verdict: CHANGES NEEDED

This was an independent re-review of `d6df59d9^..6c4d2a1a` against the [agent control contract](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/agent-control-contract.md), read at its brief path. The review read the final tree across the whole range and ran two deterministic probes in a scratch copy. No file in any repository was changed.

### Earlier blocking findings

- **[wow-day-impl-rereview3-1](wow-day-impl-rereview3-1.report.md) B1, lost blocked notifications: fixed.** [events.ts:744-766](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:744) reconstructs `blocked` from `stop-timeout`, `ownership-unverified` and `containment-unverified` receipts. [controls.ts:56-58](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/controls.ts:56) suppresses a publication failure only after the outcome is journalled.
- **[wow-day-impl-rereview3-1](wow-day-impl-rereview3-1.report.md) B2, truncated history: fixed, but over-corrected.** The `events.history` checkpoint ([events.ts:142-149](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:142), [254-272](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:254)) refuses empty or prefix truncation, altered bytes and an advanced cursor, and sequences no longer restart. The same refusal now also catches the writer's own interrupted append, which is new finding B1 below.
- **[wow-day-impl-rereview3-2](wow-day-impl-rereview3-2.report.md) B1, dead held supervisor hangs `wait`: fixed.**
  - [scope.ts:15](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/scope.ts:15) classifies a held attempt with a dead supervisor as `held supervisor unavailable`.
  - [runs.ts:222-229](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:222) reports it as `blocked`.
  - [events.ts:603-622](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:603) publishes one non-terminal `blocked` event per operation.
  - [runs.ts:1692](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:1692) makes `wait` exit 1.
- **The earlier blockers tabulated in [wow-day-impl-rereview3-3](wow-day-impl-rereview3-3.report.md): the properties still hold at `6c4d2a1a`.**
  - Control reads fail closed on a torn line or projection mismatch: [control-store.ts:122-217](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/control-store.ts:122) and [219-292](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/control-store.ts:219).
  - A spawn without an observed outcome replays as `unconfirmed`.
  - Saves are verified: [control-store.ts:366-382](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/control-store.ts:366).
  - Locks are created with `wx` and released only on a matching token, on SIGINT, SIGTERM and normal exit, with no age or PID takeover: [locking.ts:26-59](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/locking.ts:26).
  - Holder liveness is used for notification only: [control-store.ts:442-472](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/control-store.ts:442).
  - Busy waits are bounded at 120 seconds ([control-store.ts:475-490](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/control-store.ts:475)) and at 100 × 20 ms for observer locks.
  - Replacement of `unconfirmed`, `stop-requested` and `stop-timeout` attempts is fenced: [runs.ts:782-785](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:782).
  - A failed `launch` or `held` publication never turns a started worker into a failure: [events.ts:360-377](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:360).
- **Pending publication is reconciled exactly once.** [events.ts:383-461](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:383) de-duplicates by publication ID and by operation, start and end keys before appending, and removes pending files only afterwards. No duplicate or lost event was found while the journal is readable.

### New findings

1. **Blocking B1: an interrupted event append wedges the whole run until someone repairs it by hand.**
   - **Cause:** [events.ts:309-310](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:309) commits the checkpoint before `appendFile`. Any stop between the two leaves the checkpoint ahead of the journal: SIGINT or SIGTERM (whose handler at [processes.ts:103-108](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/processes.ts:103) releases the locks and re-raises the signal mid-append), SIGHUP, SIGKILL, power loss, or a plain `appendFile` error such as ENOSPC. [events.ts:267](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:267) then refuses every read.
   - **Probe P1** (production legacy path, no adapter): after the second launch's append was lost, `status`, `wait --next`, `watch` and a new `launch` all exited 1 with `events-evidence-unverified`. The run is blocked until an owner decides on recovery.
   - **Why it should change:** the checkpoint already holds the digest-verified intended journal, so rolling forward when the journal is an exact byte prefix of it is safe and loses nothing.
   - **Guide contradiction:** [background-agents.md:78](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/guides/user/background-agents.md:78) says the next observer reconciles "including an interrupted journal append", while [:80](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/guides/user/background-agents.md:80) requires an owner decision.
   - This is blocking because a non-corrupting interruption of the writer's own two-step commit can stall a run.
2. **Advisory A1: the fault matrix cannot catch B1 and accepts any refusal.**
   - Before asserting, every cell restores damaged bytes, deletes both locks and rewrites `events.jsonl` from the checkpoint ([agent-control-matrix.test.ts:566-575](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control-matrix.test.ts:566)), so recovery after a fault is never observed.
   - When status refuses, the only check is a broad regex ([:657-660](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control-matrix.test.ts:657)).
   - Every cell uses a managed adapter with containment ([:235-269](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control-matrix.test.ts:235)), which production lacks. The production legacy branches ([runs.ts:239](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:239), [485](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:485), [574](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:574)) and the v8-ignored signal cleanup are outside the matrix.
3. **Advisory A2: on the production path, a launch that provably never started still fences the agent name with no supported route out.**
   - A `spawn` error, such as a missing `claude` binary, rejects before any child exists ([processes.ts:77-80](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/processes.ts:77)). Even so, [runs.ts:486-499](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:486) and [575-594](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:575) record `claim-unconfirmed`.
   - [runs.ts:784-785](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:784) refuses relaunch, and [controls.ts:500](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/controls.ts:500) refuses `recover resolve` without an adapter. A held attempt with no pid file is fenced the same way ([runs.ts:782-783](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:782)).
   - Probe P2 confirmed this: `wait` exits 1 naming the operation, which is good. This behaviour follows contract §spawn ("unable to prove either case keeps the claim blocked") and is documented at [background-agents.md:98](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/guides/user/background-agents.md:98), but a missing binary is a likely first-run failure.
4. **Advisory A3: a reused PID can hide a lost control holder.** [control-store.ts:469](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/control-store.ts:469) suppresses the `ownership-unverified` notification when any process holds the crashed holder's PID. Plain `wait` ([runs.ts:1665-1697](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:1665)) then keeps polling with no overall bound. The lock records the holder's birth time, which would rule out a reused PID.
5. **Advisory A4: a failed `stop-requested` publication aborts the stop and cannot be reconstructed.** [controls.ts:190-193](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/controls.ts:190) saves `stop-requested` and then throws ([:56-58](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/controls.ts:56)) before any signal is sent. `deriveEvents` has no `stop-requested` path. This only happens with an adapter; the run fails closed, and a retried stop proceeds.

### Checks (scratch copy of `6c4d2a1a`, isolated HOME, offline)

- Full suite with coverage: 94 files and 2018 tests passed, with 100% lines, branches and functions against the 100% gate, exit 0.
- `tsc --noEmit`: clean. Biome: clean, with one info message.
- Probes P1 and P2 ran in-process through `sandbox()`. The probe source and output are in the [evidence folder](wow-day-impl-rereview4-2.evidence/).
- The primary checkout and live agent state were not touched.

## In Progress

Nothing.

## Queries

### EVENT-ROLL-FORWARD - How to recover an interrupted event append

**Context** B1: an interrupted append leaves `events.history` ahead of `events.jsonl`, and every status, watch, wait and launch refuses until the owner restores the journal by hand. The checkpoint already holds the exact, digest-verified bytes that were meant to be written.

**Query** Should observers roll the journal forward automatically, or should this stay an owner-decided recovery?

**Options**

a) (recommended, confidence high - this is the writer's own commit protocol, and the bytes are already verified) Under `events.lock`, roll forward only when the journal is an exact byte prefix of the checkpoint journal and the digest matches; keep refusing every other mismatch. Correct [background-agents.md:78-80](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/guides/user/background-agents.md:78), and make the matrix assert recovery without its manual repair step.

b) Keep the refusal, add an explicit `ki agent recover events` command that performs the same verified roll-forward, and correct guide line 78.

c) Accept the current behaviour and correct guide line 78 only.

Reply: `EVENT-ROLL-FORWARD a` (or b, c)

---

### 🤖 → 👤 Handoff to supervisor · since 00:01 BST

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [with you] wow-day-impl-rereview4-2: CHANGES NEEDED, one blocking finding (interrupted event append wedges the run) and query EVENT-ROLL-FORWARD · supervisor · since 00:01 BST
