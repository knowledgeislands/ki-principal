# [Foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Baseline rollout](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/baseline-rollout.md) › raise-va

**🤖 → 👤 Handoff to supervisor · Run report at 00:14 BST · last mark 00:14 BST**

---

## Done

- va-principal: captured two triage records in commit `0c54498`. [VA-PRINCIPAL-GOV-007](/Users/krisbrown/workspaces/valle-armonia/va-principal/Streams/Roadmap/VA-PRINCIPAL-GOV-007-declare-issuing-areas.md) covers AREA-TITLES (size s). [VA-PRINCIPAL-GOV-008](/Users/krisbrown/workspaces/valle-armonia/va-principal/Streams/Roadmap/VA-PRINCIPAL-GOV-008-establish-theme-registry.md) covers THEME-REGISTRY (size m). Both numbers were reserved first in [the issue ledger](/Users/krisbrown/workspaces/valle-armonia/va-principal/Streams/Roadmap/_ISSUES.md), committed on its own as `c0819af`. That makes two commits, not one, because the ledger requires the reservation to be committed separately. raise-tmx did the same. The Streams audit shows no fails, and the new records add no warnings. Its 6 warnings are the existing records' missing `size`. The repository audit's ki-work-package fail is in the `va` work package, which this run did not touch. Nothing pushed, and the working tree is clean.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- THEME-REGISTRY's option a) had said to leave va-principal without a registry until one of its records needed a theme. The condition is already met: 18 of the territory's 28 records name one of nine labels, and none of them resolves. I raised the record as the brief asked.
- VA-PRINCIPAL-GOV-008 sends relabelling in apps-vallearmonia.com and apps-markhowarth.com to each of those repositories as a handoff item. It does not edit them.

## Queries

### VA-AREA-TITLES - Confirm Valle Armonia area titles

**Context:** [VA-PRINCIPAL-GOV-007](/Users/krisbrown/workspaces/valle-armonia/va-principal/Streams/Roadmap/VA-PRINCIPAL-GOV-007-declare-issuing-areas.md) adds a `[skills.ki-work-roadmap.areas]` map to `.ki.toml` for the two areas va-principal already issues. Codes and allocations do not change. `GOV` has issued two kinds of work: territory governance, meaning the bootstrap, the declaration and repository naming, and company running, meaning social accounts, operations and the footprint audit. `KNW` has issued the source mirrors and the work bringing community identity into the Principal.

**Query:** Which titles should the two Valle Armonia areas carry?

**Options:** a) (recommended, confidence medium - both fit the noun-phrase rule and cover what each area has issued, but the wording is your call) `GOV` = "Governance and operations", `KNW` = "Knowledge and sources". b) `GOV` = "Governance", `KNW` = "Knowledge base".

### VA-THEMES - Confirm Valle Armonia themes

**Context:** The territory uses nine theme labels and has no registry. In va-principal they are `governance` and `knowledge`. In apps-vallearmonia.com they are `content`, `site`, `operations`, `governance`, `members` and `webmcp`. In apps-markhowarth.com they are `design` and `launch`. Most of them mirror area codes, not themes. The `va` work package's open PROJECTS query already proposes these groups: Community presence, Company, and a Mark Howarth site group. [VA-PRINCIPAL-GOV-008](/Users/krisbrown/workspaces/valle-armonia/va-principal/Streams/Roadmap/VA-PRINCIPAL-GOV-008-establish-theme-registry.md) proposes two theme pages and reconciles every label to one of them.

**Query:** Which theme pages should the Valle Armonia registry hold?

**Options:** a) (recommended, confidence medium - it follows the grouping PROJECTS already proposes, but it relabels 18 records across three repositories and depends on your PROJECTS answer) Create `community-presence` and `company`. Relabel GOV-003 and KNW-001 to `company`, and the website and Mark Howarth labels to `community-presence`, through handoff items in those repositories. b) Create a page for each of the nine labels in use, leaving every record as it is.
