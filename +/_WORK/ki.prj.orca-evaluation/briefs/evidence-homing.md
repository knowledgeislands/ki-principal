# Brief: unit 1 - home the Orca evidence

Work: ki.prj.orca-evaluation, ki-principal at /Users/krisbrown/kis/knowledge-islands/ki-principal. Orca worker under the Project's Run.

## Goal

Make `+/_WORK/ki.prj.orca-evaluation/design/orca-trial.md` the single, current trial log of what is known about running Knowledge Islands work through Orca, so the Orca launcher proposal (unit 2) can rest on it alone.

## Sources

- The current `design/orca-trial.md` and `design/orca-trial-plan.md`.
- Run reports in ~/.local/state/ki/agents/ki-prj-orca-evaluation/: trial-plan, thread-nesting, sidebar-restore, orca-labels, stock-take, review-upstream, file-card-bug.
- Kris's observations of 1 November (decisions.md, TRIAL-SHAPE): workers nest under the coordinator's row; Orca's wait command works as the coordinator's wake in a Claude Code chat; a chat coordinator can release a finished worker; survival of a worker when its coordinator chat ends is untested, a detail for first live use.
- This thread's own use on 1 November: a new chat session could not use the Run made by the previous session ("caller not bound"), so a new Run was made; heartbeats each arrive as an inbox delivery Orca prompts the owner about, so the waiter acknowledges them; worker_done arrives as a delivery to acknowledge; `worker-release --dispatch <id>` closes the terminal and captures the transcript; four workers (Claude and Codex) ran from the chat without permission prompts.
- Learnings routed by HNR email routing, 30 October (git history of this package's messages.md, line ORCA-DISPATCH-LEARNINGS): heartbeats become owner-visible noise and `check --wait --types` still returned on them; `--worktree current` workers share the Git index with other sessions, and a pathspec commit (`git commit -- <paths>`) avoids touching others' staged files; parallel workers editing the same notes had to be serialised; the ask path worked well; Run ids are found by an objective starting with the work id; worker-start's receipt nests ids, so read them from worker-list.
- Lesson routed from rig-terra, 31 October (line ORCA-MOVE-LESSON): hand-editing Orca's SQLite state stopped Orca starting, recovered with `orca profile state rollback --backup <id>`; a project removed and re-added gets a new identity and loses its chats; for a repository move, leave a link at the old path and never hand-edit Orca state.
- Upstream: the question-card bug filed as stablyai/orca#36830.

## Do

1. Rewrite `design/orca-trial.md` as a concise trial log: what was tried, what is proved (with date and source), what is still open, the known Orca gotchas, and upstream reports. Plain British English, ASCII hyphens only, no em or en dashes.
2. Replace the body of `design/orca-trial-plan.md` with a short note that the plan is superseded by the two-unit shape Kris adopted on 1 November (TRIAL-SHAPE, ORCA-SKILL-NOW), pointing to orca-trial.md.
3. Do not commit, stash or push; the coordinator commits at receive. Touch no other file.

## Report

Write ~/.local/state/ki/agents/ki-prj-orca-evaluation/evidence-homing.report.md: what changed, anything you could not verify, and any question only Kris can answer as a query (tag, Context, Query, Options with a recommended option and confidence). Then call worker_done with the report path.
