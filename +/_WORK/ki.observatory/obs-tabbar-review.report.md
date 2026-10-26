# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-tabbar-review

**🤖 → 👤 Handoff to supervisor · Run report at 21:41 BST · last mark 19:02 BST**

---

## Done

Recommend **b), confidence high**: add Known Lands and allow the existing scrolling bar at 1,440 px; this preserves full titles and separate destinations using behaviour already specified by [PDR-KI-OBSERVA-002](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/decisions/PDR-KI-OBSERVA-002-observatory-design-language.md), without anticipating Kris’s designs.

Static width check confirmed: 1,341 px today; 1,454 px with the saved `known lands` title. Renaming `review queue` to `review` leaves 1,412 px against 1,392 px available; option a’s 1,356 px requires also calling the new tab `map`.

Evidence checked: [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md), [layout tests](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/apps/site/src/layout.test.ts:318), [shell tests](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/apps/site/src/shell.test.ts:780), registry and all fifteen titles, saved tab and registration patch, and [Kris’s decisions](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/decisions.md), including all five requested decisions. Shell coverage includes edge fades, active/focused-tab visibility and wheel scrolling; tests were inspected, not run.

Change only the wide-window fit assertion and corresponding acceptance wording after Kris’s agreement; retain overflow containment, full-title and focus checks, and the 760 px table rules unchanged. No repository changes or commits.

## In Progress

Nothing running.

## Queries

No outstanding queries

### 🤖 → 👤 Handoff to supervisor · since 21:41 BST

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [handoff] TAB-ROOM review complete · supervisor · since 21:41 BST
