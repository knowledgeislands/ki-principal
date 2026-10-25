# [Foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Baseline rollout](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/baseline-rollout.md) › wave1-sweep

**🤖 → 👤 Handoff to supervisor · Run report at 23:48 BST · last mark 23:27 BST**

---

## Done

Read-only sweep of 28 repositories. No commits, no writes to any repository, `ki repo conform` never run. `ki repo audit` did not abort on COORD-1 in any repository. It refused the `personal/dotfiles` symlink, so I audited that one by its real path (`~/.local/share/chezmoi`). Each line below gives five checks: the area map (retired theme slugs), the ledger and record form, missing `size` (and `kind`), Mermaid, and any other roadmap finding.

**Totals:**

- **Area maps:** 5 repositories still have 19 theme slugs as area titles. None of them is a live KI theme (foundations, model, rig, techne).
- **Ledgers:** 7 use a superseded ledger form, and 3 of those also use the wrong issuing mode.
- **Record form:** 1 record fails the identity check, 9 fail the body-shape check, 4 still name `initiative`, and 6 use areas their repository never declared.
- **Size and kind:** 191 open records in 18 repositories have no `size`, and 61 adopted open records have no `kind`.
- **Mermaid:** 32 fences across 9 repositories. Existing archify or bar-table records cover all of them except one fence in a captured conversation.

humans-not-robots:

- [5g-emerge-apex](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-apex): area map 4 retired slugs (`website`, `ki-conformance`, `housekeeping`, `deployment-operations`; ROAD-6 fail) · ledger superseded and in the wrong mode (ROAD-7 fail) · 0 records · 0 missing size · 0 Mermaid.
- [5g-emerge-demos](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-demos): area map 3 retired slugs (`dashboard`, `contract-proof`, `deployment`; ROAD-6 fail) · ledger superseded and in the wrong mode (ROAD-7 fail) · 1 record, failing identity (ITEM-1, [5GE-DEMO-DBD-027](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-demos/docs/roadmap/5GE-DEMO-DBD-027-repair-canvas-readability.md)) · 1 missing size · 0 Mermaid.
- [5g-emerge-phase2](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase2): area map clean · ledger current · 10 records, 2 failing body shape because Discussion is not last ([5GE-P2-GOV-017](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase2/docs/roadmap/5GE-P2-GOV-017-deliver-wp4-calendar.md), [5GE-P2-GOV-018](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase2/docs/roadmap/5GE-P2-GOV-018-separate-wp4-pages.md)) · 10 missing size, 4 missing kind · 0 Mermaid.
- [5g-emerge-phase3](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3): area map clean · ledger current · 5 records · 5 missing size · 0 Mermaid.
- [5g-emerge-testbed](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-testbed): area map 4 retired slugs (`source-data`, `ki-conformance`, `housekeeping`, `deployment-operations`; ROAD-6 fail) · ledger superseded and in the wrong mode (ROAD-7 fail) · 0 records · 0 missing size · 0 Mermaid.
- [hnr-agentic-harness](/Users/krisbrown/workspaces/humans-not-robots/hnr-agentic-harness): no area map · ledger current · 3 records, theme `harness-foundation` not in any registry · 3 missing size, 1 missing kind · 0 Mermaid.
- [hnr-principal](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal): area map 6 retired slugs (`5g-emerge`, `engineering`, `company-finance`, `knowledge-base`, `product`, `research`), which the Streams checker does not flag · ledger current · 22 records · 8 fails because registry notes list work records (STREAM-9) · theme registry still the legacy `Streams/Initiatives/` · 20 missing size, 5 missing kind · 21 Mermaid. 19 of them come through the `Resources` link into hnr-shared and are covered by [HNR-PRINCIPAL-ENG-002](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-ENG-002-redraw-hnr-shared-mermaid-diagrams-in-archify.md). The other 2 are email-status pies covered by [HNR-PRINCIPAL-KM-018](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-KM-018-replace-email-status-pie-with-bar-table.md).
- [infoschematics](/Users/krisbrown/workspaces/humans-not-robots/infoschematics): area map clean · ledger current · 6 records · 6 missing size · 0 Mermaid.

legal:

