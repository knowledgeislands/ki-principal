# Scheduled cross-machine Git sync ownership: brief

**Owning work:** [ki.prj.observatory](../work.md) · **Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Date:** 2026-10-29 · **Status:** draft

## Problem

Regular cross-machine Git sync is being handled through bounded Rig-thread passes while HOST-SYNC, a territory dispatcher and a built-in Tools recipe are being shaped. The running Observatory is another proposed execution home. Choosing it because it is already running would leave authority, machine responsibility, exclusion and recovery unresolved. The question is which component should own each responsibility, rather than whether a view can invoke Git.

This is a preparation-only brief under AWAY-2026-10-29 and the explicit away-sync-brief instruction. The window ends at 09:00 GMT/UTC on 29 October, or explicit return sooner. No execution owner, implementation, standards/configuration change, scheduler activation, Git sync, remote call, new record, review launch or rollout is authorised by this brief. Only this brief and its owned window-plan entry are committed locally. Recommendations remain provisional pending two independent reviews, a merged report and Kris's decisions.

## Owner's proposal

The current Observatory queue's OBSERVATORY-SYNC message attributes these words to Kris at 22:55 GMT on 28 October:

> given the fact that the observatory is running, why doesn't the observatory just do it?

It also attributes this placement to Kris:

> I think this is in ki.prj.observatory

These are exact quotations verified against the local queue, not a recovered transcript. The surrounding routed message interprets the question as regular cross-machine Git sync, including fetch, fast-forward, push, ordinary merge only after repository checks and idle-work-package tidy. It asks whether the Bridge should own a scheduled activity in place of or beside the dispatcher and HOST-SYNC. That interpretation is routed context, not additional verbatim owner speech. MGIT-SYNC-JOB separately presents regular sync as a candidate for a coordinated host-based runner once SYNC-RECIPE lands. Neither message chooses the owner. [S1]

## Established facts

- **Observation and authority are already separate.** Observatory's contribution contract requires typed backend ports, scope/plan, applicable confirmation and retained receipts for mutation. Its mechanical-first rule requires usefulness without an LLM or provider MCP. PDR-KI-OBSERVA-001 calls Instruments read-only and Bridge governed command, with observation the default. Bridge capability does not establish a standing unattended sync grant. [S2]
- **The package has narrower current ownership.** Its scope includes Observatory features and CLI consumption, while territory dispatch, Rig, host network and CLI implementation have other owners. OBSERVATORY-SYNC is authority to shape this question, not to rewrite those boundaries. AWAY-2026-10-29 preserves unanswered choices and excludes service/scheduler/configuration changes; this run's explicit no-remote/no-push restriction is narrower still. [S1, S3]
- **HOST-SYNC remains a design request.** Ways of working's queue records proposed primary sync on the hour, secondary sync five minutes later and a still-undecided read-back of secondary updates by the primary. HOST-RESPONSIBILITY asks the Observatory to discover those expectations, and places personal setup in dotfiles rather than territorial Knowledge Islands configuration. None of this proves a deployed schedule. [S1, S4]
- **Seats are not primary/secondary sync policy.** The inspected chezmoi source binds Rig profiles to terra/home and sol/hub, with a hub tip and territory lists. It has no primary/secondary sync responsibility declaration. Shared territory membership is not permission to elect a machine or infer failover. [S5]
- **The dispatcher design is prior work, not an adopted ownership decision.** Terra's stage-3 report proposes a model-free due check, separately bounded child execution and individual reporting identities. It explicitly leaves owner decisions open, including source-design ownership, territory versus host fan-out and observation compatibility. It distinguishes ordinary scheduled Activities from recurring roadmap admission and headless coordination. Its historical live-state observations are dated evidence from another host, not verified present state here. [S6]
- **Native scheduling, executable source and observation differ.** The operational-resources guide puts resource intent/native launchd reconciliation in Rig and wrappers/reporting in chezmoi. It describes the Observatory service label and primary-checkout serving, but no loaded service or host liveness was inspected in this run. Reporting writes per-job latest JSON and terminal history; reporting serialisation protects records, not execution exclusion. [S7]
- **The local Tools implementation is narrower than the proposed pass.** tools-mgit's README and bin/mgit implement fetch, dirty/detached/no-upstream skips, fast-forward integration and ordinary non-force push; divergence is reported, with mergeability inspection, rather than merged. The chain record is awaiting review and explicitly excludes sync redesign. Tools-burndown's SYNC-RECIPE asks for safe ff/publish steps over chain; MGIT-AUTO separately proposes merge/exclusion/JSON improvements. Neither requested capability is assumed delivered or installed on both machines. No mgit command was executed here. [S8, S9]
- **The hand-run pass includes judgement beyond Git.** Terra's sync brief has repository exclusions, live-work checks, bounded conflict handling and idle-package tidy rules, including a 60-minute recent-work boundary. These are that pass's instructions, not generic command semantics or standing permissions for a future daemon. Its until-midnight grant cannot be carried into a new recurring job. [S10]
- **Jobs observation depends on identities and schedules.** The local Automation adapter reads reporter files/history and Rig schedules; the contract uses recognised terminal results and schedule-aware overdue judgements. Existing dispatcher evidence warns about missing starts, never-started jobs and schedule loss when child resources disappear. A healthy parent, successful process exit or reporter lock cannot prove all repositories synced. A parallel jobs-spec documentation run does not itself resolve these behaviour questions. [S6, S11]
- **Headless passes are a different governed execution form.** The current coordination method requires a mechanical trigger, a named package grant, bounded model use only when needed, one pass per work, same-repository serialisation, live-coordinator exclusion and no retries within a firing. Recurring Git execution is not automatically a coordinator pass. Criticality still excludes unattended changes that could disconnect Kris or take a site down; confidential material stays private. [S12, S13]

