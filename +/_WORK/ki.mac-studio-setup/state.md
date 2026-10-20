---
id: ki.mac-studio-setup
state: on-hold
since: 2026-10-20T01:10:00Z
received: 2026-10-19T22:27:00Z
beat: null
mark: 2026-10-20T01:10:00Z
method_read: 84b61942
reason: take stock on ways of working
release: Kris says resume
---

# ki.mac-studio-setup state

## Now

- On hold since 02:10 BST on 20 October, paused to take stock on ways of working; released when Kris says resume. Overnight autonomy (OVERNIGHT) ended with the hold.
- Drained: plan068 received (KI-TOOL-RIG-CORE-068 planned, draft); fix027 received (Q-027-REPEATS fixed within KI-TOOL-RIG-CLI-027, `5cbcdc8`); spec-sched (RIG-SCHEDULE-ENCODING for ki.observatory) stopped before it started, its brief kept.
- Records: KI-TOOL-RIG-CORE-047, KI-TOOL-RIG-CORE-062, KI-TOOL-RIG-CORE-063, KI-TOOL-RIG-CORE-065, KI-TOOL-RIG-CORE-066 and KI-TOOL-RIG-CLI-027 await Kris's acceptance; KI-TOOL-RIG-CORE-068 and KI-TOOL-RIG-CORE-069 are planned at draft. tools-rig commits are local and unpushed, beside other sessions' e651edb and 512f21f.
- Lane, confirmed by State of play on 19 October: tools-rig and the agent-host hold cluster.
- Looks resolved, to confirm with Kris: terra key-only SSH and HOSTKEY-APPLY steps 6-9 (KB-DOTFILES-UE-088), and the parked SOL-HNR-HARNESS.
- Retro for the take-stock: [retro-2026-10-20](design/retro-2026-10-20.md).

## Next steps

1. On resume: relaunch spec-sched from its kept brief.
2. Blind-review PLAN068-UNPRIV and PLAN068-READY on Codex, then put every parked query back one at a time, each with a recommendation and its reason, RIG-TRIAGE and the PLAN068 queries first.
3. With Kris: ADOBE-RESTART (deferred, "remind me another day"), then the at-screen items under Held.

## Held

- At sol's screen: key-only SSH ([ssh-keyonly](ssh-keyonly.report.md)), KB-DOTFILES-UE-086 steps 0-12 ([ue086-walk](ue086-walk.report.md)), UTM-SOL, OBS-RESTART, accepting KI-TOOL-RIG-CORE-047, and RIG-069-PROBE: the attended handler probe in step 1 of KI-TOOL-RIG-CORE-069 (rungs `legacy`, `modern`, `workspace`, `observe` after each; restore to Warp), then approve Ready.
- Attended firewall rollout for KI-TOOL-RIG-CORE-062 on both Macs (`rig apply --sudo`, with KI-TOOL-RIG-CORE-047's SSH rollback ready), on terra after a read-only `rig show firewall:<id>` or `/sbin/ifconfig` - with Kris's approval at each screen.
- At terra's screen: pull tools-rig and upgrade Rig past 0.6.3; pull chezmoi and run `chezmoi apply ~/.config/rig && rig doctor`; HOSTKEY-APPLY steps 6-9 ([hostkey-check](hostkey-check.report.md)); then key-only SSH.
- Anywhere: the Headroom favicon request ([favicons-headroom.svg](design/favicons-headroom.svg)).
- FW-LIVE's reboot check at terra's next restart; ZED-MD later at sol; FW-LINUX-LIVE until a Linux host exists.
- RIG-FULLSCREEN, an idea only, no record until Kris asks; KEYCHAIN-SSH with ki.chezmoi (looks resolved).
