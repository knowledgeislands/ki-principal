# Acquire capability consolidation

Reviewed 19 October 2026 against Acquire, the canonical KI acquisition skills and the current tools-ki importer. This replaces the initial inventory as the working assessment. It proposes a bounded consolidation; it does not approve implementation, accept roadmap records or change source/state bytes.

## Conclusion

Use one common acquisition skill, thin provider-specific contracts and one repository capture entry point. Keep request receipts, captured source packages, routing context and technical acquisition state distinct. Remove redundant instructions and obsolete working surfaces rather than introducing another queue or renaming every package.

The hidden `.acquire/` directory is an implementation choice, not a necessary capability. Its retained state and proof are necessary. Finish the previously selected move to `+/_ACQUIRE/` only after the importer supports it independently of capture paths.

## Evidence and current state

Acquire currently contains 3,278 capture files, 26 `.acquire/` files, 17 intake files including its README, nine context files and five binary-probe files. These are observed filesystem counts, not completeness claims about the external providers.

There are 16 canonical request receipts: 14 closed, one blocked on original messaging audio and one received with the unidentified seven-byte text submission. Request discovery already works from receipt state. No second pending list is needed.

The current Granola ledger retains 344 meeting identities. Its stored flagged record has zero meetings and zero unknown folders. This is local evidence only; no new provider read or import was performed. The ChatGPT export checkpoint describes 334 conversations and zero failed conversions. Historical captures outside recent owner-requested windows remain historical, not newly authorised imports.

The old `+/_CHECKPOINTS/` and `+/_THREADS/` areas were already migrated by another conversation. Acquire now retains its local conversational work under `+/_WORK/kb.regular.acquire-intake/`; live binary investigation evidence moved to `scripts/binary-probe/`, while spent reports are recoverable from Git. The assessment and cross-capability design remain here in the existing KI work folder.

The owner is moving `context/chatgpt/` to `context/`. All nine moved files currently match their committed originals byte for byte. Those moves are pre-existing owner changes and are outside this assessment's commit. Their content and callers still contain ChatGPT-specific assumptions and need the agreed follow-through.

The existing two acquisition skill entry points pass the scoped mechanical `ki-skills` audit. That verifies their declared shape, not the judgment that their responsibilities are optimally divided. The duplication findings below come from reading their contracts and the repository guides.

## One owner for each instruction

| Surface | Responsibility |
| --- | --- |
| `CAPTURE.md` | Single human-facing capture entry: purpose, goals, short workflow and route selection. |
| `AGENTS.md` | Standing repository authority and local exceptions; point to the capture entry and contracts. |
| `README.md` | Repository purpose, folder map and entry links. |
| Common `ki-acquire` skill | Reusable acquisition invariants and the operation across providers and runtimes. |
| Provider acquisition skills | Source-specific identities, completeness, capabilities, omissions and provider operations. |
| Repository capture guides | Local package/receipt conventions and the selected environment's practical steps. |
| `intake/README.md` | Canonical request identity, fulfilment and exact supplied-message evidence schema. |
| KI Principal | Durable acquisition model, rationale and accepted policy. |
| tools-ki | Executable importers, manifests, state persistence and safe relocation. |

`CAPTURE-CHATGPT.md` should remain a tiny compatibility pointer while existing prompts use it. It already is a pointer; it is not a second entry policy. Do not remove it merely to reduce the root file count. Capture detail belongs under `docs/guides/`, not in two root procedures.

Orientation can briefly state purpose and link onwards; detailed rules must have one maintained owner. Repository guides must retain enough local instruction for a connector-only capture to start without checking out another repository. A new skill must not make installed CLI tooling or another runtime a prerequisite for a simple text submission.

### Common skill

A common `ki-acquire` skill is justified by actual repetition across ChatGPT, Granola and direct intake. Create it in the canonical KI Agentic Harness, not as an unrelated user-local skill or a hand-edited installed symlink.

Its common contract should cover:

- Establish the authorised supplied scope, source identity, provenance, chronology and explicit coverage type.
- Reuse verified request/package identities on retries; preserve amendments and earlier versions.
- Route from evidence, preserving unknown or conflicting routes without inventing a territory.
- Preserve the material promised by the selected route, its required originals and explicit omissions.
- Verify destination bytes and distinguish offered, received, committed and remotely verified material.
- Retain the handling proof needed after temporary capture removal; keep receiver reconciliation and source retirement separately authorised.

It must be a small common operation with supporting references only where needed. It must not introduce a database, universal receipt for every meeting, extra approval ceremony or a fictional provider adapter. Existing machine-readable adapter declarations remain on provider skills until a reviewed tools-ki contract says otherwise.

### Provider skills

Retain `ki-acquire-chatgpt` and `ki-acquire-granola`, but make common invariants references to the shared owner. Preserve their distinct source promises:

