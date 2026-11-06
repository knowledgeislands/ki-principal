# Exchange Dynamics Analysis: design note

Design note for [ki.sop.main](../work.md), focus `_emerging`. It answers EDA-METHOD and EDA-METHOD-NAMES, routed by personal.reg.assistant-sol on 4 November 2026 from Kris's words at about 01:00 and 01:05 GMT: "can you route this please for follow up" and "we could actually just pretend anonymized anyway. We don't need know they're real people ... call them random names."

Status: draft. The home is a recommendation awaiting Kris (query EDA-HOME); nothing is built. Source: Kris's note "Knowledge Islands - Exchange Dynamics Analysis (EDA)" and its reference infographic, captured privately in krisb/inbox at `captured/knowledge-islands/intake/2026-11-04-exchange-dynamics-analysis/` (the image in the `sources-assistant` store). The capture stays the evidence of lineage; this note neither copies nor quotes the private conversation.

## Summary

Exchange Dynamics Analysis (EDA) turns a conversation into one structured, evidence-linked analysis - chronology, sentiment kept apart from tension, phases, participants - and then renders that analysis as an infographic, report or interactive view. The governing principle is Kris's: **analyse once, render many ways**.

Recommended home: a **new harness skill, `ki-exchange-dynamics`, in ki-agentic-harness**, holding the methodology, schema, visual specification and agent workflow, and delegating rendering to `archify` and `dataviz`. Ki-principal keeps at most a short Emerging Concepts note pointing to it. Neither existing skill should be extended: both are renderers, EDA is an analysis method.

## Candidate homes

| Candidate | Fit | Verdict |
| --- | --- | --- |
| Extend `archify` | A vendored third-party skill (author tt-a1i, MIT, installed through Rig at `~/.agents/skills/archify`). It draws diagrams and one-page explainers and says "Not for dashboards". Extending it means forking upstream, and it owns no analysis. | No; use as a renderer |
| Extend `dataviz` | An Anthropic-supplied chart-design skill: form heuristic, palette, mark specs. Brand-neutral, not KI-owned, no analysis. | No; use for the graph's design rules |
| Extend `ki-diagrams` | Governs a repository's living system diagrams (sources, SVGs, manifest, freshness). Different object: code-backed diagrams, not conversations. | No |
| Extend `ki-acquire` | Captures sources faithfully; analysis would break its "faithful, lean preservation" boundary. EDA consumes captures, it does not make them. | No; upstream hand-off |
| New harness skill `ki-exchange-dynamics` | Reusable across every island and territory, runtime-neutral, can carry a schema, a validator script, references and an example; discoverable by trigger description. Matches Kris's own package layout (section 7) almost file for file. | **Recommended** |
| Pillars note in ki-principal only | Good for the idea and its lineage, but island-internal, not executable by an agent in another repository, and every change would need the Enactment Process. | Supplementary only |

Family: the harness has no analysis family. `acquire` is closest in spirit (sources in, structured knowledge out) and avoids a one-skill family; a new `analysis` family is the alternative if more methods follow. Recommended: `skills/acquire/ki-exchange-dynamics/`, confidence medium.

## Units of comprehension

| Unit | Boundary | Hand-offs |
| --- | --- | --- |
| Methodology | How an exchange is analysed: event selection, the dynamics dimensions, phase detection, participant reading, scoring and safeguards | Feeds the schema; reads a source transcript, often a `ki-acquire` capture |
| Schema | The machine-readable contract of one analysis | Produced by the agent workflow, validated by a script, consumed by every renderer |
| Visual specification | How an analysis is presented: three-column reference layout, colour vocabulary, responsive and accessible variants | Instructs `archify` (page) and `dataviz` (graph rules); never alters the analysis |
| Agent workflow | The steps an agent follows from ingest to rendered output, with validation gates | Calls methodology, emits schema, hands to a renderer |
| Examples | Worked analyses with invented names | Prove the workflow end to end; carry no real person's material |

