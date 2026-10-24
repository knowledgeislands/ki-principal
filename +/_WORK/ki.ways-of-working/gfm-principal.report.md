# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Ways of working](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md>) › gfm-principal

**🤖 → 👤 Handoff to supervisor · Run report at 22:07 BST · last mark 21:25 BST**

---

## Done

- Plan note written: [gfm-migration.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/gfm-migration.md>) holds the four decisions, TOUCH-SCOPE as open, the review's prerequisites (consumer fixes, per-batch exceptions for the four width-800 embeds, 10 heading links, 2 callouts, Dataview and templates, per-link verification, reviewed paths against unchanged bytes, rollback manifest, Enactment preview checkpoint), 13 converter requirements and the batch order. Committed in ki-principal `89da42b9`.
- Record opened: [KI-PRINCIPAL-OPS-014](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md>) "Convert ki-principal to GitHub-flavoured Markdown", `status: triage`, Project ways-of-working, covering batches, exceptions, convention notes and the Wikilink Review Activity, linking the plan note. Identifier reserved in `8795d385`, record in `89da42b9`. The harness rules and the converter are named as blocking under `## Dependencies / blocks`; `blocked_by` stays `[]` because `ki-work-roadmap` allows only same-repository identifiers there. Area OPS taken as the closest fit (tools and operating practice). Scoped pre-commit audit passed.
- Converter handed to tools-ki: one GFM-CONVERTER line in `ki.tools-burndown` `messages.md` with the requirements, linking the plan note and the record. ki-principal `3e7f4ab6`.
- GFM-CAPITALS: one GFM-MIGRATION line in State of play's `messages.md` in seven capitals, each committed alone and pushed fast-forward: er `2fffbde`, hnr `14e846a`, lgl `2b584732`, kb (personal-principal) `fe2d0ae6`, tmx `dfe3176`, va `4a1cd96`, si `9099da9`. I added "once the rule lands" before "a file you edit is converted", so nobody converts by hand before the harness rule and converter exist.
- ki pin: `.github/ki-version` moved to `v0.11.5` in its own commit, `b3c44edb`, with the subject `chore(ci): install ki v0.11.5` to match the earlier pin commits.
- ki-principal is not pushed: `89da42b9`, `3e7f4ab6` and `b3c44edb` are local only. The reserve commit `8795d385` is on origin already, because another session's push (`d0782194`, ki.tools-burndown routeview) went out with it on top. I made no push in ki-principal. No other session's files were staged or touched.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- TOUCH-SCOPE is still open with the coordinator. The plan note and the record say that converting all of ki-principal narrows the question to `+/` and other islands but does not remove it.
- The roadmap ledger is behind for MOD: `KI-PRINCIPAL-MOD-010` was issued (accepted in `01f51b68`) without the ledger moving past `MOD: 9`. The next MOD capture should reserve 011, not 010. I left the ledger unchanged.
- The scoping counts in the plan note and record are labelled as re-inventoried at the pilot, not authoritative. The template count (20 tracked files against the scope's 21) is still to be reconciled.
- The repository-wide `ki repo audit` now flags `ki-repo-kb` LINK-1 as exact-case resolution, with failures in existing notes, and RUBRIC-1. This looks like gfm-harness changing the harness checkout. None of the flagged paths are this run's files.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 22:07 BST

👤 0 with you

- [committed] ki-principal plan note, KI-PRINCIPAL-OPS-014, converter handoff, ki pin
- [unpushed] ki-principal `89da42b9`, `3e7f4ab6`, `b3c44edb`
- [committed] seven capitals' GFM-MIGRATION lines, pushed
