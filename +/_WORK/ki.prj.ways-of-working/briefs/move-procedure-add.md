# Brief: move-procedure-add (ki.prj.ways-of-working)

Two owner instructions relayed by personal.reg.rig-terra on 1 November 2026 are logged in `/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/decisions.md` (DESKTOP-RESET and BACKUPS-DELETE); read that entry for the exact steps and exclusions.

1. Find the repository-move procedure (the wholesale move of 31 October from `~/workspaces/` to `~/kis/`; look in this package's `design/`, in ki.prj.chezmoi's package under `+/_WORK/`, in personal-principal's `+/_WORK/personal.reg.rig-*` packages and in Git history for `wow-move-procedure`). If its owner is this package, add both as post-move steps, quoting Kris's constraints (no backup; never touch Local Storage, cookies, Keychain or Orca's `profile-state.db.backup.*`). If another work owns it, do not edit it: send one line to that work's `messages.md` carrying both steps instead.
2. Append one line to State of play's `messages.md` (`+/_WORK/ki.sop.main/messages.md`): `- 2026-11-01 · Ways of working (ki.prj.ways-of-working): DESKTOP-RESET and BACKUPS-DELETE (from personal.reg.rig-terra) are machine steps for each Mac's Rig thread; returned, as this work does no machine operations. Procedure updated at <where>.`
3. Delete nothing on this machine; run no machine operation.

Commit each repository's change by explicit path (`docs(work): ...`), fetch and push `main` fast-forward only, never force, never `--no-verify`, never stash, rebase or reset; on a pull that cannot fast-forward, merge `origin/main` in a temporary worktree with no rebase, as earlier resolve runs did. Report as your run packet directs.
