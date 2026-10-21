# ki.ways-of-working queries

## Open

### GRANT-INTERIM - Release `--allow` so the interim grant sentence can go

**Context:** Kris answered GRANT-INTERIM a) earlier: the interim sentence in `ki-delegation`'s Grants subsection ([background-run standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md), "until the launcher offers that option") is removed once a `ki` release carrying `--allow` is installed. The `ki` on `sol` runs the tools-ki source checkout directly, so it already offers `--allow`. No tagged release contains it, though: the latest is `v0.12.0`. A release is publication, so it is Kris's to authorise. It also follows FOOTER-PROVISIONALS and the acceptance of [KI-TOOL-KI-CLI-134 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/f4811dd9310b48d8809d9143ca8864fc7b4be5e2/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md). ki.tools-burndown already plans a patch release with KI-TOOL-KI-CLI-155 and the harness pin.

**Query:** Will Kris authorise a tools-ki release carrying `--allow` once KI-TOOL-KI-CLI-134 is accepted, so that the interim sentence can go?

**Options:**

a) (recommended, confidence high - reviewed: the standard makes removal conditional on launcher support, and the agreed installed-release boundary is met by the planned release after acceptance; its complete release range still needs verification) Yes: fold it into ki.tools-burndown's planned patch release; once it is installed, a run removes the sentence.

b) Remove the sentence now, since `sol`'s `ki` already offers `--allow`, and release later.

c) Hold the release; the sentence stays.

### OBS-ACT-VISUAL - Kris's own check of KI-OBSERVA-BRG-005

**Context:** [KI-OBSERVA-BRG-005](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-005-act-board-missing-parts.md) (the Act board's missing parts) is awaiting review. Its review packet reserves a live check for Kris at <http://127.0.0.1:1675/>: the repository-fetch and Rig-apply plan rows, meaning their scope, inputs and withheld-checkout rows, at 1,440 and 760 px. The overnight grant excludes acceptance wherever Kris's own eyes are needed. accept2-observatory accepted KI-OBSERVA-OPS-003 and KI-OBSERVA-VIS-027 alongside it.

**Query:** When does Kris make the live check of KI-OBSERVA-BRG-005?

**Options:**

a) (recommended, confidence high - the packet reserves the check for Kris) Kris checks this morning and reports the result to ki.observatory; the record stays awaiting review until then.

b) Return it to in progress if the check finds a defect.

### SITE-SOURCE - KI-WEBSITE-SITE-044's ki-design citation and visual checks

**Context:** [KI-WEBSITE-SITE-044](/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/docs/roadmap/KI-WEBSITE-SITE-044-design-v1.md) (adopt ki-design v1) passes every local gate (build, routes, provenance offline, 72 tests, audits) and is awaiting review. The Field Guide cites the `ki-design` repository as its symbol source. That repository is private, so readers cannot open the citation, and the [page-provenance guide](/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/docs/guides/developer/page-provenance.md) forbids inaccessible published citations. The visual checks of the home page, an inner page and the Field Guide at 1440 and 390 px, in both colour schemes, were not repeated after the last update. The two runs disagree. burn-website recommended accepting the citation as it stands and making ki-design public later (medium confidence). accept-website recommended keeping the record awaiting review until reader access is resolved (high confidence). The website has three unpushed commits from other sessions. A conflicting source, [KI-DESIGN-ART-002](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ART-002-art-licensing.md), says ki-design went public on 18 October. This local-only review cannot resolve anonymous access to the exact cited revision.

**Query:** Which remedy should KI-WEBSITE-SITE-044's ki-design citation take before acceptance?

**Options:**

a) (recommended, confidence medium - keeps the provenance guide whole, but whether ki-design goes public is Kris's publication call; blind review disagrees and prefers d), because access is disputed and a publication promise does not make the citation readable) The record stays awaiting review. Kris makes ki-design readable, or confirms it is to be, then makes the 1440 and 390 px checks in both schemes, and an acceptance review follows.

b) Return it to in progress for a site-local remedy that keeps attribution accurate without the private link, then a fresh review packet and Kris's visual checks.

c) Accept the citation as it stands and make ki-design public later; it breaks the provenance guide until then.

d) Blind review: first verify anonymous access to the exact cited source revision. If accessible, retain the accurate citation; otherwise return the record to in progress for an accessible site-local source that preserves attribution and immutable provenance. Complete the required visual checks and independent acceptance review afterwards. Reason: the records conflict about public access, and neither a future publication promise nor making the whole repository public is needed to establish a readable citation.

