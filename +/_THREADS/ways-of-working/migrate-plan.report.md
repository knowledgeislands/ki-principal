# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/knowledge-islands-model/knowledge-islands-model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working/ways-of-working.md) › migrate-plan

**🤖 → 🧑 Handoff to supervisor · Run report at 03:22 BST · last mark 02:28 BST**

---

## Done

- The plan for phases 3 and 4 is in [migration-plan](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/migration-plan/README.md), committed as `2c6c57a`. Nothing outside the plan folder and this report was changed.
- **Scripts.** Seven Capital steps, plus one script each for ki-agentic-harness and tools-rig. Each is a dry run unless given `--apply`, and an apply commits only the paths it touched.
  1. [01-design-tidy.sh](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/migration-plan/capital/01-design-tidy.sh>) moves the design folders out of Streams.
  2. [02-themes.sh](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/migration-plan/capital/02-themes.sh>) turns the Initiatives into `Streams/Themes/`, with their wikilinks and the Work Process tree.
  3. [03-projects.sh](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/migration-plan/capital/03-projects.sh>) makes the Project notes flat and gives each a `theme:`.
  4. [04-activities.sh](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/migration-plan/capital/04-activities.sh>) gives the Activities their `theme:`.
  5. [05-work-folders.sh](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/migration-plan/capital/05-work-folders.sh>) turns checkpoints and thread folders into work folders, in the closed work-file form.
  6. [06-citations.sh](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/migration-plan/capital/06-citations.sh>) rewrites every live citation of a moved path.
  7. [07-checks.sh](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/migration-plan/capital/07-checks.sh>) runs the audits.
  - The territory scripts are [harness.sh](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/migration-plan/territory/harness.sh>) and [tools-rig.sh](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/migration-plan/territory/tools-rig.sh>).
- **Classification.** The [classification](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/migration-plan/classification.md>) sorts 14 pieces of work.
  - 9 are confident. 7 of these move on the first apply. `ki.tools-burndown` and `ki.chezmoi` are held while their sessions have them in flight.
  - 5 go to `+/_WORK_REVIEW/` for your review: `ki.baseline-rollout`, `ki.estate-factorisation`, `ki.agent-host`, `ki.regular.command-centre` and `ki.paperclip-capture-and-rebuild`.
- **Dry runs.** All 9 scripts were run as dry runs from their repositories, and each finished cleanly. Each saved its output beside it as `<script>.dry-run.txt`. Nothing was staged or changed in ki-principal, ki-agentic-harness or tools-rig.
- **Full apply in a throwaway clone.** Steps 1 to 6 ran for real in a clone and made 6 commits, touching 135 files and leaving a clean worktree. This produced the full `+/_WORK`, `+/_WORK_REVIEW` and `Streams/Themes` layout, with the held rows left where they were. The test found three bugs, now fixed:
  - Citations of paths that earlier steps had already moved were not rewritten.
  - Links to folders ending in a slash were not rewritten.
  - An index note in `+/_WORK/` breaks the new checker's rule that the area holds only work folders, so that note is no longer created.
- **Citations left after the clone apply: 22.**
  - The held chezmoi and tools-burndown paths.
  - Links to reports that had already been deleted before the migration. There are 20 such links; they are listed, and left as they were.
  - Two mentions of folders that were already removed.
- **Audits on the migrated clone.**
  - ki-repo-kb, ki-repo-kb-streams and ki-decision-records: no failures.
  - ki-checkpoint: 6 failures, all on the held tools-burndown checkpoint. The live Capital has the same failures today.
  - ki-pmo: 37 failures. 6 are those same tools-burndown ones. The other 31 are record-identifier links in reports: 12 in the new work folders and 19 in the held chezmoi and tools-burndown thread folders. The audit does not report these on today's layout.
- **Mechanical and by-hand steps.** Every move is mechanical. So are:
  - the conversion of the old files into work files;
  - the change from `initiative:` to `theme:`;
  - the wikilinks, the tree and the citations;
  - the audits.
  - What is left for hand is listed at the end of each dry run: 21 items in the Capital and 4 in the territory, such as rewriting theme pages as theme pages, merging `hosts.md` and reconciling the decisions log for Mac Studio setup.
- **Other territory repositories.** The [territory list](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/migration-plan/territory/territory.md>) covers them.
  - ki-agentic-harness and tools-rig have scripts.
  - tools-ki changes come with its phase-2 code. Another session has tools-ki in the middle of a rebase, with [KI-TOOL-KI-CLI-139](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-139-ebu-sources-sync.md) unmerged.
  - apps-knowledgeislands.info follows tools-ki.
  - mcp-m365 and mcp-gsuite wait for the Humans Not Robots migration.
  - The 13 others need nothing.
