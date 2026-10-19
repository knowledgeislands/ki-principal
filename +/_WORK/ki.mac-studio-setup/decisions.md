# Decisions

## Decision 1 (2026-10-08)

- Kris (2026-10-08, mac-studio-bootstrap thread): approved as work in hand "Capture a chezmoi roadmap record for a Mac Studio exception to Rig's tailscale-app cask, done before the runbook's step 11 swaps the app for tailscaled" and "Fold results into the checkpoint as they land"; checkpoint kept to current state only. Remote access exception for this run: agents may use SSH to sol (krisbrown@100.90.130.74) and run Homebrew on it, only when the prompt says so; no other remote calls.

## Decision 2 (2026-10-08)

- Kris: "KI-ARCADIA-GOV-033 - accepted". Accept through ki-accept only.

## Decision 3 (2026-10-08)

- Kris: "Trust knowledgeislands/tap - yes"; "Install mas and run Rig dry run - yes". Over SSH on sol only; no sudo, no rig apply, no chezmoi apply, no other taps trusted, no Tailscale change.

## Decision 4 (2026-10-08)

- Kris: 1Password CLI integration "was already ticked" on sol. Check over SSH whether op works from an SSH session (read-only, op whoami); no secrets read.

## Decision 5 (2026-10-09)

- Kris: install dockutil on sol - "yes". Trust steipete/tap for codexbar - "yes, definitely trust that tap". Damaged apps on sol (discord, drawio, notion) - "I would fix anything that is damaged on Sol". NordVPN may be installed on sol ("you can get NordVPN"). Keep the Tailscale app set to open at login for now; swap decision deferred "once we have more running". Kris ran chezmoi init on sol; 1Password relocks after about 10 seconds.

## Decision 6 (2026-10-09)

- Coordinator, under Decision 1 (walk Kris through the sol steps in order): chezmoi init on sol confirmed complete; next is the read-only chezmoi diff review summary over SSH, excluding the four 1Password-backed targets, then fold all results into the checkpoint. No chezmoi apply.

## Decision 7 (2026-10-09)

- Kris: 1Password auto-lock "has been turned off" on sol. Tailscale "Launch at login" toggle in the app was unavailable, but Kris turned it on in System Settings login items; Kris is not at sol now. Check read-only whether Tailscale will start at login. Kris also said Rig "should in some way support some kind of uninstall" (capture to be confirmed).

## Decision 8 (2026-10-09)

- Kris: Rig profiles - one single list of software; a core profile, with laptop and studio profiles building on core; "it is still my rig". Capture the tools-rig uninstall / doctor-warning record and widen DOTFILES-UE-075 ("this one makes sense"). Run the read-only sol vs laptop comparison - yes. Keep Outlook and Lightroom Classic on sol Dock (Outlook is on the laptop Dock; find why it differs). Pull chezmoi source on sol to latest - "never a problem"; and capture that chezmoi should always run from latest. Kris half-remembers a tool with a machine-local directory mechanism for per-machine selection - investigate.

## Decision 9 (2026-10-09)

- Kris: "Yes, those can be dropped" (sol VS Code local settings edits). "Yes, apply it in two parts": chezmoi apply of all non-secret targets by an agent over SSH; the four 1Password-backed targets by Kris in Terminal on sol screen.

## Decision 10 (2026-10-09)

- Kris: "I just pulled, seemed to work without issue" - Kris fast-forwarded the chezmoi source on sol himself (GUI session). The SSH-session pull had failed to reach GitHub. Relaunching the non-secret apply (Decision 9) with this context.

## Decision 11 (2026-10-09)

- Kris: "Can you put any outstanding situation or questions into the checkpoint? I am going to ask the master checkpoint to reassess where we are on some things and maybe redivide the work."

## Decision 12 (2026-10-09)

- Kris: "You can finish the work that you are doing though in terms of then reconciling the different things and also the fact that the plan that we want to support the profiles, which are effectively my rig on different physical machines." Coordinator reading: finish the sol vs laptop reconciliation, adopt DOTFILES-UE-075 (per-machine Rig profiles) into Now and plan it to Ready through ki-next and ki-plan, using the reconciliation to propose core / laptop / studio membership. Implementation, rig apply and pushes still need Kris.

## Decision 13 (2026-10-09)

- Kris answers to DOTFILES-UE-075 questions: (1) studio apps - "Only DaVinci Resolve - others not needed anymore" (PTGui, PhotoSweeper, ScanSnap, Synology Drive, Dropbox no longer needed); (2) Spark Desktop - "Do we have Spark Desktop on laptop too? if so, yes on both" (laptop has only Spark.app, so open); (3) DisplayLink and WiFi Explorer laptop-only - "Don't see why they are" (core); (4) WhatsApp and 5G-Emerge refresh jobs - laptop only; (5) Paperclip - laptop only now, in the end on the remote host only; (6) laptop Dock extras on sol - "Would need to check"; (7) shared Dock and Finder settings - "Yes, I want identical on both except where an app is not on both, but even then the place where it would be is consistent - so one order but items might be machine specific"; (8) undeclared software - "Lets capture and decide"; (9) unprofiled new machine - "Don't understand" (to explain).

## Decision 14 (2026-10-09)

- Kris: unprofiled new machine - "Yes, stop and ask". Spark - "Both should be Spark Desktop I guess!" (both machines move to Spark Desktop). Tailscale on sol - listed under Open at Login ("Yes, its in that list"); in-app start-on-login cannot be set and Tailscale is not under Allow in the Background; restart behaviour untested.

## Decision 15 (2026-10-09)

- Kris: (1) apply the four 1Password-backed targets on sol "after 1password changes have finished on my laptop"; (2) App Store on sol - "done" (signed in); (3) delivery of DOTFILES-UE-075 per-machine Rig profiles - "approved"; (4) GitHub key for sol over SSH - "no, its still me so Im happy to use my key for it" (pulls on sol stay on screen); (5) push this thread's three chezmoi commits (4812d81, ed3a669, 42c3fcb) - "yes"; (6) Project note update - asked "update it to what?".

## Decision 16 (2026-10-09)

- Kris: item 6 - "Yes" to the proposed mac-studio-bootstrap Project note wording (sol = Kris own hardware built by Rig and chezmoi studio-on-core; exempt remote agent host under KI-ARCADIA-GOV-033 administered over Tailscale and SSH with Kris approving each step; Techne may deploy onto it but never owns its build; separate from Techne agent-host; FileVault reboot needs Kris approval; 1Password and GitHub pulls on sol screen). GitHub key: happy with no 1Password SSH agent if sol reads the key from where it is stored on the machine (fix to be proposed). Spark: wants the old Spark removed, only Spark Desktop installed.

## Decision 17 (2026-10-09)

- Kris: (1) laptop rigProfile=laptop set - "done"; (2) DOTFILES-UE-075 - "accept and push"; (3) prepare a newer Rig release for sol - "agreed" (prepare only; publishing to the tap is a separate go); (4) GitHub key copy to ~/.ssh on sol - "yes", and build it into chezmoi so it happens automatically; (5) Project note - "yes", swap the record IDs for GDR-KI-ARCADIA-004 and describe the profiles without the record ID; (6) Kris has edited DOTFILES-UE-079 (uncommitted, in the working tree) and asked what "leave" means.

## Decision 18 (2026-10-09)

- Kris: happy with the Decision 17 actions. DOTFILES-UE-079: once the add and remove decisions have been acted on, revisit the items marked "leave" as a subset and decide again. Fold this into the checkpoint and the record when the record is next touched.

## Decision 19 (2026-10-09)

- Kris: "Yes, publish and push." (1) Publish Rig v0.5.0 per RIG-DIST-010 and the tools-rig release guide: push tools-rig main (5d4d8e5..a0cafaa, six commits, this thread), tag, GitHub release, Homebrew tap update; then rollout continues (Rig upgrade on sol over SSH under Decision 1). (2) Push chezmoi up to 49e43e1: a792902, 9685af8 (other sessions, approved), 2cf5403, bde824d, 0761e83, 49e43e1. Not d2500e6 (a newer other-session commit, not covered). Kris: "it is with you to get this rolled out", then report only what is left.

## Decision 20 (2026-10-09)

- Kris: "Repoint the links to DOTFILES-UE-075 and DOTFILES-UE-080 in your checkpoint (and UE-062s link to UE-075) so both done records can be pruned, then prune them." Approval to prune exactly DOTFILES-UE-075 and DOTFILES-UE-080 through ki-accept.

