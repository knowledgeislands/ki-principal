# scope-review report

## [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [Mac Studio setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup.md) › scope-review

**🤖 → 👤 Handoff to supervisor · Run report at 23:51 BST · last mark 23:36 BST**

---

### Done

- Completed the independent scope review: recommend the own-address destination without an interface match, with explicit acceptance of the remaining targeted exposure; confidence medium because the renderer and reload mechanism are verified directly, but the routing-dependent TCP case and interface renumbering were not reproduced.
- Repository guidance and review standards checked: followed the read-only boundary; no repository edits, commits, remote calls or machine changes, and none of the prohibited commands ran.
- [Firewall renderer and daemon](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/29-firewall.bash:148) checked: the current address rules have no ingress-interface constraint, and the daemon reloads a static anchor at boot and on changes to the system pf configuration; it neither rediscovers the Tailscale interface nor watches Tailscale restarts.
- [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md) checked: destination discovery, ambiguity refusal, address drift, fixture isolation and documentation changes are planned; the record remains draft and this review does not authorise delivery or settle Q-062-ABSENT.
- [RIG-ORCH-023](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/orchestration.md:232), [RIG-STATE-045](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/state.md:493), [RIG-CONF-030](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/configuration.md:295), [ADR-KI-TOOL-RIG-009](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/decisions/ADR-KI-TOOL-RIG-009-system-domain-resources-under-an-attended-grant.md:41) and the [firewall guide](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/guides/user/operational-resources.md:167) checked: present contracts describe range filtering, unprivileged evidence limits and SSH recovery; the ADR and guide understate the targeted TCP case described in the brief.
- Local unprivileged interface inventory checked: exactly one interface carries both an IPv4 address in the Tailscale range and an IPv6 address in its ULA prefix, supporting the proposed paired discovery on this Mac; the other Mac was not inspected.
- [Firewall fixtures](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/tests/rig-firewall.bats:146) and local [pf manual](/usr/share/man/man5/pf.conf.5) checked by reading only: fixtures cover the current range rules; the manual distinguishes an ingress-interface match from address matching. No tests or live probes ran.
- [Documented rollback and restore rehearsal](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md:168) checked: the existing record reports successful emergency rollback, restore and fresh SSH connections on terra; the [sol attended check](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md:222) reports tailnet access and LAN refusal. This is recorded prior evidence, not a rehearsal performed by this reviewer.
- Local path history checked: the current range implementation and later risk correction precede this draft; no implementation of the proposed narrowing was found in the reviewed module.

### In Progress

Nothing is running. The supervisor holds the scope decision for [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md).

Outstanding - no action requested now: the proposed implementation and its fixture checks remain future work. No live cross-interface TCP experiment, Tailscale restart or remote-host discovery was authorised or performed. The local IPv4 interface-check setting is enabled; its value alone does not establish the outcome of the routing-dependent attack in the brief. Before any connection-critical rollout, carry the existing tested SSH rollback and restore path explicitly into the attended task.

### Queries

#### [Q-062-SCOPE](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md:49) - Accept bounded destination filtering

**Context:** Narrowing the destination removes the current rule's permission for a neighbour to connect to the Mac's ordinary local-network address when both local addresses fall in the carrier-grade NAT range. It does not authenticate the ingress path: a neighbour able to deliver packets to the Mac's tailnet address over the LAN still satisfies the address predicates. Where the Mac accepts those packets and its return route reaches that neighbour over the LAN, TCP can complete; the remaining risk must not be described as UDP-only or as requiring merely a forged source with no reply path. The Mac's tailnet address is not a secret or an authentication boundary. Matching a discovered interface would constrain ingress, but the current static loader has no mechanism to track a changed interface name, so a routine Tailscale restart can leave Screen Sharing unreachable until attended repair. SSH recovery limits the damage but does not make that recurring failure a sound default. Retaining the broad range rule preserves the larger exposure without gaining availability over own-address rules under the stated address-stability premise.

**Query:** Should [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md) deliver own-address destination filtering without an interface match, explicitly accepting the remaining targeted LAN case?

**Options:**

a) (recommended, confidence medium - the code confirms the narrower match and static reload trade-off; the routing-dependent TCP case and restart behaviour were not reproduced) Deliver the own-address destination with no interface match. State the remaining targeted TCP and UDP exposure in the specification, [ADR-KI-TOOL-RIG-009](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/decisions/ADR-KI-TOOL-RIG-009-system-domain-resources-under-an-attended-grant.md:41) and the guide, and qualify the goal and user-facing claims so that tailnet-only is not presented as a guarantee of authenticated Tailscale ingress. Preserve the existing advice to disable Screen Sharing on untrusted shared networks when that stronger guarantee is required. Include paired-address discovery, refusal on ambiguous discovery and stale-address reporting in delivery; keep the separate absent-address decision with the supervisor.

b) Also match the discovered interface, accepting that an interface-name change can silently interrupt tailnet Screen Sharing until an attended reapply. Choose this only if the owner expressly prefers that availability cost; a reliable automatic interface-refresh design would be additional scope beyond this option and the present loader.

c) Build nothing and retain the range rule with shared-network advice, accepting that ordinary access to a local address inside the shared range remains possible.

#### 🤖 → 👤 Handoff to supervisor · since 23:51 BST

👤 1 with you · 🤖 0 running · ⛔ 0 blocked

- [with you] Q-062-SCOPE independent recommendation · supervisor of ki.mac-studio-setup · since 23:51 BST
