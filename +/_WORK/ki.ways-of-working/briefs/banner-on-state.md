# banner-on-state

Run for ki.ways-of-working in `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`, authorised by Kris on 2026-10-19 at 22:36 BST ("do it now").

## Rule (BANNER-ON-STATE)

Any coordinator reply that moves the mark, changes the work's state or answers where the work stands ends with the glyph banner, even when it is not a full report (Summary, recap, re-bootstrap, hold report). A plain answer that does none of these needs none. Background: a reply to "whats waiting on me? / mark" on a held work gave no banner, and Kris expected one.

## Task

1. Work in a fresh `git worktree` of the harness, not the main checkout: island pre-commit audits read the main checkout live, and a half-done edit there broke every island's commits tonight (22:12 to 22:14 BST). Fast-forward the main checkout only once everything passes.
2. Add the rule compactly to the `ki-coordination` coordinating-work standard's Banner section and the reply forms where they say when the banner appears; align the coordinator output style and any generated surface. Add it to the hook line only if it fits the 1,500-character test ceiling without weakening the existing clauses; otherwise leave the hook alone and say so.
3. Run the tests, type check and the repository's audits; regenerate surfaces. Commit by explicit path; pull with rebase and push fast-forward only when your own commits alone are stacked, else name the others. Never `--no-verify` or force-push. Remove the worktree afterwards.

## Report

Commits, where the rule landed (paths and lines), hook decision, checks, pushed or why not, queries with options.
