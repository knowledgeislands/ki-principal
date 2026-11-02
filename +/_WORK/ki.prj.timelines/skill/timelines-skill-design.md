# Timelines skill: decided design and rollout

**Owner:** Kris Brown · **Work:** `ki.timelines` · **Report:** [timelines-skill-report.md](timelines-skill-report.md) · **Decisions:** [decisions.md](../decisions.md) · **Date:** 2026-10-20

This note is the design as decided. It takes every settled point from the owner's decisions, cited by tag, and the points the [merged report](timelines-skill-report.md) settled on cited evidence, marked "merge". DESIGN-HIGH, DESIGN-REVIEWED and NAME-AND-PROVIDER were taken under OVERNIGHT-AUTONOMY; Kris may reverse any of them on return, and this note follows any reversal. The skill is `ki-calendars` (NAME-AND-PROVIDER). Case content from legal-principal is not reproduced.

## Contents

- [Scope](#scope)
- [Model](#model)
- [Sources](#sources)
- [Sets, targets and feeds](#sets-targets-and-feeds)
- [View data format](#view-data-format)
- [Checks](#checks)
- [Skill and code home](#skill-and-code-home)
- [Privacy rules](#privacy-rules)
- [Open points](#open-points)
- [Rollout plan](#rollout-plan)
- [Handoff to the harness](#handoff-to-the-harness)

## Scope

- **Milestone-centred.** A base keeps its key dates, due dates and milestones and may publish one or more calendar sets to subscribe to (TIMELINES-OPEN). The calendar carries milestones, not elapsed time; a span never takes busy time in a subscriber's calendar (TIMELINE-IMPROVEMENTS).
- **One skill.** `ki-calendars` owns the dated item's meaning, the feed projection and the view data format. Website rendering stays with `ki-repo-website-content`, base rendering with `ki-repo-kb-live-artifacts`, provider input and output with the connector repositories (SKILL-SHAPE, DESIGN-HIGH).
- **Description boundary (NAME-AND-PROVIDER).** The skill's description separates milestone-centred dated sets and their feeds and views from two neighbours it does not govern: a base's `Calendar/` period notes (daily, weekly, monthly and meeting notes, under `ki-repo-kb`'s zone model), and appointment management (booking, inviting, accepting or moving meetings in a provider calendar, left to the provider and its connectors).
- **Out of v1:** recurrence, spans in feeds, private publication before its adapter is proved, the Mermaid gantt's redraw (ki.observatory's LGL-PRINCIPAL-OPS-028), any cross-base Observatory view (ki.observatory), the `ki` CLI and npm publication.

## Model

### Dated item

| Field | Meaning |
| --- | --- |
| `id` | Permanent logical id, unique within its base. Never reused. |
| `title` | Short label. |
| `start` | A date at day (`YYYY-MM-DD`), month (`YYYY-MM`) or year (`YYYY`) precision, or a local date and time (`YYYY-MM-DDTHH:MM`), or a timestamp with an explicit offset. |
| `end` | Optional. For date-only items, the inclusive last day, day precision only. For timed items, an exclusive end instant. |
| `duration_minutes` | Optional positive integer, for timed items only; an alternative to a timed `end`, as legal's Guide already defines it. |
| `type` | `milestone`, `event` or `span`. |
| `busy` | Boolean, default `false`. |
| `firmness` | Optional: `confirmed`, `planned`, `target`, `proposed` or `to-confirm`. |
| `category` | Optional free per-base label (5G's `kind`; legal's `kind` and `lane`). |
| `description` | Optional text. |
| `sources` | Citations into the base's own source register or notes. |
| `sets` | The calendar sets the item belongs to. Implied by the set for a registry entry. |

Recorded beside the item, never as its identity: its provenance (source file or note title, source field, schema version) and any base-owned progress shown as presentation metadata (merge).

### Types

- `milestone` is a point: a key date, due date, deadline or decision point.
- `event` is something someone attends, on one day or several, timed or untimed.
- `span` is elapsed or waiting time. It appears only in timeline views, is never busy and never a feed event; where its end matters, that end is its own milestone (SPAN-FEED, DESIGN-HIGH; TIMELINE-IMPROVEMENTS).
- **Mapping (merge):** 5G's `milestone` and `deadline` become `milestone`; its `review`, `meeting` and `event` become `event`. legal's `event_at` becomes `event`; its other live fields become `milestone`.

### Busy and firmness

- **Busy (BUSY-STATUS, QUERIES-AGREED):** `busy: true` writes `TRANSP:OPAQUE` and `X-MICROSOFT-CDO-BUSYSTATUS:BUSY`; absent or false writes `TRANSP:TRANSPARENT` and `X-MICROSOFT-CDO-BUSYSTATUS:FREE`. These state intent; whether a subscriber's scheduling tool honours them is unproven until the adapter's acceptance matrix passes (FEED-HOME, DESIGN-REVIEWED).
- **Untimed busy** blocks the whole day.
- **Timed busy (TIMED-BUSY, DESIGN-REVIEWED):** needs an explicit `end` or a positive `duration_minutes`; the end must fall after the start; an item carrying both, disagreeing, is rejected. An invalid item stays visible in generated views with its diagnostic; feeds leave it out until it is fixed, because a feed can carry neither a diagnostic nor an invented end (this note's reading; see [Open points](#open-points)).
- **Never busy:** a span, or a month- or year-precision item.
- **Firmness (merge):** separate from busy (BUSY-STATUS). `confirmed` writes `STATUS:CONFIRMED`; every other value writes `STATUS:TENTATIVE`; absent firmness writes no `STATUS`. Each source maps into the vocabulary through a reviewed mapping: legal's `hard: true` maps to `confirmed`, and `hard: false` maps to nothing.
- **Progress** (`open`, `waiting`, `overdue`, `done`) stays the base's own state, out of the date core.

### Precision and time

- **Precision (merge):** 5G's rules stay. A month-precision item spans its month as a free placeholder titled "(day to be confirmed)"; a year-precision item stays off feeds and shows in views only. A month placeholder is uncertainty, not a span.
- **Zone (DATE-MODEL, QUERIES-AGREED):** each set declares one IANA zone. Time of day is optional per item; untimed items stay all-day (`VALUE=DATE`) and are never converted to UTC. Times and durations are never invented.
- **Conversion (merge):** timed items are written as UTC instants computed at build from the zone's offset on the item's own date, with `X-WR-TIMEZONE` as metadata. A timestamp with an explicit offset stays that instant. Floating times are never written.
- **Clock changes (merge):** a local time that does not exist (Europe/London 2026-03-29 01:30) is rejected; an ambiguous one (Europe/London 2026-10-25 01:30) needs an explicit offset.
- **Several sets:** an item in two sets keeps one instant, resolved in its source's zone.
- **Runtime:** conversion uses the runtime's `Intl`; the supported runtime is pinned.
- **Recurrence** is out of v1: birthdays and renewals are authored as dated instances and never rolled forward.

### Identity

- **UID:** `<logical id>@<uid domain>`. Each base declares one `uid_domain`, fixed once and never changed with hosting. A registry entry's logical id is its `id`. A frontmatter item's logical id is `<item_id>.<milestone key>`, the key logical (`due`, `event`, `decision`, `chase`, `review`, `target`) rather than the field name, with `due_at` taking precedence over `due_on` for the same obligation (merge).
- **5G:** declares `uid_domain: phase3.5g-emerge.io`, so every emitted UID stays exactly `<id>@phase3.5g-emerge.io` (merge). This reconciles the merge's two rules, a base namespace and 5G's kept host suffix, in one form; see [Open points](#open-points).
- **Life cycle:** rescheduling keeps the UID; set membership changes create no orphan copy. Removal and becoming undated drop the item from feeds; how a cancelled item is projected is for harness planning ([Open points](#open-points)). Sync applies the same outcomes through its own removal rules.

## Sources

One editable home per date (ONE-SOURCE, QUERIES-AGREED). A base declares its source shape and its sets; the generator reads only what is declared and never scans prose (merge; legal Guide).

- **Registry file:** a JSON5 file of sets with their entries, 5G's shape, for dates with no other home.
- **Dated frontmatter:** labelled date fields on named note types, legal's shape, where each date belongs to an Item or subject note. A field map names each date field, its milestone key and its type.
- **Manifest:** each base declares its source shape, field map, sets, zone, `uid_domain` and publication targets in one manifest. Where the manifest lives is for harness planning ([Open points](#open-points)).
- **Never empty on failure (merge):** a failed or partial source read stops generation with an error; it never yields an empty calendar or view. This matters most for sync, where an empty read would delete events.

## Sets, targets and feeds

### Sets and targets

- Each set declares `id`, `title`, `description`, optional `group`, `code` (up to three characters), `colour` (slot 1-8), `zone` and `audience`, `public` or `private`.
- Each base declares its publication targets and each target's visibility; a path alone cannot show visibility, since 5G's preview URLs have no Access bypass while production does (merge).
- The generator refuses to write a private set to a public target.

### Feeds

- **Public sets on a site:** static `.ics` at a permanent path, as 5G serves `/calendars/<id>.ics`, behind an Access bypass where the site is gated.
- **Feed properties (5G's, kept):** `PRODID` from the base's options, `METHOD:PUBLISH`, `NAME` and `X-WR-CALNAME`, `DESCRIPTION` and `X-WR-CALDESC`, `URL`, `SOURCE`, `REFRESH-INTERVAL` and `X-PUBLISHED-TTL` of 12 hours, and `X-WR-TIMEZONE` for sets with timed items.
- **Event properties:** `UID`, `DTSTAMP`, `DTSTART` and `DTEND` (all-day `VALUE=DATE` with an exclusive end, or UTC instants), `SUMMARY`, `DESCRIPTION`, `CATEGORIES` from the category, `STATUS`, `TRANSP`, `X-MICROSOFT-CDO-BUSYSTATUS` and `URL`.
- **Empty sets** stay valid and subscribable, with 5G's UTC `VTIMEZONE` kept.
- **Encoding:** 75-octet UTF-8 line folding and TEXT escaping, as 5G's tests cover.
- **Spans** stay off feeds in v1; a per-set opt-in may come later without a model change (SPAN-FEED, DESIGN-HIGH).
- **Private sets** stay unpublished in v1, served by the base's generated view (FEED-HOME, DESIGN-REVIEWED). Account sync is a later, separate adapter; see [Privacy rules](#privacy-rules).

## View data format

The core emits one view document per base, `schema: "ki-calendars-view/1"`, from the same items as the feeds. It is a superset of 5G's `ViewData` (`apps/site/lib/calendars.ts`), so 5G's `calendarView` becomes a thin adapter and its pages do not change.

```json5
{
  schema: 'ki-calendars-view/1',
  generated_from: { manifest: '<path in base>', digest: '<sha256 of resolved sources>', schema_version: 1 },
  sets: [
    { id: '', title: '', code: '', colour: 1, group: '', zone: 'Europe/London', audience: 'public', page: '', count: 0 }
  ],
  items: [
    {
      id: '', uid: '', set: '', title: '',
      type: 'milestone',            // milestone | event | span
      category: '', categoryLabel: '',
      firmness: 'confirmed', firmnessLabel: '',
      busy: false,
      precision: 'day',             // day | month | year | time
      first: 'YYYY-MM-DD', last: 'YYYY-MM-DD',          // inclusive days, in the set's zone
      start: 'YYYY-MM-DDTHH:MM:SSZ', end: 'YYYY-MM-DDTHH:MM:SSZ', // timed items only
      progress: '',                 // base-owned presentation metadata, optional
      description: '', tags: [{ pill: '', name: '' }], sources: [''], href: ''
    }
  ],
  diagnostics: [{ id: '', rule: '', message: '' }]
}
```

- **Past and today** are classified in each set's zone, not the reader's (merge; legal Guide, "Today boundary"). The reader's local time is used only to display timed items.
- **Renderings:** on a site, 5G's List (built at render), Months and Runway (drawn in the browser). In a base, a view inside an existing live artifact where one exists, otherwise a live artifact pair whose Markdown owns the view's descriptor, the sources it selects and its presentation; generated data sections are labelled and rebuilt and never become an input (merge).
- **legal:** its timeline is a view of the existing `legal-command-centre` artifact; the Working Note and Mermaid gantt stay until legal's owner confirms nothing is lost (LEGAL-VIEW, DESIGN-HIGH).
- **Spans** show as bars and milestones as marks. A Mermaid gantt may remain one generated rendering until LGL-PRINCIPAL-OPS-028 decides otherwise.
- **Public view documents** carry only allowlisted fields and no diagnostics that quote private sources.

## Checks

The skill carries a standard, a rubric and an audit, each check with a synthetic fixture (ADOPTION-ORDER, DESIGN-REVIEWED: offline cases for times, spans, busy checks and privacy).

| Check | Fails when |
| --- | --- |
| Item valid | A required field is missing, a date is impossible, `end` precedes `start`, or precision and value disagree. |
| No invented date | A date has no declared source field or registry entry. |
| Identity | A UID repeats, changes for a kept item, or a frontmatter item uses a field name as its key. |
| Busy span or placeholder | `busy: true` on a span or a month- or year-precision item. |
| Timed busy | A busy timed item lacks a real end, or its `end` and `duration_minutes` disagree (TIMED-BUSY). |
| Clock change | A local time does not exist, or is ambiguous without an offset. |
| Privacy | A private set reaches a public target, or a public feed or view carries a field off its allowlist; the contact-detail test is a backstop. |
| One source | Regenerating from the declared manifest does not reproduce the committed output, or an undeclared list of dates duplicates a declared one (flagged for a human). |
| Failed read | A partial or failed read yields any output. |

The audit regenerates deterministically and compares; it is not a generator stamp (merge). Its fixtures pin a build clock, so `DTSTAMP` never makes a golden test churn; sync compares content, not stamps (merge).

## Skill and code home

- **Home (CODE-HOME, DESIGN-HIGH):** the skill's own `scripts/` in `ki-agentic-harness`, following `ki-diagrams/scripts/`.
- **Layout:** a pure core (model, validation, `.ics` and view projection) with no dependency; source readers (registry, frontmatter) reusing the harness's existing YAML and JSON5 parsing; provider adapters later and separate.
- **5G** vendors the core with its source revision and a drift check run in its local `bun test`, since Workers Builds has no harness checkout.
- **No publication:** no npm package; no `tools-ki` command unless a stable machine contract is later needed.

## Privacy rules

- **Audience and target** are declared separately; the generator refuses a private set on a public target.
- **Public feeds and views** carry an allowlist of fields. 5G's publication-boundary test in `apps/site/tests/site.test.ts`, which catches email addresses and phone numbers, stays as a backstop; it cannot prove that private narrative is absent.
- **Private items** carry a note title and `item_id`, never a filesystem path (merge).
- **v1:** private sets stay unpublished, shown only in the base's generated view (FEED-HOME, DESIGN-REVIEWED).
- **Account sync**, when built, is a disclosure to the provider and its delegates. It follows the connector work, is proved on a test calendar and then on a few personal dates, and has private subscription, refresh and revocation verified before it is promised (FEED-HOME).
- **Secret addresses:** any provider secret URL is a bearer credential, held in a proper secret store, never in a repository, diagnostic or report (FEED-HOME).
- **Approval:** account sync or a capability URL for any base needs Kris's explicit approval for that base. Any run that calls a provider needs Kris's explicit grant.
- **Diagnostics** never quote private content into a public output.

## Open points

- **SKILL-NAME** (closed, NAME-AND-PROVIDER): `ki-calendars`, which names the subscribable sets Kris asked for, its description separating them from `Calendar/` period notes and appointment management (see [Scope](#scope)). The skill directory, view schema and manifest key take the name; nothing is built under it until the harness plans KI-HARNESS-GOV-222, so Kris can still change it.
- **Manifest home** (harness planning): a section of `.ki.toml` or a declared file in the base.
- **Invalid item in feeds** (harness planning may confirm): this note reads TIMED-BUSY's "stays visible with a diagnostic" as visible in views and left out of feeds until fixed.
- **UID form** (harness planning may confirm): `<logical id>@<uid domain>`, reconciling the merge's base namespace with 5G's kept host suffix.
- **Cancelled items** (harness planning): whether a cancellation is written `STATUS:CANCELLED` for a while or dropped at once.
- **Provider for the first adapter** (closed, NAME-AND-PROVIDER): Google first through `mcp-gsuite`; see rollout step 4.

## Rollout plan

The order is ADOPTION-ORDER (DESIGN-REVIEWED). Each receiving repository captures and owns its own record through `ki-next`, with its Context quoting the decisions in words; records outside the Knowledge Islands territory name `project: ki-principal/timelines`. The pilot runs before any parallel step, and its lessons go into each later brief.

| # | Step | Owning repository | Entry check | Proof |
| --- | --- | --- | --- | --- |
| 1 | The skill: standard, rubric, audit, core scripts, both source readers, view format and synthetic fixtures | `ki-agentic-harness`, KI-HARNESS-GOV-222 | SKILL-NAME answered; the handoff received and the record planned by the harness | Every check's fixture passes offline (times, clock changes, aliases, spans, busy, privacy refusal, failed reads); the skill's audit runs clean on its own fixtures |
| 2 | 5G parity pilot: vendor the core with provenance and a drift check | `5g-emerge-phase3` | Step 1 accepted | At a fixed build clock, feeds are identical apart from `PRODID` through options and the new busy properties; UIDs, feed paths, page anchors, escaping, folding, empty sets and List content unchanged; drift check and publication-boundary test pass in `bun test` |
| 3a | 5G source merge: generate the programme timeline from the registry | `5g-emerge-phase3` | Step 2 accepted | Each of the eleven timeline files mapped to its registry entry with `seeAlso` and source wording kept, the mapping reviewed before deletion; timeline page anchors unchanged |
| 3b | legal local timeline: field map, milestone keys, `hearing_date` resolved, view in `legal-command-centre` | `legal-principal` | Step 2 accepted; independent of 3a | A read-only comparison accounts for every current FR Timeline row; the artifact shows the generated view; the Working Note and gantt stay until legal's owner confirms nothing is lost |
| 4 | Connector work: all-day writes, transparency or `showAs`, calendar selector, update by provider id, a marker for events the tool created | `mcp-gsuite`; `mcp-m365` only if needed | Google first through `mcp-gsuite` (NAME-AND-PROVIDER); at the step's start, revalidate Kris's actual scheduling tool and add Microsoft through `mcp-m365` only if that or the acceptance matrix needs it; steps 3a and 3b need not wait | Offline connector tests for each new capability; no live call in tests |
| 5 | Adapter proof: sync runner in the skill's `scripts/`, run as an Activity under `ki-repo-kb-activities` | `ki-agentic-harness`, a new record | Step 4 accepted; Kris's explicit grant for remote calls on a test calendar | On a test calendar: dry-run comparison, provider-id mapping, sole ownership of created events, safe removal, content comparison; the acceptance matrix (account type; own, dedicated and subscribed calendar; free, busy, tentative, all-day and timed; display and free/busy result; Kris's actual scheduling tool); private subscription, refresh and revocation verified |
| 6 | personal set: Kris authors a few dates into frontmatter; a small private set syncs | `personal-principal` | Authoring may start once step 1 fixes the frontmatter shape; sync waits on step 5 and Kris's approval of the set and its disclosure | The set's events match the source; free default and busy items behave as the matrix showed; revocation removes access |
| 7 | legal sync: private publication of legal's set | `legal-principal` | Steps 5 and 6 passed; Kris's explicit approval of legal's disclosure | As step 6, plus timed items with `duration_minutes` and all-day obligations checked against the artifact view |

Steps 3a, 3b and 4 may run in parallel once their entry checks hold. The legal gantt stays Mermaid throughout, under ki.observatory's DIAGRAM-GANTT.

## Handoff to the harness

Draft for the coordinator to route to `ki-agentic-harness` through State of play, written as `ki-work-roadmap` describes for work another repository must deliver. It quotes the decisions in words and links only durable documentation, because this note and the work folder are temporary. The harness owns the record's priority, plan, project and acceptance; this is a proposal, not an edit.

**Blocking:** not blocking any ki-principal record. It is the build-order prerequisite of every later Timelines step, each in its own repository.

**Proposed for KI-HARNESS-GOV-222, Timeline and calendar skill:**

- **Project:** `timelines` in place of `observatory`, serving the [Timelines Project](https://github.com/knowledgeislands/ki-principal/blob/main/Streams/Projects/timelines.md). The harness's call.
- **Context to add:**

  > Kris Brown opened the Timelines Project on 19 October 2026 (TIMELINES-OPEN) and added on the same day (TIMELINE-IMPROVEMENTS): "it's more that we want a calendar with the milestones than it is that we want a calendar with, you know, kind of elapsed time to do some particular piece of work." A span therefore never takes busy time.
  >
  > On 19 October Kris settled (QUERIES-AGREED): a per-item `busy`, default free, with firmness separate; one editable source per date, generating both views and feeds; an optional time of day per item and one IANA zone per calendar set, never inventing a time or duration.
  >
  > On 20 October, under Kris's overnight grant and after two independent design reviews and a blind review, these were taken (Kris may reverse any): one skill owning the dated item, feeds and view data format, rendering left to `ki-repo-website-content` and `ki-repo-kb-live-artifacts`; code in the skill's own `scripts/`, which 5G Emerge vendors with a drift check; spans stay out of feeds in v1, an end that matters being its own milestone; private sets stay unpublished in v1, with account sync a later adapter proved on a test calendar then a few personal dates; a busy timed item needs an explicit end or a positive `duration_minutes`, end after start, inconsistent values rejected, an invalid item staying visible with a diagnostic; adoption by a 5G parity pilot first, then 5G's source merge and legal-principal's local timeline independently, then the adapter proof, a small personal set, and legal sync last. Also under the grant: the skill is named `ki-calendars`, its description separating milestone-centred dated sets and feeds from `Calendar/` period notes and appointment management, a name Kris can still change before anything is built under it; and the first provider adapter is Google through `mcp-gsuite`, with Kris's actual scheduling tool revalidated when the connector step starts and Microsoft added only if that or the acceptance matrix needs it.

- **Goal (unchanged in substance):** a harness skill governs the dated things a knowledge base keeps, its key dates, due dates and milestones, so each base can keep them in one source, show them as a timeline and publish calendar sets people subscribe to, each item stating whether it takes busy time.
- **Boundary to add:**
  - In: the dated item (`milestone`, `event`, `span`; `busy`; firmness; day, month, year or timed precision; logical UIDs `<logical id>@<uid domain>`, with 5G's existing UIDs kept exactly); two source readers, a registry file and dated frontmatter, from a declared manifest; the `.ics` projection; a view document that is a superset of 5G's `ViewData`; the standard, rubric and audit with a synthetic fixture for every check; a pure dependency-free core in the skill's `scripts/`.
  - Out: recurrence; spans in feeds; private publication and any provider call; changes to 5G Emerge, legal-principal or personal-principal, each of which adopts through its own record; npm publication and any `tools-ki` command.
- **Shaping to add:**
  - **Model:** a timed busy item needs a real end; a span or a month- or year-precision item is never busy; `confirmed` writes `STATUS:CONFIRMED`, other firmness `TENTATIVE`, none no `STATUS`; legal's `hard: false` maps to no firmness.
  - **Time:** convert timed items to UTC using the zone's offset on the item's own date; reject a non-existent local time and require an offset for an ambiguous one; never convert a date-only value; classify past and today in the set's zone.
  - **Sources:** never scan prose; a failed or partial read produces no output; the audit regenerates from the manifest and compares rather than trusting a stamp.
  - **Privacy:** audience (`public`, `private`) is separate from target visibility, which each base declares; a private set never reaches a public target; public outputs carry an allowlist of fields; private items carry a note title and item id, never a path.
  - **Source component:** 5G Emerge phase 3's `apps/site/lib/ics.ts`, `lib/calendars.ts`, `src/_data/calendars.json5` and `tests/calendars.test.ts`; legal-principal's Command Centre Guide, "Dates and calendar semantics" and "Derived-view contract".
  - **Name:** `ki-calendars`, with the view format `ki-calendars-view/1`; the description excludes `Calendar/` period notes and appointment management.
  - **Decisions still needed:** where a base's manifest lives; whether an invalid timed busy item is left out of feeds while it shows in views.
- **Dependencies / blocks to add:** none inbound; the skill builds on the 5G Emerge component as it stands. Later work in other repositories builds on it: 5G Emerge's vendored pilot and source merge, legal-principal's local timeline and later sync, personal-principal's authored dates and private set, and calendar-writing capabilities in `mcp-gsuite` first, with `mcp-m365` only if the step-4 revalidation of Kris's scheduling tool or the acceptance matrix needs it. A separate harness record will be needed for the sync adapter once connector work lands.
- **Verify, for planning:** every check's fixture passes offline, including times, clock changes, milestone-key aliases, spans, busy rules, privacy refusal and failed reads.
