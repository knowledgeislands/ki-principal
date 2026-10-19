# Brief - wave1-sweep

Wave 1, part two, of KI > Foundations > Baseline rollout (`ki.baseline-rollout`). Kris authorised it on 2026-10-19: "go with recommendations" (WAVE-1 a), read-only).

## Task

Across every repository with a `.ki.toml` under `/Users/krisbrown/workspaces/{humans-not-robots,legal,personal,equal-remedy,valle-armonia,techmedix}/`, sweep the roadmap or Streams records by reading files only:

1. Retired theme slugs in the `.ki.toml` area map: compare against the live themes in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/`.
2. Records not in the current issue-ledger form that `ki-work-roadmap` sets.
3. Records missing a size declaration.
4. Record whether apps-vallearmonia.com still has 7 planning gaps.
5. Mermaid diagrams that archify conversion records would cover; the known exceptions are the legal gantt and the personal email-triage pie.

You may run `ki repo audit --repo <repo>` read-only where it helps; it may abort on the COORD-1 mismatch (KI-HARNESS-GOV-220), so note any abort and fall back to reading files.

## Report

Return a run report in the `ki-coordination` run-report form: under Done one line per repository with counts for each check, linked by absolute path; then one query per decision Kris must make, such as whether to raise conformance records in a territory, each with a recommended option and confidence. Name findings; fix nothing.

Authority: read-only in every repository. No commits, no pushes, no record creation, no writes outside the run's state folder. HOOK-GUARD: never run `ki repo conform` at all in this run.
