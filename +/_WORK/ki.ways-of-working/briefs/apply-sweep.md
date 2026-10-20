# Apply Kris's sweep answers (20 October)

Nobody else is working tonight. Read `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md` (last two entries) and the sweep note `design/roadmap-sweep.md` in that folder, section `## Reviewed course`, plus `/Users/krisbrown/.local/state/ki/agents/ways-of-working/sweep-review-2.report.md`.

1. Accept under `ki-accept`, quoting Kris's words, then prune under `ki-work-roadmap`: KI-OBSERVA-VIS-022, -APP-045, -VIS-041, -VIS-043, -VIS-044, -APP-046; KI-DESIGN-TOK-001, -MAP-001, -OBS-015, -SYM-001, -TIL-001; KI-TOOL-RIG-CLI-027, KI-TOOL-RIG-CORE-065, -066.
2. Prune every other record across the Knowledge Islands repositories that is already accepted (done) or cancelled and still present, as `ki-work-roadmap` allows.
3. Merge KI-MCP-M365-TOOL-020 into KI-MCP-M365-TOOL-018 (target takes goal and steps; folded record cancelled as merged). Leave the KI-HARNESS-GOV-196 merge to harness-batch.
4. Convert to `messages.md` lines and cancel the records: KI-HARNESS-GOV-216 and KI-HARNESS-GOV-226 to ki.ways-of-working; KI-HARNESS-GOV-222 to ki.timelines (a line already went in ki-principal `20e696d2`; do not duplicate); KI-TOOL-KI-CLI-151 as a standing line to ki.tools-burndown; KI-TOOL-RIG-DIST-011 to the agent-host work; narrow KI-TOOL-RIG-CORE-064 and send its recurring scan to ki.chezmoi as an Activity line. Work packages live in `ki-principal/+/_WORK/<id>/`.
5. Cancel KI-TOOL-RIG-CORE-057 as won't do (idea kept in its Project note) and KI-TOOL-RIG-CLI-026 (Idea line on the Rig theme page), keeping both records.
6. Knip: one line to ki.tools-burndown's `messages.md` naming the harness owner for the new-configuration Knip scaffolding; return KI-TOOL-KI-CLI-167 to awaiting review only if its packet and gates hold (run them).
7. Drop ki-principal `stash@{0}` and `stash@{1}` after confirming each is fully on `main` (17 October Rig Decision 80, in `a3156df3`; 19 October `state.md` line).

Commit each repository by explicit path. Pull with rebase and push fast-forward only, pushing only commits made tonight by this programme; if another session's commits are stacked, do not push that repository and say so. Never `--no-verify` or force-push. CAPTURE-GATE: no new records. HOOK-GUARD: no `ki repo conform` without `--dry-run`. Edit tools-ki only through a worktree, never its primary working copy (`ki` runs from it). British English, ASCII hyphens. Report per repository: what changed, commits, pushed or not.
