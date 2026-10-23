# chezmoi › vscode-groups

**🤖 → 👤 Handoff to supervisor · Run report at 18:33 BST**

---

## Done

Design only. I changed nothing and made no commits. I left the trusted-folder data alone because trust-new-repos is editing it.

### 1. How it works today

- **Files.** The source is `workspaces/vscode/` in chezmoi, a flat folder of 55 `kis-<repo>.code-workspace` files. The target is `~/workspaces/vscode/`, which has 51 files because the four newer `apps-*.humansnotrobots.be` files have not been applied yet. 43 files have one folder. The 8 Capitals have two folders each: the repository and its OneDrive `sources-<territory>`. All folder paths are absolute, so a file still opens correctly after it moves.
- **How `ki` makes them.** `ki vscode check` reports changes and `ki vscode sync --write` writes them. The code is in `tools-ki`, mainly [src/core/manage/vscode.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/manage/vscode.ts).
  - It reads only the top level of `<source>/workspaces/vscode` (`workspaceDocuments`, line 114).
  - It names new files `kis-<basename>` (`workspaceFileName`, line 146).
  - It adds a file for any registered repository that no workspace file covers yet.
  - It adds the bound `sources` folder, and deletes a file when none of its folders exist any more.
  - It then rebuilds `.chezmoidata/trusted-folders.yaml` from the folders in the files, the mgit manifests and the hand-written trust file.
- **What drives the list.** The local KI registry (`~/.local/state/ki/registry.toml`) supplies the repository paths. Each repository's `.ki.toml` supplies `supported_runtimes` (which agent apps may trust it) and `stores.sources`. Territory plays no part today.
  - Every repository's `.ki.toml` names exactly one `capital`, so it belongs to exactly one territory. No repository can be in two.
  - Two things don't line up. `acquire` and four `apps-*.humansnotrobots.be` sites name a Capital, but that Capital's `territory_members` list leaves them out. `apps-sky.humansnotrobots.be` names no Capital at all.
