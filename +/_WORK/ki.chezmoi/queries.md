# ki.chezmoi queries

## Open

- RIG-APPLY (Needs: decision, Kris; replaces TOWER-APPLY and GITUP-APPLY): `chezmoi apply ~/.config/rig/conf.d/10-applications.toml ~/.config/rig/conf.d/16-homebrew.toml ~/.config/rig/conf.d/40-macos.toml ~/bin/scheduled/rig-tower-save-nudge && rig doctor`; candidate doctor 6 → 3 (gitup, gitup-formula, dock clear; firewall, `.toml` handler, 19 October failure remain), nothing new; undo from `eb5f69a`. a) apply (recommended, high); b) Rig files now, nudge script after the move; c) do not apply.
- ORCA-HOOKS (Needs: decision, Kris): a) separate change makes Codex's `hooks.json` preserve Orca's undeclared hooks (Pattern C, like Claude's), holding only that target meanwhile (recommended, high, reviewed); b) copy Orca's hooks into laptop-conditional source.
- ORCA-ADOPT (Needs: decision, Kris): a) evaluate on the laptop to 5 November after Kris turns off permission bypass, folder auto-trust and telemetry, with named checks and one retirement trial: CodexBar (blind review) or Delta (orca-eval) (recommended, high, reviewed); b) adopt now on every Mac; c) laptop-only, no trials.
- STARSHIP-APPLY (Needs: decision, Kris): `brew install starship`, then `chezmoi apply ~/.zsh/99_starship ~/.zsh/completions/_starship ~/.config/starship ~/.config/rig/conf.d/16-homebrew.toml && rig doctor`, then a new Ghostty window; includes `classic` and `--all`. a) now (recommended, high); b) hold.
- TOWER-PATH (Needs: decision, Kris): Rig has no fallback-path form, so the artefact and Dock path stay `~/Applications` until the move. a) keep until Kris moves it, then one follow-up commit switches both (recommended, high); b) switch now and accept drift; c) raise a tools-rig any-of path item.
- RADAR-DESIGN (Needs: decision, Kris): where the radar ring lives. a) both: tools-rig owns the vocabulary, review fields, doctor's `review-overdue` finding and export field; chezmoi owns the values and ring-and-profile rules; the site owns display (recommended, high - only option that serves doctor, the site and the single-catalogue rule); b) personal sidecar `dot_config/rig/radar.toml`, no tools-rig change, can drift, doctor blind; c) interim radar view profiles with dates in roadmap records.
- RADAR-PUBLIC (Needs: decision, Kris): how much radar rig.midnight.ninja shows. a) ring and Hold replacement for public tools; no review dates, checks or retired list; Trial tools only when opted into `public`; a private replacement is never named (recommended, high, reviewed); b) rings, dates and checks for every public tool; c) rings only.
- ZED-FONT-APPLY (Needs: decision, Kris): a) `brew install --cask font-symbols-only-nerd-font`, `chezmoi apply ~/.config/zed/settings.json`, reopen Zed's terminal, `starship-variant rainbow`; the Rig file goes with the combined Rig apply (recommended, high); b) also apply `10-applications.toml` now; c) hold.
- WARP-RETIRE (blind review running: warp-retire-blind).
- Not raised: CORE-SET-COMMENTS (stays in the worksheet).

## Parked

None.
