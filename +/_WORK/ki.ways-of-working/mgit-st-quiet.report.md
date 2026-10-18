# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › mgit-st-quiet

**🤖 → 🧑 Handoff to supervisor · Run report at 11:07 BST**

---

## Done

- `mgit st` is now quiet for clean checkouts level with their upstream, and the change is live. The live read-only run over the workspace closed with `mgit: 23 repositories: 20 quiet, 3 with output, 0 failed`. The three shown were ki-agentic-harness, ki-principal and tools-ki, each with local changes.
- Cause: mgit already had this rule for `git status`, but `st` is a Git alias for `status -sb`, so the rule never applied. mgit now looks up the alias, and any alias that expands to `status` follows the same rule. A checkout that is ahead, behind, diverged, detached, without an upstream, with changes or untracked files, or that fails is still shown.
- To see every checkout, use the existing `-v/--verbose` or `--json`. I added no new flag, so it can't clash with [KI-TOOL-MGIT-CLI-025](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-025-escape-hatch-flag-names.md). The completions are unchanged.
- Updated the README, man page, running-commands guide, MGIT-WS-025 spec and changelog. Added a new Bats test that failed on the old code, covering clean, behind, detached, untracked and no-upstream checkouts, an alias that is not `status`, and the `-v` view.
- The full tools-mgit gate passes: repository audit (0 failures, 3 warnings, all pre-existing in files I didn't touch), shellcheck, `bash -n`, all 124 Bats tests, mandoc lint and `git diff --check`. The work is commit `eb276dd` in tools-mgit, pushed to `main`.
- Record: folded into [KI-TOOL-MGIT-CLI-024](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-024-quiet-normal-git-output.md) (quiet normal Git output). Its "no-change messages" part stays in draft. Net open records: tools-mgit 0 new; no other repository touched.
- Install: `~/.local/bin/mgit` is a symlink to the tools-mgit checkout, so the push made the fix live. No release, tap update or `chezmoi apply` was needed.
- Two slips, both fixed straight away: a stray test command created `/tmp/.git` (removed within seconds), and I ran `git stash` in tools-mgit against the rules. The stash held only my own two uncommitted files; I popped it at once, and the stash list is empty.
- I wrote this report only to this state path, as the progress protocol requires, so no ki-principal commit was made.

## In Progress

Nothing.

## Queries

None.
