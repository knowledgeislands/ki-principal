# [Knowledge Islands model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/knowledge-islands-model/knowledge-islands-model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working/ways-of-working.md) › work-model

**Run report at 00:02 BST · last mark 22:34 BST**

---

## Done

- Brought the [thread-states report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/thread-states.report.md), the [work-cascade report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/work-cascade.report.md) and Kris's CONVERSATIONS-FOLDER and WORK-UNIT words of 17 October into one model. Where I choose between them, the section says so and why.
- Revised in place by `work-model-rev` to fold in Kris's WORK-LEVELS, SETTLE-MODEL and WORKING-AREAS words of 17 October 23:43 to 23:45 BST, read verbatim in the [decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/decisions.md). Section 0 shows what each point changed and which points the first version had already covered. Section 9, Settling it, is new.
- Revised again by `work-model-hold` to fold in Kris's WORK-STATES idea of 17 October 23:50 BST: On hold is a fourth kind of state, between with someone and Finished, with two reasons. Section 1 models it and maps the work states onto the roadmap item statuses; section 2 gives "hold" one meaning; section 6 renders it; WORK-MODEL and WORK-WORDS carry it. The diagram shows levels and roles, not states, so only its list label gains "on hold", edited in the SVG and its Archify source and checked by eye through `rsvg-convert`.
- Read the whole decisions log and sorted every entry for the worked example in section 4. The sort was made from the log and the report trail, not checked line by line against each durable home.
- Redrew the Archify diagram for the new levels and roles, exported it through the `ki-diagrams` exporter, flattened it to static light SVG with the one-off script `diagram-fix` left, and checked it by eye through `rsvg-convert`. It reads cleanly. A nested-list fallback sits under it, and its source is beside this report.
- Read [apps-observatory.local](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local) read-only for the observatory contract in section 9.
- This is counsel for discussion. No standard, skill, hook, style, record or checkpoint was changed. Only this report, its SVG and its Archify source are committed.

### 0. What Kris's work-levels words change

| Kris's point | Already covered? | Where it lands now |
|---|---|---|
| The chat session is just a channel | Yes, section 1 said so | Left as it was |
| Project definitions and work items stay in `Streams/`; the working area is not durable | Yes, section 3's canonical-zone boundary | Left; Kris's words now quoted there |
| Territory work is state of play, "the coordinations of the coordinations" | Mostly: the territory level read every head | Section 1 names it territory work and says it coordinates coordinators |
| Levels: territory, theme or area, Project | In part: Initiative existed only on demand, with no session | Changed: theme is a label, not a level (section 1, WORK-THEME) |
| "A roadmap item can also have work associated to it ... I think it is just work" | No: the first version said "nothing says work item" | Changed: the work item is the lowest level, and its record's status is its state (section 1) |
| Work cascades to the lowest level that can do it; coordination sits above execution | No | New rule in section 1 |
| "There is always a common project, which is regular activities" | No | Counsel in section 1 and WORK-REGULAR: a standing home under the territory, not a Project |
| The logbook may be the Git history, decisions may be part of it, and not every transition needs logging | No: the first version kept a moves list in `logbook.md` | Changed: Git is the logbook and `work.md` holds only the current state (section 3); decisions stay apart (section 4) |
| Kris's own work may be reading a report or editing a document | Implicitly | Section 1: an item with the supervisor can be any of these |
| `+` and `-` are working areas | No | Settled by Kris at 23:45 BST and dispatched to `working-areas`; recorded in section 2, so no query |
| Recompressing Git history now and then | No | Counsel against in section 5, with safer alternatives (WORK-HISTORY) |
| Worker and supervisor; a stuck worker comes back to its supervisor | No: holders were agent and owner | Changed: roles are relative per handoff, and the banner words follow (sections 1, 2, 6) |
| Settle it once and get it into the observatory | No | Section 9: complete queries, the durable home, the migration and the observatory contract |
| WORK-STATES: with someone, handed off, on hold (paused, or done for now with more to come), or done; "very similar to the roadmap item statuses, but it's a higher level" | In part: hold was only a receive word that drained | New: On hold is a state with two reasons and a release (section 1), mapped onto the roadmap statuses and horizons (section 1), "hold" given one meaning (section 2), and rendered (section 6) |

### 1. The model on one page

**Work** is the unit, as Kris said on 17 October: "the unit is work, not a conversation". A piece of work carries four things:

- what is being worked on;
- its current state, in one small work file;
- its own **decisions**;
- where it lies: **with** its worker or its supervisor, in **handoff** to a named target, **on hold** by agreement, or **finished**.

Its **logbook** is the Git history of its folder, as Kris put it: "The logbook could be the gate history. Yeah, I think it's probably the Git history." A chat session is only the channel through which a party works on it. The work outlives any session and is committed at every send.

**Levels.** Kris named the cascade on 17 October 23:43 BST. My counsel keeps three levels where work can lie, and makes the theme a label:

- **Territory work:** `ki`, the state of play. It coordinates the coordinators and executes nothing.
- **Project work:** `ki.ways-of-working`. It coordinates its work items and runs, and it is finite: it closes.
- **Work item:** one record, such as [KI-HARNESS-GOV-199](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-199-thread-identity-role-native-sessions.md). It is execution, done by a run or a person. Its record's status already is its state, so it gets no work file of its own.
- **Theme:** `Model`, a label on Projects with a direction note. It holds no work, has no holder and no session, and views group by it.
- **Regular activities:** `ki.regular`, a standing home beside the Projects, under the territory. It never closes and has no coordinator of its own; state of play dispatches each occurrence, as ACT-THREAD already decided. Ad hoc work with no Project lies here until it earns one.

Why the theme is a label: Kris called it "just a theme banner", and the first version had already found that an Initiative needs no session. A level that never holds anything is a grouping, and a grouping need not own folders or ids.

**The cascade rule.** Work goes down to the lowest level that can do it. Coordination sits above execution:

- territory work coordinates Project work and regular activities;
- Project work coordinates work items and runs;
- only work items, done by runs or people, execute.

Attention comes back up. Each level reads the work files beneath it and rolls up five lists: with you, oldest first; stuck; blocked; moving; on hold.

**Roles.** Every handoff has a **worker** and a **supervisor**, and the roles are relative to that handoff:

- for territory work and Project work, the coordinating agent is the worker and Kris is the supervisor;
- for a run, the Project's coordinating agent is the supervisor and the run is the worker;
- so the coordinator is worker to Kris and supervisor to its runs at the same time.