### OPS-014-RENDER - Kris's four client render checks for the GFM conversion

**Context:** [KI-PRINCIPAL-OPS-014](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md) converted ki-principal to GitHub-flavoured Markdown and is awaiting review. Kris answered RENDER-CHECK a) at 05:20 ("Vendor check fine"), and gfm-answers applied the other three answers. Acceptance test 4 is still unticked and reserved for Kris. In each of GitHub, Obsidian, Zed and the Observatory, open the Library heading link and a representative alert. Check that the four plain images read well at natural size. Record each outcome in the record and decide each failure. The Observatory drops the heading fragment; that is to be recorded either as a navigation failure or as an accepted fallback.

**Query:** When does Kris run the four client render checks, and is the Observatory's dropped fragment a failure or an accepted fallback?

**Options:**

a) (recommended, confidence high - the packet reserves acceptance test 4 for Kris) Kris runs the four checks this morning, records the outcomes, accepts the Observatory's dropped fragment as a fallback, and the record then goes to acceptance.

b) Kris runs the checks and records the dropped fragment as a navigation failure, routed to ki.observatory before acceptance.

### RIG-ATTENDED - Kris's attended Rig checks on sol and terra

**Context:** Four tools-rig records cannot move without Kris at the Macs:

- [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md) (draft, Now). Its step 1 is Kris's native handler probe at `sol`'s screen: three rungs (`legacy`, `modern`, `workspace`) run in order, stopping at the first that makes Zed the TOML handler. It is a live change, and delivery is blocked on it.
- [KI-TOOL-RIG-CORE-068](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md) (draft, Now; approved under TERRA-NORDVPN a) on 19 October). Its gate is the attended NordVPN check at `terra`'s console. The check writes pf and is connection-critical. The record carries a tested restore path, R, which is rehearsed at step 4 before NordVPN connects, and the trial stops if R fails.
- [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) and [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md) (in progress). Both failed acceptance overnight. SHELL-HOOK fails because Bats runs in pre-commit, and that fix is with ki.tools-burndown as RIG-PRECOMMIT-BATS. They also need Kris's live apply on `terra` and then `sol`, the SSH-over-tailnet check, and the missing `terra` evidence, under [ADR-KI-TOOL-RIG-009](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/decisions/ADR-KI-TOOL-RIG-009-system-domain-resources-under-an-attended-grant.md)'s attended grant.

**Query:** When and in what order does Kris run the attended Rig checks?

**Options:**

a) (recommended, confidence high - follows each record's own gate and keeps the connection-critical step at a console with its rehearsed restore) Hold one attended session. Run KI-TOOL-RIG-CORE-069's probe on `sol` first. Next comes KI-TOOL-RIG-CORE-068's NordVPN check at `terra`'s console, with R rehearsed before it. Leave the live apply of KI-TOOL-RIG-CORE-047 and -062 until RIG-PRECOMMIT-BATS lands and both pass re-review.

b) Take them one at a time, whenever Kris is at each Mac.

c) Defer all four; they stay as they are.

### TECHNE-006-REVIEW - Review the replanned guarded host commands

**Context:** [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md) (draft, Next, null baseline) is the last open tools-techne record. Its 20 October replan replaces the teardown command with destructive rebuild and withdraw commands, guarded removal operations, a stop warning and `--now`, and status schemas and exits. The record says the plan stays draft until Kris reviews it. Delivery would be local and stubbed. The `destroy` parameter from KI-TOOL-TECHNE-CLI-009, accepted overnight, takes effect only when CLI-006 lands.

**Query:** Will Kris review CLI-006's Steps, Files touched and Verify so that a later run can deliver it?

**Options:**

a) (recommended, confidence high - only Kris's review unblocks it, and delivery is local and stubbed) Kris reviews the plan and releases it to Ready.

b) Leave it in Next until the agent-host work needs rebuild and withdraw.

### DESIGN-ICONS - Kris's look at the KI-DESIGN-ICO-001 contact sheet

**Context:** [KI-DESIGN-ICO-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ICO-001-icon-seed-set.md) (icon seed set) is awaiting review. Its Verify ends "owner reviews drawings on contact sheet". There are five new glyphs, `realm`, `pillars`, `thriving`, `quiet` and `weathered`, bordered in brass on `/Users/krisbrown/workspaces/knowledge-islands/ki-design/packages/icons/contact-sheet.png`. The record's tests and lint pass.

