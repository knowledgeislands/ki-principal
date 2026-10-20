# green-main

Work: ki.ways-of-working. Authorised by Kris's GREEN-MAIN a) (20 October): "a red baseline stops the line; harness hook tests pass before any rollout; harness edits off the shared main checkout."

## Task

In ki-agentic-harness, in a fresh worktree off `origin/main`, make the full `bun run test` suite pass. Four hook tests fail on unchanged `main`: `hooks/pre-commit.test.ts`, `hooks/commit-msg.test.ts`, `hooks/git-hook-stub.test.ts` (see `/Users/krisbrown/.local/state/ki/agents/ways-of-working/checker-gaps.report.md`). Diagnose first: if a test is stale against the intended hook behaviour from ki.tools-burndown's HOOKS-MIGRATION (`/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/design/hooks-standard.md`), fix the test; if the hook itself is wrong, fix the hook. If the fix needs a decision, stop and report it as a query.

Then integrate the waiting branches, each rebased onto the green `main`, full suite re-run after each, fast-forward only:

1. branch `lane-triage` (KI-HARNESS-GOV-219, KI-HARNESS-GOV-224); afterwards run `ki dev skill rubric ki-coordination`, `ki dev skill rubric ki-diagrams` (expect no diff) and `ki repo audit --skill ki-diagrams`.
2. checker-gaps' candidate in `/Users/krisbrown/.local/state/ki/worktrees/checker-gaps-20261020` (branch `checker-gaps`): commit it there by explicit path, rebase, re-run gates, integrate.

## Rules

- Never edit in the main harness checkout; fast-forward it only after pushing. Push fast-forward only when your own commits alone are stacked; otherwise name the others once in Done and leave the push. Never `--no-verify` or force-push.
- Remove worktrees and merged branches afterwards.
- HOOK-GUARD: never run `ki repo conform` without `--dry-run`. CAPTURE-GATE: no new records. British English, ASCII hyphens.

## Report

Owner-report shape: Done, In Progress, Queries.
