# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-impl-fix-4

**🤖 → 👤 Handoff to supervisor · Run report at 23:38 BST · last mark 19:18 BST**

---

## Done

Delivered local main `6c4d2a1aeabdac5ce5ca2e4bd711908d043afcf3`, based on `6c498f3a20a0e9311baac86d47b7dfca812e7f6d`. The hook-backed commit contains only the 16 intended paths; the primary checkout is clean, and the owned worktree and branch are removed. [Integration evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-fix-4.evidence/integration.json).

Read the accepted contract in full from its last tracked accepted revision, `03954f4c`, because its supplied working-tree path was absent. The contract and principal work records were not changed.

- **Codex B1 — lost blocked notifications:** durable stop receipts reconstruct `stop-timeout`, `ownership-unverified` and `containment-unverified` notifications independently of the pending outbox. Publication deduplicates operation/kind identities. Fix: [events.ts:749](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:749). Regression: [agent-control.test.ts:672](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:672).
- **Codex B2 — truncated event history:** the v2 checkpoint stores the complete intended journal, sequence and digest before append. Reads reject missing, truncated, altered or unterminated evidence and invalid cursors; legacy adoption checks surviving receipt and snapshot evidence. Fix: [events.ts:197](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:197). Regressions: [agent-control.test.ts:719](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:719), including empty and valid-prefix truncation, plus same-length rewrites and legacy evidence loss.
- **Opus B1 — dead held supervisors:** shared ownership checks publish one `blocked` event carrying the relevant operation ID. Dead or reused held owners do not count as running; plain wait, next-event wait and watch end visibly. Unfinished controls with a dead holder also preserve their holder evidence and publish their operation ID. Fixes: [scope.ts:8](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/scope.ts:8), [control-store.ts:442](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/control-store.ts:442), [runs.ts:210](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:210). Regressions: [agent-control.test.ts:742](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:742), [agent-control.test.ts:187](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:187), [agent-control.test.ts:132](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:132).

The blocking regressions and related class cases were first run against pristine `6c498f3a`: 13 failed before the fixes. [Before-fix evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-fix-4.evidence/pristine-baseline-regressions.log).

The matrix exposed and closed these additional paths:

- **Post-effect persistence and lock release:** preserve confirmed starts and observed receipts, surface inspection warnings, and keep a later dispatcher observation failure from contradicting a start. Fixes: [control-store.ts:536](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/control-store.ts:536), [locking.ts:14](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/locking.ts:14), [runs.ts:1594](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:1594). Regressions include the existing post-start fault suite and [agent-control.test.ts:9](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:9).
- **Held and queued refusals:** persist gate/disposition reasons before fallible publication; reconstruct their terminal outcomes; publish legacy refusal evidence before removing its queue projection and fence retries by source digest. Fixes: [runs.ts:973](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:973), [runs.ts:1547](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:1547), [runs.ts:1025](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:1025). Regressions: [agent-control-faults.test.ts:124](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control-faults.test.ts:124); the queued-held, dispatch-refusal and legacy-refusal matrix flows.
- **Reports and fast completion:** use the current state-folder report before a protected or partially homed copy; capture completion and queries before relaunch archives their source; publish a fast worker's completion even before its first observation. Fixes: [events.ts:509](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:509), [events.ts:557](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:557), [runs.ts:807](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:807). Regressions: [agent-control.test.ts:264](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:264), [agent-control.test.ts:307](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:307).
- **Torn projections and copies:** verify control, queue, frozen-brief, dispatcher PID and waiter-cursor writes; turn unverified I/O into explicit refusals while preserving a known process start. Fixes: [control-store.ts:366](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/control-store.ts:366), [runs.ts:1128](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:1128), [runs.ts:1688](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:1688). Every applicable matrix mutation exercises these paths.

Fable's held-history, dispatcher-warning and dead-held-running advisories are addressed. Superseded unfinished dependencies now close visibly rather than waiting on a replacement; held history retains its true state. Confirmed packet warnings allow dispatch to continue while unavailable follow-up evidence produces an inspection result. Mixed legacy/numbered pending records now have a total order, and legacy terminal replay remains terminal. Fixes: [runs.ts:306](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:306), [events.ts:432](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:432), [events.ts:463](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:463); regressions: [agent-control.test.ts:630](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:630), [agent-control-faults.test.ts:99](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control-faults.test.ts:99), [agent-control.test.ts:486](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:486), [agent-control.test.ts:521](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:521).

