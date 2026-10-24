# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-impl-fix-3

**🤖 → 👤 Handoff to supervisor · Run report at 20:45 BST · last mark 19:18 BST**

---

## Done

- Codex B1: initialise history before effects; refuse a missing journal beside history markers, snapshots, advanced cursors or operation evidence. Fix: [events.ts:113](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:113); regressions: [missing journal](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:3348), [surviving evidence](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:3688). Denied ordinary run reads also refuse: [context.ts:53](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/context.ts:53), [denied reads](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:3552).
- Codex B2 and Opus blocking 1: retain source-line and terminal identities independently, so status messages preserve their eventual finish and recovery emits it once. Fix: [events.ts:323](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:323); regressions: [snapshot recovery](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:3361), [both status forms](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:3373). Per-attempt snapshots also protect overlapping predecessors and successors: [events.ts:50](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:50), [overlapping attempts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:3842).
- Codex B3: preserve acknowledged worker and supervisor starts through subsequent persistence failures, returning the known result with an inspection warning. Fix: [runs.ts:790](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:790); regressions: [packet failure](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:3403), [persistence boundaries](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control-faults.test.ts:195), [held transitions](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:3626).
- Codex B4 and Opus advisory 4: bound busy event waits at 120 seconds, preserving the holder identity and recovery route in the refusal. Fix: [runs.ts:1155](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:1155); shared watch/wait regressions: [bounded observers](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:3425).
- Opus blocking 2: an expired supervisor wait leaves its attempt visibly held and unconfirmed, without a false worker failure or closed dependency gate. Fix: [runs.ts:216](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:216); regression: [held lock expiry](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:3507).
- Opus blocking 3 and Fable blocking 1 are the same defect: pending publication now permits an absent event sequence while retaining the durable control receipt. Fix: [controls.ts:54](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/controls.ts:54); shared stop, dequeue and blocked-outcome regressions: [pending receipts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:3452); post-effect denial: [confirmed stop](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:3588).
- Fable blocking 2 and Opus advisory 6: dequeue ends only its own attempt and never produces a later worker-failed notification. Fix: [events.ts:323](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:323); regression: [dequeue replay](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:3482).
- Other advisories addressed: pending creation order is durable ([fix](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:222), [regression](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:3529)); legacy queue retries retain confirmed or unresolved spawn evidence, including verified recovery ([fix](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:978), [fault regressions](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control-faults.test.ts:216), [recovery regressions](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:3792)); dispatch handles its known result before fallible reloads; lock release preserves the original action refusal ([fix](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/locking.ts:59), [regression](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:3572)).
- Residual Fable advisory 3: before a confirmed start, an unreadable control store can supersede the original preparation error. This diagnostic precedence is retained deliberately because unverifiable state must control the refusal; confirmed starts are handled before reloading, and the absent-store dereference is removed.
- Native signal evidence: 16 isolated Bun 1.4.2 probes passed across both locks, SIGINT/SIGTERM/normal exit, unchanged/replaced tokens and display cleanup; [results](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-fix-3.evidence/signal-probes-final.json).
- Regression proof: all 23 initial checks and four additional queue/snapshot checks fail on unchanged `7eb0f017`; [initial evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-fix-3.evidence/before-final-regressions.log), [additional evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-fix-3.evidence/before-added-properties.log).
- Local main: `6c498f3a` in `tools-ki` on `sol.local`; fast-forward integration, clean primary checkout, explicit-path commit and post-hook contents verified.
- Lint: passed.
- Types: passed.
- Tests: 1,882 passed across 93 files.
- Coverage: 100% statements (16,486/16,486), branches (11,299/11,299), functions (3,537/3,537) and lines (13,949/13,949); thresholds and exclusions unchanged.
- Build and compiled help/version smoke checks: passed.
- Manifest and manifest formatting: passed.
- Markdown: passed.
- Command inventory and manual lint: passed.
- Isolated offline audit: passed, 19 PASS / 3 WARN / 0 FAIL; existing CI-pin, unavailable mGit-overview and undeclared-maturity warnings only.

## In Progress

Supervisor: arrange three fresh independent re-reviews of `6c498f3a`, then acceptance before publication. Record the 20:05 decision after the ki-principal rebase. The accepted contract was recovered from committed revision `03954f4c` while its checkout copy was absent.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 20:45 BST

🤖 0 running · 👤 1 you · ⛔ 0 blocked

- [with you] Third fix round delivered on local main; fresh independent review · supervisor · since 20:45 BST
