VERDICT: cancel · confidence high - Current hosts are covered; preserve the release contract and make ARM Linux expansion conditional on real demand.

# Blind review - SORT-ARM › wow-blind-sort-arm

**Run report at 04:05 BST**

---

## Done

Read-only review completed; no repository changes or commits. Exact record-field and installer-source checks passed; no runtime, network or published-release checks were performed.

The [record](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-125-ki-release-contract.md:49) corroborates rebuilt x86 vega, no planned ARM host, no current blockers and Rig's independence. Its 20 October review deliberately retained Hold; cancellation would change that choice, rather than repair an invalid record. With the supplied host context, an indefinite delivery commitment adds little value.

The [installer](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/install.sh:205) and [release guide](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/guides/developer/releasing.md:11) support the three-target claim: darwin-arm64, darwin-x64 and glibc linux-x64. Sol's architecture is supplied context, not independently verified hardware evidence.

Preserve an Agent host Idea: when an ARM Linux host is actually needed, add linux-arm64 build/archive support, installer detection and manifest validation, and release checks/tests. Existing macOS ARM support does not trigger this expansion.

Preserve separately the reusable cross-tool release-contract documentation requirement: per-platform archives, checksum manifest, Ed25519 signature and embedded installer public key. The release guide already documents KI's current implementation; a short explicit contract section there can retain the adoptable requirement, distinguishing today's three targets from conditional linux-arm64. The linked [architecture note](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Engineering%20Practice/Architecture/Hosts,%20Roles%20and%20Layers.md:94) retains the broader contract, but its “ki already does” claim overstates four-platform conformance.

Retain the three thin channels and ownership boundaries: Homebrew tap for Macs, Rig signed-release installation and bootstrap installer; other tools adopt in their own repositories; apt/AUR/Nix remain deferred. Cancellation must retain the record's provenance and rationale, and release publication remains separately approved. The original audit link is absent locally; its work-area replacement was excluded from this blind review.

## In Progress

Nothing is running. Outstanding - no action requested now: this recommendation has not changed the record or created an Idea or documentation work.

## Queries

No outstanding queries.
