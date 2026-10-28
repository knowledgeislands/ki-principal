# Coordination for any work package: merged report

**Brief:** [coord-any-package-brief.md](coord-any-package-brief.md). **Reviews:** [Codex](coord-any-package-review-codex.md), [Claude](coord-any-package-review-claude.md). **Owning work:** `ki.ways-of-working`. **Date:** 2026-10-28. **Status:** Recommendation only; no general proposal enacted.

## Summary

Make coordination an optional, explicitly opened session role on any valid work package. Regular work keeps its identity; a finite backlog can have a coordinating episode without a new Project or permanent coordinator. State of play is the specialised version that coordinates assigned packages. Conversational captures remain conversational. Preserve one authoritative package, state and inbox, with principal-default homes and deliberately approved member exceptions. Prefer an ordinary principal home reference and authorised delivery to the real inbox over a second pointer package. The package's acknowledged steward tends it; the parent State of play checks discovery and coverage without taking it over.

Acquire's interim exception is already approved and stays usable now. This design does not wait for MOD011 integration to honour that exception, and does not reopen its package-home choice. The existing bootstrap, style and repository exclusions must be read subject to the specific owner exception for this selected work; all other capture/provider boundaries remain. A missing automated reminder is a disclosed capability limitation, not a revocation of the exception. General policy, tooling changes and live migration still require the owner decisions and receiving-owner delivery described below.

Four separable choices are enough: eligibility, home rule, pointer representation and tending. Confidence is high on optional coordination, one authoritative package and explicit tending responsibility. Confidence is medium on the exact discovery representation; both reviewers independently ranked that choice before reading the brief's reflections, without seeing these merged options or any other review. The options below are recommendations, not grants.

## Source evidence

Source keys keep the matrices readable. Each link names the actual owner and entry point; the precise affected paths are expanded below. All observations are bounded to the inspected sources, not an estate-wide inventory.

- **S1:** [Work Process levels](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md:37>), especially 43-55, Roles and Homes; [GDR9](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md:28>), especially 30 and 39.
- **S2:** [Coordination levels and forms](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md:122>), Session kinds at 426-432, generated sources at 592-632, assigned-package rules at 658 and 772, opening/bootstrap at 796-854, messages at 856-866.
- **S3:** [Package location/closed contract](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md:52>), especially 56-58, 64-82, 135-152 and native-session authority at 371.
- **S4:** [Generator](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/scripts/generate/index.ts:21>), especially 61-92; [authored hook filter](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/hooks/coordinator-reminder.sh:80>), especially 90-94; [rendered style](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/output-styles/ki-coordinator.md:14>).
- **S5:** [CLI opener reader](</Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/work/prompts.ts:28>), especially 32-40 and 54-88; [prompt command](</Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/commands/agent/index.ts:308>), especially 319-331; [status placement](</Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/work/status.ts:188>), especially 196-214 and 248-255.
- **S6:** [Package coverage validator](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/scripts/rubric/contexts/work-package.ts:525>), especially 575-584, capability at 617-618 and local reconciliation at 887-907; [coordination placement validator](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/scripts/rubric/contexts/coordination.ts:239>), especially 264-271.
- **S7:** [Acquire local definition](</Users/krisbrown/workspaces/personal/acquire/+/_WORK/personal.regular.acquire-intake/work.md:2>), Scope at 23; [repository rules](</Users/krisbrown/workspaces/personal/acquire/AGENTS.md:29>); [declaration](</Users/krisbrown/workspaces/personal/acquire/.ki.toml:16>), capability declarations at 89-91; [exact registry binding](</Users/krisbrown/.local/state/ki/registry.toml:23>), Personal Principal at 171-173; [Personal coverage](</Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal/work.md:4>).
- **S8:** Principal Git snapshot `7a2e094cad1dde1d270e2542afdb8c472b81f927`, `+/_WORK/ki.ways-of-working/messages.md`: PKG-HOME line 4, PKG-POINTER line 5, TEND-PATTERN line 10, COORD-ANY-PACKAGE line 13. Local pre-design HEAD `da173e1b` has the first three and lacks the duplicate proposal. The direct owner entry at [28 October 15:05 GMT](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md:1061>) is sufficient authority for this design and interim exception.
- **S9:** Principal Git `cece8e9f:+/_WORK/ki.ways-of-working/messages.md:7` is HNR's source-backed METHOD steer. It asks for principal default, deliberate member exceptions and territory discovery, and explicitly distinguishes binding metadata from live cwd. Sender sample counts are not an independently verified current inventory.
- **S10:** Isolated candidate `996bcf64666754975f1691d8ef50678dce9a0dd8`, branch `run/wow-mod011-approved-candidate-mpg8sgz6`, retained worktree `/Users/krisbrown/.local/state/ki/worktrees/wow-mod011-approved-candidate-mpg8sgz6`. [Typed-reader plan](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/work-id-shape-plan.md:38>) distinguishes approved direction from proposed spellings/defaults. The candidate already adds principal-default homes and assigned-package cascade, but still bars regular coordination.