## Decision 21 (2026-10-09)

- MARK 2026-10-09 23:25 CEST (Kris asked for a mark; next time "summary since the mark" = everything after this entry). Open Needs-you at the mark: (1) rig.chezmoi checkpoint line 23 links pruned DOTFILES-UE-075 - other thread repoints or Kris lets this thread do it; (2) push chezmoi c47059e+eeaa891, tools-rig de4fdee, arcadia checkpoint commits - after (1); (3) on sol screen: chezmoi pull, rigProfile=studio, diff, apply, rig apply --dry-run, rig apply; (4) is the laptop 1Password work finished (decides full apply incl. the four 1Password files on sol); (5) adopt and accept RIG-DIST-010 once sol runs Rig; (6) then this thread: ki bootstrap, ki doctor, SSH pull check on sol; (7) restart test with Kris at sol (Tailscale relaunch); (8) DOTFILES-UE-079: commit Kris edits, act on add/remove, then revisit leave items (Decision 18); (9) adopt RIG-CORE-042 (per-machine Dock) and RIG-CORE-041 (unwanted-software removal)?; (10) later: NordVPN, six untrusted taps, Command Line Tools update, tailscaled swap.

## Decision 22 (2026-10-10)

- Kris: (1) rig.chezmoi checkpoint line 23 broken DOTFILES-UE-075 link - "do as recommended": this thread repins that one link to the pinned permalink (one-off, the other thread own checkpoint). (2) On sol, 1Password prompts for Touch ID with no Enter password option, blocking the apply; asked how to stop it and whether it is the service vault.

## Decision 23 (2026-10-10)

- Kris: "can the sudo and password stuff above be added somewhere for future reference?" Approved: add a new-machine / long-apply section to the chezmoi user guide docs/guides/user/macos-workstation.md (rigProfile init, apply order, 1Password Touch ID over Screen Sharing, sudo keep-alive, temporary sudoers timeout and its removal, self-updating apps such as OneDrive).

## Decision 24 (2026-10-10)

- Kris: "yes, lets get it as an improvement for rig" - capture a tools-rig record for self-updating applications (per-tool flag such as updates = "self", default from Homebrew auto_updates; install only when missing, present = satisfied regardless of version or source, rig upgrade skips, doctor flags only missing), with OneDrive on sol as the prompting example.

## Decision 25 (2026-10-10)

- Kris: "yes to all": (1) tools-rig self-updating apps record (already launched as rig-self-updating); (2) capture a chezmoi record so templates that look up a not-yet-installed tool (mcporter obscura via output "which") warn and skip rather than fail the whole apply; (3) hand the 1Password service-account option (a service account scoped to the Rig vault so chezmoi applies need no unlock prompt, enabling unattended applies on sol over SSH) to the rig.chezmoi thread - add it as a handoff item in its checkpoint Open questions; that thread owns priority and design.

## Decision 26 (2026-10-10)

- Kris: chezmoi apply on sol (full, including the four 1Password targets) finished without errors after the second rig apply. Proceed with the approved remaining steps (Decision 1 work in hand): ki bootstrap, ki doctor and the SSH pull check on sol.

## Decision 27 (2026-10-10)

- Kris: "fix what you can please" - approval to fix the sol rig apply failures and the ki doctor findings that an agent can fix over SSH: adopt already-present casks with brew install --cask --adopt, rerun rig apply on sol scoped to the failed items or in full, and fix doctor findings within sols own user setup. Excludes sudo, reboot, uninstalling apps, downgrading self-updated apps (OneDrive), on-screen approvals, and anything touching other machines or remote services.

## Decision 28 (2026-10-10)

- MARK 2 2026-10-10 17:37 CEST (Kris: "we can probably take a mark"). "Summary since the mark" = everything after this entry. See the Needs-you list in this thread reply at the mark; checkpoint to carry it.

## Decision 29 (2026-10-10)

- Kris at sol: brew --adopt of readdle-spark slack ticktick failed (TickTick App Store copy, macOS Operation not permitted); advised adopting only readdle-spark and leaving App Store copies (Slack, TickTick, DaisyDisk, WiFi Explorer) for RIG-CORE-043. ssh-add --apple-use-keychain worked; verified from an SSH session that sol authenticates to GitHub, so agent ssh -A forwarding (item 5) is not needed. Insta360 not tried yet.

## Decision 30 (2026-10-10)

- Kris: "Make sol match the laptop - yes!" Swap Slack, TickTick, WiFi Explorer (App Store copies on sol) and Spark Desktop (hand-installed; adopt blocked by App Management) to Homebrew by Kris deleting the copies at sols screen and running rig apply; Telegram switched from the cask to the App Store copy (brew uninstall --cask telegram, then rig apply); DaisyDisk keeps its App Store copy (licence); Insta360 cleaned with the two sudo commands in the same pass.

## Decision 31 (2026-10-10)

- Kris: (4) "yes" - switch sol to released ki (ki dev local off, ki bootstrap, ki doctor) over SSH. (6) asked what DaisyDisk is on the laptop: App Store copy also tracked by Homebrew, so sol keeping its App Store copy matches. (8) "yes" - fix Rig settings: architecture-aware artifact paths for beyond-compare, gitup, ollama; observatory launch agent follows mise bun rather than a fixed 1.4.1 path; and install Observatory on sol (clone apps-observatory to ~/workspaces/kit/knowledgeislands/apps-observatory).

## Decision 32 (2026-10-10)

- Kris: (1) will send the rig apply summary and sign back in; (2) RIG-DIST-010 "accepted" - accept through ki-accept; (3) "please do, and apply chezmoi" - push the local commits in chezmoi, tools-rig and ki-arcadia-principal, and apply chezmoi (on sol over SSH after pull, and the laptop), after rig-settings-fix lands; (4) close the Project only when everything is done fully; (5) restart test Monday evening at the earliest. Kris asked whether Rig needs to learn about the App Store conflicts and sudo removal of installed apps.

## Decision 33 (2026-10-10)

- Kris: "all are agreed, do what you can and then keep a track of those I need to do". (1) Declare DaisyDisk as an App Store app in Rig (licence), both machines; never uninstall the laptop Homebrew record. (2) OneDrive on sol: Kris deletes it with sudo and reruns rig apply (Kris action). (3) Widen RIG-CORE-043: doctor reports an app installed from a different source than declared and shows the swap steps, never deleting automatically. (4) Remove the stale ki runner on sol (~/.local/bin/ki, ~/.local/bin/.ki-local-runner, and the ki.1 man link only if it points into a tools-ki checkout). (5) HNR harness on sol: no answer given, so no change; stays open for Kris. (6) Delete the parked folder ~/.local/state/ki/parked/ki-agentic-harness.july-layout on sol. (7) Restart test Monday evening at the earliest. Also investigate the archify and caveman provenance-missing findings read-only, and keep the Kris to-do list in the checkpoint. Agent rig-followups runs after accept-dist-010 and before push-and-apply; SSH to sol allowed, no other remote calls, no push.

## Decision 34 (2026-10-11)

- Kris: (2) "done" - HNR harness kept on sol; verified sol ~/.config/ki/config.toml matches chezmoi and lists hnr-agentic-harness. (3) "yes" - GitHub from remote SSH sessions on sol via agent forwarding from the laptop, for the sol host only. (4) "yes" - make XDG_STATE_HOME (and the other XDG base dirs) available in non-interactive login shells so rig doctor over SSH sees skills provenance. (6) "RIG-DIST-010 - yes" - prune RIG-DIST-010, repointing inbound links to a pinned permalink first. Also correct the observatory target to service:observatory in the checkpoint. Agent sol-final-fixes; local commits only, no push; SSH to sol allowed for verification.

## Decision 35 (2026-10-11)

- Kris: (1) "yes, push as you need to" - push the local commits in chezmoi, tools-rig and ki-arcadia-principal, then apply chezmoi on sol over SSH once Kris's running rig apply on sol has finished. (2) Restart test: Kris does it at sol on Monday evening; do not remind before then; keep the Project open until the restart is proven. (3) Move the longer-term items now so the restart test is the only thing left: hand RIG-CORE-041, RIG-CORE-042, RIG-CORE-043 and DOTFILES-UE-079 (act on add and remove, then revisit leave) to the Rig Initiative; DOTFILES-UE-082 and the 1Password service account to the rig.chezmoi thread; the Later items (NordVPN, six untrusted taps, Command Line Tools update, tailscaled swap) to the Rig Initiative. (4) The cheztoi vega host manifest not listing .zshenv belongs to another project: hand it off to its owning thread. Agent handoff-and-push, --rules push.