All observations are local non-secret source evidence as of this preparation. No provider state, credentials, installed configuration, loaded jobs, other-host checkout or remote refs were queried. The source inventory below records the local bytes used; it establishes neither live deployment nor cross-host parity.

## Responsibility boundaries and alternatives

**Observation:** Observatory can show expected versus observed per-host runs and repository outcomes without owning execution. **Authority:** repository-specific publication/conflict/tidy grants need their own source, scope, expiry and exclusions. **Execution:** a deterministic Git executor and a scheduler are separate responsibilities. **Locking:** local scheduling, local repository writes and two-host coordination require distinct protection. **Failure reporting:** a job outcome must preserve repository failures and missing/unconfirmed results. **Host responsibility:** dotfile-owned setup must be discoverable without turning a host view into an authority registry. **Recovery:** resumption must reconcile partial effects and surviving processes rather than infer success or rerun blindly.

- **A - Observatory observes; existing per-job Rig/chezmoi execution remains.** Smallest provisional baseline for comparison. Retains current scheduler separation but does not settle shared host policy or replace hand-run judgement.
- **B - Rig/chezmoi dispatcher executes; Observatory consumes evidence.** Reuses the existing dispatcher design, subject to its unresolved ownership and child-schedule questions. Sync is only a candidate child, with separate permissions and repository guards.
- **C - Observatory Bridge schedules and executes.** Closest to the owner's question. Requires an explicit standing capability and host binding, bounded subprocesses, execution locks, truthful receipts and recovery independent of browser visits. Being a running service supplies none of those contracts by itself.
- **D - Observatory requests an external deterministic runner.** Bridge supplies a governed request/receipt surface while Rig/chezmoi owns timing and the runner owns Git mechanics. Avoids duplicating Git policy, but adds an interface whose request authority, idempotency and failure semantics must be justified.

These alternatives do not choose a territorial versus host-wide dispatcher. Stage 2 should compare both topology choices where relevant, including whether sync should proceed if the Observatory is stopped. A provisional preference is to keep observation available and mutation separately governed while evaluating all four alternatives; this is a design principle, not selection of an execution owner.

## Reflection

Each numbered point is one provisional claim for Agree, Differ or Add, with evidence for every Differ.

