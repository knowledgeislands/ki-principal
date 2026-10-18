---
note_type: pillars/index
tags:
  - card/note
  - topic/knowledge-islands
  - topic/work
status: current - October 2026
author: Written with Claude
---

# Work Process

## Overview

The Work Process is how coordinated work moves through a territory: who holds it, how it passes between parties, where its state is kept and how it is shown. It is the one canonical description of the model that [[GDR-KI-PRINCIPAL-009-the-work-model|GDR-KI-PRINCIPAL-009]] decides. The harness standards and skills that govern coordination, delegation, the work file, forward work, Activities and recurring work cite this note rather than restate it.

The unit is work, in Kris's words "the unit is work, not a conversation". A piece of work carries four things: what is being worked on, its current state in one small work file, its own decisions, and where it lies. A chat session is only the channel through which a party works on it. The work outlives every session and is committed at every send.

![The work model on one page](work-model.svg)

Fallback, if the diagram does not render:

- Territory work `ki`: the hub, the state of play coordinating the coordinations
  - shows Kris with you, stuck, blocked and on hold
- Two forms of work, side by side beneath it
  - Regular work `ki.regular`: recurring, defined in the Capital, self-coordinating; state of play may discuss it; creates work items
  - Project work `ki.ways-of-working`: finite; worker to Kris, supervisor to its runs; territory work sends direction down and it sends attention up
- Theme `Model`: a label either form, or ad hoc work, can carry; not a level
- Kris, supervisor, to the side: receives with `with me`; Project work sends to supervisor, and Kris replies
- Execution, the lowest level that can do it
  - Work item: a record in any repository, created by either form
  - Run: a worker, queued, running or stuck; brief out, report back
  - Other work `<id>`: in handoff until it receives

---

## Levels and forms of work

Work lies at three levels. Kris named the two forms at the middle one: "regular work and project work. That's the two forms of work that happen, right?"

| Level | Id | What it does | Ends |
| --- | --- | --- | --- |
| Territory work | `ki` | The state of play: coordinates the coordinators, executes nothing | Never |
| Regular work | `ki.regular` | The territory's recurring work, defined in the Capital's Activity notes; self-coordinating; creates work items in any repository; holds ad hoc work as `ki.regular.<slug>` | Never; rests On hold, more expected, between occurrences |
| Project work | `ki.<project>` | Coordinates one Project's work items and runs, and briefs runs | Finished when the Project closes |
| Work item | the record's id | One record in any repository, executed by a run or a person | `done` or `cancelled` |

**Regular work is self-coordinating.** It needs no coordination thread, in Kris's words "because it is sort of self-coordinating, but there's no reason why the state of play thread can't sort of talk about it". An occurrence is started by its schedule or by whoever needs it; state of play may discuss regular work but does not necessarily dispatch it. A Project's own recurring checks, needed only while it runs, stay with the Project and end with it.

**The theme is a label, not a level.** Regular work, Project work or an ad hoc piece of work may carry one. Each theme has a page in `Streams/Themes/` saying why it is a theme, what matters about it, its general direction and the guidance common to the work under it. It holds no work, has no holder and no session, and views group by it. No identifier carries a theme, so relabelling never renames anything.

**The cascade rule.** Work goes down to the lowest level that can do it, and coordination sits above execution:

- territory work coordinates regular work and Project work;
- regular work and Project work each send work items down to any repository, and Project work also briefs runs and hands work to other work;
- only work items, done by runs or people, execute.

Attention comes back up: each level reads the work files beneath it and rolls up the five views.

---

## Roles

Every handoff has a **worker** and a **supervisor**, and the roles are relative to that handoff:

- for territory work and Project work, the coordinating agent is the worker and Kris is the supervisor;
- for a run, the coordinating agent is the supervisor and the run is the worker;
- so a coordinator is worker to Kris and supervisor to its runs at the same time.

A stuck worker comes back to its supervisor: it sends the work back with a blocking query. Kris's own work, while the work lies with Kris, may be to read a report, answer a query or edit a document directly.

