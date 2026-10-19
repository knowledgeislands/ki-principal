# ki.timelines queries

## Open

### SKILL-NAME - The skill's name

since 2026-10-20 · from [tl-merge](/Users/krisbrown/.local/state/ki/agents/timelines/tl-merge.report.md) · review disagrees (tl-qreview), held for Kris

**Context:** The naming decision ADR-KI-HARNESS-SKILLS-003 allows all three names, and none is taken. The brief said "timeline" clashes with `ki-diagrams`. The source shows otherwise: `ki-diagrams` never mentions timelines, though Archify does list timeline diagrams. "Calendar" is already the name of the `Calendar/` folder for daily and weekly notes in every base. Kris's own words were "a calendar with the milestones". Both reviews favour `ki-key-dates`.

**Query:** Which name should the skill take?

**Options:** a) (recommended, confidence medium - review disagrees: the merge favours naming the stored source and avoiding the `Calendar/` folder; the blind review prefers `ki-calendars`, which names the subscribable sets you asked for, a folder name reserving no skill concern) `ki-key-dates`. b) `ki-calendars`, matching Kris's words. c) `ki-timelines`, matching the Project's name.

### PROVIDER-FIRST - Which calendar provider the first sync adapter targets

since 2026-10-20 · from [tl-decide](/Users/krisbrown/.local/state/ki/agents/timelines/tl-decide.report.md) · held for blind review (tl-qreview2)

**Context:** Under FEED-HOME, account sync comes after connector work and is proved on a test calendar before any real dates. That makes rollout step 4 belong to `mcp-gsuite`, `mcp-m365` or both. Both reviews checked the connector code. Google can already pick a calendar and update an event by its id, but it lacks all-day writes, transparency and a created-by marker. Microsoft has no update tool, no calendar picker and no busy-status field, so it needs more work. One review also notes, from prior knowledge and not verified, that a dedicated Google calendar has its own secret address, which would give subscriptions on Kris's other devices. Which calendar Kris actually schedules from is not known. Nothing needs this answer until steps 2 and 3 are done.

**Query:** Should the first calendar-writing connector work and the adapter proof target Google, Microsoft or both?

**Options:** a) (recommended, confidence medium - Google has fewer gaps in code both reviews checked, but which calendar Kris schedules from is unknown and the secret-address benefit is unverified) Google first, through `mcp-gsuite`, with Microsoft only if the acceptance matrix or Kris's scheduling tool calls for it. b) Microsoft first, through `mcp-m365`, if Kris's real scheduling happens in Outlook. c) Both together, so the acceptance matrix covers both from the start, at roughly twice the connector work. d) Leave it open until step 4 is due.

## Parked

None.
