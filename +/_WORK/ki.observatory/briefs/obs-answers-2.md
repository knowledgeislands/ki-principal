# obs-answers-2 - Fold OVERLAY-SYNC and LARGE-SCREEN-REVISIT into the Observatory records

This run is for KI > Model > Observatory (`ki.observatory`) in apps-observatory.local. Kris's words are in ki-principal `+/_WORK/ki.observatory/decisions.md` under OVERLAY-SYNC and LARGE-SCREEN-REVISIT.

1. LARGE-SCREEN-REVISIT: the Observatory is designed first for large screens, but not only for them.
   - Keep the shipped 760 px column-dropping behaviour, PDR-KI-OBSERVA-002's rule and the width test.
   - New work need not plan narrow layouts beyond what comes cheaply.
   - Reword KI-OBSERVA-APP-044 so that it no longer retires the rule or the test. Reword the LARGE-SCREEN text that obs-accept-answers added to KI-OBSERVA-BCN-008, KI-OBSERVA-VIS-030 and KI-OBSERVA-VIS-031 to match. Remove nothing that already works.
   - If the requirement for every new table to declare its dropped columns gets in the way of the "only where cheap" intent, say so as a query rather than changing it.
2. OVERLAY-SYNC: update KI-OBSERVA-VIS-042.
   - The Interactive button opens a saved viewer only when its hash receipt matches the current source and HTML, and otherwise shows the viewer as stale.
   - The same verification applies to viewers built on this Mac.
   - The receipt contract comes from a harness record that obs-viewer-sync is writing now. Note the dependency; once that record exists in ki-agentic-harness `docs/roadmap/`, link it at its local path.
3. Run `ki repo audit` on the roadmap and `rumdl`. Commit by explicit path under `ki-git`. Do not push, because Kris pushes. Touch no other repository and do not restart the service.

Report in owner-report shape, kept short: Done lists each record changed. Queries holds only what needs Kris.
