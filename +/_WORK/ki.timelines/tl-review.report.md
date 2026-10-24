# KI > Foundations > Timelines › tl-review

**🤖 → 👤 Handoff to supervisor · Run report at 19:44 BST · last mark withheld for blind review**

---

## Done

Reviewed all four queries independently; `queries.md` and `state.md` were not read.

Checked 5G source and publication documentation, legal dated Items and generated-view contracts, a personal renewal note, and [KI-HARNESS-GOV-222](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-222-timeline-and-calendar-skill.md). The harness record is under `docs/roadmap/`; the brief's `Streams/Roadmap/` path does not exist.

No commits or repository writes; no remote calls. Static inspection only: deployment and calendar-client behaviour were not tested.

## In Progress

Nothing is running. The coordinator's mark remains unverified to preserve blindness.

## Queries

Independent recommendations follow; no blocking query is raised by this review.

## FEED-HOME

**Context:** Directly verified [5G's publication documentation](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/docs/guides/developer/cloudflare.md:65): `/calendars/*` bypasses Access and is public. The [survey](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.timelines/design/survey.md) and brief supply legal/personal's no-site, private-date context; their hosting estate was not independently audited.

**Query:** Where should a base without a site serve feeds?

**Options:**

a) (recommended, confidence high - a public bypass does not establish a suitable private-feed architecture) **y:** leave hosting to design, comparing the base's site, Observatory and private-feed host against privacy and subscription-client requirements.

b) **x:** require a site per base now.

## BUSY-STATUS

**Context:** Directly verified [ics.ts](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/lib/ics.ts:182) always emits `TRANSP:TRANSPARENT`. [Legal's timeline](/Users/krisbrown/workspaces/legal/legal-principal/Pillars/Command%20Centre/Working%20Notes/XM-CRITICAL-19:44 BSTLINE%20-%20Critical%20Timeline%20and%20Preparation%20Checklist/FR%20Timeline%20to%20FDR.md:114) defines `hard` as fixed by order, court or appointment, rather than occupied time. This corroborates the survey; client-property interoperability remains unverified.

**Query:** Should per-item busy status default to free?

**Options:**

a) (recommended, confidence medium - deadlines and fixed dates do not necessarily reserve time) **y:** explicit per-item `busy`, default free; all-day items block only by explicit choice. Keep firmness separate. Design must define timed blocking intervals and verify client mappings alongside `TRANSP`.

b) **x:** default deadlines and events to busy.

## ONE-SOURCE

**Context:** Directly checked the registry's 11 milestones against the eleven programme timeline files and their separate template reader. List, Months, Runway and feeds already consume the registry. Legal explicitly says correct the controlling Item, then regenerate. These checks corroborate the survey's duplication finding.

**Query:** Should one structured source generate timeline and feeds?

**Options:**

a) (recommended, confidence high - one authoritative date avoids conflicting corrections across views) **y:** generate both from canonical dated items, allowing registry entries or note-frontmatter adapters. Preserve citations, narrative and view-specific labels without a second editable date list.

b) **x:** retain two editable lists linked by id.

## DATE-MODEL

**Context:** Directly verified timestamp-bearing legal Items, the timeline's optional `HH:MM` and file-level `timezone` schema, and [the Guide's date semantics](/Users/krisbrown/workspaces/legal/legal-principal/Pillars/Command%20Centre/Command%20Centre%20Guide.md): timestamps display in `Europe/London`, while date-only values remain dates. 5G's types have no time fields. A personal vehicle note corroborates prose renewal dates; broader personal coverage comes from the survey.

**Query:** Should the model include optional times and a calendar-set time zone?

**Options:**

a) (recommended, confidence high - dates-only feeds would discard time precision already held by an adopter) **y:** optional item time and one named time zone per set; untimed items stay all-day. Preserve existing timestamp instants, validate daylight-saving boundaries and never invent a time or duration.

b) **x:** keep dates only and treat times as labels.

### 🤖 → 👤 Handoff to supervisor · since 19:44 BST

🎯 1 handoff

- [handoff] Four-query blind review · work/ki.timelines · since 19:44 BST
