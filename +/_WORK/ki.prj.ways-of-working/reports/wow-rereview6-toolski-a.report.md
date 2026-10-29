# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rereview6-toolski-a

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 11:40 BST · last mark 08:24 BST**

VERDICT: REFUSE · confidence high - Legacy replay can still lose completion, and release jobs lack history required by the new tests.

---

## Done

Reviewed `51725e8b..219968a0` independently: `805e4d36`, `b2d8e795`, `4cd0ab87`, `b3fec501`, `a7c80cd8`, then held migration `219968a0`; the admission decision covers only `a7c80cd830d9c1e0e05f75d4f8414909d1c20e90`.

- Full tests with coverage at `a7c80cd8`: PASS, 2,078 tests across 95 files; all four coverage measures are 100% (16,881/16,881 statements), with LCOV confirming 14,281/14,281 lines, 3,592/3,592 functions and 11,723/11,723 branches.
- Fault and SIGKILL matrices: PASS, 26 scenarios each; 655 durable mutation sites and 651 controller-death sites, with 1,302 before/after death cells.
- TypeScript at `a7c80cd8`: PASS, `tsc --noEmit`.
- Biome at `a7c80cd8`: PASS, check mode; no fixes applied.
- Compiled build at `a7c80cd8`: PASS; explicit compiled-binary version and agent-help smoke checks pass.
- `KI_REPO_OFFLINE=1 ki repo audit` at `a7c80cd8`, using CI's KI `v0.12.0`: PASS on the full rerun: exit 0, 18 skill passes, four skill warnings, zero failures and eight warning findings; the first run failed only the four unchanged path-sensitive snapshots described in finding 9.
- Candidate identity: PASS; all 505 tracked files of both admission exports match `a7c80cd8` after verification, and all 1,379 tracked Harness files match the pinned revision.
- Audit provenance: PASS; locally compiled the exact `v0.12.0` tag, verified all 481 tracked release files, with the identical dependency lockfile, and exported its pinned Harness `f4d6c521ef4859dc8965579bc39a5575004e3ac5` from local Git objects into an isolated, bootstrapped HOME.
- Independent regression: FAIL in all seven added replay cases; an unfiltered control-file run passes all 481 existing cases and fails three delayed-failure cases plus four blocked-prefix cases.
- Test integrity: unchanged coverage configuration, thresholds, exclusions and package scripts; no added skip, only, todo or coverage-ignore directives; all 95 files run, with no skipped tests in the full gate.
- Read-only boundary: PASS; existing repositories, refs and tracked files unchanged; no network beyond test localhost fixtures, publication or release action; scratch material removed before DONE.

1. **Blocking — earlier review-a F1 is not fully resolved.** [events.ts:597](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/core/agent/events.ts:597) still treats launcher-like failure text as terminal without corroborating evidence. I generated state using untouched `51725e8b`: launch a live worker, observe its failure-progress line twice and acknowledge the events, preserve the old snapshot outside its active path, then replace the status with a new milestone followed by DONE and write the report before the first candidate observation. For `no report`, `attempt failed` and `exited without DONE (no status)`, the candidate waiter exits successfully as finished, publishes zero completion events and homes no report. Snapshot replay then adopts the false terminal classification. The safe outcome is verified classification or an actionable ambiguity refusal; text alone cannot establish terminal ownership. Related [blocked-event inference at events.ts:608](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/core/agent/events.ts:608) also consumes later completion for legacy worker progress beginning `gate cannot open:` or `could not launch:`. Both prefixes reproduce with retained and missing snapshots, even while the matching status line survives. All four cases return finished with no completion event or homed report.

2. **Blocking — the normal release workflow cannot run the new upgrade regressions.** [release.yml:75](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/.github/workflows/release.yml:75) checks out the release tag in each packaging job without requesting history, then runs the suite at line 84. [agent-control.test.ts:4710](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/tests/cli/agent-control.test.ts:4710) now requires Git object `51725e8b`. The CI job gained full history, but the release packaging jobs did not; the validate job's history is not shared with them. I reproduced the missing-baseline archive failure offline with a depth-one object store containing the exact candidate tip and tree; an unfiltered run of the unchanged control test file then failed all eight upgrade cases and passed the other 473. Add full history to the packaging checkout before relying on step 3 of the release plan; do not skip or filter these regressions.

3. **Non-blocking evidence gap supporting finding 1 — the added regression observes too early.** [agent-control.test.ts:4746](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/tests/cli/agent-control.test.ts:4746) runs the candidate while the matching failure status is still present, then writes the report and DONE afterward. That proves persistence of a classification already made with retained evidence. It does not prove safe first recovery after the status has changed. Add the delayed-upgrade ordering, including absent snapshots and launcher-text collisions, and require one completion, waiter notification and report homing, or explicit refusal before adoption where evidence is ambiguous. Add baseline-to-candidate blocked-prefix collisions too. Retain the retirement/no-redelivery assertions.

4. **Non-blocking — the other recovery mechanisms have substantive evidence.** [control-store.ts:568](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/core/agent/control-store.ts:568), [runs.ts:692](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/core/agent/runs.ts:692) and [events.ts:361](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/core/agent/events.ts:361) preserve confirmed effects, fence uncertain ownership, retire only preparations lacking spawn intent and restore only digest-verified journal prefixes. The fault and controller-death matrices assert journal preservation, outcome identity and refusal behavior rather than just successful execution. No additional defect was established in these paths; that does not override finding 1.

