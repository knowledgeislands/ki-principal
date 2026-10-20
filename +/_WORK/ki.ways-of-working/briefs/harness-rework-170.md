# harness-rework-170 - fix KI-HARNESS-GOV-170's review findings

Work: `ki.ways-of-working`, package `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/`. Repository: `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`.

[KI-HARNESS-GOV-170](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-170-keep-resolution-targets-local.md) failed independent review. The findings are in `/Users/krisbrown/.local/state/ki/agents/ways-of-working/accept-harness-170.report.md` and in the record itself. In brief, `skills/change-management/ki-accept/scripts/internal/acceptance-cycle.ts` (around line 154) still rejects an approved cross-repository replacement that carries no target, and still accepts a foreign-repository target. Existing fixtures preserve both behaviours.

## Do

1. In a harness worktree, under `ki-git`:
   - make the acceptance model match the record's rule;
   - update the contradicting fixtures;
   - add regression tests that fail on the old behaviour.
2. Run `bun run test`, `bunx tsc --noEmit`, and the `ki-accept`, `ki-work-roadmap` and `ki-skills` rubrics, generation and audits. If `ki-accept` cannot be audited as a skill, say so and verify it directly.
3. Return the record to awaiting review with the review packet refreshed, and fast-forward local `main`.

## Bounds

- Do not push.
- Do not accept or prune.
- Create no record.
- Never `--no-verify`.
- Do not touch other worktrees.
- Write British English with ASCII hyphens only.

## Report

The owner-report shape at your report path.
