# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › work-package-review-fable

**🤖 → 👤 Handoff to supervisor · Run report at 12:41 BST · last mark 12:04 BST**

---

## Done

- Blind review of [work-package.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/work-package.md) against Kris's 12:24 BST words in the [decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md) and the eleven live folders under `+/_WORK/`; no other review read, nothing edited, committed or pushed.
- Stocktake checked on every live folder: line and word counts, mark fields, state, Messages lines, report and brief counts and decisions-log sizes all match the table, with three small drifts: `ki.observatory` has moved since the 12:20 BST stocktake (now one report, no briefs, 298 words, still a dated log in `Next steps`); `ki.timelines` also lacks a `mark` field, which the note flags only for `ki.tools-burndown`; `ki.chezmoi` carries eight 18 October lines, not seven. The closed-list breaches (`adobe-remove.sh`, four JSON evidence files) and the `ki.baseline-rollout` twin in `+/_WORK_REVIEW/` are confirmed.
- Readers checked: `ki work status` in tools-ki reads `state`, `target`, `hold`, `blocking`, `since`, `received`, `beat`, `worker` and `supervisor` from `work.md` front matter alone, so the split needs the reader change the note names before any folder migrates; `ki agent home` only tests that `work.md` exists.
- Live sessions checked: only this work has running agents (the two reviewers); every other live folder last moved by commit this morning, five of them in the hour before the stocktake, so most have an owner-facing session that will rewrite `work.md` from memory at its next receive.

**Verdict in one paragraph.** The model is right and matches Kris's words closely: a definition file read first, state and queries beside it, one inbox file, decisions unchanged. Keep "work folder". `work.md` as proposed is small and routable: a 500-character description plus a 300-word body is well under a skill's metadata and body budgets. The State of play hub, compulsory receipt without conferred authority, and targeted refresh through `method_read` are sound and consistent with Kris's "you have to accept it" and "improvements should really go back to state of play". The migration path is right in principle, self-migration at each folder's own mark, but it is not yet safe as written: the sequencing and the open-session hazard below need stating before the pilot.

**Where I differ or extend, by topic.**

