# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › work-package-review-codex

**🤖 → 👤 Handoff to supervisor · Run report at 12:36 BST · last mark 12:04 BST**

---

## Done

- Reviewed the [design](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/work-package.md) against Kris's 12:09 and 12:24 words in the [decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md); no other review report read. The design itself contains a previous review's summary, so this was independent judgement of the design, rather than complete blindness to prior advice.
- Verdict: the package model and definition/state split fit Kris's intent. Use “work package” for the concept without renaming the directory or skill. The migration is not yet safe enough for running sessions.
- Stocktake check passed on 11 live folders: chezmoi has 62 lines/1,577 words, 25 reports and 11 Messages; registry-removal retains the old nested Messages block; tools-burndown has four JSON design files and no front-matter mark; the baseline-rollout twin exists. Observatory has since grown to 36 lines/298 words, consistent with a moving snapshot.
- Stocktake correction: [baseline-rollout/work.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/work.md:25) already contains WAVE-1's proposed scope. Its complete owner-query block is missing, rather than all query text.
- Progressive reveal: a short routing description, Goals and Scope are sufficient. The claimed 150-token register entry is unmeasured; measure the actual two-file metadata. Reading every decision and query on every owner message recreates the context burden; read changes and relevant entries after bootstrap.
- Migration gaps in [points 37-41](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/work-package.md:223): rubric tolerance alone does not protect old status readers, hooks, openers or running writers. Upgrade consumers first; define format detection/read precedence; have each steward pause all folder writers, recheck current contents and switch once. Send migration notices to the existing Messages location until that folder switches. Never maintain two authoritative state copies.
- Refresh gap in [point 29](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/work-package.md:209): specify exactly which guidance a revision attests to, how revision ordering is checked, and preserve every outstanding change when coalescing. A last notice replacing an earlier one must not lose an unread requirement.
- Overbuilt: five compulsory files for the 103-word regular work, fixed two-to-four goals and heuristic bans on dates/SHAs. Create empty detail files only when needed; warn on bulk/history rather than legitimate evidence pointers. Missing: routable does not mean a session is alive; show existing state/beat freshness and give a resume/escalation path for unattended inboxes.
- Safety checks passed: no repository edits, commits, pushes, remote calls or other review-report reads; only the requested runtime status and this report were written. Commit identifiers: none.

## In Progress

Nothing running. The supervisor owns the merged report and owner decisions; implementation remains outside this review's authority.

Outstanding - no action requested now: retain every unresolved query and its source during migration. Recover missing text before tidying; do not drop tags merely because retired reports are inconvenient to recover. Keep held state and mark unchanged during a mechanical split.

## Queries

### PACKAGE-NAME - What to call the packaged folder

**Context:** Kris asks for a package concept; another skill rename adds deployment work without changing the model.

**Query:** Use “work package” for the concept while retaining the physical and skill names?

**Options:**

a) (recommended, confidence medium - concept and storage can have distinct, clearly defined names) Note option c: define work package once; retain work folder and `ki-work-folder`.

b) Note option a: use work folder throughout.

### STATE-FILE - Where moving state fields live

**Context:** Dynamic state currently obscures the work's stable purpose.

**Query:** Move state metadata and continuation prose together?

**Options:**

a) (recommended, confidence high - one authoritative state home keeps definition small) Note option a, after compatible consumers land.

b) Note option b: retain state metadata in `work.md`.

### QUERIES-FILE - The Q file

**Context:** Tag-only references leave restart inputs outside the repository.

**Query:** Keep complete unanswered queries locally?

**Options:**

a) (recommended, confidence high - full questions survive report disposal and session loss) Note option a; preserve source and tag, and keep answered context until its decision is recorded.

b) Note option b: retain an index into reports.

### PARKED-HOME - Where parked items go

**Context:** The current Parked section mixes decisions, waiting work and ideas.

**Query:** Separate these by meaning?

**Options:**

a) (recommended, confidence high - each kind gets an existing, unambiguous owner) Note option a; every held item also needs its release condition.

b) Note option b: one mixed parked file.

### MESSAGES-FILE - Where the inbox lives

**Context:** Separating incoming writes reduces collisions with state rewrites, but simultaneous inbox edits remain possible.

**Query:** Give messages their own file?

**Options:**

a) (recommended, confidence high - a dedicated inbox isolates the cross-work write boundary) Note option a, with serialised append/removal and a source-linked disposition before removal.

b) Note option b: keep Messages inside state.

### DESCRIPTION-SHAPE - The routing description

**Context:** Outcomes describe success, while dispatch needs intake boundaries.

**Query:** Require a short local intake description?

**Options:**

a) (recommended, confidence high - purpose plus intake and exclusions distinguishes neighbouring works) Note option a; use 500 characters as guidance, avoid duplicating the Project outcome, and validate with ambiguous routing examples.

b) Note option b: route from outcomes alone.

### ROUTE-RECEIPT - What routed work must do

**Context:** Kris requires acceptance; execution still needs the receiving work's authority.

**Query:** Require a recorded disposition at the next safe receive point?

**Options:**

a) (recommended, confidence high - compulsory ownership of disposition respects authority and holds) Note option a; escalate disputed routing to State of play/Kris rather than silently bouncing it, and expose unattended messages.

b) Note option b: wait for the next mark.

### REFRESH-TARGET - How method refresh reaches works

**Context:** Targeting is useful, but one revision must have a defined coverage contract.

**Query:** Use targeted notices with explicit read evidence?

**Options:**

a) (recommended, confidence medium - sound once revision coverage and lossless coalescing are specified) Note option a, qualified by the refresh gap above; record all applicable guidance read, preserve pending effects, and retain bootstrap fallback.

b) Note option b: broadcast and require acknowledgements.

### STEWARD-HOME - Who carries method changes after Ways of working closes

**Context:** Kris explicitly makes Ways of working finite and State of play the continuing dispatch point.

**Query:** Dispatch method implementation through existing work before creating standing upkeep work?

**Options:**

a) (recommended, confidence high - follows Kris's stated end state without inventing another permanent coordinator) Note option a; keep durable method authority in its existing skills and decision owners.

b) Note option b: create standing regular upkeep work once a demonstrated recurring obligation justifies it.

### MIGRATE-PATH - How live folders move

**Context:** An outside sweep can overwrite running sessions; the proposed incremental route still lacks consumer and writer safeguards.

**Query:** Pilot and migrate incrementally after those safeguards are defined?

**Options:**

a) (recommended, confidence medium - ownership-led cutovers minimise concurrent-writer risk) Note option a, with the migration safeguards above, explicit pilot exit checks and an inventory covering live, review-held and legacy folders; do not close tolerance on live folders alone.

b) Note option b: sweep only after every writer is explicitly quiescent and the owner authorises the exact set.

### 🤖 → 👤 Handoff to supervisor · since 12:36 BST

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [with you] Work-package review and ten decision recommendations · supervisor · since 12:36 BST
