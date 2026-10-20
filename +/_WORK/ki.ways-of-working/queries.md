# ki.ways-of-working queries

## Open

### CHECKOUT-ISOLATION - Stop sessions colliding in shared checkouts

**Context:** The costliest theme, raised by eight of nine works with notes. Staged files were swept into other works' commits (`e0489e42`, `0836bcae`); one run's half-saved edit made another run report a failure; the unpushed stack in ki-principal reached 62 commits, 11 from one work. A per-session commit index stops the sweeping but not lock waits or false audit failures; worktrees stop both but need serial merging and do not clear an unpushed stack. The blind review disagreed with take-stock: it chose worktrees everywhere.

**Query:** How should sessions and runs be kept apart in a shared checkout?

**Options:**

a) (recommended, confidence medium - take-stock's view: fixes the worst incidents now; worktree cost on knowledge-base repositories untested) A `ki` commit helper with its own index per session that checks the commit landed; worktrees for code-repository build runs; serialise record-editing runs in one knowledge base; audits read committed state only. b) (blind review's view, confidence medium - separate trees and indexes stop both contamination and in-flight audit failures) Every coordinator session and writing run gets its own worktree in every repository, with serial, verified merging into `main`. c) One owning session per checkout per night, and no technical change.

### OOS-WAKE - A wake for the coordinator that survives its session

**Context:** Five works raised it; three gaps cost about 219 minutes in total (reviews finished 00:35 and were read at 02:04; a waiter overslept 00:33 to 01:43; this work's OVERNIGHT-AUTONOMY lapsed after 00:27). Runs survive; the coordinator's waiter dies with its session. A host scheduler (option b) would need a change to the Techne Programme Focus, which excludes unattended or scheduled agents on either host.

**Query:** What should wake a coordinator when its session is gone?

**Options:**

a) (recommended, confidence high - reviewed: the blind review agreed; fits the existing launcher and needs no policy change, though resuming a coordinator headlessly is new) A detached `ki agent` watcher per work, started with an expiring autonomy window, that wakes on run completion and on new `messages.md` lines and resumes the coordinator with the work's send line. b) A launchd job on the agent host through Rig checking every ten minutes in autonomy windows, after amending the Techne Programme Focus.

### OWNER-QUEUE - Cap building while acceptance lags

**Context:** Five works raised it. 21 records await your acceptance (16 Observatory, five Mac Studio). ki.chezmoi has 20 and ki.baseline-rollout 15 unresolved queries, now parked. Two works independently proposed a cap of about eight; the number is a reversible choice, not a measured optimum.

**Query:** Should works stop starting new builds and planning while their owner queue is over a cap?

**Options:**

a) (recommended, confidence high - reviewed: the blind review agreed, with corrected counts) Cap each work at about eight records awaiting acceptance or eight open queries for new builds and planning, keeping acceptance fixes and backlog-clearing work allowed; pair it with batched decision sittings by type and one at-screen checklist each for sol and terra. b) No cap; only the batched sittings and checklists. c) As a), and also let wording-only triage queries take the recommended option at medium unless you object.

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

## Parked

- NO-GATE - Project shape commit gate; reviewed, a) `ki repo audit --skill ki-repo` staged, check-only.
- GFM-HOSTING-RULES - harness protected `main` declaration; a) `branch-protection = true`, awaiting blind review.
- HARNESS-TRIAGE - eight harness triage dispositions from lane-triage; awaiting blind review.
- PRINCIPAL-TRIAGE - OPS-014 to Next, prune GOV-035; awaiting blind review.
- PKGLESS-GATE - keep the package-less pre-commit gates in homebrew-tap and ki-specifications and give each concrete shape an explicit content owner in the harness hooks contract; taken with NO-GATE on resume.
