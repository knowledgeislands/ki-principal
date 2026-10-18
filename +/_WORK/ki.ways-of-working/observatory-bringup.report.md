# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › observatory-bringup

**🤖 → 🧑 Handoff to supervisor · Run report at 05:25 BST · last mark 04:06 BST**

---

## Done

- apps-observatory.local is in line with the work model. I worked through the four items in the [Observatory bring-up note](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/bring-up/observatory.md) in order. All four are filed under the ways-of-working Project and pushed to `main`. Three are Awaiting review and one is Ready.
- `0d756d1` and `0be5dc5`: reserved the four identifiers and captured the four records.
- `49263a8`: [KI-OBSERVA-VIS-025](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-025-work-instrument.md) Work instrument, now Awaiting review. It shows the territory's work from `ki work status --format json` in five views: with you, stuck, blocked, moving and on hold. Run items sit beneath their work, and `+/_WORK_REVIEW/` is counted. Beneath the views, each work's latest `*.report.md` reads as prose, newest first, so your morning summary is in the Observatory. Against the territory it showed `ki.ways-of-working` as stuck with its three runs, plus seven latest reports, and no local path.
- `5d18927`: [KI-OBSERVA-VIS-026](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-026-review-queue-work-folders.md) Review queue work folders, now Awaiting review:
  - Open queries come from `+/_WORK/` reports. They count as answered when a decisions log names the tag, numbered or not.
  - Work with you links to the Work view.
  - `+/_WORK_REVIEW/` work is its own group.
  - A repository still read from `+/_THREADS/` is named as legacy.
  - Against the territory it found 43 open queries, all from work folders, and 6 migrated works, with no local path.
- `06bd72a` and `9886381`: [KI-OBSERVA-BCN-007](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BCN-007-beacon-raises-stuck-work.md) Beacon raises stuck work, now Awaiting review. The Work instrument is a Beacon contributor:
  - Stuck and blocked lines raise attention.
  - A paused hold past 31 days, and each line with you, raises a note.
  - Each signal lands on its line in the Work view.
  - Against the territory it raised one signal, `ki.ways-of-working` as stuck.
- `db28ae3`: [KI-OBSERVA-VIS-027](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-027-themes-in-streams-read.md) Themes in Streams read, now Ready with a five-step plan against the moved Streams: four themes and 21 flat Projects in Knowledge Islands Principal.
- Checks at each delivery:
  - `bun run test`, typecheck, build, knip and rumdl pass.
  - `biome check` reports only its 13 earlier findings, none in a line I touched.
  - `ki repo audit` reports only the earlier ITEM-1 finding on KI-OBSERVA-VIS-022's title.
  - The browser smoke check skipped, because Chromium is not installed here.

## In Progress

Nothing is running. The scratch folder `apps-observatory.local/tmp/ways-of-working/observatory-bringup/` is deleted.

Outstanding - no action requested now:

- The Observatory service needs a restart to serve these deliveries. A detached run never restarts it.
- The audit's ITEM-1 finding on [KI-OBSERVA-VIS-022](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-022-judge-overdue-against-each-job-schedule.md)'s title was there before this run. The Observatory work's parked OBS-OVERDUE-TITLE query looks to cover it.
- The browser smoke check needs Chromium for Playwright. I made no installs.
- Two signals can fire for the same run until the Sessions readers retire: one from Sessions and one from Work.

## Queries

### OBS-SESSIONS-RETIRE - when the Sessions readers retire

**Context:** KI-OBSERVA-BCN-007 was shaped to retire the Sessions instrument's checkpoint reader, threads table and run-packet contributor. Knowledge Islands Principal still holds `+/_THREADS/ways-of-working/`, though. The run packet also records runs that `ki work status` shows only when they are homed in a work folder. The Sessions `waiting` signal has no counterpart in the work contract. I moved the retirement out of BCN-007 until migration phase 5 closes the tolerance window, provisional, for Kris to confirm.

**Query:** Should the Sessions readers retire at phase 5 under a record of their own?

**Options:**

a) (recommended, confidence medium - nothing is lost while legacy folders remain, and one record can plan the retirement with the Streams rewording) File a new record for the retirement, blocked on phase 5, and take KI-OBSERVA-VIS-027 alongside it. b) Fold the retirement into KI-OBSERVA-VIS-027 as its last step. c) Retire them now and accept that legacy-homed runs drop out of the Observatory.