## Corrections to the brief

**Published provenance correction (Codex E3, independently verified).** Brief F3 conflates two origin snapshots. REGULAR-WORK-ROLE is present at local Acquire `messages.md:4` and prior tip `38c744d480f8f882a6a3cb78e688fdbd3b0fe688`; it is absent from fetched origin snapshot `6083f4e2a745637c1fc3cede633eab4bcf99e9a3`, whose message file has three lines. Exact substring predicates confirm both facts. Claude accepted F3 too broadly. The original 23 October instruction remains valid historical evidence in the local message and `design/coordination-lessons.md:134-138`; do not claim that it remains in the current published queue, reinsert it, or remove a stale local copy here.

**Home correction retained (both reviews).** Acquire's local Scope lacks its declaration; fetched `6083f4e2` already has a Home line at `work.md:25`. The real home is registry-resolved Acquire, with Personal Principal separately declared as Capital. The published source is not defective merely because this host is behind. No Acquire checkout was pulled or changed.

**Reader gap is larger than a filter (Codex E8-E10).** CLI status rejects parent/covers on non-territory work and main SoP, then silently drops invalid definitions. Acquire's regular package has a legitimate parent. Removing `level !== regular` from prompts alone would therefore still omit it. Package validation also excludes `<territory>.regular` from coverage and reconciles only locally found packages. The rubric prose mentions member-home declarations, but the actual validator does not enforce them. Capability checking currently follows territory/project levels, while Acquire declares delegation/package capability without `ki-coordination`. These are concrete later implementation surfaces, not reasons to block the interim exception.

**Lifecycle boundary (settling Claude/Codex).** A bounded episode needs an end condition, but neither ending a backlog nor leaving the coordinating role automatically puts a package On hold. S1/S2 require supervisor agreement and drain for hold, and preserve per-package marks. Claude's automatic fallback to On hold, more expected is narrowed accordingly. Continuous coordination may be explicitly selected when justified; it is never mandatory because work is regular or packaged.

**Relay correction (settling both reviews).** Claude proposes date/tag/sender deduplication and a pushed destination before removal. Date/tag/sender can repeat and is not a proven unique origin. Codex correctly requires stable origin identity and recognises a second transport stage even through SoP. Durable availability to the receiving host must precede clearing a relay source; a local commit alone may not provide it. This design grants no push or transport implementation. Direct delivery also needs reconciliation and receipt discipline; it does not eliminate cross-host conflicts.

## Model

### Role, type, package and lifetime

Use four separate concepts. Level/form describes what the work is. The package is its continuing state and authority home. Coordination is an explicitly opened session role acting on that work. Repository capability supplies the method/runtime support, not an active-session assignment. Do not encode a new field, reinterpret `worker`, infer a coordinator from id or package existence, or require a permanent session.

A coordinating opener names the exact valid package, its actual repository and scope, and cites the owner's opening authority. For a bounded episode it names the end condition. Its session dispatches substantive units through detached runs, stays responsive and uses coordinator report/banner rules. A conversational session remains available for bounded direct work, especially individual captures. Merely listing a possible opener does not open a coordinator, create a package, start a heartbeat, receive work or release a hold. Generalised prompts should advertise eligible packages rather than claim to inventory active coordinating sessions.

SoP retains its territory scope, Capital home, parent/covers assignments and authority limits. It coordinates packages, including regular work, and may act only where stewardship is explicitly assigned and acknowledged under the existing contract. Eligibility on another package is not assignment to SoP. No new steward field is selected; use existing committed assignment/Scope words until that separate question is settled. Each package keeps its own holder, state, mark, messages and decisions.

For Acquire, the finite intake backlog is a suitable episode inside `personal.regular.acquire-intake`. Use its real member home and current interim authority. At the endpoint receive or hand back outstanding reports, messages, queries and runs, then explicitly end or continue the episode. Ongoing regular work survives. Provider actions, capture bytes, historical runs and source retirement remain governed by their existing owners. The backlog figures remain sender context.