## Decision 36 (2026-10-11)

- Coordinator, under Decision 35 ("the other longer-term items can move now"; "push as you need to"): applied ~/.ssh/config and ~/.zshenv on the laptop (agent forwarding verified from sol). Agent repoint-projects repoints the project field of RIG-CORE-041, RIG-CORE-042, RIG-CORE-043, DOTFILES-UE-079 and DOTFILES-UE-082 away from mac-studio-bootstrap to the Rig Initiative (or the rig.chezmoi owner for DOTFILES-UE-082) per each repository's conventions, and pushes chezmoi and tools-rig. Arcadia push waits for Kris because three other-thread commits sit under ours.

## Decision 37 (2026-10-11)

- Kris: "yes to the pushes" - push chezmoi and ki-arcadia-principal main including the other threads' unpushed commits beneath ours (chezmoi: two DOTFILES-UE-083 macOS-settings commits; Arcadia: island-model-and-tending 97958a2, 0ee2995 and state-of-play 58a5c3c). Agent push-final, --rules push.

## Decision 38 (2026-10-11)

- From state-of-play (2026-10-11), relayed by Kris: (1) add a host table as a note (not a roadmap record) in the mac-studio-bootstrap Project: vega / agent-host / Ubuntu; sol / studio / macOS; terra / laptop / macOS; Rig profiles (core, laptop, studio) and the cheztoi host profile (--host, target_host) take their names from it; Omarchy is a separate future idea for vega in the agent-host Project. (2) Convert the checkpoint mark to the KI-HARNESS-GOV-169 form: one line in ## Current state, "Mark: <UTC timestamp>, decisions log at Decision <N>"; Mark 2 = 2026-10-10T15:37Z, Decision 28; re-read ki-delegation once KI-HARNESS-GOV-169 lands. Also fold in: Kris handed the op_cache race, the run-every-apply copy-key script, DOTFILES-UE-082, DOTFILES-UE-084 and the 1Password service account to the rig.chezmoi thread; sol rig apply now fails only on Warp (cask checksum mismatch upstream, app intact, RIG-CORE-043). Agent hosts-and-mark; push approved under Decision 37 for its own commits.

## Decision 39 (2026-10-11)

- Kris: make sure the checkpoint is really tidy; say where the decisions log lives whenever it is cited. Agent checkpoint-tidy rewrites rig.mac-studio-bootstrap to a lean current-state record, adds the decisions log location, pushes its own commit.

## Decision 40 (2026-10-11)

- Kris: "take a mark at this point" - strike a new mark after the recap; it replaces Mark 2 (Decision 28).

## Decision 41 (2026-10-11)

- Kris: the decisions log should be in the Project, or at least linked from it. Coordinator recommendation adopted: the run log stays machine-local (ki-delegation: run state is non-durable; in-force decisions are consolidated into their durable owner), so the Project note gains a short section of the in-force decisions plus where the full log lives. Kris also: `open` on a file path or URL opens Markdown in Obsidian; Kris is moving off Obsidian and wants Zed (dev.zed.Zed). Capture a tools-rig triage record, Rig Initiative, for declaring default apps per file type on every machine (Markdown to Zed), since Rig has no such feature; Kris sets the laptop by hand meanwhile. Agent project-decisions, --rules push for its own commits.

## Decision 42 (2026-10-11)

- Kris: "ZED-MD, yes, add that capability to the roadmap for rig. You can also make the change directly now for me." Coordinator sets Markdown to open in Zed on the laptop (and on sol over SSH) through Launch Services, no new installs; the Rig capture is already running in project-decisions.

## Decision 43 (2026-10-11)

- Kris: summaries need a banner like the recap header, including when a thread reaches a stop point (largely done or waiting on something), whether given on request ("summary") or proactively. Update the canonical ki-delegation background-run standard in ki-agentic-harness to cover this, same approach as the recap header; then tell Kris so he can update the state-of-play thread. Agent summary-banner, --rules push for its own commits.

## Decision 44 (2026-10-12)

- Kris (re-bootstrap 2026-10-12, at home): run the RESTART test on sol now (Kris restarts and unlocks FileVault in person) and the sol Keychain handoff (Kris stores the Automation service-account token in sol login Keychain; coordinator then fast-forwards sol chezmoi source over SSH and proves op_cache renders with rm -rf ~/.cache/op-cache && chezmoi diff). Reboot approved for this test only.

## Decision 45 (2026-10-13)

- Kris (2026-10-13): Screen Sharing, Universal Control and Handoff should be managed by Rig, and where possible on other operating systems too (screen sharing at least); everything discussed about remote access needs writing in the guides in the right place. Coordinator: capture one tools-rig triage record (Rig Initiative) for declarable remote-access and device-continuity settings, with screen sharing reachable only over the tailnet; and write a remote-access section in the chezmoi macOS workstation guide. Agent remote-access-docs, --rules push for its own commits, fast-forward only.

## Decision 46 (2026-10-13)

- Kris (2026-10-13): the RESTART on sol also upgrades it from macOS 26 Tahoe to macOS 27 Golden Gate, so the restart takes longer. After it is back: confirm Tailscale reconnects, then check sol on macOS 27 (sw_vers, rig doctor, chezmoi status) before closing the Project.

## Decision 47 (2026-10-13)

- Kris: KEYCHAIN-SSH hand to rig.chezmoi (handoff written into its checkpoint); FIREWALL-NOW wait for Rig (KI-TOOL-RIG-CORE-046), no change to sol now.

## Decision 48 (2026-10-13)

- Kris: "FIREWALL: B" - build the tailnet-only Screen Sharing firewall properly in Rig now, not as a hand fix on sol. Coordinator: a background agent splits the firewall slice out of KI-TOOL-RIG-CORE-046 into its own tools-rig record (Rig Initiative), adopts it and plans it to Ready, then stops for Kris to approve the plan; build follows only after that approval. Read-only SSH to sol allowed for evidence (pf, Screen Sharing state on macOS 27). Tell the tools-burndown thread. Agent firewall-plan, --rules push for its own commits, fast-forward only.

## Decision 49 (2026-10-13)

- Kris (2026-10-13 ~00:55 CEST), after the coordinator restated the plan: "we can at least accept what has been suggested ... ironed out for getting on with it". Approves KI-TOOL-RIG-CORE-047 plan (FW-PLAN approve; FW-SHAPE yes; FW-MATCH yes; FW-PERSIST yes, no periodic re-load yet; FW-DOCTOR yes; FW-LINUX yes, later record). Record moves to Ready and fixture-backed delivery through ki-implement to Awaiting review is authorised; live acceptance on terra/sol, personal declaration, acceptance and prune are NOT authorised. Agent firewall-deliver, --rules push for its own commits, fast-forward only.

## Decision 50 (2026-10-14)

- FW-PROFILES: Kris chose both Macs (laptop and studio). Live acceptance of KI-TOOL-RIG-CORE-047 starts on terra once delivery is reviewed; sol follows. Agent-host firewall question open (AGENT-HOST-FW).

## Decision 51 (2026-10-14)

- AGENT-HOST-FW: Kris approved a Linux firewall provider in tools-rig, Next horizon, planned to Ready and delivered now (fixtures only), plus a ki-techne-harness roadmap item for the agent-host recipe to declare it. No live apply on the agent host (Techne Programme Hold).

## Decision 52 (2026-10-14)

- From Master: state-of-play (Decision 158, Kris 2026-10-14): the roadmap has grown about 50% since last measured. Standing focus: burn it down. Create no new feature records and do not widen scope; capture only blockers, defects or items Kris asks for, and prefer closing, merging or rejecting existing records.

## Decision 53 (2026-10-14)

- Kris: go for all recommendations. FW-REVIEW approve KI-TOOL-RIG-CORE-047 and ADR-KI-TOOL-RIG-009 (closure through ki-accept after the live test passes). FW-LIVE approve, terra first then sol; a background agent prepares the chezmoi firewall entry for both Macs and the terra steps first. TERRA-VNC Kris turns it on just before the test. OBS-KICK restart the Observatory on sol. CLOSE-OUT keep the Project open until the firewall is live on sol and the SSH token fix lands. BURNDOWN-NOTE Kris pastes. SSH-ALIAS yes, chezmoi triage record. DROPBOX leave. WARP leave. ZED-MD later.