5. **Non-blocking for the selected range — earlier review-b F1 is resolved by holding the migration.** [ci.yml:12](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/.github/workflows/ci.yml:12) still pins `v0.12.0`; the audited `a7c80cd8` tree retains `tooling/boundaries`, its install commands and worktree provisioning. `219968a0` must remain held. Review-b F3 remains physically present but is deferred with it: primary has boundary dependencies and no depcruise dependency directory; provision the latter before using the migrated tree. The renamed-folder fixture concern shared by the earlier reports is resolved: [agent-events.test.ts:238](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/tests/cli/agent-events.test.ts:238) now preserves authoritative event history while testing retirement across the rename. Review-a's former constrained-gate limitation is resolved by this complete successful coverage run.

6. **Non-blocking for code review — earlier review-b F2 remains an explicit integration condition.** [AGENTS.md:13](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/AGENTS.md:13) specifies fast-forward integration. Primary `main` is still exactly `6c4d2a1aeabdac5ce5ca2e4bd711908d043afcf3`, and the candidate is not its descendant. Its only two main-only commits are `6c498f3a` and `6c4d2a1a`; range comparison confirms their representation by `805e4d36` and `b2d8e795`, with the intended first-end/homeReports conjunction preserved. The proposed full-SHA compare-and-swap is a reasonable deliberately authorized replacement, not a fast-forward or automatic standing entitlement. Execute only in the designated clean primary checkout, with a serialized Git write window, fresh branch/index/untracked-state checks, the exact expected old SHA, and checkout refresh and verification in that same window. Stop on any mismatch. No such operation was performed here.

7. **Non-blocking — the four-step release sequence is sound after correcting both blockers and renewing admission evidence.** [fixing report:45](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-toolski-fix-6.report.md:45) cannot currently justify “admit now.” Its separation of the migration is correct. Step 2 needs the explicit integration exception above. Step 3 needs separately authorized release preparation and publication: keep the old tooling layout and CI pin, select an immutable Harness revision containing `db5e3cff`, verify its digest and host compatibility, and publish a new exact KI release through normal gates and clean-install proof. Step 4 must combine the held migration with the CI pin change to that available release, rerun that release's audit on the combined tree, and provision primary dependencies before launching worktrees. Neither release availability alone nor current source pin `52779419` makes `219968a0` compatible with today's pinned audit.

8. **Non-blocking — remaining earlier review-c and attribution notes.** [earlier review-c](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-rereview5-c.report.md:1) correctly observed rebase fidelity and the homing conjunction, but its unconditional admission/fast-forward conclusion is superseded by findings 1, 2 and 6. Its trailer, author-address and guide observations, and review-b F4, remain cosmetic and require no admission fix; the pre-migration guide correctly names `tooling/boundaries`. The supplied earlier-report filenames containing `-toolski-` do not exist; I reviewed the matching range reports at `wow-rereview5-a.report.md`, `wow-rereview5-b.report.md` and `wow-rereview5-c.report.md`.

9. **Non-blocking for this range — pre-existing snapshot portability limits the green-CI claim.** [agent-compatibility.test.ts:103](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/tests/cli/agent-compatibility.test.ts:103) normalizes the lexical fixture root, while its saved expectations at [the snapshot:701](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/tests/cli/__snapshots__/agent-compatibility.test.ts.snap:701) retain macOS's private-path prefix. The first full pinned audit failed four footer snapshots under a canonical temporary path; untouched `51725e8b` reproduces exactly the same four failures. Restoring the usual macOS symlink spelling makes all seven compatibility cases pass without edits. This is outside the reviewed range. I infer that Ubuntu's canonical temporary paths also need checking before claiming hosted CI is green; this review did not run Linux. The reported final audit outcome uses the normal macOS path semantics and does not establish cross-platform release readiness.

## In Progress

Nothing running.

Outstanding — no action requested now: hosted Linux CI and release publication were outside this read-only, offline review; the pinned audit was reproduced locally with exact released source and Harness provenance. The migration stays held. The pre-existing snapshot portability issue in finding 9 remains for supervisor triage.

## Queries

### LEGACY-REPLAY — Repair before admission

**Context:** The existing gates miss legacy failure and blocked-progress cases that silently lose completion notification and report homing. The first five commits therefore remain unsafe to admit, even with the migration held.

**Query:** Should the candidate return for a bounded correction and fresh admission review?

**Options:**

a) (recommended, confidence high - the defect reproduces with untouched baseline state) Correct the evidence-based classification of failed and blocked legacy records and add the missing upgrade regressions, then rerun full gates and the CI-pinned audit before requesting admission.

b) Defer admission and retain the current main and held migration.

### RELEASE-HISTORY — Keep upgrade tests runnable in release jobs

**Context:** The new regressions need the baseline commit; the release packaging jobs retain shallow checkouts. Normal release preparation would therefore fail before packaging on every target.

**Query:** Should the bounded correction also supply the required history to the release packaging jobs?

**Options:**

a) (recommended, confidence high - the missing-baseline failure is reproduced offline) Give each packaging checkout full history, retain the upgrade tests unchanged, and verify the release checkout contract before renewed review.

b) Defer admission and release preparation until that workflow correction is ready.

### 🤖 → 👤 Handoff to supervisor · since 11:40 BST

🤖 0 running · 👤 2 you · ⛔ 2 blocked

- [with you] LEGACY-REPLAY: return the candidate for correction · supervisor · since 11:40 BST
- [with you] RELEASE-HISTORY: restore release-job test prerequisites · supervisor · since 11:40 BST
- [blocked] Admission through a7c80cd8 · supervisor · since 11:40 BST
- [blocked] Normal release preparation · supervisor · since 11:40 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