The **holder** is the party the work lies with now, derived from the state and the two roles and named `owner`, `agent`, `run/<name>`, `work/<id>`, `person/<handle>` or `repo/<name>`.

There are two moves, and only the holder may make either: to **send** puts the work into handoff to a target, and to **receive** takes it out of handoff and makes it with you. A message mid-run is a steer and moves nothing. Putting work on hold and taking it off are agreed rather than sent.

---

## The seven states

Kris named four kinds of state: "It's either with someone or it's been handed off to someone or we've agreed effectively that it's like on hold ... or we can say it's done, at which point that area is concluded." The seven states take those kinds and the role words.

| Kind | State | When | Whose move |
| --- | --- | --- | --- |
| with someone | With worker | any item with a run, or the coordinator mid-turn | worker |
| with someone | With supervisor | the supervisor has received it | supervisor |
| handed off | Handoff to supervisor | the worker has sent, and the supervisor has not received | supervisor |
| handed off | Handoff to worker | the supervisor has replied, and no session has yet received it | worker |
| handed off | Handoff to `<target>` | sent to other work, a run or a person | target |
| on hold | On hold, paused or more expected | agreed and drained: nothing running, queued or in handoff | nobody until its release |
| done | Finished | closed | nobody |

Only the supervisor's receive and the hold are set; every other state is derived from where the work's items lie.

**On hold.** On hold sits between with someone and Finished: the work is not moving, nobody owes a move, and it is not over. It has two reasons:

- **paused**: the work waits while other work goes on, with a named release condition, such as "after the harness migration" or "when Kris says resume";
- **more expected**: the work is done for now, and new work arriving releases it. Regular work rests here between occurrences, and a Project may rest here between waves.

A hold is agreed only from With supervisor: the supervisor says `pause` or `done for now`, and a worker may propose one in its send. The worker then **drains**, letting a run that will finish within about 15 minutes finish, stopping any other at a safe point with where it stopped recorded, and launching nothing new; a drain that cannot finish leaves the work With worker, blocked. The move into On hold is a mark: every repository the work touched is committed and pushed fast-forward, each open query is parked in the work file with its tag, one line of context and its recommended option, the front matter records `state: on-hold`, the reason, the release and since, decisions are struck and the working area tidied. `resume`, or the release condition being met, or new work arriving for more expected, moves it to Handoff to worker; `finish` moves it to Finished.

**Stuck and the heartbeat.** A heartbeat runs only while work lies with a worker: an update on change, at least every 5 minutes and always by 10. A worker's item that has neither moved nor beaten for 10 minutes is stuck; nobody sets stuck. Work with the supervisor is never stuck, only older, so with you is listed oldest first. On hold has no heartbeat, and a paused hold older than 31 days is flagged.

**The same machine one level down.** A work item's record already carries the states in its `status` and `horizon`, so it needs no new fields:

| Work state | Record |
| --- | --- |
| With worker | `in-progress` with horizon `now`, or `draft` while it is being planned |
| Handoff to supervisor | `awaiting-review` |
| With supervisor | `triage`, or `draft` awaiting approval |
| Handoff to worker | `ready` |
| Handoff to `<target>` | `blocked_by` an open record, or horizon `hold` with reason `waiting-for` |
| On hold, paused | horizon `hold` with reason `parked` |
| Finished | `done` or `cancelled` |

Done for now exists only at the work level: a record is finite, and more work is a new record.

---

## Words

| Term | Meaning |
| --- | --- |
| work | the unit: territory work, regular work, Project work or a work item |
| work item | one record, executed by a run or a person; "task" is fine in speech |
| theme | a label on work, with its own page; holds no work |
| work file | `work.md`: the current state, next steps, Messages and parked query tags |
| logbook | the Git history of a work folder |
| decisions | `decisions.md`: Kris's decisions about this work not yet durable elsewhere |
| worker, supervisor | the two roles of one handoff |
| holder | the party the work lies with now, derived |
| handoff | in transit to a named target |
| send, receive | the two moves |
| On hold | the agreed state; "hold" means nothing else |
| paused, more expected | the two reasons for On hold |
| release | what ends a hold: a named condition, or new work arriving |
| drain | the activity on the way into On hold, never a state |
| Finished | closed |
| with you, stuck, blocked, moving, on hold | the five views, by holder |
| `with me`, `ack`, `got it`, `seen` | the supervisor's receive |
| `pause`, `done for now` | the supervisor's receive that agrees a hold, with its reason |
| `resume`, `finish` | the supervisor's moves off hold and to Finished |
| working area | `+` inbound and `-` outbound; not canonical, history not durable |
| mark | the point at which decisions are struck and the working area tidied |

