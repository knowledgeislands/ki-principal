# Brief - review-size-kind

Blind query review for KI > Foundations > Baseline rollout (`ki.baseline-rollout`), under the `ki-coordination` standard's Query review section. You are reviewing one query before it reaches Kris. Check what you can directly by reading; write nothing in any repository.

## The query

### SIZE-KIND - Backfill size and kind

**Context:** 191 open records in 18 repositories have no `size`, and 61 adopted open records have no `kind`. The largest gaps are personal-principal (33), legal-principal (28), er-agentic-harness (22, all also without kind), hnr-principal (20), dotfiles (16) and apps-vallearmonia.com (15). The field migration window opened on 2026-10-19 and closes on a complete clean scan or a 60-day backstop, after which these warnings become fails. The standard says size and kind need judgement: a run proposes them and you confirm them, one repository at a time. dotfiles also has 4 records still naming `initiative`, which is a mechanical fix.

Since the query was drafted: HOOK-GUARD was replaced at 23:41 BST by HOOKS-MIGRATION. By Kris's order the estate moves from Husky to committed `.githooks` tonight once the new `ki` release is out; until ki.tools-burndown says otherwise, still never run `ki repo conform` without `--dry-run`.

**Query:** How should the size and kind backfill run?

**Options:**

- One read-only proposal run per territory, each producing a size and kind table for you to confirm. Then one write run per repository on your confirmation, fixing the dotfiles `initiative` fields in the same pass.
- Leave the backfill to each repository's next planning pass and accept the risk of fails at the backstop.

## Report

Return a run report in the `ki-coordination` run-report form with one query, SIZE-KIND, carrying your own recommended option first as `a) (recommended, confidence <high|medium|low> - <one-line reason>)`, the other options beneath, and under Done one line per thing you verified directly.

Authority: read-only across all repositories; no commits, no pushes, no writes outside the run's state folder; never run `ki repo conform`, even with `--dry-run`.
