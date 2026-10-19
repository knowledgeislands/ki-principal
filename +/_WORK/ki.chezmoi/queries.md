# ki.chezmoi queries

## Open

### SOURCE-LOCALS-LIVE - Whether the earlier live-config removal was intentional

since 2026-10-19 · from [sol-locals-gate](sol-locals-gate.report.md); the run's query carried no tag, so the migration gave it this one

**Context:** The brief requires live config to remain at the protected pre-apply baseline, but the target already contains the exact intended removal and the fresh one-target diff is empty. Required read-only checks are healthy. No test correction permission is needed.

**Note:** a source commit titled "Update config.toml", removing five lines from `dot_config/ki/config.toml`, landed at 17:39 BST, a minute before the live change.

**Query:** Was the 17:40 BST live-config removal intentional, so the next pass can record that fact and finish the separate verified test and bookkeeping commits without an apply?

**Options:**

a) (recommended, confidence high - current target exactly equals reviewed source and read-only checks are healthy) Confirm the earlier removal was intentional; finish local test/bookkeeping commits and record that no apply remains.

b) Investigate who changed the protected target before continuing; leave current source, target and verified test unchanged meanwhile.

### RIG-LIVE-DELIVER - Deliver the Dock tool links before the held Rig records

since 2026-10-19 · from the RIG-LIVE line of KI > Model > Ways of working

**Context:** Kris chose to hold KI-TOOL-RIG-CORE-042 and -047 until this work delivers [KB-DOTFILES-UE-091](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-091-shared-dock-tool-links.md) without linking ChatGPT (`chatgpt-current` belongs to no profile, so linking it drops ChatGPT off both Docks), and adds a firewall declaration that adopts Terra's unreceipted Rig anchor and covers Sol; Kris then applies both attended. The parked REST-HOLD query held the Dock work for CORE-042, so this reverses that order. Evidence: [rig-live report](/Users/krisbrown/.local/state/ki/agents/ways-of-working/rig-live.report.md).

**Query:** Plan and deliver KB-DOTFILES-UE-091 source-side now, with the firewall declaration, and no apply?

**Options:**

a) (recommended, confidence medium - follows Kris's routed choice; the record needs planning to Ready first) Launch a plan-then-implement run for UE-091 and the firewall declaration, source only, `rig doctor` before and after, then show the diff for an attended apply.

b) Keep REST-HOLD as parked until CORE-042 is released.

## Parked

- **SOURCE-LOCALS-GATE:** Resolved, the worker judges: the source removal of `[locals]` landed in `dot_config/ki/config.toml` at 17:39 BST on 19 October and the test correction followed. Closes with SOURCE-LOCALS-LIVE.
- **SOURCE-LOCALS-APPLY:** Superseded, the worker judges: the live target already equals the source and the one-target diff is empty. Closes with SOURCE-LOCALS-LIVE.
- **FIRST-STEP-GATES:** Resolved for this owned scope: prerequisites committed and published, source gates pass, four-target apply and user-link repair verified. Historical failure reports remain evidence, not current blockers. Looks resolved; carried for the worker to judge.
- **IWORK:** Keynote, Numbers and Pages remain catalogue-only in the approved burn-down report. The later native MAS fix does not by itself answer this completion choice. Recommendation: Keep Keynote, Numbers and Pages catalogue-only and complete the A8 source step, retaining owner review and acceptance. See [Finish the iWork source step](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-086-finish-software-alignment.md>). Options remain in the [parked query](wrap-ways-20261018.report.md).
- **STYLE-LINK:** The output-style link depends on the harness checkout. A read-only warning and an apply-time pull were offered; neither choice is approved. Recommendation: Add a read-only dead-link check after apply, with no harness pull during apply. See [Warn about a missing output style](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md>). Options remain in the [parked query](wrap-ways-20261018.report.md).
- **DIR-PRUNE:** The current merge unions additionalDirectories. Removal needs a declared ownership model so hand-added paths survive. Recommendation: Record the previously managed additionalDirectories set in a state file and prune only entries that left that declaration. See [Remove retired managed directory entries](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md>). Options remain in the [parked query](wrap-ways-20261018.report.md).
- **REST-HOLD:** Dock work still waits on the Rig profile-filter implementation: its record remains ready, not delivered. The latest release is still v0.6.3. The remaining bring-up gaps also depend on the Headroom profile work or fresh planning. Recommendation: Hold the Dock work and remaining bring-up work until CORE-042 is released and the Headroom profile work is delivered. See [Keep the remaining bring-up work parked](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-091-shared-dock-tool-links.md>). Options remain in the [parked query](wrap-ways-20261018.report.md).
