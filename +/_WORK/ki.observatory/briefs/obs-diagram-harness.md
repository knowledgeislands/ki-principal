# obs-diagram-harness

Work: KI > Model > Observatory. Repository: ki-agentic-harness. Decisions: `+/_WORK/ki.observatory/decisions.md` in ki-principal (NO-MERMAID, DIAGRAM-STANDARD, DIAGRAM-REPLACE, RECOMMENDED). Background: the obs-diagrams report at `~/.local/state/ki/agents/observatory/obs-diagrams.report.md`.

Kris decided on 19 October ("Go with recommendations"):

- DIAGRAM-STANDARD a): Archify is the one diagram standard, extended to the islands, with a KI-theme export (ki-design palette, fonts and glyphs; SVGs that stay readable in viewers that don't run Archify's CSS), D2 only for diagrams generated from code, on the tokens. Mermaid is excluded.
- DIAGRAM-NAME a): the skill keeps the name `ki-diagrams` (ADR-KI-HARNESS-SKILLS-003).
- DIAGRAM-REPLACE: every Mermaid diagram Archify can carry is replaced; others are flagged to Kris.

Under the cross-repository choreography, add handoff items; the harness owns priority and execution:

1. Fold the KI-theme export into KI-HARNESS-GOV-205 as scope, with Kris's decision quoted and dated.
2. Add a roadmap record (or item in an existing one) for a `ki-diagrams` audit check that warns on Mermaid fences.
3. If `ki-diagrams` text contradicts the decision, propose the wording in the record; do not edit the skill unless the change is a sentence the decision fixes outright, and then regenerate as the harness requires.

Run the harness roadmap audit and gate; commit by explicit path; push fast-forward only your own commits. Report in one short owner report with record links and any query.
