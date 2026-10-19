# ki.observatory queries

## Open

### VIS-030-CHART-DELIVERY - How the Known Lands chart reaches the page

**Context:** KI-OBSERVA-VIS-030's hex chart renderer is vendored from ki-design. It draws an SVG carrying an inline style, while the page's security policy uses a nonce and already has a separate policy for served SVG images.

**Query:** How should the Known Lands chart reach the page?

**Options:**

a) (recommended, confidence high - reviewed: the existing SVG policy supports it and the vendored drawing stays untouched) Serve the chart as a read-only image and draw focus, selection and signals on an accessible overlay using the same layout.

b) Draw the chart in the browser from the renderer's model, with no served SVG.

c) Relax the page's style policy for the chart.

### VIS-030-POSITIONS - Keep saved island positions on the chart?

**Context:** The renderer places islands the same way every time, with the Capital at the centre. Saving positions needs a new write route and a change to the read-only boundary spec. The reviewer notes that KI-OBSERVA-VIS-030 already records an approval of saved positions (DESIGN-POSITIONS), and says the fixed layout does not replace that. The reviewer also says the record contradicts itself on the read-only boundary, which needs settling either way.

**Query:** Should KI-OBSERVA-VIS-030 still keep island positions?

**Options:**

a) (recommended, confidence medium - review disagrees: no write route is needed and the layout is already stable) Drop the position store and use the fixed layout.

b) (reviewer's choice, medium) Keep a per-host position preference behind a new write route, amending the boundary spec.

### VIS-030-ESTATE - How the whole estate is drawn

**Context:** `ki territory list` names each territory's Capital, but the Observatory currently reads that and throws it away. Some repositories belong to no territory.

**Query:** How should the estate view be composed?

**Options:**

a) (recommended, confidence high - reviewed: it shows the estate as it really is, with no invented Capital) One archipelago per territory with its declared Capital, plus a group of repositories in no territory.

b) One estate archipelago with ki-principal as its Capital.

### BRG-005-COUNTS - Counts on the Act board

**Context:** KI-OBSERVA-BRG-005 wants counts on the confirm step and the receipt. Every Act operation today acts on one target, the record excludes batch operations, and it is still in triage, so this shapes it for later rather than building it now.

**Query:** How should the Act board counts be handled?

**Options:**

a) (recommended, confidence high - reviewed: honest with today's single-target operations; the count is of operations, never files) Count one operation per request, the receipt showing its outcome, and leave batch operations for a later record.

b) Add batch operations.

c) Leave the counts out.

### VIS-031-TABLES - Where the "who is working" column appears

**Context:** KI-OBSERVA-VIS-031 adds a worker column showing which run or person is working where. The reviewer adds that a repository match alone does not prove who owns a particular record, so the column should say when it is repository-level.

**Query:** Which tables should carry it?

**Options:**

a) (recommended, confidence medium - reviewed: matches the record's goal of repositories and records) Repositories and Roadmap rows, plus what each run touches on Sessions, labelled where the match is repository-level.

b) Repositories only, at first.

## Parked

None.
