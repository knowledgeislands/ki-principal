# Approved work model and typed identity plan

**Owner:** Kris Brown. **Work:** `ki.ways-of-working`. **As of:** 28 October 2026, 02:08 GMT, sol.local. **Status:** Planning only; no Ready baseline, source amendment, record transition, package rename or migration staged.

## Authority and remaining choices

The [owner log](../decisions.md), “Both approvals and other-machine condition”, records approval of territory/type/name IDs and written-model alignment. Those directions are settled; do not restart the design loop or ask for them again. The [stage-one brief](work-id-shape-brief.md) supplies design options, not an additional migration grant. The complete captured incoming queue and its logged dispositions were read; individual relays do not enlarge authority.

| Class | Disposition |
| --- | --- |
| Current approval | Deliver typed IDs and the agreed written model, preserving newer other-machine work. |
| Existing decisions | Preserve assigned-package cascade, acknowledged handover, parent/covers and per-package hold/mark. |
| Separately source-approved | AT-REST adoption request; independent interactive flow; HNR METHOD clarifications below. |
| Proposals only | Both account-steering messages; no account, provider, authentication or service work in this plan. |
| Material choices | Proposed lower-case spelling and `main` defaults; compatibility mechanism; pilot authorisation and safety. |
| Excluded | Eighth-state implementation, report-policy rewrite, STEWARD-FIELD, host syntax and cross-territory writes. |

AT-REST is more than an unattributed proposal: Personal's current `personal.regular.rig-terra/decisions.md` locates the struck history at `890290c0`; its original AT-REST entry records Kris's “AT REST: a)” at 19:05 GMT on 27 October. This separately authorises the request to adopt an at-rest state. It does not settle glyph, transition semantics, placement among the seven states or runtime representation. Keep that separately scoped need out of MOD-011 and the typed-ID candidate; do not silently add an eighth state.

HNR's `hnr.sop.5ge/decisions.md`, INTERACTIVE-FLOW, 27 October 23:29 GMT, directly records Kris asking to work through interactive prompts, register answers and process them in the background while proceeding to unaffected requests. Carry that compatible scheduling clarification: persist each answer before dispatch, honour dependencies and the existing authority boundary, then continue independent questions. It grants no report-policy rewrite or automatic approval.

HNR's `hnr/decisions.md` records wow-steer2 and Kris's WOW-STEER instruction at 00:16 GMT on 28 October to send the remaining feedback. The captured METHOD line is the authorised feedback, not an already-enacted shared standard. Fit its compatible clarification into MOD-011: a record may motivate a Project containing just that record; register a separate finite-outcome Project note, link the original record by its `project` slug, retain the record's ID/history/status and create no duplicate delivery. Open or assign its package only through existing registration, cap, first-message seeding and acknowledged-assignment rules; a Project need not immediately have a package or its own thread.

Make Capital/principal the default home for regular and ad hoc packages as well as Project packages, with any member-repository home a deliberate declared exception in `work.md` Scope. Keep execution, records, priority and acceptance with each owning repository. A principal-seated thread bootstraps the territory: identify its Capital, read Charter and governed inventory, resolve exact registered checkouts, then read each execution repository's rules. Package and thread are not one-to-one. A binding's repository is not evidence of a live thread's working directory. Shared-rule narrowing must be explicit in the candidate and corresponding harness contract, never inferred as a relocation grant.

## Current sources and boundaries

The already-created Principal merge `40ba0929` remains an ancestor of current `8eaed84495d4`; preserve it and its retained local design and remote queues. No repeated merge or reset is needed. Inspected heads: harness `ede90d68bc1f`, tools-ki `74a07bf83c92`, Observatory `8cb1e7dbc268`, HNR Principal `9f1f54d00243`. Method revision remains `def7f055`, not harness HEAD. These are local observations, not proof that all other-machine work has been pushed.

