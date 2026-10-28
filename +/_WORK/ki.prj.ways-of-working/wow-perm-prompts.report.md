# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-perm-prompts

**🤖 → 👤 Handoff to supervisor · Run report at 08:21 GMT · last mark 01:07 GMT**

---

## Done

- PERM-PROMPTS-SCRATCH, "Close cleans up", landed in the `ki-delegation` run packet: the refusal sentence is gone, a run never removes `$TMPDIR/ki-agents/<run>/<name>/`, and `ki agent close` empties and removes it, with the 110 of 203 denials cited. The run-prompt skeleton's scratch line says the same.
- PERM-PROMPTS-SHAPES, "Both standards", landed: a new `ki-delegation` [Permission prompts](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md#permission-prompts) subsection and the `ki-coordination` tool-calls rule and output-style source name the shapes, the coordinator and run alternatives, and the probable-not-proven note; the COORD-4 review prompt and both sources notes follow.
- Generated surfaces regenerated: `output-styles/ki-coordinator.md` and the `ki-coordination` rubric changed; the `ki-delegation` rubric regenerated unchanged.
- Checks: `bun run test` passed (1468 tests); `bunx tsc --noEmit` passed; focused audits `ki-coordination`, `ki-delegation`, `ki-skills` and `ki-repo-harness` passed. A first `ki-skills` run failed PORT-1 on three unqualified Claude Code references; the wording now compares runtimes explicitly and the rerun passed.
- Harness commit `c4b423c7`, `docs(skills): stop runs clearing scratch and name the shapes that prompt`, in the clean primary checkout; pulled fast-forward and pushed, local `main` level with `origin/main`.
- Knowledge Islands Principal commit `bbb14383`, `docs(work): queue close-cleans-up confirmation and perm-prompts refresh`: one CLOSE-CLEANS-UP line in `ki.tools-burndown`'s queue asking tools-ki to confirm `ki agent close` empties and removes the temp directory, make it so if not, and align the launcher's footer, which still says "refuses while it holds anything"; one IMPORTANT REFRESH line in `ki`'s queue naming the revision and both changes; pulled fast-forward and pushed.
- The commit trailer names Claude Fable 5.1, the model the launch record shows, under the standard's commit-trailer rule, rather than the Opus 5.5 line copied in the brief.
- Not touched: Claude Code and chezmoi settings (PERM-PROMPTS-SETTINGS parked), any other standard, and the other session's untracked `wow-review-release.report.md` in the ki-principal work folder.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- tools-ki's answer on CLOSE-CLEANS-UP waits in `ki.tools-burndown`'s queue. Until the launcher footer changes, every new run still reads that close "refuses while it holds anything".

## Queries

### WORKTREE-REMOVE - the Isolation rule still tells runs to run a shape that prompts

**Context:** The brief names `git worktree remove` among the shapes that trip the safety check, and it is now written so in both standards. The `ki-delegation` Coordination section's Isolation and Integration bullets still instruct a run to remove each worktree it created with `git worktree remove` before `DONE`, and Kris's global Claude instructions name `git worktree remove` as a safe alternative. The new subsection leaves the Isolation bullet untouched, so a run in a worktree now meets two rules that pull apart. The brief said not to change any other standard, and the Isolation bullet is a different rule in the same standard, so it was left alone.

**Query:** Should worktree removal move from the run to `ki agent close`, with the run reporting the worktree path it leaves behind, or should `git worktree remove` on a literal absolute path be named the one accepted exception?

**Options:**
a) (recommended, confidence medium - the temp-directory fix worked by moving removal to close, and worktrees already live in the state folder close removes, but whether close prunes the primary checkout's worktree metadata is unverified) Move worktree removal to `ki agent close`, with a tools-ki line asking it to run `git worktree remove` and `git worktree prune` against the primary checkout at close, and amend the Isolation and Integration bullets in a follow-up run.
b) Name `git worktree remove <literal absolute path>` the one accepted exception in the Permission prompts subsection and leave the Isolation bullet as it is, accepting that it may still prompt.
c) Leave both as they are until Kris reports a prompt's wording and the cause is proven.
