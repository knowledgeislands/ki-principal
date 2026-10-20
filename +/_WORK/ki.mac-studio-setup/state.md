---
id: ki.mac-studio-setup
state: with-worker
since: 2026-10-19T22:30:00Z
received: 2026-10-19T22:27:00Z
beat: null
mark: 2026-10-19T22:36:00Z
method_read: 84b61942
---

# ki.mac-studio-setup state

## Now

- With worker since 23:30 BST on 19 October; marked at 23:36 BST on 19 October.
- Overnight autonomy (OVERNIGHT, 00:28 BST): check every 10 minutes, act on high confidence. Chained in tools-rig: plan069, plan068, then fix027 (Q-027-REPEATS follow-up within KI-TOOL-RIG-CLI-027). The rest of RIG-TRIAGE (057, 064, DIST-011) waits for Kris. rig-triage received: KI-TOOL-RIG-CORE-065 and KI-TOOL-RIG-CORE-066 at Awaiting review;
- Records: KI-TOOL-RIG-CORE-047, KI-TOOL-RIG-CORE-062, KI-TOOL-RIG-CORE-063, KI-TOOL-RIG-CORE-065, KI-TOOL-RIG-CORE-066 and KI-TOOL-RIG-CLI-027 await Kris's acceptance; KI-TOOL-RIG-CORE-069 is in Triage. Pushes are left to Kris and the owning sessions.
- Lane, confirmed by State of play on 19 October: tools-rig and the agent-host hold cluster, which waits with the on-hold ki.agent-host until TECHNE-FOCUS is settled.
- Looks resolved, to confirm with Kris: terra key-only SSH and HOSTKEY-APPLY steps 6-9 (KB-DOTFILES-UE-088), and the parked SOL-HNR-HARNESS.

## Next steps

1. With Kris, ADOBE-RESTART first (deferred, "remind me another day"): restart sol, run [`./adobe-remove.sh`](design/adobe-remove.sh) as a dry run (nothing under What is left), then `ls -d /Applications/Adobe* /Applications/Utilities/Adobe* ~/Pictures/Lightroom/*.lrcat`, which should show only the catalogue.
2. Receive rig-triage; receive the chain, then look for the next high-confidence work; give Kris the Summary with the rest of RIG-TRIAGE in the morning; then Kris accepts the Awaiting-review records at the next sol session.
3. Then put the parked queries back one at a time, each with a recommendation and its reason.

## Held

- At sol's screen: key-only SSH ([ssh-keyonly](ssh-keyonly.report.md)), KB-DOTFILES-UE-086 steps 0-12 ([ue086-walk](ue086-walk.report.md)), UTM-SOL, OBS-RESTART and accepting KI-TOOL-RIG-CORE-047.
- Attended firewall rollout for KI-TOOL-RIG-CORE-062 on both Macs (`rig apply --sudo`, with KI-TOOL-RIG-CORE-047's SSH rollback ready), on terra after a read-only `rig show firewall:<id>` or `/sbin/ifconfig` - with Kris's approval at each screen.
- At terra's screen: pull tools-rig and upgrade Rig past 0.6.3; pull chezmoi and run `chezmoi apply ~/.config/rig && rig doctor`; HOSTKEY-APPLY steps 6-9 ([hostkey-check](hostkey-check.report.md)); then key-only SSH.
- Anywhere: the Headroom favicon request ([favicons-headroom.svg](design/favicons-headroom.svg)).
- FW-LIVE's reboot check at terra's next restart; ZED-MD later at sol; FW-LINUX-LIVE until a Linux host exists.
- RIG-FULLSCREEN, an idea only, no record until Kris asks; KEYCHAIN-SSH with ki.chezmoi (looks resolved).
