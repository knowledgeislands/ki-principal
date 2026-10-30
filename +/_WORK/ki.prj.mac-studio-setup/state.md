---
id: ki.prj.mac-studio-setup
state: with-worker
hold: null
since: 2026-10-30T00:23:00Z
received: 2026-10-30T00:16:00Z
beat: null
mark: 2026-10-20T01:10:00Z
method_read: 6868da5a
---

# ki.prj.mac-studio-setup state

## Now

- Resumed on sol at 00:16 GMT on 30 October as an Orca trial (ORCA-HOST): dispatch goes through Orca Run `run_0de85069bc1d`, not `ki agent`. Trial log: [orca-trial](design/orca-trial.md).
- plan069, an Orca worker, plans KI-TOOL-RIG-CORE-069 under GO-PLAN ([brief](briefs/plan069.md)).
- tools-rig is level with origin. Open: KI-TOOL-RIG-CORE-047 (in progress, waiting on terra's NordVPN checks and `rig apply --sudo`), KI-TOOL-RIG-CORE-068 (draft, size m), KI-TOOL-RIG-CORE-069 (draft, size s) and KI-TOOL-RIG-CORE-070 (awaiting review).
- Method read at `6868da5a`.
- Lane: tools-rig and the agent-host hold cluster.

## Next steps

1. Receive plan069: one Orca worker (`worker-start --worktree current --agent codex`) plans KI-TOOL-RIG-CORE-069 to Ready under ki-plan, or as far as it can without a system change; no sudo, no `rig apply`. Waiting with `orchestration check --wait`; the report lands in this folder; update [orca-trial](design/orca-trial.md).
2. After two or three Orca units (ORCA-SKILL a), send the trial log to ki.prj.ways-of-working as a message proposing an Orca launcher under ki-delegation and ki-coordination.
3. Shape RIG-INTAKE for the nine retained Rig capability lines in `messages.md` (capture as unadopted tools-rig triage, or hold under BURN-DOWN), blind-reviewed before it reaches Kris.
4. spec-sched waits from [its brief](briefs/spec-sched.md); OVERNIGHT, which authorised it, ended with the 20 October hold, so it needs a new go.
5. Put the parked queries back one at a time, RIG-TRIAGE and the PLAN068 queries first, blind-reviewing PLAN068-UNPRIV and PLAN068-READY.
6. With Kris: ADOBE-RESTART (deferred), then the at-screen items under Held. Home or delete `design/adobe-remove.sh` once Kris answers ADOBE-SCRIPT-HOME in State of play.

## Held

- KI-TOOL-RIG-CORE-047 waits on terra (NordVPN on/off checks and `rig apply --sudo`). No attended NordVPN trial until KI-TOOL-RIG-CORE-068 has a tested restore path; NordVPN runs on terra, not sol (NORDVPN-HOLD, from ki.prj.chezmoi, 22 October).
- At sol's screen: key-only SSH ([ssh-keyonly](ssh-keyonly.report.md)), PERSONAL-DOTFILES-UE-086 steps 0-12 ([ue086-walk](ue086-walk.report.md)), UTM-SOL, OBS-RESTART and RIG-069-PROBE, the attended handler probe in KI-TOOL-RIG-CORE-069.
- At terra's screen: HOSTKEY-APPLY steps 6-9 ([hostkey-check](hostkey-check.report.md)), then key-only SSH; the firewall re-apply recorded in KI-TOOL-RIG-CORE-047, with its SSH rollback ready and Kris's approval at each screen.
- Anywhere: the Headroom favicon request ([favicons-headroom.svg](design/favicons-headroom.svg)).
- FW-LIVE's reboot check at terra's next restart; ZED-MD later at sol; FW-LINUX-LIVE until a Linux host exists.
- RIG-FULLSCREEN, an idea only, no record until Kris asks.
