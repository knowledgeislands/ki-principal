---
id: ki.prj.mac-studio-setup
state: with-worker
hold: null
since: 2026-10-30T01:40:00Z
received: 2026-10-30T01:40:00Z
beat: null
mark: 2026-10-20T01:10:00Z
method_read: 6868da5a
---

# ki.prj.mac-studio-setup state

## Now

- Re-bootstrapped on sol at 01:39 GMT on 30 October as coordinator; dispatch through `ki agent`, run `ki-prj-mac-studio-setup` (KI-AGENT-DISPATCH), ending the Orca dispatch trial after one unit.
- rig-intake running under `ki agent`; RIG-069-PROBE with Kris.
- plan069 received: KI-TOOL-RIG-CORE-069 at draft, waiting on RIG-069-PROBE at sol's screen.
- tools-rig is level with origin. Open: KI-TOOL-RIG-CORE-047 (in progress, waiting on terra), KI-TOOL-RIG-CORE-068 (draft, size m), KI-TOOL-RIG-CORE-069 (draft, size s, probe needed) and KI-TOOL-RIG-CORE-070 (awaiting review).
- Method read at `6868da5a`.
- Lane: tools-rig and the agent-host hold cluster.

## Next steps

1. Receive rig-intake (launched 01:50 GMT, [brief](briefs/rig-intake.md)): shape RIG-INTAKE for the nine retained Rig capability lines in `messages.md` (capture as unadopted tools-rig triage, or hold under BURN-DOWN), blind-reviewed before it reaches Kris.
2. ORCA-HANDOVER: once State of play creates the Orca evaluation package, a run updates [orca-trial](design/orca-trial.md) with plan069's Orca section and sends the evidence and ORCA-HOST there as a messages.md line; then prune plan069.report.md and the trial log here.
3. spec-sched waits from [its brief](briefs/spec-sched.md); OVERNIGHT, which authorised it, ended with the 20 October hold, so it needs a new go.
4. Put the parked queries back one at a time, RIG-TRIAGE and the PLAN068 queries first, blind-reviewing PLAN068-UNPRIV and PLAN068-READY.
5. With Kris: RIG-069-PROBE, ADOBE-RESTART (deferred), then the at-screen items under Held. Home or delete `design/adobe-remove.sh` once Kris answers ADOBE-SCRIPT-HOME in State of play.

## Held

- KI-TOOL-RIG-CORE-047 waits on terra (NordVPN on/off checks and `rig apply --sudo`). No attended NordVPN trial until KI-TOOL-RIG-CORE-068 has a tested restore path; NordVPN runs on terra, not sol (NORDVPN-HOLD, from ki.prj.chezmoi, 22 October).
- At sol's screen: key-only SSH ([ssh-keyonly](ssh-keyonly.report.md)), PERSONAL-DOTFILES-UE-086 steps 0-12 ([ue086-walk](ue086-walk.report.md)), UTM-SOL, OBS-RESTART and RIG-069-PROBE, the attended handler probe in KI-TOOL-RIG-CORE-069.
- At terra's screen: HOSTKEY-APPLY steps 6-9 ([hostkey-check](hostkey-check.report.md)), then key-only SSH; the firewall re-apply recorded in KI-TOOL-RIG-CORE-047, with its SSH rollback ready and Kris's approval at each screen.
- Anywhere: the Headroom favicon request ([favicons-headroom.svg](design/favicons-headroom.svg)).
- FW-LIVE's reboot check at terra's next restart; ZED-MD later at sol; FW-LINUX-LIVE until a Linux host exists.
- RIG-FULLSCREEN, an idea only, no record until Kris asks.
