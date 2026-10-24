# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-impl-rereview4-1

**🤖 → 👤 Handoff to supervisor · Run report at 00:24 BST · last mark 00:08 BST**

---

## Done

Verdict: CHANGES NEEDED

Reviewed local main 6c4d2a1a and the cumulative first-stage range d6df59d9^..6c4d2a1a against the accepted [agent control contract](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/agent-control-contract.md). No product repository edit or commit was made.

### Findings

- **Blocking R4-ARCHIVE — a retried interrupted relaunch turns a completed predecessor into a failed one.** [runs.ts:808](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:808) determines historical outcome from the current packet, but [runs.ts:672](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:672) moves that packet before [runs.ts:825](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:825) persists the terminal history.

  Independent reproduction: launch attempt 1, queue a dependant bound to its token, write its DONE and report, and fail the archive rename of worker.prompt.md after worker.pid and worker.status have moved. The first relaunch refuses; retrying relaunch succeeds but persists attempt 1 as failed although its done event survives. Dispatch then cancels the dependant with a false predecessor-failed reason. Preserve the verified prior outcome durably before any archive move and make partial archive retries recover the same outcome; test each interrupted archive move followed by relaunch and dependent dispatch. [Reproduction and observations](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview4-1.evidence/archive-probe.json), [public-CLI probe](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview4-1.evidence/review-probes.test.ts:65).

- **Blocking R4-RESERVATION — a real controller crash before spawn intent strands a valid launch reservation without a supported recovery route.** [runs.ts:824](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:824) persists a held identity before creating its operation, while [runs.ts:782](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:782) refuses its retry for missing acknowledgement, [scope.ts:31](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/scope.ts:31) refuses observation for missing operation identity, and [controls.ts:437](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/controls.ts:437) provides no resolution without a spawn operation.

  Independent reproduction uses the committed crash child to SIGKILL its own controller immediately after the first control.json rename. The child records zero worker starts and no spawn intent exists. After positively observing controller exit and preserving its abandoned lock by rename, status refuses and launch --relaunch refuses; there is no operation ID to inspect or resolve. This is a legitimate journal-before-effect crash window, rather than the forged missing-operation case covered by the existing regression. Add a durable recoverable preparation/reservation phase, preserving the current fences for genuine unacknowledged spawn operations. [Crash trace and observations](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview4-1.evidence/preintent-probe.json), [crash fixture:42](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/fixtures/agent-crash-child.ts:42).

- **Blocking R4-DISPATCH — dispatch reports successful completion while a held attempt still has unverified ownership.** [runs.ts:1509](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:1509) excludes blocked held attempts from both the running count and the uncertainty exit, so [runs.ts:1631](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:1631) reaches its all-finished result with that attempt unresolved.

  Independent reproduction launches a held native-style attempt, makes its acknowledged supervisor unavailable, and dispatches an empty queue: dispatch exits 0 and reports completion while status retains held plus ownership-unverified and the original operation ID. This contradicts the contract's completion guard and the blocked outcomes of watch/wait. It is introduced by the latest held-ownership classification; the new regression at [agent-control.test.ts:132](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:132) actually expects dispatcher exit 0 in the dependent-queue variant. Drain blocked dependants if appropriate, then return an explicit blocked result until the held uncertainty is settled; cover empty and non-empty queues. [Reproduction and observations](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview4-1.evidence/held-dispatch-probe.json).

- **Advisory R4-SIGNALS — the repeatable real-host signal-release checks remain outside the committed suite.** [processes.ts:65](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/processes.ts:65) excludes host glue from coverage, and the matrix's injected process port at [agent-crash-child.ts:131](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/fixtures/agent-crash-child.ts:131) does not exercise SIGINT, SIGTERM or ordinary-exit registration; the independent 24-case Node/Bun probe passes and is worth retaining as an automated regression. [Probe and results](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview4-1.evidence/probes.log), [host-signal child](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview4-1.evidence/signal-child.ts).

### Earlier blocking findings

The following confirms the originally reported cases at 6c4d2a1a; it does not claim the wider failure classes are closed, because the three findings above are counterexamples.

