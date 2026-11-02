# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › away-bridge-blind-review

**🤖 → 👤 Handoff to supervisor · Run report at 01:55 GMT · last mark 01:04 GMT**

---

## Done

- Completed the independent Bridge machine-reader query review under AWAY-2026-10-29; no tracked edits or commits, record creation, adoption, provider calls, remote calls, service calls or live configuration changes.
- Direct reader checks passed: Bridge asks Rig only for its version and retains unavailable state even when the injected runner can supply JSON; Automation asks once for JSON with the shared timeout and uses only matching schedule declarations.
- Current Rig binary passed an isolated declarative `show` check against an invented catalogue with nonexistent provider and program paths; it created no state directory, and its actual JSON passed through the current Automation reader successfully.
- Focused evidence, Bridge contract and Bridge rendering tests passed: 70 tests, zero failures; the independent caller script passed both checks. An initial scratch-only fixture used an invalid schedule field and was rejected; correction to the documented calendar form passed.
- Exact source predicates confirmed the runtime explanation, fixed unavailable source, Automation argument vector and Machine's idea status; source anchors were Observatory `96f999a` and Rig `80ab019` at review time.
- Read the complete runtime inbox before verification and at finalisation. Preserved blind-review independence; queue bookkeeping, staging and other runs' receipt requests are outside this read-only brief and were not acted on. No linked reports, work queries, work decisions or design reviews were opened.
- Read current coordination, delegation and authoring standards. Applied the final inbox freshness message: inspected `07b9333a` and the current changed source; it adds only a delegation source-index contents list, with no authority change. Coordination/work-package standards remain at `6868da5a`. This run did not update package `method_read`; the coordinator owns that receipt.

## In Progress

Nothing running.

Outstanding - no action requested now: evidence is checkout and isolated-fixture evidence only. Installed Rig version, service/deployed parity, real providers, real jobs and another host were not inspected. Existing holds and source ownership remain intact. The coordinator receives this report and retains the owner choice; this run adopts nothing.

## Findings

### BRIDGE-EVIDENCE - A real integration omission, not a missing upstream interface

**Goal:** Establish what current sources prove about the remaining Bridge machine-reader gap and its bounded disposition, as requested on 29 October 2026.

**Scope:** Current Observatory reader, server wiring, contract, rendering and fixtures; Rig implementation and canonical query/state specifications; current Machine idea and convergence record. Excludes earlier recommendations and reviews, live provider state and deployed behaviour.

**As of:** 29 October 2026, 01:55 GMT.

**Recommendation: retain current behaviour and park integration; confidence high.** Reason: the remaining omission is an unadopted consumer capability with unresolved scope, while Rig already supplies JSON and the current reader honestly reports its limited coverage.

1. **Rig has a public machine contract.** [RIG-STATE-033](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/state.md) specifies JSON for `show`; [the implementation](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/30-commands.bash) emits selected tools and resources, including scheduled-job desired state and encoded schedules. [RIG-QUERY-004 and RIG-QUERY-006](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/queries.md) keep catalogue queries declarative and free of provider execution. The isolated current-binary check confirmed this path, rather than relying on old fixture claims.

2. **Bridge does not consume it.** [The live reader](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/machine.ts) observes versions, chezmoi changes and Homebrew services, then unconditionally reports the Rig source unavailable. Its [current explanation](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/machine.ts) says the Bridge reader has not yet been built and identifies Automation's schedule reader. [Server wiring](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/apps/site/src/server.ts) uses this reader for [the machine route](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/apps/site/src/server.ts). The isolated call trace confirmed that Rig installation and Rig-state observation are separate: a present Rig still supplies no state to Bridge. A newer installed Rig cannot alone enable a call that the caller never makes.

3. **Automation coverage is narrower.** [Its reader and projection](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/automation.ts) retain scheduled-job `id`, `desired` and `schedule`; [the accepted identity contract](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/specs/automation.md) joins these to reporter rows by exact ID. The check exercised matched, disabled and unmatched jobs and proved that a declaration without a reporter row is not added. This is schedule-aware freshness for reported jobs, not a full Rig inventory or observed machine-health view. Failure and timeout fallback remain covered by the existing tests.

4. **Obsolete wording remains, but it is not the production explanation.** [MachineSource documentation](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/contracts/src/bridge.ts), [signal documentation](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/contracts/src/bridge.ts), [the contract fixture](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/contracts/src/bridge.fixture.test-support.ts) and [the rendering fixture/assertion](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/instruments/src/bridge.test.ts) still claim Rig has no machine-readable projection. These are bounded wording/fixture debt. They cannot establish that the current production source reason is wrong, and correcting them would not make Bridge read Rig. No delivered-behaviour regression or breached accepted integration requirement was established by this review; the omission itself is real and directly reproducible.

5. **“Rig state” still needs a precise meaning.** `show` supplies declared intent, not observed provider health. Rig also has a [status JSON projection](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/22-observation.bash), whose [caller performs observations](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/22-observation.bash). Selecting status would introduce a different observation boundary; it was not executed here. A proposal must choose declaration coverage versus actual observation, define fields, failure/timeout and exit-status handling, privacy, visible signal destinations and tests, and retain Rig's ownership of its semantics. It must not infer health from declarations or manufacture a new Rig interface merely because Bridge has not used the existing one.

6. **Existing gates are explicit.** [KI-OBSERVA-VIS-038](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/ideas/KI-OBSERVA-VIS-038-machine-instrument.md) is an idea, not active roadmap work; its retained consolidation conditions require [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) and Kris's separate approval. The idea excludes backend-contract changes from consolidation scope. Its tool-storage phase separately requires adoption and the harness-owned declaration contract; that is not released by discovering Rig JSON. [The Observatory work boundary](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.observatory/work.md) places Rig ownership outside this Project. Neither consolidation nor a source-owner change is authorised by this review.

Query raised: BRIDGE-DISPOSITION. This is the review's own tag; the coordinator should reconcile it with the existing masked query rather than create a duplicate.

## Queries

### BRIDGE-DISPOSITION - Keep the integration parked or adopt a bounded proposal

**Context:** Bridge still has no Rig declaration/state reader, although Rig has JSON and Automation consumes its schedule subset. Current runtime wording acknowledges that limit; stale comments and fixtures do not account for the missing caller. There is no demonstrated regression requiring a behaviour repair under this brief. Machine remains an idea with consolidation and source-owner gates, and a declaration view and an observed-health view are materially different features.

**Query:** Should Rig integration stay parked, or should a separately adopted Observatory proposal define the required coverage using Rig's existing public JSON contract?

**Options:**

a) (recommended, confidence high - the absent consumer capability has no adopted scope, and current behaviour reports its limit honestly) retain current behaviour and park integration under the existing Machine/consolidation gates. Treat obsolete comments and fixtures as bounded hygiene, without saying that wording correction closes the reader gap.

b) Separately adopt proposal preparation for a Rig reader using the existing public JSON contract, first choosing declaration coverage versus observed health and confirming the source-owner boundary. Proposal preparation does not authorise implementation, consolidation, provider access or rollout; those gates remain separate.

c) Limit subsequent work to wording/fixture correction and leave the reader omission explicitly unresolved. “Wording only because no behaviour gap remains” is not supported: the caller still omits Rig state, even though no accepted-behaviour defect has been demonstrated.

### 🤖 → 👤 Handoff to supervisor · since 01:55 GMT

🤖 0 running · 👤 1 with you · ⛔ 0 blocked · 📥 0 to accept

- [with you] Bridge integration disposition; no option adopted · Kris via Observatory coordinator · since 01:55 GMT

🧵 ki.prj.observatory
