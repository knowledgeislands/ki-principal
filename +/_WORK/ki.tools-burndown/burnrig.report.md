# [Foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Tools burndown](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/tools-burndown.md) › burnrig

**🤖 → 👤 Handoff to supervisor · Run report at 00:23 BST · last mark 23:45 BST**

---

## Done

- [KI-MCP-GIT-FND-006 (pruned)](https://github.com/knowledgeislands/mcp-git-audit/blob/bd66c937d228fe19377259245f383fce22422a2e/docs/roadmap/KI-MCP-GIT-FND-006-ground-roots-in-workspaces.md) Ground roots in workspaces: adopted, planned to Ready (`5e946c4`) and delivered to Awaiting review (`6a48d6e`); an unset allow-list now defaults to `~/workspaces`, and examples and guides follow that layout. Decided under HIGH-APPLY, 20 October, and recorded in the record: a missing default root behaves like any missing root, giving empty scans with no startup failure and no fallback to `~`. Gate: tests 247 of 247 passed, coverage 100%, smoke passed, audit had no failures.
- Small audit finding CI-1, fixed without a record in mcp-git-audit (`6d843bd`) and tools-git-almanac (`36a30ec`): the ki pin moved from `ci.yml` to `.github/ki-version`, still at v0.11.3, with the house `update-ki-pin.yml` receiver copied from ki-principal. This receiver does nothing until the release App and its secret are installed. Audit afterwards had no failures. The two remaining warnings were left: `.rumdl.toml` drift is the unrelated conform rewrite the coordinator flagged, and the Claude Desktop binding is machine configuration.
- tools-git-almanac has no open records.
- tools-rig: nothing changed, following the coordinator's LANE-FIX of 00:14 BST (the lane belongs to ki.mac-studio-setup). Before that line arrived I had only read records there.
- I pushed nothing. The local refs show that another session has already pushed the two [KI-MCP-GIT-FND-006 (pruned)](https://github.com/knowledgeislands/mcp-git-audit/blob/bd66c937d228fe19377259245f383fce22422a2e/docs/roadmap/KI-MCP-GIT-FND-006-ground-roots-in-workspaces.md) commits to `origin/main`. The CI pin commits are unpushed: one on mcp-git-audit `main` and one on tools-git-almanac `main`, both on this Mac.

## In Progress

Nothing. No record is left in my lane that I can move.

## Queries

None. CANCEL-MERGE: no candidates in mcp-git-audit or tools-git-almanac.
