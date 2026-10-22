# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › prune-links

**🤖 → 👤 Handoff to supervisor · Run report at 06:57 BST · last mark 05:20 BST**

---

## Done

- [KI-TOOL-RIG-CLI-026 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/74140e53/docs/roadmap/KI-TOOL-RIG-CLI-026-per-tool-development-mode-switch.md), [KI-TOOL-RIG-CORE-057 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/74140e53/docs/roadmap/KI-TOOL-RIG-CORE-057-github-desktop-repository-list.md) and [KI-TOOL-RIG-DIST-011 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/74140e53/docs/roadmap/KI-TOOL-RIG-DIST-011-stale-terra-rig-link.md): pruned. They were still cancelled, and their last revision `74140e53` is on the remote. Prune commit tools-rig `2054674f`, pushed. Its hook ran all 602 Bats tests and they passed. The hook's existing SHELL-HOOK audit finding remains and did not block the commit. 17 links repaired in ki-principal.
- [KI-TOOL-TECHNE-CLI-009 (pruned)](https://github.com/knowledgeislands/tools-techne/blob/78f88656/docs/roadmap/KI-TOOL-TECHNE-CLI-009-tailscale-oauth-binding-field.md): pruned. It was still done, and `78f88656` is on the remote. Prune commit tools-techne `1cc9e300`, pushed. 3 links repaired in ki-principal and 1 in [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md), committed in tools-techne `c1b08a1` and pushed.
- [KI-MCP-M365-TOOL-020 (pruned)](https://github.com/knowledgeislands/mcp-m365/blob/f06d3ddb/docs/roadmap/KI-MCP-M365-TOOL-020-distribute-the-routing-core.md): pruned. It was still cancelled (merged), and `f06d3ddb` is on the remote. Prune commit mcp-m365 `8561637e`, not pushed because another session's unpushed commit `11e55b0` sits below it. 2 links repaired in ki-principal. [KI-MCP-GSUITE-TOOL-008](/Users/krisbrown/workspaces/knowledge-islands/mcp-gsuite/docs/roadmap/KI-MCP-GSUITE-TOOL-008-consume-the-routing-core.md) cited the pruned record as the home of the core's manifest. Both of its links now name [KI-MCP-M365-TOOL-018](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/roadmap/KI-MCP-M365-TOOL-018-extract-the-routing-core.md), the record that absorbed it, as that home, with the pruned record linked beside it. That change is committed as mcp-gsuite `88decf5` and not pushed, because another session's unpushed commit `df58ba7` sits below it.
- [KI-TOOL-KI-CLI-151 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/949cd36a/docs/roadmap/KI-TOOL-KI-CLI-151-cli-conventions-departures.md): pruned. It was still cancelled, and its last change `a1fdecb4` is on the remote. The link uses origin/main `949cd36a`, where the record is present and unchanged. Prune commit tools-ki `a37f3151`, not pushed because 7 commits from other runs sit below it. 3 links repaired in ki-principal.
- Skipped: [KI-HARNESS-GOV-216](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-216-three-part-updates.md), [KI-HARNESS-GOV-222](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-222-timeline-and-calendar-skill.md) and [KI-HARNESS-GOV-226](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-226-banner-rendered-glyphs.md). Their cancellation commit `ae8a1323` exists only locally, with 11 unpushed commits from other sessions in ki-agentic-harness.
- Skipped: [KI-TOOL-KI-CLI-152](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-152-work-folder-housekeeping-commands.md) and [KI-TOOL-KI-CLI-167](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-167-knip-reads-committed-hooks.md). Their acceptance commit `bc563d56` exists only locally, above 4 other sessions' unpushed commits.
- Skipped: [KI-OBSERVA-OPS-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-OPS-003-observatory-serving-location.md) and [KI-OBSERVA-VIS-027](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-027-themes-in-streams-read.md). Their acceptance commit `ab751e25` exists only locally, above 8 other runs' unpushed commits.
- Link repairs in ki-principal: 26 links across 9 work-package files in ki.agent-host, ki.mac-studio-setup, ki.tools-burndown, ki.ways-of-working's design note and ki's state. Committed as `3ecafc88`. Only links were changed.
- Link-target check: passed. Each pruned link's revision holds the record in its terminal state and is on origin/main.
- Final sweep of every Git checkout under knowledge-islands: passed, with no live link to any of the six pruned records left outside the pruned form.
- CAPTURE-GATE: PRUNE-LINKS-REST was added to [ki.ways-of-working messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/messages.md) for a second pass over the seven skipped records. Committed as ki-principal `ff207766`.
- Commit hooks: passed on every commit. Two first attempts failed commitlint on body line length and were rewrapped; nothing was bypassed and nothing was force-pushed.
- Not pushed: ki-principal (`3ecafc88`, `ff207766`) sits above 46 other sessions' unpushed commits. mcp-m365, mcp-gsuite and tools-ki each have this run's commits stacked above other sessions' commits.
- Temporary directory: emptied.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- After those repositories are pushed, a second prune-links pass can prune the seven skipped records (PRUNE-LINKS-REST).

## Queries

No outstanding queries

### 🤖 → 👤 Handoff to supervisor · since 06:57 BST

🤖 0 running · 👤 0 with you

- [committed] six records pruned, links repaired
- [unpushed] ki-principal `3ecafc88`, `ff207766` · sol · main
- [unpushed] mcp-m365 `8561637e` · sol · main
- [unpushed] mcp-gsuite `88decf5` · sol · main
- [unpushed] tools-ki `a37f3151` · sol · main
