# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-impl-rereview3-1

**🤖 → 👤 Handoff to supervisor · Run report at 20:54 BST · last mark 19:18 BST**

---

## Done

Verdict: CHANGES NEEDED

1. **Blocking B1 — A failed event write permanently loses some blocked notifications.** [controls.ts:55](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/controls.ts:55) suppresses publication failures after an observed outcome, but [events.ts:549](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:549) reconstructs only launch, held, stopped and dequeued events; denying pending writes after SIGTERM leaves confirmed `stop-timeout` and `ownership-unverified` receipts with no required `blocked` event, even after restored access, repeated status observations and identical request retries.
2. **Blocking B2 — Truncated history silently resets event identities and loses evidence.** [events.ts:116](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:116) checks surviving evidence only when the journal is absent, while [events.ts:176](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:176) assigns sequences from its current length; truncating an existing journal to empty or its valid first line makes status succeed, replaces original sequences 1–3 with launch/stopped sequences 1–2, loses stop-requested, leaves the consumed cursor at 3 and makes the next waiter return `ALL FINISHED`.

Each earlier blocking finding was checked independently against the final source and its passing CLI regressions:

- Initial review 1/B1 — **FIXED:** [control-store.ts:73](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/control-store.ts:73) distinguishes ENOENT from read failures and [control-store.ts:215](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/control-store.ts:215) refuses missing projections beside prior evidence; the read-denial and missing-projection regressions pass.
- Initial review 1/B2 — **FIXED:** [runs.ts:419](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:419) revalidates frozen evidence before and after worktree preparation immediately before spawn; held authority, model-evidence withdrawal and acceptance-digest regressions pass.
- Initial review 1/B3 — **FIXED:** [controls.ts:264](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/controls.ts:264) persists the terminal stop owner and [events.ts:574](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:574) derives only that owner's stopped event; interrupted-operation, different-request and replay regressions pass.
- Initial review 1/B4 — **FIXED:** [locking.ts:26](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/locking.ts:26) uses exclusive creation without age or PID takeover; the concurrent live-holder regression passes.
- Initial review 2/B1 — **FIXED:** [control-store.ts:382](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/control-store.ts:382), [runs.ts:917](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:917) and [runs.ts:1399](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:1399) keep launch, queue, hold and dispatch pending through contention, with a 120-second refusal boundary; busy-holder and deadline regressions pass.
- Initial review 2/B2 and first re-review 2/B2 — **FIXED:** [locking.ts:44](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/locking.ts:44) releases matching lock bytes, [processes.ts:111](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/processes.ts:111) wires host exit/signal cleanup, and the [manual recovery route](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/guides/user/background-agents.md:94) requires positive holder-exit evidence, quiescent contenders and preservation by rename; CLI regressions and twelve independent real-process cases pass.
- Initial review 2/B3 — **FIXED:** [runs.ts:876](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:876) preserves retryable queue entries when no spawn intent exists, and dispatch performs preflight before launch; role-refusal and worktree-preparation regressions pass without worker effects.
- First re-review 1, event-evidence blocker — **FIXED for its reported cases:** [events.ts:92](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:92) refuses denied reads and [events.ts:413](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:413) reconstructs a missing snapshot from the journal; denied journal/snapshot reads and missing-snapshot terminal regressions pass, while B1–B2 above refute the broader durability claim.
- First re-review 2/B1 — **FIXED:** [events.ts:194](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:194) preserves pending launch evidence and [runs.ts:865](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:865) returns an acknowledged start with an inspection warning; direct, held and dispatched start/publication-failure regressions pass without failed-launch events or duplicate workers.
- Second re-review 1/B1 — **FIXED for missing journals:** [events.ts:113](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:113) refuses ENOENT beside history markers, snapshots, advanced cursors or prior control operations; surviving-evidence regressions pass, but B2 above covers the still-accepted truncated-file variant.
- Second re-review 1/B2 — **FIXED:** [events.ts:323](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:323) restores source status identity independently of terminal identity; missing-snapshot failed-status and predecessor/successor regressions pass without duplicate terminal events.
- Second re-review 1/B3 — **FIXED:** [runs.ts:480](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:480) records the acknowledgement before fallible persistence and [runs.ts:865](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:865) preserves the started result; packet-path, PID-write, projection-write and lock-release failure regressions pass.
- Second re-review 1/B4 — **FIXED:** [runs.ts:1155](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:1155) bounds watch/wait event-lock contention and preserves holder/recovery details; both abandoned-lock observer regressions pass.
- Second re-review 2/B1 — **FIXED:** [events.ts:506](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:506) marks worker blocked/failed status lines as nonterminal, allowing a later exit or DONE event; both progress-to-terminal cases pass.
- Second re-review 2/B2 — **FIXED:** [runs.ts:210](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:210) keeps an unavailable held supervisor visibly unconfirmed and [events.ts:481](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:481) suppresses false worker failure; the held-lock-expiry and dependent-gate regression passes.
- Second re-review 2/B3 and second re-review 3/B1 — **FIXED for busy event locks:** [controls.ts:54](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/controls.ts:54) permits an unpublished sequence while retaining the control receipt; busy stop, dequeue and blocked-outcome cases publish once after exclusion clears, although B1 above exposes missing reconciliation after a failed pending write.
- Second re-review 3/B2 — **FIXED:** [events.ts:329](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:329) recognises dequeue as terminal and [events.ts:477](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:477) suppresses a cancelled held attempt's later failure; the dequeue/held-worker regression passes without another terminal notification.

