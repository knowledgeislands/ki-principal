# obs-smoke-baseline: compare the browser smoke check before and after KI-OBSERVA-VIS-041

Repository: /Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local. Owner authority: SMOKE-BASELINE a), acted on overnight under OVERNIGHT (high confidence, non-destructive).

obs-vis041-build delivered [KI-OBSERVA-VIS-041](</Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-041-git-view-replaces-repositories.md>) (commits fb456ef to d27363a). Under the headless Chromium shell its Git viewer flow passed, but other flows failed: a dimming timing failure in every view and Mermaid frames refused. Find out whether those failures come from the headless shell or from this work.

1. Install the full Chromium build for the repository's Playwright (`bunx playwright install chromium` or the repository's own documented way). Change no tracked file and no package.json.
2. Make a temporary detached worktree of 04a2ebb outside the repository (under $TMPDIR), install its dependencies frozen, and run `bun run self:test:browser` there. If the run needs the service port, follow how the script chooses its server; do not stop or restart the live service at 127.0.0.1:1675 except as the script itself does, and restore it with `launchctl kickstart -k "gui/$(id -u)/uk.me.kris.rig.observatory"` if you touch it.
3. Run the same on the primary checkout at current main (which includes d27363a).
4. Compare the failures flow by flow. Remove only the temporary worktree you made (`git worktree remove`), nothing else.
5. If a failure is new with VIS-041 and the fix is small and plainly within VIS-041's files, fix it, rerun, and commit by explicit path (`fix(...)` subject, trailer `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`); add a line to the record's Review section. Otherwise change nothing and report.

Do not push. Report as an owner report with heading `# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-smoke-baseline`, the bold form line, `---`, Done, In Progress, Queries. British English, ASCII hyphens only.
