# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › review-gov197

**🤖 → 👤 Handoff to supervisor · Run report at 20:37 BST · last mark 20:20 BST**

---

## Done

- Reviewed commit 3fc59d87 against [KI-HARNESS-GOV-197](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-197-pmo-7-outside-checkout-links.md). It meets every acceptance criterion. Nothing was edited or committed in the harness and nothing was pushed. Net records: 0 in each repository.
- Goal and boundary: [coordination.ts](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/scripts/rubric/contexts/coordination.ts) now checks a link for existence inside the audited checkout (the checkout root comes in from the session, not the working directory) and also outside it wherever the target's folder exists on this machine. Anywhere else it checks shape only, meaning the file name is `<ID>-…md` or `<ID>.md`. A link that fails the shape check is reported as its own `misshapen` finding. The COORD-7 description, the linking rule and the generated rubric all match. The bare-identifier backlog and the release were left out of scope, as the record says.
- Tests are sound: there are unit cases for shape-only links (pass, wrong identifier, folder target, identifier-prefix collision), for a sibling folder that is present (live passes, gone counts as missing) and for an inside-checkout target whose folder is absent. A context case covers a runner-style report, both passing and misshapen. The earlier `/nowhere` cases now sit inside the checkout, so they still test existence.
- Checks on 3fc59d87 (current HEAD only adds roadmap and docs commits on top): `bun run test` passed 1260/1260, `bunx tsc --noEmit` passed, `ki dev skill rubric ki-coordination` is in sync and `ki repo audit --skill ki-coordination` passes in the harness.
- ki-principal on this machine: COORD-7 has 0 `misshapen` findings and 2 `missing` ones. Both are pruned records in sibling checkouts that exist here: KI-HARNESS-GOV-186 from ki.chezmoi's coord-style report, and KI-TOOL-RIG-CORE-058 from ki.mac-studio-setup's rig-lane report (local file gone; I did not resolve their last revisions, so I have not linked them). Flagging them locally is what the design intends, so neither is a regression. The other failures are the bare-identifier backlog, which is out of scope.
- Simulated a CI runner by rewriting every link that points outside ki-principal to a folder that does not exist. Across 46 work reports, existence and shape findings dropped to 0, so COORD-7 failures on CI would come only from the bare-identifier backlog.
- Minor, non-blocking: (1) on a runner, a stale local link to a pruned record in another repository passes on shape. Only a local audit catches it, which is the accepted trade-off. (2) The rubric wording "file name opening with the linked identifier" is slightly looser than the code, which also needs `-` or `.md` straight after the identifier. (3) The standard links the record by a relative path, which will break when the record is pruned, as the existing link to [KI-HARNESS-GOV-210](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-210-work-model-write-in.md) will too.

## In Progress

Nothing is running.

Outstanding - no action requested now: the next `ki` release still has to carry this harness to ki-principal CI. The two pruned-record links above are for their own works (ki.chezmoi and ki.mac-studio-setup) to fix.

## Queries

### [GOV-197-ACCEPT-NOW](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-197-pmo-7-outside-checkout-links.md) - Accept the COORD-7 outside-checkout fix

**Context:** Commit 3fc59d87 meets every acceptance criterion of [KI-HARNESS-GOV-197](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-197-pmo-7-outside-checkout-links.md). Tests, TypeScript, the rubric sync and the harness audit all pass, and there is no COORD-7 regression in ki-principal. In a simulated runner, link findings outside the checkout drop to zero. The three minor notes are wording or trade-offs and none of them blocks.

**Query:** Do you accept KI-HARNESS-GOV-197 as Done?

**Options:**
a) (recommended, confidence high - every check was rerun directly and the review is clean) Accept it now through `ki-accept`, and leave the minor notes as they are.
b) Accept it, and first have the rubric wording tightened to "the identifier followed by `-` or `.md`".
c) Hold acceptance until the `ki` release has shown it passing in ki-principal CI.

### 🤖 → 👤 Handoff to supervisor · since 20:37 BST

👤 1 with you

- [with you] GOV-197-ACCEPT-NOW · owner · since 20:37
