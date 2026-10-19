# Brief - review-va-planning

Blind query review for KI > Foundations > Baseline rollout (`ki.baseline-rollout`), under the `ki-coordination` standard's Query review section. You are reviewing one query before it reaches Kris. Check what you can directly by reading; write nothing in any repository.

## The query

### VA-PLANNING - Close apps-vallearmonia.com planning gaps

**Context:** apps-vallearmonia.com still has 7 planning gaps, all body-shape fails (ITEM-3) across 5 records. VA-WEBSITE-CONT-005 and VA-WEBSITE-SANC-009 are Now drafts, and VA-WEBSITE-SANC-008 and VA-WEBSITE-SITE-004 are Next drafts. All four lack the Current state, Files touched, Dependencies / blocks and Documentation impact sections. VA-WEBSITE-SITE-003 is awaiting review without a complete review packet or a final Discussion. Shaping a record is `ki-plan` work in that repository and needs your authority there.

Since the query was drafted: HOOK-GUARD was replaced at 23:41 BST by HOOKS-MIGRATION. By Kris's order the estate moves from Husky to committed `.githooks` tonight once the new `ki` release is out; until ki.tools-burndown says otherwise, still never run `ki repo conform` without `--dry-run`.

**Query:** Should I launch a planning pass in apps-vallearmonia.com to close the 7 gaps?

**Options:**

- Launch one `ki-plan` run in apps-vallearmonia.com that shapes the four drafts and completes VA-WEBSITE-SITE-003's review packet, leaving every record short of Ready until you approve it.
- Leave the gaps until those records are next selected.

## Report

Return a run report in the `ki-coordination` run-report form with one query, VA-PLANNING, carrying your own recommended option first as `a) (recommended, confidence <high|medium|low> - <one-line reason>)`, the other options beneath, and under Done one line per thing you verified directly.

Authority: read-only across all repositories; no commits, no pushes, no writes outside the run's state folder; never run `ki repo conform`, even with `--dry-run`.