A stuck worker comes back to its supervisor: it sends the work back with a blocking query, as Kris said, "when a worker gets stuck, they come back to the supervisor". Kris's own work, while the work lies with Kris, may be to read a report, answer a query or edit a document directly.

**Holders.** A holder is the party the work lies with now. It is derived from the state and the two roles, and named as before: `owner`, `agent`, `run/<name>`, `work/<id>`, `person/<handle>`, `repo/<name>`.

**Moves.** There are two verbs, and only the holder may make either:

- to **send** is to put the work, or one of its items, into handoff to a target;
- to **receive** is to take it out of handoff and make it with you.

The rules the thread-states report settled carry over: a message mid-run is a steer and moves nothing; a reply moves through With supervisor on its way; finishing is a move to Finished. Two more are agreed rather than sent: putting work on hold, and taking it off.

**States.** Kris named four kinds of state on 17 October 23:50 BST: "It's either with someone or it's been handed off to someone or we've agreed effectively that it's like on hold ... or we can say it's done, at which point that area is concluded." The states take those kinds and Kris's role words:

| Kind | The work's items | State | Whose move |
|---|---|---|---|
| with someone | any item with a run, or the coordinator mid-turn | With worker | worker |
| with someone | the supervisor has said `with me`, `ack`, `got it` or `seen` | With supervisor | supervisor |
| handed off | the worker has sent, and the supervisor has not received | Handoff to supervisor | supervisor |
| handed off | the supervisor has replied, and no session has yet received it | Handoff to worker | worker |
| handed off | sent to other work, a run or a person | Handoff to `<target>` | target |
| on hold | agreed and drained: nothing running, nothing queued, nothing in handoff | On hold · paused, or On hold · more expected | nobody until its release |
| done | closed; "that area is concluded" | Finished | nobody |

The supervisor's receive and the hold are the only states that are set rather than derived. Everything else is derived from where the items lie.

**On hold.** On hold sits between with someone and Finished: the work is not moving, nobody owes a move, and it is not over. It has two reasons, both Kris's:

- **paused**: "the work can be paused for now and we're working on something else". It names a release condition, such as "after the harness migration" or "when Kris says resume". This is what a ki-pmo hold is today: a move between hosts, or the thread closed for a period.
- **more expected**: "all the work is done, but we know there's going to be more to come into this". Its release is new work arriving. Regular activities rest here between occurrences, and a Project can rest here between waves.

What moves it in:

- only from With supervisor, because a hold is agreed and the supervisor is the party who agrees. The supervisor says `pause` or `done for now`; a worker may propose a hold in its send, and the supervisor's receive with `pause` or `done for now` agrees it in one move.
- the worker then **drains**: it lets a run that will finish within about 15 minutes finish, stops any other at a safe point with where it stopped recorded, and launches nothing new. A drain that cannot finish leaves the work With worker, blocked, and says why.

What a move into On hold persists. It is the natural drain point, so it is also a mark:

- every repository the work touched is committed and pushed fast-forward, and any other session's commit or dirty file is named, not touched;
- each open query is parked in the work file with its tag, one line of context and its recommended option, with every held and waiting-on item and the next steps;
- the work file's front matter carries `state: on-hold`, the reason, the release condition and since;
- decisions are struck to their live entries and the working area is tidied, as at any mark;
- one commit carries it, `docs(work): <id> hold, paused` or `docs(work): <id> hold, more expected`, and the hold report is the send that announces it.

What moves it out:

- **resume**, by the supervisor, or the release condition being met: the work moves to Handoff to worker, and the worker re-reads the work file, puts the parked queries back and starts. This is today's resume line.
- **new work arriving**, for more expected only: a message, an Activity occurrence or a new item sent into it moves it to Handoff to worker in the same way.
- **finish**, by the supervisor: On hold to Finished, with the close-out tidy. Done for now often ends here.

On hold has no heartbeat and is never stuck. A paused hold older than 31 days is flagged in the on hold list, borrowing the roadmap checker's warning for a stale held record.

**The same machine one level up.** Kris: "that kind of maps very similar to the roadmap item statuses, but it's a higher level, right?" It does. A work item's record already carries the machine, in two fields that `ki-work-roadmap` keeps apart: `status` says how far work has got, and `horizon` says when it is intended, with `hold` one of its horizons. So work items need no new fields:

| Work state | Record, under `ki-work-roadmap` | Note |
|---|---|---|
| With worker | `in-progress`, horizon `now`; or `draft` while `ki-plan` shapes it | |
| Handoff to supervisor | `awaiting-review` | the review packet is the send |
| With supervisor | `triage`, or `draft` awaiting approval | adoption and plan approval are the supervisor's moves |
| Handoff to worker | `ready` | changed from the first version: ready means the supervisor has approved the plan, so the next move is the worker's |
| Handoff to `<target>` | `blocked_by` an open record, or horizon `hold` with reason `waiting-for` | |
| On hold · paused | horizon `hold` with reason `parked` | |
| On hold · more expected | none | see below |
| Finished | `done` or `cancelled` | |

Its since is `updated_at`. Where the two levels differ:

- **Hold is a state up here and a horizon down there.** A held record keeps its status, so `in-progress` on hold is one record in two fields. Work is drained on the way in, so nothing is left in flight to keep, and one field suffices.
- **Waiting is not holding.** The roadmap's `waiting-for` reason is a hold on an external condition. Up here, waiting on a named party is Handoff to `<target>`, because someone owes the move; On hold means nobody does. The roadmap's `parked` is the true match for paused.
- **Done for now exists only up here.** A record is finite: when its outcome lands it is `done`, and more work is a new record. Territory work, Project work between waves and regular activities do accrue more, so they need a resting state that is not an ending.
- **One ending, not two.** The roadmap ends `done` or `cancelled` with a resolution. Work ends Finished; the closing commit says whether the area concluded or was abandoned.
- **Holds are agreed up here and approved down there.** A record's move to `hold` is a `ki-next` selection the owner approves; a work hold is the supervisor's word in a receive. Both need the supervisor, so the authority is the same.
- **Release is shared.** Both name a release condition; the work level borrows the roadmap's rule that a hold says what ends it.

**Stuck and the heartbeat.** A heartbeat runs only while work lies with a worker: an update when something changes, at least every 5 minutes, and always by 10. An item with a worker that has neither moved nor beaten for 10 minutes is stuck. Nobody sets stuck. Work with the supervisor is never stuck, only older, so with you is listed oldest first. Work on hold has no heartbeat.

