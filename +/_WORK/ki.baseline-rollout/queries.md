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

### HNR-QUEUE - Tell hnr's own work package about these records

since 2026-10-20 · from `raise-hnr` at 00:08 BST · awaiting blind review

**Context:** hnr-principal's `hnr` work package has two open queries of its own that these records touch. Its AREA-TITLES asks whether to title the areas across the Capital and the 5g-emerge repositories in one pass, and HNR-PRINCIPAL-KM-019 now carries that work. Its INIT-MODEL asks which Initiatives the territory keeps, and that decides the theme set HNR-PRINCIPAL-KM-020 needs. I did not write to that work package, because the brief did not cover it.

**Query:** Should a line go to the `hnr` work package's `messages.md`, pointing its AREA-TITLES query at HNR-PRINCIPAL-KM-019 and its INIT-MODEL query at HNR-PRINCIPAL-KM-020?

**Options:**

a) (recommended, confidence high - it only routes information and decides nothing) Route one `messages.md` line to `hnr` naming both records, so its worker can link or settle its own queries.

b) Leave it, and let the hnr worker find the records at its next take-stock.

## Parked

None.
