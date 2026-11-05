# [Knowledge Islands Principal · State of play](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/work.md) › knowledge-plan

**🤖 → 👤 Handoff to supervisor · Run report at 23:40 GMT**

---

## Done

- KNOWLEDGE-FOLDER plan written as a draft design note, [knowledge.design.md](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/_emerging/knowledge.design.md), committed as 0c5ba920. Ruled out em and en dashes and checked the links: both passed. It sets out four phases: adopt the standard, pull the assistant's 41 staged cards as the first slice, upgrade Pillars one subtree at a time behind pointer stubs, then retire Pillars. Phases 0 and 1 need one governance decision record and one Enactment record. Each later subtree needs one record of its own.
- The evidence settled three of the proposal's questions. Resources stays outside `knowledge/`. Admin and Streams link in with plain links. The minimum node follows the front matter the cards already use. 29 harness files cite `Pillars/` paths, so every pulled page must leave a pointer behind.
- Line MSG-KF01 sent to the top of personal.reg.assistant-terra's Inbound with the note's path, commit cfc7f784. Its commit gate passed once the temporary worktree's packages were installed.

## In Progress

Nothing is running. The method's next step is two blind reviews of the plan before the merged report reaches Kris.

Outstanding - no action requested now: another session has an uncommitted change to `+/_WORK/ki.sop.main/messages.md` in ki-principal. I left it untouched.

## Queries

### INDEX-NAME - one name for folder notes

**Context:** The proposal wants each `knowledge/` folder to open with `_index.md`. Work-package focus folders already use `index.md`, and the island's rule elsewhere is a note named after its folder. The proposal asks for one name to cover both.

**Query:** Should folder notes be `_index.md` or `index.md`, in the graph and in work-package focus folders alike?

**Options:**

a) (recommended, confidence medium - the underscore sorts first and marks the folder's own note, but existing focus folders would need renaming) `_index.md` everywhere, with the coordination baseline updated to match.

b) `index.md` everywhere, leaving work packages as they are.

### ATTACH-HOW - how an attachment point is declared

**Context:** An attachment point is a node this island promises not to move, so that other graphs, starting with the assistant's, can pin read-only shadow copies to it. The proposal leaves open where that promise is recorded.

**Query:** How should a node be marked as an attachment point, and what should it promise?

**Options:**

a) (recommended, confidence medium - this keeps the flag on the node and the list on the home page, and lets a check confirm they agree) A front matter flag `attachment: true`, listed on `knowledge/_index.md`, promising a stable id and path and retirement by pointer rather than deletion. Shadow nodes record `shadows:` (path and revision read) and `checked:` (date).

b) A separate register file listing the attachment points, with nothing on the nodes themselves.

### ATTACH-SET - the first attachment points

**Context:** These are the nodes the assistant can pin to straight away.

**Query:** Which nodes should be the first attachment points?

**Options:**

a) (recommended, confidence medium - these are the three the proposal's picture shows) The capture funnel, the knowledge graph, and the work process once it is pulled across.

b) None until the first slice has settled.

### RESOURCES-IN - Resources in other territories' graphs

**Context:** Here Resources stays outside `knowledge/`, because the island strictly enforces the split between its own knowledge and outside reference.

**Query:** May another territory bring its Resources into its graph?

**Options:**

a) (recommended, confidence medium - no territory has shown the need yet) No for now. Revisit when a territory asks.

b) Yes, as each territory chooses.

### RENAME-WHEN - lower-casing the older areas

**Context:** You prefer everything in lower-case kebab-case. Renaming Admin, Calendar, Streams and Resources means moving every link and harness citation.

**Query:** When should the older areas be renamed?

**Options:**

a) (recommended, confidence high - renaming earlier would move the links twice) After Pillars is retired, as one separate record per repository.

b) Now, alongside the first slice.

### PACE - the first milestone

**Context:** You asked for this quickly, and Enactment still gates canonical change.

**Query:** What should the first milestone be?

**Options:**

a) (recommended, confidence high - this is the fastest route that keeps the gate) Phases 0 and 1 under one approval this week, with the harness carrying the standard in parallel, then Pillars taken one subtree at a time.

b) The standard first, and the Knowledge Islands Principal bootstrap after it.
