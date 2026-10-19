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

### AREA-TITLES - Retitle retired theme-slug areas

since 2026-10-19 · from `wave1-sweep` at 23:49 BST · in blind review

**Context:** The area-to-theme map in `.ki.toml` is retired. An area title should now be a short capitalised noun phrase. Five repositories still use theme slugs as area titles, 19 in all: 5g-emerge-apex, 5g-emerge-demos, 5g-emerge-testbed (all three failing ROAD-6), hnr-principal and tmx-principal. None of the slugs is a live KI theme. Separately, va-principal issues `GOV` and `KNW` records but declares no area map. legal-principal and 5g-emerge-phase2 already show the target form. The fix is a `.ki.toml` edit in each repository, which needs your authority. **Query:** Should I raise conformance records to retitle these areas, and declare va-principal's map, in each territory's repositories? **Options:** a) (recommended, confidence medium - the edit is mechanical, but the titles need wording you approve) Raise one conformance record per affected repository, routed through each territory's Capital: the three 5g-emerge repositories and hnr-principal through hnr-principal, tmx-principal on its own, and va-principal on its own. Each record proposes noun-phrase titles for you to confirm. b) Raise one combined record in each Capital, hnr-principal, tmx-principal and va-principal, covering its territory's repositories.

### LEDGER-FORM - Repair superseded issue ledgers

since 2026-10-19 · from `wave1-sweep` at 23:49 BST · in blind review

**Context:** Seven project-roadmap ledgers still use a superseded canonical form, which the audit warns on: 5g-emerge-apex, 5g-emerge-demos, 5g-emerge-testbed, apps-kris.me.uk, apps-dafacts.org, er-agentic-harness and apps-markhowarth.com. The three 5g-emerge ledgers also fail for being in the wrong issuing mode. That is probably a knock-on effect of their slug-valued area maps, though I have not verified it. `ki repo conform --skill ki-work-roadmap` rewrites a superseded ledger and keeps its allocation, but HOOK-GUARD bars conform until ki.tools-burndown lifts it. **Query:** How should the superseded ledgers be repaired? **Options:** a) (recommended, confidence medium - conform is the designed repair but is held, and the wrong-mode cause is inferred) Fold the three 5g-emerge ledgers into their AREA-TITLES records. Repair the other four with a `--dry-run`-checked conform once HOOK-GUARD lifts, one repository at a time on your go. b) Hand-edit all seven ledgers now under conformance records, without waiting for conform.

### SIZE-KIND - Backfill size and kind

since 2026-10-19 · from `wave1-sweep` at 23:49 BST · in blind review

**Context:** 191 open records in 18 repositories have no `size`, and 61 adopted open records have no `kind`. The largest gaps are personal-principal (33), legal-principal (28), er-agentic-harness (22, all also without kind), hnr-principal (20), dotfiles (16) and apps-vallearmonia.com (15). The field migration window opened on 2026-10-19 and closes on a complete clean scan or a 60-day backstop, after which these warnings become fails. The standard says size and kind need judgement: a run proposes them and you confirm them, one repository at a time. dotfiles also has 4 records still naming `initiative`, which is a mechanical fix. **Query:** How should the size and kind backfill run? **Options:** a) (recommended, confidence medium - it follows the standard's migration rule, but the volume makes the confirmation load real) One read-only proposal run per territory, each producing a size and kind table for you to confirm. Then one write run per repository on your confirmation, fixing the dotfiles `initiative` fields in the same pass. b) Leave the backfill to each repository's next planning pass and accept the risk of fails at the backstop.

### VA-PLANNING - Close apps-vallearmonia.com planning gaps

since 2026-10-19 · from `wave1-sweep` at 23:49 BST · in blind review

**Context:** apps-vallearmonia.com still has 7 planning gaps, all body-shape fails (ITEM-3) across 5 records. VA-WEBSITE-CONT-005 and VA-WEBSITE-SANC-009 are Now drafts, and VA-WEBSITE-SANC-008 and VA-WEBSITE-SITE-004 are Next drafts. All four lack the Current state, Files touched, Dependencies / blocks and Documentation impact sections. VA-WEBSITE-SITE-003 is awaiting review without a complete review packet or a final Discussion. Shaping a record is `ki-plan` work in that repository and needs your authority there. **Query:** Should I launch a planning pass in apps-vallearmonia.com to close the 7 gaps? **Options:** a) (recommended, confidence medium - a bounded single-repository change, but every plan needs your approval to become Ready) Launch one `ki-plan` run in apps-vallearmonia.com that shapes the four drafts and completes VA-WEBSITE-SITE-003's review packet, leaving every record short of Ready until you approve it. b) Leave the gaps until those records are next selected.

### THEME-REGISTRY - Migrate territory theme registries

since 2026-10-19 · from `wave1-sweep` at 23:49 BST · in blind review

**Context:** No Capital in the six territories has `Streams/Themes/`. hnr-principal, legal-principal and personal-principal keep the legacy `Streams/Initiatives/` registry, which the audit warns on. er-principal, va-principal and tmx-principal have no registry at all, so every theme their records name goes unresolved. Several record themes appear in no registry, such as `harness-foundation`, `source-data`, `ki-conformance`, `housekeeping` and `dashboard`. **Query:** Should this Project raise theme-registry migration records in the territories' Capitals? **Options:** a) (recommended, confidence medium - the warnings are clear, but which themes each territory keeps is your call) Raise one record in each of hnr-principal, legal-principal and personal-principal to move Initiatives to `Streams/Themes/` pages. Leave er-principal, va-principal and tmx-principal without a registry until one of their records needs a theme. b) Raise a record in all six Capitals, giving each a theme registry now.

### CHECKER-GAPS - Report audit blind spots to the harness

since 2026-10-19 · from `wave1-sweep` at 23:49 BST · in blind review

**Context:** The Streams adapter applies neither ROAD-6 nor the area-declaration check, so slug-valued area titles in hnr-principal and tmx-principal pass unflagged, and so do va-principal's undeclared `GOV` and `KNW` areas. Separately, `ki repo audit --repo` refuses a symlinked repository path (`personal/dotfiles`). Changes to harness and tools belong to ki.ways-of-working and ki.tools-burndown, not to this Project. **Query:** Should these blind spots go to the harness and tools-ki as handoff items? **Options:** a) (recommended, confidence medium - the evidence is direct, but whether symlinks should be accepted is a design choice) Route the two Streams checker gaps to ki.ways-of-working, and the symlink refusal to ki.tools-burndown, each as one `messages.md` line. b) Note them in this Project only and take them up after the territory rollout.

## Parked

- **CHECKLIST** - from the old ki.baseline-rollout package, held since 15 October: whether to adopt the stock Repository review Activity across the estate. Recommended: adopt it estate-wide only once Kris approves it for the Capital first.
- **PIN-PAYLOAD** - from the old ki.baseline-rollout package, parked 10 October with the pin-receiver idea: `update-ki-pin.yml` filters on `client_payload.source_repository` but tools-ki `release.yml` sends `client_payload.repository`, so `tool-release-published` dispatches would be skipped; the Capital's `.github/ki-version` and `update-ki-pin.yml` stay inert until the tools-release bot App and secrets are on it. Recommended: align the two field names when the pin-receiver idea is revived.
