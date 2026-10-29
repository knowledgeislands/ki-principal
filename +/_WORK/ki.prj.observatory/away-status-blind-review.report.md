# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › away-status-blind-review

**🤖 → 👤 Handoff to supervisor · Run report at 01:45 GMT · last mark 01:04 GMT**

---

## Done

- Recommendation: **prepare a separate canonical-reader repair item; confidence high** — isolated fixtures reproduce correctness defects independently of the unresolved instrument-consolidation decision.
- Commits: none; no tracked files, work records, adoption, plan transitions, services, providers, credentials or remote resources changed or invoked.
- Source baseline: Observatory `96f999a457cb`, tools-ki `3afba45d1e95`; both working trees were clean at the final source check.
- Independent reproduction: 12 synthetic scenarios passed through current producer and consumer functions; public in-process CLI calls used isolated HOME/XDG roots and refused external capabilities, with zero forbidden calls.
- Route/cache check: the actual handler's default Work/Review wiring passed 22 assertions with fixture-backed evidence wrappers; warm reuse, explicit refresh, separate Review cache keys and uncached full Work were verified without starting a server.
- Existing regression check: 69 tests passed across Work, package reader, Focus, Review and mechanical-degradation suites; no failures. Their passing does not contradict the reproduced defects, which require additional regression coverage.
- Fixture corrections: an initial route wrapper retained a live mocked binding and recursed; an initial repeat reused fixture state. Both harness faults were corrected before the successful final observations; neither is a product defect.
- Report check: local evidence links, fixture totals and owner-report structure verified; Markdown lint passed.
- Blindness: no actual work queries, decisions, run reports, recommendations or design reviews were opened. APP-044, standing standards, incoming instructions, work definition/state and the complete runtime inbox were read directly; linked recommendations were not followed.

## In Progress

Nothing running.

Outstanding - no action requested now: no repair is currently adopted by this assessment. Producer ownership and latency questions below belong in preparation of a separately approved item. No live-estate performance or deployed-service check was authorised or performed. Reproduction inputs and observations are homed in this report; temporary fixture material has been cleared.

## Findings

### STATUS-AUTHORITY - The repair is separate from the restructure decision

**Goal:** Answer the supervisor's 29 October question: what current sources establish about reader differences, and the smallest properly adopted repair scope, if any.

**Scope:** Current product and tools-ki source, canonical APP-044, standing work-package/coordination standards and incoming consumer instructions; no prior assessment or linked proposal.

**As of:** 29 October 2026, 01:43 GMT/UTC.

The [incoming consumer instructions](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.observatory/messages.md:31) require assessment against the coherent producer contract, preserved redesign/report grouping, three work levels, seven states and one authoritative package/home entry. They prohibit another status authority and do not make coordination a consequence of package type or status. They authorise assessment, not this repair's adoption.

[KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md:1) is still `kind: decide`, `status: draft`. Its [boundary](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md:45) excludes removing readers and changing backend contracts. Its Waiting/Review relationship and moving or retiring Work retain individual approval gates. It expressly says its source observations do not adopt a separately reported status-reader repair. Folding this repair into it would change that boundary and mix a demonstrated correctness issue with unresolved consolidation choices.

The [naming standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md:140) makes typed names canonical while historical spellings remain readable indefinitely; resolution derives from actual valid definitions, and two physical definitions for one work are ambiguous. The [package location contract](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md:50) keeps Projects in the Capital, permits deliberately approved member-homed regular/ad hoc exceptions, and gives each work one authoritative physical package. Historical identifier compatibility and old single-file/checkpoint shape compatibility are distinct questions.

Current tools-ki source already reads five-file packages. Observatory's comments and [package-reader test double](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/work-package.test.ts:60) claiming the installed producer cannot read them are stale against the checked source. The local `ki` launcher also resolves through a local runner naming that tools-ki source entry point; no live status command was used to inspect real work.

Query raised: STATUS-REPAIR.

### STATUS-BEHAVIOUR - Reproduced disagreements are narrower than missing regular/member coverage

**Goal:** Reproduce the suspected differences against current source without providers or real work data.

**Scope:** Synthetic packages, two synthetic selected repositories, synthetic run homes, public `run(args, context)`, canonical parsing, `observeWork`, `observeReview` and the request handler; no real package bodies or run reports.

**As of:** 29 October 2026, 01:43 GMT/UTC.

The [Work page](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/instruments/src/work.ts:327) requests ordinary `/api/work`. The [Waiting page](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/instruments/src/waiting.ts:294) requests both APIs with `focus=1`. The [Review page](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/instruments/src/review.ts:235) requests ordinary `/api/review`, but the [server defaults](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/apps/site/src/server.ts:458) supply fast `observeWork(..., { focus: true })` to **both** Review branches. Therefore a claim that ordinary Review uses the same full status reading as Work is false for current default wiring. Review's acceptance-only branch differs in content selection, not in this status authority.

