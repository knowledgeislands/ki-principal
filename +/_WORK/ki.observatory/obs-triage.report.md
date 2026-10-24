# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-triage

**🤖 → 👤 Handoff to supervisor · Run report at 23:32 BST · last mark 22:50 BST**

---

## Done

- Triage count before: 19 records in `triage`. That is the 18 listed when the pass began plus the Workers record [KI-OBSERVA-VIS-045](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-045-workers-instrument.md). KI-OBSERVA-VIS-031 was done, and was pruned at 23:21 in `af4d39d`.
- Shaping committed in `caa4d63` (local, unpushed), covering 18 records by explicit path. Each now has a `size`. Each also gained a `## Shaping` section where it lacked one, giving the approach, acceptance, files touched, dependencies and the conditions for promotion. Two records are linked by build order: [KI-OBSERVA-BRG-006](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-006-feedback-to-messages-file.md) now blocks [KI-OBSERVA-BRG-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-004-turn-feedback-sending-on.md), because a feedback send to a five-file package needs the `messages.md` writer first. VIS-045 was already fully shaped and was left alone. No status, horizon, merge, cancellation or deletion was made (PUSH-ALL).
- Facts the shaping found:
  - The Review queue already lists work waiting on you (KI-OBSERVA-VIS-026), so VIS-033 now only renames the queue.
  - Rig already declares each job's calendar in `schedule-calendar`, which answers one of VIS-022's open questions.
  - The plan contract has no scope, inputs or way-in field, so BRG-005 proposes three optional fields that existing plans and receipts stay valid without.
- `ki repo audit`: passes, FAIL=0. The 10 missing-`size` warnings on triage records are gone. The remaining warnings are template, CI and hook drift, plus missing `size` on the non-triage records VIS-027, VIS-028 and VIS-030, which this pass left alone.

### Grouped triage table

Suggested order runs top to bottom within each group.

| Record | Title | Group | Move | Reason |
| --- | --- | --- | --- | --- |
| [KI-OBSERVA-VIS-043](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-043-review-queue-reads-queries.md) | Review queue reads queries | A. Work-package and territory fixes | Ready · now | Size `s`, reuses the existing package reader, no design gate; open queries in `queries.md` reach the queue |
| [KI-OBSERVA-BRG-006](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-006-feedback-to-messages-file.md) | Feedback to messages file | A. Work-package and territory fixes | Ready · now | Size `s`; sending stays off, so it is safe now, and it unblocks BRG-004 |
| [KI-OBSERVA-APP-045](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-045-name-unregistered-territory-member.md) | Name unregistered territory member | A. Work-package and territory fixes | Ready · now | Size `s`; Kris already took it (TERRITORY-REGISTER b)); a strict match is the fallback until tools-ki reports the member |
| [KI-OBSERVA-BRG-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-004-turn-feedback-sending-on.md) | Turn feedback sending on | A. Work-package and territory fixes | Hold | Waits for ki-agentic-harness to admit a `feedback/` work-folder kind (KI-HARNESS-GOV-219, still in triage) and for BRG-006 |
| [KI-OBSERVA-VIS-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-044-commit-authors-in-tables.md) | Commit authors in tables | B. Step 3 finish | Ready · now | Size `s`; part of step 3 (COUNTS-TABLES, COMMIT-AUTHORS a)); no contract change, with its limits stated on screen |
| [KI-OBSERVA-BRG-005](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-005-act-board-missing-parts.md) | Act board missing parts | B. Step 3 finish | Ready · now | Size `m`; step 3 Act work (GET-MOVING); counts are settled, and three optional contract fields await your go |
| [KI-OBSERVA-INT-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-INT-003-extensions-switchboard.md) | Two-way live-artifact adapter | B. Step 3 finish | Hold | STEP3-LATER: shaped once the rest of step 3 lands; when released, split per phase (size `l`) |
| [KI-OBSERVA-OPS-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-OPS-004-tailnet-read-only-appearance.md) | Tailnet read-only appearance | B. Step 3 finish | Hold | Waits for unit 4 of the Host network Project (STEP3-LATER) |
| [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) | Instrument restructure decision | C. Step 4 restructure | Ready · next | A `decide` record, size `m`, and the gate to every step 4 consolidation; it opens once step 3's chart, Act board parts and commit authors land |
| [KI-OBSERVA-VIS-033](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-033-waiting-for-you.md) | Waiting for you | C. Step 4 restructure | Merge → KI-OBSERVA-APP-044 | VIS-026 already lists work waiting on you, so only a rename is left, like Council |
| [KI-OBSERVA-VIS-034](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-034-streams-instrument.md) | Streams instrument | C. Step 4 restructure | Hold | Waits for APP-044's decision, then your approval of this consolidation and of where Work goes |
| [KI-OBSERVA-VIS-032](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-032-library-instrument.md) | Library instrument | C. Step 4 restructure | Hold | Waits for APP-044's decision, then your approval of this consolidation |
| [KI-OBSERVA-VIS-045](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-045-workers-instrument.md) | Workers instrument | C. Step 4 restructure | Hold | Waits for APP-044's decision, then your approval (WORKERS-HOME) |
| [KI-OBSERVA-VIS-038](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-038-machine-instrument.md) | Machine instrument | C. Step 4 restructure | Hold | Consolidation waits for APP-044; tool storage waits for a decision on who owns storage declarations; split when released |
| [KI-OBSERVA-VIS-041](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-041-git-view-replaces-repositories.md) | Git view replaces Repositories | D. Git and diagrams | Ready · next | Decided by EXT-MODEL; not a consolidation; tokens have landed; size `l`, which planning may split |
| [KI-OBSERVA-VIS-042](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-042-diagram-overlay-everywhere.md) | Diagram overlay everywhere | D. Git and diagrams | Hold | Waits for ki-agentic-harness's viewer receipt contract (KI-HARNESS-GOV-224, still in triage) |
| [KI-OBSERVA-VIS-022](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-022-judge-overdue-against-each-job-schedule.md) | Overdue against job schedules | E. Machine, hosts and serving | Ready · next | Size `m`; Rig already declares calendars; stops false overdue signals at weekends; a grace period is still to be set |
| [KI-OBSERVA-OPS-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-OPS-003-observatory-serving-location.md) | Observatory serving location | E. Machine, hosts and serving | Ready · later (`soon`) | You said "not a now thing"; an `investigate` record with a small build-identifier half here |
| [KI-OBSERVA-VIS-029](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-029-sessions-from-every-host.md) | Sessions from every host | E. Machine, hosts and serving | Hold | Waits for unit 4 of the Host network Project; kept apart from Workers, which has no network dependency |

