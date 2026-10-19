# ki.chezmoi queries

## Open

### SOURCE-LOCALS-LIVE - Whether the earlier live-config removal was intentional

since 2026-10-19 · from [sol-locals-gate (pruned)](https://github.com/knowledgeislands/ki-principal/blob/fd50f58d1440bfb5954cc767ea7a1e958b4e907b/%2B/_WORK/ki.chezmoi/sol-locals-gate.report.md); the run's query carried no tag, so the migration gave it this one

**Context:** The brief requires live config to remain at the protected pre-apply baseline, but the target already contains the exact intended removal and the fresh one-target diff is empty. Required read-only checks are healthy. No test correction permission is needed.

**Note:** a source commit titled "Update config.toml", removing five lines from `dot_config/ki/config.toml`, landed at 17:39 BST, a minute before the live change.

**Query:** Was the 17:40 BST live-config removal intentional, so the next pass can record that fact and finish the separate verified test and bookkeeping commits without an apply?

**Options:**

a) (recommended, confidence high - current target exactly equals reviewed source and read-only checks are healthy) Confirm the earlier removal was intentional; finish local test/bookkeeping commits and record that no apply remains.

b) Investigate who changed the protected target before continuing; leave current source, target and verified test unchanged meanwhile.

### RIG-LIVE-DELIVER - Deliver the Dock tool links before the held Rig records

since 2026-10-19 · from the RIG-LIVE line of KI > Model > Ways of working

**Context:** Kris chose to hold [KI-TOOL-RIG-CORE-042](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-042-profile-filtered-dock-items.md) and [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) until this work delivers [KB-DOTFILES-UE-091](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-091-shared-dock-tool-links.md) without linking ChatGPT (`chatgpt-current` belongs to no profile, so linking it drops ChatGPT off both Docks), and adds a firewall declaration that adopts Terra's unreceipted Rig anchor and covers Sol; Kris then applies both attended. The parked REST-HOLD query held the Dock work for CORE-042, so this reverses that order. Evidence: [rig-live report](/Users/krisbrown/.local/state/ki/agents/ways-of-working/rig-live.report.md).

**Query:** Plan and deliver KB-DOTFILES-UE-091 source-side now, with the firewall declaration, and no apply?

**Options:**

a) (recommended, confidence medium - follows Kris's routed choice; the record needs planning to Ready first) Launch a plan-then-implement run for UE-091 and the firewall declaration, source only, `rig doctor` before and after, then show the diff for an attended apply.

b) Keep REST-HOLD as parked until CORE-042 is released.

### MGIT-APPLY - Apply the regenerated mgit completion

since 2026-10-19 · from run mgit-completion ([report](/Users/krisbrown/.local/state/ki/agents/chezmoi/mgit-completion.report.md))

**Context:** The source holds `_mgit` regenerated for mgit 0.17.0, gate green. The live target is unchanged. The diff drops `-f`, adds `overview`, `learn`, `-B/--bypass`, `--learn`, `-j/--jobs`, `-v`, `--json` and `--principals`, and rewords `-P`, `-L` and `-W`. The `_codex`, `_git-almanac`, `_ki` and `_rig` snapshots are also stale.

**Query:** Apply this one target, then verify an empty one-target diff and a new zsh loading `_mgit`?

**Options:**

a) (recommended, confidence high - one tool-generated file, every gate passing) Apply `~/.zsh/completions/_mgit` alone and verify.

b) Regenerate the other stale snapshots first and apply them together.

c) Do not apply.

### TRIAGE-CUT - Cut two of the three triage records

since 2026-10-19 · from run burndown-push ([report](/Users/krisbrown/.local/state/ki/agents/chezmoi/burndown-push.report.md))

**Context:** 20 open records, none Done or awaiting review, so nothing was pruned and the acceptance batch is empty. Of the 3 triage records: [KB-DOTFILES-UE-095](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-095-guide-continuity-check.md) edits the same guide [KB-DOTFILES-UE-090](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md) covers; [KB-DOTFILES-UE-096](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-096-thread-identity-hook-registration.md) waits on [KI-HARNESS-GOV-199](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-199-thread-identity-role-native-sessions.md) and [KI-TOOL-KI-CLI-145](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-145-thread-session-bindings-role.md); [KB-DOTFILES-UE-098](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-098-workspaces-git-audit-roots.md) is decided and ready to adopt.

**Query:** Which cuts go ahead?

