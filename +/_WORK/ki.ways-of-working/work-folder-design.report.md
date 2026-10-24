# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › work-folder-design

**🤖 → 🧑 Handoff to supervisor · blocked · Run report at 10:18 BST**

---

## Done

- Design note written: [work-folder.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/work-folder.md>). It covers the inventory (§1), the writers, readers and deleters with file and line citations (§2), confidence (§3), the recommended division (§4) and the name (§5). It is **not committed**: the ki-principal commit gate failed (see WORK-GATE-BLOCKED). The note is still untracked, and I left the index as I found it.
- Main finding: nobody owns the folder today. Ownership is split across ki-checkpoint, ki-pmo, the restatements in ki-delegation and tools-ki code, and these disagree:
  - ki-delegation says `ki agent` is the only writer of the decisions log and the reports, but ki-pmo has the coordinator write both.
  - The two closed lists differ on `briefs/`.
  - `ki agent decide` numbers its entries, against the standard's "no numbers".
- Confidence gap: the `ki agent close` decision gate parses only `## Decision N` headings. All 59 timestamp-headed entries in the ki.ways-of-working decisions log pass it unchecked.
- Tidy gaps:
  - Regular and ad hoc work folders have no prune owner.
  - Briefs are written by hand, and no check compares them with the reports received.
  - Messages lines are drifting in shape.
- `ki repo audit --skill ki-pmo` fails as it already did: 43 FAILs, nearly all PMO-7 unlinked identifiers, plus PMO-9 prune warnings on ki.observatory, ki.tools-burndown and ki.ways-of-working. This run changed nothing that it checks.
- I wrote this report only to the run state path, because the run protocol says that path governs any other. The launcher homes it beside `decisions.md`, so I did not commit a second copy.

## In Progress

Nothing is running. Blocked: the design note's commit and push in ki-principal wait on WORK-GATE-BLOCKED.

Outstanding - no action requested now:

- The ki-pmo to ki-coordination rename sits uncommitted in the ki-agentic-harness working tree, from another session. The note cites the `ki-pmo` paths and says so.
- `+/_WORK/ki.ways-of-working/harness-followups.report.md` and `release-ki.report.md` are untracked from other runs, and `+/_THREADS/` is untracked. I left all three alone.
- The two records that would carry the follow-up are in triage or review: [KI-HARNESS-GOV-200](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-200-thread-folder-closed-list.md) is in triage and [KI-HARNESS-GOV-212](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-212-work-area-ownership.md) is awaiting review. [KI-TOOL-KI-CLI-147](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-147-agent-state-folder-tooling.md) is done and is the base the tools-ki changes build on.

## Queries

### WORK-FOLDER-OWNER - Who owns `+/_WORK/<id>/`

**Context:** You asked which skill keeps a work folder clean and tidy, and how far we can trust the other things that write into it. Today four parties each write part of the folder, and their rules contradict one another. One skill can own the folder's shape and tidy rules outright. The other writers are safe if they follow a four-point contract:

- Write only through the declared entry points.
- Never create a kind of file outside the closed list.
- Leave pruning to the owner's rules.
- Have their output checked by `ki repo audit`.

Under this division:

- The work-folder skill (ki-checkpoint renamed) owns the shape, the closed list, the entry points, the tidy rules, the review area and the Messages line shape.
- ki-coordination owns when to tidy, the judgement of each item's durable home, the decisions entry form and its life cycle, and the report forms.
- ki-delegation owns the run side only. It drops its restatements, including the "only writer" line.
- ki-work-design owns how a design note graduates.

**Query:** Should one work-folder skill own the folder, divided as in §4 of the note?

**Options:**
a) (recommended, confidence medium - the contradictions are verified in the files; the rename is not yet committed) Use the §4 division: the work-folder skill owns shape and tidy rules, ki-coordination owns timing and judgement, ki-delegation owns the run side only, and ki-work-design owns graduation.
b) ki-coordination owns the whole folder, and ki-checkpoint keeps only `work.md`.
c) Leave ownership as it is and only fix the contradictions.

### WORK-FOLDER-NAME - Name for the work-folder skill

**Context:** On 18 October the name was left open between ki-work-file and ki-work-pack.

- `ki-work-folder` says exactly what the skill governs and sits beside ki-work-design.
- `ki-work-pack` clashes with the existing "run packet".
- `ki-work-file` names only `work.md`, not the folder around it.
- `ki-work-area` clashes with ki-repo's "working area".

**Query:** Which name should the skill take?

**Options:**
a) (recommended, confidence medium - plainest match to what it owns, and no clash) `ki-work-folder`.
b) `ki-work-pack`.
c) `ki-work-file`.

### WORK-FOLDER-CHECKS - Where the enforcement work goes

**Context:** The tidy rules need checking in two places.

The rubric checks in `ki repo audit`, to go in KI-HARNESS-GOV-200:

- A file kind outside the closed list fails.
- These warn:
  - reports whose queries are all answered;
  - briefs whose report has been received;
  - finished work that has gone stale;
  - Messages lines in the wrong shape;
  - a review index that is out of step;
  - decision headings the close gate cannot parse.

The tools-ki changes:

- The close gate parses timestamp headings as well as `## Decision N`.
- `ki agent decide` stops numbering its entries.
- `ki agent launch` refuses a brief that names a report path inside the work folder.
- New `ki work message` and `ki work prune` commands.

`ki agent sweep` stays out of the work folder.

You asked on 18 October to fold work into existing records rather than open new ones. [KI-HARNESS-GOV-200](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-200-thread-folder-closed-list.md) is the natural home for the rubric work, but tools-ki owns its own roadmap.

**Query:** Where should the enforcement work be recorded?

**Options:**
a) (recommended, confidence medium - this respects each repository's ownership of its own roadmap) Fold the rubric and skeleton checks into KI-HARNESS-GOV-200, and add one new tools-ki record for the close-gate parse, the unnumbered `decide`, `work message` and `work prune`.
b) Fold everything into KI-HARNESS-GOV-200 as a cross-repository handoff.
c) Defer until the rename lands.

### WORK-GATE-BLOCKED - ki-principal commit gate fails during the rename

**Context:** The ki-principal pre-commit gate refuses every commit with "declared skill ki-pmo is provided by no declared harness". The cause is the ki-pmo to ki-coordination rename. Another session has it uncommitted in the ki-agentic-harness working tree, about 86 changed files, so the harness no longer provides `ki-pmo`, while ki-principal's `.ki.toml` (line 139) still declares it. The brief forbids `--no-verify`, and editing `.ki.toml` is outside this run's scope. So the design note sits untracked at its final path, unchanged, and is ready to commit.

**Query:** How should the design note get committed?

**Options:**
a) (recommended, confidence high - nothing destructive, and the gate clears by itself once the rename is complete) Let the rename session update ki-principal's `.ki.toml` to `ki-coordination` as part of its rename. Then commit `+/_WORK/ki.ways-of-working/design/work-folder.md` by explicit path and push fast-forward, in that session or a short follow-up run.
b) Authorise this run, relaunched, to change the `.ki.toml` declaration itself and commit both together.
