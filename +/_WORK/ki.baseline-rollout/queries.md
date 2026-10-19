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

## Parked

None.