1. **Name.** Agree: keep "work folder" and the skill name. Kris asked "Are they work packages?" as a question, the read-back says "settle the name", and the WBS collision is real. Use "packaged like a skill" in prose and give `work.md` the role name "definition" in the Words table so that "work file" stops meaning "current state".
2. **The split.** Right in shape. Two gaps: `state.md` front matter should repeat `id` so a file read alone is self-identifying and the rubric can check the pair agree; and the coordinator's turn budget in the `ki-coordinator` style ("reads limited to the work file ... writes limited to the work file, the decisions log and a brief") must be rewritten, because pick-up is now four small files and a send writes three. Say that one read of the folder's pick-up files counts as one call, or the five-call budget is spent before the first launch.
3. **`## Now` and the log habit.** Four folders use `Next steps` as a log because the Summary needs "since the mark" and nowhere holds it. Point 7 removes the habit without naming the replacement. State it: the recap since the mark reads `git log -- +/_WORK/<id>/` and the run reports; `## Now` holds the present only. Without that sentence the log moves into `## Now` and the five-line limit becomes a warning everyone ignores.
4. **Parked tangents have no home.** The note dissolves `Parked` into parked queries, held work and ideas, but the coordination standard's "Parking tangents" is a fourth kind: an owner side topic that is not yet a query. Sending it to the Project note at the moment it is raised pushes churn into `Streams/`. Put tangents in `queries.md` under `## Parked` as one-line entries; "Parked" there means "with the owner, later", whether or not options exist yet.
5. **Description and Scope overlap.** The description says "Takes ... Not for ... (ids)" and `## Scope` says `In:` and `Out:` by id: two statements of one boundary that will drift. Keep ids in `## Scope` only, make the description plain prose of what the work does and takes, and let the rubric check that every id in Scope resolves to a live or finished work. That also brings the description under about 300 characters.
6. **Routing.** Sound. Add a loop guard to point 25: a work may return a routed unit to State of play once; a second mismatch goes to Kris as a query, not back round. Add that the receiver's disposition is one word in the removal commit subject, so the register can tell a routed line was acted on without reading the folder. Point 29's "a sender may replace its own earlier REFRESH line" is a second write kind by another work, edit-own-line, and the entry-point table must allow it explicitly or it fails the mechanical check.
7. **Refresh.** Sound. One field for the harness revision is simpler than the per-skill line and is enough while both skills live in one checkout. The fallback bootstrap check stays, which covers works that never receive a line.
8. **Migration safety.** Three amendments. First, sequence: the standard with tolerance, the rubric and the tools-ki reader accepting both shapes must land before the pilot folder splits, or `ki work status` shows the pilot with no state and the territory views lose it. Second, the open-session hazard: a session in Handoff to supervisor holds the old shape in memory and rewrites `work.md` at its next receive; any folder migrated from outside while such a session is alive will be clobbered or re-grown. So the mechanical run (point 40) must touch only work with `state: on-hold` and no session, and must leave a `FIRST-STEP` line in the new `messages.md` naming the shape change; every other folder migrates only from its own session, as point 39 says. Third, the sender rule during the window is unstated: a sender writes to `messages.md` where it exists, else to `## Messages` in `work.md`, never both. Also: unrecoverable query tags (`ki.mac-studio-setup`'s nine, whose reports are retired) should become one `## Open` line each saying the text is lost and asking Kris, not be "dropped" silently; `ki.regular` has no `decisions.md`, so its migration creates one; and the window needs a close date or a nudge rule, because `ki` has not marked in four days and `ki.regular.registry-removal` in five, so "at its own next mark" could leave two shapes live for weeks.
9. **Missing.** Territory work's Project-work queue and cap list live in its next steps today; a five-line `## Now` and a to-do `## Next steps` do not fit an ordered queue. Give territory `state.md` a `## Queue` section, or say the queue stays in `## Next steps`. State of play's own `work.md` also needs its description and Scope written first, since it is the hub everything else is matched against.
10. **Overbuilt.** The six-row limit table is fine as warnings, but "more than eight open queries" is a coordination smell, not a shape fault, and belongs in the `ki-coordination` rubric. Four reveal levels are right; do not add a fifth.

## In Progress

Nothing is running. Nothing is left in this run's temporary folder.

## Queries

### PACKAGE-NAME - What to call the packaged folder

**Context:** Kris asked "Are they work packages?" and the read-back says "settle the name". The name "work folder" was settled on 18 October and its renames are still being cleaned up in `ki.chezmoi`; "work package" is the lowest WBS deliverable, which here is the work item, the one level with no folder.

**Query:** Keep "work folder" and describe it as packaged like a skill, or adopt "work package"?

**Options:** a) (recommended, confidence medium - the collision and the fresh-rename cost are concrete, but Kris may simply prefer the word) Keep "work folder" and `ki-work-folder`; the Words table gains "definition" for `work.md`; prose says "packaged like a skill". b) Adopt "work package" and rename the skill `ki-work-package`, path unchanged. c) "Work package" in prose only, skill unchanged.

### STATE-FILE - Where the moving state fields live

**Context:** `ki work status` reads every state field from `work.md` front matter today. Splitting them into `state.md` keeps `work.md` stable and splits the logbook, at the cost of one reader change and a two-file join.

**Query:** Do the state fields move to `state.md` front matter, or stay in `work.md` with only the prose moving?

**Options:** a) (recommended, confidence medium - matches "state in its own file" and keeps the definition from changing at every move; the reader change is small and must land first anyway) State fields in `state.md` front matter, with `id` repeated there, and `## Now`, `## Next steps`, `## Held`; territory work adds `## Queue`. b) State fields stay in `work.md` front matter; only the prose moves to `state.md`.

### QUERIES-FILE - The Q file

**Context:** Six of eleven works name open query tags whose text is outside the repository or only in a Summary; `ki.chezmoi` keeps twelve reports alive only for their queries. Kris asked for "a Q one, like the decisions one".

**Query:** Does `queries.md` hold every open and parked query in full, with the owner report rendered from it?

**Options:** a) (recommended, confidence high - it is Kris's request, it closes the state-folder gap, and it decouples reports from the tidy) `queries.md` holds every query in full under `## Open` and `## Parked`; the report's Queries section is rendered from `## Open`; the coordinator copies queries in at receive. b) `queries.md` as an index of tags pointing at reports.

### PARKED-HOME - Where parked items go

**Context:** Today's `Parked` holds five kinds. The note dissolves it into parked queries, held work and ideas, but leaves the coordination standard's parked tangents, owner side topics not yet shaped as queries, with no home short of the Project note. Kris's read-back listed "parked items in their own files".

**Query:** Dissolve `Parked`, and where do tangents go?

