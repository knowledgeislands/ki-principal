# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › fields-rest

**🤖 → 👤 Handoff to supervisor · Run report at 14:24 BST · last mark 13:37 BST**

---

## Done

Field migration is finished in all nine repositories on the list. Six are pushed. Three are committed but not pushed, because a push to `main` in each of them deploys a site (DEPLOY-PUSH). A fresh scan now finds no retired horizon, no `initiative` and no theme beside a Project in any non-KI repository outside chezmoi. The net record count is 0 in every repository.

- **hnr-principal:** 8 drafts on `horizon: triage` moved to `status: triage`. Commit `8d98226`, pushed fast-forward, now level. The Streams audit gave FAIL 8 and WARN 29 both before and after, the same findings line for line; the 8 failures are pre-existing STREAM-9 registry-note findings. `ki-work` passed. The front-matter scan went from 8 retired horizons to 0.
- **5g-emerge-phase2:** 5 records changed. 3 Waiting for and 1 Parked moved to Hold, and 1 triage draft moved to `status: triage`. Commit `9780421` passed the gate; **not pushed** (DEPLOY-PUSH). `ki-work-roadmap` went from FAIL 7 to FAIL 2; the 2 left are pre-existing ITEM-3 body-shape failures. Its warnings rose from 18 to 22: the 4 Hold records now draw the expected "declare kind" warning, which waits for the `ki` release. The full audit went from FAIL 18 to FAIL 13. `ki-work` passed. Four Hold conditions need you (HOLD-CONDITIONS).
- **legal-principal:** 1 Parked record moved to Hold and 2 triage drafts moved to `status: triage`. Commit `86f112c6`, pushed and level. The Streams audit gave FAIL 0 and WARN 29 before and after, identical. `ki-work` passed. As expected, the full audit stops on the COORD-1 tool error before and after.
- **hnr-agentic-harness:** 2 triage drafts moved. Commit `702326c` passed the gate, pushed and level. `ki-work-roadmap` went from FAIL 2 to 0, with WARN 10 both times. The full audit went from FAIL 12 to 10.
- **tmx-principal:** 2 triage drafts moved. Commit `55cc0c9`, pushed and level. The Streams audit gave FAIL 0 and WARN 6 before and after, identical. `ki-work` passed, and COORD-1 stops the full audit.
- **5g-emerge-demos:** 1 triage draft moved. Commit `c51f38c` passed the gate; **not pushed** (DEPLOY-PUSH). `ki-work-roadmap` went from FAIL 4 to 3, and the 3 left are pre-existing. The full audit went from FAIL 12 to 11.
- **er-principal:** 1 triage draft moved. Commit `9f8aafb`, pushed and level. The Streams audit gave FAIL 0 and WARN 8 before and after, identical. COORD-1 stops the full audit.
- **va-principal:** 1 triage draft moved. Commit `9b24734`, pushed and level. The Streams audit gave FAIL 0 and WARN 6 before and after, identical.
- **apps-tower.midnight.ninja:** a scripted pass renamed `initiative: tower` to `theme: tower` on 6 records, run as a dry run and then applied: [KB-MIDNIGHT-TOWER-SITE-002](/Users/krisbrown/workspaces/personal/apps-tower.midnight.ninja/docs/roadmap/KB-MIDNIGHT-TOWER-SITE-002-adopt-binary-primary-source.md) (done; its status was left alone), [012](/Users/krisbrown/workspaces/personal/apps-tower.midnight.ninja/docs/roadmap/KB-MIDNIGHT-TOWER-SITE-012-weekly-maintenance-sweep.md), [013](/Users/krisbrown/workspaces/personal/apps-tower.midnight.ninja/docs/roadmap/KB-MIDNIGHT-TOWER-SITE-013-make-refresh-verification-repeatable.md), [014](/Users/krisbrown/workspaces/personal/apps-tower.midnight.ninja/docs/roadmap/KB-MIDNIGHT-TOWER-SITE-014-plan-tower-data-model.md), [015](/Users/krisbrown/workspaces/personal/apps-tower.midnight.ninja/docs/roadmap/KB-MIDNIGHT-TOWER-SITE-015-deliver-modules-first-model.md) and [018](/Users/krisbrown/workspaces/personal/apps-tower.midnight.ninja/docs/roadmap/KB-MIDNIGHT-TOWER-SITE-018-show-inactive-preset-wallets.md). `tower` is a Personal Initiative (`Streams/Initiatives/tower.md`), which the work model makes a theme. Each record's `updated_at` was advanced. Commit `35dcc64`; **not pushed** (DEPLOY-PUSH). `ki-work-roadmap` went from WARN 14 to 8 as the six `initiative` warnings cleared, with FAIL 0 both times. The full audit went from WARN 16 to 10, with FAIL 8 both times.
- **The rest of the inventory:** a fresh scan of every other non-KI repository found no mechanical debt. That covers er-agentic-harness, apps-vallearmonia.com, infoschematics, 5g-emerge-phase3, si-principal and acquire, among others. Their remaining debt is kind and size only. In roadmap repositories that waits for the `ki` release, so nothing was written. `personal/dotfiles`, the chezmoi repository, still has 4 `initiative` fields; I left them for ki.chezmoi as briefed.
- **Method:** `ki repo roadmap migrate` (ki 0.11.4), always a dry run first. Before applying, I listed each record's status beside its retired horizon: every one was a draft, so no ready or in-progress record was involved. No repository here had a theme beside a Project, so no finer grouping was lost. I proved each result with a front-matter scan, because the Streams checker still cannot see these fields (STREAMS-CHECKER-GAP holds). The roadmap checker does flag them. Every commit was staged by explicit path.
- **Audit tooling:** the installed harness is a symlink to the workspace ki-agentic-harness checkout. When I started, another run (work-package-standard) was midway through renaming `ki-work-folder` to `ki-work-package` there. Every `ki repo audit` stopped on "ki-work-folder rubric catalogue could not be imported". So I ran every before and after audit against a clean snapshot of the committed harness, `88cce3e5`, through a temporary `XDG_DATA_HOME`. The installed configuration was not changed.