- [legal-agentic-harness](/Users/krisbrown/workspaces/legal/legal-agentic-harness): no area map · ledger current · 0 records · 0 Mermaid.
- [legal-principal](/Users/krisbrown/workspaces/legal/legal-principal): area titles already migrated · ledger current · 29 records · theme registry still the legacy `Streams/Initiatives/` · 28 missing size, 5 missing kind · 2 Mermaid. The Network Map flowchart is covered by [LGL-PRINCIPAL-OPS-028](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-028-redraw-mermaid-diagrams-in-archify.md). The FR timeline gantt is excluded there as the known exception.

personal:

- [acquire](/Users/krisbrown/workspaces/personal/acquire): no area map · ledger current · 4 records (2 open) · 1 missing size · 1 Mermaid `graph`, inside a captured ChatGPT conversation and not covered by any record.
- [apps-kris.me.uk](/Users/krisbrown/workspaces/personal/apps-kris.me.uk): no area map · ledger superseded (ROAD-7 warn) · 0 records · 0 Mermaid.
- [apps-midnight.ninja](/Users/krisbrown/workspaces/personal/apps-midnight.ninja): area map clean · ledger current · 0 records · 0 Mermaid.
- [apps-rig.midnight.ninja](/Users/krisbrown/workspaces/personal/apps-rig.midnight.ninja): area map clean · ledger current · 1 record · 1 missing size · 0 Mermaid.
- [apps-tower.midnight.ninja](/Users/krisbrown/workspaces/personal/apps-tower.midnight.ninja): area map clean · ledger current · 23 records (10 open) · 6 missing size · 3 Mermaid, covered by [PERSONAL-TOWER-SITE-019](/Users/krisbrown/workspaces/personal/apps-tower.midnight.ninja/docs/roadmap/PERSONAL-TOWER-SITE-019-redraw-mermaid-in-archify.md).
- [dotfiles (chezmoi)](/Users/krisbrown/.local/share/chezmoi): area map clean · ledger current · 22 records (20 open), 4 still naming retired `initiative` · 16 missing size · 0 Mermaid.
- [personal-agentic-harness](/Users/krisbrown/workspaces/personal/personal-agentic-harness): no area map · ledger current · 0 records · 0 Mermaid.
- [personal-principal](/Users/krisbrown/workspaces/personal/personal-principal): no area map · ledger current · 36 records (35 open) · theme registry still the legacy `Streams/Initiatives/` · 33 missing size, 6 missing kind · 3 Mermaid. The Dune flowchart is covered by [PERSONAL-PRINCIPAL-045](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/PERSONAL-PRINCIPAL-045-redraw-mermaid-diagrams-in-archify.md). The 2 email-triage pies are the known exception and are covered by [PERSONAL-PRINCIPAL-046](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/PERSONAL-PRINCIPAL-046-replace-email-triage-pie-with-bar-table.md).

equal-remedy:

- [apps-dafacts.org](/Users/krisbrown/workspaces/equal-remedy/apps-dafacts.org): no area map · ledger superseded (ROAD-7 warn) · 0 records · 0 Mermaid.
- [er-agentic-harness](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness): no area map · ledger superseded (ROAD-7 warn) · 22 records · 22 missing size, 22 missing kind · 0 Mermaid.
- [er-principal](/Users/krisbrown/workspaces/equal-remedy/er-principal): no area map · ledger current · 9 records · no theme registry at all · 8 missing size, 5 missing kind · 1 Mermaid, covered by [ER-PRINCIPAL-015](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-015-redraw-mermaid-diagrams-in-archify.md).

valle-armonia:

- [apps-markhowarth.com](/Users/krisbrown/workspaces/valle-armonia/apps-markhowarth.com): no area map · ledger superseded (ROAD-7 warn) · 4 records · 4 missing size · 0 Mermaid.
- [apps-vallearmonia.com](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com): area map clean · ledger current · 16 records · 15 missing size, 10 missing kind · 1 Mermaid, covered by [VA-WEBSITE-GOV-005](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-GOV-005-redraw-mermaid-in-archify.md) · **still 7 planning gaps**: 7 body-shape fails (ITEM-3) across 5 records. Four Now or Next drafts lack Current state, Files touched, Dependencies / blocks and Documentation impact: [VA-WEBSITE-CONT-005](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-CONT-005-resolve-image-review-flags.md), [VA-WEBSITE-SANC-008](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-008-package-the-sanctuary.md), [VA-WEBSITE-SANC-009](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-009-close-the-editorial-audit.md) and [VA-WEBSITE-SITE-004](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SITE-004-choose-the-home-page-layout.md). The awaiting-review [VA-WEBSITE-SITE-003](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SITE-003-consolidate-the-design-system.md) accounts for 3 fails: missing plan sections, an incomplete review packet and no final Discussion.
- [va-agentic-harness](/Users/krisbrown/workspaces/valle-armonia/va-agentic-harness): no area map · ledger current · 0 records · 0 Mermaid.
- [va-principal](/Users/krisbrown/workspaces/valle-armonia/va-principal): no area map is declared, yet all 6 records and the ledger use the fixed areas `GOV` and `KNW`, and the checker does not flag it · no theme registry at all · 6 missing size, 1 missing kind · 0 Mermaid.

