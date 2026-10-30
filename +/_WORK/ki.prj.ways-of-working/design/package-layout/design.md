---
note_type: streams/design
status: draft
work: ki.prj.ways-of-working
run: ki-prj-ways-of-working
agent: package-layout
written_at: 2026-10-30T06:50:00Z
---

# Work-package layout

**Owner:** Kris Brown - **Work:** `ki.prj.ways-of-working` (KI > Model > Ways of working) - **Date:** 30 October 2026 - **Status:** draft for the owner's sanity check. Nothing has been moved, and no standard, skill, tool or record has been changed.

## The direction

Kris set three standing directions on 30 October 2026 at 06:15 GMT, recorded in [decisions.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/decisions.md):

- **PACKAGE-LAYOUT:** each work package has only five top-level files, `work.md` the entry point and its siblings `decisions.md`, `messages.md`, `queries.md` and `state.md`; everything else goes in subfolders, grouped by the thing that produced it, possibly group first with briefs, design and reports beneath: "it could be that we need a different dimension, which is the grouping first".
- **REVIEW-INDEPENDENCE:** "blind reviews ... must not really be concerned with previous decisions too much, and they must be able to challenge those, so we can make sure that we haven't gone down a particular avenue incorrectly".
- **READ-EXPLORE:** Kris needs a way to read, explore and feed back on useful artefacts; "the observatory is a means to be able to achieve this at some point".

This note treats those directions, and the standards they would change, as evidence rather than constraints, under REVIEW-INDEPENDENCE itself.

## What the evidence shows

As of 06:29 GMT on 30 October 2026. Other sessions were writing into the package while this note was drafted, so the counts move; the migration run re-lists the folder before it starts.

