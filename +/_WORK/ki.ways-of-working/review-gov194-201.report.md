# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › review-gov194-201

**🤖 → 🧑 Handoff to supervisor · Run report at 18:08 BST · last mark 18:04 BST**

---

## Done

- The independent review of [KI-HARNESS-GOV-194 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f7982a61/docs/roadmap/KI-HARNESS-GOV-194-review-verification-effects.md) found nothing wrong. The review checklist gains exactly the two approved items and nothing else changed. Under ACCEPT-AND-PRUNE it was accepted as done in `f7982a61`, then pruned in `33c494c9`, because nothing durable still links to it.
- The independent review of [KI-HARNESS-GOV-201](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-201-fetch-and-machine-grants.md) also found nothing wrong. Both grant texts are unchanged from the wording you approved, and the standard and the RUN-1 check match the record. It was accepted as done in `f7982a61`. It has not been pruned yet: see [PRUNE-GOV-201](https://github.com/knowledgeislands/ki-agentic-harness/blob/f7982a61/docs/roadmap/KI-HARNESS-GOV-201-fetch-and-machine-grants.md).
- GRANT-INTERIM is confirmed. The standard's Grants section still says a brief adds a grant section by hand until the launcher offers `--allow`. [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md) is still in progress and says the sentence can go once it ships. [KI-HARNESS-GOV-201](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-201-fetch-and-machine-grants.md)'s Done section records this.
- I re-ran the checks: `bun run test` passed (1254 pass, 0 fail) and `bunx --no-install tsc --noEmit` passed. `ki dev skill rubric ki-delegation` is in sync. `ki repo audit` passed with no failure or warning for `ki-delegation`, `ki-repo`, `ki-skills`, `ki-authoring`, `ki-work`, `ki-work-roadmap` and `ki-trades`. I re-ran the roadmap and authoring audits and the tests after each commit, and they passed. Every check ran locally.
- Both commits are pushed to ki-agentic-harness `main`. No other session's commits went with them.
- Net record count: ki-agentic-harness has one fewer ([KI-HARNESS-GOV-194 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f7982a61/docs/roadmap/KI-HARNESS-GOV-194-review-verification-effects.md) pruned; [KI-HARNESS-GOV-201](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-201-fetch-and-machine-grants.md) is now done but still there). tools-ki and ki-principal are unchanged.
- This report is only at the run's state path, because the launch protocol makes that the only report path. So nothing was written or committed in ki-principal.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Some ki-principal work-folder reports still link [KI-HARNESS-GOV-194 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f7982a61/docs/roadmap/KI-HARNESS-GOV-194-review-verification-effects.md) by its local path, which pruning has broken: `ki.ways-of-working/gov194-refresh.report.md`, `harness-upkeep.report.md` and `design/migration-plan/capital/05-work-folders.dry-run.txt`. The coordinator can repoint or drop them at the next mark. Two tools-burndown reports link [KI-HARNESS-GOV-201](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-201-fetch-and-machine-grants.md) the same way, which matters once it is pruned.
- tools-ki has another session's uncommitted file, `src/core/agent/thread.ts`. I left it alone.

## Queries

### [PRUNE-GOV-201](https://github.com/knowledgeislands/ki-agentic-harness/blob/f7982a61/docs/roadmap/KI-HARNESS-GOV-201-fetch-and-machine-grants.md) - A tools-ki link keeps [KI-HARNESS-GOV-201](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-201-fetch-and-machine-grants.md) from being pruned

**Context:** [KI-HARNESS-GOV-201](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-201-fetch-and-machine-grants.md) is accepted and done. The prune check found two places that link its local file. One is the ki-delegation sources note in this repository, which I can repoint. The other is two links in the Dependencies section of [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md) in tools-ki. That is another repository, which another session currently has uncommitted work in, and prune approval does not cover edits there. So the record stays done, and pruning it now would break those links.

**Query:** Should a tools-ki run repoint the [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md) links to the record's committed copy so that [KI-HARNESS-GOV-201](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-201-fetch-and-machine-grants.md) can then be pruned?

**Options:** a) (recommended, confidence high - the links are mechanical, and the pinned copy at `f7982a61` is pushed) Fold the repoint into the next tools-ki run that touches [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md). Point both links at `https://github.com/knowledgeislands/ki-agentic-harness/blob/f7982a61/docs/roadmap/KI-HARNESS-GOV-201-fetch-and-machine-grants.md`. Then have a harness run repoint the sources note and prune the record. b) Keep [KI-HARNESS-GOV-201](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-201-fetch-and-machine-grants.md) as done until [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md) ships and the interim sentence goes, then prune both together.

### 🤖 → 🧑 Handoff to supervisor · since 18:08 BST

🧑 1 with you

- [with you] [PRUNE-GOV-201](https://github.com/knowledgeislands/ki-agentic-harness/blob/f7982a61/docs/roadmap/KI-HARNESS-GOV-201-fetch-and-machine-grants.md) · owner · since 18:08
- [committed] ki-agentic-harness, pushed
