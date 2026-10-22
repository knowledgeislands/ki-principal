# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › acquire-threads

**🤖 → 👤 Handoff to supervisor · Run report at 20:50 BST · last mark 20:20 BST**

---

## Done

- **ACQUIRE-THREADS:** acquire `c6107fc`, pushed fast-forward to `origin/main`. `+/_THREADS/` is gone. Its contents now sit in the work folder [kb.regular.acquire-intake](/Users/krisbrown/workspaces/personal/acquire/+/_WORK/kb.regular.acquire-intake/work.md).
  - `decisions.md` moved with `git mv`, its bytes unchanged.
  - One report still carries open queries, so it moved: [own-binary-home-hold](/Users/krisbrown/workspaces/personal/acquire/+/_WORK/kb.regular.acquire-intake/own-binary-home-hold.report.md), holding BINARY-HOME and BINARY-HOLD, which knowledge-acquisition still carries as open.
  - The other 30 reports were deleted, with Git holding them. Their queries were all answered or homed. ACQ-FINISH was resolved in the 18 October wrap-up. GRANOLA-PLAN and BINARY-PROOF were closed in knowledge-acquisition's decisions. ACQ-PUBLISH was settled by Decision 39. REVIEW-EGRESS's record has been pruned. TECHNE-FOCUS was handed back and is not carried in the 18 October work file.
  - `local-working.md` and the wrap-up are now one design note, [intake-trial](/Users/krisbrown/workspaces/personal/acquire/+/_WORK/kb.regular.acquire-intake/design/intake-trial.md). Its links were adjusted for the new folder depth. The wrap-up's retained concerns and the incoming Personal handoff block are kept in full. The work file's next steps now point to it.
  - `binary-probe/` is still in use: KB-ACQUIRE-003 has its slice Awaiting review. It moved to `scripts/binary-probe/`, a new folder and acquire's first tooling home.
  - Links into the old folder were repointed by script after a dry run, across AGENTS.md, README.md, two guides, KB-ACQUIRE-002 and KB-ACQUIRE-003. Links to deleted reports now point to copies pinned at `2a36d3c` on GitHub.
- Checks: work-folder audit PASS (10/10). rumdl clean on the 10 touched files. Probe tests pass (24). No new broken links. No other repository links into the removed folder.
- Net records: acquire 0, ki-principal 0.

## In Progress

Nothing running. The temporary folder is empty. I wrote this report only to the state path, because the progress protocol makes that the only report path; I made no ki-principal commit.

## Queries

### ACQUIRE-STALE-LINKS - links to the old checkpoint were already broken before this run

**Context:** The link check found links that were already broken before this run and that this move did not touch. AGENTS.md, README.md and `docs/guides/operator/acquire.md` still point to `+/_CHECKPOINTS/acquire-intake.md`, which became the work file in `2a36d3c`. Acquire records also point to retired ki-principal `+/_CHECKPOINTS/` and `+/_THREADS/` paths. The brief did not cover these, so I left them alone.

**Query:** Should one small acquire run repoint the three local checkpoint links to the work file and the external retired paths to commit-pinned copies?

**Options:**

a) (recommended, confidence high - it is mechanical, uses the same script pattern and finishes the checkpoint migration) Authorise one acquire run to repoint them, then commit and push.

b) Leave them until acquire's own intake session next resumes.
