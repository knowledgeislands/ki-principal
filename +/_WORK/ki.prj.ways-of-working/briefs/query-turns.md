# Brief: query-turns

Work: ki.prj.ways-of-working, which owns `ki-coordination`. Authority: Kris's QUERY-TURNS words, given on 31 October 2026 and logged verbatim at the end of this package's `decisions.md`. They refine the INTERACTIVE-QUERIES rule already in harness `0af7ab73`.

In `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`, amend `ki-coordination`'s interactive-query rule so that it matches Kris's template exactly:

- a counter line, `Query <n> of <total>`;
- the `## <TAG>: <plain title>` heading;
- **Where things stand**, as a few short bullets, enough to decide without scrolling back;
- **The options**, numbered, each with a bold name, the recommended one carrying _(recommended, <confidence> confidence)_ and a one-line _Why:_;
- the closing line, "Reply with 1, 2 or 3, or your own words.";
- then stop and wait;
- log the answer as it arrives and read it back in one line before asking the next;
- the total is the open count when the pass starts, and if an answer raises a new query, add it to the total and say so.

Regenerate the surfaces, and run the banner test, the tests and the focused audit. Work in your own worktree, fast-forward `main`, commit by explicit path and push fast-forward only.

Then update this work's own unacted INTERACTIVE-QUERIES line in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.chezmoi/messages.md` to carry the same template, replacing only that line. Commit it alone and push fast-forward only.

Report in plain English.
