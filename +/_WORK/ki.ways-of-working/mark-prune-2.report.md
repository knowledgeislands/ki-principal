# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › mark-prune-2

**🤖 → 👤 Handoff to supervisor · Run report at 18:56 BST · last mark 18:12 BST**

---

## Done

- **Reports pruned:** I deleted the `accept-mgit` and `mgit-flags` reports. Every query in them is answered: MGIT-FLAGS-CONFIRM and MGIT-FLAGS-ACCEPT under MGIT-FLAGS in the recap batch of 18 October, MGIT-017-CONFIRM a), and MGIT-FLAGS-APPLY a), whose completion is applied on this Mac. Their outcomes are recorded in [KI-TOOL-MGIT-CLI-023](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-023-hands-on-behaviour-check.md) to [KI-TOOL-MGIT-CLI-026](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-026-sync-conflict-precheck.md). There were no briefs to delete.
- **Reports kept:**
  - `work-folder-rename`, because its query LAUNCH-REPORT-PATH is still open (see Queries).
  - The nine reports you named from runs that have finished (threads-fix, review-gov194-201, mgit-learn, records-fold, rig-lock-review, desk-kit-sop, principal-audit, accept-prune and glyph-owner). They are still uncommitted and waiting for you to receive them.
  - `work.md`, `decisions.md` and `design/`.
- **Decisions log:** cut from 409 lines to about 195.
  - Kept unchanged: everything from the "recap batch" entry onwards, and the standing rules (PAPERCLIP-REQ, ROUTINE, COUNSEL, MIGRATION-ORDER, MECHANICAL, LEAD, ONE-PROJECT, COMMIT-AS-YOU-GO, MAIN-NOT-WORKTREES, KEEP-PUSHING, the website note and VISIBLE-PUSH).
  - Kept as single lines, because they still apply to open work: DESK-KIT-SOP, RIG-LOCK-FOLLOWUP, RIG-LOCK-RELEASE, STATE-TOOLING-147, REPO-OWNERSHIP, RECORD-LINKS, PMO-CODE, REPORT-SHAPE and what is left of RESTART-ORDER (SoP, Mac Studio setup and Knowledge acquisition).
  - Cut to one-line pointers, because the full decision now lives elsewhere: CHEZMOI-APPLY, HARNESS-PATHS, DIAGRAMS-EXPORT, UPDATE-SHAPE, QUIET-146, PMO12-LEVEL, IDENTITY-TIMING, COMPOSE-REPLY-BLOCK, RIG-DOCK-MISSING, and RIG-FIREWALL-RANGE together with RIG-LINUX-RANGE.
  - Removed every other entry, because a record, a standard, a release or a later entry now fully covers it. That includes REPLY-FORMS, SESSION-IDENTITY of 22:06, HARNESS-ACCEPT, batch 5, the typed MGIT-FLAGS answer, the work-folder skill messages, the Observatory batch, and every entry from 10:56 to the 17:39 resume.
- **Work file:** I rewrote the next steps to show where things stand now: two runs going, nine reports waiting for you to receive them, one report kept for its open query, and nothing queued or otherwise owed.
- **Commit:** `725809c` in ki-principal. The commit-gate audit passed with no failures. It is pushed fast-forward after a rebase pull. Another session's commit `9d31583` (`docs(work): ki.observatory receive from owner, answers and glyph`) was sitting under mine and went up with it, which the authority covering ki-principal allows.
- **Records:** no record was added or removed in any repository.
- **Report location:** the run's own instructions say to write this report only to the agent state folder. So nothing was written or committed at `$D/mark-prune-2.report.md`.

## In Progress

- **estate-deps** is running the harness gate on its template change.
- **cli-conventions** is writing the command-line conventions into `ki-repo-tools`.

Outstanding - no action requested now:

- The work file's Parked section still lists the 13 queries you answered in the recap batch (see PARKED-STALE). I left it alone because the brief limited me to the next steps.
- Another session's untracked file is in ki-principal: `+/_WORK/ki.chezmoi/publish-first-step.report.md`. I did not touch it. `+/_WORK/ki.chezmoi/decisions.md` has no uncommitted changes any more.
- Some lines I kept unchanged still mention a record ID without a link: KI-TOOL-RIG-CORE-061 is no longer in tools-rig's roadmap, and KI-TOOL-KI-CLI-147 is done. They were unlinked before this run too.

## Queries

### LAUNCH-REPORT-PATH - bring forward the launcher's report-path fix

**Context:** The work-folder-rename run asked this at 11:27 BST. The decisions log never records an answer, and the 12:40 BST hold did not park it. The `ki agent launch` refusal and the state-folder report path are still unbuilt and at triage in [KI-TOOL-KI-CLI-150](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-150-work-folder-entry-points.md). Until they are built, launches keep filling the work-folder report path, and the run instructions have to override it.

**Query:** Should the launch part of KI-TOOL-KI-CLI-150 be planned and delivered ahead of the rest of that record?

**Options:**

a) (recommended, confidence medium - the change is small, and every brief currently contradicts the standard) Yes. Plan and deliver the launch part first, with the run-prompt wording in the harness, in the next tools-ki release. Then delete the work-folder-rename report.

b) No. Leave it inside KI-TOOL-KI-CLI-150 for normal planning, and delete the work-folder-rename report now as overtaken.

### PARKED-STALE - clear the answered queries from the work file's Parked section

**Context:** The Parked section of the [ki.ways-of-working work file](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/work.md) still lists MGIT-QUIET-RULES through CHANNEL-TELEMETRY. You answered all of them at 17:59 BST. Under the work-folder standard, Parked should hold only queries that are still parked.

**Query:** Should the coordinator replace the Parked section with the queries that are actually still parked?

**Options:**

a) (recommended, confidence high - each answer is read back in the kept recap-batch entry) Yes. At its next send, keep only the PAPERCLIP-REQ hold and the Markdown-flavour note of 9 October, and drop the answered tags and the historical answered and overtaken lists.

b) Leave it as it is until the work is next put on hold.

### 🤖 → 👤 Handoff to supervisor · since 18:56 BST

🤖 2 running · 👤 2 with you

- [running] estate-deps · run/estate-deps · since 18:53
- [running] cli-conventions · run/cli-conventions · since 18:54
- [with you] LAUNCH-REPORT-PATH · owner · since 18:56
- [with you] PARKED-STALE · owner · since 18:56
- [committed] work folder, pushed
