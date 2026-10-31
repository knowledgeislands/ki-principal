# Brief: listen-and-awake

Work: ki.prj.ways-of-working, which owns `ki-coordination`, `ki-delegation` and `ki-work-package`. Authority: Kris's FEEDBACK-AS-MESSAGE, UNATTENDED-AWAKE and LISTEN-STATUS words, and INBOX-WATCH, all at the end of `decisions.md` (31 October 2026). Read them, and `design/inbox-wake/design.md`, and the inbox queries in `queries.md`, which are not yet answered; do not settle them.

In `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`:

1. **FEEDBACK-AS-MESSAGE.** Replace the written-feedback-file route added in `16f550f7` (`ki-work-package` closed list and entry points) so that owner feedback on a document arrives as a message line. The steward may write the line word for word from Kris's words, with Kris named as the speaker. Keep `feedback/` readable for the tolerance window if anything still uses it.
2. **LISTEN-STATUS.** In `ki-coordination`: an open coordinating thread keeps an inbox watcher armed, the cheap shell loop described in the inbox-wake design. It stops listening while draining and on hold. Every Summary and banner shows the thread's listening state (listening, draining so not listening, or not listening) and whether it is the sync thread for its host. Keep it to one short banner line.
3. **UNATTENDED-AWAKE.** In the unattended-window rules: the window keeps the leading chat session alive and keeps that machine awake for the window (for example `caffeinate -dims -w <pid>` or the platform equivalent), and says so in the entry report. It is an additional mode on top of normal coordination.

Coordinate with run `drain-target`, which is also editing the banner. Start only after it has pushed, and rebase your worktree on the new `main` by merging, not by rebasing a shared checkout. Regenerate the surfaces, and run the banner test, the tests and the audit. Work in your own worktree, fast-forward `main`, commit by explicit path and push fast-forward only. Report in plain English.
