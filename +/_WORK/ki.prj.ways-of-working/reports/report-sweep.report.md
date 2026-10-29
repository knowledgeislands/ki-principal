# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › report-sweep

**🤖 → 👤 Handoff to supervisor · Run report at 18:31 BST · last mark 18:12 BST**

---

## Done

- Swept every `+/_WORK/<id>/` in all 51 registered repositories. Only five held run reports or briefs: acquire, hnr-principal, ki-principal, legal-principal and personal-principal. chezmoi has no `+/_WORK/`. Started after chezmoi-migrate read DONE.
- Deleted 133 homed reports and briefs by explicit path. Kept 104 and put one REPORT-SWEEP line in each of the 14 works that still hold kept files, asking its coordinator to receive them at its next mark.
- Correction made: in `hnr.fourth-white-paper` the subagent had deleted five reports that `design/hold-inventory.md` retains "until coordinator confirms". When in doubt the brief says keep, so I restored them before committing and named them in that work's line: `apply-gut-preview`, `body-prose`, `production-history`, `publish-reviewed-prose` and `sharepoint-review-record`.
- personal-principal: the pull-rebase conflicted on `kb.personal-tower/messages.md`. That work's live coordinator had pushed three commits at 18:20-18:25 and made the same five tower deletions itself. I resolved the conflict as its emptied queue plus my one line, so my commit adds only that line for the tower.
- Audits: every repository's audit was run, scoped to `+/_WORK`. hnr-principal and acquire pass in scope. ki-principal, legal-principal and personal-principal fail in scope only on findings that were there before: COORD-7 in kept reports I did not change, and RECORD-2 in `ki.specifications` and `ki.tools-burndown` message files I did not edit. The ki-principal commit gate passed on its 20 paths.
- Pushed fast-forward with only my own commit stacked: ki-principal `5b8ac0f3`, hnr-principal `8ce273c`, legal-principal `2977941e`, personal-principal `d447ac28`. acquire `4f1afea` is committed but not pushed (query ACQUIRE-PUSH).
- Left alone: the untracked `+/_WORK/ki.chezmoi/husky-apply.report.md`, another session's file. Nothing else was dirty in any work folder. `+/_Voice Notes/` was not touched.
- Limitations: the in-session subagents ran asynchronously. The harness launched them that way, against the progress protocol's "no background subagents". The acquire audit's `ki-repo` checks read GitHub live state. Some `queries.md` "from" links and `design/hold-inventory.md` now point at deleted reports, which Git history still holds, as the standard expects. Temporary output has been cleared.

| Repository | Work | Reports found | Deleted | Kept and messaged | Commit | Pushed |
| --- | --- | --- | --- | --- | --- | --- |
| acquire | kb.regular.acquire-intake | 1 | 0 | 1, messaged | `4f1afea` | no, ACQUIRE-PUSH |
| hnr-principal | hnr.fourth-white-paper | 86 | 76 | 10, messaged | `8ce273c` | yes |
| hnr-principal | hnr.wp2-3-1-tn | 9 | 9 | 0 | `8ce273c` | yes |
| hnr-principal | hnr.phase3 | 2 | 2 | 0 | `8ce273c` | yes |
| hnr-principal | hnr.email-routing | 2 | 1 | 1, messaged | `8ce273c` | yes |
| hnr-principal | hnr.regular.msf-ibc-handoff | 2 | 0 | 2, messaged | `8ce273c` | yes |
| hnr-principal | hnr.product-management | 1 | 0 | 1, messaged | `8ce273c` | yes |
| hnr-principal | hnr.regular.maven-transcript | 1 | 0 | 1, messaged | `8ce273c` | yes |
| ki-principal | ki.chezmoi | 38 | 13 | 24, messaged; 1 untracked left | `5b8ac0f3` | yes |
| ki-principal | ki.mac-studio-setup | 4 | 0 | 4, messaged | `5b8ac0f3` | yes |
| ki-principal | ki | 2 | 0 | 2, messaged | `5b8ac0f3` | yes |
| ki-principal | ki.knowledge-acquisition | 1 | 0 | 1, messaged | `5b8ac0f3` | yes |
| ki-principal | ki.ways-of-working | 1 | 0 | 1, messaged | `5b8ac0f3` | yes |
| ki-principal | ki.observatory | 1 | 1 | 0 | `5b8ac0f3` | yes |
| ki-principal | ki.specifications | 1 | 1 | 0 | `5b8ac0f3` | yes |
| legal-principal | lgl | 49 | 23 | 26, messaged | `2977941e` | yes |
| personal-principal | kb.personal-tower | 27 | 5, already made by its coordinator | 22, messaged | `d447ac28` | yes |
| personal-principal | kb.family-and-friends | 5 | 5 | 0 | `d447ac28` | yes |
| personal-principal | kb.personal-health | 3 | 2 | 1, messaged | `d447ac28` | yes |

## In Progress

Nothing is running.

Outstanding - no action requested now:

- 104 kept reports and briefs wait for their coordinators to receive them at their next marks. Each work's `messages.md` names them.
- The `lgl` and `kb.personal-tower` lines run well over 60 words because they name every kept file (26 and 22).

## Queries

### ACQUIRE-PUSH - Push the acquire sweep with citations-rewrite's commit beneath it

**Context:** In acquire, my prune commit `4f1afea` sits on top of `2a70d45` "docs: rewrite retired work-folder citations". citations-rewrite made that commit locally and it is unpushed. The brief lets me push only where my own commits alone are stacked, so I committed and did not push. The coordinator received citations-rewrite at 18:18.

**Query:** Should both acquire commits be pushed together now?

**Options:** a) (recommended, confidence medium - the commit is this coordinator's own received run, but I have not re-verified its content) Push `2a70d45` and `4f1afea` together, fast-forward, from acquire. b) Leave both unpushed until citations-rewrite's push is decided on its own.