The words are agreed to be proven in use, in Kris's words "We probably just need to see how it comes out in use".

---

## Homes

**The work folder.** Each piece of work above a work item has one flat folder in the working area, `+/_WORK/<id>/`, named by its dotted id. A work item has no folder: its record is its home. Runs keep hyphenated slugs.

**The work file.** `work.md` is the minimal current state. Its front matter carries the fields the observatory reads, below; its body holds next steps, Messages (the directions sent down to it) and the tags of parked queries, each linked to the report that holds it. Nothing else: there is no moves list, because each move is a commit.

**Canonical and working.** `Streams/` holds only definitions and records: Project notes flat in `Streams/Projects/` with a `theme:` key, theme pages in `Streams/Themes/`, and work items in `Streams/Roadmap/`. Everything that churns, the work file, decisions, reports, briefs and design papers, stays in the work folder. Links point upward: the work file names its Project; the Project note does not link down. Briefs sit in `briefs/<run>.md` while their handoff is open. The run state folder, `~/.local/state/ki/agents/<slug>/`, holds only runtime state.

```text
Streams/
├── Streams.md
├── Themes/                                holds no work
│   ├── Themes.md
│   ├── model.md                           theme page: why a theme, what matters, direction, common guidance
│   ├── foundations.md
│   ├── rig.md
│   └── techne.md
├── Projects/                              flat, one note each, theme: key
│   ├── Projects.md
│   ├── ways-of-working.md                 theme: model
│   └── ...
└── Roadmap/                               work item records
+/
├── _WORK/                                 one flat folder per live piece of work
│   ├── ki/                                territory work
│   │   ├── work.md
│   │   └── decisions.md
│   ├── ki.regular/                        regular work
│   │   ├── work.md
│   │   └── decisions.md
│   ├── ki.ways-of-working/                Project work
│   │   ├── work.md
│   │   ├── decisions.md
│   │   ├── <run>.report.md                open reports only
│   │   ├── briefs/<run>.md                while its handoff is open
│   │   └── design/                        design papers
│   └── ...
├── _TRADES/
└── diagrams/
```

**Git is the logbook.** `git log -- +/_WORK/<id>/` is the history. Only sends and the supervisor's receives commit, each subject carrying the move: `docs(work): ki.ways-of-working send to owner`, `docs(work): ki.ways-of-working receive by owner`, `docs(work): ki.ways-of-working hold, paused`. An agent's receive is committed with whatever it next sends.

**Shared history is never rewritten.** A rewrite breaks every clone and every revision link and needs a force-push. Instead, the working area is pruned at every mark, a finished work folder is deleted at the mark that closes it with Git keeping it, and a separate working repository is considered only if clone size or `git log` speed measurably hurts.

---

## Decisions life cycle

`decisions.md` stays apart from the logbook: a re-bootstrap must read the live decisions whole, and Git history cannot be struck.

