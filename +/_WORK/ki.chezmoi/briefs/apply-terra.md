# Brief: apply-terra

Work: KI > Rig > chezmoi (`+/_WORK/ki.chezmoi/` in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal`). Rerun (first attempt stopped at step 1, nothing changed: `apply-terra.report.md`). Authority: Kris's standing "It can do anything that's high confidence" (19 October) for TERRA-PULL a), high; and Kris, 19 October 20:30 BST, "go ahead with the 2 recommendations" (APPLY-CARRY a), narrowed by TOML-HANDLER a), reviewed high: carry Terra without the TOML target, accepting the TOML drift finding until tools-rig falls back for dynamic types. Evidence: `/Users/krisbrown/.local/state/ki/agents/chezmoi/apply-carry.report.md`.

From this Mac (sol) over SSH to terra:

1. Terra cannot reach GitHub over SSH (its key is in OneDrive, unreadable non-interactively), so feed it from Sol: confirm Terra's checkout is clean on `main` at `5bfcc4f`, then `git -C ~/.local/share/chezmoi push terra:.local/share/chezmoi main:refs/heads/sol-carry` and `ssh terra 'git -C ~/.local/share/chezmoi merge --ff-only sol-carry && git -C ~/.local/share/chezmoi branch -d sol-carry'`; confirm Terra's HEAD is `8b9ee66`. No credential or sshd change; stop if not clean or not fast-forward.
2. `rig doctor` on terra first; read every finding.
3. `chezmoi diff --no-pager --use-builtin-diff --recursive ~/.config/rig`; confirm it is only `15-command-line`, `40-macos`, `50-services`, `55-ports` and `90-profiles` under `conf.d/` and matches the work; then `chezmoi apply --exclude=scripts` those five targets only.
4. Dry-run then run `rig apply --target dock:workstation`. Do not run the TOML target.
5. `rig doctor` again and read every finding; `launchctl print gui/$(id -u)/uk.me.kris.rig.paperclip`. If Paperclip is loaded, report it and leave it.

No other target, no scripts, no `sudo`, no commit needed. Stop and report on any unexpected difference. Report under the owner report with the work's report heading and `› apply-terra`.
