# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › work-package-design

**🤖 → 👤 Handoff to supervisor · Run report at 12:31 BST · last mark 12:04 BST**

---

## Done

Stocktake, read-only: covered the 11 live work folders in ki-principal and `kb.regular.acquire-intake` in personal/acquire, the 6 folders under `+/_WORK_REVIEW/` (5 in ki-principal, 1 in ki-agentic-harness), and the old-shape records in 7 other Capitals (20 checkpoints, 18 thread entries). The result is a per-folder table and ten findings. In short:

- Work files run from 103 to 1,577 words.
- `Next steps` doubles as a log in 4 of the 11.
- In 6 of the 11, open queries have no text anywhere in the repository.
- `Parked` mixes five different kinds of item.
- 5 of the 11 still carry the 18 October MIGRATED message.
- No work states its goals or what work it takes.
- Only 3 of the 11 record which guidance revision they last read.
- `design/` holds files outside the closed list (a shell script and JSON).
- `ki.baseline-rollout` has two folders, one live and one under review.

Design note: [work-package.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/work-package.md), in the ki-work-design brief shape. It sets out:

- the package layout: `work.md` holds the definition, with a routing `description`, Goals and Scope; `state.md`, `queries.md` and `messages.md` are new; `decisions.md`, reports, `briefs/` and `design/` stay as they are
- the front matter for each file
- four reveal levels, saying who reads which file and when
- soft size limits
- the routing model, built on the review's rules: the register is derived from work files, receipt is compulsory but confers no execution authority, held work keeps its hold, and refresh is targeted, with the receiver recording `method_read`
- how it fits ki-work-folder, ki-coordination, ki-delegation, the Work Process note, [GDR-KI-PRINCIPAL-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md) and tools-ki
- a migration plan, with a starting point for each folder

Commit: 5382f613 in ki-principal, by explicit path. The commit gate's repository audit passed with no failures. The commit is local and not pushed. ki-principal `main` is now 24 commits ahead of its remote: this work's earlier commits plus other sessions' `ki.observatory` commits, so Kris decides the push.

Checks: I corrected one claim against the source before committing (all 22 Project notes carry an `outcome`). The note has no em or en dashes. Net record change is zero in every repository. I made no remote calls. The temporary directory is empty.

## In Progress

Nothing is running. Next under the authority is the two blind reviews, work-package-review-fable and work-package-review-codex, then a merged report. The coordinator launches them.

Outstanding - no action requested now: the note relies only on the skill package and the index note for the analogy, because I found no written "knowledge package" definition. Other sessions' uncommitted files in `+/_WORK/ki.chezmoi/` and `+/_WORK/ki.observatory/` were left untouched.

## Queries

### PACKAGE-NAME - What to call the packaged folder

**Context:** Kris asked whether work folders are "work packages". The name "work folder" was settled under WORK-FOLDER-NAME on 18 October, and the renames that followed are still being cleaned up. In project management, a work package is the lowest deliverable in a work breakdown, which in this model is the work item.

**Query:** Should the packaged folder keep the name "work folder" or become "work package"?

**Options:**

a) (recommended, confidence medium - it avoids another rename and a clash with the established project-management meaning) Keep "work folder" and `ki-work-folder`, and describe the shape as packaged like a skill.

b) Adopt "work package" and rename the skill `ki-work-package`, keeping the path; this costs another rename across the harness, `ki`, chezmoi and configuration.

### STATE-FILE - Where the moving state fields live

**Context:** Kris wants `work.md` to define the work, with state in its own file. The state fields (state, target, hold, mark and so on) sit today in `work.md` front matter, and `ki work status` reads them there.

**Query:** Should the state fields move into a new `state.md` front matter, leaving `work.md` as definition only?

**Options:**

a) (recommended, confidence medium - it keeps `work.md` stable, like `SKILL.md`, and splits the Git history of what the work is from the history of its moves, at the cost of one `ki work status` and rubric change) Move the state fields into `state.md`, with `## Now`, `## Next steps` and `## Held`.

b) Keep the state fields in `work.md` and move only the prose; no reader change, but `work.md` still changes at every move.

### QUERIES-FILE - The Q file

**Context:** In 6 of the 11 live works, open queries are named by tag only, with their text in reports, in state-folder reports outside the repository, or nowhere. `ki.chezmoi` keeps 12 of its 25 reports alive only because they hold queries.

**Query:** Should `queries.md` hold every open and parked query in full, with the owner report's Queries rendered from it?

**Options:**

