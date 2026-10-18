---
id: ki.observatory
level: project
title: 'KI > Model > Observatory'
project: observatory
theme: model
worker: agent
supervisor: owner
state: on-hold
hold:
  reason: paused
  release: after the work migration lands
since: 2026-10-18T03:30:38Z
received: null
beat: null
mark: 2026-10-18T01:27:13Z
created_at: 2026-10-13T23:50:00Z
---

# ki.observatory

## Next steps

**Pick-up - mark 2026-10-18T01:27:13Z (02:27 BST)**

- **Status:** hold. Drained on Kris's request of 18 October ahead of large ways-of-working updates; nothing running or queued, everything committed and pushed.
- **Resume:** `Resume KI > Knowledge Islands model > Observatory from its checkpoint under current ki-pmo and ki-delegation since 2026-10-18T01:27:13Z: re-bootstrap, read the pick-up block, take stock, put the parked queries back, restart authorised work, then banner.`
- **Where it stopped:** units 1 and 2 delivered, Awaiting review and pushed to `origin/main` of `apps-observatory.local` at `042539d`: KI-OBSERVA-VIS-023 Sessions and threads (renumbered from 022 by obs-land, the remote having given 022 to another session's record) and KI-OBSERVA-VIS-024 Review queue. The service was restarted interactively at 02:30 BST on 18 October at `042539d` and answers on `127.0.0.1:1675` with both Instruments. Unit 3 not started.
- **Parked queries** (detail in `+/_THREADS/observatory/obs-land.report.md`):
  - OBS-SESSIONS-ACCEPT - unit 1 awaits review; recommended a) review the Sessions view against the record's review notes, accept through ki-accept or send back with notes.
  - OBS-REVIEW-ACCEPT - unit 2 awaits review; recommended a) review KI-OBSERVA-VIS-024 in the running Observatory, accept or send back.
  - OBS-REVIEW-OPEN - whether `+/` items open read-only from the Review queue; recommended a) keep the staging refusal and show paths, revisit while planning unit 3.
  - OBS-OVERDUE-TITLE - the other session's KI-OBSERVA-VIS-022 title breaks the roadmap audit's four-word limit on `origin/main`; recommended a) leave it to the session that owns that record, flagged through state-of-play.
- **Idea, not now:** Kris, 18 October: "I think we should consider where it is served from on a machine and maybe look at live reloads or something similar" and "although thats not a now things". The service runs the primary checkout, so each delivery needs a manual restart; capture it as a triage record in `apps-observatory.local` when the thread resumes.
- **Next steps when back in use:** (1) Kris answers the two ACCEPT queries; (2) capture the serving and live-reload idea as triage; (3) capture, plan and deliver unit 3, Capture feedback, chained behind KI-OBSERVA-VIS-024, under the new ways-of-working standards; (4) unit 4, the tailnet name, waits for Host network.
- **Thread note:** the re-bootstrap turn of 18 October went over the five-call budget after two mis-formed launches, and the rest and hold commits of the same night left the pick-up block stale until this correction.

Take obs-sessions' report, then capture the Sessions and threads Instrument as the first record in `apps-observatory.local` through `ki-next`, and plan and deliver it as background agents in run `observatory`, with the Review queue and Capture feedback chained behind it.

## Messages

- MIGRATED - this file was `+/_CHECKPOINTS/knowledge-islands-model.observatory.md` until the work migration of 2026-10-18. At your next mark, cut it to next steps, Messages and the tags of parked queries, each linked to its report; move anything else to its durable home, then remove this line.

## Parked

- None of this thread's own. CC-HANDOFFS, held from Command centre, moved with the vocabulary to the [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working/ways-of-working.md) Project Notes.
