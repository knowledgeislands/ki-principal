# Harness: STYLE-STALE re-anchoring step

Nobody else is working tonight; Kris, 20 October, set OVERNIGHT-BURNDOWN. Kris answered STYLE-STALE a) on 18 October: "do all the recommended items, we just need to move forwards".

Repository `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`. After a compaction, the `ki-coordination` "Re-anchoring after compaction" steps must re-read `output-styles/ki-coordinator.md` from disk beside the standard and the work package, and the file wins where it differs from the loaded style. Make the compact pointer (the `SessionStart` compact hook text) and the output style's re-anchoring paragraph say the same thing. Regenerate with `ki dev skill generate ki-coordination --write`.

Work in a worktree on `run/harness-style`, fast-forward local `main` after the gates pass (tests, tsc, rubric check, focused audits). Do not push: other sessions' commits are stacked. No record needed (owner answer). Never `--no-verify` or force-push. CAPTURE-GATE: no new records. HOOK-GUARD. British English, ASCII hyphens. Report: changes, commits, checks.
