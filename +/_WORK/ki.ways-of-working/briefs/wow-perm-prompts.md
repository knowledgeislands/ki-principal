# wow-perm-prompts - stop runs clearing scratch, and name the shapes that prompt

## Goal

Land two decisions Kris agreed on 2026-10-25 in the KI Agentic Harness, in one run.

1. **PERM-PROMPTS-SCRATCH ("Close cleans up").** `ki-delegation`'s run packet contradicts itself. One sentence says "`ki agent close` refuses while the directory holds anything"; another records Kris's 20 October adoption of the temp directory "which `ki agent close` empties and removes". Remove the refusal sentence and say that a run never removes its temp directory (`$TMPDIR/ki-agents/<run>/<name>/`) and that `ki agent close` empties and removes it. Legal's scan traced 110 of 203 background-run `rm` denials to runs clearing that directory.
2. **PERM-PROMPTS-SHAPES ("Both standards").** In `ki-coordination` and `ki-delegation`, name the call shapes that trip Claude Code's built-in `rm` safety check under bypass mode, with their alternatives:
   - shapes: an `rm` with a glob, a shell-variable or `$(...)` target, or a target under a workspace directory, alone or inside a compound command or `sh -c`; `git worktree remove`; and a foreground `sleep` of 60 seconds or more;
   - alternatives: coordinators use `ki agent close` or a bounded run for removal, and runs use literal absolute paths or leave removal to the tool that made the thing.

   Add a note that the interactive cause is probable, not proven, until Kris reports a prompt's wording.

## Do

- Work in `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`, starting after wow-labels has pushed: pull first, then use a clean temporary clone of `origin/main` or the primary checkout if it is clean. Update the rubric criteria and examples the change touches, regenerate the generated surfaces (`ki dev skill generate ki-coordination --write` and any others reached), and run the tests and audits until they pass.
- Commit by explicit path as Conventional Commits ending with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`, pull with rebase and push fast-forward only.
- Append one line to `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/messages.md` asking tools-ki to confirm that `ki agent close` empties and removes a run's temp directory, and to make it do so if it doesn't, citing the harness revision. Append one REFRESH line naming the revision and both changes to `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/messages.md`. Commit and push both by explicit path.

## Do not

Change Claude Code or chezmoi settings (PERM-PROMPTS-SETTINGS is parked), change any other standard, release anything, force-push, use `--no-verify`, or touch another session's uncommitted files.

## Report

The owner report: Done with commits and checks, In Progress, and Queries, each with Context, Query and Options, the recommended option first with its confidence and reason.
