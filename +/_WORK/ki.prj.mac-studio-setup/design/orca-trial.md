# Orca trial log - ki.prj.mac-studio-setup

Trial rule ORCA-HOST, set by Kris on 29 October 2026: for this Project, dispatch runs through Orca orchestration instead of `ki agent`; every other `ki-coordination` rule still applies, and the work package stays the record. Host: sol. Orca app 1.4.244, local runtime.

## Model comparison

| Orca concept | ki agent counterpart | Matched | Fell short |
| --- | --- | --- | --- |
| Run `run_0de85069bc1d`, created 2026-10-30 00:17 GMT, one per Project | the work package, plus `ki agent status` across its runs | A durable namespace and coordinator inbox bound to this terminal | Holds no state, queries or decisions; the package still carries them |
| Task | the brief in `briefs/<run>.md` | | not yet observed |
| Dispatch | one `ki agent launch` run | | not yet observed |
| Heartbeats | the run state folder's beat and `ki agent status` step | | not yet observed |
| ask / reply | a query in the run report, received at the end | | not yet observed |
| worker_done | the run report and its completion | | not yet observed |

## Stored on this machine, not in Git

- `~/Library/Application Support/orca/` (about 974 MB): `orchestration.db` (Runs, Tasks, Dispatches, messages), `agent-session-journal.db`, runtime, device, pairing and E2EE key files, and `codex-runtime-home/`.
- `~/.orca/` (about 24 KB).
- The Run's coordinator handle is this Claude Code terminal's Orca handle; a resume after restart needs `run-use --id run_0de85069bc1d`.

## Lost if the checkout were deleted

- Nothing from Orca: its state sits outside the checkout. What would be lost is anything committed only locally and unpushed, as with `ki agent`.

## Lost if Orca's state were deleted

- The Run, Task and Dispatch history and any ask/reply thread not copied into a report or `decisions.md`; to be checked at the first worker_done.
