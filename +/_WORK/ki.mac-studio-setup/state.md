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
- Running: core062 in tools-rig. RIG-TRIAGE and RIG-MANAGERS, reviewed, wait for Kris at the Summary. rig-triage received: KI-TOOL-RIG-CORE-065 and KI-TOOL-RIG-CORE-066 at Awaiting review; KI-TOOL-RIG-CLI-027 is Ready.
- Records: KI-TOOL-RIG-CORE-047 and KI-TOOL-RIG-CORE-063 await Kris's acceptance; KI-TOOL-RIG-CORE-062's two queries are answered and run core062 is queued behind rig-triage to deliver it; KI-TOOL-RIG-CORE-069 is in Triage. Pushes are left to Kris and the owning sessions.
- Lane, confirmed by State of play on 19 October: tools-rig and the agent-host hold cluster, which waits with the on-hold ki.agent-host until TECHNE-FOCUS is settled.
- Looks resolved, to confirm with Kris: terra key-only SSH and HOSTKEY-APPLY steps 6-9 (KB-DOTFILES-UE-088), and the parked SOL-HNR-HARNESS.

## Next steps

1. With Kris, ADOBE-RESTART first (deferred, "remind me another day"): restart sol, run [`./adobe-remove.sh`](design/adobe-remove.sh) as a dry run (nothing under What is left), then `ls -d /Applications/Adobe* /Applications/Utilities/Adobe* ~/Pictures/Lightroom/*.lrcat`, which should show only the catalogue.
2. Receive rig-triage; receive core062; send RIG-TRIAGE and RIG-MANAGERS to Kris; then Kris accepts the Awaiting-review records at the next sol session.
3. Then put the parked queries back one at a time, each with a recommendation and its reason.

## Held

- At sol's screen: key-only SSH ([ssh-keyonly](ssh-keyonly.report.md)), KB-DOTFILES-UE-086 steps 0-12 ([ue086-walk](ue086-walk.report.md)), UTM-SOL, OBS-RESTART and accepting KI-TOOL-RIG-CORE-047.
- At terra's screen: pull tools-rig and upgrade Rig past 0.6.3; pull chezmoi and run `chezmoi apply ~/.config/rig && rig doctor`; HOSTKEY-APPLY steps 6-9 ([hostkey-check](hostkey-check.report.md)); then key-only SSH.
- Anywhere: the Headroom favicon request ([favicons-headroom.svg](design/favicons-headroom.svg)).
- FW-LIVE's reboot check at terra's next restart; ZED-MD later at sol; FW-LINUX-LIVE until a Linux host exists.
- RIG-FULLSCREEN, an idea only, no record until Kris asks; KEYCHAIN-SSH with ki.chezmoi (looks resolved).
