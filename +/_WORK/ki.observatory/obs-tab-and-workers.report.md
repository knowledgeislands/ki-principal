# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-tab-and-workers

**🤖 → 👤 Handoff to supervisor · Run report at 22:50 BST · last mark 22:50 BST**

---

## Done

1. Known Lands tab (TAB-SCROLL): the tab is now on the bar as `known lands`. At 1,440 px the bar scrolls with its existing fades. Only the wide-window fit check and its acceptance wording changed. The tab is in `degraded.test.ts`, and the README and operator guide are updated. [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) stays in progress. Commit 6b2096c; gate and `ki repo audit` pass.
2. Act board counts (BRG-005-COUNTS a): [KI-OBSERVA-BRG-005](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-005-act-board-missing-parts.md) is shaped and stays in triage. Confirm and receipt each count one operation per request, the receipt shows its outcome, and batch operations are left for a later record. Commit 09762d9; gate and audit pass.
3. Worker column (VIS-031-TABLES a): built.
   - Repositories and Roadmap have a `workers` column of running agent runs, each count opening Sessions. Roadmap labels its counts `repo-level` because runs match by repository only.
   - Sessions has a `touches` column that opens Repositories.
   - Every new column is declared to drop at 760 px.
   - [KI-OBSERVA-VIS-031 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/24c4bd8bfb1956c5ee9e0e2beef846bd06e298a5/docs/roadmap/KI-OBSERVA-VIS-031-who-is-working.md) was planned to Ready (horizon `now`) and is now awaiting review.
   - Commit 52f18bf; gate and audit pass at the baseline (PASS=16 WARN=4 FAIL=0).
4. Service: restarted. <http://127.0.0.1:1675/> answers 200 and serves all sixteen tabs, `known-lands` among them.

## In Progress

Nothing. The three commits are local on `main` in apps-observatory.local and have not been pushed.

## Queries

**COMMIT-AUTHORS**

**Context:** Under DESIGN-WORKERS-CHIP a), the tables were to show both agent runs and commit authors. This run built agent runs only, from the run evidence RUN-EVIDENCE names. The record notes the gap under Discussion, Commit authors.

**Query:** Should the Repositories and Roadmap tables also show commit authors from Activity?

**Options:** a) (recommended, confidence medium - it needs a separate read of Activity and its own wording for the time window) Open a triage record for commit authors in the tables and keep [KI-OBSERVA-VIS-031 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/24c4bd8bfb1956c5ee9e0e2beef846bd06e298a5/docs/roadmap/KI-OBSERVA-VIS-031-who-is-working.md) to runs. b) Reopen [KI-OBSERVA-VIS-031 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/24c4bd8bfb1956c5ee9e0e2beef846bd06e298a5/docs/roadmap/KI-OBSERVA-VIS-031-who-is-working.md) and add commit authors there before it is accepted. c) Drop commit authors from the tables and leave them to the Workers phase.

**WORKERS-JOIN**

**Context:** VIS-031's Shaping planned to join workers to rows at the backend. The build joins them in the view instead, from the same `/api/sessions` answer the workers chip reads, so no contract changes. When the run read is partial (`runsReason` is set), the whole column shows `not observed`, as the chip does.

**Query:** Do you accept the join in the view and the all-or-nothing `not observed`?

**Options:** a) (recommended, confidence high - no contract change, and it matches the chip) Accept both as built. b) Move the join to the backend with a worker field in each contract. c) Show partial counts with a warning when some run folders could not be read.
