# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › away-consumer-gap

**🤖 → 👤 Handoff to supervisor · Run report at 01:13 GMT · last mark 01:04 GMT**

---

## Done

- Completed the read-only consumer assessment under TYPED-ID-CONSUMER, COORD-REGULAR-STATUS and [AWAY-2026-10-29](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.observatory/decisions.md); no repository edits or commits were made.
- Isolated source checks passed: five reproduction groups covering status precedence, canonical-home continuity, report lookup, placement loss and legacy grouping limits.
- Existing focused tests passed: 75 tests across seven contract/evidence files, zero failures, 330 assertions; full product gate and browser/service checks were not run.
- Exact source-anchor predicates and seven source-file SHA-256 checks passed; both relevant queue instructions were verified against their actual complete source lines.
- Read the complete runtime inbox before focused verification and final synthesis; its staging/bookkeeping requests concern the package owner and did not expand this read-only unit.
- No network, provider, scheduler, service, environment or credential operations; no formatter, new work record, additional agent, repository staging or service restart.

## In Progress

Nothing is running in this unit.

Outstanding - no action requested now: the supervising Observatory owner retains follow-up planning and any separate delivery brief. This assessment neither adopts a record nor resolves the existing redesign choices. Capital staging contention did not block the assessment, and no staging window was claimed.

## Findings

### STATUS-AUTHORITY - Current screens bypass or override the canonical reader

**Goal:** Assess Observatory's current work-status consumer, requested by Kris through this bounded brief on 29 October 2026.

**Scope:** Actual local tools-ki status/identity source, Observatory contracts, fast and full work evidence paths, and current Work/Waiting callers; isolated fixtures only, with process and membership ports injected.

**As of:** 29 October 2026, 01:13 GMT, Europe/London; source evidence, not a claim about the currently served binary or another machine.

The primary reproduced gap is reader precedence. [Fast observation](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/work.ts) skips the CLI entirely; [fallback composition](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/work.ts) also supplements full observations with the old package parser whenever a folder is absent from CLI output. That absence can mean a deliberate canonical refusal, not missing CLI capability. The [local fallback parser](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/work-package.ts) validates the level vocabulary but does not apply the CLI's typed-kind, placement or ambiguity rules.

Direct reproduction imported both implementations. Each fixture lived only in this run's scratch directory:

- A member repository with a valid single-file regular package and a valid typed Project package produced two canonical entries. Fast observation produced only the Project entry: the regular work disappeared. This is a supported single-file/member case, not a claim that all current regular packages disappear.
- A live run homed using the Project's historical spelling attached to its typed package through the canonical reader. Fast observation lost that run because its local home matcher requires exact folder equality. The isolated run was injected rather than launched.
- A typed regular ID paired with Project level was refused by [canonical validation](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/work/status.ts). Full Observatory observation reintroduced it through fallback. Thus even the full reader can turn a canonical omission back into visible work.
- Two historical/typed spellings of the same Project home caused [canonical ambiguity rejection](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/work/status.ts). Fast observation displayed both packages, bypassing the one-home refusal.

Current Work's board requests the fast endpoint in [board.ts](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/instruments/src/board.ts); Waiting does likewise in [waiting.ts](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/instruments/src/waiting.ts). The server's full Review path also injects fast work observation. These are current call paths; the obsolete comment that installed ki cannot read packages is not itself the defect. Current tools-ki does read both package shapes.

Smallest proposed repair: have both fast and full work observations consume the same canonical status result and stop resurrecting refused entries. Keep caching and parallel observation within existing evidence/server boundaries; preserve the current areas, URLs and five derived views. The existing estate-latency concern is real context, so benchmark a scoped cold/warm read before selecting the cache policy. Do not silently restore a permissive scanner on CLI failure: expose an unavailable source and keep other instruments usable.

Applicable authority: the two instructions in the [Observatory queue](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.observatory/messages.md) permit assessment and receiver-owned prioritisation, not implementation in this run. They can carry an immediate bounded maintenance need without manufacturing a new record. [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) owns redesign decisions, remains Draft/Now, and is not a Ready baseline for this repair. The supervisor must supply an explicit bounded planning/delivery envelope before edits; no automatic promotion follows from this report.

Queries raised: none requiring Kris's answer to complete this assessment.

### REPORT-HOME - Historical report requests do not resolve the current canonical home

**Goal:** Check typed-ID compatibility while retaining report lookup and grouping, as TYPED-ID-CONSUMER requests.

