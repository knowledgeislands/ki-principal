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

## Parked

None.
