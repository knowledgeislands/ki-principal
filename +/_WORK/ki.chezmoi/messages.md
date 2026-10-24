# ki.chezmoi messages

None.

- 2026-10-24 01:05 BST · MGIT-REPAIR-APPLY · from ki.ways-of-working: at Kris's request `mgit repair` now repairs by default, previews with `--dry-run`/`-n`, and rejects `--apply` (tools-mgit 40ac4ebe, pushed). Two chezmoi copies still carry the old flag: `docs/guides/user/setup-mac-rig.md` line 152 (drop `--apply`) and `dot_zsh/completions/_mgit` lines 9 and 57 (take the completion from tools-mgit as it now stands).
