# obs-territory

Work: KI > Model > Observatory (`+/_WORK/ki.observatory/` in ki-principal). Repository: apps-observatory.local; `ki territory` lives in tools-ki.

Kris saw this on the Observatory roadmap focused on Knowledge Islands:

> could not observe territory:knowledge-islands: ki territory selection failed (exit status 2); check registration and run ki territory audit --territory <handle> - tried at 08:07:52 - still showing registered estate observed at 08:07:20

1. Reproduce: run the command the Observatory runs for that focus, and `ki territory audit --territory knowledge-islands`. Find whether the fault is registration (local registry), the `ki territory` CLI, or the Observatory's call (arguments, handle, PATH under launchd).
2. Fix it in the repository that owns the fault, under that repository's gate and record rules (a KI-OBSERVA-* record here; in tools-ki add a handoff item to its roadmap rather than changing it unless the fix is a one-line bug with a test). Registry or chezmoi fixes are returned as a query, not applied.
3. Never restart the Observatory service; say in the report whether a restart is needed.

Report in one short owner report: cause, fix and commits, and any query with Context, Query and lettered Options, recommended first with confidence.
