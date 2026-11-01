# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › blind-top-level

**🤖 → 👤 Handoff to supervisor · Run report at 23:45 GMT · last mark 13:55 GMT**

---

## Done

- Completed the independent read-only review; no repository changes or commits.
- Verified the launcher, rules and audit admit top-level reports; several report readers also assume that location.
- Independently counted 182 top-level reports in 17 work folders across five repositories, using filenames only.
- Tested the proposed ignore exception locally: it admits package-level reports while keeping reports elsewhere ignored; it does not admit reports inside a group.
- Respected the blind boundary: no prohibited query file, decisions log, cause note or report was read; no remote calls or background agents were used.

## In Progress

Nothing is running. Implementation and migration await the owner's decisions and the relevant repository authority.

Outstanding - no action requested now: the dated owner instructions and the layout decision's current status are supplied facts, not independently verified against decision logs. No report's receipt, durable home or deletion eligibility was assessed. Runtime behaviour was inspected in source, not exercised; the ignore exception alone was tested in an isolated temporary repository, subsequently removed.

## Findings

### REPORT-INFLOW - The layout is produced by the system

**Goal:** Assess whether reports should enter a `reports/` folder before LAYOUT-SHAPE is settled.

**Scope:** Permitted package design, canonical work-package, delegation, coordination and repository skills, and tools-ki launcher and reader source. No prohibited package material was read.

**As of:** 31 October 2026, 23:45 GMT.

The cause is a consistent older contract across writer, rules and enforcement, rather than merely missed tidying. The launcher's destination is defined in [thread.ts](/Users/krisbrown/kis/knowledge-islands/tools-ki/src/core/agent/thread.ts:91), and [events.ts](/Users/krisbrown/kis/knowledge-islands/tools-ki/src/core/agent/events.ts:708) copies completed reports there. The [closed list](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md:74) permits that location, and [the audit](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/scripts/rubric/contexts/work-folder.ts:82) accepts report files there while rejecting a `reports/` directory.

A destination-only fix is incomplete. Independently checked consumers include state-file adoption and query-option lookup in [thread.ts](/Users/krisbrown/kis/knowledge-islands/tools-ki/src/core/agent/thread.ts:178), name reuse and relaunch protection in [runs.ts](/Users/krisbrown/kis/knowledge-islands/tools-ki/src/core/agent/runs.ts:624), reviewer evidence validation in [selection.ts](/Users/krisbrown/kis/knowledge-islands/tools-ki/src/core/agent/selection.ts:184), and received-brief detection in [the audit](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/scripts/rubric/contexts/work-folder.ts:121). History checks also depend on report paths. These need coherent treatment of old and new locations during transition, including protection against restoring a retired report. Observatory consumer claims in the permitted design were not independently checked.

The shared ignore rule is confirmed in [the generated block source](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/keystone/ki-repo/scripts/rubric/contexts/gitignore.ts:71). The exact package-level exception in the brief passed a scratch test. Both group-first layouts could require another move later; B also needs an exception that reaches nested group report folders. Interim `reports/` therefore has a real migration cost and must be described as temporary, without treating A as the final decision.

Raises REPORT-LOCATION below.

### REPORT-BACKLOG - Relocation and disposal are different decisions

**Goal:** Assess who should clear existing top-level reports once the new destination lands.

**Scope:** Filename inventory under the permitted work-folder roots and the stewardship and tidy rules. Report contents and their outcomes were not inspected.

**As of:** 31 October 2026, 23:45 GMT.

The brief's 182 reports, 17 folders and five repositories are independently confirmed. The [entry-point rules](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md:97) reserve package maintenance to its steward, while [tidying](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md:127) requires durable homes and individual explicit-path deletions. The [coordination rule](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md:1123) already provides the alternative message-to-steward route.

A bounded relocation need not judge outcomes or dispose of evidence. It can bring the existing stock into the new shape without waiting for quiet or held packages to reach another mark. However, a repository boundary alone grants no authority over every package within it: a sweep needs explicit scope covering the named packages and agreement on concurrent writers. It must stop on destination collisions, contested changes or unresolved ownership. Moving also changes paths, potentially breaking incoming links and relative links inside reports; no link audit was performed here. The safe transition must preserve access and resolve those references rather than assuming an unchanged report body is enough.

Raises REPORT-CLEARANCE below.

## Queries

### REPORT-LOCATION - Where new reports should land now

**Context:** The current launcher, rules and audit reproduce the top-level layout. Tidying cannot keep the five-file top level while a still-needed report remains there. A temporary `reports/` destination is reversible and stops new accumulation, but requires coordinated reader, recovery, audit and ignore changes. It may need another move under either group-first choice; it must not silently settle LAYOUT-SHAPE.

**Query:** Should the system use a temporary package-level `reports/` folder now, or wait for the final layout?

**Options:**

a) (recommended, confidence high - the automatic inflow is directly verified, and changing its destination is reversible) Change the launcher, readers, rules, audit and managed ignore exception now to use `reports/`, retaining LAYOUT-SHAPE as an open decision and supporting existing report locations during migration.

b) Answer LAYOUT-SHAPE first and change once to its chosen layout; accept top-level arrivals until that coordinated change lands.

c) Keep reports at the top level and require strict steward tidying at each mark; accept that retained reports still prevent the five-file top level.

### REPORT-CLEARANCE - Who relocates the existing reports

**Context:** The backlog spans 17 separately stewarded folders. Waiting for each next mark has no bounded completion time. Moving reports preserves their evidence without judging durable homes; deletion still requires the steward's judgement. A sweep needs a named file list, explicit package authority in each repository, coordination with live runs, collision checks and preservation of working references. The current rules do not themselves grant that sweep authority.

**Query:** Should existing reports be relocated by bounded repository sweeps or left to each steward's next tidy?

**Options:**

a) (recommended, confidence medium - a move-only sweep gives bounded structural completion without guessing outcomes, but live-path and ownership risks remain untested) Authorise one bounded sweep per repository to move the inventoried top-level reports into `reports/`, with no report disposal, under the safeguards above; stewards receive the relocation result and prune eligible reports later.

b) Send one State of play message per folder and have its steward tidy at the next mark, deleting reports whose outcomes are homed and moving the rest into `reports/`; accept that held or quiet folders may retain the old layout indefinitely.

### 🤖 → 👤 Handoff to supervisor · since 23:45 GMT

👤 2 with you

- [with you] REPORT-LOCATION · owner · since 23:45 GMT
- [with you] REPORT-CLEARANCE · owner · since 23:45 GMT

🧵 ki.prj.ways-of-working
