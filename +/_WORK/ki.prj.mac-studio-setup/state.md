---
id: ki.prj.mac-studio-setup
state: on-hold
hold:
  reason: paused
  release: when Kris opens this Project work, or ki.sop.main closes it out; coordination runs through ki.sop.main from 3 November
since: 2026-11-03T03:10:53Z
received: 2026-10-30T01:40:00Z
beat: null
mark: 2026-11-03T03:10:53Z
method_read: b3c631c2
---

# ki.prj.mac-studio-setup state

## Now

- On hold (paused) since 3 November, 03:10 GMT; coordination taken up by State of play (ki.sop.main) under SOLE-THREAD. Nothing running.
- Site work handed to personal.reg.household-sol and personal.reg.household-terra on 2 November ([setup/handover.md](setup/handover.md)); both acknowledged.
- Close-out planned in [setup/close-out.md](setup/close-out.md) (4 November, draft): nothing routes until Kris answers TOOLS-RIG-LANE and RIG-INTAKE; the close itself is Kris's.
- Eight queries parked in [discussions](discussions.md), TOOLS-RIG-LANE first; the retained Rig lines in [messages](messages.md) wait for whoever takes the tools-rig lane.
- Lane: tools-rig and the agent-host hold cluster; open records [KI-TOOL-RIG-CORE-047](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md), [KI-TOOL-RIG-CORE-068](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md), [KI-TOOL-RIG-CORE-069](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md), [KI-TOOL-RIG-CORE-070](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-070-handler-read-back-after-confirmation.md). Method read at `b3c631c2`.

## Next steps

1. RIG-INTAKE and RIG-ASKS with Kris; after the answer the coordinator launches the captures and returns. Was: shape RIG-INTAKE for the nine retained Rig capability lines in `messages.md` (capture as unadopted tools-rig triage, or hold under BURN-DOWN), blind-reviewed before it reaches Kris.
2. spec-sched waits from [its brief](setup/spec-sched.brief.md); OVERNIGHT, which authorised it, ended with the 20 October hold, so it needs a new go.
3. Put the parked queries back one at a time, RIG-TRIAGE and the PLAN068 queries first, blind-reviewing PLAN068-UNPRIV and PLAN068-READY.
4. With Kris: RIG-069-PROBE, ADOBE-RESTART (deferred), then the at-screen items under Held. Home or delete `setup/adobe-remove.sh` once Kris answers ADOBE-SCRIPT-HOME in State of play.

## Held

- KI-TOOL-RIG-CORE-047 waits on terra (NordVPN on/off checks and `rig apply --sudo`). No attended NordVPN trial until KI-TOOL-RIG-CORE-068 has a tested restore path; NordVPN runs on terra, not sol (NORDVPN-HOLD, from ki.prj.chezmoi, 22 October).
- At sol's screen: key-only SSH ([ssh-keyonly](setup/ssh-keyonly.report.md)), PERSONAL-DOTFILES-UE-086 steps 0-12 ([ue086-walk](setup/ue086-walk.report.md)), UTM-SOL, OBS-RESTART and RIG-069-PROBE, the attended handler probe in KI-TOOL-RIG-CORE-069.
- At terra's screen: HOSTKEY-APPLY steps 6-9 ([hostkey-check](setup/hostkey-check.report.md)), then key-only SSH; the firewall re-apply recorded in KI-TOOL-RIG-CORE-047, with its SSH rollback ready and Kris's approval at each screen.
- Anywhere: the Headroom favicon request ([favicons-headroom.svg](setup/favicons-headroom.svg)).
- FW-LIVE's reboot check at terra's next restart; ZED-MD later at sol; FW-LINUX-LIVE until a Linux host exists.
- RIG-FULLSCREEN, an idea only, no record until Kris asks.
