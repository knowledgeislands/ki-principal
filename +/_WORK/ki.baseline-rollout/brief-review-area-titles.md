# Brief - review-area-titles

Blind query review for KI > Foundations > Baseline rollout (`ki.baseline-rollout`), under the `ki-coordination` standard's Query review section. You are reviewing one query before it reaches Kris. Check what you can directly by reading; write nothing in any repository.

## The query

### AREA-TITLES - Retitle retired theme-slug areas

**Context:** The area-to-theme map in `.ki.toml` is retired. An area title should now be a short capitalised noun phrase. Five repositories still use theme slugs as area titles, 19 in all: 5g-emerge-apex, 5g-emerge-demos, 5g-emerge-testbed (all three failing ROAD-6), hnr-principal and tmx-principal. None of the slugs is a live KI theme. Separately, va-principal issues `GOV` and `KNW` records but declares no area map. legal-principal and 5g-emerge-phase2 already show the target form. The fix is a `.ki.toml` edit in each repository, which needs your authority.

Since the query was drafted: HOOK-GUARD was replaced at 23:41 BST by HOOKS-MIGRATION. By Kris's order the estate moves from Husky to committed `.githooks` tonight once the new `ki` release is out; until ki.tools-burndown says otherwise, still never run `ki repo conform` without `--dry-run`.

**Query:** Should I raise conformance records to retitle these areas, and declare va-principal's map, in each territory's repositories?

**Options:**

- Raise one conformance record per affected repository, routed through each territory's Capital: the three 5g-emerge repositories and hnr-principal through hnr-principal, tmx-principal on its own, and va-principal on its own. Each record proposes noun-phrase titles for you to confirm.
- Raise one combined record in each Capital, hnr-principal, tmx-principal and va-principal, covering its territory's repositories.

## Report

Return a run report in the `ki-coordination` run-report form with one query, AREA-TITLES, carrying your own recommended option first as `a) (recommended, confidence <high|medium|low> - <one-line reason>)`, the other options beneath, and under Done one line per thing you verified directly.

Authority: read-only across all repositories; no commits, no pushes, no writes outside the run's state folder; never run `ki repo conform`, even with `--dry-run`.
