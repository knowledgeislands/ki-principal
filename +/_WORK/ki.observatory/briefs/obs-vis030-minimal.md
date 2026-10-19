# obs-vis030-minimal - A minimal Known Lands chart

Work in apps-observatory.local for KI > Model > Observatory (work package ki-principal `+/_WORK/ki.observatory/`; read its `decisions.md`, do not edit the package), under the repository's AGENTS.md, engineering standards and `ki-work-roadmap`.

Kris said under VIS-030-MINIMAL: "I'm working on some designs for this, for now, ... you can put a minimal thing in place and it will be revised, which might be easier for the design work". Build the smallest working Known Lands chart for KI-OBSERVA-VIS-030 on top of the vendored renderer (commit a4ea2ad), shaped so Kris's designs can replace its look and interaction without rework:

- Serve the chart as a read-only SVG image under the existing SVG policy; the page's nonce policy stays unchanged. Add a plain accessible overlay, island names as text and a link or focus to each island's existing view, nothing more.
- One archipelago per territory with its Capital as `ki territory list` declares it, keeping the Capital the territory parser now discards, plus a group for repositories in no territory with no invented Capital.
- The renderer's fixed layout. No saved positions, no write route, no boundary spec change.
- Keep the 760 px rule and width test whole (LARGE-SCREEN-REVISIT, NARROW-DECLARE); retire no tab, route or capability (PUSH-ALL).

Update KI-OBSERVA-VIS-030 to say the minimal chart is in place and that positions (VIS-030-POSITIONS), the fuller interaction and the look await Kris's designs; keep the record in progress. Run the full gate and `ki repo audit`, commit by explicit path, restart the service with `launchctl kickstart -k "gui/$(id -u)/uk.me.kris.rig.observatory"` and check <http://127.0.0.1:1675/> serves the chart and every tab. Do not push. Stop and raise a query where a choice is not covered here.

Report in owner-report shape: Done with commit, checks and the service check; In Progress; Queries with Context, Query and Options and a recommended option with confidence, or `No outstanding queries`.
