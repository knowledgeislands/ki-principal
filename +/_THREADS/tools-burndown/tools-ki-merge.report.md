# [Platform foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/platform-foundations.md) › [tools-burndown](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/tools-burndown.md) › tools-ki-merge

**🤖 → 🧑 Handoff to supervisor · Run report at 03:47 BST · last mark none**

---

## Done

- Starting state matched the brief: local `main`, clean tree, no merge or rebase in progress, 31 ahead and 15 behind origin.
- Merged `origin/main` into local `main` (`87a136d8`). Three files conflicted:
  - [KI-TOOL-KI-CLI-139](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-139-ebu-sources-sync.md): kept the later `updated_at`, origin's planning paragraph (which names the `.ki.toml` pointer key and the front-matter keys) and the local adoption note.
  - `docs/roadmap/_ISSUES.md`: kept the local CLI reservation of 145, which is above origin's 143.
  - `src/tests/cli/manage/inventory.test.ts`: kept both sides' commands in the help inventory, origin's `acquire mark` and the local `agent send`.
- No renumbering was needed. Origin's KI-TOOL-KI-CLI-141, -142 and -143 did not clash, because the local records use 144 and 145.
- Generated files: I regenerated `man/ki.commands.json` from `man/ki.1` and it came out unchanged; the man page passes its lint.
- KI-TOOL-KI-CLI-139: its frontmatter meets `ki-work-roadmap`. The two "Decision 55" citations are unchanged (see Queries).
- [KI-TOOL-KI-CLI-137](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-137-agent-run-tmp-home.md) (`d9769ce4`):
  - The pair record now points to KI-HARNESS-GOV-200.
  - TMP-HOME is recorded: temporary files go in `$TMPDIR/ki-agents/<run>/<name>/`, so the ignore warning and the linked-worktree steps are gone.
  - The TOOLS-PUSH state tooling is added to the boundary: the report path default, de-duplicated briefs, `_archive/` retention and sweep pruning.
  - It stays draft until that tooling is planned.
- Gate: build passed, tests passed, lint passed, and `ki repo audit` passed with no failures and five warnings. All five warnings are about CI, hooks and the project registry, not this merge.
- `ki` runs from this checkout's source, so there was nothing in `bin/` to rebuild. `ki --version` gives 0.10.5.
- Pushed `main` to origin fast-forward. Origin had not moved since the merge. Local and origin are now level (0 ahead, 0 behind).

## In Progress

Nothing. There was no release, tag or version bump, because TOOLS-RELEASE is still open.

## Queries

### DECISION-55-CITATIONS: where -139's "Decision 55" lives

**Context:** Decision 55 is not in any ki-principal `+/_THREADS/*/decisions.md`; those logs each have their own unrelated Decision 55. It is in hnr-principal's `+/_THREADS/5g-emerge-phase3/decisions.md`, dated 2026-10-15T23:12:14Z, which is the file -139 already links to. That entry records your 16 October answers, mostly paraphrased, including "SRC-TOOLING tools-ki with tracked configuration and a tools-ki record". The brief said to leave the citations if they were not in ki-principal, so I did.

**Query:** Should a run rewrite -139's two citations from the hnr-principal entry?

**Options:**

a) (recommended, confidence high - the entry is there and already linked) Rewrite both citations as "Kris Brown, 16 October 2026 (SRC-TOOLING)", quoting the entry's words, and keep the link.

b) Leave the "Decision 55" citations as they are.
