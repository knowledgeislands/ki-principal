# Brief: blind review of one owner query

Read-only. Write only ~/.local/state/ki/agents/ki-prj-orca-evaluation/review-upstream.report.md, then call worker_done with that path. Do not read any queries.md, decisions.md or report under +/_WORK/ki.prj.orca-evaluation/ or ~/.local/state/ki/agents/. You may read Orca's shipped app code or `orca --help` to check the facts below.

Review this independently: reach your own view from the context and the options before considering any other view, and say where you disagree.

**Context:** A Project evaluating Orca (an agent-orchestration desktop app, version 1.4.245) for a personal knowledge-and-agents setup has gathered five items of feedback for Orca's maintainers. On 31 October the owner authorised raising one: Orca's native chat question card drops line breaks in its title text, so multi-line questions arrive as one run-on bold line. Four await the owner: (2) while a chat's turn has ended but a background task is live, the worktree row puts "Monitoring background tasks" before the chat's name, so every waiting coordinator chat reads "Monitoring background tas..." at normal widths and no setting changes it; (3) hiding a sidebar item is one click but restoring it is only in Settings > Appearance > Sidebar with no hint, and the Mobile hide message points to the wrong Settings page; (4) there is no supported read-only settings export, so a checker comparing settings across two Macs would have to read Orca's SQLite profile database; (5) a session Orca did not start cannot declare a parent or display name, so it cannot nest under its coordinator - lower value now the owner has adopted Orca as the main launcher. The owner said on 1 November that Orca is "the way forwards". Sending is outward-facing and public.

**Query:** Which items go to Orca, and in one request or more?

**Options (unranked):**

- Send all five in one request, item 5 marked lower priority.
- Send the card bug and the name-first row only; drop the others.
- Send the authorised card bug alone now; hold the rest.

Give: your recommended option, confidence (high/medium/low) with a one-line reason, any option you would add, and any fact above you found wrong.
