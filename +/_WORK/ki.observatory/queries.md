# ki.observatory queries

## Open

### NARROW-DECLARE - Do new tables still declare which columns drop on narrow screens?

**Context:** Under LARGE-SCREEN-REVISIT the Observatory is designed first for large screens, keeping the shipped 760 px column-dropping rule and its width test. The test requires every table to declare which columns survive and which drop at 760 px. The shared pattern already accepts an empty drop list, so a table that drops nothing costs one line.

**Query:** Should new tables keep declaring their dropped columns, or may a new table opt out of the declaration?

**Options:**

a) (recommended, confidence high - reviewed: an empty drop list is already allowed, so the declaration is one line and keeps the width guard whole) Keep the requirement as it is.

b) Let a new table declare "no narrow plan", which the test accepts while still enforcing no horizontal scroll.

c) Decide when the first consolidation is delivered.

## Parked

None.
