# Work state machine

**Owner:** Kris · **Owning repository:** knowledgeislands/ki-principal · **Date:** 2026-10-29

**Work:** `ki.prj.ways-of-working`. Status: draft design under `ki-work-design`, redrawn to the nested shape Kris set under WORK-CYCLE-SHAPE on 29 October 2026 in [the decisions log](../decisions.md), with WORK-CYCLE-ENDS, WORK-ENTRY-GUARDS, WORK-STATE-MACHINE, TRANSITION-CONDITIONS, DRAIN-MEANS, STATE-MACHINE-REFINE, WORK-FOLDER-PURPOSE and WORKING-EXIT folded in. WORK-CYCLE-SHAPE supersedes the first draft's flat layout and arc names where they differ; the names stay refinable. Nothing here changes a standard, a skill or the Work Process note; the rollout at the end says where each part would land once decided.

![The work state machine: the Working cycle nested, with Bootstrap and At rest around it](work-state-machine.svg)

Interactive view, with dark and light themes: [work-state-machine.html](work-state-machine.html). Each arc's preconditions, work and postconditions are in the Transitions table below.

## Roles

Three roles act on the machine, as Kris set under ROLES-ORCHESTRATOR and ROLES-EITHER on 29 October 2026. They are roles, not kinds of actor: any of them can be AI or human; the preferred holder is named.

| Role | Preferred holder | What it does |
| --- | --- | --- |
| Supervisor | Kris, the human in the loop | Receives, directs, concludes, resumes and finishes |
| Worker | A subagent run doing the work | Holds the work while With worker |
| Orchestrator | The thread agent running the state machine | Makes the machine's transitions, launches and receives workers, and talks to the supervisor |

With worker means a worker holds the work. The diagram's legend names the supervisor and worker colours with their preferred holders, and its Roles card names all three. The legend also marks the two handoff states transitional, drawn muted beside the stable With worker and With supervisor.

## Reading the machine

The machine is nested. It begins at an initial pseudo-state, **Start (wp)** for the work package, whose `open` arc enters Bootstrap, and ends at **Finished**, the terminal state. A composite state, **Working**, holds its own initial pseudo-state, **Start (work)**, and the cycle in which the work is worked: With worker, Handoff to supervisor, With supervisor and Handoff to worker, joined by inform, receive, direct and receive, and its final state, **End (work)**, which `conclude` reaches from With worker or from With supervisor. With worker and With supervisor are stable: the work rests with a holder. Handoff to supervisor and Handoff to worker are transitional, between the two, and drawn muted. Around it sit three states: **Bootstrap**, where a session reads the package before it acts and enters Working by `ready`, into Start (work); from there a guard chooses: `[work clearly defined] pick up` to With worker, or `[needs more clarity] refine` to With supervisor; **At rest**, which `stop` reaches from End (work), the only exit from Working; and **Finished**. At rest leaves by `resume` into Bootstrap or by `finish`.

At rest carries a reason, in Kris's words "holding due to other work package demands; waiting due to waiting some response externally; moving due to moving the work to another host, work package etc.". The first draft's Handoff to target is At rest, waiting, and its On hold is At rest, holding.

Drain is not a state: it is the work done on the `stop` arc. Every arc has three parts, as Kris set under TRANSITION-CONDITIONS: preconditions that must hold before it starts, the work it does, and postconditions that must hold when it ends. An arc whose work cannot reach its postconditions does not complete: the work stays in its source state, marked blocked, and the report says what blocks. A `stop` that cannot drain is the case in practice, reported `NOT DRAINED`.

Only the holder moves: the worker informs and picks up; Kris receives, directs, concludes, resumes and finishes. A steer mid-run, a heartbeat, a run launched or received, a mark and a `drain` without a stop happen inside a state and move nothing.

## States

