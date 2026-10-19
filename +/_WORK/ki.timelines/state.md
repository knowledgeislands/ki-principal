---
id: ki.timelines
state: with-worker
since: 2026-10-19T23:40:58Z
received: 2026-10-19T22:26:30Z
beat: null
method_read: 84b61942
---

# ki.timelines state

## Now

- Kris is away overnight under OVERNIGHT-AUTONOMY (`decisions.md`): high-confidence recommendations are taken, the rest held.
- The [merged report](design/timelines-skill-report.md) is in, built on the Fable and Astra reviews; its four high-confidence queries are decided (DESIGN-HIGH).
- tl-qreview agreed on FEED-HOME, ADOPTION-ORDER and TIMED-BUSY, now decided (DESIGN-REVIEWED); it disagrees on SKILL-NAME, held for Kris.
- The [decided design](design/timelines-skill-design.md) and its seven-step rollout plan are written; its KI-HARNESS-GOV-222 handoff is routed to State of play (HANDOFF-GOV-222).
- SKILL-NAME (`ki-calendars`) and PROVIDER-FIRST (Google first) decided (NAME-AND-PROVIDER); no open queries.
- Running: tl-name, filling the name and provider into the design note; brief [tl-name.brief.md](tl-name.brief.md).
- Last mark 19:03 BST on 19 October.

## Next steps

1. Receive tl-name; then the work waits on Kris for rollout steps 2 and 3 (5G Emerge, legal-principal) and on the harness for KI-HARNESS-GOV-222; check `messages.md` every 10 minutes overnight.
2. KI-HARNESS-GOV-222 still names `project: observatory`; moving it is the harness's call.
3. legal-principal's "FR Timeline to FDR" gantt stays as Mermaid meanwhile (DIAGRAM-GANTT, ki.observatory).

## Held

- HOOK-GUARD (relayed from ki.tools-burndown, 19 October): never run `ki repo conform` without `--dry-run` on a KI repository until ki.tools-burndown lifts it; no Timelines run is authorised to conform.
