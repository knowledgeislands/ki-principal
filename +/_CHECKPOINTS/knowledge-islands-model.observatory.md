---
type: ki-checkpoint
thread: knowledge-islands-model.observatory
label: 'KI > Knowledge Islands model > Observatory'
role: coordination
state: active
created_at: 2026-10-13T23:50:00Z
updated_at: 2026-10-18T01:27:13Z
---

# knowledge-islands-model.observatory

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

## Objective

Reconstruct the Observatory thread if its session is lost. It is the one thread of the [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) Project in the [Knowledge Islands model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/knowledge-islands-model/knowledge-islands-model.md) Initiative, whose Outcome is "the operations centre for one or more territories", with the seven goals and four planned units in the Project note. The thread owns product work in `apps-observatory.local` (`knowledgeislands/apps-observatory.local`, working directory `~/workspaces/knowledge-islands/apps-observatory.local`); unit 4, the tailnet name, belongs to Host network. Cross-territory vocabulary stays with KI Model: ways-of-working.

Kris folded Command centre into this Project on 2026-10-18 (OBS-OWNER), so the command-centre checkpoint closed into this one, and set the slice (OBS-SLICE) and the restart (OBS-NOW) the same night. The earlier burn-down remit of Decision 158 ends with them.

## Current state

- Mark: 2026-10-18T01:27:13Z (02:27 BST, struck at the hold Kris asked for on 18 October).
- ki-pmo read at b7ab7eff.
- **Running.** Nothing.
- **Roadmap.** In the last stock-take, one triage record, [KI-OBSERVA-VIS-021](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-021-explain-tool-storage.md), and the 16 October Personal repository-manager intake under the repository's `+/` folder. Units 1 to 3 are not yet records; obs-sessions is shaping unit 1.
- **The app.** Twelve Instruments, a Beacon, governed Git operations, read-only Knowledge Base and Documents reading, and a Rig-managed login service running under launchd on each host at `127.0.0.1:1675`; the tab icon is on `origin/main`.
- **KI-OBSERVA-INT-002 accepted.** Kris reviewed it in the Observatory and in Cowork and passed it (Decision 160). Closed as done in `0cf59ec` ([record at that commit](https://github.com/knowledgeislands/apps-observatory.local/blob/0cf59ec/docs/roadmap/KI-OBSERVA-INT-002-portable-live-artifact-interface.md)) and pruned in `74a0eea`; the ChatGPT publication server and a confirmed write operation sit under Gaps in `docs/specs/artifacts.md`.
- **Favicons.** The Observatory tab icon is on `origin/main`; OBS-RESTART is closed as Kris's, who restarts the service on sol in an interactive session and checks the dome; HEADROOM-ICON is closed as deferred to LOCAL-DNS in the [Host network](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/host-network.md) Notes, with no upstream request; Kris fixed the two midnight.ninja icons (FAVICON-FOLLOWUPS, 17 October).
- **Restart.** Each delivery needs the service restarted on the host in an interactive session, as the repository's AGENTS.md requires; last done 02:30 BST on 18 October at `042539d`.
- **Run material.** The `observa-002`, `observa-002-build`, `observa-tabfix` and `observa-accept` reports in `~/.local/state/ki/agents/state-of-play/` hold the earlier delivery and acceptance evidence; the [observatory-goals report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/state-of-play/observatory-goals.report.md) holds the goals, the units and the diagram.
- **Thread folders.** `+/_THREADS/observatory/` holds the thread's `decisions.md`, copied from the state folder at restart, and its run reports. The inherited `+/_THREADS/command-centre/` holds `decisions.md` only, which is the closed list, so THREADS-CLEAR and PMO-7-BACKLOG needed no move or deletion there.
- **Inherited from Command centre.** Kris asked on 2026-10-14 that, while token limits are tight, work goes to lower-model background agents, mechanical steps first.

Thread rules:

- Re-read the Messages block at every Summary as well as at bootstrap, act on each line, then remove it; any coordination thread may write a line into another's block (INTERIM-MESSAGING, on Kris's DISPATCH-ORDER of 17 October, until ways of working sets the standard).
- Embed diagrams in every design or consolidation this thread writes, as Kris asked on 17 October (DIAGRAMS-NOW): "a picture or a diagram ... is worth a thousand words".
- Background agents run through `ki agent` under run name `observatory`, with status, reports and the thread's decisions log in `~/.local/state/ki/agents/observatory/`.
- Commit with explicit paths only; push own commits fast-forward only.
- `ki-accept` closes a record only with Kris's approval.
- Cross-repository needs go to the receiving repository's roadmap as a handoff, or through state-of-play.

## Decisions made

- Restart confirmed: the Observatory Project note keeps Kris's areas of 14 October under Ideas for evaluation, and its Outcome, "the operations centre for one or more territories", agrees with the Objective here; OBS-OWNER supersedes OBS-MERGE's Outcome (AREAS-DISPATCH and OBS-MERGE, confirmed 18 October).
- One Observatory Project, Outcome "the operations centre for one or more territories", this thread its one thread, the command-centre checkpoint closed into it, cross-territory vocabulary with ways of working (Kris, 2026-10-18, OBS-OWNER, in the state-of-play decisions log).
- Four units in order, the first three chained in `apps-observatory.local`, the fourth with Host network (Kris, 2026-10-18, OBS-SLICE).
- Restart now, ahead of the ways-of-working gate, with the Sessions and threads Instrument first (Kris, 2026-10-18, OBS-NOW).
- Carried from Command centre: the name "Command centre" kept "Council" for the Capital's governance body (Kris, 2026-10-11); vocabulary and model terms belong to ways of working (Kris, 2026-10-13); the state-of-play thread owns cross-project priorities, releases and decisions, and this thread works only its Project's records.
- KI-OBSERVA-INT-002 accepted on Kris's review pass (state-of-play Decision 160).

## Files touched

- `ki-principal`: this checkpoint; `+/_THREADS/observatory/decisions.md` and run reports; the state-of-play run `obs-fold` wrote the Observatory Project note and its index entries and retired the command-centre checkpoint.
- `apps-observatory.local`: `docs/roadmap/KI-OBSERVA-INT-002-portable-live-artifact-interface.md` (closed, then pruned) and `docs/specs/artifacts.md` (two Gaps).

## Open questions

- None of this thread's own. CC-HANDOFFS, held from Command centre, moved with the vocabulary to the [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working/ways-of-working.md) Project Notes.

## Next step

Take obs-sessions' report, then capture the Sessions and threads Instrument as the first record in `apps-observatory.local` through `ki-next`, and plan and deliver it as background agents in run `observatory`, with the Review queue and Capture feedback chained behind it.
