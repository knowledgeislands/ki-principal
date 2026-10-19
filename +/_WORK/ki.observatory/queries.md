# ki.observatory queries

## Open

### CONDITION-HOME - Where maturity and decline live

since 2026-10-19 · from the Summary at 12:25 BST, after [obs-step3](/Users/krisbrown/.local/state/ki/agents/observatory/obs-step3.report.md)

**Context:** Your model is that each island declares its maturity, and decline or ruin is a separate quality scale. Every possible home needs work in other repositories (the ki-repo standard in the harness, and a `ki` contract in tools-ki), so that the Observatory reads the values rather than inventing them.

**Query:** Where should an island declare its maturity, and where should decline or ruin come from?

**Options:**

a) (recommended, confidence medium - the island speaks for its own maturity, and audit already measures quality mechanically) Maturity is declared in each island's `.ki.toml` from a fixed scale the ki-repo standard defines. Decline is derived from `ki repo audit` health. `ki` exposes both to the Observatory, through handoff records to the harness and tools-ki.

b) Both are declared by hand in `.ki.toml`.

c) Both are held in the Capital's Known Lands inventory, which is one place to edit but means the Capital speaks for each island.

d) As in a), with a KI specification defining both scales first, which takes longer.

### DIAGRAM-PIES - The email triage pies

since 2026-10-19 · from the Summary at 12:25 BST, after [obs-pies](/Users/krisbrown/.local/state/ki/agents/observatory/obs-pies.report.md)

**Context:** There are four pies, all from one email-triage pattern in two repositories. Each repository has a status note and the template that writes it: [personal-principal's Email Triage Status](/Users/krisbrown/workspaces/personal/personal-principal/Pillars/Productivity/Knowledge%20Management/KB%20Specifics/Email/Email%20Triage%20Status.md) and [hnr-principal's Email Status](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Admin/Knowledge%20Management/KB%20Specifics/Email/Email%20Status.md). In both, the table beside the pie already holds the same counts, and the HNR pie has 18 slices.

**Query:** Should the pies be dropped in favour of the tables?

**Options:**

a) (recommended, confidence high - the tables already carry the counts, and 11 to 18 slices can't be read as a pie) Drop the pies from both templates and notes, sort each table by count, and add a one-line total, with one record in each repository.

b) Replace each pie with a bar chart, which would still be Mermaid.

### NEW-MARK - What "new" means on the Beacon

since 2026-10-19 · from the Summary at 12:25 BST, after [obs-accept-step2](/Users/krisbrown/.local/state/ki/agents/observatory/obs-accept-step2.report.md)

**Context:** **New** is a badge on a Beacon signal that wasn't there last time. It can count from the previous observation, which the Observatory already keeps, or from when this browser last opened the Beacon. You said you'd look at the Beacon first.

**Query:** What should **new** be measured from?

**Options:**

a) (recommended, confidence medium - every browser shows the same) Since the previous observation.

b) Since this browser last opened the Beacon.

### BEACON-NARROW - What the Beacon drops on a narrow screen

since 2026-10-19 · from the Summary at 12:25 BST, after [obs-accept-step2](/Users/krisbrown/.local/state/ki/agents/observatory/obs-accept-step2.report.md)

**Context:** Below 760 px each table drops columns, and rank and subject always stay. This also waits on your look at the Beacon.

**Query:** What should the Beacon drop at 760 px?

**Options:**

a) (recommended, confidence medium - the severity glyph and condition chip carry most of the meaning) Drop kind and instrument, and move age into the detail pane.

b) Drop only instrument.

c) Let the planning pass propose a set.

### RUN-EVIDENCE - How a run is tied to its repository

since 2026-10-19 · from the Summary at 12:25 BST, after [obs-accept-step2](/Users/krisbrown/.local/state/ki/agents/observatory/obs-accept-step2.report.md)

**Context:** Step 3's "who is working" view, [KI-OBSERVA-VIS-031](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-031-who-is-working.md), shows which repository each background run is in. The Sessions tab already records each run's repository, and a later record moves run reading onto `ki work status`.

**Query:** Where should the view get each run's repository from?

**Options:**

a) (recommended, confidence medium - it exists today, and the later move can replace it without loss) The Sessions tab's existing record, now.

b) Wait for `ki work status`.

### STEP3-TRIAGE - The two step 3 records still in triage

since 2026-10-19 · from the Summary at 12:25 BST, after [obs-accept-step2](/Users/krisbrown/.local/state/ki/agents/observatory/obs-accept-step2.report.md)

**Context:** Neither is clear enough to build: the extensions switchboard, [KI-OBSERVA-INT-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-INT-003-extensions-switchboard.md), and the read-only tailnet view, [KI-OBSERVA-OPS-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-OPS-004-tailnet-read-only-appearance.md), which waits on Host network.

**Query:** What happens to these two?

**Options:**

a) (recommended, confidence medium - neither can be shaped to Ready on what we know now) Shape the switchboard after the rest of step 3, and leave the tailnet view until Host network is ready.

b) Split the switchboard out now, leaving its adapter for later.

c) Shape the tailnet view's app half now, tested on this Mac only.

### OVERLAY-COMMITTED - Interactive button for saved viewers

since 2026-10-19 · from the Summary at 12:25 BST, after [obs-overlay](/Users/krisbrown/.local/state/ki/agents/observatory/obs-overlay.report.md)

**Context:** Some Archify diagrams have their interactive viewer saved in Git rather than built on this Mac, so a saved viewer can be older than its diagram. [KI-OBSERVA-VIS-042](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-042-diagram-overlay-everywhere.md) can compare dates and flag a stale one.

**Query:** Should the **Interactive** button open saved viewers too?

**Options:**