### Kind and size proposals (not written)

These cover every open record in the six Streams repositories that lacks a kind or a size. They come to 18 kinds for adopted records, 30 kinds for triage records to set at adoption, and 69 new sizes. Sizes follow GDR-KI-PRINCIPAL-016: `s` is one run and one commit, `m` one run with several commits and a plan, and `l` several chained runs or repositories. They are judgements from each record's title and Goal, and they are revisited before Ready.

| Record | State | Kind | Size |
| --- | --- | --- | --- |
| [HNR-PRINCIPAL-5GE-002](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-5GE-002-file-phase-3-partner-engagement-leaflet.md) File and reconcile the Phase 3 partner engagement leaflet | triage | deliver | s |
| [HNR-PRINCIPAL-5GE-003](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-5GE-003-coordinate-phase-3-integration.md) Coordinate Phase 3 integration | triage | deliver | l |
| [HNR-PRINCIPAL-5GE-004](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-5GE-004-complete-phase-2-ms3.md) Phase 2 MS3 completion ‡ | triage | deliver | l |
| [HNR-PRINCIPAL-5GE-005](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-5GE-005-keep-ebu-sources-aligned.md) Keep EBU sources aligned | triage | deliver | m |
| [HNR-PRINCIPAL-5GE-007](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-5GE-007-review-fourth-outline.md) Review fourth outline | awaiting-review · now | deliver (already set) | m |
| [HNR-PRINCIPAL-5GE-008](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-5GE-008-deliver-wp4-calendar.md) Deliver WP4 calendar | awaiting-review · now | deliver (already set) | m |
| [HNR-PRINCIPAL-5GE-009](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-5GE-009-separate-wp4-pages.md) Separate WP4 pages | awaiting-review · now | deliver (already set) | s |
| [HNR-PRINCIPAL-5GE-010](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-5GE-010-align-wp4-outline-manuscript.md) Align WP4 manuscript | awaiting-review · now | deliver (already set) | m |
| [HNR-PRINCIPAL-ENG-001](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-ENG-001-design-domain-aligned-slack-channels-and-change-feeds.md) Design domain-aligned Slack channels and change feeds | triage | decide | m |
| [HNR-PRINCIPAL-ENG-002](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-ENG-002-redraw-hnr-shared-mermaid-diagrams-in-archify.md) Redraw hnr-shared Mermaid diagrams in Archify | triage | deliver | m (already set) |
| [HNR-PRINCIPAL-FIN-001](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-FIN-001-resolve-bridge-funding-consent.md) Resolve bridge funding consent | in-progress · now | decide | l |
| [HNR-PRINCIPAL-FIN-002](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-FIN-002-complete-xero-expense-reconciliation.md) Complete Xero expense reconciliation | triage | deliver | m |
| [HNR-PRINCIPAL-KM-005](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-KM-005-operationalise-hnr-council.md) Operationalise the HNR Council | triage | deliver | l |
| [HNR-PRINCIPAL-KM-009](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-KM-009-email-triage-retention-and-schedule-governance.md) Email triage retention and schedule governance | in-progress · now | deliver | m |
| [HNR-PRINCIPAL-KM-011](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-KM-011-designate-roadmap-writing-checkout.md) Designate roadmap writing checkout | draft · next | decide | s |
| [HNR-PRINCIPAL-KM-016](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-KM-016-redirect-granola-acquisition.md) Redirect Granola Acquisition | awaiting-review · now | deliver (already set) | s |
| [HNR-PRINCIPAL-KM-017](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-KM-017-review-repository-naming.md) Review repository naming | triage | decide | s |
| [HNR-PRINCIPAL-PRD-001](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-PRD-001-bottom-out-dashboards-and-navigation.md) Bottom out dashboards and navigation | draft · now | decide | l |
| [HNR-PRINCIPAL-PRD-003](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-PRD-003-design-resource-scoped-edit-presence.md) Design resource-scoped edit presence | triage | decide | m |
| [HNR-PRINCIPAL-PRD-004](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-PRD-004-develop-next-hnr-product-strategy-synthesis.md) Develop the next HNR product strategy synthesis | draft · now | investigate | l |
| [HNR-PRINCIPAL-PRD-008](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-PRD-008-recover-co-stars-ibc-discussion.md) Recover Co-Stars discussion | triage | investigate | s |
| [LGL-PRINCIPAL-ASS-001](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-ASS-001-privilege-boundary.md) Privilege boundary | draft · soon | deliver (already set) | s |
| [LGL-PRINCIPAL-CRM-001](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-CRM-001-criminal-ccb-pack.md) Criminal CCB pack | draft · hold | deliver | l |
| [LGL-PRINCIPAL-EVD-001](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-EVD-001-whatsapp-archive-import.md) WhatsApp archive import | draft · next | deliver (already set) | m |
| [LGL-PRINCIPAL-EVD-002](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-EVD-002-device-originals-filing.md) Device originals filing | draft · next | deliver (already set) | m |
| [LGL-PRINCIPAL-EVD-003](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-EVD-003-backlog-residue-disposition-run.md) Backlog residue disposition run | draft · next | deliver | m |
| [LGL-PRINCIPAL-EVD-004](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-EVD-004-source-coverage-census.md) Source coverage census | draft · soon | audit | s |
| [LGL-PRINCIPAL-EVD-005](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-EVD-005-adopt-shared-mirror-shape.md) Adopt shared mirror shape | triage | deliver | m |
| [LGL-PRINCIPAL-FAM-001](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-FAM-001-family-chronology.md) Family chronology | ready · next | deliver (already set) | m |
| [LGL-PRINCIPAL-FAM-002](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-FAM-002-applicant-financial-disclosure-analysis.md) Applicant Financial Disclosure Analysis | in-progress · now | deliver (already set) | l |
| [LGL-PRINCIPAL-FAM-004](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-FAM-004-techmedix-director-loan-tax-review.md) Techmedix director loan tax review | in-progress · next | investigate | m |
| [LGL-PRINCIPAL-OPS-002](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-002-correspondence-drafts.md) Correspondence drafts | in-progress · next | deliver | m |
| [LGL-PRINCIPAL-OPS-005](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-005-live-artifact-reconciliation.md) Live artifact reconciliation | draft · now | deliver (already set) | m |
| [LGL-PRINCIPAL-OPS-009](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-009-complete-inbound-legal-gmail-triage.md) Inbound Legal Gmail Triage | in-progress · now | deliver (already set) | m |
| [LGL-PRINCIPAL-OPS-012](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-012-command-centre-working-material-consolidation.md) Command Centre working-material consolidation | draft · next | deliver (already set) | l |
| [LGL-PRINCIPAL-OPS-013](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-013-repository-learning-to-skills-programme.md) Repository learning-to-skills programme | draft · next | deliver (already set) | l |
| [LGL-PRINCIPAL-OPS-016](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-016-reduce-migrated-resource-duplicates.md) Reduce migrated resource duplicates | in-progress · now | deliver (already set) | m |
| [LGL-PRINCIPAL-OPS-018](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-018-acquire-granola-legal-meetings.md) Acquire Granola legal meetings | triage | deliver | m |
| [LGL-PRINCIPAL-OPS-019](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-019-command-centre-operational-state-reconciliation.md) Command Centre operational-state reconciliation | in-progress · now | deliver (already set) | m |
| [LGL-PRINCIPAL-OPS-021](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-021-redirect-granola-acquisition.md) Redirect Granola Acquisition | awaiting-review · now | deliver (already set) | s |
| [LGL-PRINCIPAL-OPS-022](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-022-bounded-legal-tidy-alignment.md) Bounded Legal Tidy Alignment | awaiting-review · now | deliver (already set) | m |
| [LGL-PRINCIPAL-OPS-023](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-023-additive-registry-grouping.md) Additive Registry Grouping | awaiting-review · now | deliver (already set) | s |
| [LGL-PRINCIPAL-OPS-024](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-024-lossless-roadmap-metadata.md) Lossless Roadmap Metadata | awaiting-review · now | deliver (already set) | s |
| [LGL-PRINCIPAL-OPS-025](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-025-dependency-security-remediation.md) Dependency Security Remediation | triage | deliver | s |
| [LGL-PRINCIPAL-OPS-026](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-026-review-repository-naming.md) Review repository naming | triage | decide | s |
| [LGL-PRINCIPAL-OPS-027](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-027-cowork-scheduled-task-follow-through.md) Cowork Scheduled Task Follow-Through | awaiting-review · now | deliver (already set) | m |
| [LGL-PRINCIPAL-OPS-028](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-028-redraw-mermaid-diagrams-in-archify.md) Redraw Mermaid diagrams in Archify | triage | deliver | s (already set) |
| [LGL-PRINCIPAL-RES-002](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-RES-002-verified-financial-remedy-statutory-authority-notes.md) Verified financial remedy statutory authority notes | triage | deliver | m |
| [LGL-PRINCIPAL-RES-003](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-RES-003-verified-case-authority-on-non-disclosure-inferences.md) Verified case authority on non-disclosure inferences | triage | deliver | m |
| [LGL-PRINCIPAL-TMX-001](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-TMX-001-missing-techmedix-messages.md) Missing Techmedix messages | draft · soon | deliver (already set) | s |
| [TMX-PRINCIPAL-CO-001](/Users/krisbrown/workspaces/techmedix/tmx-principal/Streams/Roadmap/TMX-PRINCIPAL-CO-001-commercial-spine.md) Commercial spine | draft · next | deliver | l |
| [TMX-PRINCIPAL-CO-002](/Users/krisbrown/workspaces/techmedix/tmx-principal/Streams/Roadmap/TMX-PRINCIPAL-CO-002-finance-evidence-register.md) Finance evidence register and annual books | in-progress · now | deliver | l |
| [TMX-PRINCIPAL-CO-006](/Users/krisbrown/workspaces/techmedix/tmx-principal/Streams/Roadmap/TMX-PRINCIPAL-CO-006-resolve-ico-data-protection-fee.md) Resolve ICO data protection fee ‡ | triage | investigate | s |
| [TMX-PRINCIPAL-KB-003](/Users/krisbrown/workspaces/techmedix/tmx-principal/Streams/Roadmap/TMX-PRINCIPAL-KB-003-complete-source-mirrors.md) Complete source store mirrors | triage | deliver | l |
| [TMX-PRINCIPAL-KB-006](/Users/krisbrown/workspaces/techmedix/tmx-principal/Streams/Roadmap/TMX-PRINCIPAL-KB-006-review-repository-naming.md) Review repository naming | triage | decide | s |
| [TMX-PRINCIPAL-KB-007](/Users/krisbrown/workspaces/techmedix/tmx-principal/Streams/Roadmap/TMX-PRINCIPAL-KB-007-territory-work-governance-alignment.md) Territory work alignment | triage | audit | m |
| [ER-PRINCIPAL-004](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-004-legal-and-policy-landscape.md) Legal and policy landscape | draft · future | investigate | l |
| [ER-PRINCIPAL-005](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-005-harm-panel-and-parental-involvement.md) Harm Panel and parental involvement | draft · future | investigate | m |
| [ER-PRINCIPAL-006](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-006-parliamentary-engagement.md) Parliamentary engagement | draft · future | deliver | m |
| [ER-PRINCIPAL-007](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-007-media-briefing.md) Media briefing | draft · future | deliver | m |
| [ER-PRINCIPAL-008](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-008-documentary-and-journalist-outreach.md) Documentary and journalist outreach | draft · future | investigate | s |
| [ER-PRINCIPAL-011](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-011-complete-source-mirrors.md) Complete source store mirrors | triage | deliver | l |
| [ER-PRINCIPAL-013](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-013-review-repository-naming.md) Review repository naming | triage | decide | s |
| [ER-PRINCIPAL-014](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-014-territory-alignment.md) Territory alignment | triage | audit (already set) | m |
| [ER-PRINCIPAL-015](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-015-redraw-mermaid-diagrams-in-archify.md) Redraw Mermaid diagrams in Archify | triage | deliver | s (already set) |
| [VA-PRINCIPAL-GOV-002](/Users/krisbrown/workspaces/valle-armonia/va-principal/Streams/Roadmap/VA-PRINCIPAL-GOV-002-establish-community-social-accounts.md) Establish community social accounts | triage | deliver | m |
| [VA-PRINCIPAL-GOV-003](/Users/krisbrown/workspaces/valle-armonia/va-principal/Streams/Roadmap/VA-PRINCIPAL-GOV-003-company-operations.md) Company Operations | in-progress · now | deliver | m |
| [VA-PRINCIPAL-GOV-005](/Users/krisbrown/workspaces/valle-armonia/va-principal/Streams/Roadmap/VA-PRINCIPAL-GOV-005-audit-the-social-media-footprint.md) Audit social media footprint | triage | audit | s |
| [VA-PRINCIPAL-GOV-006](/Users/krisbrown/workspaces/valle-armonia/va-principal/Streams/Roadmap/VA-PRINCIPAL-GOV-006-review-repository-naming.md) Review repository naming | triage | decide | s |
| [VA-PRINCIPAL-KNW-001](/Users/krisbrown/workspaces/valle-armonia/va-principal/Streams/Roadmap/VA-PRINCIPAL-KNW-001-complete-source-mirrors.md) Complete source store mirrors | triage | deliver | m |
| [VA-PRINCIPAL-KNW-002](/Users/krisbrown/workspaces/valle-armonia/va-principal/Streams/Roadmap/VA-PRINCIPAL-KNW-002-bring-community-identity-into-principal.md) Bring identity into Principal | triage | deliver | m |
| [SI-PRINCIPAL-KB-001](/Users/krisbrown/workspaces/sacred-inquiry/si-principal/Streams/Roadmap/SI-PRINCIPAL-KB-001-receive-personal-spiritual-material.md) Receive Spiritual Material | awaiting-review · now | deliver (already set) | m |

