# Screen Sharing firewall review › firewall-blind

**Run report at 01:30 BST**

---

## Done

Recommendation: attended re-apply now, confidence medium, after the preflight and recovery corrections below.

Reason: terra already has a recorded, successful same-machine rollback, reload and restore rehearsal; the declaration and both renderers restrict only TCP/UDP 5900. Reason: this is a bounded correction, but current kernel enforcement is unknown and Rig enables pf globally, so console attendance and live preflight remain essential.

Code review at Rig `87fa261`: confirmed `dae10f2` narrows destinations to the Mac's own tailnet addresses; see [renderer](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/29-firewall.bash:193).

Exact read-only checks: the installed anchor contains eight inbound quick rules, all naming only 5900; the declaration selects TCP/UDP 5900 and the expected literal locator.

Emergency scope: the named-anchor rules flush removes every filter rule in that anchor; for the checked file/render, those are only 5900 rules. It preserves other anchors, states and pf's enabled state; it removes this restriction rather than guaranteeing reachability through other rules. See [local pfctl manual](/usr/share/man/man8/pfctl.8:127).

Recovery evidence: [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md:166) records terra's 19 October reload, daemon bootout, anchor-only rules flush and daemon bootstrap, with fresh SSH succeeding after removal and restoration.

Unsafe assumption: flushing alone is temporary. The installed daemon can reload the anchor at boot or when pf.conf changes. For a stable emergency removal during the session, stop that exact daemon before flushing, as in the recorded rehearsal; use the full literal service name. An earlier empty-variable bootout shut terra down.

Restore assessment: backing up the anchor, restoring its bytes and loading that exact named anchor is sound for an anchor-only change. Also preserve/check the daemon, because [apply](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/29-firewall.bash:575) can replace it. If emergency recovery unloaded it, restore its previous loaded state after restoring the file; verify loaded rules, parent invocation and fresh connectivity. A failed post-load comparison does not automatically restore the old configuration.

SSH/Tailscale assessment: the 5900 rules do not directly match SSH or Tailscale transport. However, [apply's load](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/29-firewall.bash:602) enables pf globally. If pf is disabled, unrelated already-loaded rules can become effective and interrupt either connection; an anchor-only flush would not undo that. Do not claim unconditional immunity.

Exposure assessment: [doctor's logic](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/29-firewall.bash:437) combines declaration drift with wildcard listeners; it does not prove LAN reachability or ineffective kernel rules.

Read-only boundary: no sudo, firewall commands, remote calls, repository edits or commits; only the required status and report files were written. Live tests and repository gates were not run.

## In Progress

Nothing is running.

Outstanding - no action requested now: current pf enablement, effective parent/child rules and fresh Screen Sharing connectivity remain unverified.

## Queries

### FIREWALL-TIMING - Attend now or defer

**Context:** The proposed info and child-rule checks omit the effective parent ruleset. Before proceeding, check pf enablement and the loaded root/parent invocation chain, including relevant other anchors; confirm the dry-run selects only the intended work. Revalidate the recorded recovery on terra with fresh SSH before installing the new anchor. If pf is disabled or unexpected rules are present, stop: the anchor-only restore does not cover global activation. Keep the owner at the console, retain SSH, and check fresh SSH and Screen Sharing flows after apply and recovery; existing pf states can invalidate a LAN-refusal test.

**Query:** Use the corrected attended procedure now, or retain the change for the next scheduled Mac rehearsal?

**Options:**

a) (recommended, confidence medium - the same-machine recovery is recorded and the intended change is limited to 5900) Perform the attended re-apply now only after the live preflight and recovery checks succeed.

b) Leave the anchor unchanged until the next scheduled Mac rehearsal under [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md).