Totals: 5 now, 3 next, 1 later, 1 merge, 9 hold, 0 cancel.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Agent work: obs-link-pins is held until this run finishes. It will pin the links to pruned records. That now includes KI-OBSERVA-VIS-031, which `af4d39d` pruned after the obs-link-pins brief was written, and which is still linked from APP-044, VIS-044, VIS-045 and the in-progress VIS-030. This pass left every link alone so the two runs do not collide.
- Verification limitation: `ki repo roadmap promote` earlier refused on a `size` field (state.md, step 7). Every triage record now carries `size`, so horizons may have to be set by hand when you move them.
- Retained material: `caa4d63` is local; Kris pushes (PUSH-KRIS). The commit changes only roadmap records, so no service restart is due.

## Queries

### TRIAGE-NOW - Five records to build straight away

**Context:** These five records are small, shaped and covered by authority you have already given: [KI-OBSERVA-VIS-043](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-043-review-queue-reads-queries.md), [KI-OBSERVA-BRG-006](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-006-feedback-to-messages-file.md), [KI-OBSERVA-APP-045](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-045-name-unregistered-territory-member.md), [KI-OBSERVA-VIS-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-044-commit-authors-in-tables.md) and [KI-OBSERVA-BRG-005](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-005-act-board-missing-parts.md). Four are size `s`, need no design step, and each fixes something visible: open queries missing from the queue, feedback refused by migrated packages, an unexplained territory failure, and authors missing from the tables. BRG-005 is size `m` and finishes step 3's Act board, but it adds three optional fields to the plan and receipt contracts (scope, inputs with withheld reasons, and the way a request came in). The way-in field matters only once the tailnet view exists, so it could instead wait with KI-OBSERVA-OPS-004. APP-045 reads `ki`'s error text through a strict match until tools-ki offers a machine-readable failure.
**Query:** Should these five go to Ready at `now`, to be built one at a time and committed locally?
**Options:** a) (recommended, confidence high - each is shaped with acceptance and files touched, and together they clear the small fixes and finish step 3's buildable work) all five at `now`, approving BRG-005's three contract fields; b) all five at `now`, but BRG-005 without the way-in field, which waits with OPS-004; c) only the four `s` records at `now`, with BRG-005 at `next`.

