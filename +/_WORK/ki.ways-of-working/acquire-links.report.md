# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › acquire-links

**🤖 → 👤 Handoff to supervisor · Run report at 07:50 BST · last mark 20:20 BST**

---

## Done

- **ACQUIRE-STALE-LINKS a):** no acquire commit was needed. Another session had already repointed the three named links in its own commit, `cfdeda6` (docs(capture): add general goal-focused capture entry and focused routes), which was already on `origin/main` when I pulled. AGENTS.md, README.md and `docs/guides/operator/acquire.md` now point to the live work file [kb.regular.acquire-intake](/Users/krisbrown/workspaces/personal/acquire/+/_WORK/kb.regular.acquire-intake/work.md), and all three links resolve.
- Dry run: the only Markdown links left to `+/_CHECKPOINTS/acquire-intake.md` are four "Durable home" links in the work folder's [decisions log](/Users/krisbrown/workspaces/personal/acquire/+/_WORK/kb.regular.acquire-intake/decisions.md), at Decisions 27, 32, 34 and 35. I left them alone. The background-run standard says a background agent never writes a decisions log. The `home:` lines there and the code span in [KB-ACQUIRE-002](/Users/krisbrown/workspaces/personal/acquire/docs/roadmap/KB-ACQUIRE-002-migrate-granola-state.md) are plain text, not links. The link in `design/intake-trial.md` is already pinned to GitHub at `0273c16`.
- Checks: link resolution on the three files: the checkpoint links all resolve. rumdl: 11 findings, all in the decisions log and all from before this run (blank lines, from `c6107fc`). `ki repo audit`: FAIL=4 skills, 34 findings, all from before this run and none in links I would touch. Working tree clean. Nothing committed, so nothing pushed.
- Net records: acquire 0.

## In Progress

Nothing running. The temporary folder is empty. The report is only at the state path, as the progress protocol sets.

## Queries

### ACQUIRE-DECISIONS-LINKS - four checkpoint links in the acquire-intake decisions log

**Context:** Decisions 27, 32, 34 and 35 in the [acquire-intake decisions log](/Users/krisbrown/workspaces/personal/acquire/+/_WORK/kb.regular.acquire-intake/decisions.md) still link to the retired `+/_CHECKPOINTS/acquire-intake.md`. The same log has 11 rumdl blank-line findings. Only the work's steward may write the log, not a background run.

**Query:** Should acquire's steward, its intake session, repoint those four link targets to `work.md` and fix the blank lines at its next resume?

**Options:**

a) (recommended, confidence high - only the steward may write the log, and the change is mechanical) Send acquire-intake a Messages line asking it to do this at its next resume.

b) Leave the log as historical text, with Git holding the moved path.

### ACQUIRE-PRINCIPAL-CHECKPOINT - links to ki-principal's retired knowledge-acquisition checkpoint

**Context:** AGENTS.md and README.md still link to ki-principal's `+/_CHECKPOINTS/knowledge-islands-model.knowledge-acquisition.md`, which no longer exists. This brief covered only a). PRUNE-BEFORE-PIN left acquire's external links to knowledge-acquisition's next mark.

**Query:** Should this stay with knowledge-acquisition's next mark, as PRUNE-BEFORE-PIN set?

**Options:**

a) (recommended, confidence high - this is already decided under PRUNE-BEFORE-PIN) Leave it to knowledge-acquisition's next mark.

b) Authorise a separate acquire run to repoint them now.
