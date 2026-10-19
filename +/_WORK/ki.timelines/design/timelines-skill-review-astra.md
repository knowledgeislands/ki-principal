# Timelines skill: review by Astra

**Reviewer:** GPT-6 Astra on Codex, high effort · **Date:** 2026-10-19 · **Read-only:** yes, except this review and its explicit-path local commit

## Own view

The shared dated-item model is the right centre. Keep the four settled owner decisions: milestone-centred calendars, free by default with independent firmness, one editable source per date, and optional time with one zone per set. None needs reopening. This review was formed without reading another review.

The brief is not yet ready to become an implementation contract. Its principal unsupported step is from an event's busy flag to a promise that a dedicated account calendar protects the owner's availability. Subscription display, a provider's free/busy query and a scheduling product's selected calendars are distinct behaviours. Local evidence does not establish that promise. More concretely, the proposed connectors cannot currently express the full model or perform the described UID-based sync. Treat private publication as a separately proved adapter, not an already available feature.

I recommend one governance skill, provisionally `ki-key-dates`, with a pure conversion core in its harness `scripts/`, explicit source adapters and output contracts. Start with 5G extraction and semantic parity after the skill exists. Prove the frontmatter reader with synthetic fixtures and a read-only legal comparison early; prove any account-writing adapter on synthetic or low-consequence personal items before legal publication. Preserve legal's existing view until its owner verifies replacement completeness. This is an order of verification, not a change to the three first adopters.

The most consequential revisions are the private-sync capability gap, time and identity semantics, and the pilot's coverage. Lesser corrections concern the server-rendered List view, the meaning of a generated Markdown source, and the limits of a generator stamp or contact-detail scan.

Evidence is local repository documentation and code unless expressly labelled prior knowledge. No provider, browser, cloud or network call was made, and no live calendar was tested. The review discusses legal schema and view mechanics only; it reproduces no case content.

## Fact check

These fourteen entries follow the fourteen Established facts in the brief, in order.

1. **5G registry - confirmed with an identity qualification.** [Registry][registry], lines 1-36 and 38-212, declares the fields and the no-invented-date rule; only `phase3-programme` has entries. The entry `id` is not the entire emitted UID: [feed builder][ics], line 174, appends the host. This matters when extracting the code or changing hosting.

2. **Two multi-day review occurrences - confirmed.** [Registry][registry], lines 104-123, supplies two start/end pairs and describes meetings. Treating them as events rather than waiting spans is a reasonable schema interpretation supported by those descriptions, not a type already recorded by the source.

3. **Feed builder - confirmed, with the scope of genericity clarified.** [Feed builder][ics], lines 62-85 and 143-203, implements the stated precision, all-day, firmness and transparency rules without imports. `PRODID` is its only literal 5G brand; the type still contains `scenarios` and `tracks`, and `FeedOptions` supplies source and status formatting. Extraction therefore has adapter work beyond replacing a string. The empty-feed UTC component is also existing behaviour to preserve or explicitly supersede.

4. **Views - corrected.** [View helpers][views] implement grouping, subscribe links, agenda, upcoming entries and view JSON. But List is rendered by Nunjucks at build time, not drawn from JSON by browser JavaScript: [landing template][landing], lines 112-131, and [calendar template][calendar-page], lines 43-68. [View JavaScript][view-js] draws Months and Runway; [calendar JavaScript][calendar-js], lines 4-20, updates past/upcoming state using the reader's date. The survey's distinction is more accurate than the brief's combined claim.

5. **Eleven duplicate timeline milestones - confirmed, but not identical records.** The [timeline collection][timeline-collection] has eleven record files corresponding to the eleven programme entries; their date labels and statuses are separately authored. [Weekly call][weekly] illustrates the split. Some records also carry distinct source references or `seeAlso`, for example [Industry Day][industry]. Collapse must reconcile those fields and the source wording rather than delete the second representation blindly. Common source citations do not constitute a shared editable date source.

6. **Public feed bypass and contact-detail check - confirmed as locally documented behaviour.** [Cloudflare guide][cloudflare], lines 50-74, documents the public production bypass. [Site smoke tests][site-tests], lines 1974-2019, check contact details, including the bypass output. No live Access configuration was queried. The check is a contact-detail guard, not a proof that arbitrary private narrative is absent.

