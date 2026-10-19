# obs-diagram-migrate

Work: KI > Model > Observatory. Decisions: `+/_WORK/ki.observatory/decisions.md` in ki-principal (DIAGRAM-STANDARD, DIAGRAM-REPLACE, RECOMMENDED). Background: the obs-diagrams report at `~/.local/state/ki/agents/observatory/obs-diagrams.report.md`, which counted 34 Mermaid fences in 24 files across 9 repositories. Use `ki-diagrams` and Archify.

Kris on 19 October: "if they can be replaced with archify they should be, e.g. activity diagrams. Flag any others that don't and I'll decide about them too", and DIAGRAM-MIGRATION a).

1. Classify all 34: Archify carries it (by meaning, not just syntax) or not, with one line of reason for each "not".
2. Pilot: replace the two ki-principal diagrams (the canonical Acquisition Process note included; Kris's explicit instruction stands in for an Enactment record, cite it in the commit) and the Observatory ones (apps-observatory.local and `+/_WORK/ki.observatory/design/live-artifacts.md`). Put the Archify diagram above the original and keep the original in a collapsed `<details>` block until Kris signs off. Use the plain light export until the KI-theme export (KI-HARNESS-GOV-205) lands, and note that it will be re-exported.
3. Every other repository: hand it its own conversion list. KI repositories under the cross-repository choreography: a roadmap handoff item. Repositories outside the Knowledge Islands territory (such as hnr-shared): a trade through `ki-trade`. Change nothing in their notes.
4. The Observatory keeps its read-only Mermaid renderer.
5. Never commit screenshots or fixtures from real estate data. Never restart the Observatory service. Touch no file another session has dirty; name it instead.

Run each repository's gate; commit by explicit path; push fast-forward only your own commits. Report in one short owner report: the pilot, the handoffs, and one query listing every diagram Archify cannot carry, by file, with options.