The exact current model inputs still match the wording draft's SHA-256 values: Work Process `3ca01e82e4307003b50e737c18cb88604df65df3955e5086e493981bbf6c88b1`; GDR9 `dc6879077096b8925197c24a2702fe2ccb548b5f9d4e6a646f43cb35137d1ff9`. Revalidate actual bytes before later edits. Preserve the 25 October cadence amendment already present in Work Process; update GDR9's older history wording consistently. The old patch remains input, not a patch to apply blindly.

HNR's newer inventory, including `5g-emerge/apps-io.5g-emerge.p2ms3`, survives. Retain `hnr`, `hnr.sop.5ge`, `hnr.sop.sites`, their ownership, parent/covers, holds and marks. The captured sample describes 24 packages and 43 principal bindings; this inspection sees 25 package directories with `work.md`, so do not freeze the older sample as a migration manifest. Four exact member identities have local registry bindings; fourteen newer declared identities do not. Old checkout basenames are not rename aliases. Resolve missing roots through the receiver, never guess them. The separately declared shared-content root confers no membership or write authority.

Other-machine publication remains a factual prerequisite for writes to potentially affected unpublished areas. This run changes only this note. Before delivery, each owner checks actual head/index/path ownership and publication status; stop on a contested path, unexpected code or divergence rather than treating clean local state as proof of remote completeness.

## Identity contract proposed for delivery

Use `<territory>.<type>.<name>`, with stored types `sop`, `prj`, `regular` and each variable segment matching `[a-z0-9]+(-[a-z0-9]+)*`. PRJ/SOP may remain display abbreviations. Proposed defaults: main SoP `<territory>.sop.main`; regular umbrella `<territory>.regular.main`; Project `<territory>.prj.<project-slug>`; secondary SoP `<territory>.sop.<name>`; ad hoc `<territory>.regular.<slug>`. Reserve `main` for the two umbrellas only after receiver-local collision checks. Do not create four-part regular children or derive parentage from the prefix. Themes and hosts remain absent from IDs; levels and states do not change.

Bounded collision checks found no live/review-directory or derived-slug collision in accessible KI/HNR Principal scope for `ki.sop.main`, `ki.regular.main`, `ki.prj.ways-of-working`, `ki.prj.baseline-rollout`, `hnr.sop.main` or `hnr.regular.main`. Corresponding checked runtime target directories are absent. KI includes a leftover directory without `work.md`, which is not counted as a package but remains a collision surface. This is no estate-wide guarantee: recheck every proposed destination, alias key, native-binding target and receiver scope immediately before migration. An inaccessible or ambiguous destination blocks that migration only.

Keep Project registry slug `ways-of-working` unchanged, likewise `baseline-rollout` for the pilot; `project:` never becomes a dotted package ID. A runtime slug replaces dots with hyphens and is never parsed backwards to recover identity.

Readers must accept current IDs and typed IDs before writers emit typed identities. Propose an explicit old-to-new resolution map at the shared lookup boundary, with duplicate/ambiguous mappings refused, cycle detection and one canonical status entry. Retain historical old-ID readability and old-ID lookup without a time limit; no expiry, cleanup or deletion is authorised. Any future retirement needs a separate decision and evidence. Do not rewrite historical reports, Git objects or original message provenance to pretend they were born with new IDs.

## Dependency and path matrix

Paths below are relative to the owning repository. Each row is a delivery candidate, not authority to edit it now.

| Order | Owner / candidate | Exact scope key | Depends on / sufficient final evidence |
| --- | --- | --- | --- |
| 1 | Ways of working / MOD-011 | P-model | Source safety; paired semantic/link/adapter review and hooks. |
| 2 | Ways of working / harness identity contract | H-rules | 1's agreed semantics; one final harness verification on changed candidate. |
| 3 | Tools burndown / compatible readers | T-readers | 2's contract; one final CLI verification including continuity and recovery cases. |
| 4 | Observatory steward / consumer need | O-work | 3's stable output; focused consumer evidence, build only if its rules require it. |
| 5 | Baseline rollout steward / single KI pilot | P-pilot | 2-3 green, 4 assessed; manifest, ownership, quiescence and rollback. |
| 6 | HNR SoP / receiver need | N-receiver | 1-3 available; receiver resolves inventory, safety, exceptions and its own rollout. |

