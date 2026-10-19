# obs-triage - Triage pass over the Observatory roadmap

Work in apps-observatory.local for KI > Model > Observatory (work package ki-principal `+/_WORK/ki.observatory/`; read its `decisions.md` in full, do not edit it), under `ki-work-roadmap` and the repository's AGENTS.md. Kris said under TRIAGE-PUSH: "we've got a lot of items there, so we need to make sense of it all so we can get them through into moving things forwards ... we need to get it moving."

**Do:**

1. List every record in `triage` status (include the Workers phase record the previous run captured, and the four left from the burndown: KI-OBSERVA-VIS-029, VIS-032, VIS-033, VIS-034). Note each one's held state, dependencies and any decision in `decisions.md` that already governs it.
2. Group them into a few themes that make sense of the roadmap, for example by tab or by step of the design convergence (DESIGN-APPLY), with a suggested order inside each group.
3. For each record, recommend one move: **Ready** (with horizon `now`, `next` or `later`), **merge** into a named record, **hold** (naming what it waits for), or **cancel** (with a one-line reason). Prefer moves that get work flowing: aim for a short `now` list that can be built straight away under authority already given.
4. Do the shaping that needs no decision: fill in missing scope, acceptance criteria, dependencies and size so a record could go to Ready on Kris's word. Commit that by explicit path. Do not change any record's status or horizon, merge, cancel or delete anything (PUSH-ALL); those wait for Kris.

Run `ki repo audit` after your commits. Do not push.

**Report** in owner-report shape. Done: the count in triage before, the shaping committed, and the grouped table of every record - identifier linked by absolute path, title, group, recommended move and one-line reason. Queries: one batch query per move type (TRIAGE-NOW, TRIAGE-NEXT-LATER, TRIAGE-MERGE, TRIAGE-HOLD, TRIAGE-CANCEL), each listing its records, with Context, Query, Options and a recommended option with confidence; omit an empty one.
