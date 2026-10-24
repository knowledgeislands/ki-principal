# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-burndown

**🤖 → 👤 Handoff to supervisor · Run report at 19:20 BST · last mark 19:20 BST**

---

## Done

- Pruned one of the five done records: [KI-OBSERVA-APP-043](https://github.com/knowledgeislands/apps-observatory.local/blob/63e78b40c4a1c46949909c488d05f227575b37f9/docs/roadmap/KI-OBSERVA-APP-043-shell-polish-without-regrouping.md). Its outcome lives in PDR-KI-OBSERVA-009 and the CHANGELOG, and the open records that linked to it now link to its last revision on `origin/main`.
- Kept the other four done records, because pruning them would break links I am not authorised to fix. [KI-OBSERVA-APP-042](docs/roadmap/KI-OBSERVA-APP-042-design-tokens-and-glyphs.md) is linked by local path from ki-principal `+/_WORK/ki.observatory/design/live-artifacts.md`. [KI-OBSERVA-VIS-023](docs/roadmap/KI-OBSERVA-VIS-023-sessions-and-threads.md) and [KI-OBSERVA-VIS-024](docs/roadmap/KI-OBSERVA-VIS-024-review-queue.md) are linked from ki-principal `+/_WORK/ki.ways-of-working/design/bring-up/observatory.md`. [KI-OBSERVA-BRG-002](docs/roadmap/KI-OBSERVA-BRG-002-capture-feedback.md) is the source of the frozen figure `docs/diagrams/records/capture-feedback.*`, which would be left with no record to point to. I searched every repository under `workspaces/knowledge-islands` and the chezmoi source.
- Commits: `691b938` pins the links, `5c4c68e` is the prune-only commit, and `837ee05` drops the pruned ID from KI-OBSERVA-APP-042's `blocks`. That last fix belonged before the prune; the roadmap audit caught it afterwards.
- Checks: roadmap audit passes (0 failures, 28 warnings, all ITEM-2); `bun run test` and `rumdl` pass.
- Pushing: I pushed nothing. Something else moved `origin/main` up to `5c4c68e` during the run, so it now holds my first two commits and obs-reader's two. Only `837ee05` is still unpushed, on `main` in apps-observatory.local on this Mac.
- Counts, before → after pruning: 35 → 34 records. By status: triage 21, draft 4, ready 1, awaiting review 4, done 5 → 4. By horizon: now 4, next 1, soon 3, hold 1, none 26 → 25.
- Projected counts if you confirm:
  - BURNDOWN-TRIAGE a) closes 11 records, which leaves 23 once they are pruned (10 triage left).
  - Accepting all of BURNDOWN-ACCEPT and pruning those records as well leaves 19.
  - Fixing the peer links and the figure so the four kept done records can be pruned leaves 15.

## In Progress

Nothing. The Observatory service has not been restarted, and no restart is due, because these were roadmap-only changes.

## Queries

### BURNDOWN-ACCEPT

**Context:** Four records are awaiting review. All of them passed test, typecheck, build, knip and rumdl, and none was checked in a browser because Chromium is not installed on this host.

1. [KI-OBSERVA-BCN-007](docs/roadmap/KI-OBSERVA-BCN-007-beacon-raises-stuck-work.md) — the Beacon raises work that is stuck, blocked, on hold past 31 days or waiting for you.
   - Look at: the Beacon's work signals and that Explain opens the Work view.
   - Gaps: a stuck run can be raised twice until KI-OBSERVA-VIS-028 lands, and a repository that cannot be read raises no signal.
2. [KI-OBSERVA-BRG-003](docs/roadmap/KI-OBSERVA-BRG-003-governed-act-presentation.md) — places where the Observatory acts now look different, following declare, confirm and receipt.
   - Look at: Rig and Repositories operations, and the feedback send plan.
   - Gaps: the scope shown is only the plan title, and the new layout has not been seen in a browser.