- **Logged:** a decision Kris makes about this piece of work, in Kris's words, in the turn it arrives.
- **Not logged:** a relay from other work, which is a receive; an instruction to other work, which is a send; an operational event such as a push, a restart or a drain, which is a move. These are commits.
- **At each mark:** each entry is checked against its durable home and then struck, when a standard, skill, note, record, Decision Record or commit wholly carries it; reduced to a one-line pointer (tag, Kris's date, link), when it still governs live work whose home is elsewhere; or kept. A struck entry leaves no stub, and entries carry no running numbers.

---

## Banner

A report shows its state in rich text. The heading's glyphs come first and the last glyph is whose move it is: 🤖 an agent, 👤 Kris, 🎯 a named target, ⏸️ nobody until the release, 🏁 nobody. A settled state shows its holder's glyph alone: `🤖 With worker`, `👤 With supervisor`, `⏸️ On hold`, `🏁 Finished`. An arrow appears only in a handoff state, pointing to whose move it is: `🤖 → 👤 Handoff to supervisor`, `👤 → 🤖 Handoff to worker`, `→ 🎯 Handoff to <target>`. The heading gives the state in role words; a line of counts follows; then the list `- [state] what · holder · since`. The counts and lists say "with you", because they are views by holder. The report's form line takes the same prefix, as in **🤖 → 👤 Handoff to supervisor · Summary at 23:52 BST · last mark 22:34 BST**.

An example of work with its worker:

> ### 🤖 With worker · since 23:41 BST
>
> 🤖 2 running · 👤 1 with you · ⛔ 1 blocked
>
> - [running] work-model · run/work-model · since 23:20
> - [with you] WORK-HOME · owner · since 22:58
> - [blocked] thread commit · repo/ki-principal · since 22:40

And on hold:

> ### ⏸️ On hold · paused until the harness migration lands · since 00:10 BST
>
> ⏸️ drained · 👤 0 with you · 🅿️ 9 queries parked
>
> - [on hold] committed and pushed in ki-principal and ki-agentic-harness · since 00:10
> - [release] after the harness migration lands, or `resume`

The other headings follow the same form: `👤 With supervisor`, `🤖 → 👤 Handoff to supervisor`, `👤 → 🤖 Handoff to worker`, `→ 🎯 Handoff to <target>`, where the target is other work, a run or a person, `⏸️ On hold · more expected` and `🏁 Finished`. A stuck worker's send reads `🤖 → 👤 Handoff to supervisor · blocked`. The send line appears only when the work is in handoff to Kris, and it and the resume name the checkout their session must be grounded in, the primary checkout of the repository holding the work file; on hold, the hold report gives the resume that lifts it. The hold report keeps its name and its Done, Parked and Left over sections.

**Answers.** An owner report carries no copyable reply block. Each query keeps its Context, its one-sentence Query and its lettered Options, the recommended option first with its confidence. Kris answers in speech; the worker reads each answer back as taken in the decisions log and asks one line where an answer is unclear.

---

## Observatory fields

The Observatory reads work state only through the `ki` command surface: `ki work status --format json`, schema `ki/work-status/v1`, one entry per work file in each selected territory. Paths are repository-relative.

| Field | Meaning |
| --- | --- |
| `identity` | the registered repository holding the work file |
| `id` | the dotted work id, such as `ki.ways-of-working` |
| `level` | `territory`, `regular` or `project` |
| `title` | the display title |
| `theme` | the theme label, or null |
| `worker`, `supervisor` | the two parties, such as `agent` and `owner` |
| `state` | `with-worker`, `handoff-to-supervisor`, `with-supervisor`, `handoff-to-worker`, `handoff`, `on-hold` or `finished` |
| `hold` | while on hold, `reason` (`paused` or `more-expected`) and `release`, the condition in words; else null |
| `holder` | the party it lies with now |
| `role` | the holder's role, `worker` or `supervisor`, or null for another target |
| `target` | the named target while in handoff, else null |
| `blocking` | true when a worker has sent back with a blocking query |
| `since` | UTC time of the last move |
| `received` | UTC time of the supervisor's receive, or null |
| `beat` | UTC time of the last heartbeat while with a worker, or null |
| `path` | the repository-relative path of `work.md` |
| `items` | each item below it: `id`, `kind`, `holder`, `role`, `state`, `target`, `blocking`, `since` |

The five views are derived by stated rules: **with you** is every work or item whose holder is `owner`, oldest `since` first; **stuck** is a worker-held item whose later of `since` and `beat` is more than 10 minutes old; **blocked** is `blocking` true or the roadmap's own blocked signal; **on hold** is `state` `on-hold`, a paused hold flagged after 31 days; **moving** is the rest. Work items are read through the Observatory's existing roadmap read and need no new field.
