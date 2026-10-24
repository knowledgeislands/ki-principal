# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-impl-rereview-1

**🤖 → 👤 Handoff to supervisor · Run report at 19:11 BST · last mark 14:35 BST**

---

## Done

Verdict: CHANGES NEEDED

1. Reviewer 1, blocking 1 - FIXED: unreadable control projections refuse without changing queue or history; missing projections beside prior evidence cannot initialise a fresh store. The [read-denial regression](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:2542) fails on `cb165c20` and passes on `166f0cbc`; the additional missing-evidence regressions also pass.
2. Reviewer 1, blocking 2 - FIXED: held launches revalidate frozen authority, model evidence and acceptance evidence immediately before worker launch, including after worktree preparation. The [authority/evidence regressions](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:2572) and [acceptance-digest regression](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:2813) fail before the fix and pass afterwards, with no extra worker launch.
3. Reviewer 1, blocking 3 - FIXED for the reported interrupted-request failure: the persisted terminal owner prevents other stop requests or their retries from deriving another stopped event. The [different-request/replay regression](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:2594) fails before the fix and passes afterwards; the separate event-evidence failure below remains blocking.
4. Reviewer 1, blocking 4 - FIXED: event publication uses ownership-safe exclusion without age or PID takeover. The [concurrent-observer regression](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:2668) reproduces takeover after 31 seconds before the fix; afterwards the contender refuses and exactly one completion event remains.
5. Reviewer 2, blocking 1 - FIXED: held launch and dispatch loops retry busy control transactions instead of exiting. Both [busy-loop regressions](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:2714) fail before the fix and pass afterwards, retaining their pending work until the holder releases exclusion.
6. Reviewer 2, blocking 2 - FIXED through an explicit offline recovery procedure: locks retain machine, birth identity and token; the refusal names a [documented recovery route](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/guides/user/background-agents.md:72) requiring positive holder-exit or restart evidence, quiescent contenders and preservation by rename. The [abandoned-lock regression](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:2749) fails before the fix and passes afterwards. Abrupt termination deliberately retains exclusion; the test simulates the owner's verified recovery rather than proving operating-system exit evidence.
7. Reviewer 2, blocking 3 - FIXED: definite refusals occur before the spawn claim and intent; definite preparation failures leave the entry queued and retryable. The [original refusal regression](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:2628) fails before the fix and passes afterwards; the [worktree-preparation regression](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:2866) also passes without a launch or spawn intent.
8. NEW - BLOCKING: [events.ts:64](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:64) and [events.ts:204](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:204) still use the [catch-all reader](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/context.ts:53), treating unreadable event evidence as absent. On `166f0cbc`, making only `events.jsonl` write-only after a confirmed stop makes the next public status command exit 0 and append a second stopped event for the same attempt and operation, restarting its sequence at 1 after the original sequence 3. Making only `events.state.json` write-only similarly duplicates a natural done event with exit 0. Preserving that snapshot by rename, simulating its loss between journal append and snapshot persistence, also increases the same attempt's done events from one to two. This breaches the contract's no-silent-fallback and no-duplicate-terminal-event guarantees, despite the corrected lock and stop-operation ownership. Fix: distinguish absence from permission/I/O failures in both event readers and refuse before mutation on uncertainty; recover a genuinely missing snapshot from the authoritative event journal, or otherwise deduplicate terminal derivation by immutable attempt and terminal identity. Add CLI regressions for all three cases, asserting unchanged journal/cursors on read denial and one terminal event after snapshot loss. [Executable probes](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview-1.evidence/fixed/src/tests/cli/agent-rereview-probe.test.ts:283), [journal-denial evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview-1.evidence/event-journal-read-denial.json), [snapshot-denial evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview-1.evidence/event-snapshot-read-denial.json) and [missing-snapshot evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview-1.evidence/event-missing-snapshot.json) retain the reproduction.

Reviewed the [accepted contract](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/agent-control-contract.md), all three first-round reports ([1](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-review-1.report.md), [2](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-review-2.report.md), [3](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-review-3.report.md)), the [fix report](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-fix.report.md) and the complete `d6df59d9^..166f0cbc` range, including `d6df59d9`, `cb165c20` and `166f0cbc`.

Original-blocker reproductions: every reported blocking failure has a discriminating regression that fails on the pre-fix revision; the corresponding fixed-revision tests pass. [Before-fix results](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview-1.evidence/before-fix.log) and [additional before-fix results](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview-1.evidence/before-fix-two.log).

Focused agent verification: 362 tests pass across five files on the fixed revision. [Results](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview-1.evidence/focused.log).

Compatibility verification: all seven golden cases pass independently on both `d6df59d9^` and `166f0cbc`, covering ordinary decision reconciliation, runs named inspect and resolve, and all four role-free footer tiers with explicit runtime/model/effort/grants. The documented additive selection line is normalised for the baseline comparison. [Parent results](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview-1.evidence/parent-compatibility.log).

Broader offline verification: 1,770 tests pass across 92 files; networked installer fixtures were excluded. Typecheck and range whitespace checks pass. [Suite results](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview-1.evidence/suite.log).

Capability review: native containment and recovery remain unsupported, role profiles remain dormant, acceptance remains gated on combined Harness verification, and wake is absent. Fixture success is not native evidence; no silent provider or model fallback was enabled.

Read-only boundary exception: the scratch dependency symlink exposed the repository's ignored Vitest results cache, which was updated during earlier test runs. No tracked repository file changed. The final probes used a scratch cache directory with caching disabled. No tracked edit, live adapter operation, install or remote call was performed; existing cache bytes were not restored or deleted.

## In Progress

Nothing running.

Outstanding - no action requested now: the supervisor owns routing the new event-evidence blocker and commissioning its fix and independent re-review; first-stage acceptance remains withheld.

Verification limitations: this run did not repeat coverage or repository-wide audits, and excluded networked installer tests. All process behaviour used injected offline ports. Retained scratch copies and observations are in the [evidence directory](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview-1.evidence); the temporary run directory is empty.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 19:11 BST

🤖 0 running · 👤 1 you · ⛔ 0 blocked

- [with you] First-stage re-review and the event-evidence blocker · supervisor · since 19:11 BST
