# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › burn-observatory

**🤖 → 👤 Handoff to supervisor · Run report at 06:21 BST · last mark 06:21 BST**

---

## Done

- [KI-OBSERVA-OPS-003 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/ab08287869ce6d5b187be7e5266e7194146f48b5/docs/roadmap/KI-OBSERVA-OPS-003-observatory-serving-location.md), Observatory serving location: went from soon, draft to now, awaiting review. It was planned (3299dec), then delivered (89f3978). An open tab now offers `server restarted: reload` when the server behind it has restarted, using a new plain-text `GET /build`. The finding recommends keeping the primary checkout with `bun --watch` as where the service runs. Checks: test 8/8 pass, typecheck pass, biome pass, knip pass, rumdl pass, browser smoke pass, roadmap audit FAIL=0. The running service picked up the change by itself: `/build` answers and `/health` says ok.
- [KI-OBSERVA-BRG-005](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-005-act-board-missing-parts.md), Act board missing parts: stays awaiting review, and its review packet is now complete (c162c05). I put the sections in the order the audit requires, added the post-change review and the recap, and recorded tonight's re-run checks: all pass, and the audit finds nothing on this record. Your check by eye at 1,440 px and 760 px is still outstanding.
- [KI-OBSERVA-VIS-027 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/ab08287869ce6d5b187be7e5266e7194146f48b5/docs/roadmap/KI-OBSERVA-VIS-027-themes-in-streams-read.md), Themes in Streams read: stays awaiting review, and its horizon moves from next to now (c162c05). I corrected the body order and the packet order and added the post-change review and recap. The live check now passes: the running service lists 4 themes and 23 Projects, every Project has a theme, none are legacy, and no local path appears. The record said 21 Projects; two have been added since.
- [KI-OBSERVA-BRG-006 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/20061964d6e424dac55199dc393653fecc774299/docs/roadmap/KI-OBSERVA-BRG-006-feedback-to-messages-file.md): stays awaiting review. Its packet was already complete, so nothing changed.
- Local `main` in apps-observatory.local is fast-forwarded to c162c05. The worktree and the run branch are removed, and the temp folder is empty.
- Follow-ups are queued in the [ki.observatory messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/messages.md) (ki-principal 572246e1, local only), so no new records were created:
  - the OPS-003 delivery, with the idea of relaxing the AGENTS.md kickstart rule;
  - APP-044's out-of-date Current state;
  - BRG-004 being close to release from hold.
- Not pushed: either repository.
  - apps-observatory.local `main` is 8 ahead of origin. Five of those commits are other sessions' from tonight: e23d85a, c1f0083 and 24f418a (accept and prune), and cd7802b and 5d0f9ea (hook adoption). The brief says to stop pushing a repository when other sessions' commits are stacked.
  - ki-principal is 29 ahead, mostly other sessions' work.

## In Progress

Left as they are, with the reason for each:

- [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) (in progress): the only step left is positions as a host preference. Your 20 October approval left that step out, and it waits for your designs.
- [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) (now, draft): it needs your answers to the RESTRUCTURE query (converge, job switch, order, DESIGN-WORK).
- Records on hold whose condition still stands:
  - [KI-OBSERVA-BRG-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-004-turn-feedback-sending-on.md): waits until BRG-006 and [KI-HARNESS-GOV-219 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-219-feedback-work-folder-kind.md) are accepted.
  - [KI-OBSERVA-INT-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-INT-003-extensions-switchboard.md): its inbound phase waits on step 3.
  - [KI-OBSERVA-OPS-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-OPS-004-tailnet-read-only-appearance.md) and [KI-OBSERVA-VIS-029](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-029-sessions-from-every-host.md): wait on the tailnet decision.
  - [KI-OBSERVA-VIS-028](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-028-retire-sessions-readers.md): waits on migration phase 5.
  - [KI-OBSERVA-VIS-032](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-032-library-instrument.md), VIS-034, VIS-038 and VIS-045: wait on APP-044 and your approval.
  - [KI-OBSERVA-VIS-042 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/20061964d6e424dac55199dc393653fecc774299/docs/roadmap/KI-OBSERVA-VIS-042-diagram-overlay-everywhere.md): waits on [KI-HARNESS-GOV-224 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/7378f88a323454339ae61bab6bd1bdb03104a8eb/docs/roadmap/KI-HARNESS-GOV-224-diagram-viewer-receipts.md).
- None of these is stale, superseded or a duplicate.
- To review: OPS-003, BRG-005, BRG-006 and VIS-027.

## Queries

**OBS-BURN-PUSH**

**Context:** apps-observatory.local `main` carries tonight's three commits from this run, stacked on five commits from other sessions that have not been pushed. ki-principal is in the same position.

**Query:** Who pushes these, and when?

**Options:**

a) (recommended, confidence high - every commit is checked and fast-forward only) You or the next interactive session push both repositories' `main` together after a look at the log.

b) Leave them for each originating session to push its own commits.

**OBS-KICKSTART-RULE**

**Context:** Since Rig runs the service with `bun --watch`, fast-forwarding `main` in the primary checkout restarted it on its own tonight. The AGENTS.md finish step still asks for `launchctl kickstart`.

**Query:** Should the finish step change to "confirm <http://127.0.0.1:1675/> answers", with the kickstart kept as a fallback?

**Options:**

a) (recommended, confidence medium - the watcher handled tonight's delivery, but it has had only a day of use) Yes, change AGENTS.md as a small fix.

b) Keep the kickstart step as it is.

```text
OBS-BURN-PUSH: a
OBS-KICKSTART-RULE: a
```
