# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › check-pass

**🤖 → 🧑 Handoff to supervisor · Run report at 05:16 BST · last mark 22:34 BST**

---

## Done

- **Audits, all 20 Knowledge Islands repositories (`ki repo -t knowledge-islands audit`, `ki` 0.11.0):** 369 skill checks pass, 37 warn and 10 fail, with 49 failing findings, in five repositories. Fifteen repositories have no failure. `ki territory audit` finds nothing in 20 repositories, and `ki doctor` says healthy, with 16 of 16 checks passing.
- **Failures by repository.** None of them is a migration fault. I fixed only the link slips, in the next lines.
  - ki-principal: ki-pmo PMO-7 had 37 bare or missing record links in work reports, and 29 are left after my fix. ki-engineering SCR-11 fails on the `.husky/pre-commit` shape.
  - ki-agentic-harness: ki-authoring MD051 fails on the `project-close` anchor in [KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md). ki-repo-harness CAP-2 fails because `skills/README.md` differs from the SKILL.md front matter. ki-engineering SCR-11 also fails here.
  - ki-techne-harness: KNIP-2 fails because the toolchain is not installed. ITEM-3 fails on [KI-TECHNE-OPS-027](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/docs/roadmap/KI-TECHNE-OPS-027-agent-host-tailscale-key-minting.md), which is under the Techne Programme Hold.
  - apps-knowledgeislands.info: TSC-1 fails twice, and KNIP-2 and DESIGN-2 fail, all because the toolchain is not installed on this machine. My brief allows no installs.
  - apps-observatory.local: ki-guides GUIDE-4 and ki-work-roadmap ITEM-1 fail. Another session has 24 uncommitted files in that tree.
- **Warnings worth knowing.** INDEX-8: [ADR-KI-PRINCIPAL-004](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-004-provider-neutral-isolated-agent-execution.md), [ADR-KI-PRINCIPAL-005](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-005-one-persona-across-explicit-working-contexts.md) and [ADR-KI-PRINCIPAL-006](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-006-techne-implementation-ownership.md) are listed after [ADR-KI-PRINCIPAL-007](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-007-territory-seats-on-hosts.md). STREAM-10: chezmoi, mac-studio-setup, paperclip-capture-and-rebuild and website have no open records. PMO-9: seven work folders, and the empty `+/_THREADS/`, need pruning at their next mark. COV-1 is under Queries. In the harness, 136 radar warnings, 12 DIAG-4 diagram-freshness warnings and 3 LONG-3 refresh-cadence warnings have nothing to do with the migration.
- **`ki work status --format json`: pass.** It emits `ki/work-status/v1`. In ki-principal there is one entry for each of the 9 folders in `+/_WORK/`: 8 on hold, each with its reason and release, and `ki.ways-of-working` with-worker, carrying three runs (check-pass, observatory-bringup and tools-burndown). ki-agentic-harness has no `+/_WORK/` entries. The 5 items awaiting review appear only as a count, in the text view. Under the tools-ki spec, the JSON lists no review items. The tolerance window works: `ki work status` reads hnr-principal (10 entries), personal-principal (4) and legal-principal (1) from their old checkpoints, with one warning for each entry.
- **Registry: pass.** I checked 103 `theme:` and `project:` references across 7 repositories. Every one resolves to one of the 4 theme pages (foundations, model, rig, techne) or one of the 21 Project notes. The 5 `theme: null` values are on territory-level and regular work files, which is correct. The one `example-theme` is a skill template asset. `Themes.md` and `Projects.md` list every note, and no `initiative:` field remains.
- **Old-area links: pass for live content.** No live note, work file, theme page, Project note or diagram links to `+/_CHECKPOINTS`, `+/_THREADS` or `Streams/Initiatives`. The only remaining mentions are in prose: the MIGRATED lines and the history in Project notes. Under the migration plan, reports, decisions logs, design papers, roadmap records and the Calendar count as history. They hold 389 links to old paths: 340 point at files that moved and 49 at files that were pruned.
- **Trivial link slips fixed, provisional, for Kris to confirm (RECORD-LINKS):** 13 links in six open records now point at each report's `+/_WORK/` home, or at its last revision on GitHub where the report was pruned.
  - ki-agentic-harness `e434304c`: [KI-HARNESS-GOV-197](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-197-pmo-7-outside-checkout-links.md), [KI-HARNESS-GOV-199](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-199-thread-identity-role-native-sessions.md), [KI-HARNESS-GOV-205](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-205-static-light-diagram-export.md), [KI-HARNESS-GOV-206](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-206-activity-homes-and-coordination.md) and [KI-HARNESS-GOV-209](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-209-acquired-inbound-area.md). The gate passed and the commit is pushed.
  - tools-ki `09f5f3b3`: [KI-TOOL-KI-CLI-145](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-145-thread-session-bindings-role.md). The gate passed and the commit is pushed.
- **PMO-7 in this work's own reports, ki-principal `3d51689`:** I linked the bare record identifiers in eight ways-of-working reports. The gate passed and the commit is pushed. PMO-7 for this folder drops from 9 findings to 1, and the one left is a decision identifier quoted inside a commit subject in a code span (PMO-CODE).
- **`+/_WORK_REVIEW`: pass.** It holds exactly the five items the classification sent there: ki.agent-host, ki.baseline-rollout, ki.estate-factorisation, ki.paperclip-capture-and-rebuild and ki.regular.command-centre. Each has its `work.md`. In ki-agentic-harness, `+/_WORK_REVIEW/` holds ki.regular.skill-reviews, as the territory plan set. No other territory repository has a work area.
- **Pushes:** each of my three commits went up fast-forward, with no other session's commit beneath it. I committed nothing in tools-rig or apps-observatory.local.

