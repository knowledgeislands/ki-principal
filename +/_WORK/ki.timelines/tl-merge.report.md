# [Foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Timelines](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/timelines.md) › tl-merge

**🤖 → 👤 Handoff to supervisor · Run report at 23:52 BST · last mark 19:03 BST**

---

## Done

- Wrote the [merged report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.timelines/design/timelines-skill-report.md) and committed it locally as `3ccaaf3d`, not pushed; the commit hooks and repository audit passed.
- Every dispute between the two reviews was settled by re-reading the sources: the 5G site code, legal's Command Centre Guide and FR Timeline schema, the Google and Microsoft calendar connector code, and the harness skills.
- Both reviews keep the brief's core: one skill, one dated-item model, `busy` off by default, and two kinds of source.
- The main change is that private publication is not ready. Neither calendar connector can do the sync the brief assumed, and the claim about how subscribed calendars affect free/busy has not been checked. Private sets therefore stay unpublished in v1 until a separate sync adapter is proved.
- Other fixes to the model: permanent logical UIDs, with 5G's host suffix kept; handling for clock-change days; "today" judged in each calendar's own time zone; and legal's timeline built as a view of its existing Command Centre artifact.
- Re-reading legal's Guide turned up something neither review found: legal already records `duration_minutes`, which can give a timed busy item a real end.
- Limitation: the merge ran on the same model as the brief (Claude Opus 5.5). Independence rests on the two reviews (Fable 5.1 on Claude Code, GPT-6 Astra on Codex) and on going back to the source for every dispute.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The 5G and legal records stay uncaptured until Kris decides; the rollout plan in the report lists them.
- [KI-HARNESS-GOV-222 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-222-timeline-and-calendar-skill.md) still says `project: observatory`. Changing that is the harness's call.
- A brief commit-lock clash with another session cleared on retry. Nothing was touched.

## Queries

### FEED-HOME - Where a private base without a site publishes

**Context:** legal-principal and personal-principal have no site, and their dates are private. legal's include court dates. The brief proposed writing them into Kris's own Google or Microsoft calendar through `mcp-gsuite` and `mcp-m365`. The code shows neither can do that yet. Google's create tool takes only timed start and end values, and has no field for free/busy, all-day dates or a stable event key. The Microsoft server has no update tool and can only write to the default calendar. Whether a subscribed calendar counts towards free/busy is untested; both reviewers relied on memory of how the clients behave. Kris asked for sets people can subscribe to. A dedicated Google calendar has its own private subscription address, which would cover that, but this also comes from memory and is untested.

**Query:** How should private calendar sets be published?

**Options:**

a) (recommended, confidence medium - honours "publish ... to subscribe to" once proved, keeps court dates off any public URL, and promises nothing the connectors cannot do yet; the coordinator will send this for blind review) Keep private sets unpublished in v1, shown in the base's generated view. Build account sync as a separate adapter after the connector work, prove it on a test calendar and then on a few personal dates, and use the provider calendar's private address for subscribing on other devices.

b) Account sync now, as the brief proposed. This first needs the connector work.

c) An unguessable feed URL on a public host, chosen base by base. Anyone who gets the URL sees every date.

d) A private feed host behind a token-checking Cloudflare Worker. New infrastructure to build and secure.

### SPAN-FEED - Whether spans appear in calendar feeds

**Context:** Kris settled that a span (waiting, elapsed work time) never takes busy time, and left open how a feed carries one. Both reviews read that the same way, so keeping spans out of feeds is a design choice rather than something Kris already decided. Fable suggested letting each calendar opt in to showing spans as free all-day blocks. Most of legal's "waiting on the other side" rows are single dates.

**Query:** Should spans appear in calendar feeds?

**Options:**

a) (recommended, confidence high - both reviews agree spans stay off by default, it matches "a calendar with the milestones", and an opt-in can be added later without changing the model) No, not in v1. Where a span's end matters, that end is its own milestone, and the checks fail any span marked busy.

b) As a), plus an opt-in now for each calendar to show its spans as free all-day blocks.

c) Feeds show a span's start and end as two free markers.

### SKILL-SHAPE - One skill or a skill plus a view skill

**Context:** The views are 5G's List, Months and Runway, and a generated timeline in a base. Site rendering already belongs to `ki-repo-website-content`, and base rendering to `ki-repo-kb-live-artifacts`. Both reviews favour one skill.

**Query:** Should the timeline view live in the same skill as the dated items and feeds?

**Options:**

a) (recommended, confidence high - both reviews agree, and the view is generated from the same model) One skill that owns the item model, the feeds and the view data format, with rendering left to the existing website and live-artifact skills.