![The work model on one page](work-model.svg)

Fallback, if the diagram does not render:

- Territory work `ki`: the state of play coordinates the coordinations
  - dispatches occurrences to regular activities `ki.regular`, the standing home, no Project
  - sends direction down to Project work
  - shows Kris with you, stuck, blocked, moving and on hold
- Theme `Model`: a label around Project work, not a level
  - Project work `ki.ways-of-working`: worker to Kris, supervisor to its runs
    - sends attention up
    - send: handoff to supervisor, Kris
- Kris, supervisor: receives with `with me`, and sends by replying (handoff to worker)
- Execution, the lowest level that can do it
  - Work item: a record, ready, in progress or in review
  - Run: a worker, queued, running or stuck; brief out, report back
  - Other work `<id>`: in handoff until it receives

### 2. Vocabulary

| Term | Meaning | Replaces today | Collision |
|---|---|---|---|
| work | the unit: territory work, Project work, regular activities or a work item, with its id | thread, conversation, checkpoint | ki-work's "forward work", which now means the same thing |
| territory work | the territory's own coordination, read as the state of play | the `.sop` thread | none; the `.sop` id retires to `ki` |
| Project work | a Project's coordination; finite | coordination thread | none |
| work item | the lowest level: one record, executed by a run or a person; "task" is fine in speech | roadmap item, record in speech | none in practice: the Observatory's contract already calls it `WorkItem` and the Observatory's `ROADMAP.md` says "work items"; "record" stays for the file |
| regular activities | the territory's standing home for recurring Activities and ad hoc work; never closes | Initiative as the home of recurring work | an Activity note keeps its name |
| theme | a label grouping Projects, with a direction note; holds no work | Initiative | the record-level `theme` field retired on 7 October, still optional in tools-ki's reader and carried as `theme` in the Observatory's `WorkItem`; a record's theme would be derived from its Project |
| Model, Foundations | the short titles of themes | knowledge-islands-model, platform-foundations | none |
| work file | `work.md`: the current state in front matter, then next steps, Messages and parked query tags | checkpoint, pick-up block, the first version's "head" | "head" dropped, because it collides with Git's HEAD once Git is the logbook |
| logbook | the Git history of the work's folder | checkpoint moves, the first version's `logbook.md` | none |
| decisions | `decisions.md`: Kris's decisions about this work not yet durable elsewhere | decisions log | Decision Records; prose says "decisions log" for this one |
| worker | the party doing the work on a handoff | agent, "with agent" | none |
| supervisor | the party a worker answers to and comes back to when stuck | owner, "with you" | none |
| role | worker or supervisor, relative to one handoff | none | [KI-HARNESS-GOV-199](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-199-thread-identity-role-native-sessions.md)'s session role (coordinator or conversational); prose says "session role" for that one |
| holder | the party the work lies with now, derived | owner or dependency, in In Progress | ki-work's record owner; a holder is a place, not an owner |
| handoff | in transit to a named target, with its sender | Sent, `[waiting]`, resume line | none; Kris's word |
| send, receive | the two moves | "hand off", "return", ack, pick up | none |
| With worker | state: the move is the worker's | BUSY | none |
| Handoff to supervisor | state: sent, not yet received | REST with open queries | none |
| With supervisor | state: the supervisor has received it | none | none |
| Handoff to worker | state: the supervisor has replied | none | none |
| Handoff to `<target>` | state: sent to other work, a run or a person | "blocked on another thread" | none |
| On hold | state: agreed and drained; nobody owes a move until its release | HOLD, the ki-pmo drained-thread state | the roadmap's `hold` horizon, which maps onto it: its `parked` reason is paused, its `waiting-for` reason is a handoff |
| paused, more expected | the two reasons for On hold | the hold's "move between hosts or close for a period" | none |
| release | what ends a hold: a named condition, or new work arriving | resume line | the roadmap's release condition, which means the same |
| Finished | state: closed | DONE | ki-work's `done` and `cancelled` statuses, which map onto it |
| with you, stuck, blocked, moving, on hold | the five view lists, by holder, across work | `[waiting]` and `[held]` items | none |
| `with me`, `ack`, `got it`, `seen` | the supervisor's receive | none | none |
| `pause`, `done for now` | the supervisor's receive that agrees a hold, with its reason | `hold`, as a receive word and as a request to drain | none |
| `resume` | the supervisor's move off hold | resume | none |
| `finish` | the supervisor's move to Finished | close | none |
| drain | the activity on the way into On hold | drain | none: it stays an activity, never a state |
| working area | `+` inbound and `-` outbound; not canonical, history not durable | staging area | settled by Kris on 17 October 23:45 BST, "Staging is just a state that a piece of work can be in"; "zone" stays for the five canonical zones; `working-areas` is applying it |
| mark | the point at which decisions are struck and the working area tidied | mark | none |

**One meaning for "hold".** Today the word carries four:

- the ki-pmo glossary's hold, "a mark plus stopping all work", the drained-thread state behind the HOLD frame and the hold report;
- this report's first versions, where `hold` was a supervisor receive word that also drained;
- the roadmap's `hold` horizon, with reasons `waiting-for` and `parked`;
- Kris's THREAD-STATES words, "hold means I've read and accepted it and I'm putting my responses on hold".

My counsel: **hold means On hold, the agreed state, and nothing else.** The ki-pmo state is the same thing, a paused hold, so it keeps the word and gains the second reason; its drain stays the activity into it and its hold report stays the send that announces it. The roadmap horizon is the same machine one level down and keeps its word too. What retires is `hold` as a receive word: receiving and holding are different moves, and one word for both is why a received report and a drained thread read alike. The supervisor receives with `with me`, `ack`, `got it` or `seen`, agrees a hold with `pause` or `done for now`, which receives in the same move, and lifts it with `resume`. THREAD-STATES's sense, read and accepted, is With supervisor; putting responses on hold is `pause`.

### 3. Where it lives

**The folder.** `+/_WORK/<id>/`, in the working area, named by the dotted id: `+/_WORK/ki/`, `+/_WORK/ki.ways-of-working/`, `+/_WORK/ki.regular/`. Ad hoc work is `ki.regular.<slug>`, which shows its home and cannot collide with a two-part Project id. A work item has no folder: its record is its home.