Out of scope: capture (owned by `ki-acquire` and its provider skills), storing private originals (the territory's source store), and the future interactive instrument (a later work record).

## Proposed skill layout

```text
skills/acquire/ki-exchange-dynamics/
├── SKILL.md                         modes: analyse | render | audit | help
├── references/
│   ├── methodology.md
│   ├── visual-specification.md
│   ├── agent-workflow.md
│   ├── safeguards.md
│   ├── rubric.md
│   └── sources.md                   lineage: Kris's note of 2026-11-04, capture id only
├── assets/
│   └── eda-analysis.schema.json
├── scripts/
│   ├── validate.ts                  schema plus cross-reference checks
│   └── validate.test.ts
└── examples/
    └── allotment-tool-shed/
        ├── transcript.md            invented exchange
        ├── analysis.json
        └── design-decisions.md
```

Kris's section 7 names `README.md`, `methodology.md`, `schema.json`, `visual-specification.md`, `agent-instructions.md` and `examples/`; the layout keeps each, renaming only to the harness convention (`SKILL.md` as entry, `references/`, `assets/`).

## Methodology outline (`references/methodology.md`)

1. **Scope the exchange.** Record source kind (messaging, email, meeting transcript, human-AI or multi-agent), span, participants, completeness and what is missing. An incomplete transcript is stated, never smoothed over.
2. **Select events.** Choose contributions that change the exchange - a new position, a challenge, a concession, a turn - not an even sample. The count adapts: about five for a simple exchange, twenty or more for a long negotiation. Each event keeps its exact quotation and a source reference.
3. **Read dynamics on separate axes.** Sentiment (emotional tone, -5 to +5) and tension (confrontation, 0 to 10) are scored independently for every event, each with a one-line basis. Further tags: defensiveness, cooperation, escalation or de-escalation, perspective change, turning point.
4. **Detect phases.** Group consecutive events where the dynamics shift; label from a descriptive vocabulary (opening, challenge, escalation, clarification, mediation, de-escalation, resolution, unresolved disagreement) without forcing a sequence. Boundaries come from the material.
5. **Read participants.** Dominant tone, conversational role, assertiveness, constructive or confrontational contributions, change over time, each with evidence and an alternative reading. Behaviour within this exchange only; no personality claims.
6. **Conclude.** Key takeaways and an overall read: character of the exchange, sources of tension or misunderstanding, turning points, degree of resolution, uncertainties.
7. **Validate.** Every conclusion traces to events; every event to a source reference; scores carry a basis; alternatives kept where evidence allows.

Four layers are kept apart in every record: **observation** (what was said), **interpretation** (what it does in the exchange), **inference** (a possible motive, always marked as such) and **uncertainty**. Kris's ten mandatory principles go into `safeguards.md` verbatim in substance, with a stronger tier for legal, employment and other sensitive contexts: no named real person in any shared rendering without consent, and the analysis stays in the private store with its source.

## Schema outline (`assets/eda-analysis.schema.json`)

JSON Schema, versioned (`schema_version`), one document per analysis:

- `exchange` - id, title, source kind, span, language, completeness, missing context, sensitivity.
- `participants[]` - id, display name, avatar reference or initials, `tone`, `role`, `assertiveness`, `trajectory`, `evidence[]` (event ids), `alternatives[]`, `confidence`.
- `messages[]` - optional full source index: id, speaker, timestamp, text or reference.
- `events[]` - `id` (sequence), `speaker`, `timestamp`, `quotation` (verbatim), `context`, `interpretation`, `contribution`, `sentiment` {label, score, basis}, `tension` {score, band, basis}, `tags[]`, `phase`, `evidence[]` (message ids), `confidence`, `inference` (optional, marked).
- `phases[]` - id, label, event range, description.
- `takeaways[]` - text, supporting event ids.
- `overall` - character, tension sources, turning points, resolution, uncertainties, alternatives.
- `rendering` - requested outputs, layout variant, palette, which scores to display.

The validator checks the schema plus cross-references: every event's phase exists, phases cover events without gaps or overlaps, every takeaway and participant claim cites an event, tension bands match scores, and quotations appear in the source where one is supplied.

## Visual specification outline (`references/visual-specification.md`)

- **Reference layout:** wide landscape, three columns. Left, full height: numbered chronology, each event with marker, speaker, timestamp, quotation and one-line analysis. Centre: tension trajectory (x = event number, y = tension 0-10, numbered points joined, sentiment as a separate secondary line or marker shape, never merged), phase bands with their summaries, then key takeaways. Right: participant cards (avatar only where supplied and appropriate, otherwise initials; never invented likenesses), style label, evidence-based role, optional contribution indicator, and the overall read at the foot.
- **Colour vocabulary:** one scale across chronology, graph and phases - green low or constructive (0-2), yellow moderate (3-4), amber elevated (5-7), red high or confrontational (8-10). Colour encodes tension only, never who is right, and always pairs with a text label; `dataviz`'s validator checks contrast in light and dark.
- **Variants:** stacked mobile order (overall read, graph, chronology, participants), Markdown report (same sections, tables in place of the graph), PDF.
- **Renderer mapping:** `archify` explainer for the one-page infographic (conclusion first, panels, native chart); `dataviz` rules for the trajectory chart; a plain Markdown renderer from the schema for reports. Any renderer reads `analysis.json` only.
- **Future interactive view** (Kris's section 8): selectable events revealing source evidence, filters by participant, phase or sentiment, alternative-reading comparison, export. Recorded as a later capability, not part of the first build.

## Agent workflow outline (`references/agent-workflow.md`)

1. Ingest the source exchange; record provenance and gaps.
2. Identify participants and chronology; assign stable participant ids.
3. Select significant events.
4. Preserve and reference verbatim quotations.
5. Score sentiment and tension separately, each with its basis.
6. Detect phase transitions.
7. Assess participant roles with evidence and alternatives.
8. Write key takeaways and the overall read.
9. Run `scripts/validate.ts`; repair until it passes.
10. Emit `analysis.json` beside the source, in the same privacy tier.
11. Render through the available renderer; record the renderer, variant and prompt in `design-decisions.md`.

Modes: `analyse` (steps 1-10), `render` (step 11 from an existing analysis), `audit` (rubric over an analysis and its renderings), `help`.

## Worked example (invented)

Per Kris on 4 November, the example uses invented names and an invented exchange; nothing is drawn from the captured conversation. A community allotment group's chat about a new rule for the shared tool shed, six participants: **Nell Ashby**, **Tobias Wren**, **Saoirse Doyle**, **Hamid Raza**, **Greta Lund** and **Felix Okafor**.

| # | Speaker | Quotation (invented) | Tension | Phase |
| --- | --- | --- | --- | --- |
| 1 | Nell | "From Monday the shed key lives in the lockbox - code goes out tonight." | 2 green | Opening |
| 2 | Felix | "Nobody asked us. I've had a key for six years." | 6 amber | Challenge |
| 3 | Tobias | "It was in last month's minutes, Felix." | 7 amber | Escalation |
| 4 | Felix | "Minutes nobody reads aren't consultation." | 8 red | Escalation |
| 5 | Saoirse | "Can I check - is this about the missing strimmer?" | 5 amber | Clarification |
| 6 | Nell | "Partly. Mostly insurance wants a log of who goes in." | 4 yellow | Clarification |
| 7 | Hamid | "Could Felix keep his key and just sign the log too?" | 3 yellow | Mediation |
| 8 | Felix | "That I can live with." | 2 green | De-escalation |
| 9 | Greta | "Shall we put the lockbox idea to the March meeting properly?" | 2 green | Resolution, partial |

Sentiment runs separately: event 5 is anxious in tone yet lowers tension, and event 3 is polite in form yet raises it - the case the method exists to show. The overall read would note the source of tension as process (consultation) more than the rule itself, with the strimmer as an unconfirmed inference. The full example ships as `transcript.md`, `analysis.json` and `design-decisions.md`.

## Privacy and the reference image

The original infographic names and quotes real private individuals. It stays in the private capture and the `sources-inbox` store; it is **not** copied into the public harness, which departs from Kris's section 7 (`infographic-original.png` in `examples/`). The public example is re-rendered from the invented analysis instead, and `sources.md` cites the capture id as lineage. The capture also records that the transcript and the image's generation context were never supplied, so the design decisions of the original cannot be preserved beyond what the image shows.

## Build plan, once the home is chosen

1. ki-agentic-harness: one work record for the skill (its owner captures it on receipt of a message line), built under `ki-skills`, with the schema, validator and tests passing its gates.
2. ki-principal: optional Emerging Concepts note "Exchange Dynamics Analysis" giving the idea, Kris's principle and lineage, pointing to the skill; through the Enactment Process.
3. Discovery: the skill's trigger description ("analyse a conversation, chat, thread or meeting for its dynamics, sentiment, tension, phases or participants"); a line in the ways-of-working guidance once adopted.
4. Later: the interactive view as its own record.

## Queries

EDA-HOME - where the method lives. Options: a) new harness skill `ki-exchange-dynamics` under `skills/acquire/`, with an optional pointer note in ki-principal (recommended, confidence medium); b) the same skill in a new `analysis` family; c) a Pillars note in ki-principal only; d) extend `archify` or `dataviz`. Carried to Kris in the run report.
