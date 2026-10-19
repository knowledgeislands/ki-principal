# tl-qreview2 - blind review of two ki.timelines queries

You are a blind reviewer for the ki.timelines work package in /Users/krisbrown/workspaces/knowledge-islands/ki-principal, under the ki-coordination standard's Query review section. Read-only: write nothing except your report. Do not read `+/_WORK/ki.timelines/queries.md`, `state.md`, `decisions.md`, `design/timelines-skill-report.md`, either `design/*review*.md` or anything in `~/.local/state/ki/agents/timelines/`; they carry recommendations you must stay blind to. You may read `design/survey.md`, `design/timelines-skill-brief.md`, `design/timelines-skill-design.md`, the harness at /Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness (skills, `docs/decisions/`), /Users/krisbrown/workspaces/knowledge-islands/mcp-gsuite and mcp-m365, and the integration notes in /Users/krisbrown/workspaces/personal/personal-principal and ki-principal `Admin/Governance/` for which calendar Kris actually uses.

For each query, check what you can directly, then give your own recommended course (one listed or your own), a confidence of high, medium or low, and a one-line reason, saying what you verified directly and what you took on trust.

## SKILL-NAME - The skill's name

Context: Kris asked for "a calendar with the milestones" and for each knowledge base to "publish one or more calendar sets to subscribe to". The skill owns the canonical dated items, a generated timeline view and subscribable feeds. The naming decision ADR-KI-HARNESS-SKILLS-003 allows all three candidates and none is taken. Every base already has a `Calendar/` folder for daily, weekly and monthly notes. Archify lists timeline diagrams.

Query: Which name should the skill take?

Courses:

- `ki-timelines`, matching the Project's name.
- `ki-calendars`, matching the subscribable sets.
- `ki-key-dates`, naming the canonical source.

## PROVIDER-FIRST - Which calendar provider the first sync adapter targets

Context: Under FEED-HOME, account sync comes after connector work and is proved on a test calendar before any real dates. That makes rollout step 4 belong to `mcp-gsuite`, `mcp-m365` or both.Google can already pick a calendar and update an event by its id, but it lacks all-day writes, transparency and a created-by marker. Microsoft has no update tool, no calendar picker and no busy-status field, so it needs more work.Which calendar Kris actually schedules from is not known. Nothing needs this answer until steps 2 and 3 are done.

Query: Should the first calendar-writing connector work and the adapter proof target Google, Microsoft or both?

Courses:

- Leave it open until step 4 is due.
- Both together, so the acceptance matrix covers both from the start, at roughly twice the connector work.
- Microsoft first, through `mcp-m365`, if Kris's real scheduling happens in Outlook.
- Google first, through `mcp-gsuite`, with Microsoft only if the acceptance matrix or Kris's scheduling tool calls for it.

**Report** to `/Users/krisbrown/.local/state/ki/agents/timelines/tl-qreview2.report.md` and nowhere else: a `# KI > Foundations > Timelines › tl-qreview2` heading, then one `##` section per query with your course, confidence, reason and what you verified. Run tools quietly and keep it short.