The matrix covers **22 flows, 505 mutation points and 3,568 injected fault cells**, plus **501 real-controller mutation points and 1,002 SIGKILL cells**. Flows cover direct/held/resumed/relaunched work, waiting and closed gates, claimed queued holds, queue/dequeue, normal/timeout/unverified stop, foreground/detached/refused dispatch, legacy refusals, recovery inspection/resolution, status, wait and watch. Recovery inspection has no mutations.

Each fault column below counts both before and after the mutation. Truncation and corruption apply to file content and lock records; directory creation, removal and lock release have no byte payload. Every lock acquisition also receives persistent busy-lock injection.

| Mutation | Points | I/O error | Fenced death | Truncation | Corruption | Busy |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `appendFile` | 44 | 88 | 88 | 88 | 88 | 0 |
| `copyFile` | 2 | 4 | 4 | 4 | 4 | 0 |
| `lock` | 52 | 104 | 104 | 104 | 104 | 52 |
| `mkdir` | 60 | 120 | 120 | 0 | 0 | 0 |
| `rename` | 105 | 210 | 210 | 210 | 210 | 0 |
| `rm` | 19 | 38 | 38 | 0 | 0 | 0 |
| `unlock` | 52 | 104 | 104 | 0 | 0 | 0 |
| `writeFile` | 171 | 342 | 342 | 342 | 342 | 0 |

The assertions preserve the previous journal in a verified witness **before** fixture repair, then verify the exact prefix after recovery, monotonic identities, terminal and operation deduplication, surviving queries, receipts, ownership-loss IDs and bounded/refusing waits. Recovery fixtures restore known damaged bytes or the verified append intent and explicitly retire only their sandbox's abandoned locks. Lock backoff is accelerated in the isolated I/O sweep; normal contention regressions and separate-process probes retain host timers. Worker effects use injected process ports; the killed controllers are real subprocesses. Native provider containment is outside this first-stage evidence. Controller probes ran on macOS 27.0.1 (arm64), Node v24.21.0, Bun 1.4.2 and Vitest 5.0.5; [runtime evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-fix-4.evidence/native-test-runtime.json).

Matrix entry points: [agent-control-matrix.test.ts:510](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control-matrix.test.ts:510), [agent-control-matrix.test.ts:670](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control-matrix.test.ts:670); preservation assertion: [agent-control-matrix.test.ts:491](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control-matrix.test.ts:491). [Complete flow/operation ledger](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-fix-4.evidence/matrix-ledger.json) and [Complete final test transcript](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-fix-4.evidence/coverage-final.log).

- Lint: Biome passed.
- Types: TypeScript passed.
- Tests: 2,018/2,018 passed across 94 files; all 44 matrix tests passed.
- Coverage: 100% — statements 16,748/16,748; branches 11,610/11,610; functions 3,569/3,569; lines 14,170/14,170; thresholds and exclusions unchanged.
- Build and compiled version/help/recovery-help checks: passed.
- Manifest: syncpack lint and format check passed.
- Markdown: rumdl passed.
- Manual: mandoc passed.
- Command inventory: passed.
- Isolated offline full audit: PASS=17, WARN=5, FAIL=0; seven warning findings cover the inline CI version pin, offline mGit overview, undeclared maturity, and unavailable isolated Capital, trade, project and territory registry evidence.
- Compatibility snapshots: seven tests passed unchanged using the brief's supplied macOS temp-path spelling; the canonical-path diagnostic differed only in `/private` alias presentation.
- Commit hooks and post-commit path inspection: passed.

[Standalone gate evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-fix-4.evidence/final-gates.jsonl), [Full audit report](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-fix-4.evidence/audit-final.log), [Compiled smoke evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-fix-4.evidence/build-smoke-final.json).

Deferred advisories: whole-journal replay/checkpoint cost needs a separate indexing and recovery design with benchmarks; changing it during this durability repair would broaden the correctness boundary. Present publication producers retain the control-transaction ordering invariant; a generic guard for hypothetical new producers is deferred until that API is extended. A cross-platform normal-exit/SIGINT/SIGTERM host-cleanup verification policy remains separate; this round adds repeatable SIGKILL recovery coverage, while the earlier reviewers' signal probes remain their evidence.

## In Progress

Independent supervisor review of the integrated commit and the first-stage contract. The coordinator still owns mirroring the supplied 20:59 decision into the principal decision log when its stalled rebase permits it.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 23:38 BST

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [with you] Review wow-day-impl-fix-4 and its fault-injection evidence · supervisor · since 23:38 BST
