# [Foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Tools burndown](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/tools-burndown.md) › mgit-prune

**🤖 → 🧑 Handoff to supervisor · Run report at 19:10 BST · last mark 19:10 BST · blocked**

---

## Done

- Nothing was deleted, committed or pushed. tools-mgit is unchanged: its tree is clean, no rebase or merge is in progress, and the newest commit (c4da60c) is from 18:38 BST, which is more than 10 minutes old.
- All three records are `status: done` in committed history and have no trade links: [KI-TOOL-MGIT-CLI-020](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-020-safe-parallel-sync.md), [KI-TOOL-MGIT-CLI-021](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-021-estate-overview.md) and [KI-TOOL-MGIT-CLI-022](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-022-external-member-review-findings.md).
- The ki-accept reference check failed. Before a prune, links to these records must be repaired in a separate commit. Each record still has live Markdown links pointing at it:
  - KI-TOOL-MGIT-CLI-020: links from [KI-TOOL-MGIT-CLI-018](https://github.com/knowledgeislands/tools-mgit/blob/2ca3a8e06b88deb72b48476420f0f2211e56f5b8/docs/roadmap/KI-TOOL-MGIT-CLI-018-estate-scale-output.md), [KI-TOOL-MGIT-CLI-023](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-023-hands-on-behaviour-check.md) and [KI-TOOL-MGIT-CLI-026](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-026-sync-conflict-precheck.md).
  - KI-TOOL-MGIT-CLI-021: links from KI-TOOL-MGIT-CLI-018, KI-TOOL-MGIT-CLI-023 and, in the peer repository tools-ki, [KI-TOOL-KI-CLI-140](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-140-git-hygiene-estate-audit.md) (draft). That record links to 021 twice, as the source of `mgit overview --json`.
  - KI-TOOL-MGIT-CLI-022: links from [KI-TOOL-MGIT-CLI-017](https://github.com/knowledgeislands/tools-mgit/blob/af6e67736262ec4c0e0fa5f74507849bda48a503/docs/roadmap/KI-TOOL-MGIT-CLI-017-unified-external-members.md) and KI-TOOL-MGIT-CLI-023.
- The brief does not let me repair those links. It says to change no other record, Ways of working holds KI-TOOL-MGIT-CLI-017 and -018, and prune approval does not cover edits in a peer repository. The procedure says to keep a Done record whose links cannot be repaired, so I kept all three.
- Repositories searched: every repository under `workspaces/knowledge-islands`, plus chezmoi. Mentions in ki-principal `+/_WORK` reports and the decisions log name the records by ID only. They are not links, so they do not block the prune.

## In Progress

- Nothing.

## Queries

**MGIT-PRUNE-LINKS**

**Context:** Pruning KI-TOOL-MGIT-CLI-020, -021 and -022 would break links in KI-TOOL-MGIT-CLI-017, -018, -023 and -026, and in tools-ki's KI-TOOL-KI-CLI-140. A repair commit has to land before the prune. It would point each link at the record's GitHub copy at its last revision, or at a current guide.

**Query:** How should the links be repaired before the prune?

**Options:** a) (recommended, confidence high - this keeps the procedure and the Ways of working hold intact) Wait until Ways of working releases KI-TOOL-MGIT-CLI-017 and -018. Then authorise one tools-mgit commit that repoints the links in 017, 018, 023 and 026, and one tools-ki commit that does the same for KI-TOOL-KI-CLI-140. Then run the prune. b) Authorise the repairs now in 023, 026 and KI-TOOL-KI-CLI-140 only, and leave the records Ways of working holds for later. This still blocks all three prunes, because 017 and 018 link to all three records. c) Leave the three Done records in place for now.
