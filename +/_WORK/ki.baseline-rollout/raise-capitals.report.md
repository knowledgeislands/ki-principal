# [Foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Baseline rollout](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/baseline-rollout.md) › raise-capitals

**🤖 → 👤 Handoff to supervisor · Run report at 00:12 BST · last mark 23:56 BST**

---

## Done

- legal-principal: captured [LGL-PRINCIPAL-OPS-029](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-029-migrate-initiatives-to-themes.md) (Migrate Initiatives to Themes, triage, size m). It moves the six Initiative pages, renames `initiative` to `theme` on the Project and the 23 Activities, and proposes no page for three obsolete labels, following [LGL-PRINCIPAL-OPS-024](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-024-lossless-roadmap-metadata.md). It waits until OPS-023 and OPS-024 are accepted. Commits `2ae7ea60` (reserve) and `7bec4bcc` (capture), local and unpushed. Focused roadmap audit: pass, no finding on the new record.
- personal-principal: captured [KB-PRINCIPAL-047](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-047-migrate-initiatives-to-themes.md) (Migrate Initiatives to Themes, triage, size m). It moves the six Initiative pages, renames the key on five Project notes, fixes two live links, and proposes no page for `repository-governance`. Commits `232da46a` (reserve) and `64387631` (capture), local and unpushed. Focused Streams audit: no finding on the new record. This repository does not declare `ki-work-roadmap`, so it has no roadmap audit.
- er-principal: captured [ER-PRINCIPAL-016](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-016-establish-theme-registry.md) (Establish theme registry, triage, size m). It takes the three directions from the territory alignment assessment as theme pages and maps all five labels in use onto them. The harness relabelling goes to `er-agentic-harness` as a handoff, and the slugs wait on Equal Remedy's open ALIGN query. Commits `ce475e5` (reserve) and `497c7d9` (capture), local and unpushed. Focused roadmap audit: pass, no finding on the new record.
- Departure from the brief: each repository got two commits, not one. All three ledgers say to "reserve a number by committing this ledger's advance on its own before writing the record", and repository conventions govern, so I followed that rule, as `raise-tmx` did.
- None of the three Capitals had any uncommitted changes from another session. I touched no hook, package or lock file.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The `kb.personal-tower` work file names a Project, `personal-tower`, that has no Project note in personal-principal. That is a gap in the Project registry, not the theme registry. KB-PRINCIPAL-047 records it and leaves it alone.
- The Equal Remedy harness handoff (relabelling ER-HARNESS-001 to 022 to `reusable-legal-capabilities`) is described in ER-PRINCIPAL-016 but not yet placed on the `er-agentic-harness` roadmap. It would follow from adoption.
- In legal-principal, LGL-PRINCIPAL-OPS-023 and OPS-024 have been awaiting review since 11 October. OPS-029 waits until they are accepted.

## Queries

### LGL-THEMES - Legal's three obsolete theme labels

**Context:** [LGL-PRINCIPAL-OPS-029](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-029-migrate-initiatives-to-themes.md) moves Legal's six Initiatives to theme pages unchanged. Five records still name labels that have no page: `evidence-management` on EVD-003, EVD-004 and EVD-005, `financial-remedy` on FAM-004, and `criminal-casework` on CRM-001. These are exactly the seven exceptions that [LGL-PRINCIPAL-OPS-024](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-024-lossless-roadmap-metadata.md) left untouched for other reasons. OPS-024 itself removed the same labels from twelve other records, on the grounds that "obsolete themes are not replaced", and the fixed `EVD`, `FAM` and `CRM` areas still carry their meaning. OPS-024 is still awaiting your review.

**Query:** Should OPS-029 remove these three labels rather than give them theme pages?

**Options:**

a) (recommended, confidence medium - it follows the Capital's own OPS-024 rule, but you have not yet accepted that rule) Remove the label from the five records, changing nothing else but `updated_at`, and create no page.

b) Leave the five records as they are until each one's own disposition, and accept the warnings until then.

c) Give each label its own theme page.

### KB-THEMES - Personal's one stray theme label

**Context:** [KB-PRINCIPAL-047](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-047-migrate-initiatives-to-themes.md) moves Personal's six Initiatives (Acquire, Life, Thinking, Tower, Health and Rig) to theme pages unchanged. Every theme label in the territory resolves except `repository-governance`, which appears once, on KB-PRINCIPAL-011 (Reconcile KB Guidance). That record is projectless intake about the island's own guidance, and none of the six directions fits it. Separately, the Rig page keeps three parked ideas in its Notes, which sit awkwardly on a theme page; planning will decide whether they move.

**Query:** How should KB-PRINCIPAL-011's `repository-governance` label be reconciled?

**Options:**

a) (recommended, confidence medium - a judgement on one label; the record needs no theme to stay valid) Remove the label and create no page.

b) Create a seventh theme, `repository-governance`, for the island's own upkeep.

c) Qualify it to a Knowledge Islands theme, such as `knowledge-islands/foundations`.

### ER-THEMES - Equal Remedy's theme slugs

**Context:** Equal Remedy has no registry. Its records use five labels: `research` and `advocacy` (ER-PRINCIPAL-004 to 008), `resource-library` (ER-PRINCIPAL-011), and in the harness `operations` (ER-HARNESS-001) and `capabilities` (ER-HARNESS-002 to 022). The [territory alignment assessment](/Users/krisbrown/workspaces/equal-remedy/er-principal/-/territory-alignment-assessment.md) of 13 October proposed three directions and mapped every one of these records onto them: `territory-foundations`, `family-justice-reform` and `reusable-legal-capabilities`. Its question has been open since then as ALIGN in Equal Remedy's [queries](/Users/krisbrown/workspaces/equal-remedy/er-principal/+/_WORK/er/queries.md), with no options recorded. [ER-PRINCIPAL-016](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-016-establish-theme-registry.md) takes the theme half of that proposal. The Project, the record kinds and the governance repairs stay with [ER-PRINCIPAL-014](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-014-territory-alignment.md).

**Query:** Should Equal Remedy's themes be the assessment's three directions, with the five labels mapped onto them?

**Options:**

a) (recommended, confidence medium - the assessment was reviewed and covers every record, but its ALIGN question has never had options put to you) Adopt the three directions as theme pages and map the five labels as ER-PRINCIPAL-016 proposes. This answers the theme part of ALIGN and leaves the Project part open.

b) Keep the five existing labels and give each one a page.

c) Fold ER-PRINCIPAL-016 into ER-PRINCIPAL-014 and settle everything together when you answer ALIGN.

### 🤖 → 👤 Handoff to supervisor · since 00:12 BST

👤 3 with you

- [with you] LGL-THEMES · owner · since 00:12
- [with you] KB-THEMES · owner · since 00:12
- [with you] ER-THEMES · owner · since 00:12
- [committed] legal-principal, personal-principal, er-principal
- [unpushed] legal-principal, personal-principal, er-principal
