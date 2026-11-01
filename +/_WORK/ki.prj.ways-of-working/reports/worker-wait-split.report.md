# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › worker-wait-split

**🤖 → 👤 Handoff to supervisor · Run report at 06:23 GMT · last mark 01:39 GMT**

---

## Done

- Split WORKER-WAIT into five tagged parts under Open in [queries.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/queries.md): WORKER-WAIT-MEANING, WORKER-WAIT-QUEUED, WORKER-WAIT-MIDTURN and WORKER-WAIT-DELIVERY at high confidence, WORKER-WAIT-GATED at medium; no other query changed, and the file carries no em- or en-dashes.
- Limitation: the edit is on origin, but not under its own commit. Another session's commit `76beec53`, "docs(work): ki.prj.ways-of-working host-sync review (claude)", staged `queries.md` while this edit was uncommitted and pushed it; its `queries.md` change is exactly this split and nothing else. No commit with the brief's subject exists, and none could be made without rewriting published history, which is forbidden.
- Challenges to earlier reasoning, carried in the parts: "With worker means a run holds the work" is the ROLES-ORCHESTRATOR read-back's wording, not Kris's, and ROLES-EITHER's human worker contradicts it; the standard's "or the coordinator is mid-turn" clause is a remnant of the reframed coordinator-as-worker role; the current capacity rule holds only for briefed, queued units, not for work gated on outside events.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- WORKER-WAIT-GATED is medium and has had no masked blind review; under the coordinator style it goes to one before it reaches Kris. To reach high it also needs a check against REST-PORTABLE's settled wording on short external waits, a ruling on whether dated follow-ups such as ORCA-REACH's (due 6 November) are gates or ordinary next steps, and evidence of what the dispatcher does when a usage limit or provider outage stops a launch.
- The four high parts are high now; WORKER-WAIT-DELIVERY depends on the other three being taken.

## Queries

### SPLIT-COMMIT - The split was published inside another session's commit

**Context:** The brief asked for `queries.md` to be committed alone under "docs(work): ki.prj.ways-of-working split WORKER-WAIT". Before this run committed, another session's host-sync review commit `76beec53` swept the uncommitted `queries.md` into its own commit and pushed it. The content on origin is exactly this run's split; only the commit subject is misleading for that file.

**Query:** Is the split accepted as published under that commit, or should a marker be added?

**Options:**

a) (recommended, confidence high - the content is identical and on origin, and the only correction possible without rewriting history is a note) Accept it as published; the coordinator records in the decisions log, at its next receive, that `76beec53` carries the WORKER-WAIT split.

b) Add an empty commit with the brief's subject that names `76beec53` as carrying the split.

### WORKER-WAIT-MEANING - With worker means the worker role holds the work, not that a process is live

**Context:** Kris's words under ROLES-ORCHESTRATOR name three roles: "the worker is a subagent, and then the thread agent is effectively the orchestrator of the state machine". The sentence "With worker means a run holds the work" is the read-back's, not Kris's, and the [state machine](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/work-state-machine.md) States table narrows it further to "a run of the work is in flight". ROLES-EITHER then lets a human hold any role, and a human worker never has a run in flight, so the narrow reading cannot describe a case Kris has already allowed. The banner makes its last glyph whose move it is, and its list already names a holder per item, `run/<name>` for `[running]` and `[queued]` alike. This part settles only the test; WORKER-WAIT-QUEUED, WORKER-WAIT-MIDTURN and WORKER-WAIT-GATED apply it to the disputed cases.

**Query:** Is With worker defined by assignment, the worker role holding the next move on at least one named unit, or by liveness, a run process being in flight?

**Options:**

a) (recommended, confidence high - the only reading that fits Kris's own role words, ROLES-EITHER's human worker and the banner's existing holder items, and it can be checked against `ki agent status` and the run queue) Assignment: the work is With worker while at least one authorised unit is assigned to a named worker holder, running or queued, so its next move is the worker side's; a run in flight is the common case, not the definition. The States table and the read-back's narrower sentence are restated to match.

b) Liveness: With worker only while a run process is in flight; every other moment of Working must sit in another inner state.

### WORKER-WAIT-QUEUED - Briefed work waiting only for a slot stays With worker

**Context:** About three agents run per thread and the rest wait in the run queue, each with its brief, agent name and launch options; the dispatcher launches the next as a slot frees and honours each `DONE` gate, with no further decision from anyone. The banner already lists such a unit as `[queued]` with holder `run/<name>`. Current coordination says "Authorised work waiting for worker capacity stays with the worker; send to supervisor only for an actual decision or review", and the agreed `inform` arc needs a decision or review due, all dispatched work finished or a stuck worker, none of which a full queue is. This part covers only a unit that is briefed and queued; authorised work that cannot yet be queued is WORKER-WAIT-GATED.

**Query:** Is the work With worker when its remaining authorised units are briefed and in the run queue, waiting for a slot or for a `DONE` gate on another run of this work?

**Options:**