### TRIAGE-NEXT-LATER - Three records next, one later

**Context:** [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) is the decision every step 4 consolidation waits on. Under DESIGN-RESTRUCTURE a) it opens once steps 1 to 3 have shipped. The shaping proposes reading "shipped" as the Known Lands chart, the Act board's parts and commit authors having landed, without waiting for the switchboard and the tailnet view that STEP3-LATER deferred. [KI-OBSERVA-VIS-041](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-041-git-view-replaces-repositories.md) was decided by EXT-MODEL. It needs no consolidation approval, its tokens have landed, and it is size `l`. [KI-OBSERVA-VIS-022](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-022-judge-overdue-against-each-job-schedule.md) stops false overdue signals for jobs that skip weekends; Rig already declares their calendars, but a grace period is still to be set. [KI-OBSERVA-OPS-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-OPS-003-observatory-serving-location.md) is what you called "not a now thing". It is an investigation with a small reload hint that could be built here.
**Query:** Should APP-044, VIS-041 and VIS-022 go to Ready at `next`, OPS-003 be adopted at `soon`, and step 3 be read as shipped once the chart, the Act board's parts and commit authors land?
**Options:** a) (recommended, confidence medium - this keeps the queue full behind the `now` list without starting a consolidation early, but how you read "shipped" is your call) as asked; b) the same, but step 3 counts as shipped only once the switchboard and the tailnet view land too, which holds APP-044 behind the Host network Project; c) VIS-041 at `now` with the `now` list, the rest as in a).

### TRIAGE-MERGE - Fold Waiting for you into the restructure decision

**Context:** The Review queue already lists work waiting on you, from the same reading as the Work view, under KI-OBSERVA-VIS-026. So all that is left of [KI-OBSERVA-VIS-033](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-033-waiting-for-you.md) is renaming the queue to Waiting for you under the Attend job, with `?view=review` redirected. That is the same kind of step as the Council rename that [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) already carries. The burndown proposed cancelling VIS-033 as superseded, but that would lose the rename.
**Query:** Should VIS-033 be merged into APP-044 as a second rename step, carrying its acceptance, and VIS-033 closed as `merged`?
**Options:** a) (recommended, confidence medium - it keeps the rename and its acceptance while removing a record whose absorbing work is already done) merge into APP-044; b) keep VIS-033 as its own consolidation, on hold behind APP-044; c) cancel it as superseded by KI-OBSERVA-VIS-026.

### TRIAGE-HOLD - Nine records held, each with its condition

**Context:** Each of these records has a named wait, and holding them clears the triage list without starting anything:

[KI-OBSERVA-BRG-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-004-turn-feedback-sending-on.md) waits for ki-agentic-harness to admit a `feedback/` work-folder kind.

[KI-OBSERVA-INT-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-INT-003-extensions-switchboard.md) waits for the rest of step 3, under STEP3-LATER.

[KI-OBSERVA-OPS-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-OPS-004-tailnet-read-only-appearance.md) and [KI-OBSERVA-VIS-029](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-029-sessions-from-every-host.md) wait for unit 4 of the Host network Project.

[KI-OBSERVA-VIS-034](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-034-streams-instrument.md), [KI-OBSERVA-VIS-032](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-032-library-instrument.md), [KI-OBSERVA-VIS-045](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-045-workers-instrument.md) and [KI-OBSERVA-VIS-038](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-038-machine-instrument.md) wait for APP-044's decision and then your approval of each consolidation. VIS-038's tool-storage phase also waits for a decision on who owns storage declarations.

[KI-OBSERVA-VIS-042](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-042-diagram-overlay-everywhere.md) waits for ki-agentic-harness's viewer receipt contract.

The burndown's alternative was to merge VIS-032 and VIS-034 into APP-044, and VIS-029 into the Workers phase. That would make APP-044 an `l` or `xl` record carrying several separate approvals, and would tie Workers to the Host network Project. INT-003 and VIS-038 are size `l` with phases behind different gates, so they should be split per phase when released.
**Query:** Should these nine be adopted at `hold` with the conditions above, rather than merged?
**Options:** a) (recommended, confidence medium - holding keeps each consolidation's own approval and acceptance, and leaves APP-044 a decision-sized record) hold all nine as listed; b) hold them, but merge VIS-032 and VIS-034 into APP-044 as the burndown proposed; c) leave them in triage until APP-044 is decided.