b) A dated-items skill plus a separate timeline-view skill.

### SKILL-NAME - The skill's name

**Context:** The naming decision [ADR-KI-HARNESS-SKILLS-003](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-003-dependency-order-for-multi-skill-composition.md) allows all three names, and none is taken. The brief said "timeline" clashes with `ki-diagrams`. The source shows otherwise: `ki-diagrams` never mentions timelines, though Archify does list timeline diagrams. "Calendar" is already the name of the `Calendar/` folder for daily and weekly notes in every base. Kris's own words were "a calendar with the milestones". Both reviews favour `ki-key-dates`.

**Query:** Which name should the skill take?

**Options:**

a) (recommended, confidence medium - names the stored source rather than one output, and avoids both the clash with the `Calendar/` folder and the busy-calendar reading; the coordinator will send this for blind review) `ki-key-dates`.

b) `ki-calendars`, matching Kris's words.

c) `ki-timelines`, matching the Project's name.

### CODE-HOME - Where the shared code lives

**Context:** The 5G feed builder has no dependencies. `ki-diagrams` already keeps its build, export and check scripts inside the skill. Kris prefers a vendored copy with a drift check over publishing a package. 5G builds in Cloudflare, which has no harness checkout, so its drift check has to run in its local `bun test`. Both reviews agree.

**Query:** Where should the item model, feed builder and checks live?

**Options:**

a) (recommended, confidence high - both reviews agree, it follows the `ki-diagrams` precedent and Kris's shared-code preference, and nothing is published) In the skill's own `scripts/` in the harness, as a core with separate source and provider modules. 5G vendors a copy with a drift check, and `tools-ki` gains a command only if a stable machine interface is needed later.

b) A `ki` command in `tools-ki`.

c) A shared package used through a workspace or a pinned Git reference.

### ADOPTION-ORDER - The order of adoption

**Context:** Kris named the first adopters as legal-principal, personal-principal and 5G Emerge. 5G already has the component and a host, so it can prove the extracted code behaves the same, but its data has no times, spans or private dates. legal has the most urgent dates, running to February 2027. The reviews agree on splitting legal into a local part and a sync part, and on testing any write to a real calendar on low-stakes data before court dates.

**Query:** In what order should the bases adopt the skill?

**Options:**

a) (recommended, confidence medium - keeps Kris's three adopters, gets legal its view early with no credentials, and keeps the first real calendar write away from court dates; the coordinator will send this for blind review) 5G first, as a pilot proving the feeds come out unchanged. Then 5G's timeline merge and legal's local timeline. Then the sync adapter, proved on a test calendar and then on a few personal dates. legal's sync comes last.

b) The brief's order: 5G, then all of legal, then personal-principal.

c) legal first, for its urgent dates.

### LEGAL-VIEW - Where legal's generated timeline lives

**Context:** legal's Command Centre Guide says of its live artifact: "Future changes must update that artifact rather than create a second one". That artifact already has a Calendar built only from explicit date fields. The current FR Timeline is a generated Working Note with a Mermaid gantt.

**Query:** Where should legal's generated timeline live?

**Options:**

a) (recommended, confidence high - the Guide's text is explicit, and the artifact already holds a calendar view) Inside the existing Command Centre artifact, keeping the current Working Note and gantt until legal's owner confirms nothing is lost.

b) A generated Working Note, as today.

c) A new live artifact pair. The Guide forbids this.

### TIMED-BUSY - A busy item with a time but no end

**Context:** In the calendar standard, a timed event with no end takes no time at all, so marking it busy blocks nothing. Kris settled "never invent a time or duration". legal already records a numeric `duration_minutes` field, which can supply a real end. Both reviews raised the gap.

**Query:** How should a busy item with a time but no end be handled?

**Options:**

a) (recommended, confidence medium - keeps "never invent a duration" while making busy mean something; the coordinator will send this for blind review) The checks require a real end, either an end time or `duration_minutes`, and fail the item without one.

b) Write it as an all-day busy item, which blocks the whole day.

c) Allow it and write it with no duration, which blocks nothing.

### 🤖 → 👤 Handoff to supervisor · since 23:52 BST

👤 8 with you

- [with you] FEED-HOME · owner · since 23:52
- [with you] SPAN-FEED · owner · since 23:52
- [with you] SKILL-SHAPE · owner · since 23:52
- [with you] SKILL-NAME · owner · since 23:52
- [with you] CODE-HOME · owner · since 23:52
- [with you] ADOPTION-ORDER · owner · since 23:52
- [with you] LEGAL-VIEW · owner · since 23:52
- [with you] TIMED-BUSY · owner · since 23:52
- [committed] merged report, ki-principal
- [unpushed] ki-principal
