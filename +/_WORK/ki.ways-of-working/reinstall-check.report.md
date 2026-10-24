# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › reinstall-check

**🤖 → 👤 Handoff to supervisor · Run report at 14:56 BST**

---

## Done

Read-only checks against ki-agentic-harness at `db30d0ca`. Nothing was changed, committed or applied; net records 0 in every repository.

- (1) User-level skills are clean: no `ki-work-folder` in `~/.claude/skills`, `~/.agents/skills`, `~/.codex` or the Claude and Codex plugin caches, and `ki inventory` lists `ki-work-package` as a harness skill. The finding is that `ki-work-package` is not a user skill, so it resolves only where a repository declares it and has a link to it. Repository links are stale in 10 repositories: ki-principal, ki-agentic-harness, personal-principal, legal-principal, er-principal, hnr-principal, tmx-principal, va-principal, si-principal and `personal/acquire` all still have dangling `ki-work-folder` links in `.claude/skills` and `.agents/skills` (only `.agents` in acquire), and none links `ki-work-package`. This session in ki-principal did not offer `ki-work-package` as a skill.
- (2) `ki repair --dry-run` passes with nothing to change (21 user links healthy). `ki repo --estate repair --dry-run` passes too but finds 10 of 51 repositories repairable. It would add 19 `ki-work-package` links and remove 19 dangling `ki-work-folder` links in the 10 repositories above, and would change nothing else.
- (3) `chezmoi diff` touches no skills, hooks or output styles. It does show two unrelated drifts. In `~/.config/ki/config.toml`, an apply would remove the `[locals]` entries for ki-agentic-harness and hnr-agentic-harness, which would undo the dev-linked harness. In `~/.codex/config.toml`, an apply would add two Codex project-trust entries, for `ki-design` and an odd `personal/../../.local/share/chezmoi` path.
- (4) The output style is clean. `~/.claude/output-styles/ki-coordinator.md` is a symlink to the harness's `output-styles/ki-coordinator.md`. Running `ki dev skill generate ki-coordination` with no `--write` reports all 7 generated surfaces in sync. The style describes the five-file package (`work.md`, `state.md`, `queries.md`, `messages.md`, `decisions.md`) and has no `Messages` section. Its two uses of "work file" are the defined word from the Work Process Words table, so they are not stale.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Fixing the repository links belongs to each repository's owner session or the coordinator: `ki repo --estate repair`, or `ki repo --repo <path> repair` per repository. The links are gitignored projections, so no commit is needed.
- The chezmoi drift belongs to ki.chezmoi, with Kris's `chezmoi diff` review. Fold the `[locals]` entries back into the source with a reverse merge, or treat them as app-mutated, before any `chezmoi apply`. Then decide whether the two Codex trust entries should stay.

## Queries

### REPO-LINKS - refresh repository skill links now

**Context:** NO-ALIAS dropped `ki-work-folder` outright. Ten repositories, ki-principal among them, still have only dangling links and cannot load `ki-work-package` until their projections are refreshed. The dry run shows that the repair would change only those links.

**Query:** Should the coordinator launch one run that does `ki repo --estate repair` now?

**Options:**
a) (recommended, confidence high - dry run verified directly; it touches only gitignored links) Launch one short run that does `ki repo --estate repair` and then checks that `ki-work-package` resolves in ki-principal.
b) Leave it to each repository's owner session at its next bootstrap.