- I chose `_WORK` over Kris's `_CONVERSATIONS` because WORK-UNIT came after CONVERSATIONS-FOLDER and moved the unit to work.
- The id drops the theme segment, so `ki.model.ways-of-working` becomes `ki.ways-of-working`. A label must not be part of an identity, or relabelling a Project would rename it. This departs from THREAD-IDS-AGREE's three-part id and goes with WORK-THEME.
- Runs keep hyphenated slugs, because `ki agent` refuses dots in a run name.

**Flat, not nested.** A nested folder moves when its parent is renamed, and a flat folder needs only its id to be found.

**In `+/`, not beside the note.** Kris confirmed the boundary: "anything that's on the plus and minus, historically, can go because it's not really durable knowledge and that's why it's important that the project definition and that the roadmap items sit under streams". So the work file and decisions stay in `+/_WORK/`, and the Project note in `Streams/` stays slim. This reverses DECISIONS-HOME a) within SHAPE-AGREE.

**Links point upward.** The work file names its Project and links to the note; the note does not link down into the working area. `ki` finds the folder from the id.

**The work file.** `work.md` is the minimal current state that remains once Git is the log. Its front matter is the observatory contract of section 9: id, level, title, theme, worker, supervisor, state, holder, target, hold reason and release, since, received, mark and the items below it. Its body has three parts:

- next steps;
- Messages, the directions sent down to it, keeping that name so it does not collide with the `ki agent` inbox;
- the tags of parked queries, each linked to the report that holds it.

Nothing else. No moves list: each move is a commit, and `git log -- +/_WORK/<id>/` is the logbook. Kris's "we don't need to know everything about every state transition" is met because only sends and the supervisor's receives commit.

**Commit subjects carry the move.** `docs(work): ki.ways-of-working send to owner`, `docs(work): ki.ways-of-working receive by owner`, `docs(work): ki.ways-of-working hold, paused`. An agent's receive is committed with whatever it next sends in the same turn.

**Briefs move in.** A brief goes in `+/_WORK/<id>/briefs/<run>.md` while its handoff is open and is deleted once the report is received; Git keeps it. This reverses THREADS-CONTENT's briefs in the state folder.

**The run state folder.** `~/.local/state/ki/agents/<slug>/` stays runtime-only: status, process id, logs, queue and worktrees. Losing it loses no knowledge.

**What retires from today's checkpoint:** the Thread working rules (the standards carry them), Decisions made (to `decisions.md`), Files touched (Git), Open questions (parked tags), Objective (the Project note's Outcome), and the moves list (Git).

### 4. Decisions life cycle

**Decisions stay apart from the logbook.** Kris wondered whether decisions could be part of the logbook. My counsel is no: a re-bootstrap must read the live decisions whole, in Kris's words, and a strike needs a current file to strike from. Git history cannot be struck and is slow to read. So `decisions.md` stays, small, and Git keeps every struck line.

**What is logged.** A decision is logged when Kris says it about this piece of work, in Kris's words, in the turn it arrives. Not logged:

- a message or answer relayed from other work, which is a receive;
- an instruction to other work, which is a send;
- an operational event, such as a push, a restart or a drain, which is a move.

Those are commits, with the move in the subject.

