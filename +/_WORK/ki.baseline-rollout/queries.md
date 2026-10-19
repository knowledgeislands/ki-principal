# ki.baseline-rollout queries

## Open

### TMX-AREA-TITLES - Confirm Techmedix area titles

since 2026-10-20 · from `raise-tmx` at 00:04 BST · awaiting blind review

**Context:** [TMX-PRINCIPAL-KB-008](/Users/krisbrown/workspaces/techmedix/tmx-principal/Streams/Roadmap/TMX-PRINCIPAL-KB-008-retitle-issuing-areas.md) replaces the retired slugs `company-record` (`CO`) and `knowledge-base` (`KB`) in `.ki.toml` with noun-phrase titles. Area codes and allocations do not change. `CO` issues commercial history, finance evidence and compliance work. `KB` issues base structure, source mirrors, naming and governance alignment.

**Query:** Which titles should the two Techmedix areas carry?

**Options:** a) (recommended, confidence medium - both fit the noun-phrase rule, but the wording is your call) `CO` = "Company records", `KB` = "Knowledge base". b) `CO` = "Company record and compliance", `KB` = "Knowledge base".

### TMX-THEMES - Confirm Techmedix themes

since 2026-10-20 · from `raise-tmx` at 00:04 BST · awaiting blind review

**Context:** Only two theme labels are in use in Techmedix: `company-record` on CO-001, CO-002 and CO-006, and `knowledge-base` on KB-003. The 13 October alignment assessment proposed `company-record` and `knowledge-stewardship` as the territory's two themes. `knowledge-base` reads as the old `KB` area slug, not a theme. [TMX-PRINCIPAL-KB-009](/Users/krisbrown/workspaces/techmedix/tmx-principal/Streams/Roadmap/TMX-PRINCIPAL-KB-009-establish-theme-registry.md) proposes two pages under `Streams/Themes/`.

**Query:** Which theme pages should the Techmedix registry hold?

**Options:** a) (recommended, confidence medium - it follows the assessment you already have, but the change relabels one record) Create `company-record` and `knowledge-stewardship`, and relabel KB-003 from `knowledge-base` to `knowledge-stewardship`. b) Create `company-record` and `knowledge-base`, leaving every record as it is.

### AREA-WORDING - Confirm the proposed area titles

since 2026-10-20 · from `raise-hnr` at 00:08 BST · awaiting blind review

**Context:** The four records propose these titles. 5g-emerge-apex: `GOV` KI conformance, `HK` Housekeeping, `OPS` Deployment operations, `WEB` Public website. 5g-emerge-demos: `CONTRACT` Interface contracts, `DBD` Dashboard, `DEPLOY` Deployment and tooling. 5g-emerge-testbed: `DATA` Source data, `GOV` KI conformance, `HK` Housekeeping, `OPS` Deployment operations. hnr-principal: `5GE` 5G-EMERGE programme, `ENG` Engineering, `FIN` Company finance, `KM` Knowledge management, `PRD` Product, `RES` Research. The shared codes reuse the titles 5g-emerge-phase2 already has. Every code and allocation stays as it is.

**Query:** Should the area titles be adopted as proposed when each record is adopted?

**Options:**

a) (recommended, confidence medium - the scratch audits pass, but the wording is your call) Confirm all the titles as proposed, so that each record can be adopted and delivered as written.

b) Confirm them with changes you name, which each record takes before adoption.

### DEMO-AREA - Issuing area for the demos record

since 2026-10-20 · from `raise-hnr` at 00:08 BST · awaiting blind review

**Context:** 5g-emerge-demos has no conformance area like its siblings' `GOV`. I therefore issued its record in `DEPLOY`, the nearest fit, because the only earlier `DEPLOY` record fixed a tooling audit. The record proposes retitling that area "Deployment and tooling" to match. Its identity stays the same whichever option you choose.

**Query:** Should 5g-emerge-demos keep conformance work in `DEPLOY`, or gain a `GOV` area?

**Options:**

a) (recommended, confidence medium - it adds nothing to the configuration, but a `GOV` area would match the sibling repositories) Keep `DEPLOY`, titled "Deployment and tooling", as the home for conformance and tooling work.

b) Add `GOV = "KI conformance"` in the same change, for future conformance records.

### SANC008-SPLIT - Split stage 4 out of the Sanctuary packaging record