| State | `state` value | Meaning | Who holds the move | Banner | What must be true while in it |
| --- | --- | --- | --- | --- | --- |
| Bootstrap | none: transient, as BOOT-RECORD recommended | A session has been opened on the work, or resumed, and is reading the package before acting | The session, as worker | None of its own: the bootstrap report carries the glyph of the state it exits to | `state.md` still records the state the work was in; nothing is launched; the only writes are a mark if the work has none and the disposition of each `messages.md` line acted on |
| Working | the value of the inner state | Composite: the work is being worked, in one of the four inner states below, entered at Start (work) and left only through End (work) | The inner state's holder | The inner state's banner | The package is committed after every finished change and synced at least every 15 minutes |
| Working · With worker | `with-worker` | Stable: a worker holds the work: a run of this work is in flight | Worker | 🤖 With worker | Heartbeat at every change, at least every 5 minutes and always by 10; a `drain` without stop may be under way |
| Working · Handoff to supervisor | `handoff-to-supervisor` | Transitional, drawn muted: the worker has informed; Kris has not received | Supervisor | 🤖 → 👤 Handoff to supervisor, with `· blocked` when stuck | Nothing of this work runs; the inform commit is on origin; every query is in `queries.md` in full |
| Working · With supervisor | `with-supervisor` | Stable: Kris has received | Supervisor | 👤 With supervisor | `received` is set; nothing runs |
| Working · Handoff to worker | `handoff-to-worker` | Transitional, drawn muted: Kris has directed, and no session has received it | Worker | 👤 → 🤖 Handoff to worker | Every owner answer is read back in `decisions.md`; nothing runs; `state.md` next steps say what to restart |
| Working · End (work) | none: transient; `state.md` keeps the inner state concluded from until `stop` completes | Working's final state: Kris has concluded, and the `stop` arc's drain is under way | Orchestrator, draining | None of its own: the banner stays that of the state concluded from until the hold report | The reason, the release and, for waiting, the target are recorded; nothing new is launched; no wake is held. If `stop` cannot complete, the work stays here, marked blocked, `NOT DRAINED` |
| At rest | `at-rest`, with `rest.reason` (`holding`, `waiting` or `moving`) and `rest.release` | Stopped and drained, for a reason | Nobody until the release | ⏸️ At rest · `<reason>`; waiting also names its target, → 🎯 | The portability postcondition of `stop` holds throughout: deleting the local checkout loses nothing; queries are parked; no heartbeat and no scheduled wake; routed lines wait unread. Waiting: the line in the target's `messages.md` is on origin and `state.md` names the target and what is expected back. Moving: `state.md` names the destination host or package |
| Finished | `finished` | Closed: the terminal state, with no arc out | Nobody | 🏁 Finished | Every decision homed, `design/` resolved, every finding settled, runs closed; the folder is deleted at the closing mark, Git keeping it |

## Transitions

Old names map to new: send → **inform**, reply → **direct**, hold → **conclude** then **stop**, Handoff to target → **At rest · waiting**, On hold → **At rest · holding**. The first draft's hand off, answer and withdraw arcs fold into `stop` with reason waiting and `resume`; its `re-bootstrap` from each live state is not drawn, since a fresh session on live work is recovery under WORK-REENTRY below. Commit subjects marked _proposed_ are new; the rest are today's.

