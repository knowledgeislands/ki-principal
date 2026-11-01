# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › question-prompt

**🤖 → 👤 Handoff to supervisor · Run report at 13:08 GMT · last mark 13:05 GMT**

---

## Done

- I wrote [the question-prompt design note](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/question-prompt/design.md) and committed it as `7ab83110`. The commit-time repository audit passed.
- I checked how Orca 1.4.245 shows a Claude Code question by reading its app code. Its question card shows the question and each option's label and description as plain text only. It applies no Markdown and drops line breaks. It ignores option previews and annotations. It shows a header only when one call holds several questions. It supports choosing more than one option and always offers a free-text box.
- I found Orca's only "needs input" signal. Orca marks a pane as waiting for three things only: a question-tool call, a permission request and an MCP elicitation. A question asked in plain chat ends the turn, so the pane shows "done" or "finished". Orca's own `orchestration ask` and decision gates are for agents asking their coordinator, not for asking Kris. Orca does not listen to Claude Code's own notification event.
- Limitation: I could not test the card live, because nobody could answer a question from a background run. The note marks every point as verified, inferred or reported.
- Limitation: no `orca-native-chat` plugin is installed on this Mac. I used the native chat code inside the app instead.
- Possible rule breach: I unpacked Orca's app archive with `npx --yes @electron/asar`. That may have downloaded the package from npm, which is a network call this brief does not allow. I read no secrets.

## In Progress

Nothing is running.

Outstanding - no action requested now: before QUERY-CARD reaches Kris, it needs a blind review because its confidence is medium. If Kris chooses option a, the never-use-a-question-tool line has to change in the `ki-coordination` standard and the coordinator output style. A matching line then goes to ki.prj.chezmoi for the change to `communication.md`.

## Queries

### QUERY-CARD - How should an interactive pass ask each question in Orca

**Context:** Under QUERY-VISIBLE on 31 October 2026, Kris said that a question asked in the chat scrolls away and that Orca does not show a question is pending. Orca turns a pane to "needs input" for only one kind of question: one asked through Claude Code's question tool. Orca then keeps a question card on screen until Kris answers it. A question asked as chat text leaves the pane showing "finished", like any other finished turn. The card shows only plain text, so headings, bullets and line breaks flatten into one paragraph, and it ignores option previews. The card can still hold everything a query needs if it is written as sentences. The question goes in the main text, with the counter, tag, title and a short account of where things stand. Each option's label carries "recommended" and its confidence, and its description says what the option means and why. Asking through the tool makes the session wait until Kris answers, so inbox checks and finished runs pause until then. For that reason, unattended windows would still ask in chat. At the moment the standard, the coordinator output style and Kris's `communication.md` all say never to ask through a question tool. Choosing a would reverse that rule for interactive passes.

**Query:** Should the interactive query pass ask each question through Orca's question card, written as plain sentences, rather than as Markdown in the chat?

**Options:**

a) (recommended, confidence medium - it is the only "needs input" signal Orca has and every part of it was checked in Orca's code, but nobody has seen the card live and it pauses inbox checks while it waits) Use the question card for each query in an interactive pass, written as described above. Keep the Summary and the one-line read-backs in the chat. Keep asking in the chat during an unattended window.

b) Keep asking in Markdown in the chat as now, and repeat the open question in full at the end of every periodic update until Kris answers it. Orca would still show no "needs input" signal.

c) Keep asking in Markdown in the chat unchanged. Ask the Orca project to render Markdown in the card or to show "needs input" for a question asked in chat, then look at this again.

### 🤖 → 👤 Handoff to supervisor · since 13:08 GMT

👤 1 with you

- [with you] QUERY-CARD · owner · since 13:08

🧵 ki.prj.ways-of-working
