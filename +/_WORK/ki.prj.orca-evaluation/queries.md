# ki.prj.orca-evaluation queries

## Open

### RESET-DUP - Level the primary checkout after the duplicate publish

**Context:** The trial plan and the resolve-push brief were published by cherry-pick (origin/main 50217fff and c92b3ec1) because main had diverged. The primary ki-principal checkout still holds the originals, f233597c and 5615a3eb, which `git cherry` confirms are patch-identical to the published ones, so local main is ahead 2 and behind 3 and no session in that checkout can pull fast-forward. The only other local change is this package's own resolve-push brief edit. The coordinator may not reset its own checkout without your approval.

**Query:** May the primary ki-principal checkout be levelled with `git reset --keep origin/main`?

**Options:**

a) (recommended, confidence high - both local commits are verified duplicates of published ones and `--keep` refuses to touch any uncommitted change it would lose; pending blind review) Yes: run `git reset --keep origin/main` in the primary checkout through a bounded run, then pull and push as usual.

b) No: leave it, and resolve it by a merge commit instead, which keeps the duplicates in history.

### ORCA-OPTIN - This package opts in to Orca dispatch for the trial

**Context:** ORCA-REACH (30 October) lets a package use Orca only after a logged decision, and only on attended Macs. Until that decision, ki.prj.orca-evaluation launches through `ki agent`. The plan needs Orca for units 1 to 3, all on sol, with you present, in a new Run for this Project (the Mac Studio Run `run_0de85069bc1d` would not be reused).

**Query:** Does ki.prj.orca-evaluation opt in to Orca dispatch for its trial units?

**Options:**

a) (recommended, confidence high - it is exactly the bounded opt-in ORCA-REACH provides for and the plan keeps every bound) Opt in for the trial units only: sol, attended, one new Run. The opt-in ends when the ORCA-SKILL proposal is received or at the 6 November ORCA-REACH follow-up, whichever comes first. All other work in this package stays on `ki agent`.

b) Opt in for all of this package's dispatch on attended Macs until you revoke it.

c) Do not opt in yet. Wait for the ORCA-FIT notes and the second brief's line to arrive first.

### TRIAL-UNITS - The units and their order

**Context:** The plan proposes three units, all real work this package owns. Unit 1 (WAKE, legs A and B) proves `check --wait` in Claude Code and Codex while doing the Orca setup inventory. Unit 2 (LIVE) maps Orca's recovery, queue, ack and status verbs and commits that map in ki-principal. Unit 3 (SKILL, optional) drafts the ORCA-SKILL proposal under Orca. Leg B needs you to open a Codex session on this package. Units 1 and 2 should land before 6 November.

**Query:** Do you adopt units 1, 2 and 3 in that order, with unit 3 optional?

**Options:**

a) (recommended, confidence medium - units 1 and 2 cover WAKE-SESSION and the plan069 failure, but whether to dogfood the proposal is a judgement call) Run 1A, 1B and 2. Then decide on unit 3, or draft the ORCA-SKILL proposal through `ki agent`, once unit 2's evidence is in.

b) Run all three in order, with unit 3 under Orca as planned.

c) Run unit 1 only, then come back with its evidence before anything else.

### TRIAL-PUBLISH - How a trial worker publishes in ki-principal

**Context:** ki-principal's pre-commit hook runs lint-staged, which creates and drops a backup stash. In plan069, a no-stash rule in the brief collided with that stash. The run's `worker_done` read `failed` although the work had succeeded, and you then granted a bounded exception for the report-only commit. Units 2 and 3 each produce a design note, and the trial workers share the checkout with other sessions.

**Query:** How should units 2 and 3 publish their notes?

**Options:**

a) (recommended, confidence medium - it tests the worker-commit path the adapter needs while keeping the exception narrow and stated up front) Each brief carries a bounded exception from the start. The worker commits its own note by explicit path inside a write window granted by ask, and the repository's hook may create and drop lint-staged's backup stash. The worker itself never runs `git stash`. The coordinator pushes at receive.

b) No worker commits. The worker writes the note and its report, and the coordinator commits both at receive.

### TRIAL-ASK - How a question only you can answer travels

**Context:** An Orca ask blocks the worker. It times out after 10 minutes by default (30 at most), and a question left unanswered at timeout stays pending and can be resumed by message id. In plan069, an ask timed out after ten minutes and escalated, and you answered it in chat instead. The ORCA-FIT draft's OF-OWNER-ASK has not been handed over yet; its recommended option ends the worker's attempt with a blocking query.

**Query:** During the trial, how does a worker raise a question only you can answer?

**Options:**

a) (recommended, confidence medium - it keeps the ask for what the coordinator can answer and needs no one to stay attentive for half an hour) The coordinator answers its own asks with `--timeout-ms 1800000`, resuming by message id on timeout. A question only you can answer ends the attempt: the worker raises it as a blocking query, `worker_done --outcome failed` names its tag, and the coordinator records it in `queries.md` and retries after you answer.

b) The worker keeps the ask open while the coordinator relays it to you, and resumes the same message after each 30-minute timeout.

### TRIAL-PRACTICE - Provisional working practice until the ORCA-FIT notes arrive

**Context:** The units need a working rule for ids, specifications, liveness and reports. The ORCA-FIT draft recommends one for each: ids go on a `state.md` Now line; the specification is the full rendered prompt; liveness comes from Orca heartbeats only; and reports go outside the repository, named by `--report-path`. That draft has not been handed to this package. The plan uses these rules for the trial only and decides none of the open choices.

**Query:** Do the units run on the ORCA-FIT draft's recommended practice as a provisional, trial-only rule?

**Options:**

a) (recommended, confidence medium - it lets the trial generate evidence for those choices without settling them early) Yes, provisionally and for the trial only. The units' evidence then goes back to the ORCA-FIT choices when the notes arrive.

b) No. Wait for the ORCA-FIT notes and settle those choices before any unit runs.

## Parked

None.
