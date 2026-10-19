# Brief - review-register-hnr

Blind query review for KI > Foundations > Baseline rollout (`ki.baseline-rollout`), under the `ki-coordination` standard's Query review section. You are reviewing one query before it reaches Kris. Check what you can directly by reading; write nothing in any repository and make no network call beyond read-only Git or GitHub metadata.

## The query

### REGISTER-HNR - Admit or exclude hnr-backend, hnr-frontend and hnr-benchmarks

**Context:** These three active, clean Git repositories under `workspaces/humans-not-robots/` belong to `humansnotrobots`. None is declared in hnr-principal's `territory_members` or Known Lands, none is registered, and none has a `.ki.toml`, although hnr-frontend has an AGENTS.md. hnr-principal's ADR Consolidation notes already cite hnr-backend as a source of evidence. The audit reports nothing about them because it checks only declared members.

**Query:** Should these three repositories become Humans Not Robots territory members?

**Options:**

- Admit them in a later wave: hnr-principal declares them in `territory_members` and Known Lands through its Enactment Process, each repository adopts a baseline `.ki.toml`, and then they are registered.
- Leave them outside the territory as product codebases with no KI governance, and record that exclusion in Known Lands, as was done for hnr-shared.
- Decide one repository at a time, for example admitting hnr-backend and hnr-frontend and leaving hnr-benchmarks out.

## Report

Return a run report in the `ki-coordination` run-report form with one query, REGISTER-HNR, carrying your own recommended option first as `a) (recommended, confidence <high|medium|low> - <one-line reason>)`, the other options beneath, and under Done one line per thing you verified directly.

Authority: read-only across all repositories; no commits, no pushes, no registration, no writes outside the run's state folder; never run `ki repo conform`.
