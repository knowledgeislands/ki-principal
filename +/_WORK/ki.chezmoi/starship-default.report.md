# starship-default

**🤖 → 👤 Handoff to supervisor · Run report at 00:55 BST**

---

## Done

- `kris-rainbow` is now the managed Starship default (`9da18d0`): `dot_zsh/99_starship`, its tests and the Starship guide, which now notes the Nerd Font need (Ghostty built in, Zed via Symbols Nerd Font Mono) and the `starship-variant --machine kris` / `starship-variant kris` fallback.
- No terminal config (Zed, VS Code, Ghostty, Warp) sets `STARSHIP_CONFIG` or pins a variant, so nothing else needed aligning.
- Gate: `ki repo audit` passed (0 FAIL, 4 existing warnings unrelated to this change); `node --test tests/*.test.mjs` passed; `rumdl check .` clean.
- Scoped `chezmoi apply ~/.zsh/99_starship` done on terra; terra's unmanaged machine-variant file already says `kris-rainbow` and was left alone.
- Pushed chezmoi `main` (only this commit was ahead).

sol: `git -C ~/.local/share/chezmoi pull -q && chezmoi apply ~/.zsh/99_starship`, then `cat ~/.config/starship/machine-variant` — if it exists and names anything other than `kris-rainbow`, it overrides the new default; run `starship-variant --machine --reset` to clear it.

## In Progress

None.

## Queries

None.