| Transition | From → To | Actor | Trigger and owner words | Preconditions | Work on the arc | Postconditions and commit |
| --- | --- | --- | --- | --- | --- | --- |
| open | Start (wp) → Bootstrap | Supervisor | Kris pastes an opener, `Bootstrap as <id> under ki-coordination.`, from `ki agent prompts` | The machine is "Ready to coordinate" under `ki-bootstrap`; the id resolves to exactly one package home; the opener's level, scope, authority and coordination capability match the package | None | A session in Bootstrap. On a mismatch the session says so in one line and replies conversationally; the work does not move |
| ready | Bootstrap → Working · Start (work) | Orchestrator | The session, once its reads are done | The Bootstrap reads are complete: the standard and the note read and `method_read` checked; `ki agent status` reconciled; the five files and open findings read; `messages.md` acted on in queue order, IMPORTANT lines first | None | The session is at Working's initial pseudo-state, where a guard chooses `pick up` or `refine` |
| pick up | Start (work) → Working · With worker | Orchestrator | The session, once its reads are done | Guard [work clearly defined]: there is worker work, runs to recover, authorised next steps, or directions to take | Bootstrap report, a full owner report ending Done with the rename line; a mark struck if the work has none; parked queries moved back to `## Open`; stopped runs restarted from their open briefs | `state: with-worker` with `since`, `beat`, `mark` and `method_read`; _proposed_ `docs(work): <id> pick up`; sync |
| refine | Start (work) → Working · With supervisor | Orchestrator | The session, when nothing is the worker's | Guard [needs more clarity]: nothing runs and no authorised unit waits to launch; the work needs Kris to clarify it | Bootstrap report with every open query in full; a mark struck if none | `state: with-supervisor` with `received` set, the opener counting as the receive; _proposed_ `docs(work): <id> refine`; sync |
| inform | With worker → Handoff to supervisor | Orchestrator | The worker | An actual decision or review is due, or all dispatched work has finished, or the worker is stuck (`inform · blocked`); every finished run received, its report homed in `reports/`, its queries copied whole into `queries.md` and its decisions logged | Prune the work folder; rewrite `state.md` front matter and next steps; give the Summary with the banner | `state: handoff-to-supervisor`, `blocking` when stuck; `docs(work): <id> send to owner`, renamed _proposed_ `inform owner`; fetch, fast-forward pull and push |
| receive | Handoff to supervisor → With supervisor | Supervisor | Kris: `with me`, `ack`, `got it`, `seen` | The inform is committed | None | `state: with-supervisor`, `received` set; committed with the worker's next inform, `docs(work): <id> receive by owner` |
| direct | With supervisor → Handoff to worker | Supervisor | Kris answers in speech, by tag, in order or by a bare letter | Each answer read back as taken in `decisions.md` in the turn it arrives; an unclear answer asked back in one line | Answered queries leave `## Open` in `queries.md` | `state: handoff-to-worker`; _proposed_ `docs(work): <id> direct`. In a live session the worker usually receives in the same turn, so direct and receive share one commit |
| receive | Handoff to worker → With worker | Orchestrator | The worker, in a live session | The direction is committed; the worker has read it back | Restart authorised work from next steps | `state: with-worker`; _proposed_ `docs(work): <id> receive by worker` |
| conclude | With worker or With supervisor → Working · End (work) | Supervisor | Kris: `pause` or `done for now` for holding; `stop, waiting on <target>` for waiting; `move to <host or package>` for moving; the worker may propose it when it informs. From With worker the words arrive as a steer and the orchestrator makes the move | The reason and the release stated in words; for waiting, the route authorised or the transfer permitted by Kris | Read IMPORTANT messages; cancel every wake this session holds; launch nothing new; record the reason, the release and, for waiting, the target in `state.md` next steps | The work is at End (work), nothing new launched and no wake held; no commit of its own: `stop` follows in the same turn and carries the commit |
| stop | Working · End (work) → At rest | Orchestrator | Follows `conclude` at once | At End (work): the reason and the release recorded; IMPORTANT messages read; every wake this session holds cancelled | **Drain**: launch nothing new; let a run that will finish within about 15 minutes finish; stop any other at a safe point, recording where it stopped and how to restart it, its brief kept in `briefs/`. For waiting, one line in the target's `messages.md`, committed alone and pushed. **Portability checks** under DRAIN-MEANS, listed below. **Park**: strike the mark; move every open query to `## Parked` with its tag, one line of context and its recommended option; strike decisions; prune the folder | The portability postcondition: if the local checkout were deleted, nothing would be lost. `state: at-rest`, `rest.reason`, `rest.release`, `since`, and `target` for waiting; `docs(work): <id> hold, paused`, `hold, more expected` or _proposed_ `stop, <reason>`, pushed fast-forward; the hold report. If a drain step or portability check fails, such as an unpushable change, a run that must not be stopped, a diverged pull, an unknown PR state or a runtime-only report, the stop does not complete: the work stays at End (work), marked blocked, `NOT DRAINED`, `state.md` keeping the inner state concluded from with `blocking`. The terra drain of 29 October ended so |
| resume | At rest → Bootstrap | Supervisor | Kris: `resume`, or an opener on the work; for waiting, the target's reply line or receipt in this work's `messages.md`; for moving, an opener on the destination | The release holds; on another host, the repository level check proves the repositories level | None: a session opens in Bootstrap, on this host or the destination | A session in Bootstrap; `ready`, then `pick up` or `refine`, records the new state; _proposed_ `docs(work): <id> resume` |
| finish | At rest → Finished | Supervisor | Kris: `finish` | Close-out: every decision homed, none homeless or held; `design/` resolved, every note graduated and deleted; every finding settled; no run, report or brief open; the `stop` portability postcondition holds | Route the durable information; point the Project note at the outcome; `ki agent close` archives the runs, its gate strict with `--reconciled` as Kris's waiver | `state: finished`; `docs(work): <id> finish`; the folder deleted at the closing mark in one commit, Git keeping it |

### Portability checks on the stop arc

DRAIN-MEANS and TRANSITION-CONDITIONS set the test, in Kris's words: "there's no longer anything which is specific to a machine that might get lost if I was to delete the repository". The stop arc checks, in every repository the work or its runs touched:

