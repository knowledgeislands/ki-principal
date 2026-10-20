# wow-ci-check

Goal: report the harness CI state on main, read-only.

Exception: the coordinator authorises read-only GitHub API calls for this run only (`gh run list`, `gh run view`), as an explicit exception to the no-remote rule. No other remote call, no edits, no commits.

Steps: in /Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness run `gh run list --branch main --limit 15`. Report the latest result of each workflow, and specifically whether `build` has run green on or after 1b8ab57b, 979e075a and 9c17df3c (check `git merge-base --is-ancestor`). For any red run, give the failing job and its first error line from `gh run view --log-failed`.

Report: one table of workflows and results, then any failure with its cause, and whether it is new or pre-existing. British English, ASCII hyphens only.
