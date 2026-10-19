# Decisions

- Kris (2026-10-13): the RESTART on sol also upgrades it from macOS 26 Tahoe to macOS 27 Golden Gate, so the restart takes longer. After it is back: confirm Tailscale reconnects, then check sol on macOS 27 (sw_vers, rig doctor, chezmoi status) before closing the Project.

- BURN-DOWN (Kris, 2026-10-14): standing focus, burn the roadmap down; no new feature records - [ki decisions](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/decisions.md).

- FW-PROFILES, FW-REVIEW and FW-LIVE (Kris, 2026-10-14): KI-TOOL-RIG-CORE-047 live on both Macs, terra first then sol, closed through ki-accept after the live test passes - [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md).

- Kris (2026-10-14): CLOSE-OUT keep the Project open until the firewall is live on sol and the SSH token fix lands. ZED-MD later.

- Kris (2026-10-14): FW-CHEZMOI move private_56-firewall.toml out of the chezmoi source into the run folder until the release. FW-LINUX-REVIEW approve KI-TOOL-RIG-CORE-051 and ADR-KI-TOOL-RIG-010 (acceptance waits for a live Linux test).

- Kris (2026-10-11): "ZED-MD, yes, add that capability to the roadmap for rig. You can also make the change directly now for me."

- LOCAL-MODE (Kris, 2026-10-14): sol is an active development machine, so its KI tools run in local mode from the repository checkouts, on the dev channel; the agent host stays on the stable channel - [KB-DOTFILES-UE-089](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-089-ki-tool-release-channels.md).

- Kris 2026-10-14: 'OLD-TREES-RUN - I've moved them into ~/workspaces/_old'. Done by Kris at sol: kit, hnr and knowledge-wayfinder now sit in ~/workspaces/_old (not the proposed _retired-old-trees-2026-10-14).

- Kris 2026-10-15: 'even if you are waiting on me, I'm going to need instructions'. Every held item waiting on Kris carries step-by-step instructions in the report.

- Kris 2026-10-15 about 02:03 BST: 'remote login stay off? nope, happy for it to be on' - Remote Login on terra may be turned on, so sol can reach terra over SSH.

- FW-VERIFY (Kris 2026-10-15, at terra): pf Status Enabled; the screen-sharing anchor holds the eight tailnet-only rules on port 5900 (lo0, 100.64.0.0/10, fd7a:115c:a1e0::/48, then block, TCP and UDP). terra's firewall rules are proven loaded.

- REGISTRY-STORES (Kris 2026-10-15): "fix them and don't worry about a backup" - bind sol's eight sources stores now

- GOOD-STATE (Kris 2026-10-15 10:4x BST): "essentially I'm allowing you to make updates to rig, dotfiles and rig.midnight.ninja to get everything into a good state" - standing authority for local changes in tools-rig, chezmoi and apps-rig.midnight.ninja; pushing, ki-accept and at-screen applies still need Kris

- ADOBE-DATA (Kris, 2026-10-15): Once both Macs have run adobe-remove.sh, an agent proposes a per-folder list for me to approve: delete caches, logs and empty folders; keep every Lightroom catalogue, preset and Photoshop setting; I run the approved deletions at each screen.

- UTM-SOL (Kris, 2026-10-15): At sol I quit UTM, run brew uninstall --cask utm, then mas install 1538878817, and check mas list shows it and my VMs open.

- OBS-RESTART (Kris, 2026-10-15): I'll run launchctl kickstart -k "gui/$(id -u)/uk.me.kris.rig.observatory" at sol and check the tab at <http://127.0.0.1:1675/> shows the dome.

- HEADROOM-ICON (Kris, 2026-10-15): I'll file a feature request on Headroom's GitHub repository for an SVG favicon on its dashboard and settings pages, attaching favicons-headroom.svg.

- DESK-KIT (Kris, 2026-10-15): I'll buy the recommended bundle: Shure MV7+, RØDE PSA1+ arm, Logitech MX Brio and Kanto ORA, checking each price on the page first.