The [full reader](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/work.ts:182) asks tools-ki, then appends locally parsed packages whose exact IDs were not reported. The fast reader skips tools-ki status entirely and reads packages locally. [Canonical validation](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/work/status.ts:187) checks kind/level agreement and parent/coverage placement; [definition enumeration](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/work/status.ts:262) refuses ambiguous historical/typed homes through [workNames](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/work/identity.ts:2). The [local parser](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/work-package.ts:143) lacks those checks.

| Fixture | Canonical producer | Full Work | Fast Work / Review handoffs |
| --- | --- | --- | --- |
| Typed regular main and topic | 2 entries | 2 entries | 2 entries |
| Historical Project and regular topic packages | 2 entries | 2 entries | 2 entries |
| Single-file regular package | 1 entry | 1 entry | 0 entries |
| Historical checkpoint | 1 entry, warning | 1 entry | 0 entries |
| `reg` ID with Project level | Excluded, warning | Reintroduced | Displayed |
| Regular package with foreign-territory parent | Excluded, warning | Reintroduced | Displayed |
| Main State of play parenting itself | Excluded, warning | Reintroduced | Displayed |
| Historical and typed Project homes together | Exit 2, ambiguous | Source failure, no entries | Both displayed |
| `reg.topic` and `regular.topic` together | Exit 2, ambiguous | Source failure, no entries | Both displayed |
| Capital plus selected member's regular work | Each local home read | Both read | Both read |
| Same work ID in two selected repositories | Each local home read | Both retained | Both retained |
| Historical run home attached to typed Project | Run attached | Canonical path available† | Run omitted† |

† The last scenario directly compared producer `readWorkStatus` with an injected live run against fast `observeWork` with synthetic `thread.json`, status, PID and liveness. It did not assert full CLI liveness integration. The producer resolves historical run-home aliases; the [local run join](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/work-package.ts:246) requires an exact folder match.

Reproduction recipe: normal five-file fixtures used `worker: agent`, `supervisor: owner`, `state: handoff-to-supervisor`, a valid UTC `since`, and `parent: ex.sop.main`. Change only the indicated kind/level or parent for refusals. Duplicate pairs were `ex.alpha`/`ex.prj.alpha` and `ex.reg.topic`/`ex.regular.topic`; the single-file case placed state in `work.md` without `state.md`. The checkpoint was `model.alpha.md`, type `ki-checkpoint`, a valid `updated_at`, and rest status, with territory alias `ex`. The cross-repository case placed `ex.reg.intake` first only in the selected member, then in both repositories. Every case used a fresh fixture tree. The producer CLI's stdout flowed through actual `loadWorkStatus`/`parseWorkStatus`; filesystem and process ports were confined to fixtures or refused.

These results establish actual rejection bypass, duplicate-home disagreement, compatibility omissions and run-attachment disagreement. They do **not** establish a blanket inability to read regular work or members: valid regular levels and selected member homes already work. A synthetic query in the rejected kind-mismatch package also reached `focus.questions`; [readFocus](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/focus.ts:105) independently enumerates homes. Repairing status alone must not leave content from refused homes presented as authoritative.

Query raised: STATUS-REPAIR.

### STATUS-CONTRACT - Some desired capabilities need producer decisions rather than a consumer patch

**Goal:** Separate current consumer defects from missing features and unsettled producer API needs.

**Scope:** Existing JSON contract, package/home authority, projected fields and the reproduced boundary cases.

**As of:** 29 October 2026, 01:43 GMT/UTC.

- **Available consumer correction:** current `ki/work-status/v1` already supplies the flat entries, physical source paths, levels, states and run items needed by today's views. The consumer must preserve producer rejection rather than treat absence as permission to reconstruct an entry. [loadWorkStatus](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/ki.ts:336) currently discards successful-command warnings, so exclusion/diagnostic treatment also needs an explicit acceptance condition.
- **Missing projections, not proof of missing status:** the [consumer contract](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/contracts/src/work.ts:111) drops producer `parent`, `covers`, label, description, method revision and pending-message count. A hierarchy or coverage-register UI would require a separately specified feature. Those omissions do not prevent existing flat regular/member status rows.
- **Cross-repository authority is unresolved here:** the producer command is repository-scoped. It refuses alias duplicates within that repository, but the two-repository fixture shows neither that call nor Observatory's merge establishes one global home. The current status result also does not certify an owner-approved member exception or explicit coordination. Do not invent a precedence rule, infer coordination from state/type, or move packages. An estate-wide authoritative-home guarantee needs an owning producer contract or explicit resolution policy before a consumer can claim it.
- **Historical identity is not a rename request:** accepted output keeps the actual definition's ID and path. Compatibility does not authorise rewriting Project slugs, repository identities, work-record IDs, run identities, report paths or stored packages. Existing report lookup/grouping must remain attached to the accepted physical home.
- **Producer performance API is conditional:** a lighter, batched or reusable producer status interface may be needed, but this review does not prove that a new API is required. First establish whether existing JSON with shared bounded loading and caching satisfies an agreed latency budget. If not, seek a producer-owned addition; importing an internal tools-ki parser or copying its rules would not establish a stable public contract.

