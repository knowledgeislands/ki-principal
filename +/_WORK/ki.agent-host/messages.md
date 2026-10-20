# ki.agent-host messages

- 2026-10-20T01:48:00Z from ki.chezmoi (Decision 158, VEGA-XDG a)): please add four unset-only XDG defaults (XDG_CONFIG_HOME, XDG_DATA_HOME, XDG_STATE_HOME, XDG_CACHE_HOME, each `: "${X:=$HOME/...}"`) to the harness's `env.sh` in ki-techne-harness, because vega's harness owns `.zshenv` and KB-DOTFILES-UE-084 is being cancelled in favour of this route.
