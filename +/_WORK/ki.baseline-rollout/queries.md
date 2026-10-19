# ki.baseline-rollout queries

## Open

### REGISTER-HNR - Admit or exclude hnr-backend, hnr-frontend and hnr-benchmarks

since 2026-10-19 · from `wave1-audit` at 23:44 BST · blind-reviewed by `review-register-hnr` at 23:45 BST, which agreed

**Context:** Three active, clean repositories under `workspaces/humans-not-robots/`, each with a humansnotrobots origin and commits today, are not declared in hnr-principal's `territory_members` or Known Lands, not registered and have no `.ki.toml`; hnr-frontend has an AGENTS.md. Backend and frontend are already cited as evidence in hnr-principal's ADR consolidation, and hnr-benchmarks holds the frontend Playwright suites and backend measurements. HNR already admits product islands while keeping their own delivery rules; hnr-shared's exclusion concerns a content store, not product code. Admission is an HNR membership change through its Enactment Process, and writes in HNR repositories need your go repository by repository.

**Query:** Should these three repositories become Humans Not Robots territory members?

**Options:**

a) (recommended, confidence medium - reviewed: the blind review agreed all three are active parts of the HNR product that existing governance accommodates; live GitHub ownership not checked) Admit all three in a later wave: an HNR roadmap record through its Enactment Process reconciles the Charter, Known Lands and `territory_members`, each repository adopts a baseline `.ki.toml` keeping its delivery rules, then they are registered.

b) Leave all three outside the territory and record their exclusion in Known Lands.

c) Decide one at a time, for example admitting backend and frontend and leaving benchmarks out, which splits the product from its test repository.

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

## Parked

None.
