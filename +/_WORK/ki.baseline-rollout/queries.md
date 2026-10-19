# ki.baseline-rollout queries

## Open

### TERRITORY-TECHMEDIX - Techmedix audit stops on an archived, unregistered member

since 2026-10-19 · from `wave1-audit` at 23:44 BST · blind-reviewed by `review-territory-techmedix` at 23:46 BST, which agreed

**Context:** `ki territory audit -t techmedix` and `ki territory show` exit 2 before reporting anything, because tmx-principal declares `techmedix/apps-childhealthyorkshire.co.uk` as a member, Known Lands records it as archived read-only, and it has no local clone or registration; the other three Techmedix repositories are registered and fine. The strict selector is behaving as its contract says, so fixing this is a tools-ki behaviour change, not a bug fix. Cloning would only fix this machine; removing the member would change the governed set just to get a pass.

**Query:** Should Techmedix keep its declared membership while a tools-ki handoff makes audit and show report unavailable members and still check the rest?

**Options:**

a) (recommended, confidence high - reviewed: the blind review agreed; it keeps the verified membership and makes incomplete coverage visible through a bounded handoff) Hand a record to tools-ki (ki.tools-burndown) asking audit and show to name an unregistered declared member, check the available ones and still exit non-zero while coverage is incomplete, with strict selection kept for operational commands and the contract and tests reconciled; keep the declaration as it is.

b) Clone the archived repository and register it, which needs a network fetch and a registry change and fixes only this machine.

c) Remove it from `territory_members` through Techmedix's Enactment Process, keeping it in Known Lands as archived.

### REGISTER-HNR - Admit or exclude hnr-backend, hnr-frontend and hnr-benchmarks

since 2026-10-19 · from `wave1-audit` at 23:44 BST · blind-reviewed by `review-register-hnr` at 23:45 BST, which agreed

**Context:** Three active, clean repositories under `workspaces/humans-not-robots/`, each with a humansnotrobots origin and commits today, are not declared in hnr-principal's `territory_members` or Known Lands, not registered and have no `.ki.toml`; hnr-frontend has an AGENTS.md. Backend and frontend are already cited as evidence in hnr-principal's ADR consolidation, and hnr-benchmarks holds the frontend Playwright suites and backend measurements. HNR already admits product islands while keeping their own delivery rules; hnr-shared's exclusion concerns a content store, not product code. Admission is an HNR membership change through its Enactment Process, and writes in HNR repositories need your go repository by repository.

**Query:** Should these three repositories become Humans Not Robots territory members?

**Options:**

a) (recommended, confidence medium - reviewed: the blind review agreed all three are active parts of the HNR product that existing governance accommodates; live GitHub ownership not checked) Admit all three in a later wave: an HNR roadmap record through its Enactment Process reconciles the Charter, Known Lands and `territory_members`, each repository adopts a baseline `.ki.toml` keeping its delivery rules, then they are registered.

b) Leave all three outside the territory and record their exclusion in Known Lands.

c) Decide one at a time, for example admitting backend and frontend and leaving benchmarks out, which splits the product from its test repository.

### KI-BREW - Homebrew ki is one release behind

since 2026-10-19 · from `wave1-audit` at 23:44 BST

**Context:** The first `ki` on PATH, the tools-ki source runner, is at the released 0.11.5, but Homebrew's installed `ki` is 0.11.4 although the tap formula is at v0.11.5; contexts with a minimal PATH, such as launchd jobs or hooks, may run the older release. A new `ki` release is due tonight for the hooks migration, which may overtake this.

**Query:** Should Homebrew's `ki` be upgraded to the latest release?

**Options:**

a) (recommended, confidence high - a non-destructive upgrade to the released formula) Run `brew upgrade ki` once tonight's release is out, as a single authorised step on this machine.

b) Leave it as it is, since the source runner comes first on PATH for interactive sessions.

## Parked

- **CHECKLIST** - from the old ki.baseline-rollout package, held since 15 October: whether to adopt the stock Repository review Activity across the estate. Recommended: adopt it estate-wide only once Kris approves it for the Capital first.
- **PIN-PAYLOAD** - from the old ki.baseline-rollout package, parked 10 October with the pin-receiver idea: `update-ki-pin.yml` filters on `client_payload.source_repository` but tools-ki `release.yml` sends `client_payload.repository`, so `tool-release-published` dispatches would be skipped; the Capital's `.github/ki-version` and `update-ki-pin.yml` stay inert until the tools-release bot App and secrets are on it. Recommended: align the two field names when the pin-receiver idea is revived.
