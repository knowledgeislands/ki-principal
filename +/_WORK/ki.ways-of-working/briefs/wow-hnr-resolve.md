# wow-hnr-resolve

## Goal

Publish hnr-principal's one unpublished local commit `6043f001` (a line appended to `+/_WORK/hnr/messages.md` asking HNR to list its confidential sites in root `AGENTS.md`) onto `origin/main`, which is 86 commits ahead at `3052c4c3`, six of them touching the same `messages.md`.

## Do

1. In a worktree or temporary clone of your own, not the primary checkout, rebase `6043f001` onto `origin/main`. Keep every incoming line of `messages.md`; the only change of ours is the appended line.
2. If the rebase is clean or the conflict is purely positional (both sides appended lines), resolve by keeping all lines, ours last, then push fast-forward only.
3. If our line duplicates or contradicts an incoming line, or the conflict is anything other than positional, stop without pushing and report it as a query.
4. Then bring the primary checkout at the path above level with `origin/main` by fast-forward only, if it is clean apart from `6043f001`; otherwise leave it and say why.

## Rules

CONFLICT-RUN: one bounded resolve, push tier, fast-forward only, never force or `--no-verify`. Touch nothing else in hnr-principal. No messaging to people, no external systems.

## Report

Owner report: Done, In Progress, Queries; the pushed commit; the primary checkout's state.
