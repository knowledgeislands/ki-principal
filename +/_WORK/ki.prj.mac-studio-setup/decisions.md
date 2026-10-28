# Decisions

- Kris (2026-10-13): the RESTART on sol also upgrades it from macOS 26 Tahoe to macOS 27 Golden Gate, so the restart takes longer. After it is back: confirm Tailscale reconnects, then check sol on macOS 27 (sw_vers, rig doctor, chezmoi status) before closing the Project.

- BURN-DOWN (Kris, 2026-10-14): standing focus, burn the roadmap down; no new feature records - [ki decisions](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/decisions.md).

- FW-PROFILES, FW-REVIEW and FW-LIVE (Kris, 2026-10-14): KI-TOOL-RIG-CORE-047 live on both Macs, terra first then sol, closed through ki-accept after the live test passes - [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md).

- Kris (2026-10-14): CLOSE-OUT keep the Project open until the firewall is live on sol and the SSH token fix lands. ZED-MD later.

- Kris (2026-10-14): FW-CHEZMOI move private_56-firewall.toml out of the chezmoi source into the run folder until the release. FW-LINUX-REVIEW approve KI-TOOL-RIG-CORE-051 and ADR-KI-TOOL-RIG-010 (acceptance waits for a live Linux test).

- Kris (2026-10-11): "ZED-MD, yes, add that capability to the roadmap for rig. You can also make the change directly now for me."

- LOCAL-MODE (Kris, 2026-10-14): sol is an active development machine, so its KI tools run in local mode from the repository checkouts, on the dev channel; the agent host stays on the stable channel - [PERSONAL-DOTFILES-UE-089](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/PERSONAL-DOTFILES-UE-089-ki-tool-release-channels.md).

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

- 2026-10-19 23:45 BST, core063 received: KI-TOOL-RIG-CORE-063 at Awaiting review, not self-accepted, commits 41adda2 and 7665767 local in tools-rig; no queries; brief pruned.

- 2026-10-19 23:50 BST, plan062 received: KI-TOOL-RIG-CORE-062 at draft (85bafea); Q-062-SCOPE (medium) sent to blind review run scope-review on Codex at high effort; Q-062-ABSENT (high, not destructive) held for Kris; brief pruned.

- 2026-10-19 23:50 BST, IMPORTANT TRIAGE-ALL from State of play (Kris, 19 October: "Okay, there's a lot of items in triage. I need them all triaging. So I want them all running out with the high order functions and anything which is High confidence recommended. Let's move it into now and get it done. Especially to focus on anything to do with the tools burn-downs first."): run rig-triage queued behind plan027 in tools-rig; CAPTURE-GATE applied, no new records; no roadmap cap.

- 2026-10-19 23:50 BST, BURN-WAVE-1 and LANE-OWNERS from State of play: the lane it names (agent-host holds, ki-techne-harness) is not this work's; returned to State of play once, with the reason; CAPTURE-GATE and no-cap parts applied.

- 2026-10-19 23:54 BST, LANE-OWNERS confirmed by State of play: this work's lane is tools-rig and the agent-host hold cluster, which waits with the on-hold ki.agent-host until TECHNE-FOCUS is settled; ki-techne-harness is off the lane; ki.tools-burndown leaves tools-rig alone. The line is removed, which clears the work-package audit failure its format raised.

- 2026-10-19 23:54 BST, scope-review received: the blind review agrees with Q-062-SCOPE a), so its confidence rises to high, with the review's wording added (the remaining case includes TCP; "tailnet-only" not presented as authenticated ingress); brief pruned.

- 2026-10-19 23:59 BST, plan027 received: KI-TOOL-RIG-CLI-027 planned to Ready (size m, local commit in tools-rig, unpushed), `--json` documented with `--format text|json` kept as an equivalent; no queries; brief pruned.

