# ki.chezmoi queries

## Open

None.

- Not raised: CORE-SET-COMMENTS (stays in the worksheet).

## Parked

- APPLY-PLAN (Needs: decision, Kris; replaces RIG-APPLY, STARSHIP-APPLY, ZED-FONT-APPLY, WARP-RETIRE): a) stage 1 now (backup to /tmp/apply-plan-backup, `brew install starship && brew install --cask font-symbols-only-nerd-font`, scoped `chezmoi apply` of starship, zsh fragments, `~/.zshrc`, ghostty, zed settings, nudge script and the four Rig files, then `rig doctor`), stage 2 Warp retirement in one attended sitting after Ghostty proves itself and sol's account is checked, stage 3 `rig apply` handlers and Dock when the hold lifts (recommended, high); b) stages 1 and 2 together now; c) stage 1 without the Rig files and nudge script; d) hold.
- ORCA-HOOKS (Needs: decision, Kris): a) separate change makes Codex's `hooks.json` preserve Orca's undeclared hooks (Pattern C, like Claude's), holding only that target meanwhile (recommended, high, reviewed); b) copy Orca's hooks into laptop-conditional source.
- ORCA-ADOPT (Needs: decision, Kris): a) evaluate on the laptop to 5 November after Kris turns off permission bypass, folder auto-trust and telemetry, with named checks and one retirement trial: CodexBar (blind review) or Delta (orca-eval) (recommended, high, reviewed); b) adopt now on every Mac; c) laptop-only, no trials.
- TOWER-PATH (Needs: decision, Kris): Rig has no fallback-path form, so the artefact and Dock path stay `~/Applications` until the move. a) keep until Kris moves it, then one follow-up commit switches both (recommended, high); b) switch now and accept drift; c) raise a tools-rig any-of path item.
- RADAR-DESIGN (Needs: decision, Kris): where the radar ring lives. a) both: tools-rig owns the vocabulary, review fields, doctor's `review-overdue` finding and export field; chezmoi owns the values and ring-and-profile rules; the site owns display (recommended, high - only option that serves doctor, the site and the single-catalogue rule); b) personal sidecar `dot_config/rig/radar.toml`, no tools-rig change, can drift, doctor blind; c) interim radar view profiles with dates in roadmap records.
- RADAR-PUBLIC (Needs: decision, Kris): how much radar rig.midnight.ninja shows. a) ring and Hold replacement for public tools; no review dates, checks or retired list; Trial tools only when opted into `public`; a private replacement is never named (recommended, high, reviewed); b) rings, dates and checks for every public tool; c) rings only.