- **What points at the paths:**
  - **VS Code itself:**
    - 48 per-workspace storage folders (`workspaceStorage/<id>`; VS Code works out `<id>` from the workspace file's path).
    - 48 profile associations in `storage.json`.
    - `lastActiveWindow` and `backupWorkspaces`, which currently point at `kis-hnr-principal`.
    - The recent list (`recently.opened`), which holds no entries from this folder at the moment.
    - Only one storage folder holds chat or chat-editing history.
  - **Dock:** the `dock-item.vscode-workspaces` folder item in `dot_config/rig/conf.d/private_40-macos.toml`, set to list view, and its check in `tests/rig-catalogue.test.mjs`. It points at the folder, not at the files.
  - **chezmoi:** `.chezmoiremove`, which already lists about 45 retired flat names by hand. The guidance in `docs/guides/agents/audits.md:137` and `.agents/skills/ki-self/SKILL.md:51` describes the flat `kis-<repository-name>` convention.
  - **tools-ki:**
    - The tests in `src/tests/cli/manage/vscode.test.ts` assume the flat folder.
    - [vscode-management.md](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/guides/user/vscode-management.md) describes it.
    - `ki territory inspect --workspace` takes a full path to a workspace file, so it works wherever the file lives.
  - **Unaffected:** `~/bin/rig-bringup-check`, the `territory` and `territory-set` shell functions (they open Ghostty tabs, not VS Code), Claude Desktop and Claude Code settings, Raycast and Alfred (no references found), and the trust data. Trust comes from the folders listed inside the files, not from where the files are.

### 2. Proposed layout (recommended: A)

**A. One file per repository, in one folder per territory:** `workspaces/vscode/<territory-id>/<repo>.code-workspace`, for example `knowledge-islands/tools-ki.code-workspace`.

- `<territory-id>` is the territory's id from `ki territory list` (`knowledge-islands`, `humans-not-robots` and so on). These ids already match the `~/workspaces/<dir>` names.
- Drop the `kis-` prefix, because the folder now says which territory the file belongs to.
- **Which territory.** Use the repository's own `capital` claim, not its path. This places `acquire` and the hnr sites correctly. A repository with no Capital (such as `apps-sky`) or no registry entry goes in `_unassigned/`.
- **Several territories.** The model doesn't allow it, so no rule is needed. A repository's `sources` folder stays inside that repository's file.
- **Special cases.** `kis-chezmoi` becomes `personal/dotfiles.code-workspace`: chezmoi is registered as `dotfiles`, and `dotfiles` is a personal member. Hand-made multi-repository workspace files may sit in any territory folder, and sync leaves them alone wherever they are.
- **Why A.** It keeps one window per repository, so per-repository settings, source control and the Claude Code working folder stay as they are. The Dock list view shows each territory as a submenu, which is the grouping you asked for.

**B. One multi-root workspace per territory:** `workspaces/vscode/<territory-id>.code-workspace`, 8 files.

- Fewer files, but it is materially different. The Knowledge Islands window would hold 21 repositories, and source control, search, the first-folder working directory for agents and per-repository settings would all be shared.
- Better offered later as an optional extra file per territory alongside A (`<territory>/_<territory>.code-workspace`) than as a replacement.

### 3. Changes needed

**tools-ki** (hand-off to ki.tools-burndown, not edited here):

- **`workspaceDocuments`:** read one level of subfolders and record each file's folder.
- **Naming:** have `workspaceFileName` return `<territory-id>/<repo>.code-workspace`. Work out the territory from the `capital` claim, using the existing territory code (`listTerritories` / `resolveTerritory`); fall back to `_unassigned`.
- **Moving files:** when a conventional file is in the wrong place (the old flat `kis-*` name, or the wrong territory folder), plan a move: delete the old file and write the new one, both shown in the diff. Only move files whose folders are exactly that one repository, plus its `sources` folder. Leave hand-made files and settings where they are.
- **Retirement list:** add an option such as `--chezmoiremove` that adds the old target paths to `.chezmoiremove`, so moves and deletions also clean up the target. Today this is a manual step, and it is how stale flat files build up.
- **Collision checks:** check names within each territory folder.
- **Settings:** add a setting for the layout (`flat` or `territory`), defaulting to `territory` once it ships. Either keep the `kis-` prefix as a setting or drop it.
- **Tests:** add tests for the grouped placement, moving from flat names, a Capital claim that the Capital's member list leaves out, `_unassigned`, hand-made files left alone in subfolders, the territory-folder collision check and the `.chezmoiremove` lines.
- **Docs:** update `vscode-management.md`.

**chezmoi:**

- **Source:** run `ki vscode sync --write` once the new version is out; it moves the 55 sources.
- **`.chezmoiremove`:** add the 55 flat `workspaces/vscode/kis-*.code-workspace` names, written by `ki` or in one block.
- **Guidance:** update `docs/guides/agents/audits.md:137` and `.agents/skills/ki-self/SKILL.md:51`.
- **Dock and tests:** the Dock item and `tests/rig-catalogue.test.mjs` need no change; optionally add a test that no flat `kis-*` file is left behind.

**What breaks in VS Code when a file moves:**

- VS Code treats a moved file as a new workspace. Its storage folder, keyed by path, is orphaned. That folder holds open editors, layout, view state, local history settings and the one chat history.
- The profile association and backups for the old path stop applying, and recent-list and Dock entries for the old path stop working.
- **To soften it:**
  1. Do it in one sweep, with VS Code closed and nothing unsaved (backups are kept by workspace id).
  2. Optionally, a one-off script copies each `workspaceStorage/<oldId>` to the new id and rewrites the `workspace.json` path and the `profileAssociations` keys. This is worthwhile only for the one storage folder with chat history and the windows you use most; the rest rebuild themselves after one opening.
  3. Clear the recent list afterwards.
  4. Afterwards, `mcp-housekeeping-claude` (`vscode_sessions_obsolete`) can find and prune the orphaned storage.

### 4. Order and size

1. **tools-ki: grouped reading, naming and moves, plus tests.** Medium, about half a day. Hand-off to ki.tools-burndown.
2. **tools-ki: `.chezmoiremove` output and docs.** Small, about one to two hours.
3. **chezmoi: one sync, the `.chezmoiremove` block, guidance edits and the full local check, then `chezmoi diff` for your review.** Small, about one hour. Do this after trust-new-repos has landed.
4. **Apply with VS Code closed, optionally move the storage for key workspaces, then prune orphans.** Small, about 30 to 60 minutes, and it needs you there.

## In Progress

Nothing.

## Queries

**Context:** You can group by territory either as one file per repository inside a territory folder, or as a single multi-root workspace per territory.

**Query:** Which layout should the hand-off to ki.tools-burndown specify?

**Options:** a) (recommended, confidence high - keeps one window per repository, so per-repository settings, source control, agent working folders and nearly all existing behaviour stay as they are, and the Dock shows territories as submenus) A: `<territory-id>/<repo>.code-workspace`, placed by the repository's `capital` claim, with no `kis-` prefix and `_unassigned/` as the fallback. b) B: one multi-root `<territory-id>.code-workspace` per territory, replacing the per-repository files. c) A now, plus an optional multi-root `_<territory>.code-workspace` in each territory folder later.
