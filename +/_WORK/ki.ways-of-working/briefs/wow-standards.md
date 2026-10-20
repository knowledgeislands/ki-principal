# wow-standards - write the take-stock changes into the standards

Work: ki.ways-of-working (`+/_WORK/ki.ways-of-working/` in ki-principal). Read `design/take-stock-2026-10-20.md`, `design/retro-2026-10-20.md` and `decisions.md` entries from "TAKE-STOCK" onwards (Kris's words) first.

## Task

In ki-agentic-harness, working only in a new worktree (never the primary harness checkout), write Kris's agreed take-stock changes into the standards where each fits (`ki-coordination`, `ki-delegation`, `ki-git`, `ki-next`), quoting Kris's words and date as the standards do:

- BLIND-REVIEW a): masked blind review (Context and Query only, unranked options; reviewer never reads queries.md, decisions.md or reports).
- CLAIM-CHECK a), CLASS-FIX a), GREEN-MAIN a), OOS-WAKE a) (standard text only; the watcher is ki.tools-burndown's), as take-stock defines them.
- SMALL-FIXES (adopted, high): a coordinator may make one-line mechanical fixes in its own work package, committed by explicit path; judgement or other works' files still go to a run. Reconcile with "the coordinator never does substantive work itself".
- OWNER-QUEUE a) with Kris's checks: the audit counts awaiting-acceptance records and open queries per work and warns over about eight; the banner shows the count; backlog-clearing work is allowed.
- HOMELESS-STANDING and CAPTURE-GATE (runs create no new records) into `ki-next` and `ki-delegation`.

Regenerate generated surfaces (`ki dev skill generate ki-coordination --write`), run `bun run test` and the typecheck, commit with conventional subjects, fast-forward `origin/main` and the primary checkout, push only your own commits, remove the worktree.

Then send REFRESH: one line to every live work's `messages.md` and every capital's State of play `messages.md` (same set refresh-banner reached), naming the changed rules and asking each to re-read the standard; and reply to `/Users/krisbrown/workspaces/personal/acquire/+/_WORK/kb.regular.acquire-intake/messages.md` that SMALL-FIXES was adopted and where it now lives. Commit each repository by explicit path.

## Limits

- HOOK-GUARD: never run `ki repo conform` without `--dry-run`.
- CAPTURE-GATE: create no new roadmap records.
- Never `--no-verify`, never force-push, never push another session's commits. Stay out of ki-design and apps-knowledgeislands.info.
- British English, ASCII hyphens, they/them.

## Report

Owner report per ki-coordination run-report rule: Done, In Progress, Queries (Context, Query, Options; a) recommended with confidence).