- Initial review 1 B1, unreadable/missing control projection: fixed; src/core/agent/control-store.ts:75 distinguishes ENOENT and :219 refuses missing projections beside prior evidence; regression src/tests/cli/agent-control.test.ts:3322.
- Initial review 1 B2, stale held authority/model/acceptance evidence: fixed; src/core/agent/runs.ts:442 validates before and after worktree preparation; regressions src/tests/cli/agent-control.test.ts:3351 and :3597.
- Initial review 1 B3, duplicate stopped events across request IDs/replay: fixed; src/core/agent/controls.ts:169 and :263 retain stoppedBy, and src/core/agent/events.ts:865 deduplicates terminal and operation identities; regression src/tests/cli/agent-control.test.ts:3374.
- Initial review 1 B4, live event lock stolen by age: fixed; src/core/agent/locking.ts:23 uses exclusive creation, bounded refusal and no age/PID takeover; regression src/tests/cli/agent-control.test.ts:3451.
- Initial review 2 B1, transient control contention kills hold/dispatch: fixed for the reported contention cases; src/core/agent/control-store.ts:475 supplies a 120-second bound to launch, queue, hold and dispatch; regression src/tests/cli/agent-control.test.ts:3497.
- Initial review 2 B2, abandoned lock without recovery route: fixed; src/core/agent/locking.ts:44 checks unchanged bytes, src/core/agent/processes.ts:111 registers exit/signal cleanup, and docs/guides/user/background-agents.md:84 requires positive exit/restart proof, quiescence and preserved evidence; real-host probes pass.
- Initial review 2 B3, definite pre-spawn refusal becomes an uncertain claim: fixed for the reported exceptions; src/core/agent/runs.ts:1574 preflights before spawn intent and :907 restores retryable preparation failures; regressions src/tests/cli/agent-control.test.ts:3411 and :3650; crash interruption remains R4-RESERVATION.
- First re-review 1, denied event journal/snapshot reads and snapshot-loss duplication: fixed for the reported cases; src/core/agent/events.ts:94 fails closed and :557 replays journal identities; regressions src/tests/cli/agent-control.test.ts:3700 and :3740.
- First re-review 2 B1, busy post-spawn event publication misreports a running worker as failed: fixed; src/core/agent/events.ts:333 keeps durable pending publications, src/core/agent/runs.ts:895 preserves acknowledged starts, and :1601 protects dispatch outcomes; regressions src/tests/cli/agent-control.test.ts:3753 and src/tests/cli/agent-control-faults.test.ts:256.
- First re-review 2 B2, interrupted observer leaves its owned events lock: fixed; src/core/agent/locking.ts:53 registers byte-matched cleanup through the host signal port at src/core/agent/processes.ts:111; independent Node/Bun SIGINT, SIGTERM and normal-exit cases pass.
- Second re-review 1 B1, missing event journal resets history: fixed; src/core/agent/events.ts:197 refuses absence beside checkpoints, snapshot, advanced cursor or prior operations; regression src/tests/cli/agent-control.test.ts:4135.
- Second re-review 1 B2, snapshot recovery duplicates failed terminal/status events: fixed; src/core/agent/events.ts:472 retains status identity independently of terminal identity; regressions src/tests/cli/agent-control.test.ts:4148 and :4160.
- Second re-review 1 B3, post-start packet persistence rejects launch: fixed; src/core/agent/runs.ts:503 records the acknowledgement before fallible persistence and :895 returns that outcome with an inspection warning; regressions src/tests/cli/agent-control.test.ts:4190 and src/tests/cli/agent-control-faults.test.ts:278.
- Second re-review 1 B4, unbounded watch/wait contention: fixed; src/core/agent/runs.ts:1227 bounds event-lock contention at 120 seconds while preserving holder/recovery details; regression src/tests/cli/agent-control.test.ts:4212.
- Second re-review 2 B1, worker blocked/failed progress suppresses its eventual terminal notification: fixed; src/core/agent/events.ts:659 explicitly keeps progress nonterminal; regression family src/tests/cli/agent-control.test.ts:4160.
- Second re-review 2 B2, expired held-supervisor control wait invents worker failure: fixed for the reported failure notification; src/core/agent/scope.ts:8 and src/core/agent/runs.ts:221 retain an ownership-unverified held attempt; regression src/tests/cli/agent-control.test.ts:4294.
- Second re-review 2 B3 and second re-review 3 B1, stop/dequeue dereference absent event sequence after effect: fixed; src/core/agent/controls.ts:34 permits an unpublished event sequence and src/core/agent/control-store.ts:536 retains the observed receipt; regression family src/tests/cli/agent-control.test.ts:4239.
- Second re-review 3 B2, cancelled held attempt later emits failed: fixed; src/core/agent/events.ts:601 suppresses failure for dequeued identities and :463 recognises dequeue as terminal; regression src/tests/cli/agent-control.test.ts:4269.
- Third re-review 1 B1, failed pending writes lose required blocked notifications: fixed; src/core/agent/events.ts:745 reconstructs timeout/ownership/containment warnings from control receipts and :865 deduplicates operation/kind; regression src/tests/cli/agent-control.test.ts:671.
- Third re-review 1 B2, valid-prefix/empty journal truncation reuses sequences and loses events: fixed; src/core/agent/events.ts:142 commits exact append intent and :254 checks sequence count/digest, with cursor bounds at :274; regression src/tests/cli/agent-control.test.ts:718.
- Third re-review 2 B1, dead acknowledged held supervisor silently hangs wait forms: fixed for wait/watch; src/core/agent/scope.ts:8 supplies the operation identity, src/core/agent/events.ts:609 emits blocked, and src/core/agent/runs.ts:1692 and :1397 refuse unresolved loss; regression src/tests/cli/agent-control.test.ts:741; dispatch remains inconsistent under R4-DISPATCH.

The other supplied review reports introduce no additional blocking finding. The supplied contract is present and byte-identical to accepted ki-principal revision 03954f4c, so the earlier contract-path query does not recur.

### Whole-range and matrix assessment

