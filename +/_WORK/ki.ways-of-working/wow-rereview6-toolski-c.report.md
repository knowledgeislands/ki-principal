# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rereview6-toolski-c

**🤖 → 👤 Handoff to supervisor · Run report at 11:22 BST · last mark 11:22 BST**

---

## Done

VERDICT: ACCEPT · confidence medium - the five commits through a7c80cd8 pass every gate and the pinned v0.12.0 audit, resolve all earlier findings, and the real agent state replays without a new refusal; two non-blocking legacy-classifier gaps remain and should be fixed before the release step.

Range reviewed: `51725e8b..219968a0` in the worktree `wow-toolski-integrate`; admission candidate `a7c80cd830d9c1e0e05f75d4f8414909d1c20e90` (805e4d36, b2d8e795, 4cd0ab87, b3fec501, a7c80cd8), with 219968a0 (depcruise migration) held back as the fix report proposes.

Checks, one line each:

- Rebase fidelity: 805e4d36 and b2d8e795 are content-identical rebases of 6c498f3a and 6c4d2a1a on primary `main`, apart from a Co-authored-by trailer and the one-line resolution `done && homeReports && !seen.ended`. PASS
- Full gates on a7c80cd8 (scratch clone, in-place): TypeScript PASS, Biome PASS (one pre-existing info-level note), build PASS (version 0.13.0), Vitest with coverage PASS (95 files, 2,081 tests, 100% statements, branches, functions and lines; no threshold error; the fix report's 2,078 count is now 2,081).
- Test integrity: no `skip`, `only`, `todo`, `skipIf` or coverage exclusions in `src/tests` at 51725e8b or a7c80cd8; the Vitest include/exclude and 100% thresholds are unchanged; the legacy-upgrade regressions build the baseline CLI from `git archive 51725e8b` and run it for real. PASS
- Pinned audit as CI runs it: released ki v0.12.0 installed offline, `ki bootstrap`, `registry add`, `repo repair`, then `KI_REPO_OFFLINE=1 ki repo audit --repo .` on a7c80cd8. PASS for the commit: the one FAIL in the full run (FILES-2, repository identity) came from the scratch clone's local origin URL; with the GitHub origin set the ki-repo skill reports FAIL=0, and ki-engineering (which runs Vitest coverage, Biome and TypeScript under the pinned harness) reported FAIL=0 in the full run. Remaining WARNs are environmental or pre-existing (no capital checkout, hooksPath unset, inline KI_VERSION, trades hold date) and do not fail CI.
- Legacy replay correctness: a legacy `failed` progress event never consumes a later completion; progress is only inferred from a matching `failed:` status line in the snapshot or current status, terminal only from a confirmed receipt or the fixed baseline texts, anything else refuses before the checkpoint is adopted. Verified by reading `src/core/agent/events.ts:571-605` and by the regressions at `src/tests/cli/agent-control.test.ts:4699+`. PASS
- Real state scan (read-only copy of `~/.local/state/ki/agents`): 51 legacy `failed` events classify as 47 terminal, 4 progress, 0 ambiguous; no legacy `could not launch:` failed event exists on this machine. PASS
- Whole-state simulation: a7c80cd8 and primary `main` (6c4d2a1a) observed every run over identical copies of the real state with identical exit codes, and appended the same set of events to every journal (order differs only where two agents ended in the same pass). The single refusal (`mac-studio-setup`, "journal has lost an observed terminal outcome") is pre-existing and identical on both builds. PASS, no regression
- Git topology for the plan: primary `main` is 6c4d2a1a (two ahead of origin/main 51725e8b, one behind), its tree is clean, `main` is checked out only there, and a7c80cd8 is a descendant of origin/main but not of 6c4d2a1a. The guarded compare-and-swap is the right instrument. PASS

### Findings

1. `src/core/agent/events.ts:571` (not blocking). `legacyTerminalFailure` accepts only `no report`, `attempt failed` and `exited without DONE (…)`, but baseline 51725e8b also wrote operation-less `failed` events with text `could not launch: <reason>` from the queue drop at `src/core/agent/runs.ts:1418` (baseline numbering). After upgrade a run holding such an event refuses with "ambiguous legacy failure" and the documented recovery (`docs/guides/user/background-agents.md:86`) offers no route. Reproduced with a scratch test against a7c80cd8. Fix: add `text.startsWith('could not launch:')` to `legacyTerminalFailure` with a regression, mirroring the treatment at line 613. None exist on this machine, so admission is safe; fix before release step 3.
2. `src/core/agent/events.ts:597-603` (not blocking). A worker that wrote a `failed:` status line and then kept writing status lines before the upgrade has no matching snapshot or current-status evidence, so observation refuses with and without a snapshot, and the guidance's "preserve status, snapshot and control evidence" cannot resolve it. Reproduced with a scratch test. Suggested fix: treat arbitrary-text operation-less legacy failures followed by a later event of the same attempt as progress, or document a safe manual recovery.
3. Commit trailers (cosmetic, not blocking). a7c80cd8 carries `Co-authored-by: Codex (GPT-6)`, b3fec501 and 219968a0 `GPT-6`; author identity is `krisbrown@sol.local` on all six. Unchanged from round 5c's note.

### Earlier findings

- 5a F1 (legacy `failed` progress event consumed a later completion): resolved by a7c80cd8's classification before replay; regression present and run.
- 5b F1 (CI's pinned v0.12.0 audit fails on the depcruise migration): resolved by holding 219968a0 back; a7c80cd8 still references `tooling/boundaries` in `package.json`, `release.yml` and CI.
- 5b F2 (candidate not a fast-forward of primary `main`): addressed by plan step 2, the guarded compare-and-swap from 6c4d2a1a.
- 5b F3 (depcruise `node_modules` layout): moot through a7c80cd8; returns with plan step 4.
- 5b F4 and 5c trailer/author notes: still cosmetic, see finding 3.

### Admission plan

The fix report's four steps are sound: (1) admit through a7c80cd8, (2) compare-and-swap primary `main` from 6c4d2a1a to a7c80cd8 with the two superseded commits retained only as rebased equivalents, (3) release v0.13.0 pinned to harness 52779419, (4) land 219968a0 only after a tools-ki release whose harness pin includes db5e3cff, which is on harness `main` but in no released pin yet. After step 2 primary `main` is a fast-forward of origin/main. Recommend fixing finding 1 (and deciding finding 2) before step 3, since the release is what exposes other machines' legacy journals to the classifier.

Scratch work under `/private/tmp/wow-rereview6-c` removed; no repository, ref, environment or remote was touched.

## In Progress

Nothing.

## Queries

Context: Finding 1 is a real refusal for any machine holding a legacy queue-drop failure, but none exist here and it does not affect the admission itself.
Query: Fix finding 1 before release step 3, or release as is?
Options:
a) (recommended, confidence high - one-line classifier change with a regression, and release is the exposure point) fix finding 1 on a follow-up commit before step 3.
b) Release v0.13.0 as is and fix in a patch release.

Context: Finding 2 needs a design choice between widening the progress inference and documenting a manual recovery.
Query: Which route for finding 2?
Options:
a) (recommended, confidence medium - the status form is the only source of arbitrary-text operation-less failures across all releases) classify them as progress when a later same-attempt event exists.
b) Document a manual recovery in the background-agents guide and leave the classifier strict.

### 🤖 → 👤 Handoff to supervisor · since 11:22 BST

🤖 0 running · 👤 1 you

- [awaiting-decision] admit through a7c80cd8 and run the four-step plan, with the two queries above · you · since 11:22 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