- **Volume.** Beyond the five package files the folder holds 240 files: 30 run reports at the top level, 102 files in `reports/`, 32 in `briefs/` and 76 in `design/`, one of them in the subject folder `design/host-sync/`. Thirty of the top-level reports are untracked: the launcher has homed them and the coordinator has not yet received them.
- **The standard puts reports at the top level.** The `ki-work-package` [closed list](/Users/krisbrown/.local/share/ki/harnesses/knowledgeislands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md#closed-list) names the run report as `<name>.report.md` in the folder itself, briefs as `briefs/<run>.md` and design notes as `design/<slug>.md` or `design/<subject>/`. PACKAGE-LAYOUT therefore changes the standard, not only this folder's habits.
- **Reports reach the top level by design.** A run writes its report only to its state folder; when the run writes `DONE`, the launcher's `homeReport` copies it to `<package>/<name>.report.md` (`tools-ki` [events.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts), `reportPath` in [thread.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/thread.ts)), under Kris's 14 October 2026 rule "make the launcher the only writer of the thread folder's log and report files". `refuseWorkReport` in [runs.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts) refuses a brief that sends a report into a work folder itself. The top level is where every report lands; it fills up whenever receipt and tidy fall behind.
- **`reports/` is outside the closed list and partly invisible to Git.** It was created in the hold commit `515b2adf` on 29 October by moving 100 received reports out of the top level. The `ki-repo` managed block in the root `.gitignore` ignores `reports/` at any depth, so those 100 stay tracked only because they were moved as tracked files. Two later files there, `receive-more.report.md` and `z-session-retirement-20261030.md`, are untracked and do not show in `git status`; the `receive-sol` run had to force-add past the rule. The rubric's FOLDER-1 (`workFolderStray` in [work-folder.ts](/Users/krisbrown/.local/share/ki/harnesses/knowledgeislands/ki-agentic-harness/skills/governance/ki-work-package/scripts/rubric/contexts/work-folder.ts)) admits only `findings/`, `briefs/`, `feedback/` and `design/` as folders, so it fails `reports/`.
- **Several readers assume the top level.** In `tools-ki`: `takenBy` and the relaunch guard in `runs.ts`, `adoptStateFiles` and the option lookup behind `ki agent decide` in `thread.ts`, and the reviewer-report check in [selection.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/selection.ts). In the rubric, FOLDER-3 finds a received brief by a top-level `<run>.report.md`. In the Observatory, [work.ts](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/work.ts) reads each work's newest top-level `*.report.md`, and its reader opens only a top-level report or a `design/` note. The reports already moved to `reports/` have disappeared from all of these.
- **Most of the sprawl comes from retention, not layout.** 25 of the 32 briefs have their run's report beside them, so they are FOLDER-3 tidy candidates. The `wow-prune-reports-2` run reviewed 67 reports and pruned three. `state.md` has carried "Prune received reports and spent briefs at the next mark" across marks. Putting files into subfolders without changing when they leave just moves the sprawl down a level.
- **A group-first shape already exists in part.** The closed list allows `design/<subject>/`, and `design/host-sync/` uses it, with `brief.md`, `review-claude.md`, `review-codex.md` and now `report.md`. Elsewhere, design-loop artefacts share a slug prefix (`landscape-*`, `model-shape-*`, `coord-any-package-*`), and run names mostly carry the same prefix as the matter they serve.
- **Links point in from outside.** Inside the package, `decisions.md` holds 23 relative links into `design/`, `briefs/` or `reports/`, `queries.md` 11 and `state.md` one. Outside it, the [Ways of working Project note](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) links three times into the work folder, though the Project registry standard says a Project note never points into one. [KI-PRINCIPAL-MOD-011](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-MOD-011-amend-work-model-assigned-package-cascade.md) also links three times, and so do lines in the `messages.md` of ki.prj.tools-burndown, ki.prj.orca-evaluation, ki.prj.chezmoi and ki.prj.baseline-rollout, plus ki.sop.main's decisions log and one of its design notes.
- **The pattern runs across the estate.** ki.prj.observatory's folder shows the same flat sprawl, with about thirty top-level reports.

### Where this note differs from the direction

1. **Agree:** five top-level files. The evidence supports it: the top level is where receipt lag and tidy lag both show up, and readers lose the package files among the reports.
2. **Partly differ:** "briefs, design and reports beneath" each group. Most groups would hold one to three files, so a subfolder per kind triples the depth for little gain, and any folder named `reports/` collides with the estate-wide ignore rule. A flat group, with the kind shown by the file suffix, keeps the grouping Kris asked for without either cost.
3. **Add:** a group-first layout pays only if the group also becomes the unit of tidy, so that closing a group deletes it in one commit. Without that, the cheap kind-first fix is the better buy.
4. **Add:** the Project note's links into the work folder already break the registry rule. The migration is a good moment to replace them with quoted words.

## 1. Candidate layouts

| | A. Kind-first | B. Group-first, kind subfolders | C. Group-first, flat (recommended) |
| --- | --- | --- | --- |
| Top level | Five files; `reports/`, `briefs/`, `design/`, `findings/`, `feedback/` | Five files; one folder per group; `findings/`, `feedback/` | Five files; one folder per group; `findings/`, `feedback/` |
| A matter's material | Spread across three folders, joined only by slug prefix | One folder, three subfolders | One folder, flat |
| Run brief and report | `briefs/<run>.md`, `reports/<run>.report.md` | `<group>/briefs/<run>.md`, `<group>/reports/<run>.report.md` | `<group>/<run>.brief.md`, `<group>/<run>.report.md` |
| Design artefacts | `design/<slug>-*.md` | `<group>/design.md`, `<group>/brief.md`, `<group>/review-<reviewer>.md` | Same as B |
| Ignore rule | Needs a `ki-repo` exception for `+/_WORK/**/reports/` | Needs the same exception | No change |
| Unit of tidy | File by file, as today | Group, or file by file | Group, or file by file |
| Change cost | Smallest: the launcher's target folder, the rubric, the Observatory and the ignore rule | Largest: C's changes plus the ignore exception and deeper paths | Medium: launcher, rubric, Observatory and four skills |

### A. Kind-first

```text
+/_WORK/<id>/
  work.md  state.md  queries.md  messages.md  decisions.md
  briefs/<run>.md
  reports/<run>.report.md
  design/<slug>.md | design/<subject>/
  findings/<tag>.md
  feedback/<date>-<slug>.md
```

There are no groups, so nobody chooses one; matters are tied together only by the slug prefix the coordinator gives run names and design notes. Runs do not change: a run writes its report to its state folder, and the launcher homes it in `reports/` instead of the top level. This layout meets the five-file rule and nothing more. A matter stays spread across three folders, and the tidy stays a file-by-file judgement, which is where the evidence says the sprawl comes from.

### B. Group-first with kind subfolders

```text
+/_WORK/<id>/
  work.md  state.md  queries.md  messages.md  decisions.md
  findings/<tag>.md
  feedback/<date>-<slug>.md
  <group>/
    brief.md  design.md  review-<reviewer>.md  explainer.md   (design-loop artefacts, where the group is a design)
    briefs/<run>.md
    reports/<run>.report.md
```

This is Kris's sketch taken literally. Group choice and run routing work as in C below. Its costs are depth, since most groups' `briefs/` and `reports/` would each hold a single file, and the `reports/` name: every group's `reports/` folder is ignored unless the `ki-repo` managed block adds `!/+/_WORK/**/reports/`. That exception was tested in a scratch repository and does re-include the folder while still ignoring `reports/` elsewhere, but it is an estate-wide change to a managed block for a naming choice.

### C. Group-first, flat (recommended)

```text
+/_WORK/<id>/
  work.md  state.md  queries.md  messages.md  decisions.md
  findings/<tag>.md                 (unchanged: read at every pick-up, steward-written)
  feedback/<date>-<slug>.md         (unchanged: the Observatory's entry point)
  <group>/
    brief.md  design.md  review-<reviewer>.md  explainer.md   (design-loop artefacts, plain names)
    <run>.brief.md                  (run brief; a masked packet is <run>.packet.md)
    <run>.report.md                 (homed by the launcher)
    *.architecture.json  *.mmd  *.svg  *.html   (diagram sources and renders)
```

- **What a group is.** A group is the matter that produced the files: a design loop, a study, a migration, or a run of query reviews. Its name is a lower-case kebab slug naming that matter, such as `host-sync`, `landscape` or `state-machine`, never a date, host or run name. A design loop's slug becomes its group, so `design/<slug>-brief.md` becomes `<slug>/brief.md`. Reserved names: `findings`, `feedback`, and, through the tolerance window, `briefs`, `reports` and `design`.
- **Plain names and run suffixes.** Design-loop artefacts take plain names, and run artefacts take `<run>.<kind>.md`, so a brief and its report sort together and FOLDER-3 checks for a sibling. A design loop's own decisions stay in the package's `decisions.md`, so no group holds a second `decisions.md`, which the `ki agent close` gate would otherwise have to tell apart.
- **Who chooses the group.** The work's steward, normally the coordinator, chooses it when writing the brief: an open group if the run serves that matter, or a new slug if it opens one. Kris may name or merge groups at commission or at a mark. A run never chooses its group. Short operational runs, such as receipts, syncs and tidies, share one standing `ops/` group, which every mark empties.
- **How a run knows where to write.** The brief's location carries the group. The steward writes the brief to `+/_WORK/<id>/<group>/<run>.brief.md`, and `ki agent launch` takes the group from the brief's folder, with a `--group` override, and records it in `launch.json`. The run itself changes nothing: it writes its report only to its state folder, and any design note only to the exact path its brief names inside the group. The launcher homes the report as `<group>/<run>.report.md`. A brief left at `briefs/<run>.md` keeps today's behaviour, with a warning, through the tolerance window.
- **How a group leaves.** A group is open while any of its artefacts is live. It closes when every outcome it carried has a durable home, every query has been copied into `queries.md`, and every design note has graduated or been recorded as superseded. That judgement stays the steward's under `ki-coordination`. The steward then deletes the whole group with `git rm -r -q -- <group>/`, naming the folder explicitly, in one commit. This narrows today's "never folder-wide delete" rule to one named, closed group. Single files may still go one at a time, as now.
- **What readers see.** The top level shows the five files, `findings/`, `feedback/` and one folder per live matter, so the folder list doubles as the list of open matters. `state.md`'s Next steps names a group when it needs one read, as it names reports today.

## 2. What changes, and the lines to send

These changes follow from C; under A or B the same owners change less or more, as the table above shows. Nothing is sent until Kris decides LAYOUT-SHAPE.

The method skills are this work's own, since `work.md` scopes in "the work package and its migration, `ki-coordination`, `ki-delegation`". Their changes are therefore this work's rollout under `ki-work-design` (records captured in the KI Agentic Harness from the decisions), not messages to another owner:

- **`ki-work-package`:** the closed list replaces the top-level `<name>.report.md` and `briefs/<run>.md` with group folders and their kinds. The entry-point table makes the launcher write `<group>/<run>.report.md`. Tidy's "How" admits `git rm -r` of one named, closed group. Progressive reveal level 4 reads groups. FOLDER-1 accepts group folders holding the listed kinds; FOLDER-3 checks for a sibling report; and a tolerance window covers the kind-first folders in the other fifteen packages.
- **`ki-delegation`:** the run packet's report-home sentence and the brief path become `<group>/<run>.brief.md`, homed by the launcher into the brief's folder, and the brief template names its group.
- **`ki-coordination`:** at each mark the steward reviews groups and closes the ones whose outcomes are homed, and the `ops/` group empties at every mark. The REVIEW-INDEPENDENCE amendment in section 4 also lands here, in the Query review section and the generated review-brief surface.
- **`ki-work-design`:** the artefact home moves from `design/<slug>-*.md` to `+/_WORK/<id>/<slug>/`, with graduation deleting the group's design files; the Streams prohibition is unchanged.

Message lines for owners outside this work, in the `messages.md` line shape, to send once LAYOUT-SHAPE is decided:

```markdown
- 2026-10-30 · PACKAGE-LAYOUT · KI > Model > Ways of working (ki.prj.ways-of-working): Kris set five top-level package files with everything else grouped. Please make `ki agent launch` take the group from the brief's folder (`<group>/<run>.brief.md`, `--group` override), home reports as `<group>/<run>.report.md`, and teach takenBy, relaunch, adoptStateFiles, decide and acceptance's reviewer check the group path. Design: <link>.
```

That line goes to ki.prj.tools-burndown, which owns every `tools-ki` change other works hand over.

```markdown
- 2026-10-30 · PACKAGE-LAYOUT · KI > Model > Ways of working (ki.prj.ways-of-working): work packages are moving to group folders, `+/_WORK/<id>/<group>/`, with run reports at `<group>/<run>.report.md` and design notes at `<group>/*.md`. The Work evidence and its reader read only top-level reports and `design/`; please make them group-aware, with tolerance for today's shape. Design: <link>.
```

That line goes to ki.prj.observatory.

```markdown
- 2026-10-30 · PACKAGE-LAYOUT · KI > Model > Ways of working (ki.prj.ways-of-working): the `ki-repo` managed ignore block's `reports/` matches inside work folders, so new files in `+/_WORK/<id>/reports/` go silently untracked; two do now in ki.prj.ways-of-working. Please route to the `ki-repo` owner: anchor the rule or add `!/+/_WORK/**/reports/`. Needed under layout B; a hazard either way. Design: <link>.
```

That line goes to ki.sop.main, since no work package owns `ki-repo`; under C it is a hazard report rather than a prerequisite.

The Ways of working Project note's three links into the work folder are Capital content outside the package, so the migration replaces them with quoted words through this work's own Project-note update, not by a message.

## 3. Pilot migration of this package

This package is the pilot. Nothing below has been done.

1. **Preconditions.** Kris has decided LAYOUT-SHAPE and LAYOUT-PILOT-ORDER, and the harness closed list and FOLDER rubric accept groups, unless Kris takes the option of piloting ahead of them. No run of this work is writing into a file the move touches.
2. **Receive first.** The steward receives every untracked top-level report, copying its queries into `queries.md` as now, so that nothing is moved before it is received.
3. **Tidy before moving.** The steward runs its at-mark tidy: received briefs (25 at the snapshot), reports whose outcome is homed, and graduated or superseded design notes are deleted by explicit path where they stand. Only the survivors move. Moving a file only to delete it next week costs history readability and buys nothing. Most of `reports/` was moved there at the 29 October hold as already received, so most of it is a tidy candidate, but that judgement stays the steward's.
4. **Settle the anomalies.** `receive-more.report.md` exists twice, byte-identical, at the top level and in the ignored `reports/`; one copy goes. `receive-sol.report.md` exists twice with different contents, and the steward keeps the received, tracked copy unless the other adds to it. Three untracked files may hold protected material: `public-report-review.report.md`, `sol-private-report-assessment.report.md` and `reports/z-session-retirement-20261030.md`. They stay uncommitted and outside the move until PUBLIC-REPORT-RECOVERY is answered, under the confidential rule and the existing Principal publication hold.
5. **Move the survivors in one commit.** `git mv` each tracked survivor into its group by explicit path, renaming as section 1 sets: briefs become `<run>.brief.md`, and design notes lose their slug prefix, with the main note becoming `design.md`. The same commit rewrites the links in `decisions.md`, `queries.md` and `state.md`, and `briefs/`, `reports/` and `design/` go once empty. Subject: `docs(work): ki.prj.ways-of-working group-first layout pilot`.
6. **Links from outside.** Lines in other works' `messages.md` and in ki.sop.main's files that link into the package are repointed to a pinned revision. A coordinator may do that itself as a one-line mechanical fix, or ask the owning work in a line. The Project note gets quoted words instead of links. KI-PRINCIPAL-MOD-011's links are repointed to a pinned revision, or the record quotes what it needs, as `ki-work-design` requires by `ready`.
7. **Until the launcher changes.** New reports still land at the top level. The steward moves each into its group at receive, in the receive commit, so the top level is clean after every receive.
8. **Check and learn.** Run the FOLDER rubric and open the package in the Observatory. Then write the lessons into the wave brief for the other fifteen packages before any of them moves.

### Mapping of every current non-package file

Snapshot at 06:29 GMT, 240 files. † marks a file untracked by Git; ‡ marks one untracked and ignored inside `reports/`. Paths are relative to the package folder.

| Group | What it holds | Files |
| --- | --- | --- |
| `acceptance/` | Closing and pruning reviewed records | `reports/accept-prune.report.md`, `reports/prune-held.report.md`, `reports/records-fold.report.md`, `reports/wow-accept-prune.report.md`, `reports/wow-close-done-2.report.md`, `reports/wow-close-done-3b.report.md`, `reports/wow-principal-records.report.md` |
| `change-management/` | Change-management design loop and its skills diagram | `design/change-management-brief.md`, `design/change-management-decisions.md`, `design/change-management-report.md`, `design/change-management-review-astra.md`, `design/change-management-review-fable.md`, `design/change-management-skills.architecture.json`, `design/change-management-skills.svg` |
| `checkout-isolation/` | Checkout isolation and worktree flow | `design/checkout-isolation.md`, `reports/checkout-iso.report.md`, `reports/ci-review.report.md`, `reports/worktree-flow.report.md` |
| `coord-any-package/` | Coordination-for-any-package design loop | `design/coord-any-package-brief.md`, `design/coord-any-package-report.md`, `design/coord-any-package-review-claude.md`, `design/coord-any-package-review-codex.md` |
| `coordination-method/` | Coordination rule changes, lessons, retro, take-stock and method feedback | `design/agent-control-contract.md`, `design/context-efficiency.md`, `design/coordination-lessons.md`, `design/method-feedback.md`, `design/method-lines.md`, `design/retro-2026-10-20.md`, `design/tags-model.md`, `design/take-stock-2026-10-20.md`, `design/tending.md`, `reports/banner-on-state.report.md`, `reports/drain-form.report.md`, `reports/glyph-drift.report.md`, `reports/take-stock.report.md`, `reports/wow-take-stock.report.md` |
| `estate-health/` | Releases, pins, CI, audits, CLI conventions and mgit | `design/mgit-cache.md`, `reports/bats-rule.report.md`, `reports/ci-red.report.md`, `reports/cli-conventions.report.md`, `reports/green-main.report.md`, `reports/ki-release.report.md`, `reports/mgit-learn.report.md`, `reports/pin-estate.report.md`, `reports/principal-audit.report.md`, `reports/wow-ci-pins.report.md`, `reports/wow-dryrun-survey.report.md`, `reports/wow-fleet-green.report.md`, `reports/wow-ki-pin-release.report.md`, `reports/wow-release-runs.report.md`, `reports/wow-rereview6-toolski-a.report.md` |
| `gfm/` | GFM migration | `design/gfm-migration.md`, `reports/gfm-convert.report.md`, `reports/gfm-scope.report.md` |
| `host-move/` | Host move, sol and terra sync, reconciles and clones | `design/stop-for-host-move.md`, `reports/restart-consolidate.report.md`, `reports/wow-move-procedure.report.md`, `reports/wow-move-prompts.report.md`, `reports/wow-sol-clone-2.report.md`, `reports/wow-sync-2.report.md`, `reports/wow-sync-terra.report.md`, `sol-estate-origin-preflight.report.md` †, `sol-reconcile-hnr.report.md` †, `sol-reconcile-legal.report.md` † |
| `host-sync/` | HOST-SYNC design loop | `briefs/host-sync-merge.md`, `briefs/host-sync-review-claude.md`, `briefs/host-sync-review-codex.md`, `briefs/host-sync-review.md`, `briefs/wow-host-sync-design.md`, `design/host-sync-and-reply-trades.md`, `design/host-sync-report.md`, `design/host-sync/brief.md`, `design/host-sync/report.md` †, `design/host-sync/review-claude.md`, `design/host-sync/review-codex.md`, `host-sync-review-claude.report.md` †, `host-sync-review-codex.report.md` †, `host-sync-review.report.md` †, `sol-host-sync-design.report.md` † |
| `landscape/` | Landscape study and its ORCA-FIT predecessor | `briefs/landscape-merge.md`, `briefs/landscape-review-claude.md`, `briefs/landscape-review-codex.md`, `briefs/landscape-revise.md`, `briefs/landscape-rollout.md`, `briefs/landscape.md`, `briefs/orca-fit.md`, `briefs/receive-landscape.md`, `design/landscape-explainer.md`, `design/landscape-report.md`, `design/landscape-review-claude.md`, `design/landscape-review-codex.md`, `design/landscape-skills-inventory.md`, `design/landscape-vendors.md`, `design/landscape.md`, `design/orca-fit-explainer.md`, `design/orca-fit.md`, `landscape-merge.report.md` †, `landscape-review-claude.report.md` †, `landscape-review-codex.report.md` †, `landscape-revise.report.md` †, `landscape-rollout.report.md` †, `landscape.report.md` †, `receive-landscape.report.md` † |
| `model-shape/` | Model-shape design loop | `design/model-shape-report.md`, `design/model-shape-review-claude.md`, `design/model-shape-review-codex.md`, `design/model-shape.md`, `reports/wow-model-shape.report.md` |
| `naming/` | Work id shape, naming rollout, territory rename and MOD-011 | `design/mod011-wording.md`, `design/naming-rollout-manifest.md`, `design/work-id-shape-plan.md`, `reports/territory-rename.report.md`, `reports/wow-mod011-approved-candidate.report.md`, `reports/wow-rev-principal-integrate.report.md` |
| `observatory-review/` | Observatory review-view proposal | `design/observatory-review.md` |
| `ops/` | Receives, tidies, drains and sweeps | `briefs/receive-more.md`, `briefs/receive-sol.md`, `receive-more.report.md` †, `receive-sol.report.md` †, `reports/design-triage.report.md`, `reports/receive-more.report.md` ‡, `reports/receive-sol.report.md`, `reports/wow-drain-tidy.report.md`, `reports/wow-extra-writes.report.md`, `reports/wow-hnr-tidy.report.md`, `reports/wow-prune-reports-2.report.md`, `reports/wow-tidy-night.report.md`, `wow-mark-followthrough.report.md` † |
| `overview/` | Project overview, skill set, findings, finish line and work-model diagram | `briefs/wow-finish-line.md`, `design/design.md`, `design/findings.md`, `design/finish-first.md`, `design/finish-line-plan.md`, `design/overview.md`, `design/review-pack.md`, `design/skill-set.md`, `design/work-model.architecture.json`, `design/work-model.svg`, `sol-finish-line-plan.report.md` † |
| `package-freshness/` | Package definition and session freshness design loop | `design/package-definition-freshness-brief.md`, `design/package-definition-freshness-report.md`, `design/package-definition-freshness-review-freshness.md`, `design/package-definition-freshness-review-portability.md` |
| `package-layout/` | This design | `briefs/package-layout.md` |
| `public-report/` | PUBLIC-REPORT-AUDIENCE and PUBLIC-REPORT-RECOVERY, Z retirement receipt | `briefs/public-report-review.md`, `public-report-review.report.md` †, `reports/z-session-retirement-20261030.md` ‡, `sol-private-report-assessment.report.md` † |
| `query-review/` | Masked blind reviews of owner queries and query sweeps | `blind-review-1.report.md` †, `blind-review-2.report.md` †, `blind-review-3.report.md` †, `briefs/blind-review-1.md`, `briefs/blind-review-1.packet.md`, `briefs/blind-review-2.md`, `briefs/blind-review-2.packet.md`, `briefs/blind-review-3.md`, `briefs/blind-review-3.packet.md`, `briefs/blind-review-4.md`, `briefs/mask-queries-2.md`, `briefs/mask-queries-3.md`, `briefs/mask-queries-4.md`, `briefs/mask-queries.md`, `briefs/orch-name-fresh.md`, `briefs/orch-name-update.md`, `briefs/worker-wait-split.md`, `design/query-sweep.md`, `design/unparked-queries.md`, `mask-queries-2.report.md` †, `mask-queries-3.report.md` †, `mask-queries.report.md` †, `orch-name-fresh.report.md` †, `reports/delete-review.report.md`, `reports/query-review-4.report.md`, `reports/query-review.report.md`, `reports/stash-review.report.md`, `reports/wow-review-deps.report.md`, `reports/wow-review-docs-red.report.md`, `reports/wow-review-sweep.report.md`, `reports/wow-review-tending-source.report.md`, `worker-wait-split.report.md` †, `wow-freshness-reminder-blind-20261029.report.md` † |
| `rig/` | Rig fixes and reviews | `reports/rig-fixes.report.md`, `reports/rig-lock-review.report.md`, `reports/wow-rig-attended-steps.report.md` |
| `roadmap-burn/` | Roadmap burn-down, sorting and harness record triage | `design/roadmap-sizing-and-burn-down.md`, `design/roadmap-sweep.md`, `reports/burn-ki-design.report.md`, `reports/burn-observatory.report.md`, `reports/burn-tools-ki.report.md`, `reports/burn-tools-techne.report.md`, `reports/burn-website.report.md`, `reports/gov197-hook.report.md`, `reports/harness-burn.report.md`, `reports/harness-followups.report.md`, `reports/harness-link-fix.report.md`, `reports/harness-moves.report.md`, `reports/harness-upkeep.report.md`, `reports/lane-triage.report.md`, `reports/review-gov194-201.report.md`, `reports/review-gov197.report.md`, `reports/wow-burn-plan.report.md`, `reports/wow-sort-roadmap.report.md` |
| `spec-drafts/` | Specification areas and drafts (ki.prj.portable-specifications owns the outcome) | `reports/spec-areas-design.report.md`, `reports/spec-drafts.report.md` |
| `state-machine/` | Work state machine and its rollout | `design/state-machine-rollout-plan.md`, `design/work-state-machine.html`, `design/work-state-machine.md`, `design/work-state-machine.mmd`, `design/work-state-machine.svg`, `reports/wow-sm-ends.report.md`, `reports/wow-sm-guards.report.md`, `reports/wow-sm-nested.report.md`, `reports/wow-sm-polish.report.md`, `reports/wow-sm-refine.report.md`, `reports/wow-sm-roles.report.md`, `reports/wow-state-machine.report.md`, `sol-state-machine-readiness.report.md` † |
| `storage-schema/` | Storage declaration schema and repository metadata | `design/gov-227-storage-schema.md`, `design/repository-metadata.md` |
| `unattended/` | Unattended windows, grants, overload and permission prompts | `design/interim-cover.md`, `design/overload-process.md`, `design/unattended-work.md`, `design/window-plan.md`, `reports/grant-drafts.report.md`, `reports/wow-night-audit-home-registries.report.md`, `reports/wow-perm-prompts.report.md` |
| `website-docs/` | Website documentation plan | `design/website-docs.md` |
| `work-package/` | Work package and work-folder design, rename and migration | `reports/agentspecs-scan.report.md`, `reports/fields-personal-principal.report.md`, `reports/ki-toml-switch.report.md`, `reports/no-alias-sweep.report.md`, `reports/reinstall-check.report.md`, `reports/report-sweep.report.md`, `reports/threads-fix.report.md`, `reports/work-folder-design.report.md`, `reports/work-folder-rename.report.md`, `reports/work-package-design.report.md`, `reports/work-package-review-fable.report.md`, `reports/work-package-standard.report.md`, `reports/wow-review-spec-orphan.report.md` |

At the snapshot the largest groups were `query-review` (33 files), `landscape` (24), `roadmap-burn` (18), `estate-health` and `host-sync` (15 each). Groups whose material is all received and homed, such as `acceptance`, `roadmap-burn`, `estate-health`, `rig`, `gfm` and `ops`, are expected to be deleted by the tidy in step 3 rather than moved. `spec-drafts` belongs to ki.prj.portable-specifications' outcome and is a tidy candidate here.

## 4. Review independence, as a proposed change to `ki-coordination`

Today's [Query review](/Users/krisbrown/.local/share/ki/harnesses/knowledgeislands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#query-review) masks the recommendation: the reviewer sees the Context and the Query with unranked options, and never reads `queries.md`, `decisions.md` or a report. It does not mask precedent. A Context routinely frames the question inside earlier owner decisions ("Kris set X on ..."), and an agreement lifts confidence whether the reviewer checked the evidence or only followed that frame. REVIEW-INDEPENDENCE asks for the second gap to close. Proposed amendments, in the standard's terms:

1. **Independence sentence (Query review, "The review").** Every review brief, whether a query review, a `ki-work-design` review or a merged report, carries in these words: "An earlier decision is evidence, not a constraint: you may recommend a course that departs from or reverses one, naming the decision and the evidence; agreement with an earlier decision earns no confidence by itself." The sentence becomes part of the generated review-brief surface, so that it cannot be left out.
2. **Neutral Context.** The masked Context states earlier owner decisions as dated facts, Kris's words with their date, and not as the premise of the question. The coordinator strips advocacy from the Context before masking, as it already strips the ranking.
3. **No lift from precedent alone (Query review, "Agreement"; owner report, confidence rule).** Confidence rests on reversibility and on what was verified directly. Consistency with an earlier decision is not a reason, and it earns no level. A review whose agreement rests only on an earlier decision or on the coordinator's framing is marked `reviewed, precedent only` and lifts nothing. An option a) whose only stated reason is an earlier decision is capped at `medium`.
4. **Challenge shown, never acted on (Query review, new "Challenge" bullet).** Where a review challenges an earlier decision with evidence, the query's Context ends with "review challenges <TAG> (<date>): <reason>", and an option to revisit that decision joins the Options. The coordinator never reverses a decision on a review's word; only Kris does, and the split rule still applies.
5. **Design reviews (`ki-work-design` review template).** The review template gains a "Challenges" section, between the Agree-Differ-Add marks and the summary, naming each owner decision or premise of the brief the reviewer would revisit, with evidence, or "none found". The merged report carries each challenge into its agree-and-differ table rather than settling it silently.

Points 1, 2 and 4 cost one sentence and one display rule each. Point 3 changes how confidence is earned and so affects every query, which is why it is asked separately below. The COORD-11 rubric cannot judge whether a reason is "precedent only", so that check stays a COORD judgement item; the presence of the independence sentence in a review brief can be checked mechanically.

## 5. Reading, exploring and feeding back

**Now.** The island is an Obsidian vault (it carries `.obsidian/`), so Kris can open a work folder there today and, under layout C, read one folder per matter: the explainer first, where the group has one, as the landscape and ORCA-FIT studies do, then `design.md` with its diagrams, then the reviews and reports beside it. Feedback today goes by speech in the thread, by tag or by group. The coordinator reads it back into `decisions.md` in Kris's words. For document feedback longer than an answer, the closed list's `feedback/<date>-<slug>.md` package is the right home. Its only writer today is "the owner, through the Observatory", whose `feedback-send` works where the Observatory is running and reads only top-level reports and `design/` notes. The small change is to let the owner write a feedback package by hand in any editor, or let the steward write one verbatim from Kris's spoken words, committed with one `messages.md` line exactly as the Observatory path does. That is one row in the entry-point table, asked as READ-FEEDBACK-NOW below.

**Later, through the Observatory.** ki.prj.observatory owns this, its priority and its plan; this work sends it one line. Most of the parts exist: the Work instrument's reader already opens reports and `design/` notes through the redacting prose tree; [PDR-KI-OBSERVA-007](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/decisions/PDR-KI-OBSERVA-007-feedback-returns-to-the-producing-work.md) returns document feedback to the producing work as a package and a `messages.md` line through the Bridge's `feedback-send`; and the draft [Observatory review-view proposal](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/observatory-review.md) adds a query reader with answer buttons. Group-first gives the Observatory a natural unit to browse: a work's open groups, each opening on its explainer and design, its reviews and reports in order, with paragraph-anchored comments gathered into one feedback package for that group and answers to queries sent as message lines. The Observatory line in section 2 carries the reader change; the group browser is a later line once the pilot has run.

## Queries

### LAYOUT-SHAPE - Which package layout to adopt

**Context:** Kris set on 30 October that a work package keeps only its five files at the top level, with everything else grouped, possibly group first with briefs, design and reports beneath. Three shapes fit. A, kind-first: `reports/`, `briefs/` and `design/` folders, the cheapest change, but a matter stays spread across three folders and the tidy stays file by file. B, group-first with kind subfolders, as sketched: one folder per matter with `briefs/` and `reports/` inside, which needs an estate-wide ignore exception because `reports/` is ignored at any depth. C, group-first and flat: one folder per matter, with `<run>.brief.md` and `<run>.report.md` side by side and design files under plain names, needing no ignore change. The evidence suggests the sprawl comes mainly from retention, so the group earns its cost only as the unit of tidy. No shape has been piloted.

**Query:** Which layout should the pilot use?

**Options:**

a) (recommended, confidence medium - the evidence favours the group as the unit of tidy, and C avoids the ignore collision, but nothing has been piloted) C, group-first and flat.