## Decision 54 (2026-10-14)

- Kris: FW-LIVE at terra now, walk through it. TERRA-VNC on during the test. FW-CHEZMOI move private_56-firewall.toml out of the chezmoi source into the run folder until the release. FW-RELEASE approve asking state-of-play for a tools-rig release after terra passes. SOL-LAYOUT approve full mgit move on sol (Git fetch and clone from GitHub on sol over SSH allowed for this), old folders kept, dirty tools-mgit left for Kris. DOCTOR-WORKDIR capture a tools-rig triage record. FW-LINUX-REVIEW approve KI-TOOL-RIG-CORE-051 and ADR-KI-TOOL-RIG-010 (acceptance waits for a live Linux test).

## Decision 55 (2026-10-14)

- Re-bootstrap request from Master: state-of-play, on Kris's instruction (2026-10-14). Kris has seen threads regress after compaction (lost owner report, tool chatter) and the Headroom proxy was down 08:49-09:46 BST, so messages may have failed with "connection refused".

1. Re-read the ki-delegation skill (owner report, quiet level, background runs) and your own checkpoint now.
2. Add a short "Thread working rules" block to your own checkpoint (role, owner-report shape, quiet level, minimal visible tool use and outcomes only, standing rules) and re-read it after any compaction. Touch no other thread's checkpoint.
3. Recover anything missed: review your user messages since 08:45 BST and your run's decisions log, and act on anything unanswered or interrupted.
4. Standing rules now in force: burn the roadmap down, no new feature records (Decision 158); you may push other threads' committed work beneath yours when checks pass, naming it (Decision 165); connection-critical changes need a tested restore path (Decision 169); follow-up releases stop and ask first.
5. Then give Kris one owner report.

## Decision 56 (2026-10-14)

- Kris (2026-10-14 ~11:15 CEST): sol is an active development machine, so the KI tools on it should run in local mode from the repository checkouts (changes on the machine take effect at once; updates come from pulling the repositories, not brew upgrade); the agent host stays a stable, release-channel host. Coordinator: a background agent surveys how each KI tool is installed on sol and terra and the local-mode route each offers, read-only, and proposes a plan for Kris (folds in SOL-MGIT-LINK and SOL-MCP-BUILD); no changes yet. Kris also reports sol's displays never sleep (lock screen stays on); coordinator found Amphetamine and Universal Control holding display-sleep assertions.

## Decision 57 (2026-10-14)

- Kris (2026-10-14 ~12:10 CEST), replying to the local-mode report: SOL-DISPLAY concluded (Kris adjusted settings on both Macs). LOCAL-TERRA: both Macs. LOCAL-RECORD: create one triage record in the chezmoi source repository. SOL-BUILD-NOW: approved - on sol, fast-forward clean main checkouts, bun install the tool checkouts, build the eight MCP servers, link ki, rig, mgit, techne and git-almanac into ~/.local/bin, turn on ki dev local, restart mcporter, run rig doctor; Homebrew stays as fallback; no commits. RIG-UPDATE-SOURCE widened into release channels: the agent host is on a stable channel (official tagged releases only); sol and terra are on a dev channel and keep their source checkouts in sync by regularly pulling main (pull only, never push), so changes on main reach every dev machine; this channel model goes into the chezmoi record and is surfaced to Kris before implementation. DIST-011-HOST: fix KI-TOOL-RIG-DIST-011 directly (terra is the laptop, vega the Linux host), committing by path and pushing with any other thread's committed tools-rig work beneath named. SOL-OLD-TREES widened: reconcile every old tree under sol's ~/workspaces/kit and ~/workspaces/hnr against GitHub and the new layout so nothing is lost and anything left makes sense; extend sol to cover the Knowledge Islands, kit and hnr territories as on the laptop; first run is fetch and report with a tidy plan, no push, no deletion, nothing changed in hnr-org. FW-LIVE: real Screen Sharing sol to terra works; Kris does not want to restart terra - coordinator to explain and offer the rule comparison now with the boot check deferred.

## Decision 58 (2026-10-14T13:59:10Z)

- Kris (2026-10-14 ~12:10 CEST): deleted Telegram from Applications by hand and ran rig upgrade, which reported planned=0 completed=26 failed=84 unavailable=0; asked whether something is set up wrong on that machine. Coordinator: a read-only background agent diagnoses the failures on sol (and terra if that was the machine), no fixes. Kris also asked how to move coordination threads to another host (Zed on sol); coordinator answers with a proposal, nothing launched for it.

## Decision 59 (2026-10-14T14:00:02Z)

- Kris (2026-10-14 ~16:00 CEST): the Mac Studio does not have Zed on the Dock. Coordinator: queue a read-only check after the rig-upgrade diagnosis.

## Decision 60 (2026-10-14T14:16:39Z)

- Kris (2026-10-14 ~16:15 CEST): this thread now completes one thing only - getting sol ready to take this coordination work (Rig installed fully, Claude Code set up, a machine bootstrap of whatever another host needs to take work, Zed configured with Claude and Codex agents through chezmoi); everything else is put on hold and parked in the checkpoint. Moving a thread to another machine: drain only what is already running; queued work is pushed back into the checkpoint, and the next machine re-queues it from the checkpoint on start. This thread deals with that rule directly: capture it as a handoff to the ki-pmo owner rather than asking Kris to paste it.

## Decision 61 (2026-10-14T14:21:59Z)

- Kris (2026-10-14 ~16:30 CEST): SOL-CLT - Kris is installing the Command Line Tools on sol now. SOL-TELEGRAM - 'I thought you said to delete it!' (the earlier sol-fix advice was to remove the Homebrew cask copy, then install Telegram from the App Store as on the laptop; the reinstall step remains). Kris: 'I think it's going to be important to have the rig site on midnight ninja up to date so I can see how Rig is available on different hosts.' Coordinator: a read-only background agent surveys the Rig site (apps-rig.midnight.ninja), what it shows now, how it is built and published, and what it would take to show Rig's availability per host; no deploy without Kris.

## Decision 62 (2026-10-14T14:23:32Z)

- Kris (2026-10-14 ~16:25 CEST): 'you can park SOL-TELEGRAM and SOL-CLT, so I can pick it up once we have moved over.'

## Decision 63 (2026-10-14T14:27:03Z)

- Kris (2026-10-14 ~16:35 CEST) pasted a Claude error from sol, 'API Error: Connection refused - a firewall or proxy may be blocking it (ECONNREFUSED)', and said 'It's headphones not working on Sol' (read as Headroom). Coordinator check: terra's Claude settings send Claude through the Headroom proxy at 127.0.0.1:8787; on sol the headroom binary exists but no Headroom service is loaded and nothing listens on 8787. Coordinator: a read-only background agent finds why and gives the exact fix; no change on sol without Kris.

## Decision 64 (2026-10-14T14:32:04Z)

- Kris 2026-10-14 16:31 CEST: 'OLD-TREES - Can you give me a command to run that will do it?' OLD-TREES comes off hold; Kris runs it himself at sol. Coordinator supplies a reversible command (move the old kit/ and hnr/ trees into a dated holding folder, no deletion, orphans kept inside it) and drops the two ki-delegate skill links.

## Decision 65 (2026-10-14T14:34:20Z)

- Kris 2026-10-14: 'HEADROOM-NOW - this is working, which is great'. Headroom deployed on sol by hand with install apply (init-user profile, port 8787); Claude Code on sol works through it.

## Decision 66 (2026-10-14T14:35:12Z)

- Kris 2026-10-14: 'So I'm thinking I can hand off the rest of this to Sol now. In which case, we need to take a mark, and do it'. Approved: take a new mark, fold all open queries and pending reports into the checkpoint, commit and push it with the thread folder, copy the run's decisions log and reports to the same path on sol over SSH; terra's thread then stops and sol resumes from the checkpoint.

## Decision 67 (2026-10-14T14:55:13Z)

- Kris 2026-10-14: 'OLD-TREES-RUN - I've moved them into ~/workspaces/_old'. Done by Kris at sol: kit, hnr and knowledge-wayfinder now sit in ~/workspaces/_old (not the proposed _retired-old-trees-2026-10-14). The dead ki-delegate and ki-design-loop skill links remain and fold into SOL-AGENT-FIX.

## Decision 68 (2026-10-14T15:03:48Z)

