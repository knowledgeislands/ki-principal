# Brief: inbox-wake-design

Work: ki.prj.ways-of-working. Authority: Kris's INBOX-WATCH words, 31 October 2026, at the end of this package's `decisions.md`. Read them, and the decided WAKE-SESSION and WAKE-DURABLE answers and the open WAKE-HOST query in `queries.md` and `decisions.md`.

Question: how should an active coordination thread notice new messages (`messages.md` lines) and new work while it is idle and waiting on Kris, on each orchestration platform?

For each platform, establish from local help, installed skills and docs (read-only; start no worker, automation or schedule):

- **Orca 1.4.x:** the mailbox (`orca orchestration send`/`check --wait`), automations, and whether a message to a chat session wakes it.
- **Claude Code:** background tasks that re-invoke the session on exit, the `/loop` skill, `ScheduleWakeup`, cron and remote triggers.
- **Codex:** whatever it offers.
- **Paperclip:** whatever it offers.

Say what is verified and what is documented only. Then propose:

1. the portable rule for `ki-coordination` (an armed inbox watcher whenever a coordinating thread is open, not only while runs are going; its interval, what it reads, and how it stops);
2. what each platform adapter (`ki-delegation-orca`, `ki-delegation-paperclip` and `ki agent`) supplies;
3. whether a message sender should also nudge the receiving thread directly where the platform supports it (Orca's mailbox).

Plain English. You may and should challenge earlier decisions where the evidence warrants. End with queries in the QUERY-TURNS shape used in the coordination standard, the recommended option first with its confidence and reason.

Write `design/inbox-wake/design.md` only. Commit it by explicit path and push fast-forward only. Report in plain English.
