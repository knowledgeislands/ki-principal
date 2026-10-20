# worktree-flow - make worktrees visible and never stuck

Kris (CHECKOUT-ISOLATION): "happy to do a trial, and I think probably work trees make sense. The problem is, it's hard to see any progress using the normal tooling. Is there an approach to making work trees work better? What I don't like is how stuff gets stuck on them."

## Task

Design only. Read `design/checkout-isolation.md`, the launcher (`tools-ki` agent code), `ki-git` and `ki-delegation`. Count today's worktrees and branches across the estate that are unmerged or stale. Write `design/worktree-flow.md`: why work gets stuck (with today's examples), and a small set of fixes, e.g. every run integrates and removes its worktree before it reports, `ki agent status` and the Observatory show each live worktree with its ahead and behind counts and age, State of play sweeps stale worktrees at each mark, a naming rule tying worktree to run. Each fix with its owner and check, and one or two queries. Commit the note by explicit path. No code changes.

## Limits

- CAPTURE-GATE: create no new roadmap records. HOOK-GUARD: never run `ki repo conform` without `--dry-run`.
- Harness edits only in a worktree, never the primary harness checkout. Never `--no-verify`, never force-push, push only your own commits fast-forward. Stay out of ki-design and apps-knowledgeislands.info.
- Nothing destructive (cancel, prune, delete, GitHub setting change) without it coming back as a query.
- British English, ASCII hyphens, they/them. Read Kris's words in `decisions.md` ("owner answers on the 03:08 BST send") first.

## Report

Owner report: Done, In Progress, Queries (Context, Query, Options; a) recommended with confidence).
