# ki.observatory queries

## Open

### BEACON-ACCEPT - Accept the rebuilt Beacon

**Context:** KI-OBSERVA-BCN-008, the Beacon signal anatomy, is built (23f2ba5): each row shows a severity sign, its kind and how stale its evidence is, the list filters and groups by kind, and a row opens a detail pane. The gate and audit passed with the width and density tests unchanged. Condition waits on the `.ki.toml` maturity source. A build run may not accept its own work, so the record sits awaiting review.

**Query:** Will you accept the Beacon after a look at <http://127.0.0.1:1675/>?

**Options:**

a) (recommended, confidence high - gate, audit and service check passed; acceptance can be revisited) Accept it, marking KI-OBSERVA-BCN-008 done.

b) Send it back with changes you name.

## Parked

None.
