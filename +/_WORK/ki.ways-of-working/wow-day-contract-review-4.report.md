# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-contract-review-4

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 15:14 BST · last mark not supplied in the permitted inputs**

---

## Done

Verdict: Return named parts for revision first: the reconciliation command namespace and its compatibility tests.

Confidence: high - current public help and exact source predicates independently confirm the namespace collision.

Public CLI help and all existing agent subcommand help reviewed; command compatibility check found one blocking defect.

Local process, queue, gate, event, launch-default and Harness authority sources reviewed; no further blocking safety defect found under the draft's evidence gates.

No repository changes, commits, remote calls, live agents or native evaluations; only the requested report and status files written.

## In Progress

Nothing is running.

## Queries

### RECONCILE-SURFACE - settle the existing command collision before commissioning

**Context:** The recovery surfaces in [the draft](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/agent-control-contract.md:66) reuse the existing decision-reconciliation command in [the CLI](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/commands/agent/index.ts:333). Its positional run names can already include the proposed subcommand names under [current validation](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/context.ts:31). Adding those subcommands can reinterpret existing valid decision operations; the contract neither preserves those calls nor authorises their migration.

**Query:** Should the draft choose a distinct recovery namespace, or explicitly approve a migration of decision reconciliation, before its command policy is accepted?

**Options:**

a) (recommended, confidence high - the collision is verified against the current public grammar and source) Revise the reconciliation surfaces and help/compatibility tests to preserve existing decision operations, including runs sharing the proposed subcommand names, or obtain explicit migration approval; retain the other For Kris decisions, precedence policy, build order and evidence gates.

b) Accept the current draft and commission its builds without settling this command ambiguity.

c) Defer the controls entirely.

### 🤖 → 👤 Handoff to supervisor · blocked · since 15:14 BST

👤 1 with you · ⛔ 1 blocked

- [blocked] Reconciliation command policy needs revision · supervisor · since 15:14 BST