‡ Date-bound, and it lost adoption in this run (REST-READOPT).

## In Progress

Nothing is running.

Outstanding - no action requested now:

- 5g-emerge-phase2's twice-daily source refresh pushes `main` whenever its sources change, and that would carry `9780421` out with it if DEPLOY-PUSH is still open.
- COORD-1 still stops the full `ki repo audit` in legal-principal, tmx-principal, er-principal and va-principal, as it did before this run.
- `personal/dotfiles` has 4 `initiative` fields that belong to ki.chezmoi.
- Kind and size backfill in the roadmap repositories waits for the `ki` release under KI-TOOL-KI-CLI-155.

## Queries

### DEPLOY-PUSH - Whether to push three commits whose push deploys a site

**Context:** The brief allows a fast-forward push when only my commit is stacked, and that holds in all three repositories. In 5g-emerge-phase2, 5g-emerge-demos and apps-tower.midnight.ninja, though, Cloudflare Workers Builds deploys the site on every push to `main`, and 5g-emerge-phase2's AGENTS.md says to treat a push as a deploy decision. Each commit touches only `docs/roadmap/` front matter, and you said these territories are not in use.

**Query:** Should the three commits (`9780421`, `c51f38c`, `35dcc64`) be pushed now, which redeploys the three sites?