**Query:** Do the five new glyphs on the contact sheet pass Kris's look?

**Options:**

a) (recommended, confidence high - the record's Verify reserves this look for Kris) Kris looks at the contact sheet; on a pass, an independent acceptance review accepts the record.

b) Kris names the glyphs to redraw, and the record goes back to in progress.

### GOV209-OWNER - Which skill owns the acquired-area scaffold

**Context:** [KI-HARNESS-GOV-209](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-209-acquired-inbound-area.md) (draft, Next, not yet planned) gives each territory principal a `+/_ACQUIRED/` folder with a scaffold README, where the acquire port delivers whole packets, and adds receiver triage guidance to `ki-repo-kb`: file the packet, turn it into work, or park it. The record does not say which skill owns the scaffold. The repository rule is that a capability which owns a working-area subarea must require its exact README while that capability is declared, and restores the README through its own conform. If `ki-repo-kb` owned it, every knowledge base would carry the folder, not only the principals. `ki-repo-kb-principal` writes no scaffold today. Eight principals declare the `ki-repo-kb-principal` overlay and none of them has the folder yet, so under either owner all eight would fail audit until each is conformed. Acquire's dispatch guide already creates the folder on first delivery, so the scaffold is not a precondition for dispatch. Kris dropped the return route on 20 October, so the receiver writes nothing back to the port.

**Query:** Which skill should own the `+/_ACQUIRED/` scaffold, and should it be required in every principal or checked only once the folder exists?

**Options:**

a) (recommended, confidence medium - reviewed: principal-only delivery matches the overlay, and the repository rule requires declared specialist areas to retain an exact scaffold restored by their owner) Give the scaffold to `ki-repo-kb-principal`, require it while the overlay is declared and add conform support; put the receiver triage guidance in `ki-repo-kb`.

b) Check the scaffold only once `+/_ACQUIRED/` exists, which means amending the `ki-repo` rule on specialist subareas.

c) Give the scaffold to `ki-repo-kb` for every knowledge base.

### GOV189-SCOPE - Narrow the thread-move record to its decided slice

**Context:** [KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md) (draft, Next, Mac Studio Setup) adds to `ki-coordination` a procedure for moving coordinating work from one Mac to another, plus a level check at resume and at every mark with a `[behind]` banner item. Kris decided the level check and `[behind]` under SYNC-GUARD on 18 October, so that part could be delivered now. Two questions remain open. The first is how agents that must run on one host are handled: kept queued on the old host, carried with a host constraint, or treated as blocking the move. The second is which closing form the session left on the old host uses, since Kris's 14 October decision named the retired DONE frame and the work model keeps `Finished` for work that has ended. Exporting and re-importing the agent queue belongs to tools-ki, and until a command exists the standard can name the manual route of re-queuing briefs from the work package's Next steps. The record does not block the Mac Studio setup.

**Query:** Should KI-HARNESS-GOV-189 be narrowed to the decided level check and `[behind]` item, or wait until Kris answers both open questions?

**Options:**

a) (recommended, confidence medium - reviewed: SYNC-GUARD already settles the level check and banner item; host-bound queue handling and the old session's closing form remain explicit open questions) Narrow it to the level check and the `[behind]` item, and keep the two open questions in its Discussion for a later record.

b) Kris answers both questions now, so that the whole record can be planned.

### GOV202-ADOPT - Adopt the skill-area stats badge

**Context:** [KI-HARNESS-GOV-202](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-202-skill-area-stable-stats-badge.md) is still in triage with no horizon, priority or size. It replaces the uninformative SRC badge on the ten skill-area diagrams with stable stats about each skill, such as its rubric rule count, a code-size bucket and its reference count, which Kris asked for on 14 October under SRC-BADGE. It is small. Planning still has to decide whether the badge comes from the harness generator or needs a change to the vendored viewer, and which stats are stable enough not to churn the diagrams. Nobody has judged its value against other work.

**Query:** Should KI-HARNESS-GOV-202 be adopted?

**Options:**

a) (recommended, confidence low - it is small, but its value has not been judged; blind review disagrees and prefers c), because adoption should follow a value comparison and a feasible implementation route) Adopt it to Next for a later burndown.

b) Cancel it.

c) Blind review: retain it in triage until a short comparison establishes its value against other work and a feasible route within the record's boundary. Reason: capture approved the idea without adopting it, no size or effort estimate supports the smallness claim, and the generator-versus-viewer question is unresolved.

