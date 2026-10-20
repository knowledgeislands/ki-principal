# checkout-iso

Work: ki.ways-of-working. Authorised by Kris (20 October): "CHECKOUT-ISOLATION - can we look at this more?"

## Question

Take-stock recommended a) a `ki` commit helper with a per-session index, worktrees for code build runs, serial record-editing runs in a knowledge base and audits reading committed state; the blind review recommended b) a worktree for every coordinator session and writing run in every repository, with serial verified merging. Evidence: `design/take-stock-2026-10-20.md` and the retros it cites.

## Task

1. Map the incidents: for each collision in the retros, which mechanism (shared index, live working tree read by audits, `index.lock`, ref lock on `HEAD`, unpushed stack) caused it, and which of a) and b) would have prevented it.
2. Measure b) in practice, without touching the main checkouts: create and remove a scratch worktree of ki-principal and of ki-agentic-harness; time it, measure disk, run the island pre-commit and `ki repo audit --dry-run`-safe checks in it, and check what assumes the primary checkout path (`ki` registry, the harness dev link, Obsidian, OneDrive source stores, pre-commit audits reading the harness main checkout, `ki agent launch` workdir and `--repo`).
3. Check whether a per-session index (`GIT_INDEX_FILE`) and a commit-landed check are practical with the current hooks.
4. Write `+/_WORK/ki.ways-of-working/design/checkout-isolation.md`: the incident map, the measurements, a merge model for b), and a recommended course (a, b, or a staged mix) with confidence and what it needs from `ki`, the harness and Rig.

## Rules

- Read-only except scratch worktrees (removed afterwards) and the one design file, committed by explicit path in ki-principal; do not push if other sessions' commits are stacked.
- HOOK-GUARD: never run `ki repo conform` without `--dry-run`. CAPTURE-GATE: no new records. No network. British English, ASCII hyphens.

## Report

Owner-report shape: Done, In Progress, Queries (one, CHECKOUT-ISOLATION, with lettered options and confidence).