since 2026-10-20 · from `va-plan` at 00:09 BST · awaiting blind review

**Context:** [VA-WEBSITE-SANC-008](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-008-package-the-sanctuary.md) covers stages 2 to 4 of ADR-VA-WEBSITE-009, which means three chained runs. Stage 4 alone moves 21 components and their test suites into `packages/sanctuary/` and changes the root workspaces, `turbo.json` and `bun.lock`. A record needing several chained runs needs a Delegation section, and an `xl` record cannot become Ready.

**Query:** Before VA-WEBSITE-SANC-008 becomes Ready, should stage 4 be split into its own record?

**Options:** a) (recommended, confidence medium - stage 4 differs in kind and risk from stages 2 and 3, but how big it is depends on how the tests move) Split stage 4 into a new record that VA-WEBSITE-SANC-008 blocks, and keep stages 2 and 3 here. b) Keep all three stages in one record at size `l`, with a Delegation section giving one run per stage.

### VA-READY - Which plans to approve as Ready

since 2026-10-20 · from `va-plan` at 00:09 BST · awaiting blind review

**Context:** All four drafts now have every planning section, but none has `size` yet. [VA-WEBSITE-CONT-005](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-CONT-005-resolve-image-review-flags.md) and [VA-WEBSITE-SITE-004](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SITE-004-choose-the-home-page-layout.md) are concrete and checkable. [VA-WEBSITE-SANC-009](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-009-close-the-editorial-audit.md) needs access to Kit's private audit doc. [VA-WEBSITE-SANC-008](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-008-package-the-sanctuary.md) waits on SANC008-SPLIT.

**Query:** Which of the four drafts should be approved to Ready, and when?

**Options:** a) (recommended, confidence medium - the plans are complete, but size must be settled before Ready and each step needs Kit's input) Once SIZE-KIND has set `size` and `kind`, approve VA-WEBSITE-CONT-005 and VA-WEBSITE-SITE-004. Approve VA-WEBSITE-SANC-009 once Kit's audit doc is reachable, and VA-WEBSITE-SANC-008 after SANC008-SPLIT. b) Keep all four in draft until each is next selected for delivery.

### LGL-THEMES - Legal's three obsolete theme labels

since 2026-10-20 · from `raise-capitals` at 00:13 BST · awaiting blind review

**Context:** [LGL-PRINCIPAL-OPS-029](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-029-migrate-initiatives-to-themes.md) moves Legal's six Initiatives to theme pages unchanged. Five records still name labels that have no page: `evidence-management` on EVD-003, EVD-004 and EVD-005, `financial-remedy` on FAM-004, and `criminal-casework` on CRM-001. These are exactly the seven exceptions that [LGL-PRINCIPAL-OPS-024](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-024-lossless-roadmap-metadata.md) left untouched for other reasons. OPS-024 itself removed the same labels from twelve other records, on the grounds that "obsolete themes are not replaced", and the fixed `EVD`, `FAM` and `CRM` areas still carry their meaning. OPS-024 is still awaiting your review.

**Query:** Should OPS-029 remove these three labels rather than give them theme pages?

**Options:**

a) (recommended, confidence medium - it follows the Capital's own OPS-024 rule, but you have not yet accepted that rule) Remove the label from the five records, changing nothing else but `updated_at`, and create no page.

b) Leave the five records as they are until each one's own disposition, and accept the warnings until then.

c) Give each label its own theme page.

### KB-THEMES - Personal's one stray theme label

since 2026-10-20 · from `raise-capitals` at 00:13 BST · awaiting blind review

**Context:** [KB-PRINCIPAL-047](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-047-migrate-initiatives-to-themes.md) moves Personal's six Initiatives (Acquire, Life, Thinking, Tower, Health and Rig) to theme pages unchanged. Every theme label in the territory resolves except `repository-governance`, which appears once, on KB-PRINCIPAL-011 (Reconcile KB Guidance). That record is projectless intake about the island's own guidance, and none of the six directions fits it. Separately, the Rig page keeps three parked ideas in its Notes, which sit awkwardly on a theme page; planning will decide whether they move.

**Query:** How should KB-PRINCIPAL-011's `repository-governance` label be reconciled?

**Options:**

a) (recommended, confidence medium - a judgement on one label; the record needs no theme to stay valid) Remove the label and create no page.

