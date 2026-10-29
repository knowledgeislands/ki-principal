# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-tokens

**🤖 → 👤 Handoff to supervisor · Run report at 08:01 BST · last mark 20:20 BST**

---

## Done

[KI-OBSERVA-APP-042](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-042-design-tokens-and-glyphs.md) "Design tokens and glyphs" is built and is now Awaiting review. The Observatory takes its colours and font stacks from `ki-design` (pinned at `c56d394`), and none of its colours is derived locally any more. The colours on screen are the same as before, hex for hex.

Each of the fifteen tabs now has a line glyph before its title. Each Beacon repository heading and matrix column has one too: an island for a repository, the machine glyph for this machine, and an archipelago for a signal across several repositories. The Work tab's banner glyphs are unchanged, as decided. Every tab, route and `?view=` address works as before.

The decision is recorded in the new [PDR-KI-OBSERVA-008](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/decisions/PDR-KI-OBSERVA-008-line-glyphs-beside-tabs-and-subjects.md). PDR-KI-OBSERVA-002 is updated in place, and the MIT notice is added.

Commits `881d7d9` (approval, record set to Ready) and `9776345` (delivery), both pushed fast-forward to origin.

Checks: tests pass, with the contrast, density and width targets unchanged; typecheck passes; the browser check was skipped because Playwright Chromium is not installed; the repository audit shows no new finding (its one failure is an existing title-length issue on KI-OBSERVA-VIS-022).

## In Progress

A service restart is due so the running Observatory shows this delivery. This run did not do it, because a background run never restarts the service.

## Queries

**Context:** No contract the Observatory reads says what a repository is, so I drew the archipelago glyph for a signal that spans several repositories. Every single repository is drawn as an island. **Query:** Keep the archipelago glyph for signals that span several repositories? **Options:** a) (recommended, confidence medium - it is the glyph ki-design gives for a group of islands) keep it. b) Draw the island glyph there too. c) Draw no glyph on spanning signals.