**At each mark,** each entry is checked against its durable home and then struck (wholly carried by a standard, skill, note, record, Decision Record or commit), reduced to a one-line pointer (tag, Kris's date, link) if it still governs live work whose home is elsewhere, or kept. A struck entry leaves no stub, and the log carries no running numbers.

**Worked example: this run's log, now 199 entries.**

| Outcome at the next mark | Count | Which |
|---|---:|---|
| Not decisions under the model; they are moves, which Git records | 29 | <ul><li>relays from state of play and other threads, which are receives;</li><li>handoffs to and from other threads, such as HANDED-OFF and SOP-DROPPED, which are sends;</li><li>operational events, such as PUSH, RESTART-PROXY, MARK-REISSUE, MARK-FIRST, DRAIN-SOL, RESUME-SOL and GATE-FIX</li></ul> |
| Reduced to a pointer | 8 | <ul><li>PAPERCLIP-REQ, held until Wave F;</li><li>the PUSH-THREAD standing push permission of 13 October;</li><li>LINK-LEVEL;</li><li>SHAPE-FREEZE;</li><li>SESSION-IDENTITY and SESSION-ROLE, both entries, pointing to [KI-HARNESS-GOV-199](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-199-thread-identity-role-native-sessions.md);</li><li>REPLY-FORMS</li></ul> |
| Kept | 18 | <ul><li>Kris's open discussions of 13 October;</li><li>PRIORITIES;</li><li>ROUTINE;</li><li>the 22:50 BST answers, reduced to their pending items (SHAPE-AGREE, HARNESS-ACCEPT, CHEZMOI-APPLY);</li><li>THREAD-LIFECYCLE;</li><li>THREAD-STATES to WORK-LEVELS and SETTLE-MODEL, the twelve ideation entries, struck once the model is written in;</li><li>WORKING-AREAS, the question, until its answer lands</li></ul> |
| Struck | 144 | everything else, including WORKING-AREAS settled once `working-areas` lands |

That leaves 26 of 199 entries, about 13 per cent. A real strike would check each durable home before removing anything.

### 5. Git history

Kris floated recompressing Git history now and then, and was right to be wary: "It could be quite catastrophic." My counsel is not to rewrite shared history at all:

- **Every clone breaks.** Terra and Sol each hold a checkout, and other sessions commit concurrently. A rewrite forces every checkout to be reset, and any unpushed work on the other machine is stranded.
- **Every revision link breaks.** The ki-pmo standard links a pruned record as `blob/<last revision>/<path>`, and reports cite commit identifiers. A rewrite makes all of those dead links.
- **It fights the safety rules.** Rewriting needs a force-push, which every brief forbids.
- **Little is gained.** The working area is Markdown, and Git compresses it well.

Safer alternatives, in order:

1. **Prune the working area at every mark.** Delete settled reports and struck work folders from the tree, as THREAD-TIDY already does for thread folders. The tree stays small, and Git keeps the history without anyone reading it.
2. **Measure first.** Only if clone size or `git log` speed measurably hurts, consider the next step.
3. **A separate working repository.** Move `+/_WORK/` into a per-territory working repository whose history nobody cites as canonical. That repository can be archived and restarted without touching the Capital. A working branch is weaker: tools and Obsidian read the default branch, and it doubles every pull.

Local size, if it ever matters on one machine, is a `git gc` or partial-clone question, not a history rewrite.

### 6. Banner

There is one form. The glyphs come first and the last glyph is whose move it is: 🤖 an agent, 🧑 Kris, 👤 another person, ⏸️ nobody until the release, 🏁 nobody. The words give the state and, where it helps, the holder.

The report heading's form line takes the same prefix:

**🤖 → 🧑 Handoff to supervisor · Summary at 23:52 BST · last mark 22:34 BST**

The footer replaces the block-letter frame with one heading, one line of counts, and the list `- [state] what · holder · since`. The counts and lists say "with you", because they are views by holder; the heading says the state, in role words.

### 🤖 With worker · since 23:41 BST

🤖 2 running · 🧑 1 with you · ⛔ 1 blocked

- [running] work-model · run/work-model · since 23:20
- [running] tools-burndown fix · work/ki.tools-burndown · since 23:05
- [with you] WORK-HOME · owner · since 22:58
- [blocked] thread commit · repo/ki-principal · since 22:40

### 🤖 → 🧑 Handoff to supervisor · since 23:52 BST

🧑 9 with you · ⛔ 1 blocked

- [with you] WORK-MODEL · owner · since 23:52
- [blocked] thread commit · repo/ki-principal · since 22:40

### 🧑 With supervisor · received 07:40 BST · 4 items, oldest since Tue 18:10

🧑 4 with you · ⚠️ 1 stuck · ⛔ 2 blocked · 🤖 3 moving

- [with you] HARNESS-ACCEPT · owner · since Tue 18:10
- [stuck] KI-HARNESS-GOV-199 review · repo/ki-agentic-harness · since Wed 09:00

### 🧑 → 🤖 Handoff to worker · since 07:55 BST

🤖 nothing running yet · 🧑 0 with you

- [handoff] reply block of 07:55 · agent · since 07:55

### 🤖 → 🤖 Handoff to KI > Tools burndown · since 23:10 BST

🤖 1 elsewhere · 🧑 0 with you

- [handoff] gate fix · work/ki.tools-burndown · since 23:10

### 🤖 → 👤 Handoff to a reviewer · since 15:00 BST

👤 1 with another person · 🧑 0 with you

- [handoff] site copy review · person/<handle> · since 15:00

### ⏸️ On hold · paused until the harness migration lands · since 00:10 BST

⏸️ drained · 🧑 0 with you · 🅿️ 9 queries parked

- [on hold] committed and pushed in ki-principal and ki-agentic-harness · since 00:10
- [parked] WORK-MODEL to WORK-SETTLE, in the work file
- [release] after the harness migration lands, or `resume`

### ⏸️ On hold · more expected · since Fri 17:00

⏸️ drained · 🧑 0 with you

- [on hold] regular activities, between occurrences · since Fri 17:00
- [release] the next Activity occurrence, or new work sent in

### 🏁 Finished · Ways of working closed at 18:00 BST

- [finished] 14 work items accepted, folder pruned

A stuck worker's send reads `🤖 → 🧑 Handoff to supervisor · blocked`. The resume line becomes the send line and appears only when the work is in handoff to Kris; on hold, the send line is the resume that lifts it, given in the hold report. The hold report keeps its name and its `Done`, `Parked` and `Left over` sections under the On hold heading. The block-letter frames retire when the model is written in; past reports keep theirs, and so does this one.

### 7. What retires, and the migration

Each item is one line and goes into SHAPE-AGREE's single migration after the restart. Nothing is applied now.

- `+/_CHECKPOINTS/` and `+/_THREADS/` become `+/_WORK/<dotted id>/`, with `work.md`, `decisions.md`, reports and open briefs.
- `ki-checkpoint` becomes the work-file skill.
- The pick-up block becomes the work file's front matter, and the moves list goes to Git.
- REST, BUSY, HOLD and DONE frames become the glyph heading; `[waiting]` becomes `[with you]`; `[hold]` becomes `[on hold]` with its reason and release.
- The ki-pmo glossary's hold is redefined as On hold with its two reasons, drain stays its activity, and `hold` leaves the receive words.
- The resume line becomes the send line.
- The `.sop` id becomes `ki`; Project ids drop the theme segment.
- Initiative becomes theme: `Streams/Initiatives/` becomes `Streams/Themes/`, Projects stay flat in `Streams/Projects/` with a `theme` key, amending SHAPE-AGREE's nested shape before it runs.
- Recurring work's home becomes regular activities under the territory, amending ACT-HOME's "Initiative stays the default" and [KI-HARNESS-GOV-206](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-206-activity-homes-and-coordination.md).
- DECISIONS-HOME's `decisions.md` in Streams is reversed; THREADS-CONTENT's briefs in the state folder are reversed.
- "Staging area" becomes "working area" in ki-repo-kb, already dispatched as `working-areas`.
- In tools-ki, under [KI-TOOL-KI-CLI-127](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-127-agent-status-live-threads.md): the `thread.status` parser reads `work.md`, a work-status reader gives the section 9 contract, the registry reader reads themes, and the five lists are shown.
- This log is struck to its 26 entries at the first mark after the migration.

### 8. Against these choices

**The strongest objection: theme as a label undoes an agreement hours old.** Kris agreed SHAPE-AGREE's nested shape, with Projects inside Initiative folders, at 22:50 BST, and THREAD-IDS-AGREE's three-part ids. Making the theme a label reverses both before either is applied. I hold to it because Kris's own later words, "it's just a theme banner", describe a label, and because the migration has not run: changing it now costs one brief, while changing it after the migration costs a second migration. If Kris values the agreed shape more, WORK-THEME b) keeps it and still renames the word.

**Other objections, in descending weight:**

- **Regular activities is a Project in all but name.** It differs in two ways that matter: it never closes, and it has no coordinator session. Calling it a Project would force an exception into GDR-KI-PRINCIPAL-005's rule that a Project is finite, which is why WORK-REGULAR keeps it apart.
- **Two places for one piece of work.** A Project has a note in `Streams/` and a folder in `+/_WORK/`. That is the price of keeping churn out of canonical zones, and `ki` finding the folder from the id closes most of the gap.
- **Role words are longer.** "Handoff to supervisor" is longer than "Handoff to you". The lists still say "with you", so what Kris scans stays short.
- **Commits.** Committing at every send adds commits in a busy evening. Since Git is now the logbook, those commits are the record, not noise.
- **Git as the logbook can only be read with Git.** A reader without the repository, such as the Observatory's browser, cannot see the history. It does not need to: the Observatory reads current state through `ki`, its Activity instrument already derives what moved from Git, and the work file keeps everything a reader needs to act.

### 9. Settling it

Kris, 17 October 23:44 BST: "I really want to bottom this out. I don't want to go back over this again." This section makes one reply final.

**Complete queries.** Every open choice in the model has a query below, and nothing is left implicit:

| Choice | Query |
|---|---|
| the unit, the levels, the cascade rule, relative roles, states including On hold, the mapping to the roadmap, stuck and the heartbeat | WORK-MODEL |
| every word in section 2 | WORK-WORDS |
| Initiative to theme, flat Projects and two-part ids | WORK-THEME |
| the home of recurring and ad hoc work | WORK-REGULAR |
| the folder, the work file, Git as logbook, commit subjects, briefs | WORK-HOME |
| decisions apart from the logbook, and striking | DECISIONS-STRIKE |
| no history rewrite, and the alternatives | WORK-HISTORY |
| the banner form | WORK-BANNER |
| the decision record, the model note, the migration and the observatory contract | WORK-SETTLE |

The working-area name needs no query: Kris settled it at 23:45 BST.

**The durable home, once answered.**

- **One Governance Decision Record,** GDR-KI-PRINCIPAL-009, The work model, in [Admin/Governance/Decisions/](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/Decisions.md), through the [Enactment Process](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Operations/Processes/Enactment%20Process.md) with Kris's answer standing in for a record. It records the decisions and supersedes the ones it replaces: the Checkpoints bullet and the recurring-work home in [GDR-KI-PRINCIPAL-005](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-005-the-roadmap-model.md), amended in place as that record allows; and, from this log, THREADS-CONTENT, THREAD-IDS-AGREE, DECISIONS-HOME, ACT-HOME's default, SHAPE-AGREE's nesting and the banner and frame decisions. No ki-agentic-harness Decision Record governs threads or checkpoints; [ADR-KI-HARNESS-014](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-014-route-state-by-authority-and-durability.md) on routing state by durability stands and agrees with it.
- **One canonical model note,** `Pillars/Philosophy/Model/Processes/Work Process/Work Process.md`, beside the Enactment, Contribution and Acquisition Processes in [Processes](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Processes.md), with its index line added there. It explains the model; the decision record says why. ki-pmo, ki-delegation, the work-file skill, ki-work, ki-repo-kb-activities and ki-work-recurring cite it and do not restate it.

**The write-in, as one migration.** In SHAPE-AGREE's order: the harness checker and standards first, then the tools-ki readers and a `ki` release, then the Capital's folders, work files, decisions logs and ids together, then the other territories, with Personal's handoff carried as ACT-WORK set out.

**The observatory contract.** The Observatory reads only through the `ki` command surface and its own backend, and the browser receives repository-relative paths only, under [PDR-KI-OBSERVA-001](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/decisions/PDR-KI-OBSERVA-001-observatory-beacon-and-bridge.md). Its Roadmap instrument already reads work items, with `status`, `blockedBy`, `updatedAt` and a `theme` field, so work items need no new read. No Observatory record covers work state: its one open record, [KI-OBSERVA-VIS-021](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-021-explain-tool-storage.md), explains tool storage and is unrelated.

What it would read is one tools-ki command, `ki work status --format json`, owned by tools-ki under [KI-TOOL-KI-CLI-127](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-127-agent-status-live-threads.md), schema `ki/work-status/v1`, one entry per work file in each selected territory:

| Field | Meaning |
|---|---|
| `identity` | the registered repository holding the work file |
| `id` | the dotted work id, such as `ki.ways-of-working` |
| `level` | `territory`, `project` or `regular` |
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
| `items` | each item below: `id` (`run/<name>`, `work/<id>`, `person/<handle>` or a record id), `kind`, `holder`, `role`, `state`, `target`, `blocking`, `since` |

The Observatory derives the lists as stated rules, as its Roadmap instrument derives stale: with you is every work or item whose holder is `owner`, oldest `since` first; stuck is a worker-held item whose later of `since` and `beat` is more than 10 minutes old; blocked is `blocking` true or the Roadmap's own blocked signal; on hold is `state` `on-hold`, with a paused hold flagged after 31 days; moving is the rest. In the Beacon, with you and stuck are attention and blocked is blocking, all in its existing "work and review" category. `apps-observatory` is not in this Capital's choreography list, so its record, a Work instrument and a Beacon contributor, is for Kris to have captured there once the tools-ki read lands.

## In Progress

- Nothing of this run is running, and no agent is queued in run `ways-of-working` from it.

### Outstanding - no action requested now

- The diagram again used the one-off flatten script in `/tmp`, which is lost on reboot. [KI-HARNESS-GOV-205](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-205-static-light-diagram-export.md) would make it a supported export.
- `working-areas` is applying Kris's settled WORKING-AREAS answer separately; section 2 assumes it lands.
- Other sessions' files are dirty or untracked in ki-principal, including `+/_THREADS/chezmoi/decisions.md`. They were left alone.

## Queries

These nine supersede every open query in the thread-states and work-cascade reports and the six of this report's first version. Each names the ones it replaces.

### WORK-MODEL - work as the unit, levels, roles and the cascade

**Context:** Section 1 sets out the model. Work is the unit at three levels where it can lie: territory work (state of play, coordinating the coordinations), Project work (finite, coordinating) and the work item (execution, its record's status mapped to the states). Work cascades down to the lowest level that can do it, and attention rolls up in four lists. Every handoff has a worker and a supervisor, relative to it, so the coordinator is worker to Kris and supervisor to its runs; a stuck worker sends back to its supervisor. Kris's WORK-STATES words give four kinds of state: with someone, handed off, on hold and done. Seven states use those kinds and the role words; only the supervisor's receive and the hold are set rather than derived. On hold is agreed from With supervisor, drained on the way in, and has two reasons, paused (for other work, with a named release) and more expected (done for now; released by new work arriving); the move into it is a mark that commits, pushes and parks everything, and resume or new work moves it to Handoff to worker, or finish to Finished. The states map onto a record's `status` and `horizon`: one machine, one level up, differing in that hold is a state here and a horizon there, waiting on a party is a handoff here rather than a hold, done for now exists only here, and `ready` is Handoff to worker. Stuck is a worker's item quiet for 10 minutes; on hold has no heartbeat. This supersedes HANDOFF-SHAPE, CASCADE-SHAPE, INITIATIVE-THREAD and the first version's WORK-MODEL.

**Query:** Should section 1 be agreed as the one model of work?

**Options:**

a) (recommended) Agree section 1 as it stands, with nothing written into standards until WORK-SETTLE's migration.

b) Agree it, but give the theme a standing piece of work and session between territory and Project.

