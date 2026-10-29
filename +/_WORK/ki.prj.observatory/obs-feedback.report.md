# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-feedback

**🤖 → 👤 Handoff to supervisor · Run report at 20:55 BST · last mark 20:54 BST**

---

## Done

- Delivered [KI-OBSERVA-BRG-002](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-002-capture-feedback.md) Capture feedback with sending switched off, and moved it to Awaiting review. You can comment on any block, or on the whole document, in Documents, Knowledge Bases and the new Work report reader, which Review queue rows now open. Each document keeps one draft in the Observatory's state, and its package and Messages line can be previewed exactly.
- `feedback-send` commits only the package and `work.md`, puts both back if the commit fails, and binds its plan to the draft. While `FEEDBACK_SENDING` is `false`, planning it is refused, executing it is refused with a receipt, and nothing is written to any `+/_WORK` folder.
- Added PDR-KI-OBSERVA-007, OBS-ACT-014, OBS-BOUND-015, schema and route rows, the operator guide `give-feedback.md`, and README and CHANGELOG entries.
- Recorded the remaining step, turning sending on when KI-HARNESS-GOV-219 lands, under the record's Dependencies / blocks.
- Commits `ffb5e50` (feat) and `d38fe63` (docs). Both were pushed fast-forward to `origin/main`, and only those two were stacked.
- Gate: `bun run test`, typecheck, build, knip and rumdl pass. Biome passes, with only known warnings in lines this work did not touch. `ki repo audit` adds no finding; its one failure is the title length of KI-OBSERVA-VIS-022, which was already there.

## In Progress

- The Observatory service needs restarting so it serves this delivery. This detached run did not restart it.

## Queries

None.