**P-model:** Reuse `Streams/Roadmap/KI-PRINCIPAL-MOD-011-amend-work-model-assigned-package-cascade.md`; keep draft/null baseline until its actual planning gate. Re-ground `design/mod011-wording.md`, then amend `Pillars/Philosophy/Model/Processes/Work Process/Work Process.md` and `Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md` together, dated in place. Cover assigned stewardship/handover, package/thread distinction, record promotion, homes/discovery, routing, parent/covers, per-package marks/holds, host requirement versus seat and cadence. Describe typed target identities with explicit coexistence; no live rename is part of the two-document amendment. Retain seven states, roles, banner and roadmap mapping. Do not rewrite the diagram or claim a new renderer is delivered; any stale visual is a separately scoped follow-up.

**H-rules:** `skills/change-management/ki-coordination/references/standards-coordination.md`, its `scripts/rubric/items/threads.ts` and contexts; `skills/governance/ki-work-package/references/standards-work-package.md`, affected rubric items/contexts; `skills/change-management/ki-work/references/standards-project-registry.md` and relevant `ki-next`/`ki-work-roadmap` promotion/lookup boundaries where needed. Follow actual imports instead of assuming the shared work-identifiers helper defines package IDs - it defines record IDs. Update affected skill entry points and generated rubric publications. Use `skills/change-management/ki-coordination/scripts/generate/index.ts` to regenerate only affected `hooks/coordinator-reminder.sh`, `output-styles/ki-coordinator.md` and delegation report/prompt surfaces; retain owner-report policy. Reuse `scripts/banner.test.ts` and existing placement fixtures. No STEWARD-FIELD encoding.

**T-readers:** `src/core/work/status.ts` (grammar, definition lookup, main/secondary placement and parent/covers), `registry.ts`, `prompts.ts`, `src/commands/work/index.ts`, `src/commands/agent/index.ts`; `src/core/agent/thread.ts`, `identities.ts`, `context.ts`, `runs.ts`, `controls.ts`, `control-store.ts` and `src/commands/agent/control.ts` at their actual identity boundaries. Current `statePlacement` rejects main/non-territory parent/covers already allowed by the method: fix that contract mismatch in the same reader candidate. Openers must preserve declared scope and perform territory discovery; status and bindings resolve both IDs without duplicate work. Reuse `src/tests/cli/work/status.test.ts`, `agent-prompts.test.ts`, `agent-threads.test.ts` and existing control/recovery suites. Native binding metadata under XDG state is runtime-owned; inspect its actual declared schema before selecting mutable fields, never invent a new path or rewrite native session identity.

**O-work:** `packages/instruments/src/work.ts` and its actual contract/adapter consumers in `apps-observatory.local`; send the need to `ki.observatory/messages.md`. Consume coherent CLI identity/placement, retain report lookup and grouping. No deployment, service restart or separate status authority.

**P-pilot:** Propose only `ki.baseline-rollout` to `ki.prj.baseline-rollout`, in KI Principal, through its own steward. Its observed On hold remains On hold; a rename is neither receive nor release. Do not rename this live owning package `ki.ways-of-working` as a demonstration. The pilot needs the receiving steward's acknowledged ownership and a bounded migration grant before mutation; eligibility is rechecked, not presumed from an old state file.

**N-receiver:** Send a need to HNR's `+/_WORK/hnr/messages.md`, respecting its paused hold; no write to HNR records/packages in this run. Receiver preserves the new roster, resolves missing exact local identities, declares exceptions and chooses its own rollout. Observatory/HNR may report no source change necessary after assessment; do not create redundant records merely to mirror this matrix.

## Minimal future records and routing

