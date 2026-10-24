# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-smoke-record

**🤖 → 👤 Handoff to supervisor · Run report at 01:27 BST**

---

## Done

The red browser smoke check is captured as triage record [KI-OBSERVA-APP-046](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-046-browser-smoke-check-red.md). Both failures come from the check falling behind the product, not from a product fault:

- Dimming: the smoke fixture stamps every reading 2 October 2026. Since 90b8b4f (19 October) the shell marks a pane "stale" once its reading is older than the pane's threshold, and draws stale panes at opacity .85. So every loaded pane counts as dimmed. Four views (sessions, work, review, known-lands) were added on 18 and 19 October without an entry in the check's table of each view's own read.
- Mermaid: since ffb5e50 (18 October), opening a note also reads `/api/feedback/draft`, which the fixture refuses with a 403, and the check tolerates only the image refusal. The inline-handler refusal is most likely the hostile diagram's `onerror`, correctly blocked, but in wording the check's filter does not recognise. When that one started is not confirmed.
- The proposed fix is in the record: a reading time relative to the run's clock plus a deliberate stale check, the four missing reads, and the feedback read and the inline-handler wording allowed in the Mermaid step, with every containment check kept.
- [KI-OBSERVA-VIS-041](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-041-git-view-replaces-repositories.md)'s Review section now links the record in one line: "browser smoke check passes" cannot be met until it lands. VIS-041's status is unchanged.
- Commits, local only: 714e76a reserves the ID, 5209851 captures the record and adds the VIS-041 link. No code changed.
- Checks: roadmap audit FAIL=0 (three older size warnings on other records); Markdown lint clean on both files.

## In Progress

Nothing. Not pushed.

## Queries

None.
