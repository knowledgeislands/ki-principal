# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › migrate-apply

**🤖 → 🧑 Handoff to supervisor · Run report at 04:47 BST · last mark 04:39 BST**

---

## Done

- Phase 3 is applied in Knowledge Islands Principal and pushed. The commits are `f5c888d` (defer list), `25e2bfd`, `aa3c788`, `d2e3c2e`, `58bc680`, `319c169` and `9906b82` (capital steps 1-6), and `b1be9ac` and `dc571b1` (plan fixes). The hand steps are `2990311`, `b540311`, `7f663a3`, `c3802db`, `44656a1` and `6fb5599`. Two other sessions' commits sat beneath mine and went up with them: `05fd137 docs(work): note the release number`, in the decisions log, and `2173d1f docs(work): add the migrate-phase2b run report`.
- The theme pages follow the theme-page standard. Foundations, Techne, Model and Rig each carry a Direction and Notes and no lifecycle or lead. None of them lists Projects, records or work folders. `Streams/Themes/Themes.md`, `Streams/Streams.md`, `Streams/Projects/Projects.md` and `Streams/Roadmap/Roadmap.md` now say theme rather than Initiative.
- Briefings, Schedule and Tending each name `ki.regular` as their home.
- The Project notes have their old sections moved under `## Notes` and their links into work folders removed.
- The Mac Studio work is merged:
  - The `hosts.md` table now lives in [Hosts, Roles and Layers](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Engineering Practice/Architecture/Hosts, Roles and Layers.md>).
  - The decisions in force now live in [mac-studio-setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup.md). Both source files are deleted.
  - I reconciled the decisions log: apart from `<url>` formatting, the machine-local log matches the tracked one, so the tracked log is canonical. I left the machine-local file alone.
- Links to deleted reports in three work files and four Project notes now point at each report's last revision on GitHub, marked "(deleted)".
- I restored the MIGRATED origin line in all eleven migrated work files after step 6 had rewritten it. The link rewriter now skips those lines.
- The tools-burndown resume path is now [`ki.tools-burndown`](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/work.md), at `+/_WORK/ki.tools-burndown/work.md`. Its FIRST-STEP line is in `## Messages` with its content kept, and points at that file. Its resume line reads: `Resume KI > Foundations > Tools burndown from its work file, +/_WORK/ki.tools-burndown/work.md, under current ki-pmo and ki-delegation since 2026-10-18T02:55:00Z: re-bootstrap, read the pick-up block, take stock, put the parked queries back, restart authorised work, then banner.`
- `.github/ki-version` is bumped to `v0.11.0`, the released ki (GitHub release published 03:39Z, Homebrew tap at v0.11.0), in `a87d68e`. I cut no fix release because the apply hit no ki bug.
- KI Agentic Harness, `dc7d009a`:
  - skill-reviews moved to [`ki.regular.skill-reviews`](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/+/_WORK_REVIEW/ki.regular.skill-reviews/work.md) for review, and the review area has its index note.
  - The `+/_CHECKPOINTS` scaffold is gone.
  - Records HK-002, HK-003 and HK-005 name `theme: foundations`.
  - Pushed.
- KI Agentic Harness, `80144e72`: [KI-HARNESS-GOV-202](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-202-skill-area-stable-stats-badge.md) now links to the moved decisions log. [KI-HARNESS-GOV-198](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-198-reply-forms.md) still names the old path, as an audit result from the time, and I left it as history. Pushed.
- tools-rig, `30fbebf`: thirteen roadmap records name `theme: rig`. Pushed. tools-rig was level with origin, so no other session's commits went up with it.
- Plan bugs fixed in the plan copy, carried in `b1be9ac` and `dc571b1`:
  - Step 5 dropped "Parked queries" sections.
  - The step 2 and step 4 subjects were in sentence case.
  - `05 --map` failed once the old areas were gone.
  - `rewrite-links.pl` rewrote MIGRATED lines.
- Audits in Knowledge Islands Principal (`07-checks.sh --apply`):
  - ki-repo-kb, ki-repo-kb-streams and ki-decision-records: no FAIL. They give 4, 4 and 3 warnings.
  - ki-checkpoint passes.
  - ki-pmo: 34 PMO-7 failures across 32 reports. Every one of those reports is byte-identical to its pre-move version, so this is the link debt LINK-DEBT leaves to each work's first mark.
  - The whole-repository audit adds an SCR-11 failure on `.husky/pre-commit`. It comes from the `--quiet` flag in `f834a0e`, of 17 October, not from the move.
- `ki work status` reports WORK=9, ON_HOLD=8, REVIEW=5 and STUCK=1. The stuck entry is `ki.ways-of-working`, held by agent since 03:30Z.
- Whole-repository audits elsewhere:
  - tools-rig: no FAIL.
  - KI Agentic Harness: three FAILs, none from the move. They are MD051 (a missing `project-close` fragment cited by [KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md)), CAP-2 (a stale `skills/README.md` catalogue after the ki-pmo commits) and SCR-11 (the same pre-commit `--quiet` shape).

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Each moved work fixes its PMO-7 report links and prunes at its first mark (PMO-9 warns on seven work folders). [`ki`](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/work.md) also cuts its carried State of play at that mark.
- The [paperclip-capture-and-rebuild](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/paperclip-capture-and-rebuild.md) Project note still links `[[paperclip-rebuild-structure]]`, in a work folder's `design/`. I left it for that work's review.
- `ki.ways-of-working` shows as stuck in `ki work status` until its coordinator writes its next beat. That file is not mine to edit.
- STREAM-10 warns that chezmoi, mac-studio-setup, paperclip-capture-and-rebuild and website have no open records. Each needs a close-out assessment or its next work.
- Records [ADR-KI-PRINCIPAL-004](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-004-provider-neutral-isolated-agent-execution.md) to 006 appear after 007 in [Decisions](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/Decisions.md), so INDEX-8 warns.
- In the harness, MD051 and CAP-2 belong to the sessions behind the ki-pmo commits. SCR-11, in both repositories, belongs to whoever owns the commit-gate shape.
- The empty `+/_THREADS/` directory is left in Knowledge Islands Principal, because `ki agent status` still records this run's path there. No new file has landed in it.
- `desk-kit` stays on the defer list. Its folder no longer exists.

## Queries

### MIGRATE-CALLS - confirm the migrate-apply judgement calls

**Context:** These calls fell inside the pre-approvals, so I took the recommended course on each and recorded it as provisional.

1. I took chezmoi off the defer list: its decisions log had been committed at the 04:07 baseline, and no chezmoi agent was running.
2. I dropped Foundations' recurring-upkeep paragraph from its theme page. No Capital Activity describes that upkeep, and the harness housekeeping records name the theme instead.
3. I removed the links from Project notes into work folders, keeping only the Paperclip design link.
4. I treated the tracked Mac Studio decisions log as canonical and the machine-local copy as superseded.
5. I left the GOV-198 audit-result line naming the old skill-reviews path, as history.

**Query:** Do you confirm these five provisional calls?

**Options:**

a) (recommended, confidence high - each follows the brief's pre-approved options, and Git holds every prior text) Confirm all five as taken. b) Name any you want reversed, and a follow-up run reverses it.

### 🤖 → 🧑 Handoff to supervisor · since 04:47 BST

🧑 1 with you · 🏁 run finished

- [with you] MIGRATE-CALLS · owner · since 04:47
- [committed] ki-principal, ki-agentic-harness and tools-rig, pushed
