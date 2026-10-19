# obs-tabbar-review - Blind review of TAB-ROOM

This is a read-only blind review run for KI > Model > Observatory, under QUERY-REVIEW. In apps-observatory.local, read KI-OBSERVA-VIS-030 (`docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md`), `apps/site/src/layout.test.ts` (the 1,440 px tab-bar fit and the 760 px rule), `apps/site/src/shell.test.ts`, the tab registry and titles, PDR-KI-OBSERVA-002, and the unmerged tab saved at `/var/folders/6b/b4c73j8s6w12g2k9_yl652_h0000gn/T/ki-agents/observatory/obs-vis030-minimal/tab/`. Read Kris's words in ki-principal `+/_WORK/ki.observatory/decisions.md`, especially PUSH-ALL, DESIGN-APPLY, LARGE-SCREEN-REVISIT, NARROW-DECLARE and VIS-030-MINIMAL (a minimal chart now, to be revised by Kris's designs). Give your own recommended option with a confidence of `high`, `medium` or `low` and a one-line reason; you may propose a course not listed. Change nothing and commit nothing.

**Context:** The minimal Known Lands chart's backend is committed (21be3a6). Adding it as a sixteenth tab breaks the test that every tab fits the bar without scrolling at a 1,440 px window: fifteen tabs take 1,341 of 1,392 px, and any sixteenth tab overflows, even one titled `map` (1,398 px). The 760 px rule is unaffected.

**Query:** How should the bar make room for the Known Lands tab?

**Options:**

a) Shorten one existing tab's title, for example `review queue` to `review`, saving about 42 px so sixteen tabs fit (about 1,356 px).

b) Add the tab and let the bar scroll at 1,440 px with its existing fade, changing the wide-window part of the width test.

c) Add no tab yet; show the minimal chart at the top of an existing view, such as Trade routes, until the designs place it.

d) Tighten the spacing between tabs in the stylesheet, changing the look ahead of the designs.

Report in owner-report shape, kept short: Done gives your option, confidence, reason and the evidence checked. Queries: `No outstanding queries`.
