# Brief - wave1-audit

Wave 1, part one, of KI > Foundations > Baseline rollout (`ki.baseline-rollout`). Kris authorised it on 2026-10-19: "go with recommendations" (WAVE-1 a), read-only).

## Task

1. Run `ki territory audit` for each of the six territories: humans-not-robots, legal, personal, equal-remedy, valle-armonia and techmedix. Use `ki territory --help` for the exact form. For each territory, list each repository the registry knows, each repository on disk under `/Users/krisbrown/workspaces/<territory>/` that it does not know, and each declaration finding.
2. Check whether each repository's installed `ki` matches the released `ki` (`ki --version` against the released version tools-ki or Homebrew reports); report only, install nothing.
3. Report the current status of KI-HARNESS-GOV-205, KI-HARNESS-GOV-221 and KI-HARNESS-GOV-220 (COORD-1) from `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/`.
4. Note `hnr-shared` separately: it has no AGENTS.md, `.ki.toml` or roadmap, and its changes route through hnr-principal.

## Report

Return a run report in the `ki-coordination` run-report form: under Done one line per territory with its finding counts and the repositories that need registration or repair, linked by absolute path; then one query per decision Kris must make, such as REGISTER-<TERRITORY> for registration, each with a recommended option and confidence. Name findings; fix nothing.

Authority: read-only in every repository. No registration, no commits, no pushes, no writes outside the run's state folder, no network calls beyond what `ki territory audit` makes. HOOK-GUARD: never run `ki repo conform` at all in this run, and never without `--dry-run` anywhere.