Initial review 3 and first re-review 3 recorded no additional blocking findings.

Range review: inspected d6df59d9, cb165c20, 166f0cbc, 7eb0f017 and 6c498f3a, including the full delta from d6df59d9^, against the [accepted contract snapshot](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview3-1.evidence/accepted-contract.md); immutable identities, containment refusal, cancellation fences, evidence-gated spawn recovery, dependency binding, dormant roles and separate recover/reconcile namespaces remain present, but B1–B2 prevent first-stage acceptance.

Offline suite and coverage: 1,872 tests across 92 files pass with all four 100% thresholds on the archived final source; ten HTTP installer tests were excluded under the no-network instruction, so this is not an unfiltered full-suite result.

Baseline compatibility: seven cases independently pass on the d6df59d9^ archive, covering decision reconciliation for ordinary/inspect/resolve run names and all four role-free footer tiers; the final suite passes the same golden cases.

Independent CLI probes: four expected contract assertions fail, reproducing B1 for timeout and ownership loss and B2 for empty and valid-prefix truncation; supplied regressions exercise denied stopped-event publication and absent journals, without covering these combinations.

Real-process signal verification: all twelve control/events-lock cases pass for SIGINT, SIGTERM and normal exit with owned or replaced tokens, using isolated helpers that launch no agent or native session.

Typecheck, read-only Biome over 23 changed files and complete-range whitespace check: pass on the archived product tree.

Source isolation: all 502 tracked blobs in the scratch product match 6c498f3a, the primary checkout remains clean at that revision, and no existing repository files or other live runs were changed.

Verification caveat: the first coverage invocation lacked copied boundary-tool dependencies and triggered automatic mise runtime setup in scratch XDG storage; I cannot certify that invocation made no network call, and the successful final run used local dependency copies, absolute installed binaries and offline mode.

## In Progress

Nothing is running.

Outstanding - no action requested now: the supervisor owns routing B1–B2 for repair and another independent review; this run changes or accepts no implementation.

Verification limitations: repository-wide governance audits and HTTP installer fixtures were not run; no native containment, token-based spawn recovery, model suitability, scoped acceptance capability or wake delivery was enabled or claimed.

Retained material: [evidence manifest](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview3-1.evidence/manifest.json), [CLI probes](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview3-1.evidence/review-probes.test.ts:226), [structured observations](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview3-1.evidence/probe-observations.json), [coverage log](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview3-1.evidence/coverage-final.log) and [native signal results](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-rereview3-1.evidence/native/results.json); temporary scratch material has been removed after preservation.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 20:54 BST

🤖 0 running · 👤 1 you · ⛔ 0 blocked

- [with you] Two blocking event-evidence findings from the independent first-stage re-review · supervisor · since 20:54 BST
