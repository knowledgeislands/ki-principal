# scope-review brief

You are a blind reviewer for the work `ki.mac-studio-setup` in Knowledge Islands Principal, under the QUERY-REVIEW rule of the `ki-coordination` standard. Form your own view of the query below: the course you would recommend, your confidence (`high`, `medium` or `low`) with a one-line reason, and the evidence you checked. Read anything in `/Users/krisbrown/workspaces/knowledge-islands/tools-rig`, especially `docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md`, `src/rig/29-firewall.bash`, ADR-KI-TOOL-RIG-009 and the firewall specification and guide. Run read-only commands only, such as `git log`, `git show` and `ifconfig`. Never run `sudo`, `pfctl`, `launchctl`, `rig` or `ki repo conform`. Edit, commit, push or delete nothing beyond writing your report.

## Q-062-SCOPE - How far the own-address firewall destination goes

**Context:** Rig's tailnet-only Screen Sharing firewall on macOS allows traffic from the Tailscale address range. KI-TOOL-RIG-CORE-062 would narrow the rule so it allows only traffic addressed to the Mac's own tailnet address, discovered without root from `ifconfig`. That stops a neighbour on a carrier-grade NAT or hotspot network from reaching Screen Sharing by scanning. It does not stop a neighbour who already knows the Mac's tailnet address and sends traffic to it directly over the local network: macOS accepts that traffic on any interface, and a TCP connection can complete. Only matching the Tailscale interface by name would close that case, but the name (`utunN`) changes whenever Tailscale restarts, nothing would trigger Rig to reload, and tailnet access would be blocked silently until an attended `apply --sudo`, with SSH as the recovery route.

**Query:** What should KI-TOOL-RIG-CORE-062 deliver?

**Options:**

- Deliver the own-address destination with no interface match, and record the remaining targeted case as a risk in the specification, the ADR and the guide.
- Also match the discovered `utunN` interface, accepting a silent lockout after any Tailscale restart until an attended reapply.
- Build nothing: keep the range rule and rely on the advice to keep Screen Sharing off on shared networks.

## Report

Write `/Users/krisbrown/.local/state/ki/agents/mac-studio-setup/scope-review.report.md`, starting with a `# scope-review report` heading, using British English and ASCII hyphens only. Do not commit it.
