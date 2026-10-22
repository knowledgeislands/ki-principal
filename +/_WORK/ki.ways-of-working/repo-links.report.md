# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › repo-links

**🤖 → 👤 Handoff to supervisor · Run report at 15:17 BST · last mark 13:37 BST**

---

## Done

The estate dry run proposed only work-package link changes: 19 `ki-work-package` links to add and 19 dangling `ki-work-folder` links to remove, in 10 of 51 repositories. It proposed nothing else, so there was nothing to list. I applied it one repository at a time with `ki repo --repo <path> repair`, and every repository passed. The links are gitignored projections that Git does not track in any of the 10, so there were no commits and no pushes. Net records: 0 everywhere. ki-design and the chezmoi source were already healthy and I did not touch them.

- **ki-principal:** `.claude` and `.agents` links added, dangling ones removed. `ki-work-package` now resolves and loads as a skill in this session.
- **ki-agentic-harness:** `.claude` and `.agents` links added, dangling ones removed. The skill resolves.
- **personal-principal:** `.claude` and `.agents` links added, dangling ones removed.
- **personal/acquire:** `.agents` link added and dangling one removed (it has only the `.agents` projection).
- **legal-principal:** `.claude` and `.agents` links added, dangling ones removed.
- **hnr-principal:** `.claude` and `.agents` links added, dangling ones removed.
- **er-principal:** `.claude` and `.agents` links added, dangling ones removed.
- **si-principal:** `.claude` and `.agents` links added, dangling ones removed.
- **tmx-principal:** `.claude` and `.agents` links added, dangling ones removed.
- **va-principal:** `.claude` and `.agents` links added, dangling ones removed.
- **Rerun of the estate dry run:** PASS. All 51 repositories are healthy, none is repairable, no `ki-work-folder` link is left and 19 `ki-work-package` links are in place.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Sessions that were already open in these repositories need a restart before they see `ki-work-package` as a skill.

## Queries

No outstanding queries
