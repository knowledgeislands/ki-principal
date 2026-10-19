# Brief - review-ledger-form

Blind query review for KI > Foundations > Baseline rollout (`ki.baseline-rollout`), under the `ki-coordination` standard's Query review section. You are reviewing one query before it reaches Kris. Check what you can directly by reading; write nothing in any repository.

## The query

### LEDGER-FORM - Repair superseded issue ledgers

**Context:** Seven project-roadmap ledgers still use a superseded canonical form, which the audit warns on: 5g-emerge-apex, 5g-emerge-demos, 5g-emerge-testbed, apps-kris.me.uk, apps-dafacts.org, er-agentic-harness and apps-markhowarth.com. The three 5g-emerge ledgers also fail for being in the wrong issuing mode. That is probably a knock-on effect of their slug-valued area maps, though I have not verified it. `ki repo conform --skill ki-work-roadmap` rewrites a superseded ledger and keeps its allocation, but HOOK-GUARD bars conform until ki.tools-burndown lifts it.

Since the query was drafted: HOOK-GUARD was replaced at 23:41 BST by HOOKS-MIGRATION. By Kris's order the estate moves from Husky to committed `.githooks` tonight once the new `ki` release is out; until ki.tools-burndown says otherwise, still never run `ki repo conform` without `--dry-run`.

**Query:** How should the superseded ledgers be repaired?

**Options:**

- Fold the three 5g-emerge ledgers into their AREA-TITLES records. Repair the other four with a `--dry-run`-checked conform once HOOK-GUARD lifts, one repository at a time on your go.
- Hand-edit all seven ledgers now under conformance records, without waiting for conform.

## Report

Return a run report in the `ki-coordination` run-report form with one query, LEDGER-FORM, carrying your own recommended option first as `a) (recommended, confidence <high|medium|low> - <one-line reason>)`, the other options beneath, and under Done one line per thing you verified directly.

Authority: read-only across all repositories; no commits, no pushes, no writes outside the run's state folder; never run `ki repo conform`, even with `--dry-run`.