### GOV227-SCHEMA - Design the repository storage schema

**Context:** [KI-HARNESS-GOV-227](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-227-repository-storage-declarations.md) (draft, Next, Observatory) adds a `ki-repo`-owned `.ki.toml` table in which a repository declares what each tool, MCP server or app it ships stores in its XDG config, data, cache and state folders, and why. Kris decided the owner under STORAGE-OWNER a) on 20 October. Its first step is to design the schema with Kris: entries per item, each XDG category with its purpose and whether the content is disposable, recoverable or the owner's knowledge, and a way to declare shared namespaces with their owners. The record cannot be planned until the schema exists. It blocks only the tool-storage phase of the Observatory's machine instrument.

**Query:** When should Kris design the storage-declaration schema for KI-HARNESS-GOV-227?

**Options:**

a) (recommended, confidence high - reviewed: the schema still needs explicit recoverability and shared-namespace ownership, the record requires owner co-design, and one Observatory phase depends on it) Hold a short design session in its own work.

b) Defer the record to Future.

### TAGS - [KI-PRINCIPAL-MOD-008] keep subject tags beside note_type?

**Context:** Kris asked on 2026-10-12 whether subject tags are still needed. The `card/*` and `calendar/*` tags repeat what `note_type` already says, while the `topic/*` tags still help search across folders.

Independent scope check: retiring redundant kind tags is a model direction. Any later migration must check tag-dependent consumers and map existing kinds without losing information.

**Query:** Which tag families should the model keep?

**Options:**

a) (recommended, confidence low - retiring tags touches many notes and tools) **reviewed** (independent confidence high): Keep `topic/*`, `date/*` and `source/*`, and retire the `card/*` and `calendar/*` type tags in favour of `note_type`.

b) Keep the full taxonomy unchanged.

c) Retire all tags in favour of `note_type`, folders and links.

### EMERGING - [KI-PRINCIPAL-MOD-008] what to do with the Emerging Concepts

**Context:** Four notes sit in Emerging Concepts: Realm Model, Avatar Roles and Oversight, Known World and Fictional Lineage. [ADR-KI-PRINCIPAL-005](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-005-one-persona-across-explicit-working-contexts.md>) settles one persona with one name across working contexts. The Techne Programme Focus says that knowledge consolidation alone does not accept candidates.

Independent scope check: Fictional Lineage can record attributed influences as Background while keeping speculative horizons explicitly speculative. This does not adopt Realm authority, Avatar powers, a registry or a deployment. The other three notes remain unadopted. [ADR-KI-PRINCIPAL-005](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-005-one-persona-across-explicit-working-contexts.md>) explicitly fixes one enduring persona and context-bound authority; it does not expressly forbid every display alias. Agreement keeps the present persona and name, and does not settle the broader alias question by inference.

**Query:** Which Emerging Concepts should move to the settled Philosophy?

**Options:**

a) (recommended, confidence medium - this respects the Focus and ADR-005) **reviewed** (independent confidence medium): Leave Realm Model, Avatar Roles and Oversight and Known World open, and keep one Avatar name under [ADR-KI-PRINCIPAL-005](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-005-one-persona-across-explicit-working-contexts.md>). Adopt Fictional Lineage into Background beside Influences Along the Way.

b) Leave all four open.

### CANDIDATE-PRINCIPLES - [KI-PRINCIPAL-MOD-008] adopt the two candidate engineering principles?

**Context:** Engineering Practice Principles holds two candidates: a neutrality extension to Provider-Neutral Execution, and FOSS-First and Inspectable. Both are consistent with the existing principles. The Techne Programme Focus says that consolidation alone does not accept candidates.

Independent scope check: the Focus prevents consolidation from silently accepting candidates. This query can supply the explicit owner decision. These qualified principles need no new product, service, provider change or implementation mandate.

**Query:** Should the two candidate principles be adopted?

**Options:**

a) (recommended, confidence medium-high - They fit the adopted replaceability and explicit-trade-off principles; the Focus requires an owner decision, not permanent deferral of principle decisions.) **Blind review:** Adopt both now. Adopt both as qualified engineering decision criteria: extend neutrality without lowest-common-denominator limits, and prefer FOSS/open standards where practical. This grants no implementation or product expansion.

b) **Delivery run:** (recommended, confidence medium - this follows the Focus as written) Leave both as candidates until the owner takes them up.