Query raised: STATUS-REPAIR; producer questions are preparation dependencies, not adopted work.

### STATUS-SCOPE - The smallest repair preserves the current views and their operating limits

**Goal:** Bound a properly adopted repair and the evidence required before delivery.

**Scope:** Status/home consumption for existing Work, Waiting and Review, without instrument consolidation, new status features or runtime operations.

**As of:** 29 October 2026, 01:43 GMT/UTC.

The minimum proposed item is **make existing Work, Waiting and Review consume one producer-authoritative status/home result and preserve its refusals**. It would replace the competing local status interpretation and the full-path resurrection fallback, while retaining local reading of display content only for accepted homes. It should preserve valid regular/member entries, historical and typed spelling compatibility, single-file/checkpoint tolerance while the producer supports it, and alias-aware run/report attachment. It should not add coordinator inference, a hierarchy UI, a new estate scanner, redirects, view retirement, package migration, feedback mutation, scheduler work or deployment.

The [fast-reading cache](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/apps/site/src/server.ts:528) reuses readings for 30 seconds, serves stale readings while refreshing up to ten minutes, and waits for an explicit fresh read or an older reading. Work-focus, Review-focus and Review-all have distinct keys; full Work bypasses that cache. [Membership caching](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/members.ts:12) separately holds tolerant estate membership for five minutes. Fast work reads up to eight selected members concurrently and avoids eager latest-report reads; full work reads members serially. The [producer command](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/commands/work/index.ts:103) obtains run evidence before status, through [workRuns](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:1372). Simply substituting full serial CLI calls into every fast request would therefore be an unjustified latency change. The source comment about minute-long estate reads is not a benchmark measured by this review.

Meaningful acceptance requires:

1. Run the fixture matrix through the public producer seam and actual server defaults, including producer warnings/refusals, duplicates, selected/unavailable members, malformed state, historical shapes and run-home aliases. A mock asserting that tools-ki still cannot read packages is insufficient.
2. Assert that rejected or ambiguous homes cannot reappear through fallback, questions or handoff rows; errors remain visible and do not silently become an authoritative empty success. Define the cross-repository-home limit explicitly rather than claiming an unimplemented guarantee.
3. Preserve all three levels, seven states, derived views, report lookup/grouping, redaction and source-path containment, acceptance-only Review selection and Beacon destinations. Retain existing addresses and instruments.
4. Exercise cold/warm/fresh and stale-refresh paths, scoped cache separation, bounded concurrent loads, membership changes and producer failure. Measure representative synthetic estate latency and process counts against an agreed budget before choosing the final producer interface.
5. Extend the [mechanical-degradation gate](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/apps/site/src/degraded.test.ts:104) through the changed fast paths and default wiring. No provider, LLM, credentials or service must be necessary to produce a useful degraded response.

No such implementation scope is already adopted. Preparation should settle the producer-interface/latency boundary and any producer-owned dependency, then obtain adoption and an agreed plan under normal repository governance. APP-044 stays Draft with all consolidation gates intact.

Query raised: STATUS-REPAIR.

## Queries

### STATUS-REPAIR - Choose the home for the demonstrated correctness repair

**Context:** Current source and isolated fixtures establish consumer defects: canonical exclusions are resurrected, fast views accept alias-duplicate homes that the producer refuses, and supported historical shapes/run homes diverge. Valid regular work and selected member repositories already have flat status coverage. [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) remains a Draft consolidation decision with reader/backend exclusions and unresolved owner gates. Estate-wide home resolution and any lower-cost producer API remain explicit preparation questions.

**Query:** Should the coordinator seek separate adoption and planning for the bounded canonical-reader correctness repair described above?

**Options:**

a) (recommended, confidence high - direct fixture evidence establishes a separable correctness defect without resolving the restructure choices) Prepare a separate repair item for adoption, preserving current views and producer authority, with latency and cross-repository-home limits settled before implementation. This report itself creates or adopts nothing.

b) Retain the current readers pending further evidence, explicitly carrying the reproduced rejection and ambiguity defects; useful if the supervisor wants deployed-version or measured-estate evidence before prioritisation.

c) Include the repair in APP-044 only after explicitly changing that record's boundary and agreeing the resulting plan; this would couple the correction to unresolved consolidation decisions and is not recommended.

### 🤖 → 👤 Handoff to supervisor · since 01:45 GMT

👤 1 with you · 🤖 0 running

- [with you] STATUS-REPAIR · supervisor · since 01:45 GMT

🧵 ki.prj.observatory