**Options:**

a) (recommended, confidence medium - the merge is clear-cut; the cancel goes against an earlier capture) Merge UE-095 into UE-090 and cancel UE-096 until GOV-199 Phase 3 lands; keep UE-098. Net 20 to 18.

b) Merge UE-095 only and move UE-096 to Hold. Net 20 to 19.

c) Cut neither.

### CARRY-DIRECTIONS - Deliver the dropped source directions

since 2026-10-19 · from run mark-tidy-1019 ([report](/Users/krisbrown/.local/state/ki/agents/chezmoi/mark-tidy-1019.report.md))

**Context:** Kris authorised these between 15 and 17 October, and none is delivered: SEAT-BIND and SEAT-HOSTS as SEAT-CHANGE amends them (each host's seat role and territories in chezmoi host data); PAPERCLIP-OFF (keep the declaration, neither Mac applies or loads it); TOML-OPENER (`.toml` opens in Zed, not Warp); SSH-CONSOLE (physical-console fallback in the macOS workstation guide). The 19 October apply run dropped them from the work file. The firewall directions ride with RIG-LIVE-DELIVER.

**Query:** Should one source-only run deliver these four, each diff held for review?

**Options:**

a) (recommended, confidence medium - all authorised and none withdrawn, but dormant since 17 October and the seat map has changed) One source-only run after RIG-LIVE-DELIVER, `rig doctor` before and after, no apply.

b) Put each back to Kris before any run.

## Parked

- **SOURCE-LOCALS-GATE:** Resolved, the worker judges: the source removal of `[locals]` landed in `dot_config/ki/config.toml` at 17:39 BST on 19 October and the test correction followed. Closes with SOURCE-LOCALS-LIVE.
- **SOURCE-LOCALS-APPLY:** Superseded, the worker judges: the live target already equals the source and the one-target diff is empty. Closes with SOURCE-LOCALS-LIVE.
- **FIRST-STEP-GATES:** Resolved for this owned scope: prerequisites committed and published, source gates pass, four-target apply and user-link repair verified. Historical failure reports remain evidence, not current blockers. Looks resolved; carried for the worker to judge.
- **IWORK:** Keynote, Numbers and Pages remain catalogue-only in the approved burn-down report. The later native MAS fix does not by itself answer this completion choice. Recommendation: Keep Keynote, Numbers and Pages catalogue-only and complete the A8 source step, retaining owner review and acceptance. See [Finish the iWork source step](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-086-finish-software-alignment.md>). Options remain in the [parked query (pruned)](https://github.com/knowledgeislands/ki-principal/blob/319c169d611d63a4e5799877981516ee811c737c/%2B/_WORK/ki.chezmoi/wrap-ways-20261018.report.md#queries).
- **STYLE-LINK:** The output-style link depends on the harness checkout. A read-only warning and an apply-time pull were offered; neither choice is approved. Recommendation: Add a read-only dead-link check after apply, with no harness pull during apply. See [Warn about a missing output style](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md>). Options remain in the [parked query (pruned)](https://github.com/knowledgeislands/ki-principal/blob/319c169d611d63a4e5799877981516ee811c737c/%2B/_WORK/ki.chezmoi/wrap-ways-20261018.report.md#queries).
- **DIR-PRUNE:** The current merge unions additionalDirectories. Removal needs a declared ownership model so hand-added paths survive. Recommendation: Record the previously managed additionalDirectories set in a state file and prune only entries that left that declaration. See [Remove retired managed directory entries](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md>). Options remain in the [parked query (pruned)](https://github.com/knowledgeislands/ki-principal/blob/319c169d611d63a4e5799877981516ee811c737c/%2B/_WORK/ki.chezmoi/wrap-ways-20261018.report.md#queries).
- **REST-HOLD:** Dock work still waits on the Rig profile-filter implementation: its record remains ready, not delivered. The latest release is still v0.6.3. The remaining bring-up gaps also depend on the Headroom profile work or fresh planning. Recommendation: Hold the Dock work and remaining bring-up work until CORE-042 is released and the Headroom profile work is delivered. See [Keep the remaining bring-up work parked](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-091-shared-dock-tool-links.md>). Options remain in the [parked query (pruned)](https://github.com/knowledgeislands/ki-principal/blob/319c169d611d63a4e5799877981516ee811c737c/%2B/_WORK/ki.chezmoi/wrap-ways-20261018.report.md#queries).