- Kris 2026-10-14: 'ok - done up to 9'. SOL-SCREEN done at sol's screen: steps (a)2-(a)9, (a)1 skipped while SOL-CLT is held. Step 4 confirmed by 'op vault list' (op whoami still reports not signed in under app integration). Step 6 applied ~/.claude and ~/.config/zed only: ~/.codex fails in the codex-trusted-projects-json template because a dot_mgit.toml manifest lacks groups.default (CODEX-GROUPS, not yet approved); Codex not checked.

## Decision 69 (2026-10-14T15:07:22Z)

- Kris 2026-10-14: 'ok - so can I leave it to you to get this rig up and running? I want to capture any differences and also make an onboarding guide for a rig'. Approved: SOL-AGENT-FIX and CODEX-GROUPS diagnosis run now on sol (fetch allowed, no commits or pushes, CODEX-GROUPS proposes only); then capture the differences (SOL-RECORDS, local commit only, no push) and draft a Rig onboarding guide in the thread folder; its permanent home is put to Kris.

## Decision 70 (2026-10-14T16:35:11Z)

- Kris 2026-10-14: 'CODEX-GROUPS - approved: commit the dig-based line-23 fix in the chezmoi source locally, then chezmoi diff and apply ~/.codex, ~/workspaces and ~/.config/rig/conf.d/40-macos.toml on sol; add a template render check to pre-commit' / 'SKILLS-CONFIG - approved: in the chezmoi ki config replace ki-design-loop with ki-pmo-design and add ki-pmo, commit locally, apply ~/.config/ki/config.toml on sol, then ki repair --apply and ki doctor' / 'OLD-SOURCE-DIRS - remove the six stale OneDrive source entries from sol's Claude settings (with NO backup)' / 'RIG-GUIDE-HOME - move the guide to docs/guides/user/setup-mac-rig.md in the chezmoi repository, link it from macos-workstation.md in place of "Set up a new machine", commit locally under KB-DOTFILES-UE-090' / 'RIG-RECORDS - capture R1 (Command Line Tools doctor check) and R3 (interpreter port owners) as tools-rig triage records; note R2 and R4 in the mac-studio-bootstrap Project note' / 'TOOL-RECORDS - capture K2 (footer follows authority tier) and K3 (no reused run names) as tools-ki triage records; leave K1, K4 and M1 with SKILLS-CONFIG, SOL-REGISTRY and MGIT-PRESEED' / 'SOL-DOCK-ZED - prioritise KI-TOOL-RIG-CORE-042, use it to verify rather than manual change' / 'SOL-DOCK-EXTRAS - same order as the laptop, filtered by what each profile selects' / 'RIG-SITE-REFRESH - do it' / 'RIG-SITE-HOSTS - capture KB-MIDNIGHT-RIG-SITE-001 for the declared view only' / 'RIG-SITE-HOSTNAMES - hostnames and roles'. Coordinator: three agents by repository: chezmoi-fix (chezmoi + sol), tool-records (tools-rig, tools-ki, Project note), midnight-site (apps-midnight.ninja). Local commits only, no pushes.

## Decision 71 (2026-10-14T16:47:29Z)

- Kris 2026-10-14: 'HANDED-OVER-DONE - add to KI-HARNESS-GOV-189: a thread instance left behind after a host move closes with a DONE state once the handover has pushed, with no resume line and a pointer to the host that took over; my words 2026-10-14 "we do sometimes need done, not just rest and busy"'.

## Decision 72 (2026-10-14T16:47:29Z)

- Kris 2026-10-14: 'SOL-FOLD - record my 2026-10-14 remit addition "I want to add to this projects remit that it needs to look at the rig differences"; take a new mark adding RIG-DIFF (read-only comparison of Rig profiles, tools, skill links, Dock extras and undeclared set-up such as Headroom on sol against the laptop, then settle each difference), SOL-SCOPE (manage all seven groups; take SOL-REGISTRY off hold, register after a dry-run against the laptop's 52 entries) and LOCAL-MODE-CHECK (re-run ki dev local on if config.toml no longer shows in chezmoi status)'. Coordinator: RIG-DIFF and SOL-SCOPE+LOCAL-MODE-CHECK queued behind chezmoi-fix (it is changing sol's chezmoi and ki config now); read-only SSH to terra for the comparison; settling differences comes back as queries.

## Decision 73 (2026-10-14T17:53:40Z)

- Kris 2026-10-14: 'SOL-APPLY - I'll run it at sol: chezmoi apply 10-applications.toml, rig apply --dry-run (Telegram and SVG handler only), then rig apply, signed in to the App Store' / 'PUSH-ROUND - done' / 'MIDNIGHT-PUSH - push apps-rig.midnight.ninja once terra's checkout is confirmed level' / 'SOL-REGISTRY-DIFF - register sol's 51 now; settle terra's extra entry with TERRA-READ' / 'DOCK-CONSUMER - capture the KB-DOTFILES record for the core Dock with tool links, including chatgpt-classic -> chatgpt, chatgpt-current in core, Lightroom Classic after Photos' / 'DOCK-APPLY-SOL - I run the sol acceptance apply myself at acceptance' / 'UE086-AMEND - amend KB-DOTFILES-UE-086 as rig-diff recommends; local commit only' / 'UE086-SOL-PASS - do UE-086 section C plus mise prune in the same sol session as SOL-CLT' / 'AUTOUPDATE-REMOVE - approved: brew autoupdate delete and untap domt4/autoupdate on sol' / 'TERRA-READ - run the read-only terra evidence pass from terra's next session and append it; leave Remote Login off' / 'RENDER-HOOK - keep the render check in the local gate; hooks stay with KI-HARNESS-GOV-117'. Coordinator: sol-chores (registry 51, autoupdate removal) and dock-records (DOCK-CONSUMER, UE086-AMEND) launched; SOL-APPLY with Kris; MIDNIGHT-PUSH and TERRA-READ wait for terra's next session.

## Decision 74 (2026-10-14T19:38:08Z)

- Kris 2026-10-14: 'keep goimng please', in reply to the PUSH-CHECK recommendation. Taken as approval of PUSH-CHECK: after dock-records finishes, an agent on sol rebases tools-ki and ki-agentic-harness onto origin, runs each repository's gate, then pushes chezmoi, tools-rig, tools-ki and ki-agentic-harness from sol; stop on any conflict. apps-rig.midnight.ninja stays unpushed (MIDNIGHT-PUSH waits on terra).

## Decision 75 (2026-10-14T22:58:44Z)

- Kris 2026-10-14: 'in the background, I would like you to fix github desktop by cleaning out the repositories it has and then registering all of the ones from the 8 territories in it'. Approved: on sol, an agent clears GitHub Desktop's repository list and adds every checkout from the eight territories. Coordinator: back up the app's data folder before changing it; local app state only.

## Decision 76 (2026-10-14T23:34:54Z)

- Kris 2026-10-15: 'MIDNIGHT-PUSH-SEEN - a) yes, I pushed apps-rig.midnight.ninja from GitHub Desktop; record MIDNIGHT-PUSH as done at 189928e and have TERRA-READ check that terra's checkout fast-forwards to it' / 'GHD-DECLARE - a) capture a tools-rig triage record for a Rig step that adds every mgit territory checkout to GitHub Desktop through the github shim (add-only, never removes, pauses between opens), and list it as a Rig difference in the mac-studio-bootstrap Project note' / 'GHD-BACKUP - a) I have looked at the new list; an agent on sol deletes ~/Library/Application Support/GitHub Desktop.bak-2026-10-14' / 'UE091-ADOPT - a) adopt KB-DOTFILES-UE-091 now as deliver / Next; plan it to Ready when KI-TOOL-RIG-CORE-042 reaches Awaiting review'. Coordinator: ghd-followup (backup deletion, tools-rig record, Project note) and ue091-adopt (chezmoi) launched in parallel; local commits only.

## Decision 77 (2026-10-14T23:44:42Z)

- Kris 2026-10-15: 'LOCAL-PUSH - a) an agent on sol pulls chezmoi and tools-rig with --ff-only --no-rebase, re-runs each local gate and pushes main in both, leaving chezmoi's dot_gitconfig uncommitted'.

## Decision 78 (2026-10-14T23:46:46Z)

- Thread, 2026-10-15, on Master's RIG-SOL-BREW: leave sol's tools-rig checkout link and the stale Homebrew Rig 0.5.0 formula alone for now, as Master recommends. Master's GATE-FIX and GATE-REMAIN (Kris: reword the two Rig note bullets so they name no records, conform this checkpoint, commit and push from sol) go to a background agent.