3. [KI-OBSERVA-VIS-025](docs/roadmap/KI-OBSERVA-VIS-025-work-instrument.md) — the Work Instrument shows five views and the latest report, reading both work-folder shapes.
   - Look at: the Work tab against the territory.
   - Gaps: views and review count are derived here until `ki/work-status/v2` ships; feedback sending and queries do not yet use `messages.md` and `queries.md`.
4. [KI-OBSERVA-VIS-026](docs/roadmap/KI-OBSERVA-VIS-026-review-queue-work-folders.md) — the Review queue reads `+/_WORK/` and `+/_WORK_REVIEW/` and shows work waiting with you.
   - Look at: the Review queue's groups and its links to the Work view.
   - Gaps: the new row kinds raise no Beacon signal of their own, and `+/_THREADS/` is still read until phase 5.

**Query:** Which of the four do you accept?

**Options:**
a) (recommended, confidence medium - each has passing checks and stated gaps, but none has been checked in a browser) Accept all four after looking at them in the running service.
b) Accept KI-OBSERVA-VIS-025 and KI-OBSERVA-VIS-026 now, and hold KI-OBSERVA-BCN-007 and KI-OBSERVA-BRG-003 until a browser smoke run.
c) Hold all four until Chromium is installed and the smoke check has run.

### BURNDOWN-TRIAGE

**Context:** There are 21 triage records. I propose closing 11 of them: ten merges and one cancellation.

1. KI-OBSERVA-VIS-040 Extensions instrument: merge into KI-OBSERVA-INT-003. The switchboard is already the Extensions surface with its switches.
2. KI-OBSERVA-INT-004 Outbound adapter: merge into KI-OBSERVA-INT-003. EXT-MODEL is one two-way bridge, so one record keeps the contract together.
3. KI-OBSERVA-VIS-035 Trade routes as layer: merge into KI-OBSERVA-VIS-030. It is a layer on that chart.
4. KI-OBSERVA-VIS-036 Activity split: merge into KI-OBSERVA-VIS-030. Its time window becomes the chart's time control.
5. KI-OBSERVA-VIS-037 Workers instrument: merge into KI-OBSERVA-VIS-031. Both answer who is working; whether it gets its own tab is for KI-OBSERVA-APP-044 to decide.
6. KI-OBSERVA-VIS-029 Sessions from every host: merge into KI-OBSERVA-VIS-031. Marking each run's host extends who is working.
7. KI-OBSERVA-VIS-021 Explain tool storage: merge into KI-OBSERVA-VIS-038. Where tools store things is machine state.
8. KI-OBSERVA-VIS-039 Decisions as Council: merge into KI-OBSERVA-APP-044. It is only a rename, best settled with the restructure.
9. KI-OBSERVA-VIS-032 Library instrument: merge into KI-OBSERVA-APP-044. The decision is about folding two tabs together; the readers already exist.
10. KI-OBSERVA-VIS-034 Streams instrument: merge into KI-OBSERVA-APP-044. Same reason: folding Roadmap and Work together is the decision.
11. KI-OBSERVA-VIS-033 Waiting for you: cancel as superseded by KI-OBSERVA-VIS-026, which already puts work waiting with you into the Review queue.

The ten I would keep are KI-OBSERVA-APP-044, APP-045, BRG-004, INT-003, OPS-003, OPS-004, VIS-022, VIS-038, VIS-041 and VIS-042.

**Query:** Which of these cancellations and merges do you confirm?

**Options:**
a) (recommended, confidence medium - items 1–5, 7 and 8 are clear overlaps; 6, 9, 10 and 11 are judgement calls) Confirm all 11.
b) Confirm only the clear overlaps, items 1–5, 7 and 8. That closes 7 and projects 27 records.
c) Confirm none, and keep the step-4 consolidations as triage until KI-OBSERVA-APP-044 is decided.
