# ki.timelines queries

## Open

### TIMELINE-IMPROVEMENTS - Kris's improvements to the scope

since 2026-10-19 · from [tl-seed](/Users/krisbrown/.local/state/ki/agents/timelines/tl-seed.report.md) · survey open question 11

**Context:** TIMELINES-OPEN says you have improvements to the scope, and the read-back asks for them before any design run. The survey is now ready to design against.

**Query:** What are your improvements to the scope?

**Options:**

a) (recommended, confidence high - the read-back puts this before any design run) Give them now, in speech, and the coordinator logs them before launching design.

b) Start design on the scope as it stands and fold the improvements in later.

### PUSH-STACK - Push the stacked ki-principal commits

since 2026-10-19 · from [tl-seed](/Users/krisbrown/.local/state/ki/agents/timelines/tl-seed.report.md) · (looks resolved; the worker judges): all three commits are on `origin/main` at the migration

**Context:** `origin/main` in ki-principal lacks three commits: my survey commit `602f714` and two ki.mac-studio-setup commits from another session, `1a9af8a` and `de7c19e`. I may push only my own commits, so I pushed nothing.

**Query:** Should the three stacked commits be pushed together?

**Options:**

a) (recommended, confidence medium - the other two are docs-only work-folder and Project commits, but I have not reviewed them) Let the mac-studio-setup session or you push all three fast-forward.

b) Leave them unpushed until the mac-studio-setup session pushes its own work.

### FEED-HOME - Where subscription feeds are served

since 2026-10-19 · from [tl-seed](/Users/krisbrown/.local/state/ki/agents/timelines/tl-seed.report.md) · survey open question 1

**Context:** 5G serves feeds from its own Cloudflare site, with an Access bypass on `/calendars/*`. legal-principal and personal-principal have no site, and their dates are private.

**Query:** Where should a knowledge base without a site serve its calendar feeds?

**Options:**

a) (recommended, confidence low - this rests only on the survey; nothing has been designed yet) Take it into the design run as an open question, with the base's own site, the Observatory and a private-feed host as candidates.

b) Decide now that each base serves its feeds from its own site.

### BUSY-STATUS - Busy-status vocabulary and default

since 2026-10-19 · from [tl-seed](/Users/krisbrown/.local/state/ki/agents/timelines/tl-seed.report.md) · survey open question 2

**Context:** 5G writes every event as free and holds dates only. legal holds some times of day and marks some dates `hard`.

**Query:** Should busy status be a per-item field that defaults to free, with all-day items blocking time only when they are marked as blocking?

**Options:**

a) (recommended, confidence medium - this matches today's 5G behaviour and leaves legal's hard dates able to block time) Per-item `busy` defaulting to free; it maps to `TRANSP` and the client busy-status properties.

b) Default to busy for deadlines and events, and free otherwise.

### ONE-SOURCE - Programme timeline and calendar registry

since 2026-10-19 · from [tl-seed](/Users/krisbrown/.local/state/ki/agents/timelines/tl-seed.report.md) · survey open questions 4 and 5

**Context:** 5G holds the same 11 milestones twice: as structured registry entries and as free-text programme timeline files, with nothing linking the two. legal generates its timeline from the dates on its Items.

**Query:** Should one structured source feed both the timeline view and the calendar feeds?

**Options:**

a) (recommended, confidence medium - two copies of one fact drift apart, and legal already generates its timeline from a single source) Use one source, the dated items, and generate the timeline view and the feeds from it.

b) Keep two lists and link them by entry id.

### DATE-MODEL - Dates only, or times and a time zone too

since 2026-10-19 · from [tl-seed](/Users/krisbrown/.local/state/ki/agents/timelines/tl-seed.report.md) · survey open question 3

**Context:** 5G holds dates only and writes no time zone. legal's rows carry an optional `HH:MM` time and a file-level time zone.

**Query:** Should the skill model an optional time of day and a time zone?

**Options:**

a) (recommended, confidence medium - one of the first adopters, legal, already needs times) Make a time optional per item, with one time zone per calendar set; items without a time stay all-day.

b) Dates only, keeping a time as a label, as the Command Centre does with `due_time`.

### SKILL-SHAPE - Skill shape, name and code home

since 2026-10-19 · from [tl-seed](/Users/krisbrown/.local/state/ki/agents/timelines/tl-seed.report.md) · survey open questions 7 and 8

**Context:** KI-HARNESS-GOV-222 asks three things: whether this is one skill or a skill plus a view; which of `ki-calendars`, `ki-timelines` or `ki-key-dates` to use as the name; and whether the code lives in the harness, `tools-ki` or a shared package.

**Query:** Should these be settled in the design run rather than now?

**Options:**

a) (recommended, confidence high - each depends on FEED-HOME and ONE-SOURCE) Settle them in the design run under `ki-work-design`.

b) Name the skill and choose a code home now.

## Parked

None.
