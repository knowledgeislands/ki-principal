# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-impl-rereview4-3

**🤖 → 👤 Handoff to supervisor · Run report at 00:19 BST · last mark 00:19 BST**

---

## Done

Verdict: ACCEPT

Read-only review of `d6df59d9^..6c4d2a1a` in a detached scratch worktree at `6c4d2a1a`; no file in any repository was changed and no live agent state was touched. Paths below are relative to `tools-ki`.

Checks in the scratch worktree: full suite with coverage 2018 of 2018 tests passed in 94 files, 44 fault-matrix flows included; coverage thresholds 100% statements, branches, functions and lines, 247 files fully covered; Biome clean; tsc clean. Two tests in `src/tests/boundaries.test.ts` failed only because the scratch worktree lacked the isolated `tooling/boundaries/node_modules`; after linking that folder both pass, and they exercise no `src/` code, so the coverage figures are unaffected.

### Earlier blocking findings, verified at `6c4d2a1a`

All fixed; none reintroduced by a later commit in the range (removed lines in `src/core` between `6c498f3a` and `6c4d2a1a` are refactors, not dropped guards).

- Review 1, unreadable control state treated as absent: fixed. `src/core/agent/control-store.ts:75-82` fails closed except ENOENT; `:224-245` refuses a missing projection beside evidence.
- Review 1, held work starts with stale authority: fixed. `src/core/agent/runs.ts:442-444` revalidates before and after worktree preparation.
- Review 1, duplicate `stopped` events: fixed. `src/core/agent/controls.ts:264`, `control-store.ts:177`, `events.ts:791-815` derive one `stopped` per `stoppedBy`.
- Review 1, `events.lock` stolen by age: fixed. `src/core/agent/locking.ts:14-85` has no age or PID takeover; refusal names the holder and the guide route.
- Review 2, busy lock kills hold or dispatch: fixed. `control-store.ts:475-490` bounds retries at 120 s; used at `runs.ts:948` and `runs.ts:1491`.
- Review 2, leftover lock wedges a run: fixed by holder identity and release on SIGINT, SIGTERM and exit, `locking.ts:9-10`, `processes.ts:97-130`, plus the manual route in `docs/guides/user/background-agents.md` "Recover an abandoned lock" (no takeover by design).
- Review 2, refusal after claim wedges the queue: fixed. `runs.ts:907-921` restores the queued entry when no spawn operation exists.
- Re-review 1, unreadable event evidence treated as absent: fixed. `src/core/agent/events.ts:94-101`.
- Re-review 2, post-spawn publication refusal reports a started worker as failed: fixed. `events.ts:361-377` swallows busy and evidence errors only for `launch` and `held`; confirmed start preserved at `runs.ts:705-712`, `:895-906`, `:1005-1009`, `:1597-1604`.
- Re-review 2, interrupted observer wedges: fixed. `processes.ts:97-130` releases on signals; `runs.ts:1227-1238` bounds observer waits; called at `runs.ts:1391` (watch) and `:1675` (wait).
- Re-review 2 round 1, missing journal resets history: fixed, `events.ts:200-211`. Snapshot recovery duplicates failed events: fixed, `events.ts:702`, `:866-870`. Abandoned event lock wedges watch and wait: fixed, as above.
- Re-review 2 round 2, `blocked:`/`failed:` status lines lose terminal identity: fixed, `events.ts:659`. Busy lock turns a held attempt into `failed`: fixed, a held supervisor that gives up after 120 s is observed as `blocked` ownership loss, never `failed` (`runs.ts:222-230`, `scope.ts:15`). Stop or dequeue TypeError with busy events lock: fixed, `controls.ts:53-59`.
- Re-review 2 round 3, `dequeued` publication not marked ended: fixed, `events.ts:344-348`, `:600-601`.
- Re-review 3 round 1, lost `blocked` notifications after a failed pending write: fixed, `events.ts:744-766` reconstructs from stop receipts; regression `src/tests/cli/agent-control.test.ts:672`. Truncated history resets identities: fixed, `events.ts:142-149`, `:254-272`; regression `:719`.
- Re-review 3 round 2, dead held supervisor hangs `wait`: fixed, `scope.ts:15`, `runs.ts:222-230`, `events.ts:602-622`; regression `agent-control.test.ts:742`.

### `6c4d2a1a` review

No blocking defect found. The fault matrix is genuine: it wraps the real `node:fs` and `node:fs/promises` mutation calls (`src/tests/cli/agent-control-matrix.test.ts:43-170`), enumerates every durable write from a baseline run rather than a hand-kept list (`:515-532`), replays each site under I/O error before and after, fenced death, truncation, corruption and busy lock, asserts the journal was never reset (`:491-505`, `:560`), asserts a spawned or signalled worker is never reported failed or not started (`:561-565`, `:652-656`), and the SIGKILL matrix really kills a separate process at each site (`src/tests/fixtures/agent-crash-child.ts:35-39`) then checks sequence continuity, terminal uniqueness and one `blocked` per lost operation (`:738-771`).

Advisory findings:

- Advisory, `src/core/agent/events.ts:265-269`: a process killed between the checkpoint write and the journal append leaves every observer refusing `journal differs from committed history` until the coordinator restores the bytes by hand, although the checkpoint digest already proves the exact intended bytes; fail-closed and documented, but a verified self-heal would remove a manual step.
- Advisory, `src/core/agent/control-store.ts:467-469` and `runs.ts:222-230`: holder and supervisor liveness is PID-only (`processes.ts:88`), so a reused PID delays the ownership-loss notification until the reusing process exits; notification only, never takeover or signalling.
- Advisory, `src/core/agent/runs.ts:1640-1646`: once one start is confirmed, a later control or event evidence failure ends dispatch with an inspection line and exit 0, leaving remaining queue entries undispatched; visible in `dispatch.log` and `status`, but a non-zero foreground exit would make it harder to miss.
- Advisory, `src/core/agent/runs.ts:1006-1010`: a held supervisor whose 120 s busy wait expires exits, so the held attempt then needs inspection and `launch --relaunch`; resuming the hold loop after an expired wait would keep the attempt alive without weakening the bound.
- Advisory, `src/tests/cli/agent-control-matrix.test.ts:657-660`: after test-side repair a cell passes when `status` still refuses with any `unverified|unconfirmed|injected|ENOENT|no such run` text, so the matrix proves fail-closed behaviour and no false failure but not that every cell is recoverable by the documented route.
- Advisory, worktree setup: the boundary check needs `tooling/boundaries/node_modules` in each linked worktree; worth a line in the contributor guidance.

## In Progress

Nothing.

## Queries

None.

### 🤖 → 👤 Handoff to supervisor · since 00:19 BST

🤖 0 running · 👤 1 you · ⛔ 0 blocked

- [you] accept this review's verdict · supervisor · 00:19 BST
