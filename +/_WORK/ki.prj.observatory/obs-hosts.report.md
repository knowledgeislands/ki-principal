# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-hosts

**🤖 → 👤 Handoff to supervisor · Run report at 20:57 BST · last mark 20:20 BST**

---

## Done

- I captured [KI-OBSERVA-VIS-029 Sessions from every host](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-029-sessions-from-every-host.md) as an unadopted triage record. Its path is `/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-029-sessions-from-every-host.md`. Its goal is to show runs from every host in one Sessions view.
- The record links to [KI-OBSERVA-VIS-023](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-023-sessions-and-threads.md) (Sessions) and to unit 4 of the Project, the tailnet name. It states the dependency: unit 4 waits for the [Host network](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/host-network.md) thread to open. It also notes that the record overlaps [KI-OBSERVA-VIS-028](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-028-retire-sessions-readers.md); following PUSH-ALL, it does not choose between them.
- Commits: `b4f78f3` reserves the identifier in the ledger, and `19b0fa7` captures the record. Both were committed by explicit path.
- Checks: pre-commit lint passed. The repository audit fails only on a title in KI-OBSERVA-VIS-022 that was already there; nothing in this run caused it. Fetch passed, and both commits were pushed fast-forward to `origin/main`. No other commit was stacked with them.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- KI-OBSERVA-VIS-029 stays in triage until someone adopts it. The natural moment is when the Host network thread opens.
- The audit failure on the KI-OBSERVA-VIS-022 title needs a separate fix: the title must be at most four words.
- No service restart is due, because this run changed only a roadmap record.

## Queries

None.
