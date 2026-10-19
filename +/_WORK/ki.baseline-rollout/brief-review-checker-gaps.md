# Brief - review-checker-gaps

Blind query review for KI > Foundations > Baseline rollout (`ki.baseline-rollout`), under the `ki-coordination` standard's Query review section. You are reviewing one query before it reaches Kris. Check what you can directly by reading; write nothing in any repository.

## The query

### CHECKER-GAPS - Report audit blind spots to the harness

**Context:** The Streams adapter applies neither ROAD-6 nor the area-declaration check, so slug-valued area titles in hnr-principal and tmx-principal pass unflagged, and so do va-principal's undeclared `GOV` and `KNW` areas. Separately, `ki repo audit --repo` refuses a symlinked repository path (`personal/dotfiles`). Changes to harness and tools belong to ki.ways-of-working and ki.tools-burndown, not to this Project.

Since the query was drafted: HOOK-GUARD was replaced at 23:41 BST by HOOKS-MIGRATION. By Kris's order the estate moves from Husky to committed `.githooks` tonight once the new `ki` release is out; until ki.tools-burndown says otherwise, still never run `ki repo conform` without `--dry-run`.

**Query:** Should these blind spots go to the harness and tools-ki as handoff items?

**Options:**

- Route the two Streams checker gaps to ki.ways-of-working, and the symlink refusal to ki.tools-burndown, each as one `messages.md` line.
- Note them in this Project only and take them up after the territory rollout.

## Report

Return a run report in the `ki-coordination` run-report form with one query, CHECKER-GAPS, carrying your own recommended option first as `a) (recommended, confidence <high|medium|low> - <one-line reason>)`, the other options beneath, and under Done one line per thing you verified directly.

Authority: read-only across all repositories; no commits, no pushes, no writes outside the run's state folder; never run `ki repo conform`, even with `--dry-run`.
