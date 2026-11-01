# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-diagrams

**🤖 → 👤 Handoff to supervisor · Run report at 07:52 BST · last mark 20:20 BST**

---

## Done

- Read-only review, no commits and nothing pushed. This file is the only thing I wrote. The progress protocol names it as the only report path, so I wrote nothing to the work folder.
- I found [`ki-diagrams`](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-diagrams/SKILL.md) in ki-agentic-harness. [Its standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-diagrams/references/standards-diagrams.md) offers two options:
  - **Archify**, the adopted tool. It keeps a JSON source traced to files and lines, a committed SVG with a night default and a day theme, and an optional interactive HTML viewer.
  - **D2**, named as the only worthwhile addition, and only for maps generated mechanically from code. It has no interactive view.
  - The standard already excludes Mermaid and Graphviz at your direction.
- Archify against the ki-design system (`ki-design` [DESIGN.md](/Users/krisbrown/workspaces/knowledge-islands/ki-design/DESIGN.md), [maps.md](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/spec/maps.md), which is the old §13, typography and tokens). Where it fits:
  - It is night first, with a day theme under `prefers-color-scheme`, and night is the design's reference.
  - It renders flat SVG, which matches the Modern style that DESIGN.md names as the default for diagrams.
  - It is local only, has a committable source and has a text-searchable viewer.
- Where Archify breaks the ki-design hard rules:
  - It uses its own slate, teal and orange palette, not tokens. This breaks rule 2.
  - It inlines JetBrains Mono into every SVG, which breaks the Instrument rule "nothing fetched or bundled". The token should be `font.mono`.
  - Its node icons and brand marks are not the 72 KI glyphs, and third-party logos are banned as glyphs.
  - Its dual-theme SVG goes black in viewers that don't run its CSS, such as Zed and `rsvg-convert`. That is already recorded as triage record [KI-HARNESS-GOV-205](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-205-static-light-diagram-export.md).
- D2 against the same rules: its themes and fonts can be configured, so it can be brought onto tokens. However, it is a second source language, has no viewer, and its looks were judged only adequate in the 3 October review.
- The `ki-diagrams` standard is stale against the installed Archify 3.1:
  - The standard lists five types and "no tree layout". Archify 3.1 has ten types: it adds `erd`, `tree`, `class`, `timeline` and `waterfall`.
  - Archify 3.1 now **accepts Mermaid as input**. It maps `flowchart` onto workflow or architecture, `sequenceDiagram` onto sequence, `stateDiagram` onto lifecycle, `erDiagram` onto erd and `classDiagram` onto class. That makes it the migration route.
- Where diagrams live:
  - **Code repositories:** only `ki-agentic-harness` and `apps-observatory.local` keep `docs/diagrams/`, with 12 and 7 Archify sources.
  - **Islands:** no knowledge-base island has a diagram home. The Aesthetics [Diagrams](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Aesthetics/Diagrams/Diagrams.md) canon holds PNGs.
  - **Observatory:** it serves Archify SVGs at `/api/diagrams`, and it draws Mermaid in Markdown inside a sandboxed frame under `PDR-KI-OBSERVA-005`.
  - **Websites:** they use the Chart style, and DESIGN.md gives the site's poster explainers the separate Illustrated explainer style.
- Mermaid inventory (only `.md` files were counted, so the figures are a lower bound): 34 fences in 24 files across 9 repositories. Of those, 19 are in hnr-shared, 3 in `apps-observatory.local` roadmap records, 3 in apps-tower, and 2 each in ki-principal, ki-specifications and legal-principal. The other 3 are one each in personal-principal, er-principal and apps-vallearmonia. One of the ki-principal pair is the canonical Pillars note [Acquisition Process](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Acquisition Process/Acquisition Process.md>), and the other is [design/live-artifacts.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/design/live-artifacts.md), the obs-extensions redraw. The `paperclip` fork (5 files) and the `acquire` capture (1) are upstream text and evidence, so they stay as they are.
- `ki-diagrams` against the naming rule: [ADR-KI-HARNESS-SKILLS-003](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-003-dependency-order-for-multi-skill-composition.md) says a concern is plural "for a collection or repeated unit (`ki-skills`, `ki-decision-records`, `ki-trades`)" and singular for "a discipline" (`ki-authoring`). `ki-diagrams` governs a repeated unit with a manifest, so it conforms. The name appears in 67 harness files and in `ki-agentic-harness/.ki.toml`.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Whichever way you answer, the `ki-diagrams` standard needs a refresh to Archify 3.1, covering the ten types and the Mermaid input. That is harness work for its owner.
- The obs-extensions Mermaid redraw (`42e1e77`) is still there. It would be the first diagram converted under the migration.

