# ci-review

Work: ki.ways-of-working. Blind review of one query before it reaches Kris. You see Context, Query and unranked options only. Do not read `+/_WORK/ki.ways-of-working/queries.md`, `+/_WORK/ki.ways-of-working/design/checkout-isolation.md`, `design/take-stock-2026-10-20.md` or any run report.

## CHECKOUT-ISOLATION - Stop sessions colliding in shared checkouts

**Context:** Coordinator sessions and background runs share one primary checkout per repository. The 20 October retros (`/Users/krisbrown/workspaces/*/*/+/_WORK/*/design/retro-2026-10-20.md`) report about 12 collisions: `index.lock` waits, staged files swept into other works' commits (`e0489e42`, `0836bcae` in ki-principal), audits reading another run's half-saved files, plus an unpushed stack. Claims to verify: a scratch worktree of ki-principal or ki-agentic-harness creates in under a second and its pre-commit takes about 2 s; worktrees lack `node_modules`, project skill links and a `ki` registry entry, so audits there show extra failures; `ki agent launch` needs `--repo` set to the primary checkout; a per-session index (`GIT_INDEX_FILE`) can silently revert committed changes with the current hooks; a pathspec commit (`git commit -- <paths>`) leaves the shared index consistent. Kris ruled on 18 October (MAIN-NOT-WORKTREES): "you should be able to just work on the main". Coordinators route messages and state into other works' files, and Kris reads the knowledge base in Obsidian from the primary checkout.

**Query:** How should sessions and runs be kept apart in a shared checkout?

**Options (unranked):**

a) A staged mix: now, a `ki` commit helper using pathspec commits and a check that the commit landed, a `ki-git` rule against plain commits and private indexes in shared checkouts, worktrees with serial local merging for every writing run in code repositories, and audits that judge a run reading committed state; then a one-week pilot of worktrees for long multi-file knowledge-base runs, coordinators and short runs staying on `main`; extend if lock waits continue. b) Every coordinator session and writing run in every repository gets its own worktree, with serial verified merging into `main`, once `ki` supports worktrees (registry, skill links, `--worktree`, an integrate step); reverses MAIN-NOT-WORKTREES. c) One owning session per checkout per night, and no technical change.

## Task

Verify the Context claims you can (scratch worktrees allowed, removed afterwards; no edits to main checkouts, no commits, no network). Give your own pick, confidence (high, medium, low), a one-line reason, and any claim you found wrong.

## Report

Owner-report shape: Done (your pick, confidence, reason, wrong claims), In Progress, Queries (none expected).