### STRUCTURE-TODOS - [KI-PRINCIPAL-MOD-008] settle the Port and Routes and Customs to-dos

**Context:** Structure's Port to-do is now largely settled by [GDR-KI-PRINCIPAL-010](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-010-the-port.md>) and the `+`/`-` rules. Routes and Customs is still open, though Territories and Archipelagos has a route paragraph and `ki-trades` governs exchange.

**Query:** Should the Port to-do become a settled section?

**Options:**

a) (recommended, confidence medium - the decision already exists) **reviewed** (independent confidence high): Make Port a settled section that cites [GDR-KI-PRINCIPAL-010](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-010-the-port.md>). Keep the Routes and Customs to-do, with pointers to the route paragraph and to `ki-trades`.

b) Leave both to-dos as they are.

### CONTROL-CONTRACT - Remaining agent controls

**Context**

TAKE-STOCK names stop, dequeue and bounded OOS-WAKE, but its cited design supplies capability names rather than their complete observable contract. The current process port has launch, liveness and sleep; it does not establish a safe stop operation or a coordinator continuation binding. The existing queue does not define what dequeue acknowledges against a dispatcher that has already claimed an entry. Choosing signal versus cooperative stop, cancellation acknowledgement, native continuation identity, expiry and wake deduplication would add policy beyond this unit's settled-contract limit. Repository/run resolution, queue and send are verified already present; no watcher was started.

**Query**

Which settled contract should govern those remaining controls before another implementation run?

**Options**

a) (recommended, confidence high - an exact contract makes the bounded implementation reviewable) Have the coordinator supply the accepted stop/dequeue/wake contract, including process ownership and continuation binding, then redispatch only that machinery.

b) Defer the remaining controls and retain the verified repository-resolution, queue and send portion.

From wow-night-tools-ki-queue-d, 2026-10-21 03:41 BST.

### OPS009-PREFLIGHT - Four capture requests

**Context**

The required ki-next roadmap preflight returns ITEM-2 WARN because territory humans-not-robots is not available in the local registry. Registering Knowledge Islands Principal in this run's copied audit home removed the Capital-availability warning but did not resolve this foreign territory. The capture procedure stops on any roadmap warning. All four approved slices were checked against the existing queue and issuing ledger and stopped before allocation; the CLI high-water mark remains 167. No capture, adoption, implementation or provider action occurred. [Exact preflight evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-night-tools-ki-queue-d.capture-roadmap-audit.log).

**Query**

How should the missing foreign-territory prerequisite be supplied so the four already-approved capture-only requests can proceed?

**Options**

a) (recommended, confidence high - resolves the explicit preflight requirement without bypassing a gate) Supply the readable registered Capital evidence in an isolated audit home, then redispatch the four distinct capture-only slices with their exact manifest and recoverable-copy gates.

b) Keep all four requests queued until that territory registry is available.

From wow-night-tools-ki-queue-d, 2026-10-21 03:41 BST.

### RELEASE-PREP - Version and Harness pin for the next tools-ki release

**Context:** wow-night-tools-ki-release-candidate-d ([report](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-night-tools-ki-release-candidate-d.report.md)) found no releasable candidate: tools-ki main `566679b2` still declares `0.12.0`, which is already tagged; the range since `v0.12.0` holds 60 commits, some of them breaking; and tools-ki pins Harness `f4d6c521`, while newer Harness work is local and unpushed behind other sessions' commits. A candidate needs a version bump, a pushed Harness revision to pin, migration notes and fresh exact-head CI. KI-TOOL-KI-CLI-140 delivery runs next in the same lane and would join this release.

**Query:** Which version should the next tools-ki release take, and may a preparation run bump it and advance the Harness pin once the Harness commits are pushed?

**Options:**

a) (recommended, confidence high - breaking changes in range call for a minor bump before 1.0, and a pin must name a pushed revision) `v0.13.0`: after you push ki-agentic-harness, a preparation run bumps the version, pins the pushed Harness revision, writes migration notes, runs the full gates and exact-head CI, and returns a dossier with the tag commands for you.

b) Hold the release until CLI-140 and other planned work land, then prepare once.

## Parked

- NO-GATE (with PKGLESS-GATE) - project shape commit gate; Kris will come back to it. a) `ki repo audit --skill ki-repo` staged, check-only; review prefers widening KI-HARNESS-GOV-225.