## In Progress

Nothing is running from this run. Left before the other territories:

1. **ki-principal at its next marks.** `ki.ways-of-working` shows as stuck until the coordinator writes a beat. The 28 PMO-7 findings in other work folders belong to those works, each at its own mark: ki 6, ki.chezmoi 8, ki.tools-burndown 11, and ki.observatory, ki.mac-studio-setup and ki.knowledge-acquisition 1 each. The PMO-9 prunes are also due, the STREAM-10 close-out assessments for four Projects, and the INDEX-8 order.
2. **Gate shape and harness generators.** SCR-11 in ki-principal and the harness, CAP-2 and MD051 in the harness, all belonging to the sessions that own them.
3. **Toolchain installs.** apps-knowledgeislands.info and ki-techne-harness fail type-check and knip only because `bun install` has not been run on this machine.
4. **The open queries below:** COV-1, RECORD-LINKS and PMO-CODE.
5. **The other territories' areas, still in the old shape.** personal-principal has 5 checkpoints, 7 threads and 7 Initiatives. hnr-principal has 11 checkpoints, 10 threads and 3 Initiatives. legal-principal has 2 checkpoints, 1 thread and 7 Initiatives. acquire has 2 checkpoints and 1 thread. va-principal has 3 checkpoints, si-principal 2 and er-principal 2. techmedix has none.
6. **KI records that point into other territories.** Eight KI records link into hnr-principal's and acquire's `+/_THREADS/`, in mcp-m365, mcp-gsuite and tools-ki ([KI-TOOL-KI-CLI-128](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-128-granola-retention-safeguards.md) among them). Most of those targets still exist today, and they break when those territories migrate unless RECORD-LINKS covers them.

Outstanding - no action requested now:

- tools-rig: another session has 15 uncommitted files and two unpushed commits from 04:55 and 05:02. I left [KI-TOOL-RIG-CORE-057](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-057-github-desktop-repository-list.md) and its one old-area link alone.
- homebrew-tap: the local checkout is one commit behind origin, the v0.11.0 formula. I fetched nothing.
- apps-observatory.local: another session has 24 uncommitted files in flight.
- The empty `+/_THREADS/ways-of-working/` folder is untracked. It can go once no run launched against that path is still running.
- I left [KI-HARNESS-GOV-198](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-198-reply-forms.md), which is awaiting review, and [KI-TOOL-KI-CLI-128](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-128-granola-retention-safeguards.md), which is done, as evidence. I also left `+/_WORK/ki.tools-burndown/briefs/next-worker.md`, because that work is in flight.

## Queries

### COV-1 - ki-checkpoint's coverage check still looks for the old area

**Context:** After the migration, ki-principal still declares `[skills.ki-checkpoint]`. The governance coverage cascade, COV-1, warns "no +/_CHECKPOINTS/ subarea found - stale opt-in?", because the skill's coverage marker is still the old folder, while the work files now live in `+/_WORK/<id>/work.md`. Every territory that migrates will raise the same warning.

**Query:** Should the harness change ki-checkpoint's coverage marker to `+/_WORK/` before the other territories migrate?

**Options:** a) (recommended, confidence high - the warning comes from a fixed path in one skill, and the work model names `+/_WORK/` as the home) Capture a harness record, through ki-next, to move ki-checkpoint's coverage marker to `+/_WORK/`, keeping `+/_CHECKPOINTS/` accepted through the tolerance window, and land it before the next territory runs. b) Leave it, and accept one COV-1 warning in each migrated repository until the tolerance window closes.

### RECORD-LINKS - Treat open roadmap records' links as live in the territory runs

**Context:** The Capital's migration plan treats every roadmap record as history, so its citation step left the records alone. That left 14 broken old-area links in seven open records across the harness, tools-ki and tools-rig. Tonight I repointed 13 links in six of them (provisional, for Kris to confirm), sending moved targets to their new path and pruned ones to their last revision on GitHub. I left done and awaiting-review records as evidence. The other territories' migrations will break the links in eight more KI records in the same way.

**Query:** Should the territory migrations rewrite old-area links in open roadmap records, in every repository that links into the migrating territory?

**Options:** a) (recommended, confidence medium - an open record is still read and acted on, while a done record is evidence; the rewrite is mechanical) Yes: confirm tonight's repointing, and add a step to each territory run that rewrites links in open records across the estate, pinning pruned targets to their last revision and leaving done and awaiting-review records unchanged. b) Keep records as history everywhere: revert tonight's two commits and accept broken links in open records.

### PMO-CODE - PMO-7 checks identifiers inside code spans

**Context:** PMO-7 skips fenced blocks but still flags a full record identifier inside an inline code span. In `settle-model.report.md`, one is left: GDR-KI-PRINCIPAL-009 inside a quoted commit subject, `docs(decisions): add GDR-KI-PRINCIPAL-009 the work model`. A link cannot sit inside a code span, so the only ways to clear it are to unquote the subject or to change the rubric.

**Query:** Should PMO-7 skip inline code spans as well as fenced blocks?

**Options:** a) (recommended, confidence medium - a code span quotes literal text, such as a commit subject, and cannot hold a link) Capture a harness record, through ki-next, so that PMO-7 skips inline code spans, and leave the report as it is. b) Keep the rule as it is, and rewrite the quoted subject without backticks.

### 🤖 → 🧑 Handoff to supervisor · since 05:16 BST

🧑 3 with you

- [with you] COV-1 · owner · since 05:16
- [with you] RECORD-LINKS · owner · since 05:16
- [with you] PMO-CODE · owner · since 05:16
- [committed] ki-principal, ki-agentic-harness and tools-ki, pushed
