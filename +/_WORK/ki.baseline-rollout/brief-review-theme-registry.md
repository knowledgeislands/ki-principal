# Brief - review-theme-registry

Blind query review for KI > Foundations > Baseline rollout (`ki.baseline-rollout`), under the `ki-coordination` standard's Query review section. You are reviewing one query before it reaches Kris. Check what you can directly by reading; write nothing in any repository.

## The query

### THEME-REGISTRY - Migrate territory theme registries

**Context:** No Capital in the six territories has `Streams/Themes/`. hnr-principal, legal-principal and personal-principal keep the legacy `Streams/Initiatives/` registry, which the audit warns on. er-principal, va-principal and tmx-principal have no registry at all, so every theme their records name goes unresolved. Several record themes appear in no registry, such as `harness-foundation`, `source-data`, `ki-conformance`, `housekeeping` and `dashboard`.

Since the query was drafted: HOOK-GUARD was replaced at 23:41 BST by HOOKS-MIGRATION. By Kris's order the estate moves from Husky to committed `.githooks` tonight once the new `ki` release is out; until ki.tools-burndown says otherwise, still never run `ki repo conform` without `--dry-run`.

**Query:** Should this Project raise theme-registry migration records in the territories' Capitals?

**Options:**

- Raise one record in each of hnr-principal, legal-principal and personal-principal to move Initiatives to `Streams/Themes/` pages. Leave er-principal, va-principal and tmx-principal without a registry until one of their records needs a theme.
- Raise a record in all six Capitals, giving each a theme registry now.

## Report

Return a run report in the `ki-coordination` run-report form with one query, THEME-REGISTRY, carrying your own recommended option first as `a) (recommended, confidence <high|medium|low> - <one-line reason>)`, the other options beneath, and under Done one line per thing you verified directly.

Authority: read-only across all repositories; no commits, no pushes, no writes outside the run's state folder; never run `ki repo conform`, even with `--dry-run`.