7. **Legal date fields and source authority - confirmed.** [Command Centre Guide][legal-guide], lines 169-205, establishes the listed fields, excludes prose extraction, uses Europe/London for display and today's boundary, and makes canonical Items the operational source. Date-only values remain dates. The brief should preserve the distinction between live milestones and historical fields, and avoid emitting both an alternative day field and timestamp as duplicate obligations.

8. **Legal generated timeline and schema - confirmed at the note level.** [FR Timeline note][legal-timeline], lines 21-23 and 184-202, declares its generated status and `fr-timeline/1` schema, including nullable time/end, lane, kind, hardness and as-of progress. Its kinds key and dated table support interpreting the waiting rows as due points rather than durations. I verified the note's schema and inspected the table structurally; I did not inspect the external source-store JSON or establish that every generated row already has an equivalent canonical frontmatter value. The note distinguishes proposed dates, so exact regeneration is a migration acceptance question.

9. **Personal's dates - supported, with a bounded absence claim.** A local Markdown frontmatter scan outside working/runtime directories found metadata dates and five null Project targets, but no populated future-obligation schema. The [vehicle note][vehicle] holds expiry/renewal information in prose; travel/retreat notes and relationship material follow the surveyed pattern. This supports authoring an explicit schema, not a claim that personal has no structured `date` field at all. No personal dates or values are reproduced.

10. **Harness coverage and precedents - confirmed.** Inspection of skill directories and descriptions found no skill governing kept dated items plus feeds; existing recurring-work and Calendar-zone concerns have narrower scopes. [Diagram skill][diagrams], lines 21-30, owns generator/export scripts including `build-html.ts`. [Live Artifact skill][live-artifacts], lines 20-35, governs the same-stem Markdown/HTML pair. That pair's Markdown authority is the artifact definition, not permission to copy editable dates out of canonical Items.

11. **Observatory boundary - confirmed.** [Observatory README][observatory], lines 17-24, explicitly says loopback-only backend and validated path-free browser evidence. This proves the current declared boundary, not that another feed service could never be designed.

12. **Calendar connector capabilities - confirmed at the stated narrow level.** [Google README][google-readme] documents list/create/update/delete and the access gate; [Microsoft README][microsoft-readme], lines 64-70, documents calendar operations. This fact does not establish the richer sync proposed in point 17. See the exact implementation gaps below.

13. **Naming grammar and availability - confirmed.** [ADR-KI-HARNESS-SKILLS-003][naming], lines 28-34, gives the grammar and plural-collection rule. None of the three candidate directories exists in the local skill tree. The ADR permits all three; it does not select one or declare a semantic collision with diagram types.

14. **Shared-code preference - confirmed, citation label corrected.** The current [personal instructions][personal-instructions], under Publishing to package registries, require checking present distribution and prefer a canonical vendored copy with drift checking, then a pinned Git reference, then an existing workspace. The cited heading Cross-project preferences is not the current heading. No registry publication is proposed or needed here.

## Points

Each numbered Reflection point is marked once. Short reasons link to the detailed evidence below or directly to the local source.

