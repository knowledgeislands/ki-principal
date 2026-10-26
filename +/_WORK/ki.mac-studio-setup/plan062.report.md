# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [Mac Studio setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup.md) › plan062

**🤖 → 👤 Handoff to supervisor · Run report at 23:49 BST · last mark 23:36 BST · blocked**

---

## Done

- [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md) adopted to Now under Kris's RIG-ORDER a) decision of 23:27 BST and fully shaped: current state, planning answers, steps, files, verification, documentation impact, and size `m`. Its status is `draft`, not Ready, because two queries below decide its outcome.
- The plan builds on what [KI-TOOL-RIG-CORE-063 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/735a8e8560f951afeaa0194df52c5dffa26a3797/docs/roadmap/KI-TOOL-RIG-CORE-063-fatal-bats-assertions.md) changed: new assertions must end `|| false`, the SHELL-FATAL audit must stay clean, and the existing range assertions in the firewall tests are the ones to update.
- How Rig would find the address: a read-only `ifconfig` on sol, run without root, shows one tunnel interface holding both Tailscale addresses. So the Mac's own addresses can be found without root or the Tailscale command-line tool. terra is still to be checked the same way.
- Commit `85bafea` docs(roadmap): shape [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md) to draft for the destination decision. Roadmap audit: no failures. Local only on tools-rig `main`; nothing pushed, applied or touched elsewhere.

## In Progress

Nothing is running. Pending handoff: tools-rig `main` on sol holds unpushed commits `41adda2`, `7665767` and `85bafea`.

Not requested now: [KI-TOOL-RIG-CORE-068](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md) edits the same firewall module, tests and specification, so the plan says to deliver the two records one after the other.

## Queries

**Q-062-SCOPE**

**Context:** Allowing only traffic addressed to the Mac's own tailnet address stops a neighbour on a carrier-grade NAT or hotspot network from reaching Screen Sharing by scanning the network. It does not stop a neighbour who already knows the Mac's tailnet address and sends traffic to it directly over the local network. macOS accepts that traffic on any interface. The reply goes back over the local network, so a TCP connection can complete. The only full fix is to match the Tailscale interface by name, but that name (`utunN`) changes whenever Tailscale restarts, and nothing would trigger Rig to reload. Tailnet access would then be blocked silently until someone runs an attended `apply --sudo`, with SSH as the recovery route.

**Query:** Should [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md) deliver the own-address destination and record that one targeted case as a remaining risk?

**Options:** a) (recommended, confidence medium - it closes the common scanning case at no availability cost; the remaining case needs a targeted attacker on the same network) Deliver the own-address destination with no interface match, and state the narrowed remaining risk in the specification, [ADR-KI-TOOL-RIG-009](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/decisions/ADR-KI-TOOL-RIG-009-system-domain-resources-under-an-attended-grant.md) and the guide. b) Also match the discovered `utunN` interface, accepting that tailnet access is silently blocked after any Tailscale restart until an attended reapply. c) Do not build it. Keep the range rule and rely on the operational advice to keep Screen Sharing off on shared networks.

**Q-062-ABSENT**

**Context:** At apply time Tailscale may be down, or no tailnet address may be found. Tailscale keeps a node's addresses for the node's lifetime, so an anchor that is already installed stays correct.

**Query:** What should apply do when it cannot find the Mac's own tailnet address?

**Options:** a) (recommended, confidence high - addresses are stable, and this neither weakens the rule nor locks out access) Refuse: report `unknown` with `tailnet-address-undiscoverable`, and install or rewrite nothing. b) Fail closed: install an anchor that allows loopback only, blocking tailnet access until a later attended apply. c) Fall back to the current range rule for that apply.
