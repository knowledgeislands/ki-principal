# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-sm-roles

**🤖 → 👤 Handoff to supervisor · Run report at 22:09 GMT · last mark 22:09 GMT**

---

## Done

- ROLES-ORCHESTRATOR and ROLES-EITHER applied to the [work state machine](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/work-state-machine.md): a Roles section near the top (Supervisor: Kris preferred; Worker: a subagent run; Orchestrator: the thread agent; any role AI or human), and an Actor column in the Transitions table (open, receive by owner, direct, stop, resume and finish: Supervisor; ready, pick up, refine, inform and receive by worker: Orchestrator). With worker now reads "a worker holds the work".
- Diagram re-rendered with archify (all gates pass): the supervisor and worker legend entries now name their preferred holders, and a new Roles card names all three. The SVG's legend was patched to match.
- The uncommitted ROLES-EITHER entry in decisions.md was committed with it in e4116b1d, `docs(work): ki.prj.ways-of-working state machine roles`. The spent briefs wow-sm-ends, wow-sm-nested and wow-sm-guards were never tracked, so they were deleted from disk only. Pushed.

## In Progress

Nothing is running.

## Queries

### WORKER-WAIT - Which state holds work that no worker holds yet

**Context:** With worker now means a worker holds the work. The States table used to put two more cases there as well: the orchestrator in the middle of a turn, and authorised work waiting for a free worker. In neither case does a worker hold the work.

**Query:** Do those two cases stay in With worker, or does With worker mean only that a run is in flight?

**Options:**

a) (recommended, confidence medium - this keeps the four inner states, and the orchestrator acts for the worker until a run starts) Keep both in With worker, with the banner showing a queued item.

b) With worker only while a run is in flight; the two cases need a state or reading of their own.

### ROLE-WORDS - Whether the note's other columns move to role words

**Context:** The States table's "Who holds the move" column, the trigger column and the Reading the machine paragraph still use "the worker" in the old sense, where the thread agent was the worker. This now disagrees with the Actor column.

**Query:** Should those passages be restated in supervisor, worker and orchestrator terms?

**Options:**

a) (recommended, confidence high - otherwise the Actor column and the older wording disagree about who "the worker" is) Restate them in role words in one follow-up pass.

b) Leave them until the Work Process note is reframed.
