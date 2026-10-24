VERDICT: REFUSE · confidence high - Required source-review updates are missing; verification otherwise passes.

# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-review-method-enact

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 03:25 BST · last mark 02:10 BST**

---

## Done

### Findings

1. **Blocking - include the required source review.** The normative additions at [standards-coordination.md](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-method-enact.work/worktrees/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md:192), [standards-background-runs.md](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-method-enact.work/worktrees/ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md:148) and [standards-work-package.md](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-method-enact.work/worktrees/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md:78) have no accompanying update to any of the three existing `references/sources.md` files. [ki-coordination/SKILL.md](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-method-enact.work/worktrees/ki-agentic-harness/skills/change-management/ki-coordination/SKILL.md:77) and [ki-delegation/SKILL.md](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-method-enact.work/worktrees/ki-agentic-harness/skills/governance/ki-delegation/SKILL.md:66) require the source review in the same commit as normative changes; [ki-work-package/SKILL.md](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-method-enact.work/worktrees/ki-agentic-harness/skills/governance/ki-work-package/SKILL.md:64) also requires source-review evidence. Add short entries identifying the reviewed proposals and retained deferrals before integration. This needs no new mechanism or policy expansion.

- Reviewed `9bfd5a11d16fba4c4d6bda69fbe287ce3ca3f444` on `wow-method-enact` against its direct parent, local `main` at `0aa9c4d2476cba3b6e2b98834038b7050ea7fbe4`.
- No other actionable correctness, authority or complexity finding: the changes follow the two proposals, preserve narrower gates, and leave the Cloudflare credential proposal, DRAIN ending exception and wider wake service deferred.
- `bun run test`: 1,432 tests passed; zero failures.
- `bunx --no-install tsc --noEmit`: passed.
- Generated surfaces: all five outputs, including `output-styles/ki-coordinator.md`, match their canonical source bytes.
- `ki repo audit --skill ki-skills`: zero failures; two existing LONG-3 refresh warnings.
- `ki repo audit --skill ki-coordination`: zero failures; two COORD-8 warnings from the intentionally unbound isolated user environment.
- `ki repo audit --skill ki-delegation`: passed.
- `ki repo audit --skill ki-work-package`: passed.
- `ki repo audit --skill ki-authoring`: passed.
- `ki repo audit --skill ki-repo-harness`: zero failures; 15 separate warnings, DIAG-4 × 12, LONG-3 × 2 and ITEM-2 × 1.
- Audits used an isolated home with repaired projections and network denied, against a temporary snapshot whose 1394 regular tracked files matched the candidate exactly; its temporary Git HEAD and index also identify the candidate.
- Local `main` can fast-forward mechanically, but this review does not approve advancing it until the required source-review updates are included. The reviewed checkout remains clean and unchanged.

## In Progress

Nothing running in this review. Integration awaits the source-review correction and review of the replacement candidate.

## Queries

### METHOD-SOURCE-REVIEW - Complete the review evidence

**Context:** The candidate's wording, generated surfaces and required mechanical checks pass. It omits the source-review records required alongside normative skill changes, so the current candidate is refused for integration.

**Query:** Should the author complete those short source-review entries before the replacement candidate is integrated?

**Options:**

a) (recommended, confidence high - satisfies the existing skill requirements with only short documentation additions) Return the candidate to its author for the source-review entries, then review the exact replacement commit.

b) Defer the method change and leave local `main` at the reviewed parent.

### 🤖 → 👤 Handoff to supervisor · blocked · since 03:25 BST

👤 1 with you · ⛔ 1 blocked

- [with you] METHOD-SOURCE-REVIEW · ways-of-working coordinator · since 03:25 BST
- [blocked] Candidate integration · method-change author · since 03:25 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
