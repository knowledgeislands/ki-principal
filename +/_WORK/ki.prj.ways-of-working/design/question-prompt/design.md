---
note_type: streams/design
status: draft - October 2026
work: ki.prj.ways-of-working
run: ki-prj-ways-of-working
agent: question-prompt
written_at: 2026-10-31
author: Written with Claude
---

# Question prompt: keeping a pending question visible in Orca

Kris, 31 October 2026 (QUERY-VISIBLE): a question asked as chat text scrolls away under later updates, and Orca shows nothing to say a question is waiting. This note looks at what Orca and Claude Code can do about it and proposes one way forward. Read-only investigation of Orca 1.4.245 on this Mac.

## What Orca does with a Claude Code question

**Verified** by reading Orca's app code (`app.asar`, the native chat question card and its parser):

- **Question text** shows as the card's title: one paragraph of small bold text. It is plain text, not Markdown, and line breaks are not kept, so headings, bullets and bold all flatten into one run of words. This is the "one bold paragraph" Kris saw.
- **Header** shows only when one call asks several questions, as a short tab label above the card. With one question it is not shown.
- **Options** show as numbered rows. Each row has the **label** in normal text and, under it, the **description** in smaller grey text. Both are plain text, no Markdown, line breaks lost. The option list scrolls if it is taller than half the window.
- **Preview** is dropped. Orca reads it only to know which keys to send back to Claude Code; it never displays it.
- **multiSelect** works: rows toggle on and off.
- **Annotations** are not read.
- **Free text**: there is always a "Type your answer" box, so "or your own words" still works.
- Number keys 1 to 9 pick an option; Escape folds the card away but keeps it.
- **Waiting signal**: when Claude Code calls the question tool, Orca marks the pane as **waiting** ("needs input"). It does the same for a permission request and for an MCP elicitation, and for nothing else. Orca can send a desktop notification on these status changes.
- **Plain chat question**: when a turn ends with a question in chat text, Orca sees only the end of the turn and marks the pane **done** ("finished", "Task complete"). Nothing distinguishes it from any other finished turn.

**Reported, cause not verified**: chat text written before the question tool call appears only after the answer. The code suggests the card replaces the live turn while it waits, but I did not trace this end to end.

**Not found**: no `orca-native-chat` plugin is installed on this Mac (not under `~/.claude`, Orca's application data or Orca's installed skills). The native chat code inside the app is the source used here.

## Other signals

- **`orca orchestration ask` and decision gates** (verified from the CLI help): these let a worker agent ask its _coordinating agent_ and block. They do not ask Kris and do not raise the pane's waiting state. Not useful here.
- **Terminal bell** (verified string "Bell in <worktree>: Attention requested"): Orca notifies on a bell from a terminal. A chat session has no clean way to ring it. Inferred, not tried.
- **Claude Code hooks** (verified from `~/.claude/settings.json`): Orca installs its own hooks for prompt, tool, stop, permission and elicitation events. It does not listen to Claude Code's `Notification` event, so Claude Code's own "waiting for input" notice does not change Orca's status. A hook of our own could only fake one of Orca's events, which would be fragile and is not proposed.

So the **only** native way to put "question pending" on an Orca pane today is a real question tool call.

## Proposal

Use the question tool for each query of an interactive pass, with all of the query's content packed into the fields Orca does show, as plain sentences. Keep the Markdown query in the chat out of it, because Orca would only show it after the answer.

| QUERY-TURNS part | Where it goes in the question tool |
| --- | --- |
| `Query <n> of <total>` and the tag | start of the question text: "Query 3 of 17 · HOLD-SCOPE." |
| Plain title | next sentence of the question text |
| Where things stand | two to four short sentences in the question text, separated by " · " since line breaks are lost |
| The question itself | last sentence of the question text |
| Option name, recommended, confidence | option label, for example "Keep it narrow (recommended, high confidence)" |
| What the option means and _Why:_ | option description, one or two sentences, "Why:" leading the reason on the recommended option |
| "Or your own words" | Orca's free-text box, already there |
| Header | the tag, kept to 12 characters; only shown if a call ever holds several questions |

Rules that go with it:

- One question per call, as QUERY-TURNS already says; no previews, since Orca drops them.
- No chat text before the call. After the answer, log it and read it back in chat in one line, then ask the next.
- The Summary, and every query in it, stays as Markdown in chat, unchanged.
- In an unattended window, keep asking in plain chat text: a question tool call blocks the session, so inbox wakes and finished runs cannot be acted on until Kris answers. Inferred from how Claude Code waits on the tool; not tested.
- This reverses the current "never ask through a question tool" line in the `ki-coordination` standard, the coordinator output style and `communication.md`. Kris's own `communication.md` already describes the label-carries-confidence, description-gives-reason shape for question prompts, so the field mapping matches it.

**Fallback if packing is too cramped**: if a query's context is too long for a readable card, put a one-line question in the card and the context in each option's description, so that the reason sits under the choice it supports. Previews are not a fallback in Orca, because it does not show them.

**Not yet tested live**: I could not raise a question card from a background run with nobody to answer it. The first interactive pass under this proposal is the test; if the card reads badly, the coordinator falls back to chat Markdown and says so.

## Decision for Kris

Query 1 of 1

## QUERY-CARD: How should an interactive pass ask each question in Orca

**Where things stand**

- A question in chat text scrolls away, and Orca shows the pane as "finished", not "needs input".
- The question tool is the only thing that makes Orca show "needs input" and keep a card on screen until answered.
- Orca's card shows plain text only: no headings, bullets or line breaks, and it ignores option previews.
- Asking through the tool blocks the session until answered, so it pauses inbox checks while the card is up.

**The options**

1. **Question card, packed** _(recommended, medium confidence)_: use the question tool for each interactive query, with counter, tag, title and where things stand as plain sentences in the question, and each option's label carrying recommended and confidence and its description carrying what it means and why. Chat stays for the Summary and read-backs; unattended windows still ask in chat. _Why:_ it is the only native "needs input" signal Orca has, and every field it uses is verified; medium because the layout has not been seen live and it blocks inbox checks while waiting.
2. **Chat Markdown, restated**: keep asking in chat Markdown as now, and repeat the open question in full at the end of every periodic update until it is answered. No "needs input" signal in Orca.
3. **Wait for Orca**: keep chat Markdown unchanged and ask the Orca project to render Markdown in the card or to show a "needs input" state for a plain chat question, then revisit.

Reply with 1, 2 or 3, or your own words.