techmedix:

- [apps-yorkphotosoc.org](/Users/krisbrown/workspaces/techmedix/apps-yorkphotosoc.org): no roadmap at all. Its 31 audit fails are repository-contract checks, outside this sweep.
- [tmx-agentic-harness](/Users/krisbrown/workspaces/techmedix/tmx-agentic-harness): no area map · ledger current · 0 records · 0 Mermaid.
- [tmx-principal](/Users/krisbrown/workspaces/techmedix/tmx-principal): area map 2 retired slugs (`company-record`, `knowledge-base`), which the Streams checker does not flag · ledger current · 6 records · no theme registry at all · 6 missing size, 2 missing kind · 0 Mermaid.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The one Mermaid fence no record covers is in [acquire](/Users/krisbrown/workspaces/personal/acquire), inside a captured ChatGPT conversation under `captures/`. It is source evidence, so I am raising no conversion for it.
- hnr-principal's 2 email-status pies are a third pie exception the brief did not name. [HNR-PRINCIPAL-KM-018](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-KM-018-replace-email-status-pie-with-bar-table.md) already covers them.
- All six archify conversion records, plus the two bar-table records, are in triage and carry a size. Their figure re-export still waits on [KI-HARNESS-GOV-205 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/4559224e03dbf98c4cc73595596436f58b258763/docs/roadmap/KI-HARNESS-GOV-205-static-light-diagram-export.md).
- The audits ran despite [KI-HARNESS-GOV-220 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/eea04f87092cc81d0b595e161ad96757558bd125/docs/roadmap/KI-HARNESS-GOV-220-coord-1-undeclared-warn-level.md). legal-principal and personal-principal still fail COORD-7 because work reports carry unlinked record identifiers. That is outside this sweep.

## Queries

### AREA-TITLES - Retitle retired theme-slug areas

**Context:** The area-to-theme map in `.ki.toml` is retired. An area title should now be a short capitalised noun phrase. Five repositories still use theme slugs as area titles, 19 in all: 5g-emerge-apex, 5g-emerge-demos, 5g-emerge-testbed (all three failing ROAD-6), hnr-principal and tmx-principal. None of the slugs is a live KI theme. Separately, va-principal issues `GOV` and `KNW` records but declares no area map. legal-principal and 5g-emerge-phase2 already show the target form. The fix is a `.ki.toml` edit in each repository, which needs your authority. **Query:** Should I raise conformance records to retitle these areas, and declare va-principal's map, in each territory's repositories? **Options:** a) (recommended, confidence medium - the edit is mechanical, but the titles need wording you approve) Raise one conformance record per affected repository, routed through each territory's Capital: the three 5g-emerge repositories and hnr-principal through hnr-principal, tmx-principal on its own, and va-principal on its own. Each record proposes noun-phrase titles for you to confirm. b) Raise one combined record in each Capital, hnr-principal, tmx-principal and va-principal, covering its territory's repositories.

### LEDGER-FORM - Repair superseded issue ledgers

**Context:** Seven project-roadmap ledgers still use a superseded canonical form, which the audit warns on: 5g-emerge-apex, 5g-emerge-demos, 5g-emerge-testbed, apps-kris.me.uk, apps-dafacts.org, er-agentic-harness and apps-markhowarth.com. The three 5g-emerge ledgers also fail for being in the wrong issuing mode. That is probably a knock-on effect of their slug-valued area maps, though I have not verified it. `ki repo conform --skill ki-work-roadmap` rewrites a superseded ledger and keeps its allocation, but HOOK-GUARD bars conform until ki.tools-burndown lifts it. **Query:** How should the superseded ledgers be repaired? **Options:** a) (recommended, confidence medium - conform is the designed repair but is held, and the wrong-mode cause is inferred) Fold the three 5g-emerge ledgers into their AREA-TITLES records. Repair the other four with a `--dry-run`-checked conform once HOOK-GUARD lifts, one repository at a time on your go. b) Hand-edit all seven ledgers now under conformance records, without waiting for conform.

