# obs-app044-fix: factual corrections to KI-OBSERVA-APP-044

Repository: /Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local. Edit only [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md). Do not change its status, priority or decision; RESTRUCTURE stays open with Kris.

A blind review (obs-review-4, report at ~/.local/state/ki/agents/observatory/obs-review-4.report.md) checked the record against the code. Verify each point yourself, then apply what the code bears out:

1. The renderer is `renderShell` (apps/site/src/page.ts); correct the name wherever the record gives another.
2. The redirect table: `shell.ts` reads raw IDs, including on history navigation, and does not call `resolveInstrument`; the CLI in `main.ts` rejects a supplied ID whenever resolution changes it. Record in Steps or Files touched that each consumer must be adapted explicitly: canonicalise known aliases in the shell, keep unknown-ID rejection in the CLI, and verify old addresses, filters, report parameters and Beacon destinations as each consolidation lands.
3. Waiting for you: the Review queue already derives its handoff rows from Work's with-you view and links into Work, so renaming Review does not depend on DESIGN-WORK. Correct any statement that it does.
4. Keep the Shaping promotion condition (step 3 shipped before Ready) as it stands.

Run the repository's roadmap audit and Markdown lint; commit by explicit path with a `docs(roadmap):` subject and the trailer `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`; do not push. Report as an owner report with heading `# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-app044-fix`. British English, ASCII hyphens only.
