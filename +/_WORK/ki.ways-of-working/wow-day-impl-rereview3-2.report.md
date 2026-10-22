# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-impl-rereview3-2

**🤖 → 👤 Handoff to supervisor · Run report at 20:55 BST · last mark 19:18 BST**

---

## Done

Verdict: CHANGES NEEDED

This is an independent re-review of tools-ki `d6df59d9^..6c498f3a`. I read the contract from commit `03954f4c` because the ki-principal working tree is mid-rebase and the file is missing there. I changed nothing in any repository; the primary checkout is still clean at `6c498f3a`.

**Blocking**

B1. When a held attempt's supervisor dies, `wait` and `wait --next` hang forever and no event is emitted.

- Causes: a crash, a kill, a reboot, or the 120 s control-lock bound making `holdAgent` exit 1.
- The code path:
  - `src/core/agent/events.ts:482` returns no events when `held && !alive`.
  - `src/core/agent/runs.ts:210-217` keeps the attempt counted as running, with "held; supervisor unavailable".
  - `src/core/agent/runs.ts:1556-1578` (`waitForRun`) has no overall bound, so it loops for as long as the run looks live.
- Probe P2 (unmanaged, every process dead):
  - At `6c498f3a`, the second `wait --next` and the plain `wait` both hang, and the only events are held and predecessor-failed.
  - At `7eb0f017`, the same probe misreported the worker as "failed: exited without DONE" and then reached ALL FINISHED.
  - Fix-3 replaced a misreport with silence. The contract instead requires "lost ownership produces `blocked` event with operation ID", and a held attempt with no supervisor is never visibly blocked.
- Recovery: `stop` refuses on the unmanaged path production uses today (exit 1, containment-unverified), but `launch --relaunch` recovers it as attempt 2. Nothing in `wait` or `status` points to that route.
- Test gap: `src/tests/cli/agent-control.test.ts:3507` only asserts that no failed event appears, and never runs `wait` afterwards.

**Advisory**

A1. The guide contradicts itself on held-launch bounds.

- `docs/guides/user/background-agents.md:104` says busy control transactions "keep held launches … pending".
- `docs/guides/user/background-agents.md:88` says they are bounded at 120 s.
- `docs/guides/user/background-agents.md:59-60` also omits the held-but-unsupervised state.

A2. In `src/core/agent/events.ts:251-318`, `publishPending` sorts by `publicationOrder` and falls back to mtime. When legacy and ordered pending files are mixed, that comparator is not transitive, so publication order is undefined.

A3. On replay of a journal written before this range, `src/core/agent/events.ts:320-339` no longer treats legacy `could not launch:` blocked events or status-form `failed:` events as terminal. After snapshot loss, an old journal could therefore get a second terminal event.

A4. In `src/core/agent/runs.ts` `dispatchRun`, the dispatcher exits on an `inspection` result. The confirmed start is reported correctly, but the remaining queue is left showing "no dispatcher" until someone redispatches.

A5. `readSnapshot` in `src/core/agent/events.ts` replays the whole journal on every read, so watch and wait cost grows with run length.

**Earlier blocking findings, re-checked in source**

- Missing-journal refusal is fixed: `src/core/agent/events.ts:113-127`. Base `d6df59d9^` always wrote the journal, so the refusal is safe for older runs.
- Duplicate terminal events after snapshot loss are fixed for new journals by the explicit `terminal` flag at `src/core/agent/events.ts:320-339`; legacy journals are A3.
- A packet failure after a confirmed start no longer reports the worker as not started: `src/core/agent/runs.ts:864-875`. The same holds in `holdAgent` (`src/core/agent/runs.ts:899-974`) and in dispatch.
- Watch and wait are bounded at 120 s on contention and name the holder: `src/core/agent/runs.ts:1155-1166`.
- Status-form events no longer get lost or counted as terminal: the `terminal: false` handling in `agentChanges`.
- The 120 s hold misreport is gone, but what replaced it is B1.
- The stop and dequeue TypeError on a missing sequence is fixed: `src/core/agent/controls.ts:52-60`.
- Dequeue no longer emits a second terminal event: `src/core/agent/events.ts:476-478`.
- I did not individually re-trace findings from rounds before the second re-review; their regression tests pass.

**New-code checks**

- Fail-closed reads hold: `src/core/agent/context.ts` `read` raises `agent-evidence-unverified` for any error other than ENOENT.
- Lock release holds: `src/core/agent/locking.ts` `withRunLock` keeps the action's error when release fails, release is token-matched, and there is no age or PID takeover.
- Stop path: if `stop-requested` is saved (`src/core/agent/controls.ts:191-193`) and then the event write fails, a retry resumes the same operation without a duplicate signal or a false "dead before stop". No defect.
- Pending receipts publish exactly once and replay without duplicates, both by source and in probes. The one exception is A3, legacy journals only.

**Gates, run in a scratch copy with a sandboxed HOME**

- Typecheck: passes.
- Full suite: 93 files and 1,882 tests pass.
- Coverage gate: 100% statements, branches, functions and lines.
- The first coverage run lost 2 boundary tests because the scratch copy lacked `tooling/boundaries/node_modules`. Once I copied that in, the boundary tests and the full re-run passed.

**Evidence and cleanup**

- The probe file, probe logs at both commits, coverage logs and typecheck log are in `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview3-2.evidence/`.
- The temp folder is empty.

## In Progress

Nothing.

## Queries

**Context** B1: a held attempt with no live supervisor makes `wait` hang forever and emits nothing. The run before fix-3 misreported it as failed instead.

**Query** Which outcome should the fix deliver?

**Options**

a) (recommended, confidence high - this matches the contract's "lost ownership produces blocked event" and keeps the worker non-failed.) Emit one non-terminal `blocked` event with the attempt's operation ID when a held attempt is found with no live supervisor. `wait --next` returns it, `wait` and `status` treat the run as blocked rather than live, the event names the `launch --relaunch` recovery route, and a regression test runs `wait` after a supervisor dies.

b) Give `wait` an overall timeout and leave the held state as it is. This removes the hang, but the run still never shows as blocked.

c) Accept as is and document manual recovery. This leaves `wait` able to hang forever, against the contract.

### 🤖 → 👤 Handoff to supervisor · since 20:55 BST

🤖 0 running · 👤 1 you · ⛔ 0 blocked

- [with you] wow-day-impl-rereview3-2: CHANGES NEEDED, choose the B1 fix direction · supervisor · since 20:55 BST
