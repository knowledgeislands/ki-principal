# Orca trial log - ki.prj.mac-studio-setup

Trial rule ORCA-HOST, set by Kris on 29 October 2026: for this Project, dispatch runs through Orca orchestration instead of `ki agent`; every other `ki-coordination` rule still applies, and the work package stays the record. Host: sol. Orca app 1.4.244, local runtime.

The trial ended after one unit. On 30 October Kris returned this Project's dispatch to `ki agent` (KI-AGENT-DISPATCH), and the trial evidence passed with ORCA-HOST to ki.prj.orca-evaluation (ORCA-HANDOVER).

## Unit run

plan069, one Codex worker started with `orchestration worker-start --worktree current --agent codex` and waited on with `orchestration check --wait`. It planned KI-TOOL-RIG-CORE-069 under `ki-plan` and left it at draft (tools-rig `9297c9c`), Ready blocked only on an attended sol probe. No system change.

## Model comparison

| Orca concept | ki agent counterpart | Matched | Fell short |
| --- | --- | --- | --- |
| Run `run_0de85069bc1d`, created 2026-10-30 00:17 GMT, one per Project | the work package, plus `ki agent status` across its runs | A durable namespace and coordinator inbox bound to this terminal | Holds no state, queries or decisions; the package still carries them |
| Task | the brief in `briefs/<run>.md` | One task carried the plan069 brief | The brief still had to live in the package for the record |
| Dispatch | one `ki agent launch` run | One dispatch, one Codex worker in the current worktree | Shares the checkout, so Git write windows had to be granted by ask (PLAN069-GIT) |
| Heartbeats | the run state folder's beat and `ki agent status` step | Periodic heartbeats sent by the worker during planning and verification | Sent by the worker turn by turn; no background heartbeat loop, so a long step is silent |
| ask / reply | a query in the run report, received at the end | Asynchronous asks answered mid-run (PLAN069-AUDIT, PLAN069-GIT); the first ask's result was recovered after an interrupted turn by resuming its existing message ID, without a duplicate question | The hook-policy ask (PLAN069-HOOK) timed out after ten minutes unanswered and escalated; Kris answered it in chat instead |
| worker_done | the run report and its completion | One worker_done settled the dispatch | Reported `failed` although the planning had succeeded: publication of the report was blocked by the brief's no-stash rule against lint-staged's backup stash in the pre-commit hook. Kris granted a bounded exception for the report-only commit, "a bounded exception, not a general change to the no-stash rule", and the report was published as an owner-authorised follow-up with no redispatch |

## Stored on this machine, not in Git

- `~/Library/Application Support/orca/` (about 974 MB): `orchestration.db` (Runs, Tasks, Dispatches, messages), `agent-session-journal.db`, runtime, device, pairing and E2EE key files, and `codex-runtime-home/`.
- `~/.orca/` (about 24 KB).
- The Run's coordinator handle is this Claude Code terminal's Orca handle; a resume after restart needs `run-use --id run_0de85069bc1d`.

## Lost if the checkout were deleted

- Nothing from Orca: its state sits outside the checkout. What would be lost is anything committed only locally and unpushed, as with `ki agent`.

## Lost if Orca's state were deleted

- The Run, Task and Dispatch history and the raw ask/reply threads. Checked at the first worker_done: the run report copied each ask's query, options, answer and message IDs, and the decisions log recorded the outcome, so no decision depends on Orca's state alone.

## Lessons for the evaluation

- A brief's no-stash rule collides with a pre-commit hook that stashes as a backup; a brief for a hooked repository needs the bounded exception up front or a publication step outside the worker.
- An ask with no answer within ten minutes escalates; an attended coordinator must answer within that window or expect the question to arrive by another route.
- worker_done's outcome reflects the last step, not the unit; a `failed` needs reading against the report before any redispatch.