| Point | Mark | Reason and evidence |
| --- | --- | --- |
| 1 | Add | Fix stable identity, date precision and end semantics; see [model details](#model-and-identity). |
| 2 | Agree | Separate occurrences from elapsed spans; preserve lane and kind separately; [registry][registry]. |
| 3 | Differ | Keep exclusion as a v1 design choice, not an owner-imposed prohibition; [span rule](#span-rule). |
| 4 | Add | Waiting kind supports a milestone; firmness needs per-source mapping; [legal schema][legal-timeline]. |
| 5 | Add | Correct wire intent; distinguish all-day occupancy from proven scheduling effect; [time](#time-and-busy). |
| 6 | Differ | Hardness is not a complete firmness mapping; progress is not always clock-derived; [status](#status). |
| 7 | Agree | Preserve precision and free month placeholders, labelled as uncertainty; [feed builder][ics]. |
| 8 | Add | UTC is suitable for one-off instants; reject DST gaps and resolve folds; [time](#time-and-busy). |
| 9 | Add | Defer recurrence explicitly; birthdays need dated instances or later support; [adoption](#adoption). |
| 10 | Agree | Two declared adapters can preserve one editable date home; [source authority][legal-guide]. |
| 11 | Add | Merge citations and wording as well as dates; [duplicate source records](#migration-and-views). |
| 12 | Differ | Raw field names are not stable logical milestone identities; [identity](#model-and-identity). |
| 13 | Add | Owner-verified authoring, with no invented or annually rolled dates; [adoption](#adoption). |
| 14 | Add | Separate audience from target transport; contact scans cannot prove privacy; [privacy](#private-targets). |
| 15 | Agree | Static public sets fit the documented 5G boundary; [Cloudflare guide][cloudflare]. |
| 16 | Differ | The generalised free/busy claim is unverified locally; [evidence limit](#availability-evidence). |
| 17 | Differ | Existing connectors do not implement the promised sync or busy semantics; [gaps](#private-targets). |
| 18 | Agree | A bearer URL needs explicit disclosure acceptance; it is not owner-only access; [privacy](#private-targets). |
| 19 | Add | Exclude the current Observatory as a remote host, not as every possible future producer; [README][observatory]. |
| 20 | Add | Define the Markdown descriptor and generated data boundary; [views](#migration-and-views). |
| 21 | Differ | Reader-local today conflicts with legal's explicit London boundary; [view clock](#migration-and-views). |
| 22 | Agree | One date-governance skill; reuse existing presentation and provider owners; [shape](#shape-and-code). |
| 23 | Add | `ki-key-dates` fits; the supposed naming collisions are not established; [naming][naming]. |
| 24 | Add | Skill scripts fit; separate pure core from parsers, adapters and publication; [code](#shape-and-code). |
| 25 | Differ | A generator stamp cannot prove one source or freshness; [audit](#migration-and-views). |
| 26 | Add | First pilot proves extraction, not private semantics; expand the test boundary; [adoption](#adoption). |
| 27 | Differ | Do not make legal the first real test of private writes and time semantics; [adoption](#adoption). |
| 28 | Differ | Prove low-consequence personal sync before legal publication; [adoption](#adoption). |
| 29 | Agree | Harness retains priority, planning and record ownership; [harness record][harness-record]. |

### Span rule

Point 3's safe default is sensible: show elapsed spans in the timeline and export their significant endpoints as milestones. The [owner's decisions](<../decisions.md>), TIMELINE-IMPROVEMENTS, explicitly leave how a feed carries a span, if at all, to design. They settle no busy time, not no feed representation. Therefore record exclusion as the proposed v1 projection policy, not a logical consequence of the settled rule or a permanent model limitation. A transparent informational span would satisfy the busy decision; it need not be implemented now. Also distinguish an uncertain month placeholder from a real elapsed span so point 7 is not accidentally rejected by the same rule.

### Model and identity

Point 1 needs a precise distinction between inclusive date-only end days and exclusive timed end instants. A timed milestone is an instant; an event may have a known duration. A source with no end must not acquire one simply because a provider demands it. Precision belongs explicitly in validation, even if encoded in the date string. Cross-set membership must preserve one instant: one local time interpreted independently in two sets with different zones would violate one source. Give the item a designated source set/zone or an already-resolved instant, then project it into each set's declared zone.

Point 12's `<item_id>.<field>` works only if fields never represent alternatives or change identity. The [Guide][legal-guide], lines 173-189, allows `due_on` and `due_at` for the same semantic obligation. Promoting an untimed deadline to timed must update the same logical milestone, not leave an old all-day UID beside a new timestamp UID. Define alias precedence, stable per-Item milestone keys and a migration mapping; keep source-field provenance separately. Distinct labelled milestones must still remain distinct. Namespacing must also avoid collisions across bases. Existing 5G UIDs include the host ([feed builder][ics], line 174), so preserve their exact values during extraction and later hosting changes.

Add lifecycle rules: rescheduling updates identity; deletion, cancellation and becoming undated have explicit projection outcomes; set membership changes do not create abandoned copies. Shared dates in overlapping subscriptions need a documented duplicate-display policy. Account sync needs provider identifiers mapped to canonical identity, not an assumption that an iCalendar UID is a writable provider event ID.

### Time and busy

Point 8's UTC output is a reasonable v1 choice for the explicitly non-recurring model. A UTC instant does not require a local-zone component for its interpretation; `X-WR-TIMEZONE` is metadata, not a substitute for correct conversion. This is protocol prior knowledge, not current client testing. Keep already-offset source timestamps as instants; do not reinterpret them as local wall times. Date-only values must never undergo UTC conversion.

Local Python `zoneinfo` round-trip checks demonstrated the missing input cases: London 2026-03-29 01:30 is nonexistent; London 2026-10-25 01:30 maps to two distinct UTC instants. Reject the first and require explicit offset/disambiguation for the second. Verify summer/winter offsets, midnight crossing, timed multi-day ends, all-day exclusive ends and source timestamps containing offsets. Resolve using the item's actual date, not the build day's offset. Runtime zone data and the conversion library need a declared supported contract.

For point 5, mapping the settled boolean to `TRANSP` and the Microsoft extension expresses occupancy intent. It cannot establish what a scheduling consumer actually queries. An untimed busy occurrence can mean whole-day occupancy as the brief says; a timed deadline with no duration cannot honestly promise a busy interval. Specify its zero-duration/unsupported-target handling and never invent an end. Both current connector create schemas require an end, which is a real adapter mismatch, not grounds to fabricate a duration. Preserve free default even when a provider's create default differs.

### Status

Point 6 conflates two different propositions. The [legal schema][legal-timeline], lines 198-199, defines hardness by the authority fixing a date and distinguishes progress values including waiting, proposed and scheduled. Hardness does not provide all five firmness values; `hard: false` does not mean tentative. A user-authored waiting or completion state is not derivable from today's date alone. Keep base-owned progress out of the canonical date core if desired, but allow explicitly sourced presentation metadata. Define a reviewed mapping for firmness, including the case where none is known. The existing [5G status mapper][views], lines 15-21, is a useful compatibility vocabulary, not evidence that every legal state maps to it without loss.

### Availability evidence

Point 16 cannot be accepted as an established provider-wide rule on the evidence permitted in this run. The local [Microsoft availability guide][availability] documents a bounded UTC `getSchedule` wrapper for work/school accounts and excludes delegated personal Microsoft accounts. It does not establish how Internet subscriptions, secondary calendars, Outlook variants, Google scheduling or appointment schedules are aggregated. Neither connector README supplies that missing proof.

Prior knowledge, explicitly unverified here: an Internet subscription is normally separate from an owner's primary calendar; a free/busy query can depend on selected calendar identities, permissions and product-specific scheduling settings. That supports caution, not the blanket claim that `TRANSP` changes only drawing or that a dedicated secondary calendar necessarily protects the owner's availability. I have no current client-documentation verification for those statements because this run forbids remote calls.

Replace the claim with an acceptance matrix: Google and Microsoft account type; primary, dedicated and subscribed calendar; free, busy, tentative, all-day and timed event; display result; direct calendar free/busy result; and the owner's actual scheduling consumer. Include permissions and which calendars that consumer considers. Authorised documentation review and a synthetic live test belong to the private-adapter delivery before promising protection. Provider uncertainty is a merge finding, not an excuse to change the owner's settled boolean.

### Private targets

Point 17 is not implementable through the current tools as described. Exact source predicates and inspection show:

- [Google tool schemas][google-tools], lines 85-103 and 144-167, and [handlers][google-handlers], lines 86-158, create/update timed `dateTime` values, require an end on create, and expose no `transparency`, all-day date write, UID/import or private ownership-metadata field. They support an existing `calendarId`, but not dedicated-calendar creation. Update requires the provider event ID.
- [Microsoft tool schemas][microsoft-tools], lines 72-87, expose no calendar selector, `showAs`, all-day switch, idempotency key or update operation. The [create handler][microsoft-create], lines 10-33, posts to `me/events` using `DEFAULT_TIMEZONE` and returns success text rather than a useful created-event identity. It therefore does not target the proposed dedicated calendar or support UID-based convergence.

These gaps need receiver-owned connector work or another expressly chosen adapter. A write credential alone does not supply the missing contract. Separate three outputs: generated private view, subscribable feed, and account event projection. Account sync is not itself the promised subscription URL and must be presented as an additional target with owner approval, not a silent replacement for it.

For points 14 and 18, distinguish audience policy from access mechanism. An unguessable URL is bearer access, not owner-only authentication; provider sync is also disclosure to that provider and potentially the calendar's delegates. Keep private sets unpublished by default while a target is undecided. Public projections should use an allowlist of approved fields and review source links and descriptions as well as email/phone patterns. The [5G publication rules][fiveg-agents] and [smoke tests][site-tests] show why syntactic contact checks are a backstop, not the whole disclosure boundary.

Any future sync needs dry-run comparison, exclusive ownership of generated events, idempotent retries after partial failure, a mapping from source identity to provider identity, manual-edit conflict policy, stale-state reporting, safe removal and withdrawal of access. Do not silently delete unrelated account events. These are consequences of adding a stateful publication target, not a second editable source of dates. The current [Observatory boundary][observatory] rules it out as a reachable phone/hosted-calendar feed host; a future local renderer or producer is a different question and remains Observatory-owned.

### Migration and views

Point 11 should retain source-specific citations and wording from both 5G representations. The [Industry Day record][industry] has a supplementary citation; the [weekly record][weekly] has source wording distinct from the registry. Verify each mapping before removing its editable duplicate, and retain existing page anchors, feed paths and UIDs.

Point 20 must say what the Live Artifact Markdown owns. Under the [pair contract][live-artifacts], lines 22-35, it can own the view's descriptor, source selection and presentation; dates continue to belong to the registry or Item frontmatter. Generated Markdown data sections must be labelled and rebuilt. Do not make a hand-edited Markdown snapshot a new input simply to satisfy the pair shape. Retaining a generated Mermaid rendering is compatible with the owner's interim decision and the separate diagram-conversion boundary.

Point 21 cannot make viewer-local today universal: the [Command Centre Guide][legal-guide], line 187, explicitly fixes Europe/London's date boundary. With a reader abroad near midnight, adopting the 5G browser-local comparison changes legal's overdue semantics. Use the set's declared zone for date classification, label it, and distinguish that classification from optional reader-local timed display. A base-owned progress state must not be replaced by a generic past flag.

For point 25, a stamp proves neither freshness nor absence of a second editable source. Require declared source manifests, deterministic regeneration or semantic snapshot comparison, provenance and versioned schemas; check generated output against its source. Keep a human audit for undeclared duplicate lists. Include invalid/partial reads, duplicate IDs, missing citations, impossible dates, time-zone ambiguity and stale generation. A failed source read must not look like an empty calendar, especially if sync would remove events. No private data should reach diagnostics or public view JSON by accident.

### Shape and code

Points 22-24 are sound if the new skill owns dated-item semantics and the projection contract, while website, Live Artifact and provider skills keep their existing concerns. One skill need not mean one undifferentiated script. `ki-key-dates` is a defensible plural concern. However, the [naming ADR][naming] does not ban `ki-calendars` or `ki-timelines`, and [ki-diagrams][diagrams] governs authored system diagrams rather than canonical dates. The name choice should rest on discoverability and scope, not an unsupported claim that a diagram type reserves the word timeline.

The [diagram build command][diagrams], line 27, establishes a harness-script precedent. Keep the date model, validation and deterministic projections in a reusable core; separate registry/frontmatter parsers and provider I/O. Dependency-free is valuable for the small ICS core, not a requirement to hand-roll YAML, JSON5 or time-zone conversion. Pin the supported runtime, schema and callable interface. Reuse established harness parsing where suitable. A vendored 5G copy needs exact source provenance, version, tests and a drift check; preserve the 5G product metadata through options if that avoids needless feed changes. `tools-ki` need not gain a command or a registry package for this pilot.

### Adoption

Point 26 is the best first extraction pilot, after the harness skill exists, as the [harness record][harness-record], lines 38-47, requires. Use a fixed build clock for golden comparisons and preserve UIDs, feed URLs, page anchors, source citations, escaping, folding, empty sets and date precision. Compare List content and navigation as well as feed text. New busy properties and configurable branding need intentional expectations, not broad snapshot replacement. A low-risk extraction does not by itself validate timed, private, frontmatter or span support: none is exercised by the present all-day registry.

For points 27-28, bring legal schema discovery and read-only comparison forward, but bring legal publication later. First add synthetic fixtures covering all new semantics. Then prove private delivery, if chosen, with a dedicated synthetic calendar or a small owner-approved personal set. Only after convergence, deletion, free default, all-day handling and the actual availability consumer pass should legal adopt private writes. Legal's date urgency argues for early migration analysis and continued use of its current view, not for being the first high-consequence integration test. This uses the [design-loop pilot rule][design-standard], stage contracts and rollout hand-off, rather than treating parity in one public site as proof of every adapter.

Point 13's authoring can proceed as a separate receiving-base plan. For points 9 and 28, annual birthdays and renewals need an explicit dated occurrence while recurrence is deferred; do not silently roll them forward or suggest recurring-work lifecycle alone supplies calendar recurrence. The [personal evidence][vehicle] supports preserving unknown values rather than inventing dates. Keep each adoption's canonical writes and any provider mutation within that repository's own approval and verification boundary.

## Review outcome

Proceed to merge the reviews with the shared model and one-skill direction intact. Resolve the private target contract and verification plan before declaring account sync ready. Record span exclusion as a proposed v1 policy, fix source/view and identity semantics, and separate the 5G extraction pilot from private-adapter proof. This review accepts no work record and authorises no cross-repository change, deployment or provider write.

[registry]: </Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/src/_data/calendars.json5>
[ics]: </Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/lib/ics.ts>
[views]: </Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/lib/calendars.ts>
[landing]: </Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/src/content/tools/calendars/index.njk>
[calendar-page]: </Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/src/content/tools/calendars/calendar.njk>
[view-js]: </Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/src/assets/js/calendars-view.js>
[calendar-js]: </Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/src/assets/js/calendars.js>
[timeline-collection]: </Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/src/_data/programme-model/timeline/_collection.json5>
[weekly]: </Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/src/_data/programme-model/timeline/weekly-phase-3-consortium-call.json5>
[industry]: </Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/src/_data/programme-model/timeline/industry-day-paris.json5>
[cloudflare]: </Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/docs/guides/developer/cloudflare.md>
[site-tests]: </Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/tests/site.test.ts>
[fiveg-agents]: </Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/AGENTS.md>
[legal-guide]: </Users/krisbrown/workspaces/legal/legal-principal/Pillars/Command Centre/Command Centre Guide.md>
[legal-timeline]: </Users/krisbrown/workspaces/legal/legal-principal/Pillars/Command Centre/Working Notes/XM-CRITICAL-TIMELINE - Critical Timeline and Preparation Checklist/FR Timeline to FDR.md>
[vehicle]: </Users/krisbrown/workspaces/personal/personal-principal/Pillars/Home/Vehicles/YP62 LNY Silver Range Rover Evoque.md>
[diagrams]: </Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-diagrams/SKILL.md>
[live-artifacts]: </Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-kb-live-artifacts/SKILL.md>
[observatory]: </Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/README.md>
[google-readme]: </Users/krisbrown/workspaces/knowledge-islands/mcp-gsuite/README.md>
[microsoft-readme]: </Users/krisbrown/workspaces/knowledge-islands/mcp-m365/README.md>
[google-tools]: </Users/krisbrown/workspaces/knowledge-islands/mcp-gsuite/src/tools/calendar/index.ts>
[google-handlers]: </Users/krisbrown/workspaces/knowledge-islands/mcp-gsuite/src/main/calendar/index.ts>
[microsoft-tools]: </Users/krisbrown/workspaces/knowledge-islands/mcp-m365/src/tools/calendar/index.ts>
[microsoft-create]: </Users/krisbrown/workspaces/knowledge-islands/mcp-m365/src/main/calendar/create.ts>
[availability]: </Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/guides/user/calendar-availability.md>
[naming]: </Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-003-dependency-order-for-multi-skill-composition.md>
[harness-record]: </Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-222-timeline-and-calendar-skill.md>
[personal-instructions]: </Users/krisbrown/.codex/AGENTS.md>
[design-standard]: </Users/krisbrown/.agents/skills/ki-work-design/references/standards-work-design.md>