b) Create a seventh theme, `repository-governance`, for the island's own upkeep.

c) Qualify it to a Knowledge Islands theme, such as `knowledge-islands/foundations`.

### ER-THEMES - Equal Remedy's theme slugs

since 2026-10-20 · from `raise-capitals` at 00:13 BST · awaiting blind review

**Context:** Equal Remedy has no registry. Its records use five labels: `research` and `advocacy` (ER-PRINCIPAL-004 to 008), `resource-library` (ER-PRINCIPAL-011), and in the harness `operations` (ER-HARNESS-001) and `capabilities` (ER-HARNESS-002 to 022). The [territory alignment assessment](/Users/krisbrown/workspaces/equal-remedy/er-principal/-/territory-alignment-assessment.md) of 13 October proposed three directions and mapped every one of these records onto them: `territory-foundations`, `family-justice-reform` and `reusable-legal-capabilities`. Its question has been open since then as ALIGN in Equal Remedy's [queries](/Users/krisbrown/workspaces/equal-remedy/er-principal/+/_WORK/er/queries.md), with no options recorded. [ER-PRINCIPAL-016](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-016-establish-theme-registry.md) takes the theme half of that proposal. The Project, the record kinds and the governance repairs stay with [ER-PRINCIPAL-014](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-014-territory-alignment.md).

**Query:** Should Equal Remedy's themes be the assessment's three directions, with the five labels mapped onto them?

**Options:**

a) (recommended, confidence medium - the assessment was reviewed and covers every record, but its ALIGN question has never had options put to you) Adopt the three directions as theme pages and map the five labels as ER-PRINCIPAL-016 proposes. This answers the theme part of ALIGN and leaves the Project part open.

b) Keep the five existing labels and give each one a page.

c) Fold ER-PRINCIPAL-016 into ER-PRINCIPAL-014 and settle everything together when you answer ALIGN.

### VA-AREA-TITLES - Confirm Valle Armonia area titles

since 2026-10-20 · from `raise-va` at 00:15 BST · awaiting blind review

**Context:** [VA-PRINCIPAL-GOV-007](/Users/krisbrown/workspaces/valle-armonia/va-principal/Streams/Roadmap/VA-PRINCIPAL-GOV-007-declare-issuing-areas.md) adds a `[skills.ki-work-roadmap.areas]` map to `.ki.toml` for the two areas va-principal already issues. Codes and allocations do not change. `GOV` has issued two kinds of work: territory governance, meaning the bootstrap, the declaration and repository naming, and company running, meaning social accounts, operations and the footprint audit. `KNW` has issued the source mirrors and the work bringing community identity into the Principal.

**Query:** Which titles should the two Valle Armonia areas carry?

**Options:** a) (recommended, confidence medium - both fit the noun-phrase rule and cover what each area has issued, but the wording is your call) `GOV` = "Governance and operations", `KNW` = "Knowledge and sources". b) `GOV` = "Governance", `KNW` = "Knowledge base".

### VA-THEMES - Confirm Valle Armonia themes

since 2026-10-20 · from `raise-va` at 00:15 BST · awaiting blind review

**Context:** The territory uses nine theme labels and has no registry. In va-principal they are `governance` and `knowledge`. In apps-vallearmonia.com they are `content`, `site`, `operations`, `governance`, `members` and `webmcp`. In apps-markhowarth.com they are `design` and `launch`. Most of them mirror area codes, not themes. The `va` work package's open PROJECTS query already proposes these groups: Community presence, Company, and a Mark Howarth site group. [VA-PRINCIPAL-GOV-008](/Users/krisbrown/workspaces/valle-armonia/va-principal/Streams/Roadmap/VA-PRINCIPAL-GOV-008-establish-theme-registry.md) proposes two theme pages and reconciles every label to one of them.

**Query:** Which theme pages should the Valle Armonia registry hold?

**Options:** a) (recommended, confidence medium - it follows the grouping PROJECTS already proposes, but it relabels 18 records across three repositories and depends on your PROJECTS answer) Create `community-presence` and `company`. Relabel GOV-003 and KNW-001 to `company`, and the website and Mark Howarth labels to `community-presence`, through handoff items in those repositories. b) Create a page for each of the nine labels in use, leaving every record as it is.

### SIZEKIND-CONFIRM-1 - Confirm the size and kind proposals for humans-not-robots, legal and personal

