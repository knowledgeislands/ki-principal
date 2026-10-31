# Brief: question-prompt

Work: ki.prj.ways-of-working. Authority: QUERY-VISIBLE, Kris, 31 October 2026, at the end of `decisions.md`. Read it there.

Problem: a question asked as chat text scrolls away, and Orca shows no "question pending" signal. The question tool (AskUserQuestion) does flag that Kris needs to answer, but in Orca it renders as one bold paragraph, and chat text written before the call appears only after the answer.

Investigate, read-only:

1. How Orca's native chat renders a Claude Code AskUserQuestion. Find out which fields it shows (question, header, option label, option description, option `preview`, `multiSelect`, annotations) and whether any of them render Markdown. Look in the Orca app bundle under `/Applications/Orca.app`, in `~/Library/Application Support/orca/` and in the installed `orca-native-chat` plugin and skills. Read code and assets only; read no secrets.
2. Whether Orca has another native "needs your input" signal a session can raise, for example a status, a badge, `orca orchestration ask`, or a notification.
3. Whether Claude Code offers anything else, such as notifications or hooks that set a waiting state.

Then propose the best way to put the full question (counter, plain-title heading, where things stand, numbered options with recommended, confidence and why) into the prompt box or an Orca input-needed signal, so that the question stays visible. Give a fallback if the box can't render Markdown, such as context in the option descriptions or previews. Say exactly what is verified versus inferred.

Write `design/question-prompt/design.md` in plain English, short, ending with one decision in the QUERY-TURNS shape. Commit it by explicit path and push fast-forward only.
