# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-shape-review-claude

**🤖 → 👤 Handoff to supervisor · Run report at 01:50 BST · last mark 02:10 BST (23 October)**

---

## Done

- Wrote and committed the Claude review of the model-shape brief, [model-shape-review-claude.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/model-shape-review-claude.md), commit `ccf88dd3`; the commit hook's repository audit passed for the committed path.
- What the review found: the brief's main idea holds, that a package is where the work lives and a thread is whoever is working on it. It agrees with 11 of the 17 points as written or with small limits, and disagrees with 3, 10, 14 and 16 in whole or in part.
- Five conflicts with current text that the brief's table leaves out: the Work Process note and the work-package standard both say "Only sends and the supervisor's receives commit"; the coordination Glossary says a session "works at most one piece of coordinating work"; the turn budget limits reads to "the work package", singular; both fast-forward-only pull rules; and "commits and pushes" in Committing the work folder.
- Corrections: point 14's "pull with rebase" cannot work in a shared checkout that has uncommitted changes, so the review gives a fast-forward-then-commit-then-push order instead; `self` is not a valid holder value; and the existing word "thread" needs redefining rather than adding.
- Suggested simpler approaches: record stewardship in `work.md`'s existing `worker` field; keep `covers` as the main State of play's list of what it covers and check each `parent` against it; and wait for the pilot before choosing a merge mechanism for `messages.md`.
- Things the brief missed: how runs already in flight are handed over when stewardship changes; dropping the stale-thread rule, because the existing stuck view already covers it; what `parent` means for ad hoc work; and trying host requirements in `ki.chezmoi` rather than in the Valle Armonia pilot.
- The review gives a view and a confidence level on each of the brief's six open questions.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- I took COMMIT-CADENCE's wording from the brief without checking it, because this brief told me not to read `decisions.md`. The review's point 14 correction applies to that wording too.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 01:50 BST

👤 0 with you

- [committed] model-shape review (claude)

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
