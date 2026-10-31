# Brief: card-rule-2

Work: ki.prj.ways-of-working, which owns `ki-coordination`. Authority: CARD-PATTERN settled, logged at the end of `decisions.md` on 31 October 2026. Read it, and check what run `card-rule` already wrote (its harness commit) so you build on it.

In ki-agentic-harness, make the interactive-query rule describe the settled pattern exactly:

1. **First reply.** Start a short background timer, about 5 seconds. Then end the reply with its last text: the one-line read-back of the previous answer, if there is one, followed by the next query's context (`Query <n> of <total>`, the `## <TAG>: <plain title>` heading, **Where things stand** bullets).
2. **Second reply,** woken by the timer, holds only the card: a one-line title with the counter and the plain question; short option labels, the recommended one first carrying "(recommended, <confidence> confidence)"; descriptions of one or two sentences, the recommended one opening with "Why:"; and the free-text box for Kris's own words.
3. **After the answer:** log it, then go back to step 1.
4. **Why:** Orca folds everything in a reply except its last text, and doesn't show text written after an answer within the same reply. Keep a plain chat fallback for runtimes with no card or no wake.
5. **At the end of the set:** the mark, then the Summary.

Keep everything else. Regenerate the surfaces, and run the banner test, the tests and the audit. Work in your own worktree, fast-forward `main`, commit by explicit path and push fast-forward only. Report in plain English.