**Options:**

a) (recommended, confidence medium - only roadmap front matter changed and the territories are idle, but I have not checked whether the sites render roadmap pages) Push all three now, fast-forward after a rebase pull.

b) Leave them local until each repository's next deliberate deploy. For 5g-emerge-phase2 that means letting the source refresh carry it.

### HOLD-CONDITIONS - Release conditions on the five records moved to Hold

**Context:** `migrate` lifted a Hold condition from each record's prose or wrote a REVIEW placeholder. One is a placeholder and four are lifted text that is not a release condition. [5GE-P2-GOV-014](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase2/docs/roadmap/5GE-P2-GOV-014-propose-an-unsettled-source-review-lens.md) has `REVIEW: name the release condition`, and its prose waits on [KI-HARNESS-GOV-123 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/45493030/docs/roadmap/KI-HARNESS-GOV-123-review-unsettled-source-readings.md). [5GE-P2-GOV-015](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase2/docs/roadmap/5GE-P2-GOV-015-propose-artefact-idempotence-lens.md) carries a closing instruction, and its prose waits on [KI-HARNESS-GOV-124 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/7d7cdde1/docs/roadmap/KI-HARNESS-GOV-124-review-artefact-idempotence.md). Both harness records are done and pruned, so those two waits are already over. [5GE-P2-DATA-002](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase2/docs/roadmap/5GE-P2-DATA-002-resolve-open-source-queries.md) carries the text of one query, SDQ-023; its prose waits on the 2026-10-01 hand-over pack reaching Darko and the source owners answering. [5GE-P2-HK-012](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase2/docs/roadmap/5GE-P2-HK-012-finish-grand-unified-testbed-page.md) carries a history line; its prose waits on BFBS partner positioning and the owner of the architecture narrative. [LGL-PRINCIPAL-CRM-001](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-CRM-001-criminal-ccb-pack.md) carries the authority-verification rule, and its prose names no release condition.

