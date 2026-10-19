# Brief - specifications/live-read

Kris approved SPEC-LIVE-READ on 19 October: one read-only check of the live Agent Skills specification for the portable specs drafted in `+/_WORK/ki.portable-specifications/design/specs/` of `/Users/krisbrown/workspaces/knowledge-islands/ki-principal`. Read `design/plan.md` and the drafts first.

## Do

1. Read <https://agentskills.io/specification> and any pages it links for the format, the licence of the specification text, and the source of the `skills-ref` validator (find its repository from the site).
2. Answer, each with the exact quotation or code line and its URL:
   - Does Agent Skills say anything about the case of files other than `SKILL.md`, and do its examples use upper-case names such as `REFERENCE.md`?
   - Where does a skill's own version live (`metadata.version` or elsewhere)?
   - Is the set of top-level front-matter fields closed, and does `skills-ref` reject unknown top-level keys? Is `metadata` string-to-string only?
   - Under what licence is the specification text published, and may the drafts copy its wording closely with attribution?
3. Compare with the harness's local reference `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-skills/references/standards-agent-skills.md` and list any drift.
4. Write the findings to `+/_WORK/ki.portable-specifications/design/agentskills-check.md`, with what each finding means for the drafts' claims, notably "a conforming package is also a valid skill".

Read only beyond that one file: do not edit, commit, push or publish anything. Never run `ki repo conform` without `--dry-run`.

## Report

Write your report as the run packet directs: Done, one line per question with its answer; Queries in owner-query form, or `No outstanding queries`.
