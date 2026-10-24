# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-impl-fix-2

**🤖 → 👤 Handoff to supervisor · Run report at 19:43 BST · last mark 19:18 BST**

---

## Done

Local main commit: `7eb0f017b9d50fff9a16a9b206dfdd714782f192` (`fix(agent): preserve event evidence and truthful start outcomes`) in tools-ki on sol.local; verified fast-forward from `166f0cbc`, with only nine intended paths committed and the delivery worktree and branch retired.

- Re-review 1, blocking finding 8: only ENOENT counts as absent event evidence; read, parse and shape failures refuse with the documented recovery route before changing the journal or waiter cursor. Missing and stale snapshots recover terminal and query identities from the journal. Fix: [events.ts:78](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:78), [events.ts:335](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:335); recovery guide: [background-agents.md:72](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/guides/user/background-agents.md:72). Regressions: `rereview-1: unreadable %s preserves event evidence and cursors`, `rereview-1: corrupt %s refuses with recovery before mutation`, `rereview-1: missing snapshot replays the journal without duplicate terminal events`, and `missing snapshot reconstructs outstanding query identities without duplication`, starting at [agent-control.test.ts:2917](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:2917).
- Re-review 2, blocking finding 1: publication first records an immutable pending event; busy publication leaves the worker truthfully started, and the next observer reconciles it once. Confirmed control receipts reconstruct a launch if even the pending write failed. Launch and held notifications deduplicate by attempt across late publication, and dispatch never cancels an already-started entry or infers failure across a spawn intent. Fix: [events.ts:149](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:149), [events.ts:195](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:195), [events.ts:459](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:459), [runs.ts:1400](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:1400). Regressions: `rereview-2: busy event publication after %s preserves a started worker` for launch, hold and dispatch at [agent-control.test.ts:2969](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:2969); `rereview-2: a failed pending write still reports %s start and reconstructs its event`; `rereview-1: duplicate operation publications and interrupted temporary records reconcile once`; and `a post-start queue projection failure never cancels a started entry` at [agent-control-faults.test.ts:125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control-faults.test.ts:125).
- Re-review 2, blocking finding 2, and re-review 3, advisory 1: both locks register synchronous cleanup for SIGINT, SIGTERM and normal exit; acquisition and registration have no asynchronous gap. Release checks the unchanged holder bytes and token, and preserves another holder or unverifiable evidence. Crashed holders retain the documented offline recovery route, with no age or PID takeover. Fix: [locking.ts:14](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/locking.ts:14), [processes.ts:111](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/processes.ts:111). Regressions: `rereview-2: interrupt and normal exit release only the held %s lock` at [agent-control.test.ts:3015](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:3015), and `rereview-2: %s cleanup preserves a changed holder token`, each covering control and events locks.
- Re-review 2, advisory 3, and re-review 3, advisories 2–3: foreground launch and queue share the control wait with hold and dispatch; the 120-second bound gives a visible refusal naming the holder and recovery route. Fix: [control-store.ts:382](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/control-store.ts:382), [locking.ts:38](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/locking.ts:38). Regressions: `advisory: foreground %s waits for a busy control transaction` at [agent-control.test.ts:3065](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:3065), and `advisory: a bounded control wait names the holder and recovery route` at [agent-control.test.ts:3153](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:3153).
- Re-review 3, advisory 4: long-running watch and wait retry a busy event transaction; single-shot status retains a bounded refusal. Fix: [runs.ts:1076](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:1076). Regression: `advisory: %s stays pending on a busy event transaction` at [agent-control.test.ts:3133](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:3133).
- Advisory disposition: all new re-review advisories are addressed; none is deferred. The original seven fixes and prior compatibility protections remain covered.
- Before-fix evidence: the unchanged baseline passes 1,780 tests; 38 of the 43 added cases fail on `166f0cbc`, while five already-pass safety or edge cases remain covered.
- Full tests: 1,823 tests across 93 files pass through the required coverage gate.
- Coverage: statements 16,408/16,408; branches 11,187/11,187; functions 3,521/3,521; lines 13,869/13,869 — all 100%, with thresholds and exclusions unchanged and no new ignore pragma.
- Source lint: pass.
- Typecheck: pass.
- Manifest formatting: pass.
- Markdown check: pass.
- Manual lint: pass.
- Generated command inventory: pass.
- Build and compiled root, agent and recovery help/version checks: pass.
- Full isolated offline repository audit: pass, 19 PASS / 3 WARN / 0 FAIL; warnings are the existing CI pin, unavailable mGit overview in the isolated home, and undeclared maturity.
- Commit hooks and post-hook inspection: pass; all nine committed paths and their bytes match the verified delivery.
- Retained verification material: [evidence directory](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-fix-2.evidence).

## In Progress

Nothing running.

Outstanding — no action requested now: the supervisor owns fresh independent re-review before acceptance or publication. This run used offline process fixtures; host signal registration was reviewed and its cleanup was exercised through the injected exit port. No live worker, native containment, wake or model-suitability claim was introduced.

Verification boundary exception: early probes used shared dependency links and refreshed the primary checkout's ignored Vitest results cache. Final gates used private dependency copies. No tracked primary file was edited before the authorised fast-forward; the ignored cache was left in place rather than attempting to restore unknown prior bytes.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 19:43 BST

🤖 0 running · 👤 1 you · ⛔ 0 blocked

- [with you] Second fix round delivered on local main; fresh independent re-review · supervisor · since 19:43 BST
