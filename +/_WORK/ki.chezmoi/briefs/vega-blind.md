# vega-blind

Work: ki.chezmoi (KI > Rig > chezmoi). Repository: /Users/krisbrown/.local/share/chezmoi, on Sol; you may read /Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness and tools-techne. Read-only blind review of one query.

Read docs/roadmap/KB-DOTFILES-UE-084-render-zshenv-on-vega.md (grounded in commit 8d235fe), scripts/cheztoi-render, and the agent-host harness's env.sh and its reserved-file lists.

Context: KB-DOTFILES-UE-084 planned to add `.zshenv` to vega's Cheztoi manifest so non-interactive shells get the XDG variables. Both `scripts/cheztoi-render` and the agent-host harness reserve `~/.zshenv`, because the harness owns it on vega, and the harness's `env.sh`, sourced by `.zshenv`, `.profile`, `.bashrc` and Git hooks, sets no XDG variables.

Query: which route should the XDG variables take on vega?

Options: a) the agent-host Project adds the four XDG defaults (each set only if unset) to the harness's `env.sh` in ki-techne-harness, and KB-DOTFILES-UE-084 is cancelled with that resolution; b) the harness's `env.sh` sources `~/.zsh/00_xdg_base_dirs` when the Cheztoi payload provides it, and KB-DOTFILES-UE-084 is cancelled the same way; c) release `.zshenv` from both reserved lists so the payload can own it; d) cancel with no change, accepting no XDG variables in vega's non-interactive shells.

Pick one option and give your confidence (high, medium or low) with a one-line reason. Read-only: edit nothing, commit nothing, no network.

Report: heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › vega-blind`, Done, In Progress and Queries.