c) Agree it, but keep agent and owner as fixed holders instead of relative worker and supervisor roles.

d) Agree it, but fold done for now into Finished, with new work reopening it, so On hold has the one reason paused.

### WORK-WORDS - the vocabulary

**Context:** Section 2 lists every term. The main choices are: work item for the lowest level, with "task" fine in speech; the work file `work.md` in place of "head", which collides with Git's HEAD; worker and supervisor; the states With worker, Handoff to supervisor, With supervisor, Handoff to worker, Handoff to `<target>`, On hold and Finished, with On hold's reasons paused and more expected and its release; the view lists with you, stuck, blocked, moving and on hold; the receive words `with me`, `ack`, `got it` and `seen`; and the supervisor's `pause`, `done for now`, `resume` and `finish`. "Hold" today means four things: the ki-pmo drained-thread state, this report's earlier receive-with-drain word, the roadmap's `hold` horizon and Kris's "read and accepted" in THREAD-STATES. Section 2 gives it one meaning, On hold the agreed state, which the ki-pmo state and the roadmap horizon already are; `hold` leaves the receive words, `pause` and `done for now` replace it, drain stays the activity and the hold report keeps its name. This supersedes STATE-NAMES, RECEIVE-WORDS, LEVEL-NAME and the first version's WORK-WORDS.