### Homes and discovery

Principal is the default. A member home is a deliberate owner-approved exception declared in the real package's Scope and discoverable from the principal. Preserve Acquire's selected exception without moving it. SoP stays Capital-homed under territorial governance. Current Project homes remain where they are; the proposed general non-SoP exception policy would permit a Project member exception only after an explicit per-package owner decision and aligned reader/contract support. No such Project exception or relocation is granted here.

First representation: parent `covers` names the work; a plain home reference in the parent package's existing Scope names the exact repository identity, work id and authoritative queue. This is ordinary prose in an existing file, not a second `+/_WORK/` folder, new registry schema, binding, machine path convention or shadow state. The root is resolved through the governed territory inventory and exact local registry identity. A portable reference names repository identity rather than a hardcoded host checkout. Readers must support the approved representation before claiming machine discoverability; a prose reference alone does not magically make today's CLI resolve it.

Current evidence supports regular/ad hoc exceptions directly. Broadening the exception policy to Project work is a prospective owner choice within PACKAGE-HOME, not a reinterpretation of today's absolute Project-Capital rule. If the owner chooses the narrower existing regular/ad hoc allowance, later wording must preserve that boundary explicitly. This distinction does not affect coordination eligibility.

### Pointer and message semantics

Reject a two-file pseudo-package under `+/_WORK/`: it fails the five-core-file contract and resume validation. Supplying three dummy files instead is worse because readers see two valid states, marks and queues for one work. Symlinks, recursive pointer chains and host-specific aliases are not an escape from the physical-package contract. A locator outside that namespace is not picked up as work, counted as another package, or granted a heartbeat, state or mark.

Recommend direct authorised delivery to the one real `messages.md`. When the sender lacks authority or access, retain the request and route the limitation through the existing principal SoP queue under its actual routing authority. That is a request to SoP, not a second work-owned inbox or an automatic ferry. The owner proposal that senders never write across repositories is therefore not delivered by the recommended locator; centralising all writes requires a separate explicit relay design and actual receiving authority. A pointer alone does not remove cross-repository writes or Git conflicts.

| Failure case | Required boundary if any relay is later chosen |
| --- | --- |
| Duplicate/retry | Stable original source reference and receiver receipt; date/tag/sender alone is insufficient. |
| Crash/loss | Make destination durably available before removing source; keep source on uncertain delivery. |
| Loop | Resolve one real home; reject self/cyclic routes and preserve origin through forwarding. |
| Two hosts | Reconcile latest tips, detect duplicate receipts, preserve peer lines and stop on unresolved conflict. |
| Stale/missing home | Retain source, expose precise unavailable/ambiguous identity, and ask its owner; never guess. |
| Move mid-delivery | Owner-approved move, explicit recovery mapping and receipt checks; no two active homes. |
| Meaning/priority | Preserve sender, instruction and IMPORTANT priority; receipt is disposition, not completion. |

These are acceptance requirements for a possible later design, not a new live transport schema, implemented deduplication or an exactly-once promise. Publication/access authority must be established separately. A relay route needs an origin key that survives retries and host changes; this report deliberately does not invent that key's stored encoding.

### Tending

The package's acknowledged steward owns its state, open queries/findings, message disposition and tidy. The parent SoP owns visibility: register every assigned package, including regular/ad hoc and member homes, check omissions and stale/unreachable homes at opening, approved move, bootstrap and ordinary stewardship, and surface the unresolved owner. Preserve existing assignment/handover evidence, `parent`/`covers`, receiver-owned findings and route receipts. Silence, a missing binding or an unread queue does not confer stewardship.

Discovery and assignment are distinct. A bounded reconciliation against packages in declared, registry-resolved territory members can expose a missing registration; it must not adopt the discovered work or infer authority. Home resolution follows explicit references. Do not put an estate scan or a new service into the per-message hook. Extending `covers` to the regular umbrella requires the actual S6 validator change, not only adding prose. Keep a package without active coordination well tended without a permanent coordinator or scheduler. Findings go to its real messages queue; the receiving steward homes and settles them under the existing contract.

## Before/after change matrix

This is the proposed target, not current live behaviour. S-keys identify exact source evidence above; the implementation paths follow the table.

