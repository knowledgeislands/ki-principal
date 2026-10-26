# [Foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Timelines](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/timelines.md) › tl-seed

**🤖 → 👤 Handoff to supervisor · Run report at 11:07 BST · last mark 11:02 BST**

---

## Done

- Added the [Timelines](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/timelines.md) Project note (theme `foundations`, active, lead Kris Brown) and its line in [Projects](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/Projects.md), commit `f4f3cd2`. The commit audit passed with one warning: the Project has no open records yet. The [Foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/foundations.md) theme page lists no Projects, so I left it unchanged.
- Correction: the first commit attempt failed the commit audit (rule STREAM-9) because the note named [KI-HARNESS-GOV-222 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-222-timeline-and-calendar-skill.md). Registry notes may not name work records. The note now says "the existing calendar record in the `ki-agentic-harness` roadmap", and its TIMELINES-OPEN quote stops before the record identifier.
- Wrote the [survey](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.timelines/design/survey.md), commit `602f714`, commit audit passed. It covers four areas:
  - the 5G Emerge calendar component: its data shape, busy status, how feeds are built and where they are served, its views, and what is 5G-specific;
  - [KI-HARNESS-GOV-222 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-222-timeline-and-calendar-skill.md), summarised in full;
  - the three first adopters;
  - existing harness standards that touch dates.
- Key facts from the survey:
  - Every 5G event is written as free (`TRANSP:TRANSPARENT`).
  - Feeds are static files at `phase3.5g-emerge.io/calendars/*`. That path bypasses Cloudflare Access so people can subscribe without signing in.
  - 5G's separate programme timeline duplicates the 11 `phase3-programme` registry entries with free-text dates, and nothing links the two.
  - The legal gantt is generated from the dates on Command Centre Items. Its row schema (`fr-timeline/1`) includes times of day.
  - personal-principal keeps its future dates in prose, not in structured fields.
  - No harness skill covers kept dated items or calendar feeds today.
- Not pushed: `origin/main` also lacks two commits from another session (`1a9af8a`, `de7c19e`, both ki.mac-studio-setup), stacked under my `602f714`. `f4f3cd2` was already on `origin`.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- [KI-HARNESS-GOV-222 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-222-timeline-and-calendar-skill.md) still names `project: observatory`. Moving it to `timelines` is the harness's call; it is listed as open question 9 in the survey.

## Queries

### PUSH-STACK - Push the stacked ki-principal commits

**Context:** `origin/main` in ki-principal lacks three commits: my survey commit `602f714` and two ki.mac-studio-setup commits from another session, `1a9af8a` and `de7c19e`. I may push only my own commits, so I pushed nothing.

**Query:** Should the three stacked commits be pushed together?

**Options:**

a) (recommended, confidence medium - the other two are docs-only work-folder and Project commits, but I have not reviewed them) Let the mac-studio-setup session or you push all three fast-forward.

b) Leave them unpushed until the mac-studio-setup session pushes its own work.

### TIMELINE-IMPROVEMENTS - Kris's improvements to the scope

**Context:** TIMELINES-OPEN says you have improvements to the scope, and the read-back asks for them before any design run. The survey is now ready to design against.

**Query:** What are your improvements to the scope?

**Options:**

a) (recommended, confidence high - the read-back puts this before any design run) Give them now, in speech, and the coordinator logs them before launching design.

b) Start design on the scope as it stands and fold the improvements in later.

### FEED-HOME - Where subscription feeds are served

**Context:** 5G serves feeds from its own Cloudflare site, with an Access bypass on `/calendars/*`. legal-principal and personal-principal have no site, and their dates are private.

**Query:** Where should a knowledge base without a site serve its calendar feeds?

**Options:**

a) (recommended, confidence low - this rests only on the survey; nothing has been designed yet) Take it into the design run as an open question, with the base's own site, the Observatory and a private-feed host as candidates.

b) Decide now that each base serves its feeds from its own site.

### BUSY-STATUS - Busy-status vocabulary and default

**Context:** 5G writes every event as free and holds dates only. legal holds some times of day and marks some dates `hard`.

**Query:** Should busy status be a per-item field that defaults to free, with all-day items blocking time only when they are marked as blocking?

**Options:**

a) (recommended, confidence medium - this matches today's 5G behaviour and leaves legal's hard dates able to block time) Per-item `busy` defaulting to free; it maps to `TRANSP` and the client busy-status properties.

b) Default to busy for deadlines and events, and free otherwise.

### ONE-SOURCE - Programme timeline and calendar registry

**Context:** 5G holds the same 11 milestones twice: as structured registry entries and as free-text programme timeline files, with nothing linking the two. legal generates its timeline from the dates on its Items.

**Query:** Should one structured source feed both the timeline view and the calendar feeds?

**Options:**

a) (recommended, confidence medium - two copies of one fact drift apart, and legal already generates its timeline from a single source) Use one source, the dated items, and generate the timeline view and the feeds from it.

b) Keep two lists and link them by entry id.

### DATE-MODEL - Dates only, or times and a time zone too

**Context:** 5G holds dates only and writes no time zone. legal's rows carry an optional `HH:MM` time and a file-level time zone.

**Query:** Should the skill model an optional time of day and a time zone?

**Options:**

a) (recommended, confidence medium - one of the first adopters, legal, already needs times) Make a time optional per item, with one time zone per calendar set; items without a time stay all-day.

b) Dates only, keeping a time as a label, as the Command Centre does with `due_time`.

### SKILL-SHAPE - Skill shape, name and code home

**Context:** [KI-HARNESS-GOV-222 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-222-timeline-and-calendar-skill.md) asks three things: whether this is one skill or a skill plus a view; which of `ki-calendars`, `ki-timelines` or `ki-key-dates` to use as the name; and whether the code lives in the harness, `tools-ki` or a shared package.

**Query:** Should these be settled in the design run rather than now?

**Options:**

a) (recommended, confidence high - each depends on FEED-HOME and ONE-SOURCE) Settle them in the design run under `ki-work-design`.

b) Name the skill and choose a code home now.

### 🤖 → 👤 Handoff to supervisor · since 11:07 BST

👤 7 with you

- [with you] PUSH-STACK · owner · since 11:07
- [with you] TIMELINE-IMPROVEMENTS · owner · since 11:02
- [with you] FEED-HOME · owner · since 11:07
- [with you] BUSY-STATUS · owner · since 11:07
- [with you] ONE-SOURCE · owner · since 11:07
- [with you] DATE-MODEL · owner · since 11:07
- [with you] SKILL-SHAPE · owner · since 11:07
- [committed] Project note, pushed
- [unpushed] survey, stacked on two mac-studio-setup commits
