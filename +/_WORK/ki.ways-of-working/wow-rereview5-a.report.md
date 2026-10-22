# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rereview5-a

**🤖 → 👤 Handoff to supervisor · Run report at 08:56 BST · last mark 08:24 BST**

---

## Done

VERDICT: REFUSE · confidence high · Legacy failure progress can consume a later completion during upgrade, suppressing its event and report homing.

**F1 — Repair legacy progress replay before admission.** [terminalEvent and publicationSeen](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/core/agent/events.ts:498) treat every older `failed` event without explicit terminal metadata as an attempt ending; [snapshot replay](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/core/agent/events.ts:595) carries that ending forward. This leaves an inherited v1-state defect unresolved by the new terminal-identity contract. I reproduced it through the public CLI using history produced by an untouched temporary export of `51725e8b`: launch a live legacy worker, observe an arbitrary `failed:` progress line once, upgrade to `a9aba774`, then write its report and `DONE`. With either the original snapshot or no snapshot, status succeeds but publishes no completion, does not home the report, and the next waiter returns `ALL FINISHED` after the earlier events are acknowledged.

**Exact change needed:** classify legacy failure records from proven terminal forms and available status/control evidence before trusting or checkpointing `Seen.ended`; preserve arbitrary worker failure progress as nonterminal, and refuse ambiguous legacy evidence with recovery guidance. Extend the [older-journal CLI regressions](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/tests/cli/agent-control.test.ts:4518) to run this baseline-to-candidate transition with and without a snapshot and require exactly one completion, one report homing and a completion notification to the waiter. Preserve genuine terminal failures and retired-report protection.

- Reviewed commits: `805e4d36`, `b2d8e795`, `4cd0ab87`, `b3fec501`, `a9aba774`, against `51725e8b`; no repository changes or commits made.
- Independent upgrade probes: FAIL in both failure-progress cases; two blocked-progress controls safely completed or refused with recovery guidance.
- Rebase comparison: PASS; the report-homing conflict retains both permission and first-end guards, and the third fix matches its original patch.
- Renamed-folder fixture review: PASS; it tests a legitimate first completion after rename while retaining authoritative history.
- Depcruise migration review: PASS; manifest and lockfile bytes are unchanged, and no old tooling path remains in the candidate sources.
- Offline frozen installs: PASS in disposable manifest copies; lifecycle scripts were skipped, and the reviewed worktree was untouched.
- Full unfiltered coverage invocation: FAIL; all 2,049 tests ran across 95 files, with 2,040 passed and nine sandbox-constrained failures.
- Full-run limitations: one fallback test requires a forbidden `/tmp` write; eight installer tests encountered forbidden shell temporary output or loopback fixtures, with nine unhandled loopback-listen denials.
- Durable I/O matrix: PASS; 26 flows, 655 mutation sites and 4,674 fault cells.
- Controller SIGKILL matrix: PASS; 26 flows, 651 mutation sites and 1,302 before/after cells; all 52 matrix tests passed.
- Dependency-boundary, worktree-provisioning and hook suites: PASS, respectively two, nine and 56 tests.
- Coverage: NOT ESTABLISHED; the failed constrained run emitted no LCOV; thresholds and exclusions remain byte-identical to `51725e8b`.
- TypeScript: PASS.
- Biome: PASS.
- Manifest formatting: PASS.
- Markdown: PASS.
- Manual lint: PASS.
- Command inventory: PASS.
- Compiled build: PASS; output stayed in the assigned temporary directory.
- Compiled CLI smoke checks: PASS; seven version, help, recovery and reconciliation checks.
- Isolated native audit: FAIL only at `TEST-5`, reusing this review's full coverage invocation; 17 skill passes, four skill warnings, one skill failure and eight warning findings.
- Read-only boundary: PASS; verification denied network access and repository writes, and the candidate remains clean at `a9aba774bb198b25773f7d4e93cc932052daf3f4`.

## In Progress

Nothing is running.

Outstanding - no action requested now: the supervisor retains the candidate branch and worktree. Admission needs F1 repaired and fresh successful full-suite and coverage evidence under explicitly permitted test-fixture boundaries; this review makes no green-coverage claim.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 08:56 BST

🤖 0 running · 👤 1 you

- [with you] Resolve F1 and obtain fresh admission evidence · supervisor · since 08:56 BST