- RESEARCH-FOOTER (Kris, 2026-10-15): Briefs that need them add: "read-only web search and fetches, git fetch and read-only SSH named in the task are allowed; no sign-in, purchase, posting, push or other remote call".

- SITE-SPARK (Kris, 2026-10-15): Yes: change the line to "Spark Desktop - one mail client on every machine".

- SITE-PRIVATE (Kris, 2026-10-15): Keep 1Password, its CLI and Tower named in the guide.

- RIG-OWNER and RIG-CATALOGUE (Kris via state-of-play, 2026-10-17 14:20 BST): this thread carries the tools-rig burndown lane, starting once SOL-APPLY, SOL-CLT and TERRA-READ are answered; RIG-CATALOGUE captured as an idea only, no record or design until Kris asks.

- Kris 2026-10-18 RIG-STACK-PUSH: 'Step 2, leave it' - the tools-rig push is left to the session owning KI-TOOL-RIG-CORE-060; confirm the prune reached GitHub at the next report.

- Kris 2026-10-18: 'I'm going to defer the restarting for now. Maybe remind me another day.' - ADOBE-RUN part 3 (restart sol and final check) held; remind Kris at the next resume.

- Kris 2026-10-18 ADOBE-LOG: 'I'm less worried about the Adobe logs, you can just get rid of everything. And also I don't think we don't have it installed on Terra, so it's all good. Let's have a look at something that's other than Adobe.' - delete the Adobe logs and the answered Adobe thread reports; terra Adobe steps dropped (not installed there); ADOBE-DATA parked, not deleted, since it holds the Lightroom catalogue; script kept for the deferred restart check.

- Kris 2026-10-19 23:27 BST: "All three are high confidence to do them." - taken as a) on all three: RIG-ORDER, plan and deliver KI-TOOL-RIG-CORE-063 in the background now, then plan KI-TOOL-RIG-CORE-062 and KI-TOOL-RIG-CLI-027 (chained runs core063, plan062, plan027; local commits in tools-rig, no push); SOL-FW-TEST, Kris restates or confirms it and the entry stays until then; PUSH-STACK, leave the ki-principal push to the next owning session that pushes, which fetches and rechecks first.

- 2026-10-19 23:30 BST, messages taken in queue order: HOOK-GUARD (IMPORTANT) folded into every brief; RIG-UNLOAD-LABEL and TOML-HANDLER sent to run rig-capture in tools-rig, ahead of core063 because of the safety question; METHOD-READ applied, `method_read` set to `84b61942`; RIG-FULLSCREEN held here as an idea only, with no record or implementation authority (Kris approved, 19 October): an interactive full-screen Rig terminal mode with btop-style panes, distinct from the two-line progress footer, wording at 135fe9e1 in +/_THREADS/state-of-play/decisions.md line 367.

- 2026-10-19 23:39 BST, decision-strike received: struck in 64ddf80f; its flags on terra key-only SSH, HOSTKEY-APPLY and SOL-HNR-HARNESS recorded in state.md as looks resolved, to confirm with Kris; brief pruned.

- Kris 2026-10-19 23:41 BST: "The firewall test was finished. It's all good. I think the boot out guard was not necessary; it was just a complete mistake, and it won't happen again. It was down to a script error." - SOL-FW-TEST closed as the sol firewall test, finished and good; KI-TOOL-RIG-CORE-047 acceptance still with Kris; BOOTOUT-GUARD b), no record captured, the terra shutdown put down to a script error.

- 2026-10-19 23:44 BST, IMPORTANT HOOKS-MIGRATION line from ki (State of play): this work leaves no uncommitted package.json, bun.lock, .husky/ or .githooks/ changes in ki-principal or tools-rig (tools-rig checked clean on those paths); HOOK-GUARD superseded, the briefs' extra --dry-run caution left in place as harmless.
