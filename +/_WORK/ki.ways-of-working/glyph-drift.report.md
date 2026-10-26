# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › glyph-drift

**🤖 → 👤 Handoff to supervisor · Run report at 19:43 BST · last mark 19:08 BST**

---

## Done

- Investigated, and no file regressed. The coordinator's style is the harness file `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/output-styles/ki-coordinator.md`, symlinked from `~/.claude/output-styles/` by chezmoi. No other copy exists. The file was last changed at 18:47 BST and committed in `5f8d6165`. It names `ki-coordination`, shows 👤 for Kris and 🎯 for targets, and puts `in <checkout>` in the send and resume lines.
- Found the cause in the coordinator session's own Claude Code process (transcript `e049de95`). It compacted at 19:26 BST. The style it loaded straight after still matched `5f8d6165`. At 19:27 BST the process sent a style matching `0ae39eac` instead. That is the 07:56 BST revision, from before the rename, before GLYPH-OWNER and before RESUME-PWD. It is the copy the process loaded when it started at about 08:52 BST. The same transcript flips between old and new copies earlier too, at 03:23-03:50 BST. So Claude Code keeps a stale start-up copy of the style and served it again after compaction. No commit, rename or session brought the old wording back.
- Confirmed the rename was the owner's decision: Kris's PMO-NAME answer of 18 October renamed `ki-pmo` to `ki-coordination`, with no alias, in `c4cbb5aa` under [KI-HARNESS-GOV-217 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/218b8e3df7c67412382c34960cf4edfc3c7a9152/docs/roadmap/KI-HARNESS-GOV-217-coordination-and-work-design-renames.md). The direction is `ki-pmo` to `ki-coordination`, so the coordinator session saw the change undone, not a new rename.
- Checked every other surface, and all hold both decisions. These are the `ki-coordination` standard, the [Work Process note](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work%20Process/Work%20Process.md) (`898df10`), the banner tests and the rubric. The rubric still accepts 🧑 only in reports written before GLYPH-OWNER, which is intended. No other file in the harness, ki-principal, tools-ki or ki-specifications prints 🧑 for Kris.
- Found one stale `ki-pmo` mention outside the style: the live `~/.claude/communication.md`, and `delegation.md` beside it, still name the `ki-pmo` reply forms. The chezmoi source already fixes this in uncommitted edits from the ki.chezmoi work's FIRST-STEP on USER-SKILL-LINKS, so I left it alone and did not run `chezmoi apply`.
- Commits: none. Checks: none needed, because nothing changed. Net records: 0 in every repository. I left one note of my own untouched, the [KI-HARNESS-GOV-210 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/218b8e3df7c67412382c34960cf4edfc3c7a9152/docs/roadmap/KI-HARNESS-GOV-210-work-model-write-in.md) GLYPH-OWNER note. It is correct.
- Files left untouched that other sessions have changed but not committed. ki-agentic-harness: `docs/roadmap/KI-HARNESS-GOV-218-cli-conventions.md`, `skills/keystone/ki-repo/references/standards-configuration.md` and `skills/repo-structure/ki-repo-tools/references/standards-cli-conventions.md`. ki-principal: `+/_WORK/ki.ways-of-working/mgit-filter.report.md`, `+/_WORK/ki.ways-of-working/small-fixes.report.md` and `+/_WORK/ki.chezmoi/mark-tidy-current.report.md`. chezmoi source: six files of the ki.chezmoi work, including `dot_claude/private_communication.md`.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The chezmoi source edits that change `ki-pmo` to `ki-coordination` in `communication.md`, `delegation.md` and the Codex `AGENTS.md` are with the ki.chezmoi work. They reach the live files through that work's usual `chezmoi diff` review.

## Queries

### STYLE-STALE - The coordinator session is showing an old copy of its style

**Context:** The style file is correct, but the coordinator's Claude Code process sent a copy from 08:52 BST after its 19:26 BST compaction. That copy uses 🧑 for Kris, says `ki-pmo` and leaves the checkout out of the send line. It will stay stale until the process reloads the style. The standard the coordinator re-reads after compaction is current, so it can override the style by hand. A fresh session fixes it for good.

**Query:** Should the coordinator session be restarted from its send line so it loads the current style, and should the re-anchoring step also re-read the style file from disk?

**Options:**

a) (recommended, confidence high - the transcript shows the stale copy came from the start-up snapshot and the file on disk is correct) Restart the Ways of working coordinator from its send line now. Add a Messages line asking for a harness change, folded into an existing `ki-coordination` record: after compaction, re-anchoring re-reads `output-styles/ki-coordinator.md` from disk and follows it wherever it differs from the loaded style.

b) Only restart the coordinator, and accept that the same stale copy may come back after a later compaction.

c) Keep the session as it is, and have the coordinator follow the standard over the loaded style until the session ends.

### 🤖 → 👤 Handoff to supervisor · since 19:43 BST

👤 1 with you

- [with you] STYLE-STALE · owner · since 19:43
- [committed] nothing to commit; no file regressed