a) (recommended, confidence high - it gives queries a home in the repository and lets reports be pruned once their outcome is homed) Use full query blocks in `queries.md`, copied in when a report is received; delete each answered block in the same commit as its decisions read-back.

b) Make `queries.md` an index of tags pointing to reports; less copying, but reports stay coupled to queries and the state-folder gap remains.

### PARKED-HOME - Where parked items go

**Context:** Today's `Parked` sections mix parked queries, held work with a release condition, to-do lists for a particular screen, ideas and items already resolved.

**Query:** Should `Parked` be split by kind instead of getting its own file?

**Options:**

a) (recommended, confidence medium - a single file would keep the mix) Parked queries go to `queries.md` `## Parked`, held work to `state.md` `## Held`, and ideas to the Project note or a record; no `parked.md`.

b) Create a separate `parked.md` for everything parked.

### MESSAGES-FILE - Where the inbox lives

**Context:** Other works write their Messages lines into the same work file the owner rewrites at every move. Stale lines collect: 7 lines dated 18 October in `ki.chezmoi`, and the MIGRATED line in 5 works.

**Query:** Should the inbox move to its own `messages.md`?

**Options:**

a) (recommended, confidence high - a separate file makes the one write other work may make checkable by path) Use `messages.md`; other work appends one line there and writes nowhere else in the folder.

b) Keep a `## Messages` section, moved into `state.md`.

### DESCRIPTION-SHAPE - The routing description

**Context:** State of play now routes new units of work to existing works, but no work says what it takes. The only stated goal is the Project note's `outcome`, and regular and territory work have no Project note.

**Query:** Should every `work.md` carry a required routing `description` in the style of a skill description?

**Options:**

a) (recommended, confidence medium - it gives routing something to match against at every level of work) Make `description` required: at most 500 characters, in the form "does ... Takes ... Not for ...", naming neighbouring works by id and written by the steward. Goals link the Project `outcome` rather than copy it.

b) Route on the Project `outcome` alone; one fewer field, but it says nothing about what the work takes and leaves regular and territory work uncovered.

### ROUTE-RECEIPT - What a routed work must do

**Context:** Kris said a routed work "has to accept it". The Codex review added three rules: receipt grants no execution authority, conflicts are flagged back, and paused holds are preserved.

**Query:** Should receipt mean a recorded disposition, with no execution authority?

**Options:**

a) (recommended, confidence high - it combines Kris's words with the review's rules) The receiver acts on every routed line at its next bootstrap or owner message and records one disposition: a next step, a query to Kris, or a return to State of play with the reason. Paused work keeps the line waiting; more-expected work is released by it; units that already have an owner bypass the hub.

b) Act on routed lines only at the next mark; less interruption, slower routing.

### REFRESH-TARGET - How method refresh reaches works

**Context:** Only 3 of the 11 live works record which guidance revision they read, so a refresh cannot tell which works are behind. WOW-REFRESH a) has Ways of working send refresh lines directly while the method is being defined.

**Query:** Should a `method_read` field drive targeted refresh lines?

**Options:**

a) (recommended, confidence high - it adds the missing field to rules that already exist) Record `method_read` in `state.md`. Send one coalescing `REFRESH` line only to affected works that are behind; updating the field is the confirmation. Held work waits, and the bootstrap check stays as the fallback.

b) Broadcast every method change to every live work and ask each to acknowledge in one line.

### STEWARD-HOME - Who carries method changes after Ways of working closes

**Context:** Kris decided that Ways of working goes away once the method is defined and that State of play then takes stewardship. State of play executes nothing itself, so accepted improvements still need a worker.

**Query:** How should State of play get accepted method improvements done once Ways of working has closed?

**Options:**

a) (recommended, confidence low - how much the method will change after it settles is unknown, so start light) State of play keeps a method backlog and dispatches each improvement as ad hoc regular work, `ki.regular.<slug>`, or to the Project it most affects.

b) A standing regular work for method upkeep, defined by an Activity note with a periodic review.

### MIGRATE-PATH - How the live folders move

**Context:** Only a folder's own work writes or deletes in it. The review asked for a pilot with one active and one held work. Held works have no session to migrate themselves.

**Query:** Should migration pilot two works, then let each work migrate at its own next mark?

**Options:**

a) (recommended, confidence medium - it matches the review's pilot and folder ownership) Open a tolerance window. Pilot `ki.ways-of-working` and `ki.regular.registry-removal`. Each live work then migrates at its own next mark, held works through one owner-approved mechanical run, and other Capitals go straight to the package shape at their own migration.

b) After the pilot, run one owner-approved mechanical sweep of all 11 folders; faster, but it writes into active works' folders from outside.
