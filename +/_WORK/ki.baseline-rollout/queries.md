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

since 2026-10-19 · from `wave1-sweep` at 23:49 BST · blind-reviewed by `review-area-titles` at 23:52 BST, which agreed

**Context:** The area-to-theme map in `.ki.toml` is retired: an area title should now be a short capitalised noun phrase. Five repositories still use 19 theme slugs as area titles: 5g-emerge-apex, 5g-emerge-demos and 5g-emerge-testbed (all three failing the audit) and hnr-principal and tmx-principal (which the checker misses). None is a live theme. va-principal issues `GOV` and `KNW` records with no area map declared at all. legal-principal and 5g-emerge-phase2 already show the target form. Each fix is a `.ki.toml` edit in that repository and needs your authority there.

**Query:** Should this Project raise conformance records to retitle the areas, and to declare va-principal's map, in each affected repository?

**Options:**

a) (recommended, confidence high - reviewed: the blind review agreed that repository-owned records keep local delivery and acceptance while Capitals coordinate routing) Raise one conformance record per affected repository, routed through its Capital: the three 5g-emerge repositories and hnr-principal through hnr-principal, tmx-principal and va-principal each through themselves; each record proposes noun-phrase titles for you to confirm.

b) Raise one combined record in each Capital covering its territory's repositories, which would need explicit per-repository delivery and acceptance scopes.

### LEDGER-FORM - Repair superseded issue ledgers

since 2026-10-19 · from `wave1-sweep` at 23:49 BST · blind-reviewed by `review-ledger-form` at 23:52 BST, which agreed

**Context:** Seven roadmap ledgers use a superseded form, which the audit warns on: 5g-emerge-apex, 5g-emerge-demos, 5g-emerge-testbed, apps-kris.me.uk, apps-dafacts.org, er-agentic-harness and apps-markhowarth.com; the three 5g-emerge ledgers also fail for the wrong issuing mode. The review verified exact legacy matches and that a repair can keep every area code and allocation. `ki repo conform --skill ki-work-roadmap` is the designed repair, but conform stays barred without `--dry-run` while the Husky-to-`.githooks` migration lands tonight.

**Query:** How should the superseded ledgers be repaired?

**Options:**

a) (recommended, confidence high - reviewed: the blind review verified the legacy matches and an allocation-preserving repair) Fold the three 5g-emerge ledger repairs into their AREA-TITLES records; repair the other four with a `--dry-run`-checked conform once ki.tools-burndown clears conform after tonight's release, one repository at a time on your go.

b) Hand-edit all seven ledger bodies now under conformance records, keeping every allocation, without waiting for conform.

### SIZE-KIND - Backfill size and kind on open records

since 2026-10-19 · from `wave1-sweep` at 23:49 BST · blind-reviewed by `review-size-kind` at 23:52 BST, which agreed

**Context:** 191 open records in 18 repositories have no `size`, and 61 adopted open records have no `kind`; the largest gaps are personal-principal (33), legal-principal (28), er-agentic-harness (22, all also without kind), hnr-principal (20), dotfiles (16) and apps-vallearmonia.com (15); dotfiles also has 4 records still naming `initiative`. The field migration window opened on 2026-10-19 and closes on a complete clean scan or a 60-day backstop, after which these warnings become failures. The standard says size and kind need judgement: a run proposes, you confirm, one repository at a time.

**Query:** How should the size and kind backfill run?

**Options:**

a) (recommended, confidence high - reviewed: the blind review agreed, from direct counts and the migration rule) Run one read-only proposal pass per territory, giving a table per repository of each record's proposed size and kind with a short reason or open uncertainty; you confirm per repository, then one approved write pass runs per repository.

b) Leave the backfill to each repository's next planning pass, accepting that untouched records become failures when the window closes.

### VA-PLANNING - Close apps-vallearmonia.com planning gaps

since 2026-10-19 · from `wave1-sweep` at 23:49 BST · blind-reviewed by `review-va-planning` at 23:55 BST, which disagreed; the worker now takes the review's course

