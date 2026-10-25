# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rules2

**🤖 → 👤 Handoff to supervisor · Run report at 03:59 BST · last mark 03:34 BST**

---

## Done

- HOOK-4-CLASS: the census covered 78 tracked hooks across 48 workspace repositories, in 12 content variants. Every external tool any hook calls is already tested in its refusal frame, so the impact is nil. HOOK-4 now also checks each external tool a hook calls, at WARN, and every hook in all 48 repositories passes it. Harness `8eb6ef19`, pushed. The repository standard's HOOK-4 bullet quotes Kris's "makes sense" of 20 October.
- HANDOFF-AS-MESSAGE and ACCEPT-BUNDLE are written into the standards, harness `76b6e5c5`, pushed:
  - ki-coordination gains the handoffs bullet in Messages between work and acceptance first in Territory work. Bootstrap step 5 now gathers unaccepted records first. A new Acceptance bundles section covers when, shape, grant and closure, and the ki-coordinator output style is regenerated to match.
  - ki-accept treats a bundle answer as a standing grant.
  - ki-next, ki-work-roadmap (`blocks`) and ki-delegation (CAPTURE-GATE) each carry the handoff rule.
  - Each quotes Kris's words of 20 October.
- Checks on the harness:
  - Full test suite: 1328 pass, 0 fail.
  - Typecheck: clean.
  - Markdown lint: clean.
  - Generated rubric and output style: in sync.
  - ki-engineering audit: PASS.
  - Pre-commit hooks: passed on every commit.
  - The worktree audit's only failure was REPO-REG-1, because the worktree is not registered; that is environmental.
- Harness push: origin/main equalled the base `d45a6179`, so only my two commits were stacked. They went up fast-forward. The worktree and its branch are removed.
- The cross-repository choreography sections now send handoffs and rollouts as a `messages.md` line, never a record. Only the receiver captures a record, and only for deferred work it owns. Local commits, not pushed:
  - Knowledge Islands Principal `f9716cd9`
  - KI Specifications `6b4e2e3d`
  - Techne Harness `03c60e4d`
  - `tools-techne` `5287124d`
- The harness and `tools-ki` AGENTS.md files have no choreography section, so they are unchanged.
- apps-knowledgeislands.info is not edited. A HANDOFF-AS-MESSAGE line in State of play's queue asks for its AGENTS.md change, in Knowledge Islands Principal `25bff0e3`, not pushed.
- REFRESH lines naming both rules, with links to ki-coordination and ki-accept at `76b6e5c5`, went into State of play's queue in eight capitals. Local commits, not pushed:
  - ki `25bff0e3`
  - er `8d5d3fa9`
  - hnr `4158ee57`
  - lgl `6fc8155a`
  - personal `6bcb32d3`
  - si `fc879c0d`
  - tmx `17f8f3de`
  - va `94ccc7b3`
- The eighth capital is si-principal, which now has territory work. The earlier rollout spoke of seven.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- `[unpushed]` 12 local commits: the four AGENTS.md commits, in Knowledge Islands Principal, KI Specifications, Techne Harness and `tools-techne`, and the eight State of play message commits. I read the brief's "push your own" as covering the harness flow only, so none of these is pushed.
- The `ki` CLI fails to load ("export 'granolaStatus' not found") because another session has uncommitted granola edits in `tools-ki`. I worked from a clean export of `tools-ki` HEAD and touched nothing there. The failure will last until that session commits or reverts its edits.

## Queries

No outstanding queries.
