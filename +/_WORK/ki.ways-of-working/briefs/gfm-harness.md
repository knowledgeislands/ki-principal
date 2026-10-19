# gfm-harness

Run for ki.ways-of-working in `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`, authorised by Kris on 2026-10-19 at 22:00 BST: "Do all recommended". Read `~/.local/state/ki/agents/ways-of-working/gfm-scope.report.md` and `gfm-review.report.md` first; the decisions are GFM-ORDER a), FLAVOUR-FIELD a), GFM-LINK-FORM a), GFM-ENACT a), METHOD-READ-RUBRIC a).

## Task

1. `ki-authoring` `standards-markdown.md`: add the "Markdown flavour" clause from the scoping report, amended by the review: GFM preferred; other flavours supported and never failed on; a file you edit is converted (whole file, through the converter once it exists; a file the converter refuses is flagged or gets a recorded exception) - keep this sentence in its own paragraph, as TOUCH-SCOPE is still with Kris; batches may be rewritten whole in a dedicated change; constructs with no GFM equivalent are decided, never dropped. House link form: note-relative paths in angle brackets, Obsidian's `%20` normalised. No per-note flavour field. Remove the KB exception from "Links".
2. `ki-repo-kb` "Linking within a base" and LINK-1: GFM preferred, wikilinks tolerated; LINK-1 becomes "every internal link resolves, exact case", covering wikilinks and Markdown links, with fixtures for angle-bracket and `%20` destinations, reference definitions and escaped table aliases.
3. Fix `ki-decision-records` `bodyLinks` (angle-bracket destinations with spaces, reference definitions) and `ki-repo-kb-activities` `%20` decoding, without global percent-decoding.
4. Reword the `ki-authoring`, `ki-skills` and `ki-subagents` evals that test the old KB exception; make the source-mirror script strip Markdown links too.
5. `ki-work-package` rubric: flag a `state.md` `method_read` value that is not a short harness revision (METHOD-READ-RUBRIC), with a fixture.
6. Regenerate surfaces as the repository requires; run its tests, type check and audits. Commit by explicit path in coherent commits; pull with rebase and push fast-forward only when your own commits alone are stacked, else name the others and do not push. Never `--no-verify` or force-push. Follow the harness's own record rules.

## Report

Commits per step, tests and audits, pushed or why not, anything left, queries with options.
