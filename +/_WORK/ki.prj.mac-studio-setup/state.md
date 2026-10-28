---
id: ki.prj.mac-studio-setup
state: on-hold
hold:
  reason: paused
  release: Kris says resume
since: 2026-10-20T01:10:00Z
received: 2026-10-19T22:27:00Z
beat: null
mark: 2026-10-20T01:10:00Z
method_read: 84b61942
---

# ki.prj.mac-studio-setup state

## Now

- On hold since 02:10 BST on 20 October, to take stock on ways of working; released when Kris says resume. Nothing is running.
- tools-rig: KI-TOOL-RIG-CORE-062, KI-TOOL-RIG-CORE-063, KI-TOOL-RIG-CORE-065, KI-TOOL-RIG-CORE-066 and KI-TOOL-RIG-CLI-027 are done and pruned. Open: KI-TOOL-RIG-CORE-047 (in progress, waiting on terra's NordVPN checks and `rig apply --sudo`), KI-TOOL-RIG-CORE-068 and KI-TOOL-RIG-CORE-069 (draft) and KI-TOOL-RIG-CORE-070 (awaiting review).
- Queries are parked in `queries.md`; `messages.md` holds the Rig capability requests to take at resume.
- Lane: tools-rig and the agent-host hold cluster.

## Next steps

1. On resume: re-read the method, take `messages.md` in order, then relaunch spec-sched from [its brief](briefs/spec-sched.md).
2. Blind-review PLAN068-UNPRIV and PLAN068-READY, then put every parked query back one at a time, RIG-TRIAGE and the PLAN068 queries first.
3. With Kris: ADOBE-RESTART (deferred), then the at-screen items under Held.

## Held

- At sol's screen: key-only SSH ([ssh-keyonly](ssh-keyonly.report.md)), PERSONAL-DOTFILES-UE-086 steps 0-12 ([ue086-walk](ue086-walk.report.md)), UTM-SOL, OBS-RESTART and RIG-069-PROBE, the attended handler probe in KI-TOOL-RIG-CORE-069.
- At terra's screen: HOSTKEY-APPLY steps 6-9 ([hostkey-check](hostkey-check.report.md)), then key-only SSH; the firewall re-apply recorded in KI-TOOL-RIG-CORE-047, with its SSH rollback ready and Kris's approval at each screen.
- Anywhere: the Headroom favicon request ([favicons-headroom.svg](design/favicons-headroom.svg)).
- FW-LIVE's reboot check at terra's next restart; ZED-MD later at sol; FW-LINUX-LIVE until a Linux host exists.
- RIG-FULLSCREEN, an idea only, no record until Kris asks.
