---
id: ki.sop.main
state: on-hold
since: 2026-11-08T12:21:00Z
received: 2026-10-19T17:58:50Z
beat: null
hold:
  reason: paused
  release: when Kris resumes this work on its new host, or resume
  set_by: owner
  since: 2026-11-08T12:21:00Z
mark: 2026-11-08T12:21:00Z
method_read: d5ede6dd
listening_enabled: true
listening_status: off
workers:
  - name: 🏛️ 🔑 ki.sop.main
    role: governor
    tier: leaders
    focus: []
    since: 2026-11-03T03:14:00Z
    status: active
    listening: off
---

# ki.sop.main state

## Now

- On hold, paused at 12:21 GMT on 8 November: Kris asked to "drain down ready to stop working, we are moving host". Nothing was running; the watcher is stopped and everything is pushed.
- 24 queries and the three ACCEPT records (KI-TOOL-MGIT-CLI-033, KI-TOOL-MGIT-CLI-032, KI-TOOL-RIG-CORE-070) are parked in `discussions.md`; 42 Outbound lines await their ACKs.

## Queue

- ki.prj.website is seeded on hold until Kris opens it; Host network opens fifth, after its decision paper and restore path.

## Standing rule

- ACK-ALWAYS (Kris, about 23:30 GMT 5 Nov): every line taken, held or acted on gets its ACK at the top of the sender's Inbound at the moment it is taken, with no exceptions; lines kept in Inbound to act on later are ACKed too.

## Next steps (8 November 12:21 GMT)

1. On resume on the new host: fetch and fast-forward ki-principal and ki-agentic-harness, read `messages.md` (IMPORTANT first), re-arm listening only if Kris asks.
2. Bring the three ACCEPT records and the 24 parked queries back to Kris.
3. At the first mark, launch the audit-route run: rerun the ki-work-package and coordination audits in ki-principal and send each flagged package one line naming its findings (MSG-e19b4a07 PRINCIPAL-AUDIT).

## Held

- Until 12 November: KI-TECHNE-OPS-018 and KI-TECHNE-OPS-024, with ki.prj.agent-host.
- CLI-FIELDS, until ki.prj.tools-burndown releases KI-TOOL-KI-CLI-155.
- Carried for ki.prj.ways-of-working under HOLD-POINTERS: the harness CI `build` confirmations, GFM-HOSTING-RULES, GFM-CONVERTER, BURNDOWN-PUSH and PAPERCLIP-REQ.