## Queries

### DIAGRAM-STANDARD - Which diagram standard replaces Mermaid

**Context:** Archify is already the standard, and two code repositories use it. Out of the box it breaks four ki-design rules: palette, bundled font, glyphs, and rendering in viewers that don't run its CSS. A "KI theme" export would fix all four. It would extend the triage record KI-HARNESS-GOV-205 in the exporter: colours mapped from `packages/tokens` for night and day, plain colour attributes so any viewer renders it, the `font.mono` system stack instead of JetBrains Mono, and KI glyphs where the symbol library has the meaning. The JSON source and the interactive viewer stay as they are. D2 would add a second source language for little gain. Islands would embed the SVG beside its note in Markdown, which Obsidian and GitHub both render. The Observatory would keep `/api/diagrams`. Websites would use Archify for technical diagrams and the Illustrated explainer style for posters.

**Query:** Should the one standard be Archify through `ki-diagrams`, with a KI-themed static export built into its exporter?

**Options:**

a) (recommended, confidence medium - Archify is proven in two repositories and reads Mermaid, but the theme layer is unbuilt and depends on Archify's CSS variables staying stable) Archify through `ki-diagrams`, plus a KI theme export folded into KI-HARNESS-GOV-205. The standard is extended to knowledge-base islands, with the SVG beside its note. D2 stays allowed only for maps generated from code, on tokens.

b) Archify as it is, with only KI-HARNESS-GOV-205's flattened light export. This is quicker, but it keeps Archify's palette and font, outside ki-design.

c) D2 for every diagram, on a KI theme. This needs one source language and is themable, but it loses the interactive viewer and the existing 19 Archify diagrams would have to be redrawn.

### DIAGRAM-MIGRATION - How existing Mermaid moves without loss

**Context:** There are 34 Mermaid fences in 24 files across 9 repositories. Archify 3.1 converts them by meaning, not by style. Under PUSH-ALL nothing may be lost, and each island owns its own notes. The Pillars note needs the Enactment Process. The Observatory's sandboxed Mermaid renderer is the only way to read Mermaid that stays behind, such as the Paperclip fork and the captures. NO-MERMAID forbids drawing new Mermaid; reading old Mermaid is a separate question.

**Query:** How should the existing Mermaid diagrams be migrated?

**Options:**

a) (recommended, confidence medium - the side-by-side step keeps the PUSH-ALL guarantee, but the per-repository handoffs are slow and hnr-shared alone has 19 fences) Pilot on the two ki-principal diagrams and the three Observatory ones. In each note, the new SVG sits above the original fence, which is kept in a collapsed `<details>` block until you sign off, and only then removed so that Git holds it. Each other repository gets a handoff item and converts its own diagrams. A `ki-diagrams` audit item warns on any Mermaid fence. The Observatory keeps its renderer, read-only, for Mermaid that is foreign or not yet converted.

b) A single run converts every fence in all 9 repositories, side by side, under your cross-repository instruction.

c) Leave the existing Mermaid alone and forbid only new Mermaid.

### DIAGRAM-NAME - `ki-diagrams` or `ki-diagramming`

**Context:** ADR-KI-HARNESS-SKILLS-003 sets plural names for a collection or repeated unit and singular names for a discipline. `ki-diagrams` governs diagram artefacts and their manifest, as `ki-decision-records` and `ki-trades` govern theirs, so it conforms. `ki-diagramming` would fit only if the skill became a drawing practice, like `ki-authoring`, rather than a standard for kept diagrams. Renaming touches 67 harness files, the rubric host id `ki repo audit --skill ki-diagrams` and every adopting `.ki.toml`.

**Query:** Keep the name `ki-diagrams`, or rename it `ki-diagramming`?

**Options:**

a) (recommended, confidence high - checked directly against the naming grammar, and nothing to undo) Keep `ki-diagrams`. Widening it to islands and websites still governs a repeated unit.

b) Rename it `ki-diagramming` and recast it as the discipline of drawing every KI diagram. The rename would need its own harness record.
