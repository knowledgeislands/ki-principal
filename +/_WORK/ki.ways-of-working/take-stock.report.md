# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › take-stock

**🤖 → 👤 Handoff to supervisor · Run report at 02:14 BST · last mark 02:01 BST**

---

## Done

- Read all ten retros in full (nine in ki-principal, one in Acquire) and every work's `state.md` front matter. Two live works have no retro: [ki.agent-host](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.agent-host/state.md), with worker, and [kb.personal-tower](/Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/kb.personal-tower/state.md), handed to the supervisor.
- Wrote [take-stock-2026-10-20.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/take-stock-2026-10-20.md). It has 8 Working well themes, 13 ranked Not working themes, each with a root cause, and 27 deduplicated changes grouped under five owners.
- Committed it locally as `fd4e657b` by explicit path. Pre-commit and the repository audit passed. Nothing was pushed. `4ba9ffe2`, another session's ki.observatory commit, sits in the same unpushed stack.
- Applied no change and created no record.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Under the coordinator style, the medium-confidence queries below (CHECKOUT-ISOLATION, OOS-WAKE, OWNER-QUEUE) need one blind review before they reach Kris. As the take-stock note itself found, the reviewer should get Context and Query only.
- Smaller changes such as K1, K3, K4, H2, H8, R2, C5 and C6 are in the note and not raised as queries.

## Queries

### CHECKOUT-ISOLATION - Stop sessions colliding in shared checkouts

**Context:** This is the costliest theme. Nine of ten works raised it. Staged files were swept into other works' commits (`e0489e42`, `0836bcae`). One run's half-saved edit made another run report a failure, which cost a decision and a fix run that found nothing to fix. obs-build-brg005 was dropped. The unpushed stack in ki-principal reached 62 commits, only 11 of them from one work. A commit helper with its own index per session stops the sweeping cheaply, but it does not stop lock waits or false audit failures. Worktrees stop all of these, at the cost of merging.

**Query:** How should sessions and runs be kept apart in a shared checkout?

**Options:** a) (recommended, confidence medium - it fixes the worst incidents now, but worktree cost on knowledge-base repositories is untested) Ship a `ki` commit helper that uses a separate index per session and checks that the commit landed. Give each code-repository build run its own worktree. Serialise runs that edit records in one knowledge-base repository, and have audits read committed state only. b) Give every coordinator session and writing run its own worktree in every repository. c) Allow one owning session per checkout per night, and no technical change.

### OOS-WAKE - A wake for the coordinator that survives its session

**Context:** Five works raised this. Autonomy windows lost about four hours across three works. Reviews finished at 00:35 and were not read until 02:04. A waiter overslept from 00:33 to 01:43. OVERNIGHT-AUTONOMY lapsed after 00:27. Detached runs survive, but the coordinator's waiter dies with its session.

**Query:** What should wake a coordinator when its session is gone?

**Options:** a) (recommended, confidence medium - it reuses the detached runs that already work, but resuming a coordinator headlessly is unproven) Add a detached `ki agent` watcher, started with an autonomy window. When a run finishes, it resumes the coordinator with the work's send line. b) Run a launchd job on the agent host through Rig that checks every ten minutes during autonomy windows.

### OWNER-QUEUE - Cap building while acceptance lags

**Context:** Five works raised this. Twenty-two records await Kris's acceptance: 16 for observatory and 6 for mac-studio-setup. ki.chezmoi has 20 open queries and ki.baseline-rollout has 15, against the audit's warning at 8. Every new build adds to the pile. Two works proposed a cap of about eight on their own.

**Query:** Should works stop starting builds and planning while the owner queue is over a cap?

**Options:** a) (recommended, confidence medium - two works reached the same number independently, but it slows overnight throughput) Cap each work at about eight records awaiting acceptance or eight open queries. Pair the cap with a batched decision sitting by decision type and one at-screen checklist for each of sol and terra. b) Keep no cap, and only batch the sittings and checklists. c) Also let wording-only queries on triage records take the recommended option at medium unless Kris objects.

### BLIND-REVIEW - Make reviews actually blind

**Context:** Eight works credit blind review with their best catches. But ki.baseline-rollout found that each reviewer read `queries.md`, which shows the recommendation and its confidence. So every confidence lift may be anchored to the recommendation it was meant to check.

**Query:** Should reviewer briefs carry a masked copy of each query and keep `queries.md` out of the reviewer's reading?

**Options:** a) (recommended, confidence high - cheap, and it makes the standard's existing claim true) Yes. Reviewer briefs carry Context and Query only. `ki agent new` scaffolds the review brief that way. b) Leave things as they are, and record in each review that it was not blind.

### LAUNCH-DEFAULTS - Fix `ki agent` launch and control

**Context:** Six works lost turns to launching. `queue` printed help and queued nothing. `--repo` failed when it named the target repository. Prepared prompts failed with "has already run". A review started on the wrong model. Two accept runs stopped because the default footer forbids accepting. `send` failed with "invalid run". There is no `stop` or `dequeue` command.

**Query:** Should tools-ki take these as one bundle: per-role defaults, a footer chosen from the run's purpose, repository resolution, and working `queue`, `send`, `stop` and `dequeue`?

**Options:** a) (recommended, confidence high - every item has a cited failure and none is destructive) Yes, as one handoff to ki.tools-burndown, with per-role defaults and footer-from-purpose first. b) Fix only `send` and `queue` now, and leave defaults to the coordinators' launch lines.

### CLAIM-CHECK - Check premises and claims before acting

**Context:** Five works did wrong work from unchecked claims. KB-ACQUIRE-005 and 006 were cancelled on a wrong premise. Observatory briefs told runs to restart the service against its AGENTS.md. "Add something about it to the SoP" was run as METHOD-READ when Kris meant GFM. Two Summaries carried a wrong path and a wrong ownership claim.

**Query:** Should the coordination standard require a direct check of every path, ownership claim and instruction premise, plus a one-line read-back of any ambiguous direction, before a brief or Summary?

**Options:** a) (recommended, confidence high - each incident would have been caught, at the cost of one read) Yes. Also make briefs carry each target repository's standing rules by default. b) Require only the read-back of ambiguous directions.

### CLASS-FIX - Fix the class of a finding, not the instance

**Context:** KB-DOTFILES-UE-090 took four fix-and-review cycles, and one validator claim took three drafts, because each fix brief targeted only the cited lines.

**Query:** Should fix and revise briefs sweep for the whole class of a finding, and should review loops stop when no must-fix remains?

**Options:** a) (recommended, confidence high - both works proposed it on their own and it shortens loops) Yes. Should-fix items go to the owner's read. b) Sweep for the class, but keep looping until a clean review.

### GREEN-MAIN - Keep the harness's `main` green

**Context:** A harness edit made in the main checkout broke every island's pre-commit for two minutes. The estate hook migration shipped while the harness's own hook tests were failing (HOOK-TESTS), and baseline hook tests still block full-suite gates.

**Query:** Should a green harness `main` gate every run and every estate-wide rollout?

**Options:** a) (recommended, confidence high - an estate-wide blast radius justifies stopping the line) Yes. A red baseline stops the line, harness hook tests pass before any rollout, and harness edits are made off the shared main checkout. b) Gate only estate-wide rollouts on green.
