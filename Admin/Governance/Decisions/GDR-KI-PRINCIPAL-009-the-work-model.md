---
note_type: admin/governance/decision
id: GDR-KI-PRINCIPAL-009
title: 'The work model'
date: 2026-10-18
updated: 2026-10-18
status: current
decision_type_url: https://knowledgeislands.info/specifications/decision-records/gdr
decision_type: governance
decision_depends_on: ['GDR-KI-PRINCIPAL-005']
---

# GDR-KI-PRINCIPAL-009: The work model

## Context

Kris works with agents through coordinating sessions that brief background runs, collect their reports and put decisions to Kris. That work was carried by three separate instruments: a thread, named after the chat session; a checkpoint holding its pick-up state; and a thread folder holding its decisions log and reports. The same work could be described by any of them, "hold" carried four meanings, and nothing said where a piece of work lay or for how long. The ways of working Project designed one model of work to replace them, and Kris answered its queries on 18 October 2026.

Kris set the unit: "the unit is work, not a conversation". Kris named the two forms of work: "regular work and project work. That's the two forms of work that happen, right?", and the states: "It's either with someone or it's been handed off to someone or we've agreed effectively that it's like on hold ... or we can say it's done, at which point that area is concluded." Kris placed the logbook: "The logbook could be the [Git] history. Yeah, I think it's probably the Git history." On regular work, Kris answered: "there's no coordination thread needed for it because it is sort of self-coordinating, but there's no reason why the state of play thread can't sort of talk about it". On themes: "it makes sense for themes themselves to have a page because you can document why it's a theme, what's important about it, any general direction, and guidance", and on Project notes, "I think they should be flat in streams/projects". On the words, Kris agreed them while noting "We probably just need to see how it comes out in use". Later that day Kris settled the banner glyphs, "with worker, I think you just need a robot saying with a robot", and the answers, "the new reply block is better", having said "I'm starting to outlive the copy block ... Maybe the best approach is just for me to talk like this if it's clear."

## Decision

Knowledge Islands organises coordinated work under one work model. The Work Process note in this island's Pillars describes it in full; this record states what is decided.

- **The unit.** Work is the unit. A piece of work carries what is being worked on, its current state in one small work file, its own decisions, and where it lies. A chat session is only the channel through which a party works on it, and the work outlives every session.
- **Levels and forms.** Work lies at three levels and cascades down to the lowest level that can do it; coordination sits above execution and attention rolls back up.
  - **Territory work**, id `ki` in this territory, is the state of play: it coordinates the coordinators and executes nothing.
  - **Regular work** and **Project work** are the two forms of work, side by side beneath it. Regular work, id `ki.regular`, is the territory's recurring work, defined at territory level in the Capital's Activity notes. It is self-coordinating: it needs no coordination thread, never closes, and is not necessarily dispatched by state of play, which may still discuss it. Ad hoc work with no Project lies in it as `ki.regular.<slug>`. Project work, id `ki.<project>`, coordinates a Project and is finite. A Project's own recurring checks stay with the Project and end with it.
  - **A work item** is one record in any repository, created by either form and executed by a run or a person. Its record's status is its state.
