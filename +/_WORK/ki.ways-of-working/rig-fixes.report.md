# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › rig-fixes

**🤖 → 🧑 Handoff to supervisor · Run report at 10:37 BST · last mark 22:34 BST**

---

## Done

- **RIG-DOCK-MISSING a), pushed in tools-rig `43d712c`.** Status and doctor now flag every Dock app the profile includes when its path is missing, whether or not it links to a tool. They also stop treating a configuration read error as "nothing missing". A new test deletes an unlinked app and expects drift; it fails on the old executable. The older Dock observation tests had passed only because the old check skipped folder paths that did not exist; they now use real test-owned folders, with every assertion unchanged. [KI-TOOL-RIG-CORE-042](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-042-profile-filtered-dock-items.md) stays at Awaiting review. Its new Review fix section records the fix and corrects the earlier test-coverage claim. It also lists what acceptance on `sol` still needs: the chezmoi Dock record, Kris's placement of studio-only apps such as Lightroom Classic, and an approved live run.
- **RIG-FIREWALL-RANGE a), pushed in tools-rig `225fef3` and `6e93218`.** [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) gains a Range correction section, and RIG-ORCH-023 and [ADR-KI-TOOL-RIG-009](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/decisions/ADR-KI-TOOL-RIG-009-system-domain-resources-under-an-attended-grant.md) are corrected. They now say that a neighbour can reach the port on a carrier-grade NAT or hotspot network that gives the Mac a `100.64.0.0/10` address, and that a one-way forged UDP packet can arrive because the rule names no interface. The operational-resources guide wrongly said such a device "cannot reach the port"; that is corrected too. No code changed. I captured one triage follow-up, [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md), to narrow the rule to each Mac's own tailnet addresses, refreshed at apply.
- **Gate:** the audit has no failures; its only warnings were already there (HOOK-1, plus SHELL-FATAL in files I did not touch). ShellCheck, Bash syntax, assembly drift, benchmark, mandoc and diff checks pass, and all 582 Bats tests pass. I did not run `scripts/smoke-native-providers`, which calls the real package managers, because this run was fixture-only.
- No live `rig apply`, `rig upgrade` or system change on any Mac. Every push was a fast-forward of my commits alone. Nothing was left dirty in tools-rig. The protocol makes this file the only report path, so I wrote nothing in the work folder.

## In Progress

Nothing.

## Queries

**Context:** the Linux `linux-nftables` provider has the same range-only rule (`ip saddr 100.64.0.0/10 ip daddr 100.64.0.0/10`), so it carries the same shared-range risk. I named this in KI-TOOL-RIG-CORE-047's Range correction but left Linux outside KI-TOOL-RIG-CORE-062, because the brief named the Macs. Linux can match the `tailscale0` interface, which would also close the forged-packet gap. **Query:** Should the Linux provider's range risk stay noted but unrecorded, or be added to KI-TOOL-RIG-CORE-062's scope? **Options:** a) (recommended, confidence medium - no Linux profile exists yet, so nothing is exposed today) Leave it noted in KI-TOOL-RIG-CORE-047 and decide when KI-TOOL-RIG-CORE-062 is planned. b) Widen KI-TOOL-RIG-CORE-062 now to cover `linux-nftables`, matching `tailscale0` there. c) Capture a separate Linux record.