**Context:** apps-vallearmonia.com still has 7 planning gaps across 5 records. Four drafts, [VA-WEBSITE-CONT-005](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-CONT-005-resolve-image-review-flags.md) and [VA-WEBSITE-SANC-009](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-009-close-the-editorial-audit.md) (Now) and [VA-WEBSITE-SANC-008](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-008-package-the-sanctuary.md) and [VA-WEBSITE-SITE-004](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SITE-004-choose-the-home-page-layout.md) (Next), lack their planning sections; [VA-WEBSITE-SITE-003](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SITE-003-consolidate-the-design-system.md) is awaiting review without a complete review packet or final Discussion. The worker first proposed one `ki-plan` run for all five; the review found `ki-plan` accepts only drafts and excludes review-packet assembly, and that SITE-003's verification claims need real evidence, so the worker now recommends splitting the repair by lifecycle state.

**Query:** Should the repair run as `ki-plan` on the four drafts plus a separate evidence-backed repair of SITE-003?

**Options:**

a) (recommended, confidence high - reviewed: the review verified the defects and `ki-plan`'s boundary directly; the worker's single-run plan crossed that boundary) Authorise `ki-plan` for the four drafts, keeping them draft until you approve each plan, and separately an evidence-backed repair of SITE-003 that keeps it awaiting review and reports any evidence it cannot recover.

b) One `ki-plan` run covering all five, the worker's original proposal, which needs an explicit override of `ki-plan`'s scope.

c) Leave the gaps until those records are next selected.

### THEME-REGISTRY - Give territory Capitals a theme registry

since 2026-10-19 · from `wave1-sweep` at 23:49 BST · blind-reviewed by `review-theme-registry` at 23:54 BST, which disagreed; the worker now takes the review's course

**Context:** No Capital in the six territories has `Streams/Themes/`. hnr-principal, legal-principal and personal-principal keep the legacy `Streams/Initiatives/` registry, which the audit warns on; er-principal, va-principal and tmx-principal have none, so their records' themes go unresolved, and labels such as `harness-foundation`, `source-data`, `ki-conformance`, `housekeeping` and `dashboard` appear in no registry. The worker first proposed records for the three legacy Capitals only, deferring the other three until a record needed a theme; the review verified that open records in all three already name themes, so that condition is already met. Raising records asks each Capital for work it owns; it approves no delivery.

**Query:** Should this Project raise theme-registry migration records in all six Capitals?

**Options:**

a) (recommended, confidence high - reviewed: the review verified theme references in all six Capitals, which defeats the worker's reason for deferring three) Raise one record in each of hnr-principal, legal-principal, personal-principal, er-principal, va-principal and tmx-principal: inventory the territory's actual theme references, migrate legacy Initiatives pages where they exist, and have the Capital reconcile unresolved labels rather than create a page for every string.

b) Raise records only in hnr-principal, legal-principal and personal-principal, the worker's original proposal, deferring the other three.

### CHECKER-GAPS - Report audit blind spots to the harness and tools-ki

since 2026-10-19 · from `wave1-sweep` at 23:49 BST · blind-reviewed by `review-checker-gaps` at 23:55 BST, which agreed

**Context:** The Streams roadmap adapter applies neither the area-title check (ROAD-6) nor the area-declaration check, so slug-valued area titles in hnr-principal and tmx-principal, and va-principal's undeclared `GOV` and `KNW` areas, pass unflagged. Separately, `ki repo audit --repo` refuses a symlinked repository path (`personal/dotfiles`). Harness checks belong to ki.ways-of-working and `ki` changes to ki.tools-burndown, not this Project.

**Query:** Should the blind spots go to the harness and tools-ki as handoff items?

**Options:**

a) (recommended, confidence high - reviewed: the blind review agreed on the direct evidence and the owners) Route the two Streams checker gaps to ki.ways-of-working and the symlink refusal to ki.tools-burndown, one `messages.md` line each.

b) Note them in this Project only and take them up after the territory rollout.

## Parked

None.
