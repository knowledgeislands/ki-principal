# bringup-review

Work: ki.chezmoi (KI > Rig > chezmoi). Repository: /Users/krisbrown/.local/share/chezmoi. Read-only blind review: change no file, commit nothing.

Read [KB-DOTFILES-UE-090](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md) (gaps 2, 7, 8 and 9), [KB-DOTFILES-UE-076](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-076-always-run-latest-source.md), and the setup guide `docs/guides/user/setup-mac-rig.md` (Stage 7 especially).

Question: how should gaps 2 (sign-ins, Keychain, App Store), 7 and 8 (harness installed, MCP checkouts built, no mise `claude` ahead of Homebrew's, no stale mise versions) and 9 (prompt after a source pull) be closed?

Options:

- a) One read-only re-runnable `rig-bringup-check` script covering gaps 2, 7 and 8, the guide updated to match, gap 9 handed to UE-076.
- b) Guide text only for all four gaps; Stage 7's checks stay manual.
- c) As a), but gap 9 stays in UE-090 as a notice at shell start.

Form your own view from the sources. Give your choice, your confidence (high, medium or low) and the reasons, plus any risk the other options miss, such as a check that handles credentials or overlaps a `tools-rig` responsibility (`rig doctor`).

Never run `ki repo conform` without `--dry-run`.

Report: the run report form, heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › bringup-review`.