- ChatGPT account/project export acquisition preserves returned conversation content and source relationships. A live-thread digest is an explicitly bounded derived capture, not a complete raw export. Preserve that distinction, source-boundary marks, amendments, artefact obligations and the current prepared-capture CLI capability limits.
- Granola owns principal-only selection, date windows, stable folder/meeting UUIDs, pagination, note/transcript coverage, screenshot manifests and the separately confirmed additive Acquired marker. The common skill must not weaken these into a generic digest or authorise provider writes.

Both skills currently repeat lifecycle separation, identities, version/hash evidence, fidelity, retries and retirement constraints. The detailed provider rules remain where they are; the shared rules should be stated once. Provider-specific retirement checks remain conditional detail, not the default capture workflow.

## Proposed top-level contract

| Location | Contents and action |
| --- | --- |
| `captures/<territory>/<source-or-ingress>/...` | Routed source packages and originals. Preserve existing paths and identities. |
| `context/<territory>/...` | Small source-independent routing/context summaries; Capitals remain authoritative. |
| `intake/` | Compact owner-request receipts. One request can produce zero, one or several packages. |
| `docs/` | Practical local guides and the existing roadmap; no per-capture tickets. |
| `+/` | Working areas and, after tooling support, tracked acquisition state/proof under `+/_ACQUIRE/`. |
| `-/` | The existing outbound working area. |
| `.agents/` and existing configuration | Managed skills/bindings and repository configuration. |

Keep `captures/` as the physical package root. Customs describes the facility and clearance describes a lifecycle stage; neither needs another directory or a rename of thousands of files. Earlier Customs/clearance discussion did not enact a capture-root migration. This recommendation needs owner agreement before being treated as the final naming decision.

There is no separate acquisition log to introduce. Git records changes; intake receipts record owner requests; package manifests and technical state record source preservation and handling. They should link to each other rather than repeat every field or copy original bytes.

### Git and source-store pairing

Retain the declared `sources-acquire` binding. For externally held assets, the relative item path in the store mirrors its Git capture-package path. Git keeps the asset locator, exact filename, byte count, hash and disposition; the source store keeps the actual externally held bytes. Existing images in Git stay there. A batch has one identity and one manifest, regardless of byte location.

The store's `+/` remains inbound delivery, not an archive. Remove only a specifically verified duplicate after its preservation and publication checks satisfy the existing clearance authority. Never delete an unexplained inbound item by age or name.

### Remove `.acquire/` through the existing state work

The 26 files are not a second owner-request inbox:

- The Granola ledger supplies source/account identity, versions, capture locators, image/transcript evidence and handled-source suppression. Removing it can re-import already handled material or invalidate marker evidence.
- The ChatGPT checkpoint preserves export bindings, conversion outcomes, conversation identities and receiver moves. It serves a different source contract from intake receipts.
- Migration manifests, original receiver ledgers and reconciliation evidence prove earlier moves and variants.
- The historical export converter is a reproducibility artefact; it is not a reusable importer merely because it ends in `.py`.

Recommended final state placement is the already selected `+/_ACQUIRE/{granola,chatgpt,migration}/`, with all source bytes and historical locators retained. Extend the existing Granola state-migration work to specify the untouched ChatGPT/proof disposition explicitly; do not silently include it in a Granola-only migration grant.

Current code at tools-ki `src/core/acquire/granola/layout.ts` selects `.acquire/granola/` whenever `capture_root` is configured. No independently selectable state root is accepted by the current Granola skill declaration. Retention safeguards have landed, but they do not change this location contract. Changing `capture_root`, adding a symlink or simply moving the ledger is not a safe substitute.

Before relocation, add and verify the independent state-root contract in tools-ki and the adapter declaration. Then migrate using exact source/destination hashes, retained paths and versions, handled dispositions and a committed rollback locator. Verify import/reconcile/marker preview against the relocated state without a reset or live provider mutation. Only then remove the old tracked paths. Do not compact Git history.

### Intake retention

Keep the request layer because request and source-package identities differ. Simplify its presentation and avoid copying source manifests into receipts. Closed receipts disappear from pending discovery already; closure is not source reconciliation.

The minimum surviving receipt is request identity and dates, supplied scope and evidence locator, any sole exact supplied text, capture IDs/paths, verified preservation locators, disposition and unresolved limits. Compact redundant progress prose only after those facts are homed. Do not create an archive queue or apply an age-based deletion rule. Any later deletion of a whole receipt needs an agreed proof contract; this assessment does not grant it.

### Scripts

The five `scripts/binary-probe/` files are an offline MCP/attachment engineering prototype and its tests. They do not implement routine capture, and their real transport/identity binding is unimplemented. Do not present them as a working acquisition service or move them wholesale into the common skill.

Keep the prototype attached to the existing binary-bridge review until its engineering home/disposition is decided. Reusable CLI execution belongs in tools-ki; a genuinely skill-internal helper can live in its owning skill's `scripts/`. One-off reproduction code stays with its source/migration proof. The target has no general top-level `scripts/` directory unless a concrete maintained repository operation needs one.

## Existing work and disposition

These are current canonical states, not self-acceptance or permission to start every item.

