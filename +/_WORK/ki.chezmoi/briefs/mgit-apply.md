# Brief: mgit-apply

Work: KI > Rig > chezmoi (`+/_WORK/ki.chezmoi/` in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal`); queries and options in that folder's `queries.md`. Authority: Kris, 19 October 19:47 BST, "It can do anything that's high confidence", taking option a) of every open query. This is MGIT-APPLY a).

1. `chezmoi diff ~/.zsh/completions/_mgit`: confirm it is only the regenerated completion, then `chezmoi apply ~/.zsh/completions/_mgit`, that target alone, scripts excluded.
2. Verify: the one-target diff is empty, and `zsh -i -c 'autoload -Uz _mgit && whence -w _mgit'` loads it.
3. Nothing else is applied. No commit is needed.

Commit by explicit path with a Conventional Commit subject; never push, never `chezmoi apply` beyond what this brief names. Stop and report on any unexpected gate failure. Report under the owner report with the work's report heading and `› <run name>`.
