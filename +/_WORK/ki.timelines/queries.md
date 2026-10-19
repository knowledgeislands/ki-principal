# ki.timelines queries

## Open

### FEED-HOME - Where a private base without a site publishes

since 2026-10-20 · from [tl-merge](/Users/krisbrown/.local/state/ki/agents/timelines/tl-merge.report.md) · held for blind review (tl-qreview)

**Context:** legal-principal and personal-principal have no site, and their dates are private. legal's include court dates. The brief proposed writing them into Kris's own Google or Microsoft calendar through `mcp-gsuite` and `mcp-m365`. The code shows neither can do that yet. Google's create tool takes only timed start and end values, and has no field for free/busy, all-day dates or a stable event key. The Microsoft server has no update tool and can only write to the default calendar. Whether a subscribed calendar counts towards free/busy is untested; both reviewers relied on memory of how the clients behave. Kris asked for sets people can subscribe to. A dedicated Google calendar has its own private subscription address, which would cover that, but this also comes from memory and is untested.

**Query:** How should private calendar sets be published?

**Options:** a) (recommended, confidence medium - honours "publish ... to subscribe to" once proved, keeps court dates off any public URL, and promises nothing the connectors cannot do yet; the coordinator will send this for blind review) Keep private sets unpublished in v1, shown in the base's generated view. Build account sync as a separate adapter after the connector work, prove it on a test calendar and then on a few personal dates, and use the provider calendar's private address for subscribing on other devices. b) Account sync now, as the brief proposed. This first needs the connector work. c) An unguessable feed URL on a public host, chosen base by base. Anyone who gets the URL sees every date. d) A private feed host behind a token-checking Cloudflare Worker. New infrastructure to build and secure.

### SKILL-NAME - The skill's name

since 2026-10-20 · from [tl-merge](/Users/krisbrown/.local/state/ki/agents/timelines/tl-merge.report.md) · held for blind review (tl-qreview)

**Context:** The naming decision ADR-KI-HARNESS-SKILLS-003 allows all three names, and none is taken. The brief said "timeline" clashes with `ki-diagrams`. The source shows otherwise: `ki-diagrams` never mentions timelines, though Archify does list timeline diagrams. "Calendar" is already the name of the `Calendar/` folder for daily and weekly notes in every base. Kris's own words were "a calendar with the milestones". Both reviews favour `ki-key-dates`.

**Query:** Which name should the skill take?

**Options:** a) (recommended, confidence medium - names the stored source rather than one output, and avoids both the clash with the `Calendar/` folder and the busy-calendar reading; the coordinator will send this for blind review) `ki-key-dates`. b) `ki-calendars`, matching Kris's words. c) `ki-timelines`, matching the Project's name.

### ADOPTION-ORDER - The order of adoption

since 2026-10-20 · from [tl-merge](/Users/krisbrown/.local/state/ki/agents/timelines/tl-merge.report.md) · held for blind review (tl-qreview)

**Context:** Kris named the first adopters as legal-principal, personal-principal and 5G Emerge. 5G already has the component and a host, so it can prove the extracted code behaves the same, but its data has no times, spans or private dates. legal has the most urgent dates, running to February 2027. The reviews agree on splitting legal into a local part and a sync part, and on testing any write to a real calendar on low-stakes data before court dates.

**Query:** In what order should the bases adopt the skill?

**Options:** a) (recommended, confidence medium - keeps Kris's three adopters, gets legal its view early with no credentials, and keeps the first real calendar write away from court dates; the coordinator will send this for blind review) 5G first, as a pilot proving the feeds come out unchanged. Then 5G's timeline merge and legal's local timeline. Then the sync adapter, proved on a test calendar and then on a few personal dates. legal's sync comes last. b) The brief's order: 5G, then all of legal, then personal-principal. c) legal first, for its urgent dates.

### TIMED-BUSY - A busy item with a time but no end

since 2026-10-20 · from [tl-merge](/Users/krisbrown/.local/state/ki/agents/timelines/tl-merge.report.md) · held for blind review (tl-qreview)

**Context:** In the calendar standard, a timed event with no end takes no time at all, so marking it busy blocks nothing. Kris settled "never invent a time or duration". legal already records a numeric `duration_minutes` field, which can supply a real end. Both reviews raised the gap.

**Query:** How should a busy item with a time but no end be handled?

**Options:** a) (recommended, confidence medium - keeps "never invent a duration" while making busy mean something; the coordinator will send this for blind review) The checks require a real end, either an end time or `duration_minutes`, and fail the item without one. b) Write it as an all-day busy item, which blocks the whole day. c) Allow it and write it with no duration, which blocks nothing.

## Parked

None.
