# [Knowledge Islands](/Users/krisbrown/kis/knowledge-islands/ki-principal/Admin/Governance/Charter.md) › State of play › skill-harvest

**🤖 → 👤 Handoff to supervisor · Run report at 22:19 GMT · last mark 00:03 GMT**

---

## Done

- Surveyed ki.sop.main's package and checked each lesson against the harness skills; nine items to capture, one candidate (the coordinator not removing its own worktree) already held by ki-delegation's runtime-check rule and not sent.
- Reply sent as one ACK MSG-c6fa7c81 line at the top of [ki.reg.guilds' Inbound](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/+/_WORK/ki.reg.guilds/messages.md), committed as ki-agentic-harness `9ab67275`; rumdl clean, commit hooks passed. **Not published:** `origin/main` took another session's reply to the same file a minute earlier, so local `main` is 1 ahead and 3 behind and this run may not rebase; it needs a bounded resolve run that rebases only `9ab67275`, keeping both lines at the top of Inbound. Until then the harness checkout's fast-forward pulls fail for every session using it.
- The nine items sent: (1) watcher lifetime and the runtime's background limit, re-armed at the longest limit each wake, to ki-coordination; (2) ki-delegation's five-minute waiter bound against ki-coordination's no timed bound, to ki-delegation; (3) count only `## Inbound` lines, to ki-coordination; (4) wait on Agora's `call/` and `doorbell/` paths, to ki-coordination with ki-delegation; (5) never drop Inbound lines when rewriting `messages.md`, to ki-work-package; (6) ACK-ALWAYS, to ki-coordination; (7) reply line written, committed and pushed in one step through a temporary worktree, to ki-git; (8) `bun install` in a fresh worktree before hooks run, to ki-git; (9) `--allow fetch` for brief bodies that fetch, pull or push, to ki-delegation.
- Disposition recorded in ki.sop.main's [decisions log](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/decisions.md) (SKILL-HARVEST), Inbound line removed and brief deleted in ki-principal `30bcacbb`; rumdl clean, hooks passed, pushed.
- One correction to the brief: the 13 lost Inbound lines were dropped by the 4 November rewrite `73a0774a` and found on 6 November; the item says so.
- Leftover worktree `/tmp/inbox-ack-83530` was clean with HEAD `590948d4` on the inbox's `origin/main`, and is removed.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The harness reply `9ab67275` waits on a bounded resolve run, which the coordinator launches; nothing is needed from Kris.
- `_emerging/refresh-footer.report.md` in ki.sop.main is untracked from another run and was left untouched.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 22:19 GMT

🤖 0 running · ⛔ 1 blocked

- [blocked] harness reply `9ab67275` push, diverged from origin · ki-agentic-harness · since 22:18

🧵 ki.sop.main