**Scope:** Current status-to-summary grouping, direct report-document lookup and the existing tools identity helper; no historical report rewrites or package migrations.

**As of:** 29 October 2026, 01:13 GMT.

Existing coverage is substantial: typed IDs pass the work-name guard and status parser, all three levels and seven states are supported, repository identity is retained, and [latest-report grouping](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/work.ts) uses the authoritative entry path rather than slicing a Project slug out of the typed ID. The current typed package's report opened successfully in the source reproduction.

The narrower reproduced gap is historical addressing. The fixture held only the canonical typed Project home and its report. tools-ki's [identity helper](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/work/identity.ts) recognised its historical spelling. The canonical report request succeeded, while the historical spelling was refused as an absent report. [readWorkDocument](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/work.ts) constructs the requested work folder directly without canonical identity resolution. This affects a retained old-ID report URL even though canonical report grouping works.

A second verified limitation is placement metadata loss: [parseWorkStatus](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/contracts/src/work.ts) reconstructs a narrower entry and drops the canonical parent; the fixture's valid parent was present before parsing and absent afterwards. The same return shape does not carry label or covers. This demonstrates information loss, not a proved defect in every current screen: no claim is made that the board promises a parent-grouped UI today.

Smallest proposed follow-up: preserve the needed additive identity/placement fields with explicit compatibility handling for older v1 producers, and resolve historical report IDs through a governed tools-owned lookup before filesystem containment checks. Retain repository identity plus canonical work ID as the grouping key; preserve unchanged Project slugs and work-record IDs. Never search another repository by basename or invent a local alias registry. The current work-status JSON does not expose alias spellings, so the historical report fix needs a verified public machine lookup contract or a bounded Tools-owner dependency; the internal helper alone is not an authorised cross-repository import. Keep the existing realpath, readable-name, scope and redaction guards after resolution, and refuse ambiguous homes.

Applicable authority and record: TYPED-ID-CONSUMER in the [Observatory queue](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.observatory/messages.md) is the existing receiver-owned need. [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) remains the design boundary, not implementation authority. No new alias field, record or producer change was made here.

Queries raised: none now; the supervisor can route a precise producer-contract need if planning confirms no public lookup seam.

### COVERAGE-BOUNDARY - Regular status works without implying a coordinating session

**Goal:** Compare regular/member status, canonical grouping and explicit coordination independently of package type.

**Scope:** Canonical status schema, current work parser/views, the model's current coordination/home rules, and the legacy Sessions helper and caller.

**As of:** 29 October 2026, 01:13 GMT.

The canonical source preserves regular supervision and main/secondary placement, accepts deliberate member-local real packages, attaches historical-home runs once, and rejects ambiguous old/new homes. Existing tools tests cover regular parents, typed continuity and duplicate homes in [status.test.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/work/status.test.ts). The Observatory full canonical path accepts regular entries and derives views by holder/state, without a Project-level filter. Those are covered behaviours, not missing features to reimplement.

The current [Work Process](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md) explicitly separates coordination from package type and state. Current status JSON has no active-coordinator-role field. No new coordination inference should be added from a typed segment, a worker state, a nonempty backlog or a capability declaration. Retain regular as the level during an explicitly opened coordinating episode. Absence of an active-role projection is not, by itself, a proved product defect or a grant to add a new source of state.

Legacy Sessions remains a separate limitation. [Its current reader](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/sessions.ts) reads checkpoints, and [its run association](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/sessions.ts) matches a runtime-directory name to a checkpoint suffix rather than using the full binding home. The [Project-slug helper](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/contracts/src/sessions.ts) returned the same slug for synthetic Project, regular and secondary-State-of-play IDs. This last check is helper-level evidence only: it does not prove that current typed packages are being misgrouped in Sessions, because that caller still reads legacy checkpoints. Do not turn it into a fresh typed-package production defect.

Relevant existing holdings are [KI-OBSERVA-VIS-045](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-045-workers-instrument.md), held pending [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) and Kris's individual consolidation approval, plus [KI-OBSERVA-VIS-028 (idea)](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/ideas/KI-OBSERVA-VIS-028-retire-sessions-readers.md), which remains an idea outside the roadmap. Do not release either, retire readers, rename Streams/Workers or create a duplicate scanner under the status repair. General Capital-to-member automatic home-reference discovery is also explicitly deferred in the [Tools enactment receipt](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/decisions.md); member-local status support is not proof that this broader discovery contract exists.

