# ki.observatory queries

## Open

### COMMIT-AUTHORS - Show commit authors in the worker column too?

**Context:** KI-OBSERVA-VIS-031's worker column (52f18bf) shows running agent runs on Repositories and Roadmap. The record's earlier DESIGN-WORKERS-CHIP answer approved showing commit authors as well; the build left them out and noted the gap. Activity knows Git author names over 7, 14 or 30 days, but only for the latest 50 commits across the scope, so a per-repository author count would be incomplete without a new read. Git author names also miss model co-authors. The reviewer reads DESIGN-WORKERS-CHIP as still in force and prefers finishing it now, as recent commit authors kept separate from active runs, with a stated window and honest coverage limits.

**Query:** Should the Repositories and Roadmap tables also show commit authors?

**Options:**

a) (recommended, confidence medium - review disagrees: authors need their own read, window and wording, so a separate record keeps VIS-031 small) Open a triage record for commit authors and accept KI-OBSERVA-VIS-031 with runs only.

b) (reviewer's choice, high) Reopen KI-OBSERVA-VIS-031 and add recent commit authors, separate from runs, before it is accepted.

c) Drop commit authors from the tables and leave them to the later Workers phase.

### WORKERS-JOIN - How the worker column gets its data

**Context:** KI-OBSERVA-VIS-031 planned to join workers to rows on the server. The build joins them in the page instead, from the same `/api/sessions` answer the workers chip already reads, so no data contract changes. When the run folders can only be partly read, the whole column shows `not observed`, as the chip does.

**Query:** Do you accept the join in the page and the all-or-nothing `not observed`?

**Options:**

a) (recommended, confidence high - no contract change, and it matches the chip) Accept both as built.

b) Move the join to the server, with a worker field in each contract.

c) Show partial counts with a warning when some run folders cannot be read.

## Parked

None.