since 2026-10-20 · from `sizekind-1` at 00:15 BST · tables in `report-sizekind-1.md` · awaiting blind review

**Context:** The tables above propose a `size` for 129 open records and a `kind` for 21 adopted records in 12 repositories, plus the mechanical `initiative` to `theme` fix on 4 dotfiles records. Rows marked "Uncertain" carry the proposal's own doubt. The standard says size and kind need judgement: a run proposes them, the owner confirms them, and the migration runs one repository at a time. Sizes set now stay provisional and are revisited before each record becomes Ready.

**Query:** Should the write passes apply these tables as proposed, one repository at a time?

**Options:** a) (recommended, confidence medium - most rows follow plainly from the record's plan, but 14 rows carry a stated uncertainty) Confirm each repository's table as proposed, naming any row to change, then run one write pass per repository that also makes the dotfiles `theme` fix. b) Review the flagged "Uncertain" rows one by one before any write pass, and confirm the rest wholesale.

### SPLIT-5GE-004 - Split the Phase 2 and MS3 completion record

since 2026-10-20 · from `sizekind-1` at 00:15 BST · tables in `report-sizekind-1.md` · awaiting blind review

**Context:** [HNR-PRINCIPAL-5GE-004](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-5GE-004-phase-2-ms3-completion.md) is a triage record covering telemetry integrations, operational ownership, registry entries, dashboards, outputs and the wider MS3 obligations. It reads as several records, so it is proposed as `xl`. An `xl` record is allowed in triage but must be split before it becomes Ready.

**Query:** Should HNR-PRINCIPAL-5GE-004 be recorded as `xl` and left for hnr-principal to split when it adopts the record?

**Options:** a) (recommended, confidence medium - the scope plainly spans several deliveries, but the split is hnr-principal's call) Record `size: xl` now and leave the split to hnr-principal's triage review. b) Record `size: l` and treat it as one chained delivery.

### SIZEKIND-CONFIRM-2 - Confirm the size and kind proposals for Equal Remedy, Valle Armonia and Techmedix

since 2026-10-20 · from `sizekind-2` at 00:19 BST · tables in `report-sizekind-2.md` · awaiting blind review

**Context:** The tables above propose 61 sizes and 40 kinds across six repositories. Each row carries its own confidence. 57 rows are high or medium and rest on the record text and the standard's shapes. The 4 low rows (ER-PRINCIPAL-004, VA-WEBSITE-MEM-001, VA-WEBSITE-WEB-001 and TMX-PRINCIPAL-KB-003) are flagged as needing investigation. The standard says a run proposes and you confirm, one repository at a time, before a write pass. Each write pass stages one repository's records by explicit path and follows that repository's AGENTS.md.

**Query:** Which proposals should the write passes apply?

**Options:**

a) (recommended, confidence medium - the high and medium rows follow the record text closely, and the low rows are honest guesses the standard says to investigate) Apply every high and medium row in all six repositories, one write run per repository, and leave the low rows without `size` until each record's next planning pass.

b) Apply every row, low ones included, and revisit sizes before Ready as the standard already requires.

c) Confirm repository by repository, starting with the largest, er-agentic-harness.

### ICO-DATE - TechMedix's ICO registration may already have lapsed

since 2026-10-20 · from `sizekind-2` at 00:19 BST · tables in `report-sizekind-2.md` · awaiting blind review

**Context:** [TMX-PRINCIPAL-CO-006](/Users/krisbrown/workspaces/techmedix/tmx-principal/Streams/Roadmap/TMX-PRINCIPAL-CO-006-resolve-ico-data-protection-fee.md) is unadopted triage. It records renewal coverage through 16 October 2026, an unpaid reminder dated 16 September, and a goal of avoiding "a registration lapse or a duplicate payment". Today is 20 October, four days after that coverage date. This run cannot see whether anything has been paid. Adoption and priority belong to TechMedix's Capital, not to this rollout.

**Query:** Should the ICO question be raised with TechMedix's Capital now, outside the size and kind backfill?

**Options:**

a) (recommended, confidence medium - the date has passed on the record's own evidence, but payment may have happened outside the repository) Route one line to the TechMedix master thread's `messages.md` asking it to check the registration status and consider adopting the record at `high` priority.

b) Leave it as triage with size `s` and let TechMedix pick it up in its own time.

## Parked

None.
