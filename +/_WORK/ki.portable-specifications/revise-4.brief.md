# Brief - specifications/revise-4

Revise the five drafts in `design/specs/` of `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/` from draft 0.4 to draft 0.5. Read `decisions.md` first, every entry, including LINK-FIELDS, the last; then `design/agentskills-check.md`; then the review at `draft-review-2.report.md` in the same folder.

## Do

1. Fix all seven findings in `draft-review-2.report.md` as its proposed fixes describe, keeping every owner decision intact. Finding 5 is also LINK-FIELDS' instruction: neither spec defines or requires a metadata field linking it to the other; do not forbid profile keys.
2. For finding 1, choose one base per notation and classify relative targets by normalised location against the package boundary; add one nested-file example for each case.
3. For finding 3, give package-name references a notation a validator can tell apart without resolving the target, keep sibling-first lookup, and report ambiguity among fallback candidates.
4. Bump every status line to draft 0.5, 20 October, and add the revision to the overview's history.
5. Check: no em or en dashes; every Validation list covers its spec's normative constraints; example front matter still passes the field, type, name and length checks.

Write only in `design/specs/`. Do not commit, push or publish. Never run `ki repo conform` without `--dry-run`.

## Report

Write your report as the run packet directs: Done, one line per finding with how it was fixed; Queries in owner-query form only for matters Kris must decide, or `No outstanding queries`.