**Query:** Should a short follow-up run rewrite these five conditions from the record prose, and move GOV-014 and GOV-015, whose waits are over, to their next step?

**Options:**

a) (recommended, confidence medium - four conditions come straight from each record's own Dependencies section; CRM-001 needs your words) Run it: write the prose conditions for DATA-002, HK-012, GOV-014 and GOV-015, release GOV-014 and GOV-015 through `ki-next` for review against the harness outcome, and set CRM-001's condition to the words you give.

b) Leave the conditions as `migrate` wrote them until each record is next reviewed.

### REST-READOPT - Whether the 18 drafts that left adoption are re-adopted

**Context:** The mechanical rule moved 18 drafts on `horizon: triage` to `status: triage`: 8 in hnr-principal, 2 in legal-principal, 2 in hnr-agentic-harness, 2 in tmx-principal, and 1 each in 5g-emerge-phase2, 5g-emerge-demos, er-principal and va-principal. In the old model that combination meant captured intake, so the meaning holds. Two are date-bound. [HNR-PRINCIPAL-5GE-004](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-5GE-004-complete-phase-2-ms3.md) (Phase 2 MS3 completion) names work due "before 19 October", which is today. [TMX-PRINCIPAL-CO-006](/Users/krisbrown/workspaces/techmedix/tmx-principal/Streams/Roadmap/TMX-PRINCIPAL-CO-006-resolve-ico-data-protection-fee.md) is an unpaid ICO fee where the registration risks lapsing.