1. **The running service is insufficient ownership evidence.** Observation, authority and execution must remain separately named under every alternative; extending Bridge cannot import Rig-thread grants. Test against S1-S3 and S10.
2. **Routine sync should be mechanical first.** Due checks, safe Git steps and structured outcomes should run without a model; judgement about conflicts, permissions or tidy eligibility must stop or enter a separately authorised bounded workflow. Preserve Observatory's provider-independent operation. Test against S2, S8-S10 and S12.
3. **Host offsets are collision reduction, not exclusion.** Primary-at-hour and secondary-five-minutes-later cannot prevent overlap after sleep, slow runs, manual starts or clock differences. Explicit host binding and an execution/claim policy are necessary; seats must not be reinterpreted as that policy. Test against S4-S6.
4. **Execution locks and reporting locks have different jobs.** The design must state per-occurrence overlap protection, shared-checkout Git write windows and cross-host behaviour separately, with identifiable ownership and safe stale-claim disposition. A launchd label or reporter lock cannot cover every layer. Test against S6-S7 and S13.
5. **Publication needs repository-specific eligibility.** A future runner must check grants, unpublished ancestors and actual changed paths, confidential/deployment boundaries, live work and upstream state before push; a generic push command is not that authority check. Divergence handling and ordinary merges require a separately reviewed boundary. Test against S8-S10 and S13.
6. **Package tidy should remain a separate candidate capability.** It needs explicit owned paths, idle/live-work evidence and the package method's preservation rules; no fetch/ff/publish recipe should silently acquire deletion or acceptance powers. Test against S3, S10 and S12-S13.
7. **Failures must be visible below the parent job.** Preserve job/run/host identity and per-repository success, skip, blocked and failed reasons; distinguish no evidence, unfinished, partial and terminal results. A successful tick or process exit must not flatten a failed repository into healthy. Test against S6-S7 and S11.
8. **Recovery needs partial-effect accounting.** After timeout, crash, lost report, host sleep or lost connectivity, reobserve repositories and reconcile claims before retrying. No immediate retry loop, implicit failover, stale-lock removal, stash, reset or force update follows from a schedule. Test against S6-S7, S10 and S12-S13.
9. **Criticality and source ownership remain gates.** A later machine rollout must use its own reviewed authority and restore requirements; no connection-critical unattended change, service restart, credentials change or public release is justified by this brief. Ways of working owns shared method changes, Tools owns the recipe, and repository owners retain acceptance. Test against S3, S6 and S12-S13.
10. **A later pilot should demonstrate preservation before replacement.** After reviews and owner decisions, compare due predictions without mutation, then separately authorise one bounded execution owner. Test overlap/manual starts, dirty/live repositories, divergence, expired grants, missing hosts, skipped slots, reporting failure and safe retirement/restoration of the old binding. No pilot or record allocation occurs at this stage. Test against S6 and S12-S13.

## Independent review briefs

### Review A - Authority and ownership

Use a model or runtime different from Review B. Form your own view before reading any other review; read only and create no records or runtime changes. Starting from the review template, fact-check this brief, mark every claim 1-10 Agree, Differ or Add and cite evidence for each Differ. Compare A-D without treating existing service placement or queue routing as an owner decision. Identify exactly which choices belong to Kris, Ways of working, Rig/chezmoi, Tools and repository owners. Examine publication grants, mechanical versus judgement work, ordinary scheduled Activities versus recurring admission/headless passes, and whether tidy belongs in scope.

Required evidence: S1-S4, S6's complete brief and merged report, S8-S10, S12-S13, the design-loop standard and review template. Read the complete current Observatory queue and AWAY entry, and verify that source snapshots still match before relying on them. Do not read Review B until your own view and point-by-point review are complete.

### Review B - Reliability and observation

Use a model or runtime different from Review A. Form your own view before reading any other review; read only, make no remote calls and operate no service or scheduler. Starting from the review template, fact-check this brief and mark every claim 1-10 Agree, Differ or Add with evidence for each Differ. Stress-test A-D for two-host overlap, local write contention, manual starts, sleep/wake, partial Git effects, claim fencing, stale-lock recovery, bounded execution, missing/late reports and restart independence. Specify what would prove expected host responsibility and honest per-repository outcomes without choosing a schema or execution owner.

Required evidence: S1-S2, S4-S8, S10-S13, the dispatcher report's exclusion/recovery/Jobs discussion, tools-mgit bin/mgit sync paths, Automation adapter/contract and tests, and the design-loop review template. Inspect source only; seats and historical source schedules are not live-state proof. Do not read Review A until your own view and point-by-point review are complete.

The coordinator may commission these two reviews later under a new bounded instruction; none is launched here. Each eventual review belongs beside this brief with the observatory-sync slug. A merged report must settle disputes on source evidence, leave unresolved choices to Kris and quote any later grant before rollout.

## Sources

### S1

- [messages.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.observatory/messages.md>) - local SHA-256 `6ab369f349512695049ed686fb5a07a6150d292011b49b9c0a70eff87b05ec0d`.

### S2

- [AGENTS.md](</Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/AGENTS.md>) - local SHA-256 `94544f33c77faae22dc0805c09243d03288a9e1a19e7df7408e0cacdddf33487`.
- [PDR-KI-OBSERVA-001-observatory-beacon-and-bridge.md](</Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/decisions/PDR-KI-OBSERVA-001-observatory-beacon-and-bridge.md>) - local SHA-256 `449d78307f5e43989846bc5612889e1afee4beb173e1ddf2fac5bcf6690bf318`.

### S3

- [work.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.observatory/work.md>) - local SHA-256 `75ebe0e72c9a7936e06b7f686932a4ee3206effd037514af7f4d35e2f4e485f2`.
- [decisions.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.observatory/decisions.md>) - local SHA-256 `baf2f345c6ffeda5d43b4e11eb37195574f00c7d3488353fb0e6c832e663de8c`.