- Kris 2026-10-20 00:16 BST: "Q-062-SCOPE/ABSENT proceed with recommendation" - taken as a) on both: Q-062-SCOPE, deliver KI-TOOL-RIG-CORE-062's own-address destination with no interface match, the remaining targeted TCP and UDP case stated in the specification, ADR-KI-TOOL-RIG-009 and the guide, "tailnet-only" not presented as authenticated ingress, the shared-network advice kept; Q-062-ABSENT, refuse with `unknown` and `tailnet-address-undiscoverable`, installing or rewriting nothing. Run core062 queued behind rig-triage in tools-rig to deliver it to Awaiting review, local commits, no push.

- 2026-10-20 00:22 BST, rig-triage received: KI-TOOL-RIG-CORE-065 and KI-TOOL-RIG-CORE-066 delivered to Awaiting review (local, unpushed); the other six Triage records (053, 057, 064, 067, 068, 069) recorded with medium or low recommendations for the RIG-TRIAGE lane query; brief pruned, report kept until its queries are answered.

- 2026-10-20 00:22 BST, CANCEL-MERGE from State of play (routed from ki.tools-burndown's acceptrig): cancel KI-TOOL-RIG-DIST-011, merge KI-TOOL-RIG-CORE-056 into KI-TOOL-RIG-CORE-053, reject KI-TOOL-RIG-CORE-057 and KI-TOOL-RIG-CORE-064; medium and destructive, and overlapping RIG-TRIAGE on 053, 057 and 064, so both go to one blind review, run triage-review on Codex at high effort, before either reaches Kris.

- 2026-10-20 00:26 BST, triage-review received: RIG-TRIAGE (CANCEL-MERGE folded in, all three views shown since the review disagreed in places) and RIG-MANAGERS (high) copied into queries.md for Kris at the Summary; brief pruned, report kept until answered.

- OVERNIGHT (Kris 2026-10-20 00:28 BST): "I'm going to bed now. I want you to keep looking every 10 minutes to see if there's any new work for yourself in some way. And if there is, I want you to progress it. You can do anything on a high confidence level that you recommend. If you can get a good recommendation, you can move on to the next one, and as you do more and work, it might be that when you come back to ones that you couldn't get a good recommendation for, it might be more accurate. We've got autonomy to make this happen, so I'm going to leave you with this in your safe hands." - taken as: check messages.md and the lane at least every 10 minutes; act on every high-confidence recommendation without asking (medium and low still go to blind review and wait for Kris, revisited as work lands); no push, no live machine change, no acceptance, no new records. Taken now: RIG-MANAGERS a) (high); from RIG-TRIAGE, the parts where rig-triage and the blind review agree: KI-TOOL-RIG-CORE-053 and KI-TOOL-RIG-CORE-067 to Next, KI-TOOL-RIG-CORE-068 to Now for planning only, KI-TOOL-RIG-CORE-069 to Now for diagnosis and planning with no live handler change; KI-TOOL-RIG-CORE-056 stays in Future (the merge not taken). Left for Kris: the KI-TOOL-RIG-CORE-057 and KI-TOOL-RIG-CORE-064 handoffs and KI-TOOL-RIG-DIST-011. Also delivering KI-TOOL-RIG-CLI-027, Ready under RIG-ORDER and TRIAGE-ALL. Chained runs in tools-rig: rig-dispose, deliver027, plan069, plan068, each after the one before, from core062.

- 2026-10-20 00:57 BST, core062 received: KI-TOOL-RIG-CORE-062 delivered to Awaiting review (local, unpushed, 593 of 593 tests); Q-062-TERRA a) (high, read-only) taken under OVERNIGHT: run `rig show firewall:<id>` or `/sbin/ifconfig` on terra at the start of the attended rollout, before any `rig apply --sudo`; the rollout itself, which both Macs need once this Rig is in use (their anchors will show `drifted (anchor-changed)`), waits for Kris's approval at the screen; brief pruned.

