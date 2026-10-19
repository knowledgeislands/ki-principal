# tl-qreview - blind review of four ki.timelines design queries

You are a blind reviewer for the ki.timelines work package in /Users/krisbrown/workspaces/knowledge-islands/ki-principal, under the ki-coordination standard's Query review section. Read-only: write nothing except your report. Do not read `+/_WORK/ki.timelines/queries.md`, `state.md`, `decisions.md`, `design/timelines-skill-report.md` or any run report in `~/.local/state/ki/agents/timelines/`; they carry the recommendations you must stay blind to. You may read `design/survey.md`, `design/timelines-skill-brief.md` and the sources: /Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3 (apps/site), /Users/krisbrown/workspaces/legal/legal-principal (Command Centre Guide, FR Timeline, dated Items), /Users/krisbrown/workspaces/personal/personal-principal, /Users/krisbrown/workspaces/knowledge-islands/mcp-gsuite and mcp-m365 (calendar tools), and the harness skills in /Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness.

Settled by Kris: the calendar is milestone-centred and a span never takes busy time; per-item `busy` defaults to free; one source of dated items generates views and feeds; optional time per item with one time zone per set, never inventing a time or duration; one skill whose code lives in its own `scripts/` in the harness.

For each query, check what you can directly, then give your own recommended course (one of the listed courses or your own), a confidence of high, medium or low, and a one-line reason, saying what you verified directly and what you took on trust.

## FEED-HOME - Where a private base without a site publishes

Context: legal-principal and personal-principal have no site, and their dates are private. legal's include court dates. The brief proposed writing them into Kris's own Google or Microsoft calendar through `mcp-gsuite` and `mcp-m365`. The code shows neither can do that yet. Google's create tool takes only timed start and end values, and has no field for free/busy, all-day dates or a stable event key. The Microsoft server has no update tool and can only write to the default calendar.Kris asked for sets people can subscribe to. A dedicated Google calendar has its own private subscription address, which would cover that, but this also comes from memory and is untested.

Query: How should private calendar sets be published?

Courses:

- A private feed host behind a token-checking Cloudflare Worker. New infrastructure to build and secure.
- An unguessable feed URL on a public host, chosen base by base. Anyone who gets the URL sees every date.
- Account sync now, as the brief proposed. This first needs the connector work.
- Keep private sets unpublished in v1, shown in the base's generated view. Build account sync as a separate adapter after the connector work, prove it on a test calendar and then on a few personal dates, and use the provider calendar's private address for subscribing on other devices.

## SKILL-NAME - The skill's name

Context: The naming decision ADR-KI-HARNESS-SKILLS-003 allows all three names, and none is taken. The brief said "timeline" clashes with `ki-diagrams`. The source shows otherwise: `ki-diagrams` never mentions timelines, though Archify does list timeline diagrams. "Calendar" is already the name of the `Calendar/` folder for daily and weekly notes in every base. Kris's own words were "a calendar with the milestones".

Query: Which name should the skill take?

Courses:

- `ki-timelines`, matching the Project's name.
- `ki-calendars`, matching Kris's words.
- `ki-key-dates`.

## ADOPTION-ORDER - The order of adoption

Context: Kris named the first adopters as legal-principal, personal-principal and 5G Emerge. 5G already has the component and a host, so it can prove the extracted code behaves the same, but its data has no times, spans or private dates. legal has the most urgent dates, running to February 2027.

Query: In what order should the bases adopt the skill?

Courses:

- legal first, for its urgent dates.
- The brief's order: 5G, then all of legal, then personal-principal.
- 5G first, as a pilot proving the feeds come out unchanged. Then 5G's timeline merge and legal's local timeline. Then the sync adapter, proved on a test calendar and then on a few personal dates. legal's sync comes last.

## TIMED-BUSY - A busy item with a time but no end

Context: In the calendar standard, a timed event with no end takes no time at all, so marking it busy blocks nothing. Kris settled "never invent a time or duration". legal already records a numeric `duration_minutes` field, which can supply a real end.

Query: How should a busy item with a time but no end be handled?

Courses:

- Allow it and write it with no duration, which blocks nothing.
- Write it as an all-day busy item, which blocks the whole day.
- The checks require a real end, either an end time or `duration_minutes`, and fail the item without one.

**Report** to `/Users/krisbrown/.local/state/ki/agents/timelines/tl-qreview.report.md` and nowhere else: a `# KI > Foundations > Timelines › tl-qreview` heading, then one `##` section per query with your course, confidence, reason and what you verified. Run tools quietly and keep it short.
