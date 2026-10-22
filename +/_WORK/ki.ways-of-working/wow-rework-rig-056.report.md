# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rework-rig-056

**🤖 → 👤 Handoff to supervisor · Run report at 23:05 BST · last mark 09:27 BST**

---

## Done

- [KI-TOOL-RIG-CORE-056](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-rework-rig-056.work/rework/docs/roadmap/KI-TOOL-RIG-CORE-056-menu-bar-order-persistence.md) reworked and returned to `awaiting-review`, with a Review response in Discussion. Only the wording changed: nothing was gathered or rerun, and there were no defaults writes, restarts, app launches or protected-container probes.
- Defect 1, access boundary: the Finding opening and Evidence 4 now say only that the container refused the terminal. That it is closed to Rig and to other unentitled processes, and that MenuBarAgent's store is the authority for order, are marked inferred. Which processes can read or write the store, and its contents and format, are gaps. Evidence 5 and Answers 1 and 3 match, and the container gap row now covers who can read or write it.
- Defect 2, durability: Evidence 7 is retitled as a single snapshot, and the staleness it suggests is marked inferred. Answer 2 drops "plainly survive" and says the snapshot cannot show persistence across a display change, an app update or a later rewrite. Survival across those events is now a gap.
- Defect 3, write and restart behaviour: Answer 3 now opens "Unknown; no route was found" instead of "No". Two questions are now gaps, each with its own row in the gap table: whether a legacy key written while the app runs takes effect or needs the item recreated, and whether restarting ControlCenter, SystemUIServer or MenuBarAgent changes order. ControlCenter acting as a client of MenuBarAgent is marked as inferred from strings.
- Recommendation: still report-only, now at moderate confidence instead of high. It rests on there being no supported interface, and on untested behaviour, not on any claim that a declaration is impossible. The Review packet sections are updated to match.
- Commit `3160dcc744c3f78788a5f17090a38a2456a06ba1` on branch `run/wow-rework-rig-056`, built on `4efcee6`, in worktree `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-rework-rig-056.work/rework`. Only the record path was committed.
- Checks: roadmap audit PASS (no finding on this record; the three existing size warnings remain); `git diff --check` PASS; ASCII-only check PASS; pre-commit hook (full Bats suite and scoped audit) PASS.
- Not done, as the brief directs: no fast-forward of main and no push. The branch and worktree are left in place.

## In Progress

- Nothing running. Integration of `run/wow-rework-rig-056` (which also carries `4efcee6`) waits until RIG-056-INTEGRATE clears the pre-existing `SHELL-HOOK` audit failure. After that, the record needs a fresh independent review.

## Queries

None.
