# wow-ci-timeout

Goal: stop the harness CI Test step burning six hours when it hangs. wow-ci-check found two six-hour Test hangs in the last 15 runs of /Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness (19 Oct 23:16 UTC on 185624b0, 20 Oct 04:19 UTC on ba4055ef), each cancelled at the job limit, with orphaned bun processes; the cause is unknown. Its report is ~/.local/state/ki/agents/ways-of-working/wow-ci-check.report.md.

Authority: Kris, 20 October 2026 22:03 BST: "Is there anything more that you can do by yourself without me? ... roadmap down".

Steps: in a worktree, add a tight timeout-minutes to the build workflow's Test step (or job), sized from recent green run durations with a generous margin. Spend at most a bounded look (about 20 minutes) for the hang's likely cause in the test suite (open handles, hook tests spawning shells); fix it only if the cause is clear and local, otherwise name the suspects in the report. Run the harness's local checks. Fast-forward local main.

Constraints: British English, ASCII hyphens only, they/them. Harness and tools-ki edits only in a worktree, fast-forwarded into local main; commit by explicit path; do not push. Never --no-verify or force-push. Create no new records; route follow-ups as a messages.md line. Raise anything needing Kris as a query (Context, Query, lettered Options, recommendation first with confidence).

Report: change made, timeout chosen and why, suspected cause, commit SHAs.
