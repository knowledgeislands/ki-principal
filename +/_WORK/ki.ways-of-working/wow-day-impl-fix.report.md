# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-impl-fix

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 19:02 BST · last mark 14:35 BST**

---

## Done

- Fixed all seven blocking findings and the small advisories in `166f0cbc` (`fix(agent): preserve control ownership across refusals and recovery`), committed with hooks and 17 explicit paths, then fast-forwarded local `main`. The shared checkout is clean.
- Reviewer 1, blocking 1: unreadable control state fails closed; missing projections cannot discard prior journals, receipts, temporary projections or immutable launch evidence. Regression: `review-1: unreadable control projection fails closed without queue mutation` in [agent-control.test.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts), with missing-evidence and filesystem-race cases in [agent-control-faults.test.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control-faults.test.ts).
- Reviewer 1, blocking 2: held launches revalidate frozen authority, profile evidence and acceptance digests at worker authorisation, before preparation and again before spawn. Regressions: `review-1: held role rechecks %s when its gate opens` and `review-1: held acceptance revalidates record digests after waiting`.
- Reviewer 1, blocking 3: persisted terminal ownership makes different stop requests, receipt replay and event observers derive one stopped event. Regression: `review-1: a different stop request and replay cannot duplicate a terminal event`; older projections also recover terminal ownership from receipts.
- Reviewer 1, blocking 4: event observers use bounded ownership-safe exclusion without age-based takeover. Regression: `review-1: an observer cannot take a live lock after thirty seconds`.
- Reviewer 2, blocking 1: held launch and dispatch loops remain pending through a busy control transaction. Regressions: `review-2: a busy transaction keeps the %s loop pending`, for both hold and dispatch. Spawn authorisation remains serialised as the accepted contract permits.
- Reviewer 2, blocking 2: locks record machine, process birth and token; refusals name an explicit [offline recovery route](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/guides/user/background-agents.md#recover-an-abandoned-lock). It requires verified holder exit or restart, quiescent contenders and preserved evidence before renaming an abandoned lock. Abrupt termination can leave a lock; it is never automatically released while an effect may remain live. Regression: `review-2: leftover locks refuse with a documented offline recovery route and retain evidence`.
- Reviewer 2, blocking 3: known pre-spawn refusals do not claim the entry or journal a spawn; definite preparation failures leave role entries retryable. Regressions: `review-2: a definite role refusal leaves its queue entry queued without a spawn intent` and `a known worktree preparation refusal leaves a role queue retryable without an effect intent`. Unacknowledged supervisors retain their original recovery operation.
- Reviewer 2, advisory 4: unused authority and acceptance declarations are refused. Regression: `review-2: refuses unused declaration %s`.
- Reviewer 2, advisory 5: lower roles cannot acquire pruning or release footers; frozen selections enforce the same ceilings. Regressions: `review-2: %s cannot acquire the release footer` and `frozen lower-role metadata cannot elevate its footer after launch`. Explicitly authorised push remains available where the accepted contract permits it.
- Reviewer 2, advisory 6: uncertain dequeue receipts include the original operation's exact recovery command in JSON and text. Regression: `review-2: uncertain dequeue receipts give the exact frozen recovery operation`.
- Reviewer 2, advisory 7: text launch and queue receipts show effective runtime, model, effort, footer and grants. Regression: `review-2: text launch receipts show explicit effective fields`, plus queue receipt assertions and compatibility goldens.
- Reviewer 2, advisory 8: durable [parent-baseline goldens](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-compatibility.test.ts) cover decision reconciliation for runs `r`, `inspect` and `resolve`, and all four role-free footer tiers. They compare receipts, decision changes, prompts, launch effects and frozen queue values against `d6df59d9^`; the requested additive selection line is checked separately.
- Reviewer 2, advisory 9a: losing the journal between replay and inspection produces a typed refusal. Regression: `recovery inspection refuses a journal lost after replay with a typed result`.
- Reviewer 2, advisory 9b: work identity is read from frontmatter. Regression: `a body id cannot override the work frontmatter identity`.
- Reviewer 3, advisory 1: documented live-while-queued behaviour in the changelog and user guide. Regression coverage: `reports finished, running and exited agents and the queue` and run-listing tests.
- Reviewer 3, advisory 2: documented closed held gates rendering `failed`, with the reason preserved in status and events. Regression: `refuses a gate that cannot open and ends a held agent when its gate closes`.
- Reviewer 3, advisory 3: documented that fenced native spawn failures cannot currently be cleared by assertion or replacement; inspection and owner review preserve the fence. Regression: `surfaces an unexpected launch failure`, plus uncertain receipt and supervisor regressions.
- Reviewer 3, advisory 4: machine-binding refusals name stored and current machines. Regression: `review-3: machine binding refusal names both recorded and current machine`.
- Reviewer 3, advisory 6: one compatibility changelog bullet and the user guide record the role-free behaviour changes; parent-baseline goldens retain the existing decision and footer contracts.
- Blocking reproductions: 15 regression cases failed against unchanged `cb165c20` before the fixes; the two additional compatibility/refusal cases already passed. [Evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-fix.work/evidence/all-blockers-before.log).
- Focused contract gate: 361 tests passed, followed by the final machine-refusal regression passing separately.
- Full suite and coverage gate: 1,780 tests passed across 93 files; statements, branches, functions and lines are all 100%. Thresholds and exclusions are unchanged; no ignore pragma was added. [Verified coverage evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-fix.work/evidence/coverage-verified.log).
- Typecheck: pass.
- Source lint: pass; only the unchanged baseline's informational style suggestion remains.
- Document lint: pass.
- Manual lint: pass.
- Compiled build: pass.
- Compiled root and agent help: pass.
- Decision compatibility comparison against `d6df59d9^`: pass.
- Role-free footer compatibility comparison against `d6df59d9^`: pass; the requested additive selection line is separately asserted and documented.
- Focused offline audits: ki-self, ki-authoring, ki-guides, ki-repo-tools and ki-work-roadmap pass. Ki-engineering is an attributed pass against the unchanged baseline: external boundary dependency link and sandbox-denied installer loopback fixtures, with the existing CI warning.
- Full offline audit: attributed pass; the same DESIGN-2, TEST-5 and SELECT-1 failures and warning families occur on the unchanged baseline. The extra owned staging warning cleared with the commit; the post-commit Git audit passes. Both Capitals were registered only in the fresh copied home. [Attribution](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-fix.work/evidence/full-audit-attribution.json).
- Commit hook: pass, including staged repository audit; post-hook path and byte checks confirm only the 17 intended paths were committed and no verified content changed.
- Native control evidence, model profiles and scoped acceptance remain disabled behind their gates; wake remains outside this stage. No Harness edit, tag, installation, live apply or ki-principal write was made.
- The verified tools-ki fix remains unpublished on `sol.local`, repository `/Users/krisbrown/workspaces/knowledge-islands/tools-ki`, branch `main`, commit `166f0cbc`: the own-commits-only publishing prerequisite is not satisfied, so no push was attempted.

## In Progress

Nothing is running. The fix is integrated locally and ready for independent re-review; publication needs the supervisor's disposition below. The owned worktree and branch are retained under the task's no-deletion rule, with no intended uncommitted edits. Reviewer 3's advisory 5 requires no change: legacy queue normalisation remains lossless.

## Queries

### PUBLISH-OWN-FIX

**Context:** The verified fix is on clean local `main` on `sol.local`. After the final fetch, publishing it would include commits outside this run's own unit. The task expressly forbids that wider push.

**Query:** How should the verified fix be published under the own-commits-only restriction?

**Options:**

a) (recommended, confidence high - preserves the granted boundary) Supervisor settles the publication prerequisite, then commissions the fix's own-only fast-forward push.

b) Give explicit authority for a reviewed wider fast-forward range.

### 🤖 → 👤 Handoff to supervisor · blocked · since 19:02 BST

🤖 0 running · 👤 1 you · ⛔ 1 blocked

- [blocked] Publish the verified tools-ki fix within the granted boundary · supervisor · since 19:02 BST
