# Brief: interactive-queries

Work: ki.prj.ways-of-working, which owns `ki-coordination`. Authority: the IMPORTANT message INTERACTIVE-QUERIES, sent at Kris's request on 31 October 2026 and logged in this package's `decisions.md`. Read it there in full.

In `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`, change `ki-coordination`'s rule for taking queries interactively:

1. Ask exactly one decision per turn. A Summary may still list every open query, but interactive mode never batches.
2. Put the query in the chat as ordinary Markdown, not in a question tool: a `## <TAG>: <plain title>` heading, a short **Where things stand** section in bullets, then **The options** as a numbered list, with the recommended option first carrying its confidence in italics and a one-line _Why:_. Close with "Reply with 1, 2 or 3, or your own words." Then end the turn and wait.
3. Never use a question tool such as AskUserQuestion for this. Say why: in Orca its prompt renders as one bold paragraph, and chat text written before the call appears only after the answer.
4. Log each answer as it arrives, and only then ask the next.

Replace today's wording that allows "one or two at a time" and question tools. Regenerate the generated surfaces (`ki dev skill generate ki-coordination --write`), and run the banner test, the tests and the focused audit. Work in your own worktree, fast-forward `main`, commit by explicit path and push fast-forward only. Never force or skip hooks.

Then add one line to `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.chezmoi/messages.md`, in the Messages line shape. It asks for the matching change to `~/.local/share/chezmoi/dot_claude/communication.md`, replacing "through a question tool" with this rule, and says it waits for Kris's diff review before `chezmoi apply`. Commit that line alone and push fast-forward only.

Report in plain English.
