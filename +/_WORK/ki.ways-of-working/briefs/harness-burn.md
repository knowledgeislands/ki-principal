# harness-burn - work down the harness roadmap

Work: `ki.ways-of-working`, package `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/`. Repository: `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`.

Kris, 20 October about 05:20 BST: "then we can have a good run at whatever's left in the agentic harness ... keep you know motoring through them, committing and pushing as you go."

## Do

1. List every open record in the harness roadmap (`docs/roadmap/`), and classify each as one of:
   - workable now with no owner decision;
   - needs Kris;
   - blocked on another repository or date;
   - accepted but not pruned.
2. Deliver the workable records one at a time, smallest and most valuable first, for up to about 90 minutes. For each one:
   - refine it to Ready under `ki-work-roadmap` if needed;
   - deliver it under `ki-git` in its own harness worktree (never edit the primary checkout directly), with `bun run test`, `bunx tsc --noEmit`, the affected skill rubrics and generation, and the hooks;
   - take it to awaiting review with a review packet;
   - fast-forward it onto local `main`.
3. Stop cleanly at a record boundary when time is up.

## Bounds

- Do not push: local `main` carries other sessions' unpushed commits.
- Do not accept or prune.
- Create no new record (CAPTURE-GATE); follow-ups go as one line in this work's `messages.md`.
- Never `--no-verify`.
- Run no `ki repo conform` without `--dry-run`.
- Do not touch other sessions' uncommitted files or worktrees.
- Write British English with ASCII hyphens only.

## Report

The owner-report shape at your report path, including:

- the classification table, with each record linked by absolute path;
- the records delivered, each with its commit;
- each owner query, in Context/Query/Options form with a recommended option and confidence.