b) B, group-first with `briefs/` and `reports/` subfolders, plus the `ki-repo` ignore exception.

c) A, kind-first, with a stricter tidy cadence instead of groups.

### LAYOUT-GROUP-TIDY - Whether closing a group deletes it whole

**Context:** Today's tidy deletes file by file, by explicit path, never folder-wide, and the steward judges each file's durable home. Under a group-first layout, a matter's files usually become homed together. The proposal is that once the steward judges a whole group closed, with outcomes homed, queries copied and design notes graduated or superseded, it deletes the group with one `git rm -r` naming that folder, in one commit, with Git keeping the history. Single-file deletion remains available.

**Query:** Should the tidy rule allow deleting one named, closed group folder whole?

**Options:**

a) (recommended, confidence medium - it makes the group pay its way and Git keeps history, but it widens a deletion rule and is untested) Yes: a steward may delete one named, closed group in one commit.

b) No: keep file-by-file deletion inside groups.

### LAYOUT-PILOT-ORDER - When the pilot moves files

**Context:** The rubric's FOLDER-1 fails any folder outside the closed list, the launcher homes reports only at the top level, and the Observatory reads only top-level reports and `design/`. Piloting this package before those change gives evidence sooner but shows rubric failures and hides moved reports from the Observatory and `ki agent decide`. Changing the standard and rubric first is a small harness change; the launcher and Observatory changes belong to other works and would take longer.

