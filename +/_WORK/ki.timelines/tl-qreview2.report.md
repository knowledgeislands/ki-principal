# KI > Foundations > Timelines › tl-qreview2

**🤖 → 👤 Handoff to supervisor · Run report at 00:40 BST**

---

## Done

Reviewed both queries against permitted local documentation and connector source; no remote calls, repository changes or commits.

Naming check: all three candidates are unused and fit [ADR-KI-HARNESS-SKILLS-003](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-003-dependency-order-for-multi-skill-composition.md).

Blindness limitation: the expressly permitted [brief](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.timelines/design/timelines-skill-brief.md) contains an earlier naming recommendation. No forbidden file was read, but SKILL-NAME cannot count as a fully blind review.

## In Progress

Nothing is running. Current scheduling behaviour and live provider semantics remain unverified; no connector tests were run.

## Queries

The following are review recommendations for the supervisor, not decisions or implementation authority.

## SKILL-NAME - The skill's name

**Context:** The skill governs dated sources, calendar sets, feeds and a derived timeline. Directly checked the naming rule, candidate availability, the permitted design's scope and the repository's existing Calendar note convention. The owner's wording and Archify's timeline capability are taken from the supplied context. A folder name is an ambiguity to explain in the skill description, not a naming prohibition.

**Query:** Which name should the skill take?

**Options:**

a) (recommended, confidence medium - Calendar sets are the user-facing capability and match Kris's stated request.) `ki-calendars`; explicitly distinguish dated-item publication from daily notes and appointment management in its description.

b) `ki-key-dates`, emphasising the canonical source but less clearly covering events, spans and publication.

c) `ki-timelines`, matching the Project but foregrounding only one generated view.

## PROVIDER-FIRST - First sync provider

**Context:** Directly verified that Personal's [Integrations note](</Users/krisbrown/workspaces/personal/personal-principal/Pillars/Productivity/Knowledge Management/KB Specifics/Integrations.md:26>) identifies Google Calendar MCP, with July 2026 currency. This is documented configuration, not proof of Kris's current scheduling client. Microsoft's integration note establishes availability, not primacy. Inspected both connectors' calendar registration and implementation: Google selects calendars and patches by event id; Microsoft lacks those tools and its create handler discards the returned event id. Both lack the required explicit all-day and busy-status write controls. The permitted design confirms test-calendar proof before real dates. The claimed roughly doubled effort for both providers is unmeasured, not adopted as fact.

**Query:** Which provider should the first connector work and adapter proof target?

**Options:**

a) (recommended, confidence medium - Documented personal calendar use and the smaller verified connector gap both favour Google.) Google first through `mcp-gsuite`; revalidate Kris's actual scheduling tool when step 4 starts, and add Microsoft only if that or the acceptance matrix requires it.

b) Leave the choice open until step 4 if the integration note is no longer representative.

c) Microsoft first if current Outlook scheduling is established.

d) Both together if a concrete requirement needs both from the first proof.

```text
SKILL-NAME - Use ki-calendars; do not count this naming review as fully blind.
PROVIDER-FIRST - Target Google first, revalidating actual scheduling at step 4; add Microsoft if required.
```