**Query:** Should the vocabulary in section 2 be adopted, with "hold" meaning only the agreed On hold state?

**Options:**

a) (recommended) Adopt section 2 as it stands.

b) Adopt it, but keep "With you" and "Handoff to you" as state words when the supervisor is Kris.

c) Adopt it, but call the lowest level "task" rather than work item.

d) Adopt it, but keep `hold` as the receive word that agrees a hold, in place of `pause` and `done for now`.

### WORK-THEME - Initiative becomes a theme label

**Context:** Kris called the Initiative "just a theme banner". Section 1 makes it a label: no work, no holder, no folder of its own in `+/_WORK/`. Section 7 renames `Streams/Initiatives/` to `Streams/Themes/`, keeps Projects flat in `Streams/Projects/` with a `theme` key, and drops the theme from ids, so `ki.model.ways-of-working` becomes `ki.ways-of-working`. That amends SHAPE-AGREE's nested shape and THREAD-IDS-AGREE's three-part ids before the migration runs. The retired record-level `theme` field would be derived from the Project. Short titles such as "Model" stay, as ACT-NAMES set.

**Query:** Should Initiative become a theme label, with flat Projects and two-part ids?

**Options:**

a) (recommended) Rename Initiative to theme everywhere, keep Projects flat with a `theme` key, drop the theme from ids, and amend SHAPE-AGREE and THREAD-IDS-AGREE within the one migration.

b) Rename it to theme, but keep SHAPE-AGREE's nested folders and three-part ids as agreed.

c) Keep Initiative as the word and the shape.

### WORK-REGULAR - the common home for regular activities

**Context:** Kris said "there is always a common project, which is regular activities". That runs against GDR-KI-PRINCIPAL-005, under which a Project is finite and closes, and against ACT-HOME of 22:50 BST, "never in a Project". Section 1 meets Kris's intent with a standing home, `ki.regular`, beside the Projects under the territory: it never closes, has no coordinator session, and state of play dispatches each occurrence as ACT-THREAD set. Activities name it as their home and may carry a theme label; ad hoc work with no Project lies there as `ki.regular.<slug>` until it earns a Project. This amends ACT-HOME's "Initiative stays the default" and [KI-HARNESS-GOV-206](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-206-activity-homes-and-coordination.md).

**Query:** Should regular activities be a standing home under the territory rather than a Project?

**Options:**

a) (recommended) Make `ki.regular` a standing home under the territory, not a Project, for recurring and ad hoc work, coordinated by state of play, and amend ACT-HOME and KI-HARNESS-GOV-206 to match.

b) Make it a real standing Project in each territory, amending GDR-KI-PRINCIPAL-005's rule that a Project is finite.

c) Keep ACT-HOME as decided, with the theme as the default home, and add nothing.

### WORK-HOME - where a piece of work's files live

**Context:** Section 3 puts each piece of work in a flat folder `+/_WORK/<dotted id>/` in the working area, holding `work.md`, `decisions.md`, its reports and `briefs/` while a handoff is open. `work.md` is the minimal current state: the section 9 fields in front matter, then next steps, Messages and parked query tags. Git is the logbook: there is no moves list, only sends and the supervisor's receives commit, and each commit subject carries the move. Links point up from the work file to its note. This reverses DECISIONS-HOME and THREADS-CONTENT within SHAPE-AGREE, and supersedes LOGBOOK and the first version's WORK-HOME.

**Query:** Should work live in flat `+/_WORK/<dotted id>/` folders with a minimal `work.md` and Git as the logbook?

**Options:**

a) (recommended) Agree section 3 as it stands.

b) Agree it, but keep an append-only moves list in the work file as well as Git.

c) Keep DECISIONS-HOME as agreed, with `decisions.md` beside the Project's note in Streams.

### DECISIONS-STRIKE - decisions apart, struck once durable

**Context:** Kris wondered whether decisions could be part of the logbook. Section 4 keeps `decisions.md` apart, because a re-bootstrap must read the live decisions whole and Git history cannot be struck. At each mark each entry is struck, reduced to a one-line pointer or kept, after checking its durable home; relays, sends and operational events are moves, not decisions. Applied to this log, that leaves 26 of 199 entries. This supersedes the first version's DECISIONS-STRIKE.

**Query:** Should decisions stay in their own file and be struck to their live entries at each mark?

**Options:**

a) (recommended) Agree section 4: a separate `decisions.md`, struck, pointed or kept at each mark, no numbering, first applied to this log at the first mark after the migration.

b) Fold decisions into the Git history as commit messages and keep no decisions file.

c) Strike only at Project close.

### WORK-HISTORY - no history rewrite

**Context:** Kris floated recompressing Git history and was wary it "could be quite catastrophic". Section 5 counsels against any rewrite of shared history: it breaks every clone on Terra and Sol, every `blob/<revision>` link to a pruned record and every cited commit, and it needs a force-push. The safer path is to prune the working area at every mark, measure, and only if size measurably hurts move `+/_WORK/` to a per-territory working repository that can be archived and restarted.

**Query:** Should shared history never be rewritten, with pruning the working area as the remedy?

**Options:**

