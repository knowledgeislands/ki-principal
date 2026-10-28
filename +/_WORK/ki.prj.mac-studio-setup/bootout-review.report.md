# bootout-review report

**🤖 → 👤 Handoff to supervisor · Run report at 23:34 BST**

---

## Done

- Completed the independent BOOTOUT-GUARD review for `ki.mac-studio-setup`; recommend capturing a separate Triage record, confidence high - the missing local guards are directly verified and capturing work is reversible.
- Reviewed checkout `4f97d743b1942f5b6e78c03e5f92d0d01062ad77`; read-only Git comparison found no unstaged differences in the reviewed runtime, payload, test and CORE-047 paths; no commit made.
- Exact source predicates passed: there are three authored bootout sites, and the corresponding functions match the assembled `bin/rig` payload.
- Claim correction: [rig_firewall_load_state](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/29-firewall.bash:220) only observes with `print`; the firewall bootout sites are [rig_firewall_apply](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/29-firewall.bash:505) and [rig_firewall_retire](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/29-firewall.bash:543), neither of which calls the locator validator locally.
- Firewall validation checked: [rig_firewall_locator_valid](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/29-firewall.bash:21) refuses empty, malformed and reserved Apple locators; [declaration validation](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/29-firewall.bash:54) and [retirement preflight](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/29-firewall.bash:413) invoke it.
- Retirement call chain checked: [apply preflight](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/23-application.bash:284) prepares every stale resource and propagates failure; [rig_prepare_retire_invocation](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/21-provider-state.bash:375) dispatches firewall preflight, but [rig_retire_resource](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/21-provider-state.bash:405) dispatches native firewall retirement before its own preparation call at line 413. The public apply path supplies the earlier preflight; native retirement does not independently enforce it.
- Receipt containment checked: [receipt parsing](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/21-provider-state.bash:343) rejects an empty locator before retirement planning.
- Launchd call chain checked: [rig_launchd_unload](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/20-orchestration.bash:600) lacks local label validation; its apply and retire callers pass through [rig_launchd_plist_path](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/20-orchestration.bash:568), which validates the label, before unloading. [Domain selection](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/20-orchestration.bash:296) defaults to `gui/<uid>` and permits an override.
- Fixture coverage inspected: [unsafe declaration rejection](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/tests/rig-firewall.bats:207), [daemon replacement](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/tests/rig-firewall.bats:389), [receipted retirement](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/tests/rig-firewall.bats:444) and [launchd replacement and timeout](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/tests/rig.bats:4247) cover existing public behaviour; no direct references to the four reviewed native helpers were found in the Bats or Bash test files.
- Scope observed: no runtime commands, tests, remote calls or machine changes were performed; the reported terra shutdown is supplied context, not an independently established incident cause.

## In Progress

Nothing is running. No Triage record has been created; this run is authorised to review and report only.

Verification limitation: static review found no demonstrated public-command route past the current checks. Runtime refusal behaviour remains untested in this run.

Report metadata limitation: the supervisor's theme/Project links and last mark were not supplied within the permitted reading scope; the explicitly requested report title is retained and those values have not been invented.

## Queries

### BOOTOUT-GUARD - Guard each native bootout against an empty or invalid label

**Context:** The normal command paths currently validate the relevant locator or label before bootout. Nevertheless, each of the three native bootout sites relies on earlier control flow, and the firewall retirement helper can be reached without performing its own locator preflight. An empty interpolation produces a domain-only target instead of the intended service target. Local refusal makes that safety boundary explicit and protects future callers and refactors. This is a defence-in-depth finding, not proof that Rig caused the reported shutdown. [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) is already awaiting review, and the launchd site extends beyond its firewall scope.

**Query:** Should tools-rig capture a separate Triage record for local validation at all three bootout sites?

**Options:**

a) (recommended, confidence high - all three missing local checks were verified directly and a separate Triage record is reversible) Capture a Triage record for local refusal of empty or invalid labels at the firewall apply, firewall retire and launchd unload boundaries, using each provider's existing label policy. Require a fixture test for each site that bypasses earlier validation and proves a non-zero refusal with no native mutation, plus preservation of valid service-specific argv. Place refusal before other side effects in each affected operation. Any later connection-critical implementation or rollout must carry its tested restore path.

b) Capture nothing because the current public command guards hold; accept continued dependence on distant validation and caller ordering.

c) Fold the guards into CORE-047 when next planned; this delays a shared safety invariant and adds launchd scope to a firewall record already awaiting review.

### 🤖 → 👤 Handoff to supervisor · since 23:34 BST

👤 1 with you

- [with you] BOOTOUT-GUARD recommendation · supervisor · since 23:34 BST