Reviewed the net d6df59d9^..6c4d2a1a change, including selection, identity, stop/dequeue, reconciliation, event derivation and legacy compatibility introduced before the latest fix. Intermediate commits are not individually conformant: cb165c20 still has the age-based event lock, 166f0cbc has finally-only cleanup, and 7eb0f017 dereferences the absent event sequence. The final cumulative range retains R4-ARCHIVE and R4-RESERVATION, while the latest held-ownership classification produces R4-DISPATCH; the contract therefore does not hold across the delivered first stage.

All 44 supplied matrix tests pass: independently recounted totals are 22 flows, 505 interface mutation sites, 3,568 injected fault cells, 501 separate-controller mutation sites and 1,002 SIGKILL cells. The matrix genuinely enumerates real filesystem mutation calls and runs both interface faults and separately killed controllers; its native worker/process-control effects are injected fixtures. The read-only recovery-inspection row has zero mutation points. This is meaningful durability evidence, including preservation witnesses checked before fixture repair, but it is not a proof of complete recovery.

The non-matrix diagnostic passes all 1,974 cases but leaves coverage below threshold: unhit lines include control projection verification at src/core/agent/control-store.ts:379, interrupted-outcome retention at :569, append verification at src/core/agent/events.ts:312, and copied-brief/PID/cursor verification in src/core/agent/runs.ts:1128, :1469 and :1688. The matrix therefore contributes real failure-path coverage. [Diagnostic coverage](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview4-1.evidence/coverage-without-matrix.lcov.info).

The key assertion gap is src/tests/cli/agent-control-matrix.test.ts:578: successful post-repair status permits deduplication checks, while :658 and :772 accept generic unverified/unconfirmed errors without requiring a usable recovery route. The SIGKILL recovery check at :757 only examines operations that exist, so R4-RESERVATION's empty operation map escapes it. The relaunch row never retries the interrupted relaunch or dispatches a dependant bound to the prior attempt, missing R4-ARCHIVE; the dispatch row does not model a lost held supervisor, missing R4-DISPATCH.

Confirmed stop containment, native spawn reconciliation, model suitability and scoped acceptance remain gated on unproved native/Harness evidence; wake is absent. Their offline fixture results do not enable those capabilities. Existing producers hold control.lock while allocating publication order; no present producer violates that ordering assumption.

### Verification

- Complete unfiltered suite: 2,018/2,018 tests across 94 files passed, including all 44 matrix tests. [Final gate log](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview4-1.evidence/coverage-final.log).
- Complete coverage gate: exit 0; statements 16,748/16,748, branches 11,610/11,610, functions 3,569/3,569 and lines 14,170/14,170, all 100%, with the repository's existing thresholds and exclusions. [Coverage evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview4-1.evidence/coverage-final.lcov.info).
- Independent recovery probes: all three safety expectations fail and reproduce R4-ARCHIVE, R4-RESERVATION and R4-DISPATCH through the public CLI seam. [Probe source](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview4-1.evidence/review-probes.test.ts), [results](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview4-1.evidence/probes.log).
- Independent host cleanup: 24/24 cases passed on Node v24.22.0 and Bun 1.4.2, covering both locks, SIGINT/SIGTERM/normal exit, owned/changed holder bytes, and the presentation interrupt handler's ordering. Only these probes' own controller children were signalled. [Procedure](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview4-1.evidence/signal-child.ts).
- Pre-stage compatibility: seven golden cases passed against an exported d6df59d9^ baseline, independently checking reconcile for r/inspect/resolve and the four role-free footer tiers; current goldens also pass in the full suite. [Baseline comparison](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview4-1.evidence/baseline-compatibility.log).
- TypeScript typecheck: passed. [Evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview4-1.evidence/types.log).
- Read-only Biome check of changed TypeScript/JSON paths: passed. [Evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview4-1.evidence/biome.log).
- Whole-range whitespace check: passed.
- Scratch setup correction: the initial complete run had two boundary-tooling failures because the private tooling/boundaries dependency copy was missing; copying the locally installed tooling fixed both, and the complete unfiltered rerun above is clean. The deliberate non-matrix coverage diagnostic and initial failure log are retained rather than hidden. [Initial run](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview4-1.evidence/coverage-initial.log), [tooling rerun](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview4-1.evidence/boundaries-rerun.log), [coverage diagnostic](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview4-1.evidence/coverage-without-matrix.log).
- Read-only boundary: the primary checkout remains clean at 6c4d2a1a; no live agent state, credentials, scheduler, environment configuration or remote service was changed or contacted. The owned scratch worktree is removed and the supplied temporary root is empty. [Verification metadata](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview4-1.evidence/review-metadata.json).

## In Progress

Nothing is running.

Outstanding - no action requested now: the supervisor owns correction and independent re-review of the three blocking recovery findings. Build, manual-lint and repository-wide audit claims were not independently rerun in this review; validation is limited to the checks above. Retained evidence is in the run's [evidence directory](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview4-1.evidence).

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 00:24 BST

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [with you] Review the three blocking first-stage recovery findings · supervisor · since 00:24 BST

