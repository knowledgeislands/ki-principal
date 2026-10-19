# ki.chezmoi queries

## Open

### SOURCE-LOCALS-LIVE - Whether the earlier live-config removal was intentional

since 2026-10-19 · from [sol-locals-gate](sol-locals-gate.report.md); the run's query carried no tag, so the migration gave it this one

**Context:** The brief requires live config to remain at the protected pre-apply baseline, but the target already contains the exact intended removal and the fresh one-target diff is empty. Required read-only checks are healthy. No test correction permission is needed.

**Query:** Was the 17:40 BST live-config removal intentional, so the next pass can record that fact and finish the separate verified test and bookkeeping commits without an apply?

**Options:**

a) (recommended, confidence high - current target exactly equals reviewed source and read-only checks are healthy) Confirm the earlier removal was intentional; finish local test/bookkeeping commits and record that no apply remains.

b) Investigate who changed the protected target before continuing; leave current source, target and verified test unchanged meanwhile.

### SOURCE-LOCALS-GATE - The source gate on the `[locals]` removal

since 2026-10-19 · from [sol-locals-complete](sol-locals-complete.report.md); looks resolved, the worker judges: the work file of 19 October records Kris's commits of the source removal (`dea74ab`) and the verified test correction (`006ce2d`)

**Context:** Live migration passed, but source removal exposes a test that still requires legacy locals. A second failure reflects the run's restrictive umask. The task explicitly requires stopping on unexpected gate failures, so neither was repaired and no source commit was made.

**Query:** Authorise the focused follow-up to update the obsolete locals test contract and rerun the full gate under the normal umask before committing the intended source/test paths?

**Options:**

a) (recommended, confidence high - aligns the assertion with the approved migration and separates the capture umask from render semantics) Authorise that bounded test update and gate rerun; retain the explicit apply hold.

b) Leave the candidate and bookkeeping uncommitted for a later owner-led review.

### SOURCE-LOCALS-APPLY - Keeping the `[locals]` removal unapplied

since 2026-10-19 · from [sol-locals-complete](sol-locals-complete.report.md); looks superseded by SOURCE-LOCALS-LIVE, the worker judges: the later gate run found the live target already equal to the source

**Context:** Both hosts passed; the source-only removal and bounded non-secret diff are ready, but the source gate is unresolved. Live configuration and host-local state are still unchanged.

**Query:** Keep the removal unapplied until the gate is resolved and Kris explicitly approves the proposed scripts-excluded apply and verification?

**Options:**

a) (recommended, confidence high - preserves the explicit apply boundary) Keep this gate in force and request approval after source verification succeeds.

b) Defer source removal entirely while retaining the migration evidence.

## Parked

- **FIRST-STEP-GATES:** Resolved for this owned scope: prerequisites committed and published, source gates pass, four-target apply and user-link repair verified. Historical failure reports remain evidence, not current blockers. Looks resolved; carried for the worker to judge.
- **IWORK:** Keynote, Numbers and Pages remain catalogue-only in the approved burn-down report. The later native MAS fix does not by itself answer this completion choice. Recommendation: Keep Keynote, Numbers and Pages catalogue-only and complete the A8 source step, retaining owner review and acceptance. See [Finish the iWork source step](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-086-finish-software-alignment.md>). Options remain in the [parked query](wrap-ways-20261018.report.md).
- **STYLE-LINK:** The output-style link depends on the harness checkout. A read-only warning and an apply-time pull were offered; neither choice is approved. Recommendation: Add a read-only dead-link check after apply, with no harness pull during apply. See [Warn about a missing output style](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md>). Options remain in the [parked query](wrap-ways-20261018.report.md).
- **DIR-PRUNE:** The current merge unions additionalDirectories. Removal needs a declared ownership model so hand-added paths survive. Recommendation: Record the previously managed additionalDirectories set in a state file and prune only entries that left that declaration. See [Remove retired managed directory entries](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md>). Options remain in the [parked query](wrap-ways-20261018.report.md).
- **REST-HOLD:** Dock work still waits on the Rig profile-filter implementation: its record remains ready, not delivered. The latest release is still v0.6.3. The remaining bring-up gaps also depend on the Headroom profile work or fresh planning. Recommendation: Hold the Dock work and remaining bring-up work until CORE-042 is released and the Headroom profile work is delivered. See [Keep the remaining bring-up work parked](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-091-shared-dock-tool-links.md>). Options remain in the [parked query](wrap-ways-20261018.report.md).
