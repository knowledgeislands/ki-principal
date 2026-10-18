# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › rig-review

**🤖 → 🧑 Handoff to supervisor · Run report at 07:08 BST · last mark 07:08 BST**

---

## Done

I worked in tools-rig's main checkout within fable-opinion-2: one provisional acceptance, six read-only reviews with no acceptance, and KI-TOOL-RIG-CORE-061 planned and built to Awaiting review on fixtures only. Nothing live was touched: no `rig apply`, `rig upgrade` or `rig remove`, no change on Terra, Sol or vega, no chezmoi change and no release. tools-rig `main` is pushed fast-forward.

Rig (tools-rig):

- [KI-TOOL-RIG-CORE-060](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-060-single-target-operation-speed.md) accepted, provisional, on Fable's opinion of 18 October, for Kris to confirm (`92d2d27`). Its independent review had passed; the record says so in `## Done` and is not pruned.
- Independent reviews recorded in each record's Discussion, none accepted (`a31a96c`):
  - [KI-TOOL-RIG-CORE-042](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-042-profile-filtered-dock-items.md), profile-filtered Dock items: **not ready as recorded.** Status and doctor miss a missing app that has no tool link; a fixture confirmed it still reports `present`. See the first query.
  - [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md), tailnet-only firewall: sound as built, but the rule admits any tailnet-range destination, not only the Mac's own tailnet address, so a carrier-grade NAT or hotspot network leaves the gap open that the record says is closed. See the second query.
  - [KI-TOOL-RIG-CORE-052](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-052-doctor-service-launch-prerequisites.md), [KI-TOOL-RIG-CORE-054](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-054-command-line-tools-check.md), [KI-TOOL-RIG-CORE-055](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-055-interpreter-port-owner-matching.md) and [KI-TOOL-RIG-CORE-058](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-058-apply-lock-handler-history.md): no blocking findings, only low notes, each written in the record. These four are ready for your ki-accept sitting.
- [KI-TOOL-RIG-CORE-061](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-061-removal-lock-diagnostics.md), removal lock diagnostics: adopted and planned to Ready, provisional, on Fable's opinion of 18 October, for Kris to confirm (`16a8f80`), then built to Awaiting review on fixtures only (`cacce0c`). `rig remove --apply` now takes the same operation lock as apply and upgrade, before its first observation. `rig doctor` warns about a lock whose owner is still running, and fails on a stale or unknown one, printing the exact command to remove it in text output only. The three planning questions were answered with the recommended course, provisional, for Kris to confirm. RIG-STATE-015, -025 and -030, the manual, two guides and the changelog are updated.

Checks:

- Full test suite: all 581 Bats tests pass.
- `ki repo audit`: passes, with only the existing HOOK-1 warning.
- ShellCheck, Bash syntax and the assembly drift check: clean.
- Fixture benchmark: within budget.
- Native-provider version smoke (version probes only): passes.
- `mandoc` lint and `git diff --check`: clean.
- The six reviews ran at `92d2d27`, where the same gate passed with 572 tests; the version smoke was not run for them.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Your confirmation of the KI-TOOL-RIG-CORE-060 acceptance and of the KI-TOOL-RIG-CORE-061 adoption, plan and build.
- KI-TOOL-RIG-CORE-052, -054, -055 and -058 await your ki-accept; -061 joins them once you have read its packet.
- KI-TOOL-RIG-CORE-042's acceptance check on Sol still needs the chezmoi declaration, your placement decision and an approved live apply, as before.
- The installed Rig on both Macs runs the old code until a release, which is yours (TOOLS-RELEASE).

## Queries

### 1. KI-TOOL-RIG-CORE-042 missing-app check

**Context:** The record says status and doctor flag a missing included Dock app whether or not it is linked to a tool, but the code skips unlinked items, so a missing unlinked app still reads as `present`. Apply still refuses before changing anything, so this is a reporting gap, not a wrong write.

**Query:** Should the code be fixed to check every included item, or should the record and specification be narrowed to linked items?

**Options:**

a) (recommended, confidence high - the plan's Verify contract asks for any selected missing app, and the fix is one condition plus a test) Fix the code under KI-TOOL-RIG-CORE-042 before acceptance, as a small fixture-only change.

b) Accept as built and correct the record and specification to say only linked items are checked.

c) Accept now and capture the fix as a follow-up record.

### 2. KI-TOOL-RIG-CORE-047 destination range

**Context:** The firewall passes traffic from and to the whole `100.64.0.0/10` tailnet range. If the Mac's own LAN address falls in that range, as on carrier-grade NAT and some hotspots, a neighbour on that network reaches port 5900. The Discussion says this gap is closed.

**Query:** Should the residual risk be documented and accepted, or should the destination be narrowed to the Mac's own tailnet addresses?

**Options:**

a) (recommended, confidence medium - both Macs sit on home networks outside that range today, so documenting is honest and cheap, and narrowing needs live address discovery) Correct the Discussion, specification and ADR-KI-TOOL-RIG-009 to state the risk, and capture a follow-up that narrows the destination with a pf table refreshed at apply.

b) Narrow the destination under KI-TOOL-RIG-CORE-047 before acceptance.

c) Accept as recorded.

### 🤖 → 🧑 Handoff to supervisor · since 06:36 BST

🧑 2 with you · 🏁 run finished

- [committed] KI-TOOL-RIG-CORE-060 accepted provisionally, tools-rig, pushed
- [committed] six independent reviews, tools-rig, pushed
- [committed] KI-TOOL-RIG-CORE-061 planned and built to Awaiting review, tools-rig, pushed
- [committed] rig-review report in ki-principal, pushed
