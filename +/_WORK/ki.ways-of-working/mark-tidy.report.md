# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › mark-tidy

**🤖 → 👤 Handoff to supervisor · Run report at 18:21 BST · last mark 18:12 BST**

---

## Done

- Decisions log struck at the mark and pushed fast-forward in ki-principal as `09e3e775`, `docs(work): ki.ways-of-working strike decisions at mark`; only this work's commit was stacked. Scoped commit gate passed.
- Size: 405 lines and 60 entries at the start of the run, then 411 and 61 when the coordinator added LOCAL-MODE (18:19 BST) during the run. I kept that entry. The log now has 265 lines and 41 entries.
- Struck 20 entries, each wholly carried elsewhere:
  - The batch 4 answers: [KI-TOOL-KI-CLI-147 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/683abf5f/docs/roadmap/KI-TOOL-KI-CLI-147-agent-state-folder-tooling.md) was accepted and pruned, and [KI-TOOL-KI-CLI-146](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-146-ki-quiet-setting.md) was accepted on 19 October.
  - CLI-CONVENTIONS and its home correction: now in `ki-repo-tools`' [CLI conventions standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-tools/references/standards-cli-conventions.md).
  - The 08:03 BST answers: [KI-TOOL-KI-CLI-150](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-150-work-folder-entry-points.md) and [KI-TOOL-KI-CLI-153](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-153-biome-schema-drift.md) are done, and ki v0.11.4 is tagged and pinned in ki-principal.
  - The Rig-upgraded note: the RIG-LIVE holds and `state.md` carry it.
  - The SIZE-PRIORITY, mark-recap and ITEM-FIELDS pointers: [GDR-KI-PRINCIPAL-016](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-016-priority-and-size-on-work-records.md) carries all three.
  - The 08:07, 08:40 and 12:04 BST mark entries: Git holds them.
  - The SoP-restart note: the morning restriction has lapsed, and the coordination standard and the output style carry the rest.
  - The WORK-ROUTING request: answered at 12:24 BST.
  - The 13:37 BST work-package answers and STATE-FILE: [`ki-work-package`](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/SKILL.md) carries both.
  - SPECIFICATIONS-OPENED: handoff done.
  - KI-FIRST, the FIRST-STEP disposition and REPO-LINKS: done and in `state.md`.
  - PUSH-KIP: closed.
- Reduced 4 entries to one-line pointers:
  - The 12:24 BST WORK-ROUTING and WOW-REFRESH answers, to the coordination standard, `work.md` Goals and the work-package standard.
  - The 14:02 BST package answers, to the work-package and coordination standards, plus GDR-KI-PRINCIPAL-016 and `state.md`.
  - SPEC-AREAS refined, to ki.specifications' `work.md` and `queries.md`.
  - SPECIFICATIONS-PROJECT, to ki.specifications' `work.md` and `decisions.md`.
- Kept 37 entries whole, LOCAL-MODE among them; the existing pointers that still govern open records are kept as they were. In the batches 6 and 7 entry I struck two bullets:
  - REPO-OWNERSHIP, now in the `ki-repo` repository standard.
  - REPORT-SHAPE, now in the background-runs owner-report rule.
- Check QUERY-REVIEW: the harness has no record for blind review of medium queries. That is as the decision intended: a record is captured only after two or three reviews show whether the review helps.
- Check CI on `main`: both repositories are red.
  - ki-principal fails at "Install released KI" (latest completed run, on `0d106aed`): the pinned ki v0.11.4 installs a harness that does not yet provide the declared skill `ki-work-package`. The run for `8dd63141` was still in progress.
  - ki-agentic-harness fails at Audit (on `db30d0ca`): `ki-skills` KI-LINK-2 finds an absolute local link to a tools-ki record in `ki-work-package`'s `standards-work-package.md`. The link is broken on CI.
- Check desk-kit: closed. `ki agent close` archived the run at 18:27Z on 18 October, and every gate item passed.
- Check cli150-deliver: I cleared its seven gate logs and removed its temporary folder. Its status is DONE and its record, KI-TOOL-KI-CLI-150, is done, so nothing of it now blocks closing the run. It is not closed yet: `ki agent close` closes the whole `ways-of-working` run, which still has agents running.
- Repository audit of ki-principal: FAIL from findings already present before this run, none on the decisions log:
  - two GDR body-link findings;
  - DEPENDS-4 findings in GDR-KI-PRINCIPAL-005 and GDR-KI-PRINCIPAL-010;
  - message-line format in ki.specifications and ki.tools-burndown;
  - COORD-7 unlinked identifiers in ki.chezmoi reports.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The PAPERCLIP-REQ entry links `work.md`, which no longer mentions it. `state.md` Held carries the hold but not the requirement for both Claude and Codex top models, so I kept the entry whole.
- I kept CLI-F-FILTER whole because I could not verify its chezmoi completion-note part. Its `ki-repo-tools`, tools-ki and mgit parts are all in place.
- Another session's untracked `+/_WORK/ki.chezmoi/husky-apply.report.md` was left untouched.

## Queries

### CI-RED-MAIN - Both Capital and harness CI red on main

**Context:** Two separate faults keep `main` red in both repositories.

- **ki-principal:** CI installs the pinned ki v0.11.4, which brings a harness from before the `ki-work-package` rename, so the audit cannot find the skill that `.ki.toml` now declares. This clears only when a `ki` release pins a harness that carries `ki-work-package`.
- **Harness:** `standards-work-package.md` carries an absolute `/Users/...` link to a tools-ki record, which KI-LINK-2 rejects on CI. A one-line link change fixes it.

**Query:** Should one harness run fix the link now, and the next `ki` release pin the fixed harness so ki-principal's CI goes green?

**Options:**

a) (recommended, confidence medium - both causes read directly from the CI logs, but the release timing sits with ki.tools-burndown) A harness run repoints the link to a GitHub or relative form. Then ask ki.tools-burndown, through a `messages.md` line, for a `ki` patch release pinning that harness, and move ki-principal's `.github/ki-version` after it.

b) Fix only the harness link now, and leave ki-principal red until the next scheduled `ki` release.

### 🤖 → 👤 Handoff to supervisor · since 18:21 BST

👤 1 with you

- [with you] CI-RED-MAIN · coordinator · since 18:21
- [committed] decisions log, pushed
