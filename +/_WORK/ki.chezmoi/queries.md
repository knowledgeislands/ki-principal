# ki.chezmoi queries

## Open

### APPLY-CARRY - Apply the Dock, TOML and Paperclip source changes on both Macs

since 2026-10-19 · from runs rig-dock and carry-directions ([report](/Users/krisbrown/.local/state/ki/agents/chezmoi/carry-directions.report.md))

**Context:** Five Rig targets differ under `~/.config/rig/conf.d/`, nothing applied: `40-macos` (Dock tool links from [KB-DOTFILES-UE-091](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-091-shared-dock-tool-links.md) plus the `.toml` handler to Zed), `90-profiles` (Dock), and `15-command-line`, `50-services`, `55-ports` (Paperclip held off every profile). Seat bindings render nothing yet. Removing Paperclip from profiles does not unload a launchd job an earlier apply installed; on Terra it was declared stopped but nobody has checked. Live `rig doctor` has one standing finding, `utm` drifted via the App Store, which needs Kris to reinstall.

**Query:** Apply these on Sol and then Terra, attended?

**Options:**

a) (recommended, confidence high - each step reviewed and reversible) On each Mac: review `chezmoi diff ~/.config/rig`, apply those five targets only, `rig apply --target dock:workstation` and `--target default-application:toml` (dry run first), `rig doctor`; on Terra also check `launchctl print gui/$(id -u)/uk.me.kris.rig.paperclip`.

b) Hold them and fold them into a later combined review.

### RIG-FIREWALL-REHEARSE - Where to rehearse the firewall restore

since 2026-10-19 · from run rig-dock ([report](/Users/krisbrown/.local/state/ki/agents/chezmoi/rig-dock.report.md)) · reviewed ([firewall-review](/Users/krisbrown/.local/state/ki/agents/chezmoi/firewall-review.report.md))

**Context:** The firewall declaration (tailnet-only Screen Sharing on `tcp:5900` and `udp:5900` for every Mac in `core`, adopting Terra's anchor) is not written, because the connection-critical rule needs the restore rehearsed before the change on the same machine. Sol has no anchor, daemon or service; this session has no `sudo`. Terra's daemon was recorded loaded since 15 October, but its kernel anchor being loaded is unproved, and "tailnet-only" still allows shared-range LAN access and forged-source UDP ([KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md)). The review prefers c): a) proves Terra's restore only before applying on Sol too, and b) rehearses after the change.

**Query:** Where should the restore be rehearsed before the declaration is written?

**Options:**

a) (recommended, confidence high - review disagrees, it would still need a Sol rehearsal before the Sol apply) Attended, from Sol: run the restore on Terra over SSH, confirm SSH holds and the rules are gone, re-bootstrap, record evidence; then a run writes the declaration for an attended `rig apply --sudo` on Terra, then Sol.

b) Attended on Sol: apply with `--sudo` and rehearse the restore there at once.

c) Leave the firewall to KI-TOOL-RIG-CORE-047's live acceptance and write no declaration now.

## Parked

- **FIRST-STEP-GATES:** Resolved for this owned scope: prerequisites committed and published, source gates pass, four-target apply and user-link repair verified. Historical failure reports remain evidence, not current blockers. Looks resolved; carried for the worker to judge.
- **IWORK:** Keynote, Numbers and Pages remain catalogue-only in the approved burn-down report. The later native MAS fix does not by itself answer this completion choice. Recommendation: Keep Keynote, Numbers and Pages catalogue-only and complete the A8 source step, retaining owner review and acceptance. See [Finish the iWork source step](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-086-finish-software-alignment.md>). Options remain in the [parked query (pruned)](https://github.com/knowledgeislands/ki-principal/blob/319c169d611d63a4e5799877981516ee811c737c/%2B/_WORK/ki.chezmoi/wrap-ways-20261018.report.md#queries).
- **STYLE-LINK:** The output-style link depends on the harness checkout. A read-only warning and an apply-time pull were offered; neither choice is approved. Recommendation: Add a read-only dead-link check after apply, with no harness pull during apply. See [Warn about a missing output style](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md>). Options remain in the [parked query (pruned)](https://github.com/knowledgeislands/ki-principal/blob/319c169d611d63a4e5799877981516ee811c737c/%2B/_WORK/ki.chezmoi/wrap-ways-20261018.report.md#queries).
- **DIR-PRUNE:** The current merge unions additionalDirectories. Removal needs a declared ownership model so hand-added paths survive. Recommendation: Record the previously managed additionalDirectories set in a state file and prune only entries that left that declaration. See [Remove retired managed directory entries](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md>). Options remain in the [parked query (pruned)](https://github.com/knowledgeislands/ki-principal/blob/319c169d611d63a4e5799877981516ee811c737c/%2B/_WORK/ki.chezmoi/wrap-ways-20261018.report.md#queries).
- **REST-HOLD:** Dock work still waits on the Rig profile-filter implementation: its record remains ready, not delivered. The latest release is still v0.6.3. The remaining bring-up gaps also depend on the Headroom profile work or fresh planning. Recommendation: Hold the Dock work and remaining bring-up work until CORE-042 is released and the Headroom profile work is delivered. See [Keep the remaining bring-up work parked](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-091-shared-dock-tool-links.md>). Options remain in the [parked query (pruned)](https://github.com/knowledgeislands/ki-principal/blob/319c169d611d63a4e5799877981516ee811c737c/%2B/_WORK/ki.chezmoi/wrap-ways-20261018.report.md#queries).
