# Brief: mgit-completion

Work: KI > Rig > chezmoi (`+/_WORK/ki.chezmoi/` in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal`). Source change only; no apply.

Authority: the MGIT-ZSH-COMPLETION line in that work's `messages.md` (Kris answered CLI-F-FILTER c) on 18 October) and the work's goal of bringing handed-over tool configuration into the source for Kris's review.

In `/Users/krisbrown/.local/share/chezmoi`:

1. Regenerate `dot_zsh/completions/_mgit` from `mgit completion zsh`, through the repository's existing completion generator if it has one (see `AGENTS.md`, Shell precedence), and keep the generator repeatable and guarded.
2. Run the local gate: `ki repo audit --repo .`, `node --test tests/*.test.mjs`, `rumdl check .`.
3. Show `chezmoi diff ~/.zsh/completions/_mgit` in the report, summarised: `-f` dropped, `overview`, `learn`, `-B/--bypass`, `--learn`, `-j/--jobs` added, `-P` and `-L` reworded, and anything else.
4. Commit by explicit path with a Conventional Commit subject. Do not push, do not run `chezmoi apply`.

Stop and report on any unexpected gate failure.

Report under the owner report with the work's report heading and `› mgit-completion`, with a query asking Kris to approve the one-target apply.