**Query:** In what order should the pilot run?

**Options:**

a) (recommended, confidence medium - a small harness change first keeps the rubric honest, and moving received reports by hand at receive bridges the launcher gap) Change the closed list and FOLDER rubric first, then pilot this package by hand, receiving and tidying before moving, with launcher and Observatory changes following.

b) Pilot now, ahead of the rubric, and accept FOLDER-1 failures in this package until the harness catches up.

c) Wait until the launcher and Observatory changes have also landed.

### REVIEW-CHALLENGE - Let reviews challenge earlier decisions, visibly

**Context:** Kris asked on 30 October that blind reviews be free to challenge earlier decisions. Today's masked query review hides the recommendation but not the precedent in the Context. The proposal: every review brief carries a fixed independence sentence, generated so that it cannot be left out; the masked Context states earlier decisions as dated facts, not as premises; a review that challenges a decision is shown at the end of the Context with an option to revisit it, never acted on without Kris; and `ki-work-design` reviews gain a Challenges section.

**Query:** Should `ki-coordination` and `ki-work-design` adopt these four amendments?

**Options:**

a) (recommended, confidence high - each part only adds text or display, is reversible, and implements Kris's own words) Adopt the independence sentence, neutral Context, challenge display and design-review Challenges section.

b) Adopt only the independence sentence in review briefs.

