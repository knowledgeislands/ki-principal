# obs-step3-review - Blind review of five step 3 queries

This is a read-only blind review run for KI > Model > Observatory, under QUERY-REVIEW. Work in apps-observatory.local: read the records named, the page's content security policy and SVG route, the vendored ki-design hex chart renderer (commit a4ea2ad), the Act board operations and the Observatory's territory summary. Read Kris's words in ki-principal `+/_WORK/ki.observatory/decisions.md`, especially PUSH-ALL, STEP3-ANSWERS, HEXMAP, CAPITAL-GLYPH, LARGE-SCREEN-REVISIT and GET-MOVING. For each query, give your own recommended option with a confidence of `high`, `medium` or `low` and a one-line reason. You may propose a course that is not listed. Change nothing and commit nothing.

## VIS-030-CHART-DELIVERY (KI-OBSERVA-VIS-030)

Context: the page's content security policy uses a nonce; the vendored renderer emits an SVG with an inline style. Query: how should the Known Lands chart reach the page? Options: a) serve the chart from a read-only image route under the existing SVG policy, with script drawing focus, selection and signals on an overlay; b) draw the chart in the browser from the renderer's model, with no served SVG; c) relax the style policy for the chart.

## VIS-030-POSITIONS (KI-OBSERVA-VIS-030)

Context: the renderer lays islands out deterministically, Capital at the centre; a position store would need a new POST route and a boundary spec change. Query: should KI-OBSERVA-VIS-030 still keep island positions? Options: a) drop the position store and use the deterministic layout; b) keep a host preference under XDG state behind a new POST route.

## VIS-030-ESTATE (KI-OBSERVA-VIS-030)

Context: `ki territory list` names each territory's Capital, but the Observatory's territory summary drops it, and some repositories belong to no territory. Query: how should the estate view be composed? Options: a) one archipelago per territory, Capital from `ki`, plus a group for repositories in no territory; b) one estate archipelago with ki-principal as its Capital.

## BRG-005-COUNTS (KI-OBSERVA-BRG-005)

Context: the record wants counts on confirm and receipt, but every Act operation acts on one target, the record excludes batch operations, and it is a triage record. Query: how should the Act board counts be handled? Options: a) show a count of 1 now and leave batch operations to a later record; b) add batch operations; c) leave the counts out.

## VIS-031-TABLES (KI-OBSERVA-VIS-031)

Context: the who-is-working record still needs a decision on which tables carry the worker column. Query: which tables carry it? Options: a) Repositories and Roadmap rows, plus what each run touches on Sessions; b) Repositories only, at first.

Report in owner-report shape, kept short: Done gives, per query tag, your option, confidence, reason and the evidence checked. Queries: `No outstanding queries`.
