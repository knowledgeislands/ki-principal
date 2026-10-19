# ki.chezmoi queries

## Open

### RIG-FIREWALL-RUN - Run Terra's firewall restore rehearsal attended

since 2026-10-19 · from run firewall-rehearse ([report, with the two-terminal sequence](/Users/krisbrown/.local/state/ki/agents/chezmoi/firewall-rehearse.report.md))

**Context:** Every rehearsal step needs `sudo`, which asks for a password on Terra, so the run stopped before any change after recording Terra's state: anchor and LaunchDaemon present, daemon loaded with last exit 0, Screen Sharing listening, SSH from Sol working. Port 22 is outside the anchor, so SSH should hold throughout; a second terminal proves it. Sol still needs its own rehearsal before its `rig apply --sudo`.

**Query:** Will Kris run the sequence from two terminals on Sol and paste the output or say "passed"?

**Options:**

a) (recommended, confidence high - every step reversible, an open session stays as fallback) Run it now from Sol; a follow-up run records the evidence in [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) and writes, gates and commits the `core` declaration, no push or apply.

b) Hold until Kris is at Terra and run it on Terra's console.

## Parked

- **FIRST-STEP-GATES:** Resolved for this owned scope: prerequisites committed and published, source gates pass, four-target apply and user-link repair verified. Historical failure reports remain evidence, not current blockers. Looks resolved; carried for the worker to judge.
- **IWORK:** Keynote, Numbers and Pages remain catalogue-only in the approved burn-down report. The later native MAS fix does not by itself answer this completion choice. Recommendation: Keep Keynote, Numbers and Pages catalogue-only and complete the A8 source step, retaining owner review and acceptance. See [Finish the iWork source step](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-086-finish-software-alignment.md>). Options remain in the [parked query (pruned)](https://github.com/knowledgeislands/ki-principal/blob/319c169d611d63a4e5799877981516ee811c737c/%2B/_WORK/ki.chezmoi/wrap-ways-20261018.report.md#queries).
- **STYLE-LINK:** The output-style link depends on the harness checkout. A read-only warning and an apply-time pull were offered; neither choice is approved. Recommendation: Add a read-only dead-link check after apply, with no harness pull during apply. See [Warn about a missing output style](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md>). Options remain in the [parked query (pruned)](https://github.com/knowledgeislands/ki-principal/blob/319c169d611d63a4e5799877981516ee811c737c/%2B/_WORK/ki.chezmoi/wrap-ways-20261018.report.md#queries).
- **DIR-PRUNE:** The current merge unions additionalDirectories. Removal needs a declared ownership model so hand-added paths survive. Recommendation: Record the previously managed additionalDirectories set in a state file and prune only entries that left that declaration. See [Remove retired managed directory entries](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md>). Options remain in the [parked query (pruned)](https://github.com/knowledgeislands/ki-principal/blob/319c169d611d63a4e5799877981516ee811c737c/%2B/_WORK/ki.chezmoi/wrap-ways-20261018.report.md#queries).
- **REST-HOLD:** Dock work still waits on the Rig profile-filter implementation: its record remains ready, not delivered. The latest release is still v0.6.3. The remaining bring-up gaps also depend on the Headroom profile work or fresh planning. Recommendation: Hold the Dock work and remaining bring-up work until CORE-042 is released and the Headroom profile work is delivered. See [Keep the remaining bring-up work parked](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-091-shared-dock-tool-links.md>). Options remain in the [parked query (pruned)](https://github.com/knowledgeislands/ki-principal/blob/319c169d611d63a4e5799877981516ee811c737c/%2B/_WORK/ki.chezmoi/wrap-ways-20261018.report.md#queries).
