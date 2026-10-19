# query-review

Work: ki.ways-of-working (`/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/`). Read its `decisions.md` entries QUERY-REVIEW (2026-10-19 08:22 BST) and QUERY-REVIEW-STANDARD (19:48 BST) first; they are your authority.

## Task

1. In `ki-agentic-harness` (main checkout, not a worktree), add the QUERY-REVIEW rule to the `ki-coordination` standard, `skills/change-management/ki-coordination/references/standards-coordination.md`, under Owner report (beside Needs tags or the query shape), in Kris's words as decided: before a query reaches the owner, every medium- or low-confidence query, and any high-confidence query whose recommended course is destructive, goes to one blind review run on the strongest model at high effort (Codex where independence matters); agreement lifts the confidence one level and marks it `reviewed`; disagreement shows both views in the query. Cite the decision by its words and date. Add it to the generated `output-style` and `hook-line` sources only as far as the five hard rules and style length allow (a short clause, not a paragraph), and to `ki-delegation`'s run-report or footer-report source if a background agent raising a query should do the same. Add a rubric item if one fits.
2. Regenerate with `ki dev skill generate ki-coordination --write` (and `ki-delegation` if touched); run the repository gate; commit by explicit path with Conventional Commits; push fast-forward (only your own commits; name any other stacked commit in your report and do not push it).
3. In `ki-principal`, add one line at the top of each `messages.md` (below its `#` heading) of `+/_WORK/ki`, `ki.tools-burndown`, `ki.observatory`, `ki.specifications`, `ki.chezmoi`, `ki.mac-studio-setup`, `ki.baseline-rollout`, `ki.timelines`, and `/Users/krisbrown/workspaces/personal/acquire/+/_WORK/kb.regular.acquire-intake/messages.md`: `- IMPORTANT · 2026-10-19 <HH:MM> BST · from ki.ways-of-working · REFRESH: QUERY-REVIEW is now in the ki-coordination standard (<harness commit>): re-read it; from now on every medium- or low-confidence query, and any high-confidence destructive one, goes to one blind review run before it reaches Kris, including any queries already drafted and not yet sent.` Commit each repository by explicit path (`git commit -q -m ... -- <paths>`, never a bare `git commit`); push ki-principal and acquire fast-forward only if only your commits are stacked, otherwise name the stack in your report.

## Limits

Change nothing else. Do not touch ki-design or apps-knowledgeislands.info. Run Git with `-q`; never paste gate or Git output into the report.

## Report

Write the report to `~/.local/state/ki/agents/ways-of-working/query-review.report.md` in owner-report form (the ki-delegation run-report rule), with commits named, any stacked commits named, and any query.