- **Themes.** A theme is a label that regular work, Project work or ad hoc work can carry, not a level. Each theme has one page in `Streams/Themes/` saying why it is a theme, what matters about it, its general direction and the guidance common to the work under it, and it holds no work. Project notes stay flat in `Streams/Projects/` with a `theme:` key. No identifier carries a theme.
- **Roles.** Every handoff has a worker and a supervisor, relative to that handoff: a coordinating agent is worker to Kris and supervisor to its runs. A stuck worker sends the work back to its supervisor with a blocking query. The holder, the party the work lies with now, is derived from the state and the two roles.
- **States.** Work is in one of seven states: With worker; With supervisor; Handoff to supervisor; Handoff to worker; Handoff to a named target; On hold; Finished. Only the supervisor's receive and the hold are set; every other state is derived from where the work's items lie. Only the holder moves the work, by sending it into handoff or receiving it out of handoff.
- **On hold.** On hold is agreed by the supervisor from With supervisor, with one of two reasons: paused, with a named release condition, or more expected, released when new work arrives. The worker drains on the way in, and the move is a mark: every touched repository is committed and pushed, each open query is parked in the work file, and the work file records the reason, release and since. Resume or new work moves it to Handoff to worker; finish moves it to Finished. On hold has no heartbeat and is never stuck; a paused hold older than 31 days is flagged.
- **The roadmap mapping.** The states are the roadmap's machine one level up. `in-progress` is With worker, `awaiting-review` Handoff to supervisor, `triage` and an unapproved `draft` With supervisor, `ready` Handoff to worker, a blocker or a `waiting-for` hold a handoff to its target, a `parked` hold On hold paused, and `done` or `cancelled` Finished. Work items need no new fields.
- **Stuck and the heartbeat.** A heartbeat runs only while work lies with a worker: an update on change, at least every 5 minutes and always by 10. A worker's item that has neither moved nor beaten for 10 minutes is stuck. Work with the supervisor is never stuck, only older.
- **Words.** Hold means only the agreed On hold state; drain is the activity on the way into it. The supervisor receives with `with me`, `ack`, `got it` or `seen`, agrees a hold with `pause` or `done for now`, and moves the work with `resume` and `finish`. The views by holder are with you, stuck, blocked, moving and on hold. `+` and `-` are working areas.
- **Homes.** Each piece of work above a work item has one flat folder in the working area, `+/_WORK/<id>/`, holding `work.md`, `decisions.md`, open reports, open briefs and its design papers. `work.md` holds only the current state in its front matter, then next steps, Messages and the tags of parked queries. `Streams/` holds only definitions and records: Project notes, theme pages and work items. Links point upward, from the work file to its Project note. The run state folder holds only runtime state.
- **History.** The Git history of a work folder is its logbook, and each send and supervisor receive is a commit whose subject carries the move. Shared history is never rewritten: the working area is pruned at every mark, and a separate working repository is considered only if size measurably hurts.
- **Decisions.** `decisions.md` stays apart from the logbook and holds Kris's decisions about that work, in Kris's words, in the turn they arrive. Relays, sends and operational events are moves, recorded as commits, not decisions. At each mark each entry is checked against its durable home and then struck, reduced to a one-line pointer, or kept; entries carry no running numbers.
- **The banner.** A report shows its state in rich text: a heading whose glyphs end with whose move it is, the state in role words, a line of counts and a list of items with holder and since. A settled state shows its holder's glyph alone, as in `🤖 With worker`; an arrow appears only in a handoff state, as in `🤖 → 🧑 Handoff to supervisor` or `→ 👤 Handoff to <target>`. The report's form line carries the same prefix, and the send line appears only when the work is in handoff to Kris.
- **Answers.** An owner report carries no copyable reply block. Queries keep their Context, Query and Options with confidence; Kris answers in speech, and the worker reads each answer back as taken in the decisions log and asks one line where an answer is unclear.
- **The observatory.** Work state is read through one `ki` command, `ki work status --format json`, schema `ki/work-status/v1`, one entry per work file, from which the five views are derived.

## Consequences

- The Work Process note is the one canonical description of the model. The harness standards and skills that govern coordination, delegation, the work file, forward work, Activities and recurring work cite it and do not restate it.
- One migration writes the model in: the harness standards and checker first, then the `tools-ki` readers and a `ki` release, then this Capital's folders, work files, decisions logs and ids together, then the other territories. Until each step lands, the current skills keep governing the instruments it replaces.
- These earlier choices no longer govern: checkpoints and thread folders as separate instruments, and the pick-up block; briefs held in the run state folder; three-part thread ids carrying the Initiative, and the `.sop` id; a decisions log beside the Project note in `Streams/`; nesting Project notes under their Initiative; Initiatives as the home of recurring work; state of play dispatching every occurrence of regular work; design papers kept beside a Project or Initiative in `Streams/`; the block-letter footer frames and the resume line; the copyable stacked reply block; and `hold` as a receive word.
- Initiatives become themes, and records, Activity notes and Project notes name an optional `theme` where they named an `initiative`.
- An Observatory work instrument reads the `ki work status` contract once `tools-ki` provides it.

## References

- [GDR-KI-PRINCIPAL-005](GDR-KI-PRINCIPAL-005-the-roadmap-model.md) - the roadmap model whose states and registry this work model sits above.