### S4

- [messages.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/messages.md>) - local SHA-256 `6f5d99a8a55fa2a515df98004c13eabec4da9d902a4985a24f4d643cb160360e`.

### S5

- [seats.yaml](</Users/krisbrown/.local/share/chezmoi/.chezmoidata/seats.yaml>) - local SHA-256 `431a7f9f57ef3c3b3d2cc8fee32c2b855901476a316e642ddd3ee5b0210a25d3`.

### S6

- [territory-dispatcher-brief.md](</Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-terra/design/territory-dispatcher-brief.md>) - local SHA-256 `409321a710c8da002db3a35cb8b08ffad95c30f7af7a4771108a4c4976b6b4b6`.
- [territory-dispatcher-report.md](</Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-terra/design/territory-dispatcher-report.md>) - local SHA-256 `ae444f595811ad0e2962f1e10a1e958f445ea7d43c711ccd05dcba0da90ef431`.

### S7

- [operational-resources.md](</Users/krisbrown/.local/share/chezmoi/docs/guides/agents/operational-resources.md>) - local SHA-256 `999606a428681dce279883221222019a0e2948f44e41adcbbca43706d5868502`.

### S8

- [README.md](</Users/krisbrown/workspaces/knowledge-islands/tools-mgit/README.md>) - local SHA-256 `8f0168bcf43f98e9a9f9b4d5ed9ff202d241e781e13a6713c24fe8a414b1681e`.
- [mgit](</Users/krisbrown/workspaces/knowledge-islands/tools-mgit/bin/mgit>) - local SHA-256 `4b47d996a0c01bea787734a0e9c40e5f24ebf3c04dea85addf6be9c6cdeadf2c`.
- [KI-TOOL-MGIT-CLI-032-chain-command.md](</Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-032-chain-command.md>) - local SHA-256 `6023a96310ce2ea629bff488abf4e94de761382060dc19abd18010f429f019f9`.

### S9

- [messages.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.tools-burndown/messages.md>) - local SHA-256 `c5cb6b6adb7687d6cf05011aa91cc53bb848999efa6739e1dcaa0b2253ebe321`.

### S10

- [sync.md](</Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-terra/briefs/sync.md>) - local SHA-256 `0eb1c57c0bb691eee69a6923be9cefd163501d0f375587e783b64f05946783bc`.

### S11

- [automation.ts](</Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/automation.ts>) - local SHA-256 `9ddd4e3797353aad1d3d229aabb4944291b79bca33037aac1cfd711c593d5f1c`.
- [automation.ts](</Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/contracts/src/automation.ts>) - local SHA-256 `3ada15394cb7ea6b7384e4802eb4156f285bc56379edccd1c22b7fea5208a690`.

### S12

- [standards-coordination.md](</Users/krisbrown/.agents/skills/ki-coordination/references/standards-coordination.md>) - local SHA-256 `72bc8461bdb30aa14acc748db9a043616e7356b7a29e1738892ef8f2e57667ce`.

### S13

- [standards-background-runs.md](</Users/krisbrown/.agents/skills/ki-delegation/references/standards-background-runs.md>) - local SHA-256 `fed72c93a9a07bc3f43f19e8e3a8ed158014532300ed4327ea88d65bac362979`.
- [standards-git.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/.agents/skills/ki-git/references/standards-git.md>) - local SHA-256 `782bfa33005f8106d753d1099d60f7d7da6fe4d4a10db33939100cfeb3a4e032`.

### Method and additional review evidence

- [standards-work-design.md](</Users/krisbrown/.agents/skills/ki-work-design/references/standards-work-design.md>) - local SHA-256 `0947f3f0eae6d582853f476741953b95b4e1365479477adfcd6f855c93b25aeb`.
- [brief.md](</Users/krisbrown/.agents/skills/ki-work-design/assets/brief.md>) - local SHA-256 `472547813cf377f60aa49142d237d09419c74434911e0862d2af7d6d7fcbd9fe`.
- [review.md](</Users/krisbrown/.agents/skills/ki-work-design/assets/review.md>) - local SHA-256 `a318078b2930271674e0452ca0ef83e0392b749e16c94daacb4120b95e31b14e`.
- [automation.test.ts](</Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/automation.test.ts>) - local SHA-256 `5f98bdd75ffff5605ef77e4abe3e90743a69c916901ddb8b37b502267dcf8def`.
- [automation.test.ts](</Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/contracts/src/automation.test.ts>) - local SHA-256 `a55e9c39c81e9a712b41347f5a18564a565b4e4f5221952d0f52138975ac9bfd`.
