# Brief: apply-carry

Work: KI > Rig > chezmoi (`+/_WORK/ki.chezmoi/` in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal`); queries in its `queries.md`. Authority: Kris, 19 October 20:30 BST, "go ahead with the 2 recommendations". This is APPLY-CARRY a). Start with `hostname` and `scutil --get LocalHostName` to confirm which Mac this is.

1. Chezmoi source `/Users/krisbrown/.local/share/chezmoi`: fetch, confirm every commit above `origin/main` belongs to this work (`_mgit`, triage, UE-091, seats, TOML, Paperclip), and push fast-forward so the other Mac can pull. Name and do not push any commit that is not.
2. On this Mac: `chezmoi diff ~/.config/rig`; confirm it is the five files `15-command-line`, `40-macos`, `50-services`, `55-ports` and `90-profiles` under `conf.d/` and nothing else; `chezmoi apply --exclude=scripts` those five targets only. Then dry-run, then run, `rig apply --target dock:workstation` and `rig apply --target default-application:toml`. Run `rig doctor` and read every finding.
3. On the other Mac over SSH: `git -C ~/.local/share/chezmoi pull --ff-only` (stop if it is not clean), then the same steps as 2, plus `launchctl print gui/$(id -u)/uk.me.kris.rig.paperclip`. If Paperclip is loaded, report it and leave it.
4. No other target, no scripts, no `sudo`. Do not touch the `[locals]` or Codex config the LOCALS-DIFF warning names.

Never use `--no-verify` or force-push. Commit by explicit path. Stop and report on any unexpected difference, failure, or prompt for a password or Touch ID you cannot satisfy; give Kris the exact commands to run attended instead. Report under the owner report with the work's report heading and `› <run name>`.