| Surface | Before | Proposed after |
| --- | --- | --- |
| Levels/forms, S1/S2 | Coordination limited to territory/Project | Same levels; any valid package eligible for an explicit role |
| SoP, S2 | Territory coordination/assigned cascade | Specialised package coordination; Capital authority and assignments retained |
| Regular lifecycle, S1 | Self-coordinating; no coordinator | See †. |
| Capture, S7 | Conversational, receipt-first | Same capture default; selected backlog coordination does not widen capture powers |
| Role selection, S2/S3 | `level` determines whether it coordinates | See ‡. |
| Names, S10 | `ki`, `ki.ways-of-working`, `personal.regular.acquire-intake` | See §. |
| Bootstrap, S2 | Stops on regular or opener mismatch | Resolve one exact home; allow regular opener; still stop on ambiguity/mismatch |
| Capability, S6/S7 | Level-gated check; Acquire lacks coordination declaration | See ¶. |
| Hook text, S4 | Generated territory/project restriction | Generated conditional reminder for any explicitly coordinating package |
| Hook executable, S4 | METHOD-NUDGE excludes regular | See ‖. |
| Output style, S2/S4 | Territory/project applicability only | See ††. |
| Report naming, S2 | Project or SoP coordinating headings | Regular coordinator uses real work label/page, not a fabricated Project |
| Package home, S3/S10 | Project Capital required; regular member permitted | See ‡‡. |
| Pointer, S3/S8 | Five files required; no pointer-only shape | See §§. |
| CLI prompts, S5 | Omits regular; one-root/Capital assumptions | See ¶¶. |
| CLI status, S5 | Valid parent rejected; invalid definitions omitted | See ‖‖. |
| Coverage/tending, S6 | Regular umbrella excluded; local-only reconciliation | See †††. |
| Readers/Observatory | Current level/state and report contracts | See ‡‡‡. |

† Regular lifecycle, S1: Conversational default; optional episode or explicitly continued coordination

‡ Role selection, S2/S3: Explicit opener/owner authority determines session role; no new stored field

§ Names, S10: Keep live ids; typed direction and proposed defaults remain distinct

¶ Capability, S6/S7: Check at explicit coordination entry, preserve specific interim override

‖ Hook executable, S4: Local advisory for eligible package with method_read; no role inference/estate scan

†† Output style, S2/S4: Coordinating role applicability; ordinary sessions and runs keep their forms

‡‡ Package home, S3/S10: Principal default; explicit member exception, actual move separately authorised

§§ Pointer, S3/S8: One package; prose locator outside package namespace; no second state/queue

¶¶ CLI prompts, S5: Offer eligible regular/member openers with actual home, without opening them

‖‖ CLI status, S5: Compatible placement, visible unavailable homes, one entry per real package

††† Coverage/tending, S6: Assigned regular/member work visible; gaps surfaced without taking ownership

‡‡‡ Readers/Observatory: Preserve seven states; resolve one home; compatible typed readers before migration

Typed identity detail: approval covers territory/type/name, not a claim that every proposed spelling is live. Current `level` values remain `territory`, `project`, `regular`. `sop` is the specialised typed naming direction, not a fourth parser level. Existing planning examples `ki.sop.main`, `ki.prj.ways-of-working`, `ki.regular.main` and `hnr.sop.<name>` include proposed `prj`/`main` choices and compatibility work. Do not rename `ki.ways-of-working` or Acquire as this design's demonstration, parse theme into ids, or assume the owner word `project` in this proposal silently settles the `prj` token.

Proposed wording boundaries for later exact review:

- Eligibility: Any valid work package may have a coordinating session explicitly opened by its owner. Package existence, level/type and home do not by themselves select that role.
- SoP: State of play is specialised coordinating work across explicitly assigned packages, with territory authority and per-package state preserved.
- Lifetime: Coordination may serve a finite episode or continue by explicit choice. Ending an episode neither closes the work nor changes a hold or mark without its existing agreement/move rule.
- Homes: Principal is default; deliberate owner-approved member exceptions are declared in Scope and made discoverable. SoP remains Capital-homed. Actual exceptions/moves require their own authority.
- Forms: While coordinating, apply the responsive-coordinator contract and coordinator forms. Otherwise apply conversational reply forms; capture remains receipt-first. A run follows its own brief.
- Regular report heading: where no Project exists, link the real work label to its authoritative work file, optionally preceded by its real theme. Keep the existing coordination thread line for all non-SoP coordinating sessions and the State of play line for SoP. Do not invent a Project note merely to fill a heading.