## Decision 79 (2026-10-15T00:15:47Z)

- Kris 2026-10-15: 'SOL-CLT - thats been done'. Taken as: Command Line Tools for Xcode 27.0 installed at sol's screen; the agent half of SOL-CLT (brew reinstall pkgconf, rig upgrade) and UE086-SOL-PASS (KB-DOTFILES-UE-086 section C plus mise prune, Kris 2026-10-14) now run; SOL-TELEGRAM checked and reported.

## Decision 80 (2026-10-15T00:16:05Z)

- Kris 2026-10-15: 'even if you are waiting on me, I'm going to need instructions'. Every held item waiting on Kris carries step-by-step instructions in the report.

## Decision 81 (2026-10-15T00:16:51Z)

- Kris 2026-10-15 about 01:20 BST, from sol's screen: 'telegram was successfully installed!' (Homebrew cask).

## Decision 82 (2026-10-15T00:17:51Z)

- Kris 2026-10-15: 'telegram on its own' - SOL-TELEGRAM done (Homebrew cask installed at sol's screen); SOL-APPLY still open (applications file, dry-run and full rig apply, SVG handler).

## Decision 83 (2026-10-15T00:22:40Z)

- Kris 2026-10-15 about 01:21 BST, from sol's screen: rig apply ran alongside sol-clt's rig upgrade and ended 'apply incomplete: status 1 (planned=165 completed=173 failed=9 skipped=68)'. Thread queues a read-only diagnosis after sol-clt.

## Decision 84 (2026-10-15T00:49:05Z)

- Kris 2026-10-15 about 01:45 BST, from sol's screen: re-ran rig apply for the eight cargo tools - 'apply succeeded: status 0 (planned=8 completed=8 skipped=0)'. SOL-APPLY done.

## Decision 85 (2026-10-15T00:52:20Z)

- Kris 2026-10-15 about 01:55 BST: 'I think all the steps are done and I am happy with the recommended options'. Taken as: SOL-TELEGRAM-DIRECTION a) follow the declaration (App Store build via Homebrew mas; Kris reports the steps done, to verify); UE086-SOL-REST a) one session at sol, an agent writes step-by-step instructions first and checks afterwards; APPLY-RUST-ORDER a) add rust to requires for the eight cargo tools in dot_config/rig/conf.d/private_15-command-line.toml, gate, local commit, Kris applies; APPLY-UPGRADE-LOCK a) one tools-rig triage defect record, local commit.

## Decision 86 (2026-10-15T00:58:09Z)

- Kris 2026-10-15 about 02:00 BST: 'telegram sorted' - SOL-TELEGRAM-DIRECTION a) done at sol's screen (App Store build via mas).

## Decision 87 (2026-10-15T00:59:17Z)

- Kris 2026-10-15 about 02:03 BST: 'remote login stay off? nope, happy for it to be on' - Remote Login on terra may be turned on, so sol can reach terra over SSH; TERRA-READ may then run from sol over SSH, read-only.

## Decision 88 (2026-10-15T01:01:08Z)

- Kris 2026-10-15 about 02:05 BST: 'why are 5 apps not in rig then? and why all the brew vs mas for telegram? brew and mas are different, like brew and npm. The old brewfile was where is was wider still'. Thread queues a read-only investigation.

## Decision 89 (2026-10-15T01:05:57Z)

- Kris 2026-10-15 about 02:10 BST: Remote Login on terra turned on and sol's key test returned 'exit 0'. TERRA-SSH done; TERRA-READ now runs from sol over SSH, read-only.

## Decision 90 (2026-10-15T01:11:30Z)

- PUSH-SOL (Kris 2026-10-15 02:1x BST): once rust-order's report confirms its gate, an agent on sol pulls chezmoi and tools-rig with --ff-only, re-runs each local gate and pushes main in both, leaving dot_gitconfig uncommitted

## Decision 91 (2026-10-15T01:37:00Z)

- SOL-GITCONFIG-PUSHED (Kris 2026-10-15): keep f2971fc (dot_gitconfig, "tailscale") as it stands; no further action

## Decision 92 (2026-10-15T01:37:00Z)

- TERRA-HOSTKEY (Kris 2026-10-15): widen KB-DOTFILES-UE-088: add terra's host key line to private_dot_ssh/private_known_hosts and a Host terra block (HostName 100.96.126.29, User krisbrown, no agent forwarding) to private_dot_ssh/private_config, extend the test, gate and commit locally; I apply on each Mac using UE-088's restore path

## Decision 93 (2026-10-15T01:37:00Z)

- SSH-TAILNET (Kris 2026-10-15): keep port 22 outside the KI-TOOL-RIG-CORE-047 firewall as designed; an agent checks on sol and terra, read-only, that SSH refuses password logins

## Decision 94 (2026-10-15T01:37:00Z)

- KEYNOTE-ROUTE (Kris 2026-10-15): option a) (mas info check, App Store route if all three resolve, else catalogue-only with corrected comment and A8 closed), plus: "we don't want adobe photoshop and creative cloud on either, so really we should have it removed from both and also removed from rig"

## Decision 95 (2026-10-15T01:37:00Z)

- MAS-UNDECLARED (Kris 2026-10-15): "keep the decision: PhotoSweeper and Blackmagic Disk Speed Test stay undeclared. But, can you do that now, not wait."

## Decision 96 (2026-10-15T01:37:01Z)

- MAS-PROVIDER (Kris 2026-10-15): "Lets do this now, so its done done." - an exception to the burn-down rule: Rig gets its own Mac App Store provider and the declarations migrate

## Decision 97 (2026-10-15T01:37:01Z)

- TERRA-HARNESS-AHEAD (Kris 2026-10-15): an agent on sol checks read-only whether origin/main of ki-agentic-harness contains 8a453bcd; if not, the next report gives Kris the commands to pull fast-forward and push at terra's screen

## Decision 98 (2026-10-15T01:37:01Z)

- TERRA-CHEZMOI-APPLY (Kris 2026-10-15): "Done and all worked" at terra's screen

## Decision 99 (2026-10-15T01:37:01Z)

- REGISTRY-STORES (Kris 2026-10-15): "I don't follow, the folders are under /Users/krisbrown/Library/CloudStorage/OneDrive-Personal on both machines" - terra-read's 'no sources-* folders on terra' is likely an SSH privacy limit; re-checked read-only, query re-put

## Decision 100 (2026-10-15T01:37:01Z)

- TERRA-CASK-RECORDS (Kris 2026-10-15): "I removed from brew and installed from App Store on both, can you update rig config." (DaisyDisk and UTM)

## Decision 101 (2026-10-15T01:37:01Z)

- FW-VERIFY (Kris 2026-10-15, at terra): pf Status Enabled; the screen-sharing anchor holds the eight tailnet-only rules on port 5900 (lo0, 100.64.0.0/10, fd7a:115c:a1e0::/48, then block, TCP and UDP). terra's firewall rules are proven loaded.

## Decision 102 (2026-10-15T09:25:51Z)

- ADOBE-OUT (Kris 2026-10-15, about 02:50 BST): "Lighthouse Classic can go too" - read as Adobe Lightroom Classic (speech-to-text); with Photoshop and Creative Cloud, every Adobe app comes off both Macs and out of Rig

## Decision 103 (2026-10-15T09:26:24Z)

- Coordinator 2026-10-15 10:27 BST: rig-apps and mas-provider exited without DONE at about 02:45 BST, leaving uncommitted edits in chezmoi and tools-rig; resumed in place under the same authority (KEYNOTE-ROUTE, TERRA-CASK-RECORDS, MAS-PROVIDER, ADOBE-OUT). chezmoi gained 37295bc 'chore(ssh): retain terra host keys' from another session; terra-hostkey re-queued to check it first.

## Decision 104 (2026-10-15T09:32:42Z)

- SSH-TAILNET (Kris 2026-10-15 10:3x BST): widen KB-DOTFILES-UE-088: chezmoi installs /etc/ssh/sshd_config.d/050-ki-key-only.conf (PasswordAuthentication no, KbdInteractiveAuthentication no) through a run_onchange_after_ script that checks with sshd -t first and skips with a message without sudo; test, gate, commit locally; I apply at each Mac's screen with a second login open as the way back

## Decision 105 (2026-10-15T09:32:42Z)

