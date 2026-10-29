---
id: ki.prj.ways-of-working
state: handoff-to-supervisor
since: 2026-10-29T22:21:00Z
received: 2026-10-29T15:38:09Z
beat: null
mark: 2026-10-29T16:18:42Z
method_read: 07b9333a
---

# ki.prj.ways-of-working state

## Now

- On terra, 29 October evening. Main thread: the work state machine (WORK-STATE-MACHINE and the decisions after it, all in decisions.md): Start (wp) -open-> Bootstrap -ready-> Working (entry choice: pick up / refine; cycle inform, receive, direct, receive; End (work) by conclude) -stop, drain, portable-> At rest (holding, waiting, moving) -resume-> Bootstrap, or -finish-> Finished. Roles: supervisor, worker, orchestrator, each AI or human (ROLES-ORCHESTRATOR, ROLES-EITHER).
- Design: [work-state-machine.md](design/work-state-machine.md) with Archify views; Mermaid sketch [work-state-machine.mmd](design/work-state-machine.mmd) holds the agreed shape. wow-sm-polish is applying WORKING-EXIT and beautifying.
- Aside, routed: DIAGRAM-TOOLS to ki.sop.main for the `ki-diagrams` and `ki-authoring` owners; DIAGRAM-FEEDBACK to ki.prj.observatory.
- Kris took every recommended option earlier today (RECOMMENDED-ALL): HOST-SYNC design, FINISH-LINE, CROSS-MACHINE-SOURCE, PUBLIC-REPORT-AUDIENCE.

## Next steps

1. Receive wow-sm-polish; settle the design note's Decisions for Kris and ARC-CONDITIONS, blind-reviewing medium and low ones first; decide MACHINE-HOME.
2. Roll the machine out as message lines: Work Process note (Enactment), `ki-work-package` (states, transitions, conditions, WORK-FOLDER-PURPOSE layout), `ki-coordination` (orchestrator behaviour, DRAIN-MEANS portability on stop), tools-ki (`ki agent` reports into `reports/`, `ki work status` values).
3. Relaunch wow-host-sync-design and wow-finish-line from briefs/; then HOST-SYNC rollout lines to personal.reg.rig-terra and personal.reg.rig-sol.
4. From the finish-line plan: MOD-011 reconciliation from published sources; hand-offs through KI State of play; move or prune the 86 root reports (FOLDER-MIGRATE).
5. PUBLIC-REPORT-AUDIENCE private review run, changing no access or history.
6. Dispose of the six messages.md lines (HOST-SYNC-REVIEW to the design run; five confirm parked routes).
7. Before moving to sol: stop with the portability checks; prune spent briefs; remove stranded run worktrees (wow-sync-2).

## Held

- Preserve the original model candidate, Tools retained refs and publication recovery evidence. Reconcile published sources without overwriting unresolved overlaps or replaying stale trees.
- Host-sync and other unchosen designs await their existing decision stages; no executor, schedule or automatic takeover is selected.
- HNR remains excluded. Observatory appearance belongs to its own work.
- No release, deployment, install, credential/provider operation, confidential publication, force/reset/stash or hook bypass is authorised here.