a) (recommended, confidence medium - the harness already saves twelve) Yes, with a "may be out of date" flag.

b) Yes, without a flag.

c) No, only viewers built on this Mac.

### PUSH-STACKED - Other sessions' commits in ki-principal

since 2026-10-19 · from the Summary at 12:25 BST

**Context:** ki-principal is 12 commits ahead of its remote. This work's work-folder commits are mixed in with commits from State of play, Ways of working and other sibling sessions, so they can't be pushed alone. apps-observatory.local is 1 ahead: `837ee05`, obs-burndown's fix to KI-OBSERVA-APP-042's `blocks` list, this work's only.

**Query:** Should ki-principal be pushed with those commits, and apps-observatory.local with its one?

**Options:**

a) (recommended, confidence medium - all are work-folder and decision documentation commits by sibling sessions in this checkout) You check and push them all, and push apps-observatory.local.

b) Leave them until those threads push their own.

### OBS-PACKAGE-FOLLOWUPS - Two Observatory readers still use the old shape

since 2026-10-19 · from [obs-reader](/Users/krisbrown/.local/state/ki/agents/observatory/obs-reader.report.md)

**Context:** Feedback send writes only into the `## Messages` section of `work.md`, so it refuses to send to any migrated work. Feedback send is switched off for now. The Review queue takes open queries from run reports, not from `queries.md`. Once reports are pruned after their queries are copied into `queries.md`, those queries will drop out of the Review queue.

**Query:** Should these two be captured as Observatory records now?

**Options:**

a) (recommended, confidence high - both break as the migrated works tidy up) Capture two triage records under `ki-next`: feedback writing to `messages.md`, and the Review queue reading `## Open` in `queries.md`.

b) Capture only the Review queue one, since feedback send is still switched off.

c) Leave both until the migration pass has finished.

### BURNDOWN-ACCEPT - The four records awaiting your review

since 2026-10-19 · from [obs-burndown](/Users/krisbrown/.local/state/ki/agents/observatory/obs-burndown.report.md), reviewed by [obs-query-review](/Users/krisbrown/.local/state/ki/agents/observatory/obs-query-review.report.md)

**Context:** Four Observatory records are awaiting review. All of them passed test, typecheck, build, knip and rumdl, and none has been checked in a browser because Chromium is not on this Mac. [KI-OBSERVA-BCN-007](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BCN-007-beacon-raises-stuck-work.md) has the Beacon raise work that is stuck, blocked, on hold past 31 days or waiting for you; a stuck run can be raised twice until KI-OBSERVA-VIS-028 lands. [KI-OBSERVA-BRG-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-003-governed-act-presentation.md) is the declare, confirm and receipt presentation for actions; five parts of the design board are left out because there is no data for them. [KI-OBSERVA-VIS-025](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-025-work-instrument.md) is the Work Instrument, now reading both work-folder shapes. [KI-OBSERVA-VIS-026](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-026-review-queue-work-folders.md) has the Review queue read `+/_WORK/` and show work waiting with you. The blind review found that the code supports all four deliveries, and that the gaps left in KI-OBSERVA-BRG-003 should be accepted explicitly as a scope concession.

**Query:** Which of the four do you accept?

**Options:**

a) (recommended, confidence high - reviewed, the code supports each delivery and you look before accepting) Look at them in the running service and accept all four, with KI-OBSERVA-BRG-003's five missing board parts captured as a triage record.

b) Accept KI-OBSERVA-VIS-025 and KI-OBSERVA-VIS-026 now, and hold KI-OBSERVA-BCN-007 and KI-OBSERVA-BRG-003 until a browser smoke check.

c) Hold all four until Chromium is installed and the smoke check has run.

### BURNDOWN-TRIAGE - Merging and cancelling triage records

since 2026-10-19 · from [obs-burndown](/Users/krisbrown/.local/state/ki/agents/observatory/obs-burndown.report.md), reviewed by [obs-query-review](/Users/krisbrown/.local/state/ki/agents/observatory/obs-query-review.report.md)

**Context:** There are 21 triage records, and the burndown proposed closing 11. Ten would be merges: VIS-040 and INT-004 into [KI-OBSERVA-INT-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-INT-003-extensions-switchboard.md); VIS-035 and VIS-036 into [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md); VIS-037 and VIS-029 into [KI-OBSERVA-VIS-031](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-031-who-is-working.md); VIS-021 into [KI-OBSERVA-VIS-038](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-038-machine-instrument.md); and VIS-039, VIS-032 and VIS-034 into [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md). The eleventh would cancel [KI-OBSERVA-VIS-033](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-033-waiting-for-you.md) as covered by KI-OBSERVA-VIS-026. Nothing has been merged or cancelled. The blind review would confirm only the merge of [KI-OBSERVA-INT-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-INT-004-outbound-live-artifact-adapter.md) into INT-003, the one two-way bridge. It checked each record and found that every other target explicitly excludes the step-4 consolidation, rename or extra scope its source carries, and that KI-OBSERVA-VIS-026 does not deliver VIS-033's Waiting instrument, so the other ten would lose outcomes.

**Query:** Which of these merges and cancellations do you confirm?

**Options:**

a) (recommended, confidence medium - review disagrees, 7 of the 11 are clear overlaps and the rest judgement calls) Confirm all 11, which projects 23 records.

b) Confirm only the merge of INT-004 into INT-003, keeping both directions' acceptance checks, and keep the other ten in triage until KI-OBSERVA-APP-044 decides the restructure.

c) Confirm items 1 to 5, 7 and 8 only: VIS-040, INT-004, VIS-035, VIS-036, VIS-037, VIS-021 and VIS-039.

d) Confirm none for now.

## Parked

None.
