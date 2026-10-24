# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-impl-rereview2-1

**🤖 → 👤 Handoff to supervisor · Run report at 19:52 BST · last mark 19:18 BST**

---

## Done

Verdict: CHANGES NEEDED

1. **Blocking B1 — Missing event journal silently resets history:** [events.ts:101](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:101) treats ENOENT as an empty journal even beside an existing snapshot and control receipts; after preserving the journal by rename, public status succeeds and replaces sequences 1–3 with sequences 1–2, loses the stop-requested event and invalidates existing waiter cursors; refuse missing authoritative history beside prior evidence instead of silently rebuilding a subset.
2. **Blocking B2 — Snapshot recovery duplicates failed terminal events:** [events.ts:373](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:373) restores terminal flags without the observed status identity, while [events.ts:421](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:421) republishes an unchanged failed status regardless of that terminal flag; public status after snapshot loss appends a second failed event for the same attempt, so the earlier event-evidence blocker is only partly fixed.
3. **Blocking B3 — Confirmed worker start can still end as a CLI failure:** [runs.ts:479](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:479) performs fallible packet persistence after the durable started receipt, and [runs.ts:836](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:836) rethrows it; an injected post-spawn packet-path failure makes public launch reject with EISDIR despite one spawned worker, running state and a confirmed started receipt, rather than returning that known outcome with an inspection warning.
4. **Blocking B4 — Abandoned event exclusion wedges watch and wait:** [runs.ts:1077](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:1077) retries contention forever without a deadline or holder/recovery message, and both [watch](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:1237) and [wait](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:1462) enter it before recognising completion; both remain pending with an already-finished worker and an abandoned lock after fifteen injected minutes, until the probe deliberately aborts.

Earlier blocking findings, independently checked against source and the passing regressions:

- Review 1, blocking 1 — FIXED: [control-store.ts:73](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/control-store.ts:73) refuses non-ENOENT reads, and [control-store.ts:215](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/control-store.ts:215) refuses missing projections beside existing evidence; read-denial and missing-evidence cases pass.
- Review 1, blocking 2 — FIXED: [runs.ts:409](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:409) revalidates frozen selections before and after worktree preparation immediately before spawn; held authority, withdrawn model evidence and changed acceptance-record cases pass.
- Review 1, blocking 3 — FIXED for the reported stop-operation race: [controls.ts:256](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/controls.ts:256) persists stoppedBy, and [events.ts:497](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:497) derives only its terminal stop event; different-request, replay and interrupted-receipt cases pass.
- Review 1, blocking 4 — FIXED: [locking.ts:26](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/locking.ts:26) acquires exclusive creation without age or PID takeover; the live-holder-over-thirty-seconds regression passes.
- Review 2, blocking 1 — FIXED for the reported control contention: [control-store.ts:382](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/control-store.ts:382) now retries for a bounded 120 seconds in launch, queue, hold and dispatch; the busy-holder and deadline/refusal cases pass.
- Review 2, blocking 2 — FIXED: [locking.ts:44](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/locking.ts:44) releases only matching bytes, [processes.ts:111](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/processes.ts:111) wires real SIGINT/SIGTERM/exit cleanup, and the [manual recovery route](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/guides/user/background-agents.md:78) requires verified holder exit, quiescent contenders and preservation by rename; real helper-process tests verify both locks and changed-token preservation.
- Review 2, blocking 3 — FIXED: [runs.ts:820](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:820) preserves retryable entries when no spawn intent exists, and [runs.ts:1393](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:1393) launches without the former premature dispatcher claim; role-refusal and preparation-refusal cases pass without worker effects.
- Re-review 1, blocking event-evidence finding — PARTLY FIXED: [events.ts:78](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:78) now refuses denied/corrupt reads, and missing snapshots preserve done/stopped/query identities in the supplied cases; B1 and B2 independently refute the broader fail-closed and exactly-once claim.
- Re-review 2, blocking 1 — Reported busy-event cases FIXED by [events.ts:149](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:149) and the dispatcher started-entry guard; direct, held and dispatched launches remain started and reconcile one pending launch; B3 exposes the remaining post-start failure boundary.
- Re-review 2, blocking 2 — Signal-release defect FIXED by the lock changes above; bounded observer recovery is still broken as B4, rather than an interrupt leaving its own lock behind.
- Re-review 3 — No blocking findings were recorded; its unbounded-wait advisory remains materially unresolved for event contention as B4.

Range review: inspected d6df59d9, cb165c20, 166f0cbc and 7eb0f017 against the [accepted contract](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/agent-control-contract.md); stop containment refusal, identity fences, transactional cancellation, evidence-gated recovery, dormant roles and distinct recover/reconcile namespaces remain present, while B1–B4 prevent first-stage acceptance.

Offline suite and coverage on an archived 7eb0f017 with private dependency copies: 1,813 tests across 92 files pass; statements, branches, functions and lines all meet the 100% gate; HTTP installer fixtures were excluded under the no-network instruction, so this is not an unfiltered full-suite result.

Compatibility against the unchanged d6df59d9^ archive: all seven golden cases pass, covering decision reconciliation for ordinary/inspect/resolve run names and every role-free footer tier.

Typecheck, read-only Biome check over 28 relevant files and complete-range whitespace check: pass on the unmodified archived product tree.

Independent CLI probes: five expected assertions fail and reproduce B1, B2, B3 and both B4 callers; the supplied snapshot regressions cover done/query recovery, the observer retry test releases its holder on the first retry, and the post-start fault test covers queue projection rather than direct-launch packet persistence, leaving these defects untested.

Real local helper-process signal checks: all twelve combinations pass for control/events locks, SIGINT/SIGTERM/normal exit, and owned/changed tokens; these helpers launch no agent or native session and establish lock cleanup only.

Repository boundary: no repository file, tracked or ignored, was changed; dependencies resolve entirely inside scratch storage, the primary checkout remains clean, and no remote call, live agent operation, commit or publication occurred.

## In Progress

Nothing is running.

Outstanding - no action requested now: the supervisor owns routing B1–B4 for fixes and a further independent review; this run does not accept or amend the implementation.

Verification limitations: no native worker containment, spawn recovery, model suitability, scoped acceptance capability or wake delivery was enabled or claimed; installer HTTP fixtures and repository-wide governance audits were not run.

Retained material: [evidence manifest](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview2-1.evidence/manifest.json), [CLI reproductions](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview2-1.evidence/review-probes.test.ts), [probe results](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview2-1.evidence/probes.log), [coverage results](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview2-1.evidence/coverage.log) and [signal results](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview2-1.evidence/signal-probes.log); scratch copies and temporary output have been removed after preservation.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 19:52 BST

🤖 0 running · 👤 1 you · ⛔ 0 blocked

- [with you] Four blocking findings from the independent first-stage re-review · supervisor · since 19:52 BST
