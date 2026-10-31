# Brief: card-rule

Work: ki.prj.ways-of-working, which owns `ki-coordination`. Authority: CARD-PATTERN and CARD-LOOP, Kris, 31 October 2026, in `decisions.md`. Read them, the card-test findings there, and `design/question-prompt/design.md`.

In ki-agentic-harness, amend the interactive-query rule (INTERACTIVE-QUERIES, QUERY-TURNS, QUERY-SET-MARK) so that each query is asked like this:

1. **Context first, in the chat.** The counter (`Query <n> of <total>`), a `## <TAG>: <plain title>` heading and **Where things stand** as short bullets, written as ordinary Markdown in the chat.
2. **Then a short question card** (`AskUserQuestion`):
   - the title is one line: the counter and the plain question;
   - each option has a short label, with the recommended one carrying "(recommended, <confidence> confidence)";
   - each option description is one or two sentences, with the recommended option's starting with its "Why:";
   - Kris's free-text box serves for "your own words";
   - two related questions may share one card, each with a short header.
3. **After the answer:** log it, then reply with a one-line read-back and end the reply. Ask the next query in the following reply, never in the same one.

State why, in a sentence: Orca's card drops line breaks in its title (reported to Orca), while chat text renders fully and shows above the card. Keep the counter, the set-end mark and Summary, and the read-back rule.

Remove the ban on question tools, but keep the plain-text fallback for runtimes with no card. Regenerate the surfaces, and run the banner test, the tests and the audit. Work in your own worktree, fast-forward `main`, commit by explicit path and push fast-forward only. Report in plain English.
