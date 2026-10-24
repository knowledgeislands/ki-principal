# ki.chezmoi queries

## Open

### ZED-KEYMAP - Confirm the Zed key bindings are deleted

**Context:** On CONFIG-ADOPT you said the Zed key bindings did not work and should go. The command was given at 11:38 BST and has not been confirmed run. **Query:** Has `rm ~/.config/zed/keymap.json` been run on terra? **Options:** a) (recommended, confidence high - it is the removal you asked for, and Zed falls back to its defaults) run it now and say done. b) keep the file after all.

### DISPLAY-ADAPTER - Is the USB display adapter still used

**Context:** terra has MacroSilicon's display software (MSDisplayManager) for a USB display adapter. It is now recognised in Rig as a placeholder under SHIM-APPS. **Query:** Do you still use that USB display adapter? **Options:** a) (recommended, confidence high - recognising it costs nothing, and only you know whether the hardware is in use) still used: keep it declared. b) no longer used: a run gives you one command to delete it outright.

### PI-INSTALL - Install Pi on terra

**Context:** Pi is now declared in Rig at Trial (laptop only). The only installed copy sits under an old Node version, so the `pi` command does nothing. Rig's dry run plans one npm install. **Query:** Will you run `rig apply --scope tools --target pi-coding-agent` on terra? **Options:** a) (recommended, confidence high - one planned npm install, and it clears the new missing-Pi health finding) run it and say done. b) leave Pi uninstalled for now.

### ADR-007 - Amend the URL-handler line

**Context:** ADR-KB-DOTFILES-007 line 31 says Claude Code's URL handler "is not declared or managed by Rig". After SHIM-APPS it is declared as a recognised, unselected entry, still not managed. The guide and test are updated; the decision record needs your approval. **Query:** Should the decision record get a dated amendment? **Options:** a) (recommended, confidence high - the handler is still not managed, so only the word "declared" is out of date) add a dated amendment saying it is a recognised, unselected catalogue entry that Rig still does not manage. b) leave the record and let the guide carry the change.

### PI-SOL - Pi trial scope and sol's planned uninstall

**Context:** Pi is at Trial, declared for the laptop (terra) only. KB-DOTFILES-UE-086 step C7g still plans to uninstall Pi on sol. Trial status and which Mac runs the trial are separate choices. Orca's own record (KB-DOTFILES-UE-107) names sol as its evaluation Mac, but Orca too is declared laptop-only, so that record and its declaration disagree. **Query:** Which Macs should the Pi trial cover, and should C7g still remove Pi from sol? **Options:** a) (recommended, confidence medium, blind review - follows the declared laptop-only trial; no reason was found to test on both Macs; the first run had preferred b) keep C7g: remove Pi from sol and trial it on terra alone. b) change C7g to keep Pi on sol until the trial ends, with sol outside the trial. c) add the studio profile and trial Pi on both Macs.

## Parked

None (Kris unparked everything, 24 October).