- REGISTRY-STORES (Kris 2026-10-15): "fix them and don't worry about a backup" - bind sol's eight sources stores now

## Decision 106 (2026-10-15T09:32:42Z)

- KI-STORE-TOLERANCE (Kris 2026-10-15): "as a followup, we need to make the tooling more tolerant of errors like this and if anything they should suggest fixes, not just error" - captured as a tools-ki record (explicit owner request, outside the burn-down rule)

## Decision 107 (2026-10-15T09:41:38Z)

- GOOD-STATE (Kris 2026-10-15 10:4x BST): "essentially I'm allowing you to make updates to rig, dotfiles and rig.midnight.ninja to get everything into a good state" - standing authority for local changes in tools-rig, chezmoi and apps-rig.midnight.ninja; pushing, ki-accept and at-screen applies still need Kris

## Decision 108 (2026-10-15T12:18:10Z)

- FAVICONS (2026-10-15 13:2x BST): 'might not be a thing for this but I figured it could be a quick win, can I get better favicons for: <http://localhost:8787/> and <http://127.0.0.1:1675/>'

## Decision 109 (2026-10-15T21:08:39Z)

- AT-SCREEN sol (2026-10-15 13:3x BST): '1. Done' (sudo mas uninstall of PhotoSweeper and Blackmagic Disk Speed Test); '3. Done' (chezmoi apply ~/.config/rig and rig doctor); '4. Done' (HOSTKEY-APPLY on sol).

## Decision 110 (2026-10-15T21:08:39Z)

- ADOBE-SCRIPT (2026-10-15): 'I can't do the Adobe uninstall, can you script this instead?'

## Decision 111 (2026-10-15T21:08:39Z)

- WALKTHROUGH (2026-10-15): key-only SSH '5. Not done yet, can you walk me through it more'; rest of UE-086 '6. Not done yet, walk me through it more'.

## Decision 112 (2026-10-15T21:09:12Z)

- QUERY-CHECK (2026-10-15 22:1x BST): 'then check all the queries are still open'

## Decision 113 (2026-10-15T21:36:01Z)

- RENAME (Kris, 2026-10-15): rename from `mac-studio-bootstrap` to `mac-studio-setup`

## Decision 114 (2026-10-15T22:52:47Z)

- HARNESS-LINK (Kris, 2026-10-15): Yes: an agent changes only the transferred_from value and the link target in KI-HARNESS-GOV-189 (ki-agentic-harness) to ki-principal/Streams/Projects/mac-studio-setup/mac-studio-setup.md and commits that one file locally by explicit path, without pushing.

## Decision 115 (2026-10-15T22:52:47Z)

- LINK-PUSH (Kris, 2026-10-15): Push chezmoi main now (bd04386 is the only commit ahead); tools-rig 0f1aff0 goes with TERRA-ORDER.

## Decision 116 (2026-10-15T22:52:47Z)

- TERRA-ORDER (Kris, 2026-10-15): Yes: an agent pushes main in tools-rig, tools-ki and apps-observatory.local from sol, each after pull --ff-only and its own checks; I then follow the terra steps.

## Decision 117 (2026-10-15T22:52:47Z)

- CORE-059-ACCEPT (Kris, 2026-10-15): Yes: an agent closes KI-TOOL-RIG-CORE-059 as done under ki-accept and commits it in tools-rig locally.

## Decision 118 (2026-10-15T22:52:47Z)

- SITE-PUSH (Kris, 2026-10-15): An agent rebases cef3f96 and e9503fd onto origin/main in apps-rig.midnight.ninja, re-pulls the catalogue on conflict, runs the checks including 550a946's test, and pushes; it stops and reports on a conflict needing a decision.

## Decision 119 (2026-10-15T22:52:47Z)

- SITE-ACTUAL (Kris, 2026-10-15): Yes: an agent removes Actual from the software page, in line with my C7d removal, and commits it locally for SITE-PUSH.

## Decision 120 (2026-10-15T22:52:47Z)

- ADOBE-DATA (Kris, 2026-10-15): Once both Macs have run adobe-remove.sh, an agent proposes a per-folder list for me to approve: delete caches, logs and empty folders; keep every Lightroom catalogue, preset and Photoshop setting; I run the approved deletions at each screen.

## Decision 121 (2026-10-15T22:52:48Z)

- C56-TICK (Kris, 2026-10-15): Yes: an agent ticks C5 and C6 in KB-DOTFILES-UE-086 with today's evidence and commits only the record, locally.

## Decision 122 (2026-10-15T22:52:48Z)

- C8-WORDING (Kris, 2026-10-15): Yes: an agent rewords C8 in KB-DOTFILES-UE-086 to expect Keynote, Numbers and Pages catalogue-only and DaVinci Resolve present, keeps the Adobe check after C7i, and commits only the record, locally.

## Decision 123 (2026-10-15T22:52:48Z)

- UTM-SOL (Kris, 2026-10-15): At sol I quit UTM, run brew uninstall --cask utm, then mas install 1538878817, and check mas list shows it and my VMs open.

## Decision 124 (2026-10-15T22:52:48Z)

- KEYONLY-SKIP-EXIT (Kris, 2026-10-15): Keep exit 1 on a skip, so chezmoi retries until the key-only setting is installed.

## Decision 125 (2026-10-15T22:52:48Z)

- MAS-PUBLIC (Kris, 2026-10-15): Keep mas in the public catalogue as committed in 79d667f.

## Decision 126 (2026-10-15T22:52:48Z)

- OBS-RESTART (Kris, 2026-10-15): I'll run launchctl kickstart -k "gui/$(id -u)/uk.me.kris.rig.observatory" at sol and check the tab at <http://127.0.0.1:1675/> shows the dome.

## Decision 127 (2026-10-15T22:52:48Z)

- HEADROOM-ICON (Kris, 2026-10-15): I'll file a feature request on Headroom's GitHub repository for an SVG favicon on its dashboard and settings pages, attaching favicons-headroom.svg.

## Decision 128 (2026-10-15T22:52:48Z)

- DESK-KIT (Kris, 2026-10-15): I'll buy the recommended bundle: Shure MV7+, RØDE PSA1+ arm, Logitech MX Brio and Kanto ORA, checking each price on the page first.

## Decision 129 (2026-10-15T22:52:48Z)

- RESEARCH-FOOTER (Kris, 2026-10-15): Briefs that need them add: "read-only web search and fetches, git fetch and read-only SSH named in the task are allowed; no sign-in, purchase, posting, push or other remote call".

## Decision 130 (2026-10-15T22:52:48Z)

- SITE-SPARK (Kris, 2026-10-15): Yes: change the line to "Spark Desktop - one mail client on every machine".

## Decision 131 (2026-10-15T22:52:48Z)

- SITE-PRIVATE (Kris, 2026-10-15): Keep 1Password, its CLI and Tower named in the guide.

## Decision 132 (2026-10-16T20:32:35Z)

- PUSH-STACK (Kris, 2026-10-16): Yes, push

## Decision 133 (2026-10-16T20:32:35Z)

- HARNESS-PUSH (Kris, 2026-10-16): Yes, push

## Decision 134 (2026-10-16T20:32:35Z)

- LINK-TEXT (Kris, 2026-10-16): Yes: an agent renames the link text and the Boundary mention in KI-HARNESS-GOV-189 to "Mac Studio Setup Project", leaves the evidence as written, and commits that one file in ki-agentic-harness locally.

## Decision 135 (2026-10-16T20:32:35Z)

- LAUNCHER-FOOTER (Kris, 2026-10-16): Yes: an agent adds a handoff record to the tools-ki roadmap asking that ki agent launch's own rules give way to remote calls a brief names along with an owner approval; tools-ki decides its priority; the record is committed locally.

## Decision 136 (2026-10-16T20:34:36Z)

- SITE-EXTLINKS (Kris, 2026-10-16): links on tools at rig.midnight.ninja are marked as external links but do not open in a new tab... fix that directly please

## Decision 137 (2026-10-16T20:51:56Z)

- FOOTER-RECORD (Kris, 2026-10-16): An agent adds a dated handoff note from Knowledge Islands Principal (mac-studio-setup) to the Discussion of KI-TOOL-KI-CLI-134 with the 15 October evidence and RESEARCH-FOOTER, asking tools-ki to revisit the Boundary so a remote call named in a brief with a quoted approval, or a launch flag, can lift the footer; not blocking; tools-ki keeps priority.

## Decision 138 (2026-10-16T20:51:56Z)

