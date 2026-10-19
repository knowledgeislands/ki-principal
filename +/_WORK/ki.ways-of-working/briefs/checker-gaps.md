# checker-gaps

Work: ki.ways-of-working. Authorised by Kris, routed from ki.baseline-rollout (19 October, "Anything high confidence can be done.").

## Task

In ki-agentic-harness, in a fresh worktree, make the Streams roadmap adapter (`ki-repo-kb-streams`) apply the area-title check (ROAD-6) and the area-declaration check that the local roadmap adapter applies, sharing the existing check code rather than copying it. Evidence: `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/report-wave1-sweep.md` (slug-valued area titles in hnr-principal and tmx-principal; undeclared `GOV` and `KNW` areas in va-principal). Add fixtures for both checks. Default level WARN if switching straight to FAIL would turn island audits red; report which islands would fail at FAIL. Do not fix the islands.

## Rules

- Tests, type check, Biome and the touched skills' audits pass before commit. Commit by explicit path; push fast-forward only when your own commits alone are stacked; remove the worktree afterwards. Never `--no-verify` or force-push.
- HOOK-GUARD: never run `ki repo conform` without `--dry-run`. CAPTURE-GATE: no new records.
- British English, ASCII hyphens.

## Report

Owner-report shape: Done, In Progress, Queries.
