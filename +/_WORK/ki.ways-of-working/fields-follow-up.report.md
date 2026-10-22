# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › fields-follow-up

**🤖 → 👤 Handoff to supervisor · Run report at 12:14 BST · last mark 12:04 BST**

---

## Done

- **ki-agentic-harness, `57eb2f16`, pushed fast-forward. Only my commit was unpushed.** It covers SIZE-MEANING, SELECTION-ORDER, FIELDS-MIGRATE, FIELDS-CORE and FIELDS-KEPT.
  - **Size:** the [work-item format](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-work-item-format.md#priority-and-size) now defines size as relative end-to-end effort, not hours. The delivery shapes are given as worked examples. A size set at capture is provisional and is revisited before Ready.
  - **Selection order and priority meanings:** stated in the format, the [ki-work crosswalk](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work/references/standards-change-management-adapters.md) and [ki-next selection](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-next/references/standards-next-work.md#4-select-candidates).
  - **Migration window:** the [repository-roadmap standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-repository-roadmaps.md#migration-tolerance) names its inventory, the no-gaps or 60-day close, the per-repository runs you approve, and kind and size as proposals you confirm.
  - **Other standards:** the required-fields sentence now matches the warning window. The Streams structure and the Project registry line up. `task_links` is to be revisited at Wave F.
  - **Checkers:** both the roadmap and the Streams checkers now exempt done and cancelled records from size and kind, and fail a `ready` record of size `xl`. The roadmap checker also warns on a theme named beside a Project during the window, whether or not the registry is available. Tests cover each rule, and the Streams rubric was regenerated.
- **ki-agentic-harness checks:**
  - `bun run test` passes 1265 of 1265.
  - `bunx tsc --noEmit` is clean, and Biome is clean.
  - The `ki-work-roadmap` audit has no failures and 18 warnings. These are the harness's own records without a size, the same backlog as before, not a failure.
  - The `ki-work` and `ki-skills` audits pass.
  - `ki-repo-kb-streams` and `ki-next` are not declared in this repository, so they have no focused audit here.
  - The other session's KI-HARNESS-GOV-220 files were not in the tree at commit time. Nothing of theirs was touched.
- **ki-principal, `12be8e7`, committed but not pushed.** The pre-commit audit passed.
  - It amends [GDR-KI-PRINCIPAL-016](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-016-priority-and-size-on-work-records.md) in place with all five answers.
  - It drops `adoption` from the purpose list in [GDR-KI-PRINCIPAL-005](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-005-the-roadmap-model.md) and points to GDR-KI-PRINCIPAL-016.
  - **Correction to the brief:** the decision-record standard forbids any section titled for amendments (BODY-12). So the amendment is dated 2026-10-19 12:04 BST in the Context section, and the Decision itself is rewritten, rather than given an "Amendment" section.
  - Not pushed because 15 other sessions' commits are stacked beneath mine, from `1a9af8a` to `3599c07`, mostly `docs(work)` moves for ki, ki.timelines, ki.mac-studio-setup, ki.observatory, ki.knowledge-acquisition and ki.ways-of-working.
  - Another session's dirty files under `+/_WORK/ki.chezmoi/` were left alone.
- **Inventory, read-only.** No other repository was edited.
  - The registry lists 51 repositories, all available.
  - 50 of them have a roadmap or Streams folder, and 33 hold records: 341 records in 393 Markdown files.
  - Mechanical fixes: 49 retired horizons, 13 `initiative` fields, and 12 themes named beside a Project. `purpose: adoption` appears nowhere.
  - Open records lacking `kind`: 56. This counts adopted open records only, leaving out those on retired horizons, which the mechanical fix moves first.
  - Open records lacking `size`: 307, triage included.
- **Reconciling 316 and 367.** Both come from the committed state at about 08:00 BST.
  - At that point the estate held 316 records in 31 repositories, inside 368 Markdown files.
  - So 316 counted records. 367 counted every Markdown file in the roadmap folders, which adds each repository's `_ISSUES.md` ledger and index notes, about 52 files.
  - The one-file gap is most likely a working-tree difference at the time of the earlier count.
  - Both figures already include chezmoi (19 records) and ki-design (9 records, 10 files). ki-design is now in the registry.
  - The count has since grown to 341 records with today's captures.
- **Net records:** 0 in ki-agentic-harness and 0 in ki-principal.

| Repository | Adapter | Records | Retired horizons | `initiative` | Theme beside Project | Open, no kind | Open, no size |
| --- | --- | --- | --- | --- | --- | --- | --- |
| personal-principal | Streams | 35 | 22 | 3 | 12 | 6 | 33 |
| hnr-principal | Streams | 21 | 8 | 0 | 0 | 5 | 20 |
| apps-tower.midnight.ninja | roadmap | 20 | 0 | 6 | 0 | 0 | 6 |
| 5g-emerge-phase2 | roadmap | 10 | 5 | 0 | 0 | 0 | 10 |
| apps-markhowarth.com | roadmap | 4 | 4 | 0 | 0 | 0 | 4 |
| chezmoi | roadmap | 20 | 0 | 4 | 0 | 0 | 20 |
| legal-principal | Streams | 29 | 3 | 0 | 0 | 4 | 28 |
| hnr-agentic-harness | roadmap | 3 | 2 | 0 | 0 | 1 | 3 |
| tmx-principal | Streams | 6 | 2 | 0 | 0 | 2 | 6 |
| 5g-emerge-demos | roadmap | 1 | 1 | 0 | 0 | 0 | 1 |
| er-principal | Streams | 9 | 1 | 0 | 0 | 5 | 8 |
| va-principal | Streams | 6 | 1 | 0 | 0 | 1 | 6 |
| er-agentic-harness | roadmap | 22 | 0 | 0 | 0 | 22 | 22 |
| apps-vallearmonia.com | roadmap | 16 | 0 | 0 | 0 | 10 | 15 |
| apps-observatory.local | roadmap | 35 | 0 | 0 | 0 | 0 | 28 |
| ki-agentic-harness | roadmap | 19 | 0 | 0 | 0 | 0 | 18 |
| tools-rig | roadmap | 13 | 0 | 0 | 0 | 0 | 12 |
| tools-ki | roadmap | 14 | 0 | 0 | 0 | 0 | 11 |
| mcp-m365 | roadmap | 10 | 0 | 0 | 0 | 0 | 10 |
| acquire | roadmap | 9 | 0 | 0 | 0 | 0 | 9 |
| ki-design | roadmap | 9 | 0 | 0 | 0 | 0 | 9 |
| infoschematics | roadmap | 6 | 0 | 0 | 0 | 0 | 6 |
| 5g-emerge-phase3 | roadmap | 5 | 0 | 0 | 0 | 0 | 5 |
| tools-mgit | roadmap | 4 | 0 | 0 | 0 | 0 | 3 |
| ki-principal | Streams | 3 | 0 | 0 | 0 | 0 | 3 |
| apps-knowledgeislands.info, apps-rig.midnight.ninja, ki-specifications, ki-techne-harness, mcp-git-audit, mcp-gsuite, si-principal, tools-techne | roadmap or Streams | 12 | 0 | 0 | 0 | 0 | 11 |

## In Progress

Nothing is running.

Outstanding - no action requested now:

- ki-principal `12be8e7` waits to be pushed with the 15 stacked commits from other sessions, at your discretion under PUSH-STACKED.
- Size and kind backfill in roadmap repositories waits for a ki release that accepts the fields, under [KI-TOOL-KI-CLI-155](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-155-priority-and-size-fields.md). The 60-day backstop counts from that release. Mechanical fixes need no new field and can run now.
- The tools-burndown Messages line for the shared rule table (VALIDATOR-PARITY) was not mine to send. It stays with the coordinator.

## Queries

### FIELDS-MIGRATE-ORDER - Which repositories to migrate first

**Context:** Twelve repositories need mechanical fixes. Personal-principal alone holds 22 of the 49 retired horizons and all 12 themes beside a Project; hnr-principal has 8. Kind and size proposals can be written in Streams Capitals now. In roadmap repositories they must wait for the ki release under KI-TOOL-KI-CLI-155, because today's `ki` rejects unknown fields. Each run is approved by you, one repository at a time.

**Query:** Which repositories should the first migration runs cover?

**Options:**

a) (recommended, confidence medium - it clears most of the mechanical load where no ki release is needed, and the per-repository counts come from a fresh scan) Run personal-principal first, all fixes plus kind and size proposals, as the pilot. Then hnr-principal, legal-principal, tmx-principal, er-principal and va-principal. Then mechanical-only runs in apps-tower.midnight.ninja, 5g-emerge-phase2, apps-markhowarth.com, chezmoi, hnr-agentic-harness and 5g-emerge-demos. Kind and size in roadmap repositories follow after the ki release.

b) Pilot in ki-agentic-harness, which has no mechanical fixes, once the ki release lands, then follow the order in a).

c) Run the mechanical fixes across all twelve repositories in one approved batch, then take kind and size per repository.

### 🤖 → 👤 Handoff to supervisor · since 12:14 BST

👤 1 with you · ⬆️ 1 unpushed

- [with you] FIELDS-MIGRATE-ORDER · owner · since 12:14
- [committed] ki-agentic-harness, pushed
- [unpushed] ki-principal, beneath 15 other sessions' commits