a) (recommended, confidence high - each unit has a named holder and will start without anyone's further move, so sending it to Kris would ask Kris for nothing) Yes: With worker, each unit shown `[queued] · run/<name>` and never counted as running or with you; the `pick up` and `receive by worker` arcs complete only when every authorised unit they restart is running, queued or recorded as gated.

b) No: entry to With worker waits for a launch, so after a direction the work stays in Handoff to worker until a slot frees, and a bootstrap that finds only queued work refines to With supervisor.

### WORKER-WAIT-MIDTURN - An orchestrator turn moves nothing

**Context:** Current coordination, States and moves, says territory and Project work are With worker "while any items lies with a run or the coordinator is mid-turn". The clause dates from when the thread agent was the worker to Kris, which ROLES-ORCHESTRATOR reframed. The agreed machine says a steer, a heartbeat, a run launched or received and a mark happen inside a state and move nothing; only an arc moves the work, and the orchestrator makes the arcs. A coordinator answering Kris in With supervisor, or receiving a report before it informs, is orchestrating, not working. The coordinator style already forbids the orchestrator substantive work, so no coordinating case needs it as the worker.

**Query:** Does an orchestrator turn by itself put or keep the work With worker?

**Options:**

a) (recommended, confidence high - follows the agreed rule that only arcs move the work, and the clause is a remnant of the role ROLES-ORCHESTRATOR reframed) No: during an orchestrator turn the work stays in its last committed state and moves only by an arc; drop "or the coordinator is mid-turn" from the state rule. If ROLES-EITHER ever puts the orchestrating actor in the worker role, it is named as a unit's holder like any other, under WORKER-WAIT-MEANING.

b) Yes: keep the clause, so any orchestrator turn reads as With worker whatever was last committed.

### WORKER-WAIT-GATED - Authorised work that nothing will start by itself

**Context:** Some authorised units cannot be briefed or queued yet because they wait on something outside this work's runs: another work's reply, a person, a date, a host, or model capacity lost to a usage limit or outage. Nothing will start them until someone acts on an event. While other units run or are queued the work is With worker anyway; the question arises only when gated units are all that remain. The current capacity rule would keep such work with the worker indefinitely, which can show a With worker with nothing running and no heartbeat for days. REST-PORTABLE makes At rest · waiting the honest state for a real wait, but at the cost of the full stop: drain, the portability checks, parked queries and a struck mark, even for a short reply. A live coordinator wakes at least every five minutes and reads `messages.md` at each wake, so it notices a reply line; once the session ends nothing does, unless a granted headless pass names the work.

**Query:** When gated units are all the authorised work that remains, does the work stay With worker or stop to At rest · waiting?

**Options:**

a) (recommended, confidence medium - honest about the holder while a live session can act on the gate and avoids an idle With worker, but where the line falls is untested) Stay With worker, each gate shown as an item naming it, `[handoff]` where it is other work or a person, only while the orchestrator session that will act on it is open and waking; conclude and stop to At rest · waiting, the gate as release, before that session ends or when the gate is a date or outlasts it.

b) Stop to At rest · waiting as soon as nothing of this work is running or queued, however short the gate.

c) Stay With worker while any authorised gated unit remains, however long the gate, each shown as an item naming it.

### WORKER-WAIT-DELIVERY - Carry the high parts into the rollout now

**Context:** The [state-machine rollout plan](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/state-machine-rollout-plan.md) excludes WORKER-WAIT's two cases from U1's Harness contract fixtures and from the pilot pending an answer, and says WORKER-WAIT blocks only their enforcement. WORKER-WAIT-MEANING, WORKER-WAIT-QUEUED and WORKER-WAIT-MIDTURN change wording, fixtures and holder projections only: no state value, arc or diagram. WORKER-WAIT-GATED may change when a stop falls due, which touches the stop arc's trigger.

**Query:** Once the three high parts are taken, should U1 and U2 carry them now, with WORKER-WAIT-GATED left isolated until it is decided?

**Options:**

a) (recommended, confidence high - the three are consistency corrections inside the agreed shape, and holding them back leaves the mid-turn clause live in the standard) Yes: U1 restates States and moves, the States table and the role words to the adopted reading and adds running, queued and orchestrator-turn fixtures; U2's readers show queued apart from running wherever they project holders; WORKER-WAIT-GATED stays out of enforcement and the pilot until decided.

b) Hold every part of WORKER-WAIT out of U1 and U2 until WORKER-WAIT-GATED is decided too.

### 🤖 → 👤 Handoff to supervisor · since 06:23 GMT

👤 6 with you

- [with you] SPLIT-COMMIT · owner · since 06:23
- [with you] WORKER-WAIT-MEANING · owner · since 06:23
- [with you] WORKER-WAIT-QUEUED · owner · since 06:23
- [with you] WORKER-WAIT-MIDTURN · owner · since 06:23
- [with you] WORKER-WAIT-GATED · owner · since 06:23
- [with you] WORKER-WAIT-DELIVERY · owner · since 06:23
- [committed] work folder

🧵 ki.prj.ways-of-working
