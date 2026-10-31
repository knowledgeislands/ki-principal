# Brief: quiet-listen

Work: ki.prj.ways-of-working, which owns `ki-coordination`. Authority: QUIET-LISTEN, Kris, 31 October 2026, in `decisions.md`.

In ki-agentic-harness `ki-coordination`, change the inbox-watcher and heartbeat wording:

- The watcher is one long-running background loop that spends no model time.
- Every couple of minutes it fetches and fast-forwards silently.
- It exits only on news: a new line in `messages.md`, or a run in this thread's group finishing.
- It has no timed bound while idle, so a quiet period produces no wake, no tool calls and no chat line.
- On a wake, the thread speaks only about what landed.
- Replace the "five minutes while runs go, fifteen otherwise" bounds and the timed heartbeat updates while waiting with this. A run finishing is itself the wake.
- Keep "stop the wake" and the opt-in.

Regenerate the surfaces, and run the banner test, the tests and the audit. Work in your own worktree, fast-forward `main`, commit by explicit path and push fast-forward only. Report in plain English.