### OBS-STREAMS-VIEW - what the Sessions instrument becomes

**Context:** Once threads and runs leave it, the Sessions instrument holds only themes and Projects from Streams. KI-OBSERVA-VIS-027 rewords it but keeps its name and route.

**Query:** Should the Sessions instrument become a Streams view once its thread and run readers retire?

**Options:**

a) (recommended, confidence medium - the name would then describe what it shows, and the Work view already owns runs) Rename it to Streams in the retirement record and keep `sessions` addresses redirecting. b) Keep the name Sessions. c) Fold themes and Projects into the Work view and retire the instrument.

### OBS-WITH-YOU-SIGNAL - one note per waiting work

**Context:** BCN-007's Goal says the Beacon "shows the work with the owner". I raised one note per work or item with you, each landing on its line, rather than one count. Provisional, for Kris to confirm.

**Query:** Do you confirm one Beacon note per work with you?

**Options:**

a) (recommended, confidence medium - each note lands on its own row and is marked new when it arrives) Confirm one note per line. b) Raise one note carrying the count instead.

### OBS-KI-CONTRACT-GAPS - views and review count derived locally

**Context:** `ki/work-status/v1` carries entries, not the five views. It also shows the `+/_WORK_REVIEW/` count only in its text form. The Observatory therefore derives the views by the printed rules and counts the review folders itself, provisional, for Kris to confirm.

**Query:** Should tools-ki publish the views and the review count in a later work-status schema?

**Options:**

a) (recommended, confidence medium - one derivation instead of two that can drift) Ask tools-ki for both in `ki/work-status/v2`, and keep the Observatory's derivation until then. b) Keep deriving them in the Observatory.

### OBS-RECORD-FIELDS - Project field and titles of the four records

**Context:** The four records carry `project: ways-of-working` and no theme field, because the roadmap schema has none. Their titles are shortened to four words or fewer for the audit's ITEM-1 rule, for example "Work instrument" and "Themes in Streams read". Provisional, for Kris to confirm.

**Query:** Do you confirm the Project field and the shortened titles?

**Options:**

a) (recommended, confidence high - they satisfy the audit and keep the rollout under one Project, as you set) Confirm both. b) Move the records to the observatory Project once the rollout ends.

## Restart prompt

The Observatory work is paused until the work migration lands. Paste this into an interactive session in the ki-principal checkout to resume it.

```text
Resume KI > Model > Observatory, work id ki.observatory, from +/_WORK/ki.observatory/work.md under current ki-pmo and ki-delegation.

The ways-of-working run observatory-bringup has done the four bring-up items in apps-observatory.local, all pushed to main:
- KI-OBSERVA-VIS-025 Work instrument: Awaiting review.
- KI-OBSERVA-VIS-026 Review queue work folders: Awaiting review.
- KI-OBSERVA-BCN-007 Beacon raises stuck work: Awaiting review; the Sessions readers' retirement is deferred to phase 5 (query OBS-SESSIONS-RETIRE).
- KI-OBSERVA-VIS-027 Themes in Streams read: Ready with a plan.
Its report is +/_WORK/ki.ways-of-working/observatory-bringup.report.md, with five queries.

First steps:
1. A service restart is due, because the service runs the primary checkout: launchctl kickstart -k "gui/$(id -u)/uk.me.kris.rig.observatory", then confirm http://127.0.0.1:1675/ answers. Ask Kris before running it.
2. Re-read the work file, decisions.md and the Messages section, mark, and take stock (ki agent status; apps-observatory.local roadmap and git status).
3. Walk Kris through the three records awaiting review in the Work, Review queue and Beacon views, and take the report's queries.
4. Put back the parked queries OBS-SESSIONS-ACCEPT and OBS-REVIEW-ACCEPT for KI-OBSERVA-VIS-023 and KI-OBSERVA-VIS-024, OBS-REVIEW-OPEN and OBS-OVERDUE-TITLE.
5. Then deliver KI-OBSERVA-VIS-027 as a run, and the carried work: the serving and live-reload triage record and unit 3, Capture feedback.
Then banner.
```
