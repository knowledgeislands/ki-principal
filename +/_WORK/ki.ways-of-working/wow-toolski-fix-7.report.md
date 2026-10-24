# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-toolski-fix-7

**🤖 → 👤 Handoff to supervisor · Run report at 13:09 BST · last mark 08:24 BST**

---

## Done

Resolved the sixth-round findings in two new commits after `a7c80cd8`. The five existing fix commits are unchanged. Candidate branch: `wow-toolski-integrate` on `sol.local`, in the supplied worktree.

- **A1, including the blocked-prefix case, and B5:** [legacy replay](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/core/agent/events.ts:571) now distinguishes worker progress from terminal failure and blocked outcomes before adoption. Matching status identity and later same-attempt events preserve progress; launcher-like wording without corroboration refuses with recovery guidance instead of consuming completion. Both classifications survive snapshot loss in the verified checkpoint. Regressions run untouched `51725e8b` through 28 status/snapshot combinations and five missing-evidence/recovery cases, requiring one completion, waiter notification and report homing. Existing synthetic terminal fixtures now include corroborating control outcomes while retaining their assertions.
- **C2 and B1:** arbitrary legacy failure progress survives overwritten status and a failed worker's relaunch. Wording is classified by event kind, so failure text mentioning a gate and blocked text resembling a failure remain progress. [Baseline regressions](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/tests/cli/agent-control.test.ts:4833) reproduce exit/relaunch with both snapshot variants, plus five cases where status changes before observation. The reported whole-run refusal was real and is fixed.
- **C1 and B2:** legacy `could not launch:` outcomes use the matching attempt's recorded queue cancellation or confirmed terminal evidence. The [untouched-baseline queue regression](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/tests/cli/agent-control.test.ts:4857) and six cancellation checks cover successful replay and refusal for mismatched name, attempt, state or outcome.
- **A2 and B3:** [release packaging](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/.github/workflows/release.yml:78) now fetches full history in every matrix job. A [workflow regression](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/tests/cli/agent-upgrade-workflows.test.ts:5) checks every workflow job running the suite or repository audit for baseline history.
- **B4:** the [recovery guide](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/docs/guides/user/background-agents.md:86) now describes automatic progress recovery, corroborated terminal outcomes and the remaining fail-closed ambiguity route.

The expanded regressions produced 32 expected failures and 18 passing controls on the prior `a7c80cd8` candidate; every case passes in the final unfiltered suite.

Ordered range `51725e8b..d4849813`, oldest first:

- `805e4d36` — terminal identity and confirmed control outcomes.
- `b2d8e795` — evidence preservation across interrupted control operations.
- `4cd0ab87` — interrupted preparation and append recovery.
- `b3fec501` — renamed-folder fixture history.
- `a7c80cd8` — initial legacy-failure classification.
- `22e0ea9c` — sixth-round legacy replay fixes, upgrade regressions and recovery guidance.
- `3a3407e0` — release checkout history and workflow regression; **pre-migration admission tip**.
- `d4849813` — held depcruise migration, rebased from `219968a0` only; **last**.

Final gates, one outcome per line:

- PASS — Full suite with coverage: 2,127 tests in 96 files, including all 52 persistence and abrupt-exit matrix cases; no filtered or skipped tests.
- PASS — Coverage: statements 16,893/16,893; branches 11,749/11,749; functions 3,596/3,596; lines 14,291/14,291; all 100%, with thresholds and exclusions unchanged.
- PASS — TypeScript: full `tsc --noEmit`; configuration unchanged.
- PASS — Biome: full repository check; no errors, one pre-existing informational suggestion; configuration unchanged.
- PASS — Build: canonical Bun compilation to temporary output; compiled version `0.13.0` and agent-help smoke checks.
- PASS — rumdl: changed recovery guide and this report.
- PASS — Candidate `KI_REPO_OFFLINE=1 ki repo audit`: migration tree `d4849813`, candidate Harness `db5e3cff`; exit 0, 17 skill passes, five skill warnings, zero failures, nine warning findings.
- PASS — CI-pinned `KI_REPO_OFFLINE=1 ki repo audit`: pre-migration `3a3407e0`, KI `v0.12.0`, Harness `f4d6c521ef4859dc8965579bc39a5575004e3ac5`; exit 0, 18 skill passes, four skill warnings, zero failures, nine warning findings.
- PASS — Normal commit hooks and explicit paths: both new commits contain exactly their intended files; their final co-author trailers name Codex (GPT-6).
- PASS — Rebase and audit fidelity: only the migration was rebased; all 506 tracked files in each committed tree match its independently composed audit copy byte for byte.
- PASS — Scope: primary `main` remains `6c4d2a1a`; no admission, remote operation, tag, release, work-record acceptance or pruning was performed.

The audit executable for KI `v0.12.0` was compiled offline from the exact local release tag with its unchanged dependency lockfile. Both Harness exports were verified against local Git archives: 1,388 files at `db5e3cff2946beaa05bbf2f821dc7d93fb1daf97` and 1,379 at the pinned `f4d6c521` revision. All test and audit processes ran behind the external-network denial fence. Hosted CI was not contacted.

Earlier verification attempts exposed missing local pre-migration dependency tools and isolated-home memory defaults that disagreed with the repository's disabled-memory policy. Those verification setups were corrected before the final complete reruns. No real user environment, scheduler or credential configuration changed.

## In Progress

Nothing is running. Admission remains with the supervisor; this run did not admit either tree. Updated admission plan:

1. Review and admit through `3a3407e09dd0b2d39976840d95e8b4ee94b63de7` while retaining `tooling/boundaries` and CI's `KI_VERSION: v0.12.0`. Its exact committed tree passed that pinned audit offline. Keep `d4849813` held back; hosted CI remains the subsequent publication check.
2. Reconcile the existing local-main mismatch deliberately. After verifying a clean primary and that its two local fix commits are represented by the rebased equivalents, use a guarded compare-and-swap from expected `6c4d2a1aeabdac5ce5ca2e4bd711908d043afcf3` to `3a3407e09dd0b2d39976840d95e8b4ee94b63de7` and refresh that checkout. This is not a fast-forward from the present local `main`; no such operation was performed here.
3. Separately authorize the pin-carrying KI release preparation: keep the old tooling layout and current CI pin, update `canonicalHarnessRelease` to an immutable published Harness revision containing `db5e3cff` with its verified archive digest, and set the new KI release version. Gate, review and release that preparation through the normal workflow. Today's source pin `52779419` and CI-pinned `v0.12.0` do not provide the new depcruise rule.
4. Once that KI release is available and clean-install verified, rebase the held migration onto the release preparation and admit it together with a CI `KI_VERSION` bump to that exact released tag. Populate the primary's `tooling/depcruise/node_modules` before launching worktrees, and rerun the migrated tree's gates and audit with the newly released KI. Release availability alone does not make the migration compatible with CI's unchanged `v0.12.0` pin.

## Queries

None.

### 🤖 → 👤 Handoff to supervisor · since 13:09 BST

🤖 0 running · 👤 1 you

- [with you] Review the verified range and execute the staged admission plan · supervisor · since 13:09 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
