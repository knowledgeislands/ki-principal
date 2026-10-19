# obs-overlay-review - Blind review of OVERLAY-COMMITTED

This is a read-only blind review run for KI > Model > Observatory, under QUERY-REVIEW. Check what you can directly: how Archify interactive viewers are generated and committed in ki-agentic-harness and the 5G Emerge sites, and KI-OBSERVA-VIS-042 in apps-observatory.local. Then give your own recommended option with a confidence of `high`, `medium` or `low` and a one-line reason. You may propose a course that is not listed. Change nothing and commit nothing.

**Context:** Some Archify diagrams have their interactive viewer saved in Git as a generated HTML file, rather than built on this Mac when it is needed. A saved viewer is written only when someone re-renders it. If the diagram's source changes and nobody re-renders, the saved viewer silently falls behind. Kris assumed the two were always in sync. KI-OBSERVA-VIS-042 would add an **Interactive** button to the Observatory that opens these viewers.

**Query:** How should saved viewers be kept in sync, and should the Interactive button open them?

**Options:**

a) Make sync mechanical: a harness check, run in `ki repo audit` and at commit, fails when a saved viewer is older than its source, and the render step re-renders it. The button then opens saved viewers with no flag.

b) Leave sync as it is: the button opens saved viewers with a "may be out of date" flag when the dates differ.

c) Open only viewers built on this Mac.

Report in owner-report shape, kept short: Done gives your recommended option, confidence, reason and the evidence you checked. Queries: `No outstanding queries`.
