# wow-accept-prune

## Goal

Clear finished work off the Knowledge Islands roadmaps under `ki-accept`. Kris, 27 October 2026: "we can also do the accepting of the ones which are awaiting-review and then pruning those and the others with it." Finish within about 45 minutes.

## Scope

The KI repositories under `/Users/krisbrown/workspaces/knowledge-islands/` that keep a roadmap (`docs/roadmap/` or ki-principal's `Streams/Roadmap/`): ki-principal, ki-agentic-harness, tools-ki, tools-rig, tools-mgit, apps-observatory.local, apps-knowledgeislands.info, ki-design, ki-techne-harness, ki-specifications and the `mcp-*` repositories.

1. **Awaiting review:** for every record whose status is Awaiting review, check its acceptance criteria against the repository as it stands (the commits it cites exist on main, its checks pass where cheap to run). Where the evidence holds, accept it as done; where it does not, leave it untouched and list it under Queries with one line on what is missing.
2. **SWEEP-ACCEPT, Kris's approval as listed:** accept KI-PRINCIPAL-OPS-014, KI-OBSERVA-BRG-005, KI-OBSERVA-VIS-030, KI-WEBSITE-SITE-044 and KI-TOOL-RIG-CORE-062 on the evidence in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/roadmap-sweep.md` section A, rechecking it; prune KI-PRINCIPAL-MOD-009, KI-HARNESS-GOV-189, KI-HARNESS-GOV-209 and KI-TOOL-RIG-CORE-053 as that section proposes (close each with the resolution it gives, then prune).
3. **Prune:** prune every record accepted or closed in steps 1 and 2, under `ki-accept` and `ki-work-roadmap` done-before-prune commit boundaries (the closing commit lands before the pruning commit). Fix inbound links the repository's audit flags, pointing them at the record's last revision on GitHub.

Touch no other record: do not cancel, defer or re-horizon anything. In `apps-observatory.local`, another run is building a new page; commit only `docs/roadmap/` paths there and the roadmap index it regenerates.

## Bounds

Roadmap records, their indexes and inbound links only. Run `ki repo audit --repo .` with the linked `ki` in each repository before its final commit. Commit by explicit path with Conventional Commits (`docs(roadmap): ...`), pull with rebase, push fast-forward only, never force or `--no-verify`, stop on divergence; leave other sessions' files alone. No new software.

## Report

Owner report. Done: one table per repository (record ID linked to its last revision, accepted or pruned, commit). In Progress. Queries: only records that failed their evidence check, one line each, and anything that blocked.
