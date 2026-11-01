# Brief: unit 2 - the Orca launcher proposal

Work: ki.prj.orca-evaluation, ki-principal at /Users/krisbrown/kis/knowledge-islands/ki-principal. Orca worker under the Project's Run. Authority: Kris, 30 October (ORCA-SKILL: "after two or three units, crystallise the trial into a proposal for an Orca launcher under ki-delegation and ki-coordination") and 1 November (ORCA-SKILL-NOW a: draft it now as a design note in this package, then hand it to ki.prj.ways-of-working to adopt).

## Read

- `+/_WORK/ki.prj.orca-evaluation/design/orca-trial.md` (the trial log, the evidence base) and this package's decisions.md (ORCA-REACH, WAKE-SESSION, WAKE-DURABLE, ORCA-OPTIN, TRIAL-SHAPE).
- ki.prj.ways-of-working: `design/orca-subagents/design.md`, `design/orca-fit.md` and its decisions.md for ORCA-QUEUE, ORCA-PLACEMENT, ORCA-CLOSE-OUT, ORCA-ROUTING, ORCH-NAME-DISPATCH, HOOK-STASH and Part B.
- The current method at ki-agentic-harness main: ki-coordination `references/standards-coordination.md` and the ki-delegation background-runs standard.
- `orca orchestration --help` and each subcommand's `--help`, read-only, to verify every command the proposal names.

## Produce

`+/_WORK/ki.prj.orca-evaluation/design/orca-launcher.md`, a proposal of at most about two pages, for the adapter `ki-delegation-orca`: when Orca is the launcher (reach under ORCA-REACH) and when `ki agent` stays; start (run-create, worker-start, worktree choice, agent choice); the wait verb under WAKE-SESSION, including acknowledging heartbeats inside the waiter; status, stop, release and close-out; recovery after a coordinator session changes (a new Run, since an old Run is bound to its session); queueing; ids under ORCA-ROUTING; brief and report paths; how a question only Kris can answer travels (point to OF-OWNER-ASK in Ways of working, do not decide it); commit rule (point to HOOK-STASH, do not decide it); what stays in Knowledge Islands (the work package is the record); open points (worker survival when the coordinator chat ends). Mark each statement as proved (with trial-log source), designed elsewhere (with its owner) or proposed. Plain British English, ASCII hyphens only.

Do not commit, stash or push; touch no other file; send nothing.

## Report

Write ~/.local/state/ki/agents/ki-prj-orca-evaluation/launcher-proposal.report.md: what the proposal says in a few lines, anything unverified, any query only Kris can answer (tag, Context, Query, Options, recommended with confidence), and a draft message line for ki.prj.ways-of-working asking it to adopt the proposal. Then call worker_done with the report path.