Queries raised: none; all adoption and consolidation choices remain with their existing owners.

### FOLLOW-UP-BOUND - One small status repair first, report alias lookup separately

**Goal:** Identify the smallest safe fixes and their required verification under current authority.

**Scope:** Proposed work only; no record creation, implementation, promotion or dispatch.

**As of:** 29 October 2026, 01:13 GMT.

Recommended first envelope: reconcile fast/full status authority only. Owned product paths would be work evidence/contracts and their existing tests, plus the existing server loader/cache tests only where needed. Reuse the current board and Waiting UI. Do not include Sessions consolidation, scheduler ownership, new home locators, design renames or active-coordinator inference. Carry report lookup as a second dependent envelope after verifying the public canonical resolver seam.

Required regression coverage for the first envelope: valid typed and historical package spellings individually; duplicate-home refusal; kind/level and invalid-placement refusal not resurrected by fallback; identical regular/member coverage in fast/full observations; canonical run attachment for historical homes; unchanged holder/state views for all seven states; parent/covers round-trip if retained; path redaction; unavailable CLI and missing provider behaviour; no mutation or network from browser code. Exercise Work, Waiting and Review endpoint wiring so a port-only test cannot miss a remaining fast bypass. Check cold/warm latency and existing cache freshness rather than restoring another state reader.

Required report-lookup coverage: old and canonical requests resolve to one current entry and summary, preserve repository/Project/record identities, reject ambiguous and out-of-scope homes, and retain traversal, symlink, unreadable-file and redaction refusals. Include regular and secondary IDs that share a Project's final segment so grouping never infers Project identity from that suffix alone.

Assessment verification already performed: existing work and sessions contract tests, ki evidence tests, work and work-package evidence tests, Focus tests and Sessions evidence tests passed. Before any later delivery, run the repository's required `bun run test` gate, including `apps/site/src/degraded.test.ts`, plus the relevant typecheck and declared boundary/contrast/density/width checks if those paths change. No broad gate was claimed in this read-only unit.

Coordinator method digest: explicit coordination requires an owner opener on any valid package; Capital is the default single home and member exceptions remain deliberate; parent/covers are discovery rather than authority; seven states and one state owner persist; typed IDs do not rename repository, Project or work-record identities; historical references remain readable. Before dispatch read the current Work Process sections “Levels and forms of work” and “Homes” (including its “The work package and its folder” and “One real home” paragraphs), the coordination standard's “Reply forms” and “Owner report”, the exact two consumer queue lines and the current away decision. The current method revision recorded by this Project is afb126f2. No REFRESH or package metadata action belongs to this assessment.

Queries raised: none. A separate bounded brief is the implementation prerequisite, not a new adoption choice to answer implicitly.

Source provenance: Observatory `8cb1e7dbc268e2e5349d988f6b4c38440a41361b`; tools-ki `32b913c68bb826687638ad81334b06dd97888aeb`. These are local source revisions; effective installed CLI/runtime parity was not tested.

Exact checked source digests (SHA-256):

- [packages/evidence/src/work.ts](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/work.ts): `128beac8173ee966def035576d6e63e5f195746f8c5e374eb42015685bd7f2c8`.
- [packages/evidence/src/work-package.ts](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/work-package.ts): `cf5827983c161538c77e85b197c2c62958fcac107d46b09e84b47198780495ad`.
- [packages/contracts/src/work.ts](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/contracts/src/work.ts): `9ca9d0cb1f38632442d32726df3121578a09ab9edff9d18afaeac215fea69043`.
- [packages/evidence/src/sessions.ts](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/sessions.ts): `1bb8fc70bac179e6cc85265cb3871187b7e33ed997fa795d13c398ccf9d4f1f8`.
- [packages/contracts/src/sessions.ts](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/contracts/src/sessions.ts): `0e420eedd5b99e77fbb900d422923b0c0e7fd03e56604d5c3d31c9f037a33478`.
- [src/core/work/status.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/work/status.ts): `ba9fa44b5f81de4a24202ea464a94abcd3af2c3fbf9dc35e819ed653cf7012eb`.

## Queries

No outstanding queries from this read-only unit. Existing Project queries and unanswered adoption choices remain unchanged.

### 🤖 → 👤 Handoff to supervisor · since 01:13 GMT

👤 1 with supervisor · 🤖 0 running

- [with supervisor] Consumer-gap assessment and bounded follow-up · Observatory supervisor · since 01:13 GMT

🧵 ki.prj.observatory