**Options:** a) (recommended, confidence medium - a separate file would recreate the catch-all, but the note's split departs from the read-back and misses tangents) Dissolve it: parked queries and parked tangents in `queries.md` `## Parked`, held work in `state.md` `## Held`, ideas in the Project note or a record; no `parked.md`. b) A separate `parked.md` for everything parked, as the read-back says.

### MESSAGES-FILE - Where the inbox lives

**Context:** Every sender writes today into the file the owner rewrites at each move, and five works still carry the 18 October MIGRATED line. A separate file makes the one permitted outside write checkable by path and isolates merge conflicts to one small file.

**Query:** Does the inbox move to `messages.md`?

**Options:** a) (recommended, confidence high - the write-by-path check is the whole point of the entry-point model, and conflicts shrink) `messages.md` beside `work.md`; during the tolerance window a sender writes there where it exists, else to `## Messages` in `work.md`; the entry-point table allows append and replace-own-line only. b) Keep `## Messages`, moved into `state.md`.

### DESCRIPTION-SHAPE - The routing description

**Context:** No work today says what it is for or what it takes; the only goal is the Project note's `outcome`, which regular and territory work lack. The note proposes a 500-character skill-style description with "Takes ... Not for ... (ids)" and a `## Scope` with `In:` and `Out:` by id, two statements of one boundary.

**Query:** What shape does the routing description take?

**Options:** a) (recommended, confidence medium - a description is what routing can match, but ids should live in one place) Required `description` in `work.md`, plain prose of what the work does and takes, about 300 characters, no ids; `## Scope` carries `In:` and `Out:` by id and the rubric checks those ids resolve; Goals link the Project `outcome`. b) The note's shape: description up to 500 characters including "Not for ..." by id, plus `## Scope`. c) Route on the Project `outcome` alone, no description.

### ROUTE-RECEIPT - What a routed work must do

**Context:** Kris said "if it then decides it's your work, you have to accept it". The note reads this as owning the disposition, not as execution authority, keeps paused holds, releases more-expected holds, and routes only unowned units through the hub.

**Query:** Is receipt compulsory at the next bootstrap or owner message, with a recorded disposition and no conferred authority?

**Options:** a) (recommended, confidence high - it is Kris's words with the authority boundary the earlier review set) As the note, plus a loop guard: one return to State of play per unit, then a query to Kris; the disposition is named in the removal commit subject. b) Receipt only at the next mark.

### REFRESH-TARGET - How method refresh reaches works

**Context:** Three of eleven works record the revision they last read, in a body line outside the heading sequence; a targeted refresh cannot tell who is behind. The note adds `method_read` to `state.md` and one coalescing REFRESH line to affected works only.

**Query:** Is refresh targeted through `method_read` with the field update as the only confirmation?

**Options:** a) (recommended, confidence high - it reuses the existing dated line and revision check and adds only the missing field) `method_read` in `state.md`; one coalescing REFRESH line to affected works behind the change; held work waits; bootstrap checks stay as the fallback. b) Broadcast every change to every live work with a one-line acknowledgement.

### STEWARD-HOME - Who carries method changes after Ways of working closes

**Context:** Kris said "ways of working goes away" and "improvements should really go back to state of play". The volume of method change after the definition settles is unknown.

**Query:** Where do method improvements live once Ways of working is Finished?

**Options:** a) (recommended, confidence medium - the lightest home that matches Kris's words, and an Activity note can be added if volume shows) State of play keeps the method backlog and dispatches each accepted improvement as ad hoc regular work or into the Project it most affects, with `ki-work-design` reviews for shape changes. b) A standing regular work for method upkeep under an Activity note with a periodic review.

### MIGRATE-PATH - How the live folders move

**Context:** Eleven live folders, most with an owner-facing session that will rewrite `work.md` from memory at its next receive; only this work has agents running. `ki work status` reads state from `work.md` alone. `ki` has not marked in four days and `ki.regular.registry-removal` in five.

**Query:** How do the live folders move to the new shape without breaking a reader or clobbering a session's write?

**Options:** a) (recommended, confidence medium - self-migration respects the entry points, but the note's ordering and the open-session hazard are unstated) The note's path with three amendments: the standard, rubric and tools-ki reader land first, both shapes accepted; the mechanical run touches only on-hold work with no session and leaves a FIRST-STEP line in `messages.md`; every other folder migrates from its own session at its next mark, with a nudge line from State of play if the window passes seven days; unrecoverable query tags become an `## Open` line asking Kris, never dropped. b) One owner-approved mechanical sweep of all eleven folders after the pilot; faster, but it writes into folders whose sessions hold the old shape in memory.
