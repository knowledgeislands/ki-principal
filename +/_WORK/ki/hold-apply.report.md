# [Techne](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/techne.md) › [Agent host](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/agent-host.md) › hold-apply

**🤖 → 👤 Handoff to supervisor · Run report at 01:02 BST · last mark 15:59 BST, 15 October**

---

## Done

- CHAIN-GATE a): [KI-TOOL-RIG-CORE-048](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-048-signed-release-install-kind.md) is released from hold to `soon`. It has a Shaping section covering the built-in signed-release approach and the shared-role scope it already had. The section says delivery clears only the signed-install prerequisite: KI-TECHNE-OPS-018 still needs the binding owner's evidence of a clean `rig status` through a pin bump, and KI-TECHNE-OPS-024 still needs the role-profile move. Both stay held, and nothing was created, split or merged. tools-rig `512f21f`.
- CLI125-HOLD a): [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-125-ki-release-contract.md) stays on hold. Its condition now reads "An ARM host is needed", with the review date still 2026-11-16. tools-ki `1baef525`.
- In the [ki.agent-host package](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.agent-host/): both queries are deleted from `queries.md`, as the package standard does for answered queries. They are recorded as Decisions 71 and 72 in `decisions.md`, each "taken under OVERNIGHT, reviewed by query-review-6". I also brought the first next step in `state.md` up to date, since it still listed both queries as waiting. ki-principal `ea182d66`.
- Checks: `ki repo audit` passes in tools-rig and tools-ki; both records keep the existing migration-window `size` warning.
- Checks: `ki repo audit` fails in ki-principal on findings that were already there: Markdown, Decision Records, and work-package schema in other packages. One of those is ki.agent-host `state.md`'s `hold: null`, which was already committed. My commit added none of them.
- Checks: `rumdl` passes on every file I changed. The tools-rig pre-commit gate passed, all 593 tests included.
- Commits: tools-rig and tools-ki were committed with the path on the commit command. In ki-principal, another session appended Decision 73 (CLI006-PLAN) to `decisions.md` while I was working. I therefore committed my three paths through a private index, without Decision 73, rather than putting the paths on the commit command. Decision 73 is still uncommitted, belongs to that session, and is untouched. Nothing pushed.

## In Progress

None.

## Queries

None.