- 2026-10-20 01:09 BST, rig-dispose received: RIG-MANAGERS a) applied (G2 folded into KI-TOOL-RIG-CORE-067, KI-TOOL-RIG-CORE-066 narrowed to G3 at Awaiting review); KI-TOOL-RIG-CORE-053 and KI-TOOL-RIG-CORE-067 in Next; KI-TOOL-RIG-CORE-068 and KI-TOOL-RIG-CORE-069 in Now, planning only; 056, 057, 064 and DIST-011 untouched; local, unpushed; no queries; brief pruned.

- 2026-10-20 01:35 BST, deliver027 received: KI-TOOL-RIG-CLI-027 delivered to Awaiting review (local, unpushed, 600 of 600 tests); Q-027-REPEATS (medium) sent to blind review run review027 on Codex at high effort; brief pruned.

- 2026-10-20 01:38 BST, review027 received: the review disagreed with deliver027's medium a) (capture a Triage record) and recommended, at high confidence from direct source checks and isolated probes, fixing all three gaps within KI-TOOL-RIG-CLI-027 before acceptance (deliver027's own option b). Taken under OVERNIGHT, as it is reversible, local, inside the record's own promises and consistent with CAPTURE-GATE: run fix027 queued behind plan068 to reject the four repeated status options, make `remove`'s format scan respect value boundaries, add `--sudo` to both apply synopses, with regression tests and the full gate; no new record. Kris may still choose deliver027's view at acceptance. Brief pruned.

- 2026-10-20 01:45 BST, plan069 received: KI-TOOL-RIG-CORE-069 shaped and left at draft (local, unpushed), since only a live handler change can choose the native setter; RIG-069-PROBE a) (high) needs Kris at sol's screen, so it is held there: run step 1's rungs `legacy`, `modern`, `workspace` with `observe` after each, stopping at the first that makes Zed effective, restoring Warp if needed, then approve Ready; brief pruned.

- 2026-10-20 01:48 BST, RIG-SCHEDULE-ENCODING from State of play (routed from ki.observatory, not blocking): taken under OVERNIGHT at high confidence as a specification-only change that documents today's behaviour, not the additive structured field (a new feature, against BURN-DOWN): run spec-sched queued behind fix027 to specify the `schedule` string encoding in `rig show --format json` (`calendar:` and `interval:` prefixes, records joined by `;`) beside RIG-STATE-033 and RIG-CONF-016, with a fixture test pinning it; if tools-rig needs a record for it, the run raises a query rather than creating one.

- 2026-10-20 02:00 BST, plan068 received: KI-TOOL-RIG-CORE-068 shaped and left at draft (`fcf14da`, local, unpushed), with a ten-step attended NordVPN check (blocks N, P, R, restore rehearsed on terra first), none run. Three queries copied to `queries.md`: PLAN068-VERIFY-GRANT (high), PLAN068-UNPRIV (medium) and PLAN068-READY (medium); the medium two still need their blind review, which the hold stops before launch. Brief pruned.

- 2026-10-20 02:04 BST, HOLD from Kris, in his words: "pause - take stock. Go On hold under current ki-coordination: drain (let a run that will end within about 15 minutes finish, stop any other at a safe point and record where), launch nothing new, commit your own work by explicit path and push only as the standard allows, park every open query, and set state.md to on-hold with reason "take stock on ways of working" and release "Kris says resume". Before the hold report, write design/retro-2026-10-20.md in your work folder with three headings, Working well, Not working and Would change, in five to ten plain bullets that cite real incidents from this work, and commit it with the hold." Taken: fix027 left to finish (in its final test run); spec-sched stopped before it started, its brief kept for resume; no blind review launched for the plan068 queries; PLAN068-VERIFY-GRANT not taken under OVERNIGHT, since the hold ends overnight autonomy.

- 2026-10-20 02:15 BST, fix027 received at the drain: Q-027-REPEATS resolved within KI-TOOL-RIG-CLI-027 in `5cbcdc8` (local, unpushed): repeated `rig status` options exit 2, `remove`'s format pre-scan keeps values verbatim, `--sudo` added to both apply synopses, two regression tests, Bats 602 of 602 and the full gate passing; the record stays at Awaiting review for Kris's acceptance; no new record; brief pruned.