### SIZE-KIND - Backfill size and kind

**Context:** 191 open records in 18 repositories have no `size`, and 61 adopted open records have no `kind`. The largest gaps are personal-principal (33), legal-principal (28), er-agentic-harness (22, all also without kind), hnr-principal (20), dotfiles (16) and apps-vallearmonia.com (15). The field migration window opened on 2026-10-19 and closes on a complete clean scan or a 60-day backstop, after which these warnings become fails. The standard says size and kind need judgement: a run proposes them and you confirm them, one repository at a time. dotfiles also has 4 records still naming `initiative`, which is a mechanical fix. **Query:** How should the size and kind backfill run? **Options:** a) (recommended, confidence medium - it follows the standard's migration rule, but the volume makes the confirmation load real) One read-only proposal run per territory, each producing a size and kind table for you to confirm. Then one write run per repository on your confirmation, fixing the dotfiles `initiative` fields in the same pass. b) Leave the backfill to each repository's next planning pass and accept the risk of fails at the backstop.

### VA-PLANNING - Close apps-vallearmonia.com planning gaps

**Context:** apps-vallearmonia.com still has 7 planning gaps, all body-shape fails (ITEM-3) across 5 records. VA-WEBSITE-CONT-005 and VA-WEBSITE-SANC-009 are Now drafts, and VA-WEBSITE-SANC-008 and VA-WEBSITE-SITE-004 are Next drafts. All four lack the Current state, Files touched, Dependencies / blocks and Documentation impact sections. VA-WEBSITE-SITE-003 is awaiting review without a complete review packet or a final Discussion. Shaping a record is `ki-plan` work in that repository and needs your authority there. **Query:** Should I launch a planning pass in apps-vallearmonia.com to close the 7 gaps? **Options:** a) (recommended, confidence medium - a bounded single-repository change, but every plan needs your approval to become Ready) Launch one `ki-plan` run in apps-vallearmonia.com that shapes the four drafts and completes VA-WEBSITE-SITE-003's review packet, leaving every record short of Ready until you approve it. b) Leave the gaps until those records are next selected.

### THEME-REGISTRY - Migrate territory theme registries

**Context:** No Capital in the six territories has `Streams/Themes/`. hnr-principal, legal-principal and personal-principal keep the legacy `Streams/Initiatives/` registry, which the audit warns on. er-principal, va-principal and tmx-principal have no registry at all, so every theme their records name goes unresolved. Several record themes appear in no registry, such as `harness-foundation`, `source-data`, `ki-conformance`, `housekeeping` and `dashboard`. **Query:** Should this Project raise theme-registry migration records in the territories' Capitals? **Options:** a) (recommended, confidence medium - the warnings are clear, but which themes each territory keeps is your call) Raise one record in each of hnr-principal, legal-principal and personal-principal to move Initiatives to `Streams/Themes/` pages. Leave er-principal, va-principal and tmx-principal without a registry until one of their records needs a theme. b) Raise a record in all six Capitals, giving each a theme registry now.

### CHECKER-GAPS - Report audit blind spots to the harness

**Context:** The Streams adapter applies neither ROAD-6 nor the area-declaration check, so slug-valued area titles in hnr-principal and tmx-principal pass unflagged, and so do va-principal's undeclared `GOV` and `KNW` areas. Separately, `ki repo audit --repo` refuses a symlinked repository path (`personal/dotfiles`). Changes to harness and tools belong to ki.ways-of-working and ki.tools-burndown, not to this Project. **Query:** Should these blind spots go to the harness and tools-ki as handoff items? **Options:** a) (recommended, confidence medium - the evidence is direct, but whether symlinks should be accepted is a design choice) Route the two Streams checker gaps to ki.ways-of-working, and the symlink refusal to ki.tools-burndown, each as one `messages.md` line. b) Note them in this Project only and take them up after the territory rollout.

### 🤖 → 👤 Handoff to supervisor · since 23:48 BST

👤 6 with you

- [with you] AREA-TITLES · owner · since 23:48
- [with you] LEDGER-FORM · owner · since 23:48
- [with you] SIZE-KIND · owner · since 23:48
- [with you] VA-PLANNING · owner · since 23:48
- [with you] THEME-REGISTRY · owner · since 23:48
- [with you] CHECKER-GAPS · owner · since 23:48
