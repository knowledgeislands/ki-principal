# [State of play](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/work.md) › live-man-switch

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 23:10 BST**

---

## Done

- Added the reverse dead man's switch idea, dated 15 October, to the Notes of [Host network](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/host-network.md) as a design input for the firewall and key-only SSH rollouts and the restore-path decision paper, linking [KI-TOOL-RIG-CORE-046 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/06da52aec5de/docs/roadmap/KI-TOOL-RIG-CORE-046-remote-access-and-continuity.md), and set `updated`; no en or em dashes.
- Commit refused by the pre-commit audit: `ki-repo-kb-streams` STREAM-9 (upward-only registry notes) fails because a Project note names a work record. A test with the record identifier taken out of the link text still failed, because the identifier is also in the URL.

## In Progress

Nothing is running. The edit is left uncommitted and unstaged in `Streams/Projects/host-network.md` in ki-principal; nothing else was touched.

## Queries

### PRUNED-LINK - Project note cannot link the pruned record

**Context:** The brief asked for the idea's earlier home to be linked by its pruned-record link. STREAM-9 does not let a Project note name a work record, even a pruned one in another repository, so the commit hook rejects the note while that link is there. `--no-verify` is not allowed. The idea itself passes; only the link to the record fails.

**Query:** How should the Host network note point to the idea's earlier home so the commit can go through?

**Options:**
a) (recommended, confidence medium - this passes the check and keeps the provenance in the commit, but drops the link the brief asked for) Remove the link from the note, say in prose that the idea was first captured in a tools-rig remote-access record that has since been cancelled, and put the pruned link in the commit body.
b) Keep the link and have `ki-agentic-harness` change STREAM-9 so it allows pruned links to other repositories; the note stays uncommitted until that change ships.
c) Record the link in the `ki` work package's decisions log instead, and keep the note free of record identifiers.
