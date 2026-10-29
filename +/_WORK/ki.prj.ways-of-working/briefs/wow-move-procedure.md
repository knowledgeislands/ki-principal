# wow-move-procedure - stop for a host move: a procedure any thread can follow now

Goal (MOVE-READY-GOAL, decisions.md): a short, self-contained procedure Kris can send to existing coordinating threads so each gets its work to a portable rest before Kris moves hosts (terra to sol). It must work under today's `ki-coordination` standard and words, while matching the agreed state machine (stop -> At rest, reason moving; resume -> Bootstrap on the new host).

Read: decisions DRAIN-MEANS, TRANSITION-CONDITIONS, WORK-CYCLE-SHAPE, WORKING-EXIT, ROLES-ORCHESTRATOR; `design/work-state-machine.md` (Portability checks, Host moves); the `ki-coordination` standard's hold section in `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md`.

Write `+/_WORK/ki.prj.ways-of-working/design/stop-for-host-move.md` (one page, plain language):

1. What "stopped for a move" means: the portability postcondition - deleting the local checkout loses nothing.
2. The steps in order, as a thread performs them: read IMPORTANT messages; cancel wakes; drain (launch nothing; let near-finished runs finish; stop others at a safe point with restart recorded, brief kept); receive finished runs and home their outcomes; the eight portability checks across every repository the work or its runs touched (commit by explicit path, ff-only pull/push, run worktrees removed, branches merged or pushed, `git fetch --prune`, no stash or local-only ref, PRs recorded, runtime-only reports homed); park open queries; set `state.md` to `state: on-hold`, `hold.reason: moving to sol`, `hold.release: resume on sol`; commit `docs(work): <id> hold, paused` and push; give the hold report.
3. If any check fails or cannot be run: do not set on-hold; report NOT DRAINED with the one-line blocker, leave everything in place, and name another session's files without touching them.
4. On the new host: fetch, level check, `Re-bootstrap as <id> under ki-coordination.`
5. Draft the one message line to send to each thread (`- IMPORTANT · 2026-10-29 · HOST-MOVE · KI > Model > Ways of working (ki.prj.ways-of-working): ...` linking the procedure by absolute path), and list the live work packages that should receive it: every `+/_WORK/*/state.md` not on-hold or finished across the workspace repositories under `/Users/krisbrown/workspaces/`, with id, repository and state.

Do not send anything or change any other file. Commit only the procedure by explicit path (`docs(work): ki.prj.ways-of-working stop-for-host-move procedure`); pull ff-only, else `git merge origin/main` (never rebase, stash, reset or force); push ff-only. Be quick.
