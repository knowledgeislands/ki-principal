# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-impl-rereview3-3

**🤖 → 👤 Handoff to supervisor · Run report at 20:58 BST · last mark 20:57 BST**

---

## Done

Verdict: ACCEPT

Independent read-only re-review of `d6df59d9^..6c498f3a` in `tools-ki` (local `main` at `6c498f3a`, unchanged). No file in any repository was changed. All line references are at `6c498f3a`, paths relative to `tools-ki/`.

### Verification in a scratch worktree

- Detached scratch worktree of `6c498f3a` under the run's temporary folder, with its own XDG state, config, cache and data homes; the primary checkout and live agent state were not touched.
- `bun run test:coverage`: 93 files, 1,882 tests passed, coverage 100% statements, branches, functions and lines, exit 0. A first run failed only because the `tooling/boundaries` dependency folder had not been copied into the scratch tree; after copying it the rerun was clean. Both logs are homed in `wow-day-impl-rereview3-3.evidence/`.
- Biome check on the agent sources and both control test files: clean. `tsc --noEmit`: clean.
- Independent real-signal lock probe (my own script, not fix-3's): for both `control.lock` and `events.lock`, SIGINT, SIGTERM and normal exit each released an owned lock and left a replaced-token lock untouched, 12 of 12 cases as expected. Script and results homed in the evidence folder.
- Scratch worktree removed and pruned from the primary checkout after the report was written.

### Earlier blocking findings — all confirmed fixed

| Finding | Evidence at 6c498f3a | Regression test |
| --- | --- | --- |
| Review 1 B1 unreadable `control.json` silently replaced | `src/core/agent/control-store.ts:73-80` reads fail closed except ENOENT; `:215-242` refuses a missing projection beside journal, receipts, temp files or launch identity | `agent-control.test.ts:2543`, `:2562` |
| Review 1 B2 held work starts with stale authority | `src/core/agent/runs.ts:419-421` revalidates before and after worktree preparation | `:2815` |
| Review 1 B3 one stop produces several `stopped` events | `src/core/agent/controls.ts:169-177` `stoppedBy` fence; `src/core/agent/events.ts:300-306` dedupes by publication and operation/kind | `:2595` |
| Review 1 B4 `events.lock` stolen by age | `src/core/agent/locking.ts:24-42` exclusive create, bounded retries, busy refusal naming holder and recovery route; no age or PID branch exists | `:2669`, `:3271` |
| Review 2 B1 busy lock kills hold and dispatch | `src/core/agent/control-store.ts:382-397` bounded 120 s pending wait; `src/core/agent/runs.ts:674`, `:1399` wrap hold and dispatch in it | `:2715` |
| Review 2 B2 leftover lock wedges run with no route | `src/core/agent/locking.ts:35-42` names machine, PID, birth, token and the guide anchor; `docs/guides/user/background-agents.md` "Recover an abandoned lock" | `:2750`, `:3155` |
| Review 2 B3 refusal after claim wedges queue as unconfirmed | `src/core/agent/runs.ts:1505-1520` classifies only when spawn intent exists; `:1521` rethrows role refusals | `:2629`, `:2654` |
| Rereview-1 B8 catch-all readers reset identities | `src/core/agent/events.ts:92-108` `evidenceRead`/`parseEvidence`; `:113-157` `readEvents` refuses missing journal beside any prior evidence | `:2918`, `:2943` |
| Rereview-2 B1 busy publication after spawn reports failed | `src/core/agent/events.ts:230-247` busy and launch/held evidence errors are swallowed once the pending record is durable; `src/core/agent/runs.ts:865-875` returns the started result | `:3016`, `:3066`, `:3656` |
| Rereview-2 B2 interrupted observer leaves `events.lock` | `src/core/agent/locking.ts:52-58` host `onExit` registration, token/byte-matched release `:44-51` | signal probe; `:3086` |
| Rereview2-1 B1 missing journal silently resets history | `src/core/agent/events.ts:113-157` refuses on `events.history`, snapshot, advanced cursor or operations | `:3348`, `:3615`, `:3687` |
| Rereview2-1 B2 snapshot recovery duplicates failed terminal events | `src/core/agent/events.ts:323-339` explicit `terminal` flag; `:486-491` single `attempt failed` | `:3361`, `:3372`, `:3723` |
| Rereview2-1 B3 post-start packet failure rejects launch | `src/core/agent/runs.ts:480` confirms the PID before any persistence; `:865-875` | `:3403`, `:3625`, `agent-control-faults.test.ts:194` |
| Rereview2-1 B4 `pendingObservation` unbounded | `src/core/agent/runs.ts:1155-1165` bounded at 120 s via injected clock and sleep | `:3424` |
| Rereview2-2 B1 `blocked:`/`failed:` status line loses terminal event | `src/core/agent/events.ts:504-507` status-form events carry `terminal: false` | `:3372` |
| Rereview2-2 B2 held attempt reported failed after 120 s bound | `src/core/agent/runs.ts:210-217` held with dead supervisor stays held; `gate` `:291-295` keeps waiting | `:3507` |
| Rereview2-2 B3 / Rereview2-3 B1 `TypeError` on `.seq` under busy lock | `src/core/agent/controls.ts:34-61` `event()` returns `number \| undefined` and only `stop-requested` rethrows | `:3451` |
| Rereview2-3 B2 dequeued entry later emits `attempt failed` | `src/core/agent/events.ts:477` stopped/dequeued end without a new event; `src/core/agent/runs.ts:987-1012` legacy queue filtering | `:3482`, `:3842`, `:3868` |

Each test above was read, not only counted: they drive the public `run()` seam with injected processes, clocks and sleeps, rename or corrupt the real evidence files, and assert on the journal and receipts afterwards.

### New-defect review of 7eb0f017 and 6c498f3a

No blocking defect found. Fail-closed reads, no false "failed" or "not started" for a spawned worker, exactly-once pending publication (`events.ts:251-320` dedupes then removes pending files only after the journal append, so a crash between the two replays as a no-op), token-matched release on all three exit paths, no age or PID takeover, and bounded waits in launch, queue, hold, dispatch, watch and wait all hold at `6c498f3a`.

Advisory findings, none blocking:

- Advisory: `src/core/agent/runs.ts:784-787` — relaunching a name whose held attempt's supervisor has died records the superseded held attempt in history as `failed` although it never started; a dependant bound to that token then closes with "was failed". No event is emitted, so no run outcome is misreported, but the label is untrue to the attempt's life.
- Advisory: `src/core/agent/runs.ts:1491-1499` — after any confirmed start with an inspection warning the dispatcher returns and stops; remaining queued entries wait until a dispatcher is started again. Fail-closed and logged, but the guide does not say the dispatcher ends in this case.
- Advisory: `src/core/agent/runs.ts:210-217`, `:1414-1416` — a held attempt whose supervisor died after the 120 s bound counts as running for the dispatcher and keeps dependants waiting; the only supported way forward is `launch --relaunch` (`:755`, `:789`), while the guide says "inspect preserved control evidence before recovering it" without naming that command.
- Advisory: `src/core/agent/events.ts:294-298` — the pending-record sort compares `publicationOrder` only when both sides carry it, else modification time; a mix of records with and without the field, possible only from pending files written by the unreleased intermediate commits, sorts inconsistently.
- Advisory: `src/core/agent/processes.ts` host `onExit` and `src/core/agent/locking.ts:52-58` remain v8-ignored and are exercised only by out-of-suite probes (fix-3's and mine); worth a documented repeatable probe in the repository's verification policy.
- Advisory: `src/core/agent/events.ts:220-224` — `publicationOrder` is journal length plus pending count plus one, computed by producers under `control.lock`; a producer that does not hold `control.lock` (none exists today) would break the order guarantee. Comment documents the assumption; a guard would make it explicit.

### Contract across the whole range

- The properties hold for the net range `d6df59d9^..6c498f3a`. The three intermediate commits `d6df59d9`, `cb165c20` and `166f0cbc` do not satisfy them on their own; that is what the earlier reviews found and the later commits fixed. No property fixed in one commit was reopened by a later one.
- `reconcile` grammar is untouched across the range: the `src/commands/agent/index.ts` diff adds only `--authority`, `--acceptance`, `--dry-run` and `--json` to launch and queue; `recover inspect|resolve` lives in the new `control.ts`. Role acceptance remains disabled by option text and by the `selection.ts` dormant path.
- Evidence files read: `src/core/agent/{locking,processes,events,control-store,controls,runs,context}.ts` in full at `6c498f3a`, the three later commits' diffs, `agent-control.test.ts:2500-3900`, `agent-control-faults.test.ts:99-394`, the guide's recovery sections, and the contract at ki-principal commit `03954f4c`.

## In Progress

Nothing. The scratch worktree is removed; the temporary folder holds only disposable copies that `ki agent close` may remove.

## Queries

### CONTRACT-PATH

- Context: the brief's contract path `+/_WORK/ki.ways-of-working/design/agent-control-contract.md` is absent from the ki-principal worktree because that checkout has a stalled interactive rebase (62 commands done, onto `a139a5ec`). I read the contract from the accepted commit `03954f4c` instead. Rereview2-2 raised the same gap.
- Query: should the ki-principal rebase be finished or aborted before the publication decision, so the accepted contract is on disk for the next reader?
- Options:
  - a) (recommended, confidence high - the accepted commit is unambiguous and this review used it) Treat the review as complete on `03954f4c`; have the coordinator resolve the ki-principal rebase separately before publication.
  - b) Hold publication until the rebase is resolved and the file is back on disk, then re-read for drift.
  - c) Re-point the brief for the other reviewers at the commit reference and proceed.

### 🤖 → 👤 Handoff to supervisor · since 20:58 BST

🤖 0 running · 👤 1 you · ⛔ 0 blocked

- [you] accept this review's verdict and settle CONTRACT-PATH · supervisor · 20:58 BST

```text
wow-day-impl-rereview3-3: Verdict ACCEPT at 6c498f3a. All 18 earlier blocking findings confirmed fixed with file:line evidence; no new blocking defects in 7eb0f017 or 6c498f3a; six advisories (held-attempt history label, dispatcher stops after inspection warning, held dead-supervisor recovery route undocumented, mixed publicationOrder sort, v8-ignored signal cleanup, publicationOrder lock assumption). Suite 1882/1882 and 100% coverage, Biome and tsc clean, independent signal probe 12/12, all in a scratch worktree. One query: CONTRACT-PATH (ki-principal rebase stalled; contract read from 03954f4c).
```
