# obs-declare-review - Blind review of NARROW-DECLARE

This is a read-only blind review run for KI > Model > Observatory, under QUERY-REVIEW. In apps-observatory.local, look at PDR-KI-OBSERVA-002, the width test in `apps/site/src/layout.test.ts`, the declaration check in `packages/instruments/src/registry.test.ts`, and how existing tables declare their columns, for example in `packages/instruments/src/repositories.ts`. Read Kris's words under LARGE-SCREEN and LARGE-SCREEN-REVISIT in ki-principal `+/_WORK/ki.observatory/decisions.md`. Then give your own recommended option with a confidence of `high`, `medium` or `low` and a one-line reason. You may propose a course that is not listed. Change nothing and commit nothing.

**Context:** The Observatory is designed first for large screens, but not only for them. The shipped 760 px column-dropping behaviour and its width test are kept, and new work need not plan narrow layouts beyond what comes cheaply. The test requires every instrument that renders a table to declare which columns survive and which drop at 760 px.

**Query:** Should new tables keep declaring their dropped columns, or may a new table opt out of the declaration?

**Options:**

a) Keep the requirement as it is.

b) Let a new table declare "no narrow plan", which the test accepts while still enforcing no horizontal scroll.

c) Decide when the first consolidation is delivered.

Report in owner-report shape, kept short: Done gives your recommended option, confidence, reason and the evidence you checked. Queries: `No outstanding queries`.
