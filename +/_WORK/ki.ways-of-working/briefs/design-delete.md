# design-delete

Run for ki.ways-of-working, authorised by Kris on 2026-10-19 at 21:25 BST ("as recommended", DESIGN-DELETE a)).

## Task

1. Read `~/.local/state/ki/agents/ways-of-working/design-triage.report.md` and `delete-review.report.md`. The delete set is exactly 26 files in ki-principal `+/_WORK/ki.ways-of-working/design/`: the 25 migration-plan files in the triage's delete set and `work-folder.md`. Do NOT delete the two thread-model notes (`thread-banner-and-re-anchoring.md`, `thread-types-and-durable-decisions.md`), `applied-map.tsv`, or any graduate-first or keep file. Stop and report if the set on disk is not exactly 26 files.
2. Harness (`/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`): rewrite `skills/governance/ki-work-package/references/standards-work-package.md:77` so its attribution cites the standing contract, not the design note, as delete-review describes. Run the repo's tests and audits; commit by explicit path; pull with rebase and push fast-forward only when your own commit alone is stacked, otherwise name the others and do not push.
3. ki-principal: grep for live links to the 26 files; rewrite any outside `+/_WORK/` history-only reports, and report (do not edit) the Acquire intake run-report link. `git rm` the 26 by explicit path and commit `docs(work): ki.ways-of-working delete graduated design notes`. Do not push ki-principal.

## Rules

British English, ASCII hyphens. Never `--no-verify` or force-push. Touch nothing outside the files named.

## Report

Write `~/.local/state/ki/agents/ways-of-working/design-delete.report.md`: commits with SHAs per repository, pushed or not and why, links rewritten, anything left, queries (none expected).
