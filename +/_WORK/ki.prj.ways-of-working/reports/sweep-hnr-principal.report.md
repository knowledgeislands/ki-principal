# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › sweep-hnr-principal

**🤖 → 👤 Handoff to supervisor · Run report at 00:28 GMT · last mark 00:24 GMT**

---

## Done

- hnr-principal `.gitignore`: added `!/+/_WORK/*/reports/` and `!/+/_WORK_REVIEW/*/reports/` after the `reports/` rule (`5d378f67`); verified that a work-folder `reports/` path is no longer ignored.
- 59 top-level reports moved with `git mv` (all were tracked) across seven work folders. No folder had a live run, so none was skipped. No name clashes. Nothing deleted. Each commit adds the REPORTS-MOVED line to that folder's `messages.md`:
  - `hnr.prj.5g-emerge-p2ms3`: 16 moved (`6b87c765`); 1 link repointed.
  - `hnr.prj.5g-emerge-phase2`: 5 moved (`53bd4903`); 9 links/paths repointed, including the two `home:` paths in `decisions.md`.
  - `hnr.prj.portal-framework`: 2 moved (`93e341cf`); 2 reference links repointed in `hnr.sop.sites/design/eit-retirement.md`, one of them to a phase2 report.
  - `hnr.reg.email-routing`: 2 moved (`74e93191`); 1 link repointed.
  - `hnr.reg.msf-ibc-handoff`: 2 moved (`6a43d00b`); 11 links repointed across its own `work.md`, `state.md` and `queries.md`, `hnr.prj.product-management/design/umso-intake.md`, `umso-gap-review.md` and `Streams/Projects/hnr-command-centre.md`.
  - `hnr.sop.main`: 9 moved (`c68ed1b3`); 9 links repointed, 4 in its `decisions.md` and 5 absolute links in `Streams/Roadmap/HNR-PRINCIPAL-ENG-004-set-the-console-icon-standard.md`.
  - `hnr.prj.developer-experience-and-build-pipelines`: 23 moved (`f708b443`); no path links to repoint. The first commit attempt failed the Markdown lint because this `messages.md` puts a blank line between items. I added the blank line before the new line and the commit then went through.
- Left as they were: references that only give a report's file name in backticks or plain text, links pinned to GitHub revisions, links to runtime copies under `~/.local/state`, and the display label `prj.5g-emerge-phase2/phosphor-plan.report.md` in `eit-retirement.md`, whose link target I did update.
- Publishing: the remote had moved on by one commit from another session (phase3 work, no files in common), so I merged `origin/main` in a temporary worktree (`09ac534e`, no rebase) and pushed fast-forward only. The checkout is level with `origin/main` and the temporary worktree is removed. The automatic merge commit message reads "into HEAD" and has no co-author trailer. It was already pushed, so I left it as it is.

## In Progress

Nothing is running.

Outstanding - no action requested now: the moved reports' own relative links, for example to `state.md` or `work.md` in the same folder, now point one level too shallow. The brief covered only links to the reports, so I did not edit them. Each steward can prune these reports at their next mark.

## Queries

No outstanding queries.