- FOOTER-REBASE (Kris, 2026-10-16): Wait until the tools-ki checkout's rebase is finished and main is clean, then an agent commits only the KI-TOOL-KI-CLI-134 note locally by explicit path, without pushing.

## Decision 139 (2026-10-16T20:51:56Z)

- GOV189-REST (Kris, 2026-10-16): Yes: an agent changes "Mac Studio bootstrap Project" in KI-HARNESS-GOV-189's Context to "Mac Studio Setup Project" and commits the one file in ki-agentic-harness locally.

## Decision 140 (2026-10-16T20:51:56Z)

- GOV189-PUSH (Kris, 2026-10-16): Yes: an agent runs pull --ff-only in ki-agentic-harness, checks only the KI-HARNESS-GOV-189 rename commits are ahead, runs the repo's checks and pushes main.

## Decision 141 (2026-10-17T17:15:18Z)

- THREAD-TIDY (from state-of-play, 2026-10-16/17: MAC-TIDY, CI-RED-PRINCIPAL, THREADS-CLEAR, PMO-7-BACKLOG, on Kris's decisions of 15 and 16 October): clear the thread folder to decisions.md and reports with open queries, home tracked work products, archive spent runtime files, fix PMO-7 and NOTE-1a findings in kept reports.

## Decision 142 (2026-10-17T17:15:18Z)

- HOLD-BRANCH (inbox from state-of-play, 2026-10-15): discard the folded-formatting copy of chezmoi-fix.report.md on origin/hold/2026-10-15/working-state; the report itself is removed under THREAD-TIDY; tell state-of-play.

## Decision 143 (2026-10-17T17:15:18Z)

- AWAITING-REVIEW (Kris via state-of-play, 2026-10-17 14:20 BST): "the owning threads prune KI-PRINCIPAL-ECO-014 and KI-TOOL-RIG-CORE-059." This thread prunes KI-TOOL-RIG-CORE-059.

## Decision 144 (2026-10-17T17:15:18Z)

- RIG-OWNER and RIG-CATALOGUE (Kris via state-of-play, 2026-10-17 14:20 BST): this thread carries the tools-rig burndown lane, starting once SOL-APPLY, SOL-CLT and TERRA-READ are answered; RIG-CATALOGUE captured as an idea only, no record or design until Kris asks.

## Decision 145 (2026-10-17T17:22:37Z)

- GOV195-DUP overtaken (thread, 2026-10-17): ki-agentic-harness ab48fec0 renumbered the thread-folder record to KI-HARNESS-GOV-200; query closed, gov189-finish report removed.

## Decision 146 (2026-10-17T21:33:42Z)

- Kris 2026-10-17 22:33 BST resume line: re-bootstrap and mark; mark moved to 2026-10-17T21:33Z; thread-tidy report deleted at the mark (CORE059-REPORT done, GOV195-DUP overtaken); nothing authorised to restart (FOOTER-RECORD still blocked by the tools-ki rebase).

## Decision 147 (2026-10-17T22:44:22Z)

- 2026-10-17 23:44 BST stock-take: PRINCIPAL-STACK overtaken (another session pushed ki-principal, mark commit on origin); tools-rig now carries 4 other-session KI-TOOL-RIG-CORE-060 commits above the prune, so RIG-PRUNE-PUSH restated as RIG-STACK-PUSH.

## Decision 148 (2026-10-17T22:47:35Z)

- Kris 2026-10-17 23:47 BST: 'Adobe removal dry run: Streams/Projects/mac-studio-setup/adobe-remove.sol.20261017-234633.dry-run.log' - an agent reviews the sol dry run and reports whether the real run is safe, with step-by-step instructions.

## Decision 149 (2026-10-17T22:47:49Z)

- Kris 2026-10-17 23:49 BST: 'I think you're gonna take me through this step by step because there's too much for me just to contemplate all at once and reply to. So let's just go through it step by step. The things you want me to do.' - walk Kris through one item per message, decisions first, then at-screen steps.

## Decision 150 (2026-10-17T22:48:56Z)

- Kris 2026-10-17 RIG-LANE: 'yes' - SOL-APPLY, SOL-CLT and TERRA-READ treated as answered; an agent proposes a tools-rig burndown order, changing nothing; state-of-play told.

## Decision 151 (2026-10-17T22:48:56Z)

- Kris 2026-10-17: 'If there's a question for any step though, can you give me what you recommend and sort of why?' - every step-by-step question carries a recommendation and its reason.

## Decision 152 (2026-10-17T23:01:39Z)

- Kris 2026-10-18 RIG-STACK-PUSH: 'Step 2, leave it' - the tools-rig push is left to the session owning KI-TOOL-RIG-CORE-060; confirm the prune reached GitHub at the next report.

## Decision 153 (2026-10-18T00:41:11Z)

- Kris 2026-10-18 00:46 BST ran the real Adobe removal on sol (ADOBE-RUN, step-by-step walk): apply log clean, 0 failed steps, nothing left under What is left, only the two expected exit 3 boot-outs; next is part 3, restart sol and the final check.

## Decision 154 (2026-10-18T00:45:10Z)

- Kris 2026-10-18: 'I'm going to defer the restarting for now. Maybe remind me another day.' - ADOBE-RUN part 3 (restart sol and final check) held; remind Kris at the next resume.

## Decision 155 (2026-10-18T00:53:05Z)

- Kris 2026-10-18 ADOBE-LOG: 'I'm less worried about the Adobe logs, you can just get rid of everything. And also I don't think we don't have it installed on Terra, so it's all good. Let's have a look at something that's other than Adobe.' - delete the Adobe logs and the answered Adobe thread reports; terra Adobe steps dropped (not installed there); ADOBE-DATA parked, not deleted, since it holds the Lightroom catalogue; script kept for the deferred restart check.

## Decision 156 (2026-10-18T01:20:26Z)

- Kris 2026-10-18 02:19 BST: 'We're going to do some quite big updates for "ways of working". So I think it's probably a good idea for you to wrap up any outstanding points you've got and make sure that you've persisted everything into the checkpoints and the threads.' - drain to a hold; mark 2026-10-18T01:20Z; open queries parked in the checkpoint.

## Decision 157 (2026-10-19T10:04:52Z)

- Kris 2026-10-19 11:04 BST pasted the resume line: hold lifted; re-bootstrap under the work model; run rehomed to +/_WORK/ki.mac-studio-setup; put parked queries back one at a time, ADOBE-RESTART reminder first.

## Decision 158 (2026-10-19T10:09:16Z)

- 2026-10-19 11:20 BST: FOOTER-RECORD overtaken - KI-TOOL-KI-CLI-134 already committed and pushed in tools-ki and has moved on (named --allow grants, 18 October harness handoff); nothing committed; launcher-footer and footer-record reports pruned.

- Kris 2026-10-19 19:00 BST pasted the send line: sent back to its worker since the 2026-10-18T01:20Z mark; re-read, marked at 2026-10-19T18:01Z; FIRST-STEP done and REPORT-SWEEP received (all four reports kept, outcomes not homed); nothing authorised to restart; sent to Kris with ADOBE-RESTART first.

- 2026-10-19 19:40 BST, IMPORTANT REFRESH line from ki.ways-of-working (QUERY-REVIEW; REFRESH-RESUMMARY, Kris 19 October: "I want the other threads to pick it up and resummary me so that I get the better recommendations"): standard re-read; SOL-FW-TEST (low) and PUSH-STACK (medium) sent to one blind review run, query-review, on Codex at high effort; RIG-ORDER (high, not destructive) not reviewed; a fresh Summary follows the report.

- 2026-10-19 19:51 BST, query-review received: the reviewer disagrees on SOL-FW-TEST and recommends Kris restate or confirm it (both views shown); it agrees on PUSH-STACK, now high; the mark commit was already pushed by another session; the brief and report pruned, their outcome homed in queries.md; sent to Kris with a fresh Summary.

- Kris 2026-10-19 19:55 BST: "All three are high confidence to do them." - taken as a) on all three: RIG-ORDER, plan and deliver KI-TOOL-RIG-CORE-063 in the background now, then plan KI-TOOL-RIG-CORE-062 and KI-TOOL-RIG-CLI-027 (chained runs core063, plan062, plan027; local commits in tools-rig, no push); SOL-FW-TEST, Kris restates or confirms it and the entry stays until then; PUSH-STACK, leave the ki-principal push to the next owning session that pushes, which fetches and rechecks first.