| Record | State | Consolidation disposition |
| --- | --- | --- |
| [KB-ACQUIRE-002][acq-002] | Draft | Existing carrier for physical state relocation; tooling prerequisite remains. |
| [KB-ACQUIRE-003][acq-003] | Awaiting review | Keep offline delivery distinct from unproved live bridge; settle prototype ownership. |
| [KB-ACQUIRE-004][acq-004] | Awaiting review | Working screenshots/markers have delivery evidence; no new importer is needed. |
| [KB-ACQUIRE-005][acq-005] | Triage | Later dispatch trial; not a prerequisite for capturing supplied knowledge. |
| [KB-ACQUIRE-006][acq-006] | Triage | Incorporate demonstrated store/clearance paths; retain prospective scope separately. |
| [KB-ACQUIRE-007][acq-007] | Triage | Downstream dispatch/return; not part of capture's completion claim. |
| [KB-ACQUIRE-008][acq-008] | Triage | Use to develop context refresh; do not make the trial depend on another queue. |
| [KB-ACQUIRE-009][acq-009] | Awaiting review | Preserve working source marks and explicit coverage; inspect before changing common rules. |
| [KB-ACQUIRE-010][acq-010] | Awaiting review | Already delivers the single front door; consolidate around it. |

[acq-002]: /Users/krisbrown/workspaces/personal/acquire/docs/roadmap/KB-ACQUIRE-002-migrate-granola-state.md
[acq-003]: /Users/krisbrown/workspaces/personal/acquire/docs/roadmap/KB-ACQUIRE-003-investigate-binary-bridge.md
[acq-004]: /Users/krisbrown/workspaces/personal/acquire/docs/roadmap/KB-ACQUIRE-004-granola-acquired-workflow.md
[acq-005]: /Users/krisbrown/workspaces/personal/acquire/docs/roadmap/KB-ACQUIRE-005-seed-and-return-loop.md
[acq-006]: /Users/krisbrown/workspaces/personal/acquire/docs/roadmap/KB-ACQUIRE-006-image-video-holding-area.md
[acq-007]: /Users/krisbrown/workspaces/personal/acquire/docs/roadmap/KB-ACQUIRE-007-dispatch-packet-push-and-return.md
[acq-008]: /Users/krisbrown/workspaces/personal/acquire/docs/roadmap/KB-ACQUIRE-008-routing-knowledge-cards.md
[acq-009]: /Users/krisbrown/workspaces/personal/acquire/docs/roadmap/KB-ACQUIRE-009-chat-capture-marks.md
[acq-010]: /Users/krisbrown/workspaces/personal/acquire/docs/roadmap/KB-ACQUIRE-010-general-capture-entry-point.md

The earlier stocktake remains useful source material, but its historical provider counts, holding suggestions and outstanding queries are not current operating instructions. Do not revive its proposed size caps, schedules or old bridge launches as part of this cleanup.

## Implementation plan for agreement

1. Finish the source-independent context change with the owner: agree ownership of the moved files, update live callers and summary wording, then verify bootstrap and territory links. Do not stage the owner's pre-existing moves without that ownership agreement.
2. Establish the small common `ki-acquire` contract in the canonical Harness, then point the provider contracts at it while retaining their capability declarations and fidelity. Declare/install it through the native managed route. Verify ordinary supplied text, live digest, complete export, Granola import, required-original gaps and unchanged retry.
3. Consolidate Acquire's `CAPTURE.md`, `AGENTS.md`, README and guides around the responsibility table. Keep the compatibility stub. Shorten the receipt explanation, retaining its existing schema and exact evidence. Make the folder map describe the actual implemented structure.
4. Complete the tools-ki state-root prerequisite and the reviewed state/proof migration under the existing work carrier. Verify every retained state/proof byte and handled disposition before removing `.acquire/`; leave source packages and provider state untouched by the documentation pass.
5. Resolve the binary prototype's engineering home or retained-evidence disposition under the existing review. Remove the top-level scripts surface only after that home and recovery evidence are established. Review existing delivered records with the owner; do not automatically accept or reopen them.

The initial documentation/skill consolidation and the later executable state relocation are distinct delivery boundaries. Continue ordinary intake throughout. No new coordination thread, source-store binding, provider import window, remote service, schedule, source retirement or receiver write follows from this plan.

## Acceptance checks

A new operator can start from `CAPTURE.md`, choose one route and complete a simple text capture without loading every provider guide or acquiring another runtime. AGENTS supplies repository authority and short pointers. Compatibility prompts still reach the same entry point. `context/<territory>/` is discoverable without a provider name. Each shared rule has one detailed owner and provider-specific source guarantees remain intact.

Retries reuse the right identities; amended content remains explicit. Required-original gaps stay visible. Exact source bytes, historical package paths, receipts, handling evidence and variants survive. The later state relocation neither reacquires handled sources nor grants provider mutation. A receipt's pending status is discoverable without a second queue. Existing roadmap records retain their lifecycle until separately reviewed.
