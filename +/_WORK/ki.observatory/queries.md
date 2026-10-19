# ki.observatory queries

## Open

### OVERLAY-COMMITTED - Keeping saved diagram viewers in sync

since 2026-10-19 · reworded after Kris asked at 19:44 BST why a saved viewer could differ from its diagram; reviewed by [obs-overlay-review](/Users/krisbrown/.local/state/ki/agents/observatory/obs-overlay-review.report.md)

**Context:** Twelve harness diagrams, and the 5G Emerge phase 2 and 3 sites, save their interactive viewer in Git as a generated HTML file. That file is rewritten only when someone re-renders the diagram. Nothing checks it at commit or in audit, so if the source changes and nobody re-renders, the saved viewer falls behind without anyone noticing. The review found none out of step today. Two phase 2 receipts already record content hashes of source and HTML, and both match. Dates can't prove the two match, but hashes can. [KI-OBSERVA-VIS-042](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-042-diagram-overlay-everywhere.md) would add an **Interactive** button that opens these viewers.

**Query:** How should saved viewers be kept in sync, and when should the Interactive button open them?

**Options:**

a) (recommended, confidence high - reviewed, hashes prove a match where dates cannot) Make sync mechanical. Rendering writes the HTML together with a receipt of the source and HTML hashes, and `ki repo audit` and the commit check fail when the receipt is missing or doesn't match. The button opens a viewer only when its receipt matches, and otherwise shows it as stale. This needs a harness record and an update to KI-OBSERVA-VIS-042.

b) Leave sync as it is, and have the button open saved viewers with a "may be out of date" flag when dates differ.

c) Open only viewers built on this Mac.

### MATURITY-SCALE - Names for the island maturity scale

since 2026-10-19 · from [obs-condition](/Users/krisbrown/.local/state/ki/agents/observatory/obs-condition.report.md), reviewed by [obs-scale-review](/Users/krisbrown/.local/state/ki/agents/observatory/obs-scale-review.report.md)

**Context:** [KI-HARNESS-GOV-223](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-223-island-maturity-declaration.md) needs a fixed, ordered set of maturity levels each island declares in `.ki.toml`; the draft builds on your words "settled" and "thriving", and decline and ruin are not levels because they come from audit health. The blind review prefers three levels, `founding`, `settled`, `thriving`, because "growing" overlaps with settled islands that are still adding to themselves.

**Query:** Which names should the maturity scale use?

**Options:**

a) (recommended, confidence medium - review disagrees, four steps give younger islands a clearer path up) `founding`, `growing`, `settled`, `thriving`

b) `founding`, `settled`, `thriving`: three levels, coarser but each one distinct

c) `outpost`, `village`, `town`, `city`: a settlement-size metaphor that drops "settled" and "thriving"

## Parked

None.