a) (recommended) Never rewrite shared history; prune the working area at every mark; consider a separate working repository only if size measurably hurts.

b) Move `+/_WORK/` into a separate working repository now.

c) Allow a planned, announced history rewrite once a year with every checkout level first.

### WORK-BANNER - one banner form and the heartbeat

**Context:** Section 6 replaces the block-letter frames with one form: a glyph heading whose last glyph is whose move it is, the state in role words, a line of counts, and the list of items with holder and since. The counts and lists say "with you". The report's form line takes the same prefix. The heartbeat runs only while work lies with a worker: on change, at least every 5 minutes, always by 10. This supersedes BANNER-FORM, HEARTBEAT-PACE and the first version's WORK-BANNER.

**Query:** Should section 6's single banner form and heartbeat replace the frames?

**Options:**

a) (recommended) Adopt section 6 for every state, and retire the frames when the model is written in.

b) Keep the block-letter frame and add the glyph heading above it.

### WORK-SETTLE - the durable home, the migration and the observatory

**Context:** Section 9 settles the model once the other eight are answered: one Governance Decision Record, GDR-KI-PRINCIPAL-009, through the Enactment Process with Kris's answer standing in, superseding the decisions it lists; one model note, `Work Process`, under `Pillars/Philosophy/Model/Processes/`, which the harness skills cite rather than restate; the write-in as SHAPE-AGREE's one migration, harness first, then tools-ki and a release, then the Capital, then the other territories; and the observatory contract, `ki work status --format json` with the fields in section 9, under KI-TOOL-KI-CLI-127, with an Observatory Work instrument and Beacon contributor to be captured in apps-observatory. This supersedes the first version's WORK-MIGRATE.

**Query:** Should the model be settled through one decision record, one model note, one migration and the section 9 observatory contract?

**Options:**

a) (recommended) Agree section 9: write GDR-KI-PRINCIPAL-009 and the Work Process note first, then brief SHAPE-AGREE's one migration with section 7 folded in, add the work-status contract to KI-TOOL-KI-CLI-127, and have the Observatory record captured once that read lands.

b) Agree it, but run the work model as a second migration after SHAPE-AGREE lands.

```text
WORK-MODEL

Agree section 1 of work-model.report.md as the one model of work: territory work, Project work and the work item as the levels, work cascading to the lowest level that can do it, relative worker and supervisor roles per handoff, the four kinds of state (with someone, handed off, on hold, done) as seven role-word states with only the supervisor's receive and the hold set, On hold agreed from With supervisor and drained on the way in with the reasons paused (named release) and more expected (released by new work), the move into it a mark that commits, pushes and parks everything, resume or new work moving it to Handoff to worker and finish to Finished, the states mapped onto a record's status and horizon with ready as Handoff to worker, stuck as a worker's item quiet for 10 minutes and no heartbeat on hold; nothing written into standards until WORK-SETTLE's migration.

---

WORK-WORDS

Adopt section 2 of work-model.report.md as it stands: work item (task in speech), work file work.md, worker and supervisor, the states With worker, Handoff to supervisor, With supervisor, Handoff to worker, Handoff to <target>, On hold (paused or more expected, with a release) and Finished, the lists with you, stuck, blocked, moving and on hold, the receive words with me, ack, got it and seen, and the supervisor's pause, done for now, resume and finish; hold means only the agreed On hold state, which the ki-pmo hold and the roadmap hold horizon already are, hold leaves the receive words, drain stays the activity and the hold report keeps its name.

---

WORK-THEME

Rename Initiative to theme everywhere as a label: Streams/Themes/, Projects flat in Streams/Projects/ with a theme key, ids without the theme segment (ki.ways-of-working), and SHAPE-AGREE's nesting and THREAD-IDS-AGREE's three-part ids amended within the one migration.

---

WORK-REGULAR

Make ki.regular a standing home under the territory, not a Project, for recurring Activities and ad hoc work (ki.regular.<slug>), coordinated by state of play; amend ACT-HOME's Initiative default and KI-HARNESS-GOV-206 to match.

---

WORK-HOME

Agree section 3 of work-model.report.md: flat +/_WORK/<dotted id>/ folders with work.md, decisions.md, reports and open briefs; work.md holds only the current state, next steps, Messages and parked tags; Git is the logbook, with only sends and the supervisor's receives committing and the move in each subject; links only upward; DECISIONS-HOME and THREADS-CONTENT amended within SHAPE-AGREE.

---

DECISIONS-STRIKE

Agree section 4 of work-model.report.md: decisions.md kept apart from the Git logbook; at each mark each entry is struck, reduced to a pointer or kept after checking its durable home; moves are not decisions; no numbering; first applied to the ways-of-working log at the first mark after the migration.

---

WORK-HISTORY

Never rewrite shared Git history; prune the working area at every mark; consider a separate per-territory working repository only if size measurably hurts.

---

WORK-BANNER

Adopt section 6 of work-model.report.md: one glyph-heading banner for every state in role words, counts and lists saying with you, the same prefix on the form line, the heartbeat only while work lies with a worker, and the frames retired when the model is written in.

---

WORK-SETTLE

Agree section 9 of work-model.report.md: write GDR-KI-PRINCIPAL-009 and the Work Process note under Pillars/Philosophy/Model/Processes/ first, then brief SHAPE-AGREE's one migration with section 7 folded in, add the ki work status contract to KI-TOOL-KI-CLI-127, and have the Observatory Work instrument record captured once that read lands.
```

```text
╭─ run report · 2026-10-17T23:02:00Z ──────────────╮
│                                                  │
│  █▀▀▄ █▀▀▀ █▀▀▀ ▀▀█▀   · thread at rest          │
│  █▀▀▄ █▀▀  ▀▀▀█   █    · nothing running         │
│  █  █ █▄▄▄ ▄▄▄█   █    · nothing queued          │
│                                                  │
╰──────────────────────────────────────────────────╯

- [at rest] nothing running or queued
- [waiting] WORK-MODEL
- [waiting] WORK-WORDS
- [waiting] WORK-THEME
- [waiting] WORK-REGULAR
- [waiting] WORK-HOME
- [waiting] DECISIONS-STRIKE
- [waiting] WORK-HISTORY
- [waiting] WORK-BANNER
- [waiting] WORK-SETTLE
- [committed] work-model report, revised for On hold
```

```text
Resume KI > Model > ways of working under current ki-pmo and ki-delegation since 22:34 BST: re-bootstrap, mark, fresh summary with carried-forward open points, take stock, restart authorised work, then banner.
```
