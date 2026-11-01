# Brief: ephemeral Orca worker threads in recents lists

Work: ki.prj.orca-evaluation. Read-only investigation. Orca worker under the Project's Run.

## Why

Kris, 1 November 2026: the ChatGPT app's recent list is full of threads that begin "You are working inside Orca, a multi-agent IDE. You are a dispatched worker." They are ephemeral worker sessions, not thinking threads like coordinator chats, so once finished they should be deleted and should not crowd recents. "How does Orca suggest we deal with that?"

## Find out

1. What Orca itself does or recommends: read `orca orchestration --help` and the help for `worker-release`, `worker-stop`, `run-*` and any archive, cleanup or retention verb; Orca's settings and docs on worker sessions; and Orca's shipped app code on sol (read-only) for what release does to the agent's own session (it reported "archive transcript [captured]"). Check Orca's public GitHub issues (stablyai/orca) for existing requests about worker sessions polluting agent history, without posting.
2. Where those threads come from: Codex workers started by `worker-start --agent codex` write Codex sessions, which the ChatGPT desktop app lists. Find how they reach the list (local `~/.codex/sessions` versus synced cloud conversations), and whether Claude workers do the same in Claude's apps.
3. Supported ways to hide or remove them: Codex CLI or app archive and delete (for example any `codex` archive or delete command, `~/.codex/archived_sessions`), ChatGPT's archive and delete, any setting to exclude non-interactive or `exec` sessions from history, and whether Orca can start Codex workers in a mode that does not record history. Say which are supported and which would mean editing app state by hand (do not recommend hand edits; Orca's own state was damaged that way on 31 October).
4. Do not delete, archive or change anything. List, but do not open the contents of, a sample of the affected sessions to confirm the pattern and count.

## Report

Write ~/.local/state/ki/agents/ki-prj-orca-evaluation/worker-threads.report.md: what Orca suggests (or that it suggests nothing), where the threads come from, the supported options ranked, and a query for Kris in owner-report form (tag WORKER-THREADS, Context, Query, lettered Options with a) recommended and a confidence with reason) covering both clearing the existing threads and stopping new ones. Plain British English. Then call worker_done with the report path.
