# [KI > Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/work.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/work.md) › obs-restart

**🤖 → 👤 Handoff to supervisor · Run report at 19:25 BST**

---

## Done

- The Observatory is up at <http://127.0.0.1:1675/>, serving `main` at `837ee05`, which includes [KI-OBSERVA-VIS-025 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/02cb729bf7a8c2fc9305ef4c597a19acd8e968e4/docs/roadmap/KI-OBSERVA-VIS-025-work-instrument.md) (`a9fb2ed`, `53a40b0`).
- It runs from source through the launchd agent `uk.me.kris.rig.observatory` (`bun run src/main.ts` in `apps/site`), so no rebuild was needed; ran `launchctl kickstart -k "gui/$(id -u)/uk.me.kris.rig.observatory"`.
- Checks: the root answers 200 and the service is running; `/api/work` lists `knowledgeislands/ki-principal` with 12 works, matching its 12 work folders (`ki`, `ki.observatory`, `ki.regular` and the rest), plus 5 in review.
- No source changed, nothing committed or pushed.

## In Progress

None.

## Queries

No outstanding queries
