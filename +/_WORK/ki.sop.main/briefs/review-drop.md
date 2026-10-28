# review-drop: blind review of two questions

Authority: read only. Change, commit and send nothing. Do not read any `queries.md`, `decisions.md` or `*.report.md` file anywhere. You may read work-package `state.md`, `messages.md`, Git logs and roadmap records in the Knowledge Islands repositories under `/Users/krisbrown/workspaces/` to check facts.

For each question, choose the option you would recommend, give a confidence (high, medium, low) and a one-line reason, and name any evidence you checked.

## Q1 - dropping overtaken queries

Context: work packages under `ki-principal/+/_WORK/` carry parked queries for the owner. A census found 15 whose subject is gone, each evidenced by a commit that accepted or pruned the record concerned or deleted the folder: ki.sop.main 8 (ACCEPT-KI-WEBSITE-SITE-044, ACCEPT-KI-PRINCIPAL-OPS-014, ACCEPT-KI-PRINCIPAL-MOD-009, ACCEPT-KI-TOOL-RIG-CORE-062, ACCEPT-OBSERVATORY, CLI006-CONFIRM, CLI006-READY, SPECS-FOLDER); ki.prj.estate-factorisation 4 (HOST-GUARDS: KI-TOOL-TECHNE-CLI-006 pruned; STORE-REPAIR: KI-TOOL-KI-CLI-126 pruned; TRIAGE-OWNERS: KI-TOOL-KI-CLI-131/134/135 pruned; DOCK: KI-TOOL-RIG-CORE-042 pruned); ki.prj.agent-host 1 (CLI006-PLAN); ki.prj.chezmoi 1 (WARP-HANDLER, settled by a later SOL-SETTLED message); ki.prj.baseline-rollout 1 (VA-AREA-TITLES: VA-PRINCIPAL-GOV-007 accepted and pruned). Five more in ki.prj.mac-studio-setup rest only on the state of host sol (RIG-TRIAGE, SOL-SOURCES, SOL-HNR-HARNESS, SOL-KI-CONFIG-DRIFT, FW-LIVE). Git keeps the deleted text.

Question: how should these be cleared?

Options (unranked):

- Each package tidy drops the 15 commit-proven queries with a decisions-log line citing the commit, and the five host-evidenced ones go to the owner as a batch.
- All 20 go to the owner one by one before any drop.
- All 20 are dropped on the census evidence.

## Q2 - old orphaned repositories

Context: a parked query in ki.prj.mac-studio-setup concerns old orphaned repositories that were to be kept during the Mac Studio migration. A census found no checkout of them under `~/workspaces` and no bundle in OneDrive. If they lived only on a retired disk or host, the last copies may be gone.

Question: what should happen to that query?

Options (unranked):

- The owner names the location or confirms they are gone, and ki.prj.mac-studio-setup records the answer before its query closes.
- Treat them as lost and close the query.

Report to `/Users/krisbrown/.local/state/ki/agents/ki-sop-main/review-drop.report.md`: per question, the chosen option quoted, confidence, reason and evidence. Plain British English, no em-dashes.
