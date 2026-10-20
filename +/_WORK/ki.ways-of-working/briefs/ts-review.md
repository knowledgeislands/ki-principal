# ts-review

Work: ki.ways-of-working. Blind review of three take-stock queries before they reach Kris. You see each query's Context, Query and unranked options only; do not read `+/_WORK/ki.ways-of-working/queries.md`, `design/take-stock-2026-10-20.md` or any run report.

## Task

For each query, check the Context's factual claims against the repositories and `/Users/krisbrown/workspaces/knowledge-islands/*/+/_WORK/*/design/retro-2026-10-20.md`, then give your own recommended option, its confidence (high, medium, low) and a one-line reason, and any claim you found wrong. Read-only: no edits, no commits, no network.

### CHECKOUT-ISOLATION - Stop sessions colliding in shared checkouts

**Context:** This is the costliest theme. Nine of ten works raised it. Staged files were swept into other works' commits (`e0489e42`, `0836bcae`). One run's half-saved edit made another run report a failure, which cost a decision and a fix run that found nothing to fix. obs-build-brg005 was dropped. The unpushed stack in ki-principal reached 62 commits, only 11 of them from one work. A commit helper with its own index per session stops the sweeping cheaply, but it does not stop lock waits or false audit failures. Worktrees stop all of these, at the cost of merging.

**Query:** How should sessions and runs be kept apart in a shared checkout?

**Options (unranked):**

a) Ship a `ki` commit helper that uses a separate index per session and checks that the commit landed. Give each code-repository build run its own worktree. Serialise runs that edit records in one knowledge-base repository, and have audits read committed state only. b) Give every coordinator session and writing run its own worktree in every repository. c) Allow one owning session per checkout per night, and no technical change.

### OOS-WAKE - A wake for the coordinator that survives its session

**Context:** Five works raised this. Autonomy windows lost about four hours across three works. Reviews finished at 00:35 and were not read until 02:04. A waiter overslept from 00:33 to 01:43. OVERNIGHT-AUTONOMY lapsed after 00:27. Detached runs survive, but the coordinator's waiter dies with its session.

**Query:** What should wake a coordinator when its session is gone?

**Options (unranked):**

a) Add a detached `ki agent` watcher, started with an autonomy window. When a run finishes, it resumes the coordinator with the work's send line. b) Run a launchd job on the agent host through Rig that checks every ten minutes during autonomy windows.

### OWNER-QUEUE - Cap building while acceptance lags

**Context:** Five works raised this. Twenty-two records await Kris's acceptance: 16 for observatory and 6 for mac-studio-setup. ki.chezmoi has 20 open queries and ki.baseline-rollout has 15, against the audit's warning at 8. Every new build adds to the pile. Two works proposed a cap of about eight on their own.

**Query:** Should works stop starting builds and planning while the owner queue is over a cap?

**Options (unranked):**

a) Cap each work at about eight records awaiting acceptance or eight open queries. Pair the cap with a batched decision sitting by decision type and one at-screen checklist for each of sol and terra. b) Keep no cap, and only batch the sittings and checklists. c) Also let wording-only queries on triage records take the recommended option at medium unless Kris objects.

## Report

Owner-report shape: Done (one line per query: your pick, confidence, reason, wrong claims), In Progress, Queries (none expected).
