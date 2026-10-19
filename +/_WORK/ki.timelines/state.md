---
id: ki.timelines
state: with-worker
since: 2026-10-19T23:38:44Z
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
- Running: tl-qreview2, a blind Codex review of SKILL-NAME (second look) and PROVIDER-FIRST; brief [tl-qreview2.brief.md](tl-qreview2.brief.md).
- Last mark 19:03 BST on 19 October.

## Next steps

1. Receive tl-qreview2; take a query only at high confidence; rollout steps 2 and 3 run in 5G Emerge and legal-principal, outside this territory, and wait for Kris.
2. KI-HARNESS-GOV-222 still names `project: observatory`; moving it is the harness's call.
3. legal-principal's "FR Timeline to FDR" gantt stays as Mermaid meanwhile (DIAGRAM-GANTT, ki.observatory).

## Held

- HOOK-GUARD (relayed from ki.tools-burndown, 19 October): never run `ki repo conform` without `--dry-run` on a KI repository until ki.tools-burndown lifts it; no Timelines run is authorised to conform.
