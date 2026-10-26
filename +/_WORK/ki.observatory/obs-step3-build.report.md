# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-step3-build

**🤖 → 👤 Handoff to supervisor · Run report at 20:57 BST · last mark 20:57 BST**

---

## Done

- [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) steps 2 and 3: the ki-design hex chart renderer and its tokens are vendored by script from the pinned commit, with a per-file drift check, and the `capital` glyph is added. Commit a4ea2ad. Full gate and `ki repo audit` passed. The record stays in progress.
- [KI-OBSERVA-BCN-008 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/22ea8dcbf7fba0806f1370899cd506a6705c3741/docs/roadmap/KI-OBSERVA-BCN-008-beacon-signal-anatomy.md) Beacon signal anatomy. Each row now shows a reef or lantern sign or an outline tag for its severity, its kind, and how much older its evidence is than the reading. The list filters and groups by kind, and choosing a row opens a detail pane. Commit 23f2ba5. Full gate, with the density, width and degraded tests unchanged, and `ki repo audit` passed with no failure. Set to awaiting-review, not done, because this run may not accept records. Condition is left out until the `.ki.toml` maturity source exists.
- Service restarted. The page and all 15 tabs answer 200, `/api/beacon` answers, and the new Beacon parts are served.

## In Progress

- [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md): the position store and the `known-lands` instrument are unbuilt and wait on the queries below.
- I stopped early, with time left, because every other step 3 record needs a decision the authorised answers don't cover. Nothing is pushed: apps-observatory.local on this Mac, branch `main`, has a4ea2ad and 23f2ba5 unpushed.

## Queries

**VIS-030-CHART-DELIVERY**

**Context:** The page's content security policy uses a nonce, and the vendored renderer emits an SVG with an inline style.

**Query:** How should the Known Lands chart reach the page?

**Options:** a) (recommended, confidence medium - this keeps the CSP unchanged and reuses the existing SVG policy) Serve the chart from a read-only image route under the SVG policy, and have the script draw focus, selection and signals on an overlay. b) Draw the chart in the browser from the renderer's model, with no served SVG. c) Relax the style policy for the chart.

**VIS-030-POSITIONS**

**Context:** The renderer lays islands out deterministically, with the Capital at the centre. A position store would need a new POST route and a change to the boundary spec.

**Query:** Should [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) still keep island positions?

**Options:** a) (recommended, confidence medium - this adds no write route, and the layout is already stable) Drop the position store and use the deterministic layout. b) Keep a host preference under XDG state behind a new POST route.

**VIS-030-ESTATE**

**Context:** `ki territory list` names each territory's Capital, but the Observatory's territory summary drops it, and some repositories belong to no territory.

**Query:** How should the estate view be composed?

**Options:** a) (recommended, confidence medium - this follows the renderer's one Capital per archipelago) Draw one archipelago per territory, with its Capital from `ki`, plus a group of repositories in no territory. b) Draw one estate archipelago with ki-principal as its Capital.

**BRG-005-COUNTS**

**Context:** [KI-OBSERVA-BRG-005](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-005-act-board-missing-parts.md) wants counts on confirm and receipt, but every operation acts on one target, the record excludes batch operations, and it is a triage record that authorises no adoption.

**Query:** How should the Act board counts be handled?

**Options:** a) (recommended, confidence medium - this is honest with today's single-target operations) Show a count of 1 now and leave batch operations for a later record. b) Add batch operations. c) Leave the counts out.

**VIS-031-TABLES**

**Context:** [KI-OBSERVA-VIS-031 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/24c4bd8bfb1956c5ee9e0e2beef846bd06e298a5/docs/roadmap/KI-OBSERVA-VIS-031-who-is-working.md) still needs a decision on which tables carry the worker column.

**Query:** Which tables should carry it?

**Options:** a) (recommended, confidence low - these are the tables where runs and authors meet repositories) Repositories and Roadmap rows, plus what each run touches on Sessions. b) Repositories only, at first.
