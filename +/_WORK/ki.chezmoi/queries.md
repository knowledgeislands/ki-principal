# ki.chezmoi queries

## Open

### SOL-PF-ROOT - Check what Sol's root pf ruleset holds

since 2026-10-19 · from run sol-preflight ([report, with the read-only block](/Users/krisbrown/.local/state/ki/agents/chezmoi/sol-preflight.report.md))

**Context:** Sol's pf files are Apple's defaults, but NordVPN's helper can replace root's ruleset with a block-by-default one; if it is still loaded, the first `pfctl -E` would switch it on and could cut SSH, Tailscale and Screen Sharing, and a NordVPN connection would bypass the anchor. Only root can see which.

**Query:** Will Kris run the read-only block on Sol and give the result line?

**Options:** a) (recommended, confidence high - settles the unknown without changing anything; the apply sequence re-checks it before enabling pf) Run it; on `STOCK`, sol-preflight finishes and gates the apply on a stock ruleset with NordVPN disconnected, and the NordVPN bypass goes to KI-TOOL-RIG-CORE-047. b) Disconnect or quit NordVPN first, then run it. c) Hold Sol's apply until KI-TOOL-RIG-CORE-047 settles NordVPN.

## Parked

- **GUIDE-REMOTE:** The macOS workstation guide's Remote access section (line 107) still says to turn Screen Sharing off until a pf rule exists. Recommendation: update it after Sol's attended apply, pointing at `[firewall.screen-sharing-tailnet]` and KI-TOOL-RIG-CORE-047's rollback (confidence medium; blind review before it returns to Kris). From [firewall-record](/Users/krisbrown/.local/state/ki/agents/chezmoi/firewall-record.report.md).
- **FIRST-STEP-GATES:** Resolved for this owned scope: prerequisites committed and published, source gates pass, four-target apply and user-link repair verified. Historical failure reports remain evidence, not current blockers. Looks resolved; carried for the worker to judge.
- **IWORK:** Keynote, Numbers and Pages remain catalogue-only in the approved burn-down report. The later native MAS fix does not by itself answer this completion choice. Recommendation: Keep Keynote, Numbers and Pages catalogue-only and complete the A8 source step, retaining owner review and acceptance. See [Finish the iWork source step](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-086-finish-software-alignment.md>). Options remain in the [parked query (pruned)](https://github.com/knowledgeislands/ki-principal/blob/319c169d611d63a4e5799877981516ee811c737c/%2B/_WORK/ki.chezmoi/wrap-ways-20261018.report.md#queries).
- **STYLE-LINK:** The output-style link depends on the harness checkout. A read-only warning and an apply-time pull were offered; neither choice is approved. Recommendation: Add a read-only dead-link check after apply, with no harness pull during apply. See [Warn about a missing output style](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md>). Options remain in the [parked query (pruned)](https://github.com/knowledgeislands/ki-principal/blob/319c169d611d63a4e5799877981516ee811c737c/%2B/_WORK/ki.chezmoi/wrap-ways-20261018.report.md#queries).
- **DIR-PRUNE:** The current merge unions additionalDirectories. Removal needs a declared ownership model so hand-added paths survive. Recommendation: Record the previously managed additionalDirectories set in a state file and prune only entries that left that declaration. See [Remove retired managed directory entries](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md>). Options remain in the [parked query (pruned)](https://github.com/knowledgeislands/ki-principal/blob/319c169d611d63a4e5799877981516ee811c737c/%2B/_WORK/ki.chezmoi/wrap-ways-20261018.report.md#queries).
- **REST-HOLD:** Dock work still waits on the Rig profile-filter implementation: its record remains ready, not delivered. The latest release is still v0.6.3. The remaining bring-up gaps also depend on the Headroom profile work or fresh planning. Recommendation: Hold the Dock work and remaining bring-up work until CORE-042 is released and the Headroom profile work is delivered. See [Keep the remaining bring-up work parked](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-091-shared-dock-tool-links.md>). Options remain in the [parked query (pruned)](https://github.com/knowledgeislands/ki-principal/blob/319c169d611d63a4e5799877981516ee811c737c/%2B/_WORK/ki.chezmoi/wrap-ways-20261018.report.md#queries).
