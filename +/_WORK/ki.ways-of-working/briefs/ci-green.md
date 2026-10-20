# ci-green

Work: ki.ways-of-working. Authorised by Kris's GREEN-MAIN a) (20 October: a red baseline stops the line) and TRIAGE-ALL (high-confidence adoptions delivered).

## Task

ki-agentic-harness CI's `build` job runs `ki repo audit --repo .` before tests and is red on `main` (`30cbbd1d`): 16 FAIL findings across 3 skills, 9 of them pre-existing and 7 ITEM-3 findings on the unplanned Now drafts (see `/Users/krisbrown/.local/state/ki/agents/ways-of-working/green-main.report.md`).

1. Diagnose each of the 9 pre-existing FAILs; fix the class of each finding, not just the cited lines (CLASS-FIX). If a fix needs a decision, stop on that finding and report it as a query.
2. Run `ki-plan` on KI-HARNESS-GOV-200, -205, -214, -215, -220, -221 and -223 so they reach the planned body shape (planning only; deliver none).
3. Add the missing `bun` presence check before content in KI-HARNESS-GOV-224's receipt step in `.githooks/pre-commit`, per the hooks standard's refuse-before-content rule.
4. Confirm `ki repo audit --repo .` reports 0 FAIL and `bun run test` passes on the result, using a per-command `KI_DATA_HOME` pointing at the worktree as green-main did.

## Rules

- Fresh worktree off `origin/main`; never edit the main harness checkout; fast-forward it only after pushing. Push fast-forward only when your own commits alone are stacked; otherwise name the others once in Done. Never `--no-verify` or force-push. Remove the worktree afterwards.
- Check every path and claim before acting (CLAIM-CHECK). HOOK-GUARD: never run `ki repo conform` without `--dry-run`. CAPTURE-GATE: no new records. British English, ASCII hyphens.

## Report

Owner-report shape: Done, In Progress, Queries.