**Query:** Should the two date-bound records be adopted now while the other 16 stay in triage?

**Options:**

a) (recommended, confidence medium - the result matches the old meaning, and only these two carry a dated consequence) Adopt HNR-PRINCIPAL-5GE-004 and TMX-PRINCIPAL-CO-006 now through `ki-next` at Now with the proposed kind and size, and leave the other 16 for ordinary intake review.

b) Leave all 18 in triage, since these territories are not in use.

### REST-KIND-SIZE - Confirming the proposed kind and size

**Context:** The table above proposes 18 kinds for adopted records, 30 kinds for triage records to set at adoption, and 69 sizes across hnr-principal, legal-principal, tmx-principal, er-principal, va-principal and si-principal. GDR-KI-PRINCIPAL-016 makes these your judgement, and the Streams writers already accept `size`.

**Query:** Do you confirm the proposals, with any changes, so that a follow-up run can write them?

**Options:**

a) (recommended, confidence medium - provisional judgements from each Goal, revisited before Ready anyway) Confirm them as listed. A follow-up run writes the 69 sizes and 18 adopted kinds now, and the triage kinds are set at adoption.

b) Confirm them with the changes you name.

c) Hold every kind and size write until the `ki` release, and write them together with the roadmap repositories.

### 🤖 → 👤 Handoff to supervisor · since 14:24 BST

👤 4 with you · 🤖 0 running · ⬆️ 3 unpushed

- [with you] DEPLOY-PUSH · owner · since 14:24
- [with you] HOLD-CONDITIONS · owner · since 14:24
- [with you] REST-READOPT · owner · since 14:24
- [with you] REST-KIND-SIZE · owner · since 14:24
- [committed] hnr-principal, legal-principal, hnr-agentic-harness, tmx-principal, er-principal, va-principal, pushed
- [unpushed] 5g-emerge-phase2, 5g-emerge-demos, apps-tower.midnight.ninja
