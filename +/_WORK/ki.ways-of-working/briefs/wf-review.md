# Blind review: worktree trial queries

Run under Codex at high effort, read-only. Do not read `+/_WORK/ki.ways-of-working/` or any decisions log: this review is blind. You may read the harness standards (`ki-git`, `ki-delegation`, `ki-coordination` in /Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills), tools-ki source and `ki agent --help`.

## Context

Sessions collide in shared checkouts, so Kris agreed a trial of Git worktrees for runs. Today's stuck work sat on run branches: a run finishes on its branch, and merging waits for a separate launch (one branch waited 1 h 39 min, another 2 h 4 min behind a red baseline). Under `ki-git`, merging into `main` is a separate decision a run does not make without authority. Proposed fixes: F1 a run integrates its own branch, removes its worktree and reports; F2 one worktree path and branch name per run; F3 `ki agent status` and the Observatory show each worktree's ahead and behind counts, uncommitted files and age, flagging stranded ones; F4 the coordinating session sweeps worktrees at each mark; F5 the repository registry recognises linked worktrees (until then audits in a ki-principal worktree report false failures); F6 tools-ki edited only off its primary checkout. F1 and F4 are rules alone; F2, F3, F5 and F6 need tooling. ki-principal's shared checkout is busy, with many sessions committing.

## Queries

WORKTREE-INTEGRATE: Should every worktree run have standing authority to fast-forward its own branch into the local primary checkout's `main` before it reports?

- Yes, fast-forward only, after gates pass on the rebased range; a run that cannot fast-forward cleanly keeps its worktree and reports it stranded.
- No; runs stop at the branch, the coordinator launches a merge run, and F3 and F4 make waiting branches visible.

WORKTREE-START: Should the trial start now on F1 and F4 with tooling delivered during it, or wait until F2, F3 and F5 have landed?

- Start now in code repositories under F1 and F4, adding ki-principal's runs once F5 lands.
- Wait until F2, F3 and F5 have landed, then start everywhere.

## Report

For each query give your pick, confidence (high, medium, low), a one-line reason and any conditions. Make no changes, records or commits.
