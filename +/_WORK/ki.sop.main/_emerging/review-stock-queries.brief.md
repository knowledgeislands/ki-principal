# review-stock-queries (blind review)

Independent review: you have not seen anyone's recommendation; give your own for each. Do not read any `discussions.md`, `decisions.md`, `*.report.md` or `*.findings.md` in a `+/_WORK/` folder; you may inspect repositories read-only.

## BRANCH-SWEEP - Clear merged branches and the worktrees of finished runs

**Context:** Every repository is level with GitHub, but finished runs left branches and working copies behind. Merged into `main` and safe to remove by Git's own check: ki-agentic-harness `finished-tidy`, `quiet-listen` and `rename-paperclip`; tools-ki `wow-rel-0141`; tools-rig `run/wow-night-rig-048-f` and `run/wow-night-rig-056-e`; the remote `ways-of-working-learn` in apps-knowledgeislands.info. Most still have a worktree (a second working copy of the repository) under `~/.local/state/ki/agents/` or `$TMPDIR`, from Ways of working runs that `ki agent status` no longer lists. I did not check those worktrees for uncommitted files.

**Query:** Should one housekeeping run remove the merged branches and their worktrees?

**Options (unranked):**

- Leave them until each owning Project closes.

- One bounded run checks each worktree is clean, removes clean ones with `git worktree remove` and their merged branches with `git branch -d`, and lists any dirty one for you without touching it.

## RESUME-SPECS - Resume Portable specifications

**Context:** [ki.prj.portable-specifications](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.portable-specifications/state.md) has been paused since 20 October, released only when Kris says resume. Its draft 0.8 specifications passed six blind reviews, the last finding nothing, and its two parked queries, SPEC-TEXT and HOMING-EDITS, are both recommended at high confidence. Resuming means planning KI-HARNESS-GOV-229 and KI-HARNESS-GOV-230 to Ready in the harness, which the summary-model and emerging-only chain also edits. Timelines and Baseline rollout are paused the same way, with two and fifteen parked queries.

**Query:** Should Portable specifications resume now, with the other two paused works left as they are?

**Options (unranked):**

- Keep all three paused until the open method queries are settled.

- Resume Portable specifications only: put SPEC-TEXT and HOMING-EDITS to you, then plan its harness records after the harness chain finishes.

For each: your choice, confidence and a two-line reason. Read-only; no commits. Write it as your run report.