### REVIEW-LIFT - Precedent earns no confidence

**Context:** Under the query-review rule, a blind review that agrees with a recommendation lifts its confidence one level. A review can agree simply because the Context framed the question inside an earlier decision. The proposal: agreement that rests only on an earlier decision or on the framing is marked `reviewed, precedent only` and lifts nothing, and an option whose only stated reason is an earlier decision is capped at medium. This changes how confidence is earned across every query, and it will send more queries to Kris at medium.

**Query:** Should precedent alone stop counting towards confidence?

**Options:**

a) (recommended, confidence medium - it follows Kris's direction directly, but it shifts confidence on every query and has no trial evidence) Yes: no lift from precedent-only agreement, and a precedent-only reason caps at medium.

b) No: keep today's lift rule, relying on the independence sentence alone.

### READ-FEEDBACK-NOW - Feedback packages before the Observatory can write them

**Context:** The closed list keeps owner feedback on documents as `feedback/<date>-<slug>.md` plus one `messages.md` line, and names only "the owner, through the Observatory" as its writer. Kris can read design notes in Obsidian today, but feedback longer than a spoken answer can be left only through the Observatory's `feedback-send`, which reads only top-level reports and `design/` notes and so loses sight of moved files until it is made group-aware. The proposal widens that row: the owner may write the package by hand, or the steward may write it verbatim from the owner's spoken words, committed with its message line in the same shape.

**Query:** Should feedback packages be writable now, outside the Observatory?

**Options:**

a) (recommended, confidence medium - it uses an existing kind and shape, but a steward writing on the owner's behalf needs the verbatim rule held) Yes, by the owner by hand or by the steward verbatim from the owner's words.

b) No: feedback stays spoken until the Observatory path is ready.