These are reviewable policy sentences, not an applied patch or a new schema. Later wording must also update the package standard's native-session Authority sentence at S3:371 and the canonical cascade/roles so that another paragraph does not reintroduce the exclusion.

## Agreement and difference

Both reviewers independently formed their own view and rankings before reflections. They used different installed runtimes: default Codex (GPT-6.1 Sol) and default Claude (Claude Opus 5.5). Neither read the other review, governing decisions/queries/run reports or this synthesis. Both marked all eight reflections Agree with additions. Agreement is not the reason to adopt: the table records how source evidence resolves qualifications.

| Point | Codex / Claude | Evidence-based settlement |
| --- | --- | --- |
| 1 - eligibility | Agree / Agree + logged opening | Optional explicit role; cite owner authority, no new level/role field (S1-S3). |
| 2 - SoP | Agree / Agree | Preserve assignment and per-package authority; remove level-only gates (S2/S3). |
| 3 - backlog | Agree + lifecycle guard / Agree + local authority | Interim valid now; no automatic hold/finish/mark change (S1/S2/S7/S8). |
| 4 - homes | Agree / Agree + enforcement | Principal default and declared exceptions; current published Acquire home already declared. |
| 5 - pointer | Agree, mechanism medium / Agree, mechanism medium | See †. |
| 6 - relay | Agree, stable origin / Agree, tag/date/sender | See ‡. |
| 7 - tending | Agree + umbrella/capability / Agree + nudges | See §. |
| 8 - rollout | Agree / Agree | Reconcile overlapping candidate and compatible readers; pilot and owner gates remain. |
| F3 provenance | Corrects fetched snapshot / accepts broad claim | See ¶. |
| Coverage | Adds concrete reader rejects / identifies omission | See ‖. |

† 5 - pointer: Plain locator plus one package; reader mechanics remain a separately approved design detail.

‡ 6 - relay: Prefer direct delivery; uniqueness and durable receipt require more than tag/date/sender.

§ 7 - tending: Fix real validators/readers, keep hook local and advisory, no new steward field.

¶ F3 provenance: Exact source predicates favour Codex: local/prior message, absent at fetched tip.

‖ Coverage: Both matter: register omission and technical invisibility are separate failures (S5-S7).

Medium-confidence pointer/home mechanics and tending costs received genuinely blind recommendations in both stage-one reviews. The merged choices retain their preferred order and make the source-supported simplification explicit. No destructive/publication choice is requested; rejected shadow packages or relocation alternatives are described only to delimit the recommendation. No third review was launched.

## Rollout plan

Only the owner/coordinator records decisions and queue receipt. This run changes no governing file, canonical model, roadmap, package identity or receiving queue. It modifies neither retained MOD011 branch nor another repository. Later delivery surfaces below are receiving-owner needs, not instructions to write across repositories or new receiver roadmap items.

1. Decide the four policy choices. Keep Acquire's already-approved exception separate and active. Home its authority/readback through the receiving steward's normal process when appropriate; do not demand new global approval before it coordinates.
2. Establish the existing cross-machine source confirmation and re-ground against current destination HEAD, index, source hashes and concurrent writers. Retained MOD011 candidate `996bcf64` already contains default homes and assigned-package wording but retains regular exclusion. Either integrate that reviewed unit under its existing authority before the new amendment, or prepare a newly scoped combined candidate under fresh explicit authority. This run selects neither integration nor acceptance. Never replay `mod011-wording.md` or an older whole-tree patch blindly.
3. Through Enactment and the existing owning work, align Work Process/GDR9 and the harness contract. Preserve the three-file MOD011 packet and its record lifecycle; the new proposal does not silently self-accept it or expand its authority. The coordinator can use the existing record only if its approved scope genuinely covers the new change; otherwise it owns capturing the needed additional work after approval.
4. Receiving Harness owner edits canonical semantic/generator sources once and the separate executable gates, then regenerates and verifies equality. Tools owner updates actual identity/placement/home/prompt readers and their contracts. No consumer relies on a prose-only home locator or new typed writer before its reader is ready.
5. Personal and Acquire stewards reconcile their current published source, declarations, local scope/authority wording and coverage without rewriting capture/provider boundaries. Existing interim exception is not paused while they plan this. HNR keeps its own acceptance, assignments, holds, marks and actual inventory; no outbound message or HNR write occurs here.
6. Pilot optional regular coordination and home discovery in an owner-approved bounded case without live renames. Acquire's existing exception is useful evidence, not general acceptance of tooling. Keep the separate held Baseline rollout naming pilot dependent on its own steward, compatible readers, source safety and explicit move authority. A held pilot remains held. Roll out further only after pilot lessons and receiving-owner approval.

