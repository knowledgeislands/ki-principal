# ki.chezmoi queries

## Open

### ZED-KEYMAP - Confirm the Zed key bindings are deleted

**Context:** On CONFIG-ADOPT you said the Zed key bindings did not work and should go. The command was given at 11:38 BST and has not been confirmed run. **Query:** Has `rm ~/.config/zed/keymap.json` been run on terra? **Options:** a) (recommended, confidence high - it is the removal you asked for, and Zed falls back to its defaults) run it now and say done. b) keep the file after all.

### DISPLAY-ADAPTER - Is the USB display adapter still used

**Context:** terra has MacroSilicon's display software (MSDisplayManager) for a USB display adapter. It is now recognised in Rig as a placeholder under SHIM-APPS. **Query:** Do you still use that USB display adapter? **Options:** a) (recommended, confidence high - recognising it costs nothing, and only you know whether the hardware is in use) still used: keep it declared. b) no longer used: a run gives you one command to delete it outright.

## Parked

None (Kris unparked everything, 24 October).
