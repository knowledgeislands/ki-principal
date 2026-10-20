# obs-vis041-unpushed: select unpushed commits by reachability

Repository: /Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local. Record: [KI-OBSERVA-VIS-041](</Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-041-git-view-replaces-repositories.md>), Awaiting review. Acted on overnight under OVERNIGHT as a high-confidence, non-destructive correctness fix.

A blind review (~/.local/state/ki/agents/observatory/obs-review-5.report.md) found that packages/evidence/src/repositories.ts (around line 387 to 410) splits the recent log at the ahead count to get the "unpushed" and "earlier" lists, and the Review section (around line 165) says that equals selecting by upstream reachability. It does not when merges interleave history: the unpushed commits need not be the log's leading segment.

1. Verify the claim with a test: a temporary repository whose branch merges upstream work so that an unpushed commit is not in the leading segment.
2. If it holds, select unpushed commits by reachability (`git log @{upstream}..HEAD` or the equivalent through the existing git bridge and its fallback) and earlier commits as the remainder, keeping today's behaviour where there is no upstream. Keep the ten-commit list exactly as it is: whether to change it (TEN-COMMITS) is with Kris.
3. Correct the Review section's sentence. Run tests, typecheck, lint and the roadmap audit; restart the service with `launchctl kickstart -k "gui/$(id -u)/uk.me.kris.rig.observatory"` and check <http://127.0.0.1:1675/> answers.
4. Commit by explicit path (`fix(...)` subject, trailer `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`); keep the record at Awaiting review. Do not push.

If the claim does not hold, change nothing and say why. Report as an owner report with heading `# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-vis041-unpushed`, the bold form line, `---`, Done, In Progress, Queries. British English, ASCII hyphens only.