### Exact proposed implementation surfaces and ownership

**Principal:** `Pillars/Philosophy/Model/Processes/Work Process/Work Process.md` (levels/forms, regular explanation, cascade/roles, homes and words); `Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md` (consolidated decision at 28-40). Coordinate with the retained `Streams/Roadmap/KI-PRINCIPAL-MOD-011-amend-work-model-assigned-package-cascade.md` packet; no record is changed by this design. The Work Process fallback text/visual can otherwise keep stating the exclusion: `Pillars/Philosophy/Model/Processes/Work Process/work-model.svg` must be assessed by its source owner, not patched as an isolated visual. Existing working sources are `design/work-model.architecture.json` and `design/work-model.svg`; verify their intended generator/ownership before selecting a later visual edit.

**Harness policy:** `skills/change-management/ki-coordination/SKILL.md` and `references/standards-coordination.md` under that skill, especially scope/glossary, levels/forms, session kinds, report heading/thread line, openers/bootstrap, messages, assigned packages and marked generated-source blocks. `skills/governance/ki-work-package/SKILL.md` and `references/standards-work-package.md` under that skill, especially location/Scope, coverage, single home, native-session Authority and capability semantics. `skills/keystone/ki-bootstrap/references/standards-bootstrap.md:112` currently sends every opener to the Capital; revise for a deliberate member home while retaining territory discovery and ordinary machine-readiness requirements. The interim exception is explicitly distinguished from those later defaults.

**Harness implemented validators:** `skills/change-management/ki-coordination/scripts/rubric/items/threads.ts` and `scripts/rubric/contexts/coordination.ts`; `skills/governance/ki-work-package/scripts/rubric/items/records.ts` and `scripts/rubric/contexts/work-package.ts`. Fix actual regular-home declaration, parent/covers, umbrella and capability checks rather than only changing rubric descriptions. Preserve closed five-file validation and machine-local bindings. Regenerate each affected `references/rubric.md` publication from its source; no hand-divergent generated rubric.

**Harness generation:** semantic marked blocks in the coordination standard feed `skills/change-management/ki-coordination/scripts/generate/index.ts`; `ki dev skill generate ki-coordination --write` is the existing rendering entry point. Its targets are `hooks/coordinator-reminder.sh` line/pointer, `output-styles/ki-coordinator.md`, `skills/governance/ki-delegation/assets/run-prompt.md` Report paragraph and `rules-none.md`, `rules-push.md`, `rules-prune.md`, `rules-release.md` report paragraphs in that assets directory. Regeneration may leave unaffected target bytes identical. Generalise scope/heading wording at the source only where needed; retain the report shape and authority tiers. Separately edit authored hook `method_warning` filtering at `hooks/coordinator-reminder.sh:90-94`; regeneration does not own that function. Preserve background-run suppression and repository declaration gating. No binding or runtime settings changes are authorised here.

**Tools CLI:** `src/core/work/prompts.ts` (kinds, offering versus activation, level filter, scope/id parsing and actual home); `src/core/work/status.ts` (placement, valid parent/covers, per-root reading and visible failures); `src/core/work/registry.ts` (declared identity/Capital resolution, not a guessed package-home path); `src/commands/agent/index.ts` prompts action (registered member exception resolution, labels/launch directory); `src/commands/work/index.ts` status action (single authoritative entry and receiver scope). `src/core/agent/thread.ts` owns report/package home resolution, `src/core/agent/identities.ts` owns run workHome identity: check exact repository-plus-id handoff through these boundaries, not an added parallel locator store. Typed migration overlaps the existing plan's `src/core/agent/context.ts`, `runs.ts`, `controls.ts`, `control-store.ts` and `src/commands/agent/control.ts`; that is a dependency check at the existing control identity boundary, not a request to redesign unrelated control machinery. Runtime binding schemas remain runtime-owned; do not invent or mutate them through documentation.

**Observatory reader:** in `apps-observatory.local`, `packages/contracts/src/work.ts`, `packages/evidence/src/work.ts`, `packages/evidence/src/work-package.ts` and `packages/instruments/src/work.ts`. Source inspection shows `ki/work-status/v1`, levels `territory/regular/project`, per-repository collection, five-file fallback and real-home report lookup. Preserve those levels/states and one identity/home; assess whether already-correct aggregation needs changes after CLI compatibility, rather than requiring an unnecessary schema rewrite. No deployment or separate authoritative status is part of this work.

