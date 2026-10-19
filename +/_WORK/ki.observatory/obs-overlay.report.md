# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-overlay

**🤖 → 👤 Handoff to supervisor · Run report at 11:10 BST · last mark 08:47 BST**

---

## Done

Answer to Kris: yes, and the Observatory already has the overlay. It has an **Interactive** chip on the figure that opens the full Archify viewer in an overlay or a new tab, built more strictly than the phase sites' version: sandboxed, with Escape forwarded by message.

The gap is reach. The chip appears only on top-level `docs/diagrams/` pairs that have a local `tmp/` build. Diagrams embedded in prose (record figures, documents, and every Mermaid replacement under DIAGRAM-REPLACE) get no chip, and nor do viewers committed under the `ki-diagrams` manifest's `commit_html`.

Captured [KI-OBSERVA-VIS-042](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-042-diagram-overlay-everywhere.md) as triage. It quotes Kris's words and proposes four changes: list diagrams by the manifest, serve committed viewers under the same confinement, put the chip on prose-embedded Archify SVGs, and add Previous and Next as phase 3 has them. Its dependencies are KI-OBSERVA-VIS-041, KI-OBSERVA-APP-042, obs-diagram-migrate and the manifest's stability. KI-HARNESS-GOV-205 is related but not a blocker, because it changes only the SVG figure, not the viewer.

The phase sites use Archify's self-contained delivered HTML (MIT, tt-a1i, no external references, so it fits the Observatory's offline content security policy), an Eleventy shortcode and about 200 lines of `diagrams.js`. Archify is pinned by `skills-lock.json` and not vendored.

Commits `a6f6c05` (number reserved) and `eaa8495` (record), both pushed fast-forward to `origin/main`. The roadmap audit passes; its 33 warnings are size fields missing from older records, none in the new one. The authoring audit passes with one existing `.rumdl.toml` drift warning outside scope.

## In Progress

Nothing. Nothing was built, so no service restart is due.

## Queries

**Context:** A viewer committed under the manifest can fall behind its source, where a local build is fresh by construction. The manifest's `last_checked` field, compared with the source's last commit, could flag a stale viewer on the figure. **Query:** Should KI-OBSERVA-VIS-042 open committed viewers as well as local builds? **Options:** a) (recommended, confidence medium - the harness already commits twelve, and the staleness flag closes an open gap in the specification) Yes, with a staleness flag from `last_checked`. b) Yes, without a flag. c) No, local builds only, so that committed viewers stay invisible.
