# obs-query-review - Blind review of the burndown queries

This is a read-only blind review run for KI > Model > Observatory (`ki.observatory`), under the QUERY-REVIEW rule of the `ki-coordination` standard. Two queries are about to go to Kris. For each one, check what you can directly in apps-observatory.local (the records under `docs/roadmap/`, the code, and `git log`). Then give your own recommended option with a confidence of `high`, `medium` or `low` and a one-line reason. You may propose a course that is not listed. Change nothing and commit nothing.

## BURNDOWN-ACCEPT

**Context:** Four records in apps-observatory.local are awaiting review. All of them passed test, typecheck, build, knip and rumdl, and none was checked in a browser because Chromium is not installed on this host.

1. [KI-OBSERVA-BCN-007](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BCN-007-beacon-raises-stuck-work.md): the Beacon raises work that is stuck, blocked, on hold past 31 days or waiting for the owner. Known gaps: a stuck run can be raised twice until KI-OBSERVA-VIS-028 lands, and a repository that cannot be read raises no signal.
2. [KI-OBSERVA-BRG-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-003-governed-act-presentation.md): places where the Observatory acts follow declare, confirm and receipt. Known gaps: the scope shown is only the plan title, and five board parts have no data field.
3. [KI-OBSERVA-VIS-025](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-025-work-instrument.md): the Work Instrument shows five views and reads both work-folder shapes. Known gaps: views are derived locally until `ki/work-status/v2` ships, and feedback and queries do not yet use `messages.md` and `queries.md`.
4. [KI-OBSERVA-VIS-026](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-026-review-queue-work-folders.md): the Review queue reads `+/_WORK/` and `+/_WORK_REVIEW/` and shows work waiting with the owner. Known gaps: the new row kinds raise no Beacon signal, and `+/_THREADS/` is still read until phase 5.

**Query:** Which of the four should Kris accept?

**Options:**

a) Accept all four after Kris looks at them in the running service.

b) Accept KI-OBSERVA-VIS-025 and KI-OBSERVA-VIS-026 now, and hold KI-OBSERVA-BCN-007 and KI-OBSERVA-BRG-003 until a browser smoke run.

c) Hold all four until Chromium is installed and the smoke check has run.

## BURNDOWN-TRIAGE

**Context:** There are 21 triage records. The proposal is to close 11 of them: ten merges and one cancellation.

1. VIS-040 into INT-003, because the switchboard is the Extensions surface.
2. INT-004 into INT-003, because one two-way bridge keeps the contract together.
3. VIS-035 into VIS-030, as a layer on that chart.
4. VIS-036 into VIS-030, its time window becoming the chart's time control.
5. VIS-037 into VIS-031, because both answer who is working.
6. VIS-029 into VIS-031, because marking each run's host extends who is working; VIS-029 is held until Host network unit 4 opens.
7. VIS-021 into VIS-038, because tool storage is machine state.
8. VIS-039 into APP-044, as a rename best settled with the restructure.
9. VIS-032 into APP-044, because the decision is about folding two tabs.
10. VIS-034 into APP-044, because folding Roadmap and Work is the decision.
11. Cancel VIS-033, as superseded by VIS-026.

All records are `KI-OBSERVA-*` in `docs/roadmap/`. Check each pair's scope and dependencies directly.

**Query:** Which of these cancellations and merges should Kris confirm?

**Options:**

a) Confirm all 11.

b) Confirm only items 1-5, 7 and 8.

c) Confirm none, and keep the step-4 consolidations in triage until KI-OBSERVA-APP-044 is decided.

## Report

Write a short report in owner-report shape. For each query, Done gives your recommended option, your confidence and a one-line reason. For BURNDOWN-TRIAGE, add one line on each numbered item you would not confirm. Queries: `No outstanding queries` unless something blocks the review.