**Receiver-local rules:** Acquire `AGENTS.md:29-31`, `.ki.toml` coordination capability readiness and selected `+/_WORK/personal.regular.acquire-intake/work.md` description/Scope/exception provenance; Personal `+/_WORK/personal/work.md` coverage and prose home reference. The principal reference is in an existing SoP Scope, not a new pointer package; its exact portable reader interpretation is approved/piloted before automated reliance. Current Acquire origin already declares its home and has consumed the old queue line: preserve that newer source. The receiving steward owns any write and receipt. HNR's packages, holds and identities are not implementation surfaces of this run.

### Later focused regression checks

Use existing fixtures for these changed boundaries; this design ran no product tests or builds and does not waive later repository-required checks.

- Explicit owner-opened regular coordination succeeds; conversational capture remains direct; a capability declaration, package creation or id alone starts no coordinator. Current Acquire exception is honoured despite general exclusion; other packages cannot inherit it.
- Ordinary Project/SoP behaviour, background-run suppression, report headings/forms/thread lines and seven states remain intact. Ending a bounded episode does not reset marks, auto-hold/finish, abandon runs or release another package.
- Status/prompt definitions retain valid regular parent and main covers; regular umbrella and children are discoverable. Both principal and member contexts resolve the same real home. Absent/ambiguous/out-of-territory roots fail visibly and retain messages, without guessed paths or duplicate entries.
- Declared member exception and principal reference agree on repository identity/work id; `+/_WORK/` still rejects two-file/shadow/symlink pointer shapes. Opening/offering coordination is distinct from existing typed-id compatibility; old and new ids cannot double-count a work.
- If a relay is separately approved, interruption before/after destination receipt, duplicate same-tag messages, repeated forwarding, peer-host writes, stale home and move-in-flight retain or recognise the origin without loss or loops. Do not claim those tests passed for an unbuilt mechanism.
- Extend `skills/change-management/ki-coordination/scripts/banner.test.ts` generated-surface guards and affected `scripts/rubric/contexts/coordination.test.ts`, `items/threads.test.ts`, `skills/governance/ki-work-package/scripts/rubric/contexts/work-package.test.ts`. Reuse Tools `src/tests/cli/agent-prompts.test.ts`, `src/tests/cli/work/status.test.ts`, `src/tests/cli/agent-threads.test.ts` and existing targeted home/control identity fixtures where actual changes justify them. Observatory contracts/evidence/instrument work fixtures run only if their surface changes.

## Decisions

### COORD-ELIGIBILITY - Make coordination a selectable session role

**Context:** S1-S3 bar regular coordinators, while the owner explicitly proposes eligibility for any package. Both blind reviews prefer optional explicit opening. A finite backlog is a reason to choose the role, not proof of a new Project or permanent coordinator.

**Query:** Adopt optional coordination for every valid work package, retaining type, conversational work and per-package authority?

**Options:**

a) (recommended, confidence high - directly fits the owner proposal and existing work/session distinction) Any valid package may coordinate under an explicit owner opener/authority and scope. Bounded episodes state an end condition; continuity is an explicit choice, never inferred. SoP specialises the role across assigned packages.

b) Keep territory/Project-only coordination and grant individual regular exceptions. Acquire's existing exception continues under either choice.

### PACKAGE-HOME - Principal default with deliberate member exceptions

**Context:** S3 currently permits regular member homes and requires Project Capital homes. S9 and the retained candidate favour principal default; S7/S8 establish Acquire's deliberate member need. Specific Acquire authority is settled. Broader home policy is distinct from eligibility.

**Query:** Use principal-default homes with deliberately owner-approved non-SoP member exceptions, explicitly declared and discoverable, without moving any package now?

**Options:**

a) (recommended, confidence high - reconciles the two evidenced needs while requiring explicit authority for every exception) Principal default; preserve Acquire. Allow owner-approved non-SoP member exceptions, with Scope declaration and principal discovery. Any future Project exception needs explicit per-package approval and aligned contract/readers; no Project move or exception is inferred here. SoP stays Capital-homed.

b) Principal default with exceptions limited to regular/ad hoc work, retaining today's absolute Project-Capital requirement. This is a narrower policy if the owner wants Project exceptions excluded even from the general permission model.

