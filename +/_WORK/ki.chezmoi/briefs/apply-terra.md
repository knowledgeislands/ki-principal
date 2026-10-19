# Brief: apply-terra

Work: KI > Rig > chezmoi (`+/_WORK/ki.chezmoi/` in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal`). Authority: Kris, 19 October 20:30 BST, "go ahead with the 2 recommendations" (APPLY-CARRY a), narrowed by TOML-HANDLER a), reviewed high: carry Terra without the TOML target, accepting the TOML drift finding until tools-rig falls back for dynamic types. Evidence: `/Users/krisbrown/.local/state/ki/agents/chezmoi/apply-carry.report.md`.

From this Mac (sol) over SSH to terra:

1. `ssh terra 'hostname; git -C ~/.local/share/chezmoi status -sb; git -C ~/.local/share/chezmoi pull --ff-only'`; stop if not clean or not fast-forward.
2. `rig doctor` on terra first; read every finding.
3. `chezmoi diff --no-pager --use-builtin-diff --recursive ~/.config/rig`; confirm it is only `15-command-line`, `40-macos`, `50-services`, `55-ports` and `90-profiles` under `conf.d/` and matches the work; then `chezmoi apply --exclude=scripts` those five targets only.
4. Dry-run then run `rig apply --target dock:workstation`. Do not run the TOML target.
5. `rig doctor` again and read every finding; `launchctl print gui/$(id -u)/uk.me.kris.rig.paperclip`. If Paperclip is loaded, report it and leave it.

No other target, no scripts, no `sudo`, no commit needed. Stop and report on any unexpected difference. Report under the owner report with the work's report heading and `› apply-terra`.
