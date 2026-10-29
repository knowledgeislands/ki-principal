# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › away-sync-query-review

**🤖 → 👤 Handoff to supervisor · Run report at 01:52 GMT · last mark 01:04 GMT**

---

## Done

- Reviewed both questions independently from current instructions, product contracts, local source and host declarations; no package queries, decisions logs, run reports, design reports or linked prior recommendations were opened.
- Direct source checks confirm existing Rig scheduling declarations, Bridge confirmation gates and mgit's fast-forward/non-force behaviour; these checks establish capabilities, not authority or live readiness.
- Read the complete run inbox and retained the blind-review boundary; no remote, service, scheduler, credential or runtime operation was made.
- No commits: this unit writes only its required machine-local report and progress status; no tracked artefact, owner choice or implementation was created.
- Report checks passed: required sections, both confidence-labelled recommendations, all local evidence links and six exact source predicates; scratch directory is empty.

## In Progress

Nothing running in this review.

Outstanding - no action requested now: live deployment, credentials, cross-host availability and an executable sync recipe were not tested. Source inspection cannot establish those facts. The recommendations below are for planning only; all existing holds and approval boundaries remain in force.

## Findings

### SYNC-DIRECTION - Develop the direct per-host scheduled-job candidate

**Goal:** Independently recommend which candidate the owners should develop into a reviewable cross-machine Git sync plan, without selecting an executor or authorising rollout; requested on 29 October 2026.

**Scope:** Current repository instructions, Rig/chezmoi scheduling contracts, mgit source, Observatory Bridge source and specifications, standing publication rules and host policy. Excludes earlier proposals and reviews, live machines and remote state.

**As of:** 29 October 2026, 01:52 GMT; local source only.

**Recommendation: direct per-host Rig scheduled activity using a deterministic Tools recipe. Confidence: medium. Reason: it fits the existing separation between host scheduling, Git mechanics and observation with the fewest additional control components.**

Settled constraints:

- Rig already declares scheduled jobs and renders native scheduling; chezmoi owns personal declarations and wrappers, while portable tool behaviour stays with its product. This supports a job invoking a reviewed command, not adding a generic imperative dispatcher to Rig. See [Rig's product boundary](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/AGENTS.md), [scheduled-job schema](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/configuration.md) and [operational resources](/Users/krisbrown/.local/share/chezmoi/docs/guides/agents/operational-resources.md).
- Existing Git mechanics are useful ingredients, not a safe unattended publication policy. [mgit sync](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/README.md) skips dirty, diverged, detached and untracked branches; its [fast-forward step](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/bin/mgit) and [ordinary push](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/bin/mgit) do not supply the owner's unpublished-ancestor review, repository permissions or deployment checks.
- Observatory's current Bridge requires a fresh, single-use plan and exact identifier confirmation for push. Its running service confers no periodic execution mandate. See [governed operations](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/specs/authority.md) and [enforcement](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/operations.ts). An external runner requested by Observatory would still need its own authority; moving the call does not remove the gate.
- Publication and local deployment are separate risks. The supplied standing publication rule is limited to verified low-risk knowledge/documentation/history and yields to narrower repository rules. ChezMoi still requires reviewed apply, and [Observatory runs from its checkout](/Users/krisbrown/.local/share/chezmoi/docs/guides/agents/operational-resources.md). A pull into executable source can affect later execution even without an immediate restart. Connection-critical changes retain a tested restore-path requirement. [Techné policy](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Policies/Techne Programme Focus.md>) does not grant unattended agent sessions; a deterministic job must not silently become one.

Genuinely open: eligible repositories and branches; fetch, local integration and publication permissions separately; runtime-source exclusions; dirty-tree and concurrent-writer handling; bounded execution, durable per-host receipts and post-action read-back; offline recovery and credentials under an explicit deployment decision. The first plan must identify these boundaries rather than equate `mgit sync` with an authorised recipe.

Candidate assessment: attended passes remain the operational fallback under fresh grants. A Rig/chezmoi dispatcher adds coordination that simple scheduling has not yet shown it needs. Bridge scheduling/execution adds a new product and authority contract. Observatory requesting an external runner preserves separation better than Bridge execution, but still introduces a request/control protocol without an established requirement. None is forbidden forever; none is selected by the existence of a running service.

**Ownership split:** [Rig/Mac Studio work](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/work.md) and [chezmoi work](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.chezmoi/work.md) own the host/declaration parts; [Tools work](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.tools-burndown/work.md) owns the deterministic Git-tool part. Observatory owns any separately approved observation or request interface. Kris must approve the planning direction and later grants. This is cross-owner planning, not an Observatory implementation assignment.

Raises: SYNC-DIRECTION below.

### HOST-MEANING - Independent local responsibility, with no automatic takeover

**Goal:** Independently recommend the primary/secondary meaning HOST-SYNC should use and who should settle it; requested on 29 October 2026.

**Scope:** Territory-seat decision and rendered-source bindings, host-project remits, local scheduling and Git mechanics. Excludes prior HOST-SYNC recommendations and live reachability evidence.

**As of:** 29 October 2026, 01:52 GMT; local source only.

**Recommendation: independent per-host responsibility with explicit non-force contention/read-back and no automatic takeover. Confidence: medium. Reason: each machine has its own checkout to keep current, whereas offsets and seats provide no fencing or failover authority.**

Settled constraints: the [territory-seat decision](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-007-territory-seats-on-hosts.md) governs where coordination lands, and explicitly grants no live agent-host authority. The [chezmoi seat binding](/Users/krisbrown/.local/share/chezmoi/.chezmoidata/seats.yaml) describes which territories a coordination service treats as live. These are not a sync-job lease. The [Host network remit](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/host-network.md) owns seat resolution and failover. Neither a five-minute delay nor native same-label non-overlap coordinates writers on different hosts.

For HOST-SYNC planning, each enabled host would act only on its own explicitly eligible checkouts under its own grant. The proposed offsets would mean cadence preference only. A host would not take over another host's jobs, credentials, sessions or deployment duties after lost contact. Failure to observe the other host would remain unknown, not proof that it is stopped. This meaning is independent of which scheduler candidate is eventually chosen.

The plan must make shared-remote contention explicit: serialize local Git writes, recheck the checkout and upstream, use non-force publication and fast-forward integration only, retain a rejected push/divergence as a named outcome, and read back the resulting local and remote revision under the allowed network scope. Bound any retry and re-evaluate eligibility; do not quietly merge, rebase, reset or assume ownership. Each host needs its own durable result, including stale, unavailable and incomplete outcomes. These are proposed planning requirements, not claims that the current tools already implement the whole policy.

**Who settles it:** Kris, through the Rig/Mac Studio and chezmoi owners of HOST-SYNC's operational plan, with Tools defining the Git/read-back contract. Split out any proposal to redefine territory seats, exclusive responsibility, fencing or failover and settle that through [Host network](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/host-network.md). Observatory may report the result but should not decide either authority. The exact placement of the HOST-SYNC tag was not established from a primary work definition; this ownership recommendation follows the verified remits, not an inferred assignment from that tag.

Genuinely open: whether Kris actually requires one exclusive actor or merely fresh local copies on both hosts, plus the freshness target and acceptable offline behaviour. If exclusivity is required, this recommendation no longer suffices: retain attended passes while Host network and the operational owners prepare a separate fencing/failover plan. Existing seat fallback language must not be interpreted as that grant.

Raises: HOST-MEANING below.

## Queries

### SYNC-DIRECTION - Which candidate should receive planning effort?

**Context:** Existing contracts support native scheduled jobs invoking tools, while Bridge execution requires per-operation confirmation. No reviewed unattended sync policy or executor has been selected. Host scheduling, Git behaviour and publication authority have separate owners.

**Query:** Which candidate should the owners develop into a reviewable plan, without selecting an executor or authorising rollout now?

**Options:**

a) (recommended, confidence medium - it follows existing product boundaries and adds the least new coordination machinery) Develop direct per-host Rig scheduled activity using a deterministic Tools recipe, jointly scoped by the host, chezmoi and Tools owners, with grants and rollout left for later review.

b) Retain attended passes under fresh grants while narrowing the required automation outcome.

c) Develop a Rig/chezmoi dispatcher, first demonstrating why direct scheduled jobs cannot meet the requirement.

d) Develop Observatory Bridge scheduling/execution as an explicit product and authority change.

e) Develop Observatory requesting an external deterministic runner, defining the request, authorisation and receipt contracts separately.

### HOST-MEANING - What responsibility should primary and secondary describe?

**Context:** Both hosts hold local checkouts; offsets do not provide exclusivity, and seats govern coordination routing rather than Git execution authority. The host-operation owners can specify independent local sync; territory-seat or failover changes belong to Host network with Kris's decision.

**Query:** What primary/secondary meaning should HOST-SYNC planning use, and which owner should settle it?

**Options:**

a) (recommended, confidence medium - independent local duties keep both checkouts current without inventing a takeover grant) Have Kris settle independent per-host responsibility through Rig/Mac Studio and chezmoi planning, with Tools specifying non-force contention and read-back; treat offsets as cadence only and allow no automatic takeover. Route any seat/failover change separately to Host network.

b) Require exclusive responsibility, with Kris and Host network settling fencing, loss-of-contact and separately reviewed failover before the host-operation owners plan rollout.

c) Retain attended passes while Kris narrows whether the requirement is local freshness on both hosts or a single exclusive actor.

### 🤖 → 👤 Handoff to supervisor · since 01:52 GMT

👤 2 with you · 🅿️ 0 parked

- [with you] SYNC-DIRECTION planning recommendation · supervisor for owner routing · since 01:52 GMT
- [with you] HOST-MEANING planning recommendation · supervisor for owner routing · since 01:52 GMT

🧵 ki.prj.observatory