### PACKAGE-POINTER - Choose the representation before adding transport

**Context:** S3 disallows the proposed two-file pointer package; a shadow five-file package would compete for authority. Both blind stage-one reviews rank a locator first at medium confidence. The exact read path needs compatible readers. A locator does not fulfil a strict ban on sender cross-repository writes.

**Query:** Start with a plain principal home reference and one real inbox, or separately design principal-only relay access?

**Options:**

a) (recommended, confidence medium - uses existing parent coverage/Scope and keeps one authoritative package/queue) Parent `covers` plus a prose home reference in the existing parent Scope, outside a second package namespace; direct authorised delivery to the real inbox. Settle the portable repository identity/work id interpretation with the CLI owner before automated reliance. Lack of access is surfaced/routed through SoP, never bypassed.

b) Retain one real package but separately design a principal relay through SoP if principal-only sender writes are essential. Specify stable-origin receipt, durable destination availability, retries, conflict and loop behaviour before implementation; do not create a pointer package under the current contract.

### PACKAGE-TENDING - Name responsibility independently of active coordination

**Context:** Personal's register missed Acquire; S5/S6 additionally hide regular/member/umbrella packages. Tending, discoverability and active coordinator role are separate. No new steward field or scheduler is justified.

**Query:** Have the acknowledged package steward tend the work and its parent SoP explicitly check coverage/home/routing gaps at normal lifecycle boundaries?

**Options:**

a) (recommended, confidence high - assigns existing responsibilities and addresses demonstrated omissions without inventing a role field) Steward owns package disposition/tidy; parent SoP maintains discovery and reconciles registered member/regular coverage at opening, approved move, bootstrap and ordinary tending. Surface stale/unreachable homes and ownership gaps; preserve acknowledgements, holds and execution authority. Extend actual readers/validators and keep the hook local/advisory.

b) Retain today's tending practice and report omissions individually; optional coordination can still proceed, but coverage/readability gaps remain visible limitations until separately corrected.

## Changes after review

- Codex's exact snapshot predicate corrects brief F3; no stale queue receipt is claimed. Claude's broader acceptance loses to immutable-source evidence.
- Both reviews sharpen the explicit role/package distinction; S3:371, capability validation and bootstrap machine guidance are added to implementation surfaces.
- Codex's parent/covers rejection, umbrella restriction and silent omission findings make reader repair a prerequisite to reliable discovery, beyond deleting the regular prompt filter.
- Claude's principal reference suggestion is made concrete as existing parent Scope prose, retaining medium confidence until readers/pilot settle the portable interpretation. No new live schema/file is introduced.
- Claude's automatic On hold fallback is narrowed under the actual supervisor-agreement/drain rules, supported by Codex's lifecycle guard.
- Relay risk is explicit: tag/date/sender is not a unique receipt key; commit-before-removal needs receiving-host durability and leaves duplicate windows. No relay is adopted or promised.
- General non-SoP home exceptions and a narrower regular-only alternative are stated explicitly so existing Project-Capital policy cannot change by ambiguous wording. Neither option authorises a move.
- Exact generator ownership, authored hook filtering, local validation gaps and downstream actual readers are separated; no hand-edit of generated copies or blind replay of MOD011 is proposed.

## Practical limits and recovery

Only the brief, two homed reviews and this report were authored in the repository. The five governing files, queues, canonical content, roadmap, other repositories, runtime bindings and retained MOD011 branch remain untouched by this run. Normal staged-path document hooks ran on each committed artefact; no product builds, broad audits or unchanged test suites were run. These checks establish document delivery, not runtime behaviour or estate health.

Reviews are complete, not pending. Default runtime identities are supported by their launch/runtime evidence and reviewer declarations; no model/runtime installation or native subagent was used. The stage-one recommendations are preserved in the homed reviews. The initial brief commit's trailer was corrected to the actual model; its content is unchanged and recoverable as `12ed2066`. Claude review is recoverable as `f2917073`; Codex review as `9e4ee330`. This report is committed separately. All four artefact paths are named at the top and share the `coord-any-package` prefix.

The complete existing inbox beside the launched prompt was directly read after the review wait and before final verification. Its 13 lines target earlier named runs, not this design. Canonical package ownership, focused verification and no dependency/network fallback cautions were respected; none authorised a schema, code edit, foreign write, mark move or additional review. No relevant in-authority steering remains unhandled. Queue receipt and all decisions remain for the coordinator. This report does not claim adoption, acceptance, release or deployment.
