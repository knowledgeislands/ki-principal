# Brief - specifications/revise-7

Revise the drafts in `design/specs/` of `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/` from draft 0.7 to draft 0.8. Read `decisions.md` first; then the review at `draft-review-5.report.md` in the same folder.

## Do

1. Fix N1 in `draft-review-5.report.md` in all four places it names, as its proposed fix describes: premature termination at an embedded delimiter causes either a parse failure or silent truncation. Change nothing else of substance.
2. Bump every status line to draft 0.8 and add the revision to the overview's history.
3. Check: no em or en dashes; no remaining wording that says the validator reliably rejects such input.

Write only in `design/specs/`. Do not commit, push or publish. Never run `ki repo conform` without `--dry-run`.

## Report

Write your report as the run packet directs: Done, one line per file changed; Queries in owner-query form only for matters Kris must decide, or `No outstanding queries`.