1. Nothing of this work is running, queued or scheduled; each stopped run has its restart recorded and its brief kept.
2. No uncommitted change of this work; everything committed by explicit path, pulled fast-forward and pushed fast-forward, never forced and never with `--no-verify`.
3. Every run worktree removed once its work is on origin; every branch either merged into `main` or pushed to origin, in Kris's words "making sure that any branches are folded in. Or, if not, they need to be pushed to the origin".
4. Stale remote-tracking branches pruned, "a prune of origin ones which are no longer there".
5. No stash and no local-only ref holding this work's content.
6. Every open PR recorded in `state.md` as merged, closed or named for its owner.
7. Every run report homed in `reports/`, or its outcome homed; anything in `~/.local/state/ki/agents/<run>/` needed to resume copied into the package, never a secret.
8. The package reviewed and tidied: mark struck, queries parked, decisions struck, folder pruned.

Another session's uncommitted file is named in the hold report's Left over and left alone. A check that cannot be run, such as PR state under a provider-call ban, is unknown, never passed, and the stop does not complete.

## At rest by reason

| Reason | Replaces | Release, and so what resumes it | Typical next arc after Bootstrap |
| --- | --- | --- | --- |
| holding | On hold, paused or more expected | Kris's `resume`, the stated condition, or new work arriving for more expected | `pick up`, or `refine` when the work needs more clarity |
| waiting | Handoff to target | The target's reply, receipt or return lands in this work's `messages.md` | `pick up` to take the reply into next steps, or `refine` when it needs Kris |
| moving | the planned host move through a drain | An opener on the destination host or package, after the repository level check | `pick up` on the destination |

A target still holds no authority over this work: whatever it does lands as a line this work reads, and only Kris finishes. The machine-local binding is never moved but rebuilt on each host; HOST-SYNC, the two-host regular synchronisation, is a separate design that moves no work through the machine.

## Work folder layout

WORK-FOLDER-PURPOSE, in Kris's words: "anything else that we create under that structure must be in a folder based on what its purpose is". The root holds the five package files and nothing else; every other kind lives in a named purpose folder:

```text
+/_WORK/<id>/
├── work.md                      definition: description, Goals, Scope
├── state.md                     state fields, Now, Next steps, Held
├── queries.md                   open and parked queries in full
├── messages.md                  inbox, a queue in priority order
├── decisions.md                 Kris's decisions not yet durable elsewhere
├── reports/<run>.report.md      a run report, until its outcome is homed
├── briefs/<run>.md              a brief, until its run's report is received
├── design/<slug>.md             a design note, or design/<subject>/
│   └── <slug>.architecture.json and its .svg and .html renders
├── findings/<tag>.md            an open finding, until settled
└── feedback/<date>-<slug>.md    Kris's Observatory feedback, until homed
```

Against today's `ki-work-package` closed list, only the run report moves, from the root to `reports/`; briefs, design, findings and feedback already sit in purpose folders. The list stays closed: a new purpose folder needs a change to the standard, not a writer's choice. The launcher, `ki agent`, homes reports and so must write into `reports/`, and the rubric's FOLDER family would fail any root file beyond the five.

The folder moves with the machine: `inform` and every mark prune it, `stop` prunes it and proves it portable, and the closing mark after `finish` deletes it.

## Rollout once decided

Each part goes to its owner as a `messages.md` line under HANDOFF-AS-MESSAGE, not done here:

- **Work Process note**, in this repository through the Enactment Process: the nested drawing and states table, the transition names in the Words table, drain as the stop arc's work.
- **`ki-coordination` standard**, in `ki-agentic-harness`: States and moves carries the transition table and the old-to-new names; Putting work on hold becomes stopping, with the portability checks as the stop postcondition; banners for At rest by reason.
- **`ki-work-package` standard**, in `ki-agentic-harness`: the `at-rest` state value with `rest.reason`; the closed list moves reports into `reports/`.
- **`tools-ki`**: `ki agent` homes reports into `reports/`; `ki work status` and the Observatory learn `at-rest` and its reasons.

## Decisions for Kris

This shape settles the first draft's BOOT-RECEIVE (refine goes to With supervisor), TARGET-RUN (a target is outside the work's runs; its own runs are With worker), TARGET-SILENT (a waiting rest has no holder to time out; Kris resumes or finishes it), HOST-MOVE-PATH (a planned move is a stop with reason moving) and ARC-NAMES (Kris's names, still refinable). BOOT-RECORD, REPORTS-NAME and FOLDER-MIGRATE are untouched by the reshape and stay recommended as before: Bootstrap transient, `reports/<run>.report.md`, and tidy-then-move at each package's next mark. What the shape leaves open:

### REST-PORTABLE - Whether every At rest reason needs full portability

**Context:** Kris's TRANSITION-CONDITIONS makes portability the postcondition of going to rest: deleting the checkout loses nothing. For holding and moving that is the point. A waiting rest may last an hour, for a reply from another work on the same host, and full portability means stopping long runs, parking every query and striking the mark each time.

**Query:** Does `stop` require the full portability checks for every reason, or a lighter check for waiting?

**Options:**

a) (recommended, confidence medium - one postcondition keeps At rest one state with one guarantee, and a short wait is better kept inside Working as With worker) Full portability for every reason; a short wait for another work stays in Working, With worker, with the item shown waiting in the banner.