- **Other sessions' work, left alone.**
  - In ki-principal: `+/_CHECKPOINTS/rig.chezmoi.md`, `+/_THREADS/chezmoi/`, `+/_THREADS/tools-burndown/` and its checkpoint. `+/_THREADS/desk-kit/` no longer exists.
  - In ki-agentic-harness: 14 ki-checkpoint standard files.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Applying the plan waits on tools-ki: it must accept `theme` on records and ship `ki work status`. It also waits for the ki-checkpoint work-file standard, now in flight in ki-agentic-harness, to be committed.
- The chezmoi and tools-burndown rows stay held until their sessions land. Then their `defer.list` lines come out, and steps 5 and 6 run again.
- At its first mark, each work prunes its settled reports and cuts its MIGRATED work file down.

## Queries

### SECTIONS-DROP - Dropping the old checkpoint sections

**Context:** Step 5 builds each new work file from the old checkpoint's pick-up block, Next step and Open questions. It drops Objective, Current state, Decisions made and Files touched; Git keeps them, and a MIGRATED line in Messages names the old path.

**Query:** Should the conversion drop those four sections, rather than carry the whole old body until the work's first mark?

**Options:** a) (recommended, confidence medium - the work file stays inside the closed form from the start, and Git holds the rest) Drop them, as the scripts do now. b) Carry the whole body under Next steps and let each work cut it at its first mark.

### STRAYS-DESIGN - Where files outside the closed list go

**Context:** Some thread files fall outside the work folder's closed list, for example state-of-play's `themes/` and `observatory-goals/`, ways-of-working's diagrams and this plan, and the tools-burndown evidence files. Step 5 moves each into the work folder's `design/` and names it. The Mac Studio files also go to `design/`, not to the folder root as the brief said.

**Query:** Should these files go to `design/`, leaving each work's first mark to home or delete them?

**Options:** a) (recommended, confidence medium - `design/` is the only place in the closed list that admits them, and no file is lost) Move them to `design/`, as scripted. b) Leave them in the old thread folders until each owning work clears them by hand.

### LINK-DEBT - Report links the new layout exposes

**Context:** After the migration, the ki-pmo audit flags 31 record-identifier links in reports, 12 in migrated work folders and 19 in the held ones. Separately, 20 links point at reports that were deleted before the migration; the scripts list these and leave them as they are.

**Query:** Should the reports be fixed by each work's first-mark prune, rather than by a further mechanical script?

**Options:** a) (recommended, confidence medium - most of the flagged reports are settled, so the Work Process prune deletes them and only a few are left to fix) Leave it to each work's first mark, and fix by hand whatever survives. b) Add a step 8 that rewrites dead report links to GitHub links at the file's last revision, and links bare record identifiers where the file can be found.

### REVIEW-SPLIT - The five pieces of work for review

**Context:** Five pieces of work go to `+/_WORK_REVIEW/`, each with its reason in that area's index note:

- `ki.baseline-rollout`;
- `ki.estate-factorisation`, which has no thread;
- `ki.agent-host`, whose thread is `+/_THREADS/techne/`;
- `ki.regular.command-centre`, a decisions log with no checkpoint;
- `ki.paperclip-capture-and-rebuild`, which has design papers only.

In the harness, `skill-reviews` likewise becomes `ki.regular.skill-reviews` in review.

**Query:** Do you accept this split between confident and review?

**Options:** a) (recommended, confidence medium - each has no live checkpoint, an unclear owner or is under the Techne Programme Hold) Accept it, and review each folder as it next comes up. b) Name the items to promote to `+/_WORK/` or to finish before the apply.

### APPLY-TRIGGER - When to apply

**Context:** The scripts are ready to run, but the new layout is valid only once tools-ki reads `Streams/Themes/`, accepts `theme` and ships `ki work status`. tools-ki is in the middle of another session's rebase. The apply copies the plan to `tmp/` first, then runs steps 1 to 7 with `--apply`, from a clean index.

**Query:** Should the apply wait for the tools-ki release and then run as one batch in the Capital, followed by the harness and tools-rig?

**Options:** a) (recommended, confidence high - each step commits only its own paths and holds anything another session has in flight) Wait for the tools-ki release, then apply the Capital, the harness and tools-rig in that order, and do the hand steps after. b) Apply step 1 now, since it only moves design folders, and the rest after the release.
