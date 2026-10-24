# mgit-member

**🤖 → 👤 Handoff to supervisor · Run report at 22:14 BST**

---

## Done

- Diagnosed: the fault is in tools-ki, not the chezmoi source. `ki`'s mgit reader (`tools-ki/src/core/repository/mgit.ts:72`, `safeRelativePath`) rejects any member path containing `..`. That rule dates from `4aa46ae8` (29 August). mgit then adopted external repositories as ordinary `[members."PATH"]` entries in `e7511d1` (17 October); its README uses `../../.local/share/chezmoi` as the worked example. The personal manifest switched to that form on 19 October (`d2a6c42`). The installed `ki` runs the tools-ki checkout source directly (0.13.0), so it matches HEAD, which still has the old rule.
- The chezmoi entry is correct and meant to be there: `workspaces/personal/dot_mgit.toml` declares `../../.local/share/chezmoi` (source `krisb/dotfiles`) next to `locations = [..., "repo:../../.local/share/chezmoi"]`, plus the `dotfiles` navigation symlink. No other workspace declares an outside member. The rendered target matches the source, so nothing in chezmoi needed changing and nothing was committed.
- Confirmed: `ki repo roadmap summary` works from `~/.local/share/chezmoi` and from `~/workspaces/personal/dotfiles`. It fails with exit 2 and the reported error only when run in `~/workspaces/personal`, where it reads the workspace manifest. `mgit status -s` in `~/workspaces/personal` reads the workspace cleanly: 9 repositories including the chezmoi checkout, 0 failed (mgit 0.18.0).

## In Progress

- Nothing. I changed nothing in tools-ki and wrote nothing to `ki-principal`.

## Queries

**Context:** tools-ki has to accept mgit's typed external members before `ki` works inside `~/workspaces/personal`. The proposed line for `~/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/messages.md` is: `- 2026-10-22 22:14 BST · MGIT-EXTERNAL-MEMBER · from ki.chezmoi: ki's mgit reader (src/core/repository/mgit.ts structuralMembers/safeRelativePath, from 4aa46ae8) rejects mgit's typed external members (mgit e7511d1, 17 October: [members."../../.local/share/chezmoi"]), so any ki repository selection run in ~/workspaces/personal fails with "workspace has unsafe or invalid member ../../.local/share/chezmoi"; please accept a member path that climbs out with leading ".." and then names a safe relative path, resolve it physically, dispatch it once, and reject one that resolves back inside the workspace, matching mgit's workspace-dispatch spec and its bats cases.` Until that lands, the safe workaround is to run `ki` from inside a repository (for example `~/.local/share/chezmoi`), not from the workspace root. Rewriting the manifest is no workaround, because mgit generates this form and refuses a navigation symlink as a repository member.

**Query:** Shall I post that line to the tools-burndown queue?

**Options:** a) (recommended, confidence high - the fault is in tools-ki and mgit's spec already defines the behaviour) post the line as drafted and use the workaround meanwhile; b) post it and also capture a tools-ki roadmap record directly; c) hold it, since the error only appears at the workspace root.