b) Waiting needs only committed and pushed, no parking or run stopping; holding and moving need the full checks.

### WAIT-RESUME - How a waiting rest resumes when the response arrives

**Context:** At rest has nobody holding the move. When the target's reply line lands in this work's `messages.md`, nothing runs to notice it unless a session is opened. Territory work already sweeps inboxes at its mark, and the coordinator style forbids timeout takeovers.

**Query:** When the response arrives, what moves a waiting rest to Bootstrap?

**Options:**

a) (recommended, confidence medium - keeps "only Kris or an opener resumes" while making the arrival visible without a new wake mechanism) The reply line is the release; territory work flags it at its next mark and in its Summary, and Kris resumes with an opener.

b) The reply line resumes the work automatically: the replying session, or a headless pass, opens a Bootstrap on it.

### FINISH-FROM - Whether finish is only from At rest

**Context:** Kris's shape draws finish only from At rest. Today Kris can finish from With supervisor, and the first draft allowed it. Requiring At rest first means a finish always passes through stop, and so through drain and the portability checks, before close-out.

**Query:** Is `finish` only from At rest, or also directly from Working, With supervisor?

**Options:**

a) (recommended, confidence high - follows Kris's drawing, and close-out already needs everything the stop postcondition proves, so the extra step costs one commit) Only from At rest: `finish` in Work is a stop then a finish, in one turn when the checks pass.

b) Also from With supervisor, running the portability checks as finish preconditions.

### WORK-REENTRY - How a fresh session re-enters live work

**Context:** Kris's shape has Bootstrap entered only by resume from At rest. A compaction, a model switch, a lost host or a new session on work still in Working (With worker or With supervisor) also needs a bootstrap read, and today that is `Re-bootstrap as <id>`. The first draft drew a re-bootstrap arc from every live state.

**Query:** How is a re-bootstrap of live work modelled?

**Options:**

a) (recommended, confidence medium - a re-read moves nothing, so it need not be an arc, and the drawing stays as Kris set it) As a re-entry inside Working: the session reads as Bootstrap does, the recorded state is unchanged, and no arc is drawn; an unpushed loss on an unplanned move is recovered from the last pushed state.

b) As a drawn arc, Working → Bootstrap, labelled re-bootstrap.

### REST-NAMES - Whether to keep Kris's working names

**Context:** Kris said "some of these names could be refined". The shape uses inform, direct, stop, At rest, holding, waiting and moving. Commit subjects today use `send to owner` and `hold, paused`; banners use On hold and Handoff to `<target>`.

**Query:** Adopt the names as drawn, renaming commit subjects and banners to match?

**Options:**

a) (recommended, confidence medium - they are Kris's own and read plainly, and proving them in use is how the note's other words were settled) Adopt them as drawn, to be proven in use; old subjects stay readable in history.

b) Refine some first; name which.

### WORKER-WAIT - Which state holds work that no worker holds yet

**Context:** With worker now means a worker holds the work, under ROLES-ORCHESTRATOR. The States table used to put two more cases there: the orchestrator mid-turn, and authorised work waiting for worker capacity, which the coordinator style keeps "with the worker". Neither has a worker holding the work.

**Query:** Do those two cases stay in With worker, or does With worker mean only a run in flight?

**Options:**

a) (recommended, confidence medium - it keeps the four inner states, and the orchestrator acts on the worker's behalf until a run starts) Keep both in With worker, read as the worker side holding the work, the banner showing a queued item.

b) With worker only while a run is in flight; the two cases need a state or a reading of their own.

### ROLE-WORDS - Whether the note's other columns move to role words

**Context:** The Transitions table now carries an Actor column. The States table's "Who holds the move" column and the trigger column still say "the worker", "the session, as worker" and "Kris" in the old sense, where the thread agent was the worker; the Reading the machine paragraph does too. The brief changed nothing else.

**Query:** Should those passages be restated in supervisor, worker and orchestrator terms?

**Options:**

a) (recommended, confidence high - the Actor column and the older wording now disagree on who "the worker" is) Restate them in role words in one follow-up pass.

b) Leave them until the Work Process note is reframed, and read them through the Actor column meanwhile.
