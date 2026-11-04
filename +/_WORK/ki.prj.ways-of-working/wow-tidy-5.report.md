# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-tidy-5

**🤖 → 👤 Handoff to supervisor · Run report at 05:11 GMT · last mark 05:11 GMT**

---

## Done

- I deleted 73 loose reports from the top level of the package. Each one's outcome is recorded in `decisions.md` and its queries are in `discussions.md` or answered in the decisions log. Fifteen of them were byte-identical or near-identical copies of reports the focus folders already hold. Note: the launcher had kept its own copy for only 36 of the 88 loose reports. The other 52 had no copy under `~/.local/state/ki/agents/ki-project-ways-of-working/`, so I deleted only those whose outcome and queries were recorded in the logs.
- I moved 15 reports into their focus folders and committed them in `a485f90b`. Their outcome or a query was not recorded in the logs. Ten conform sweeps went to `rollout/`, `apply-reviews` to `discussions/`, `resolve-5` to `host-reconcile/`, `acquire-held` (CURATE-STRIKE) to `capture-model/`, `footer-fields` (SYNC-OFF-WORDING, STOP-LISTENING-CAPABILITY) to `inbox-wake/`, and `withdraw-adr-007` (PEER-CITE) to `aside/`. Commit check passed. The commit is published.
- I deleted the two spent briefs, `resolve-5` and `resolve-6`, and removed the empty `briefs/` folder.
- I kept 2 files: the two Z files in `reports/` (see Z-FILES-HOME below).
- The `ki-work-package` audit failed both before and after the tidy, with failures in other packages. For this package, the warning about loose top-level reports is gone. One failure remains, because `reports/` still exists.
- I left the focus folders alone, as the brief asked. The audit still flags received briefs and answered reports inside them (FOLDER-2, FOLDER-3). The `personal-shape/handover-plan.report.md` file in the focus folder is the earlier draft. The final version is the launcher's copy.

## In Progress

Nothing is running.

## Queries

### Z-FILES-HOME - Where the two Z files go

**Context:** `reports/` still holds `hold-request-20261030-z.md` and `z-session-retirement-20261030.md`. They have never been committed. The open query Z-FILES in [discussions.md](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/discussions.md) says to keep them out of any commit until the public-report questions are settled. The brief asked to move live material into a focus folder with `git mv`, but that would commit them. So I left them where they are, and the audit's one failure for this package remains until they move.

**Query:** Should the two Z files move, uncommitted, into `package-layout/` so that `reports/` can be removed now?

**Options:**

a) (recommended, confidence medium - this clears the audit and keeps Z-FILES's no-commit rule, but it changes the path that Z-FILES names) A small run moves them with a plain `mv` into `package-layout/`, removes `reports/`, and updates the path in Z-FILES.

b) Leave them in `reports/` until Z-FILES is answered.
