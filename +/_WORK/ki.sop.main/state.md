---
id: ki.sop.main
state: with-supervisor
since: 2026-11-08T18:20Z
received: 2026-10-19T17:58:50Z
beat: null
hold: null
mark: 2026-11-08T12:21:00Z
method_read: d5ede6dd
listening_enabled: true
listening_status: off
workers:
  - name: 🏛️ 🔑 ki.sop.main+governor
    role: governor
    tier: leaders
    focus: []
    since: 2026-11-03T03:14:00Z
    status: active
    listening: off
---

# ki.sop.main state

## Now

- Resumed on sol at 18:20 GMT on 8 November and reset at Kris's word straight after: all open work is parked under RESET-PARK. Nothing is running or queued; launch nothing and resume nothing from before the reset.
- Act only on Kris's messages and on lines from ki.sop.main+governor, ki.reg.guilds+guildmaster, ki.prj.agora+warden, personal.reg.inbox+gatekeeper, personal.reg.rig-terra+housekeeper and personal.reg.rig-sol+housekeeper; any other line is received but parked (SENDER-ALLOWLIST).
- Kris carries messages between sessions by hand; the Agora store `krisb/ki-agora-store` was cleared for a clean start. This session stays the one front door for sending Knowledge Islands work out but sends nothing until Kris says so (HAND-CARRY).

## Parked by RESET-PARK (8 November 18:20 GMT)

- The 24 queries under `## Parked` in `discussions.md`, and the three ACCEPT records KI-TOOL-MGIT-CLI-033, KI-TOOL-MGIT-CLI-032 and KI-TOOL-RIG-CORE-070.
- The queue: ki.prj.website seeded on hold until Kris opens it; Host network fifth, after its decision paper and restore path.
- The next steps of 12:21 GMT, including the audit-route run (MSG-e19b4a07 PRINCIPAL-AUDIT).
- The 42 Outbound lines awaiting ACK: parked, not written off, left in `messages.md` and not chased (RESET-ANSWERS).
- The briefs, reports and design notes in `_emerging/`, left in place.
- Standing rule ACK-ALWAYS (Kris, about 23:30 GMT 5 Nov) is paused: a line from one of the six SENDER-ALLOWLIST sessions still gets its ACK; any other line gets none (RESET-ANSWERS).

## Next steps (8 November 18:20 GMT)

1. Wait for the first message round, which Kris brings through personal.reg.inbox; launch, resume and send nothing else.
2. Record each change Kris gives in `decisions.md` the turn it arrives, naming the standard it departs from.

## Held

All parked under RESET-PARK. Date noted only: KI-TECHNE-OPS-018 and KI-TECHNE-OPS-024 are held until 12 November.

- Until 12 November: KI-TECHNE-OPS-018 and KI-TECHNE-OPS-024, with ki.prj.agent-host.
- CLI-FIELDS, until ki.prj.tools-burndown releases KI-TOOL-KI-CLI-155.
- Carried for ki.prj.ways-of-working under HOLD-POINTERS: the harness CI `build` confirmations, GFM-HOSTING-RULES, GFM-CONVERTER, BURNDOWN-PUSH and PAPERCLIP-REQ.
