# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Portable specifications](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/portable-specifications.md>) › revise-6

**🤖 → 👤 Handoff to supervisor · Run report at 00:52 BST · last mark 23:45 BST**

---

## Done

1. R1 fixed in [work-house-profile.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work-house-profile.md>), Conversion rules / Links. One entry-rename rule now covers both relative and absolute targets. A relative target is resolved from the house file that holds it. If it lands at this package's root `work.md`, it is rewritten as a path to `WORK.md` relative to the converted file, with its fragment kept. A target into another package with a supplied conversion mapping gets that mapping's renames. A sibling's `work.md` with no supplied mapping is left as it is and reported as a dependency that needs conversion; it is still a well-formed external reference, so it does not affect conformance. Conformance today gains a bullet on relative links to `work.md`, and its conformance sentence now gives one reading.
2. N1 fixed in [acquire.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/acquire.md>). `metadata.omissions` is now defined against the Scope section. It is required when the method has gaps and must be the only place they are declared; leaving it out claims there are none. Anything Scope excludes is not an omission, and what one run fails to reach is reported under Verification. The front-matter table row and the reviewer's judgement in Validation say the same.
3. All three spec status lines now read draft 0.7, and the profile's reference to the work spec too. The draft 0.7 entry is added to the history in [specs.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/specs.md>), and the profile's revision line names revise-6.
4. Checks: no em or en dashes in any of the five drafts. No draft 0.6 status line is left. All six front-matter examples parse with Ruby YAML and pass the closed-field, string-metadata, name-pattern, length, `spec` and acquire `source`, `mutation` and `omissions` checks. Every owner decision and earlier fix was left as it was.
5. Repository outcome: only `design/specs/` changed. No commit, as the brief says; commit identifiers: none. No conform, Git, remote or publication operation.

## In Progress

Nothing is running.

Outstanding - no action requested now: draft 0.7 has not had its own blind review yet. Running the full reference validator is still outside what has been verified.

## Queries

No outstanding queries.