MOD-011 is the single existing canonical amendment record; do not create a second model record or new GDR. For deferred delivery, propose exactly three further records: harness a harness typed-identity record allocated by its receiving owner owned by Ways of working; tools-ki a tools-ki compatible-reader record allocated by its receiving owner owned by Tools burndown; Principal a Principal pilot record allocated by its receiving owner owned by Baseline rollout. These are unreserved proposed next identifiers, not created records; the receiving owner checks allocator/history and selects the legal next serial before capture. No foreign record is written by this work. If a receiver can execute an immediately owned need without deferral, its message suffices rather than manufacturing a roadmap item.

Route exact needs, dependency and completion evidence to those owners via `messages.md`; identify true reader-before-writer prerequisites as blocking. Route AT-REST separately to Ways of working for state-specific planning; account steering remains an idea with its source owner. No duplicate record for every generated file, test, consumer or rollout territory.

## Pilot transaction and rollback

Before any pilot, enumerate every incoming reference to its old ID and path in accessible tracked packages, parent/covers registers, open briefs, message targets/senders, queued launch requests, dependency edges, run homes, native bindings, status/openers and Observatory report routes. Expand only to declared dependencies; an inaccessible incoming reference stays a named blocker, not assumed absent. Preserve original queued message bytes/order and immutable sender/target provenance; resolve through the compatibility map at consumption time. Historical references remain readable.

Freeze new pilot launches and obtain acknowledgement from the current steward; wait for active and queued native/run transactions to finish or safely defer them. Snapshot exact source/destination blobs, reference manifest, alias map and runtime binding versions outside the repository. Keep queued launch tokens, run/attempt IDs, native session UUIDs, dependency identities and original runtime folders immutable. Prefer lookup indirection to physical runtime moves. If an existing reader cannot resolve a frozen queued/native identity safely, keep that identity on the old route and defer the pilot until it can; do not edit launch records to force continuity.

Under one serialised write window, revalidate snapshot versions, then change the one package directory and identity fields plus every mutable incoming reference in its explicit manifest. Preserve state/since/received/beat/mark, queries/decisions, assignment and Project slug. Publish the alias mapping before enabling new writers. No mixed old/new split-brain window may accept dispatch. Reopen dispatch only after old/new lookup, resume, one-entry status, opener scope and queued delivery all resolve to the same package.

Rollback is a compensating explicit-path commit restoring the original directory, fields and mutable references, with version-checked restoration of mutable binding pointers only. Keep compatibility lookup and immutable IDs/runtime folders; reconcile any messages arriving after the snapshot before restoring pointers. Never reset shared history, overwrite another writer or replay a launch twice. A version mismatch stops rollback for the steward to reconcile. Prove recovery against the same candidate before wider migration, not through a second live pilot.

## Verification reuse and exact next action

Reuse the reconciler's merge-preservation evidence, original model reviews, MOD-011 hashes/patch work and existing fixtures. Revalidate only facts that can have advanced. Each changed candidate gets one sufficient final gate against its actual combined result: model semantic parity/exact-case links/Streams and authoring requirements; harness's declared sequential test/type/focused-audit gate; tools-ki's declared product gate with relevant status/opener/control recovery cases; consumer's own required gate; pilot's manifest and continuity/rollback gate. Required hooks remain mandatory. Do not repeat unchanged coverage, builds, deploys, archive probes or full estate audits. A changed candidate or actual failure justifies replacement evidence; a fresh destination head calls for scoped revalidation first. Local symlinked CLI delivery does not imply a release/install cycle.

**Next action:** coordinator receives this note, resolves the pending other-machine publication fact for affected paths, then prepares the current-source MOD-011 candidate under its existing approved direction and sends compatible-reader needs to their owners. Confirm only genuinely new choices at the appropriate delivery boundary: `main` reservation/lower-case grammar and explicit compatibility mechanism; pilot ownership and mutation envelope; separately scoped AT-REST representation. Do not reopen the two core approvals. No test/build/provider call, authentication/install/release, canonical write, migration or Ready baseline belongs to this planning run.
