# ki.chezmoi queries

## Open

- HOLD-LIFT (Needs: decision, Kris): lift the 14 October both-Mac `rig apply` hold (RIG-CASKS) once apply-stages confirms the fixed release is installed, so Rig does stage 3 (handlers, Dock) and future installs and removals.
- ORCA-HOOKS (Needs: decision, Kris): a) separate change makes Codex's `hooks.json` preserve Orca's undeclared hooks (Pattern C, like Claude's), holding only that target meanwhile (recommended, high, reviewed); b) copy Orca's hooks into laptop-conditional source.
- CODEX-CONFIG (Needs: action, Kris; a) chosen 18:44, awaiting his apply-or-hold): `~/.codex/config.toml` changed on both sides and its render reads 1Password, so no run diffs it; at the screen run `chezmoi diff ~/.codex/config.toml` and say apply or hold (9 of its 11 hook-trust entries are Orca's).
- TERRA-REMOVALS (Needs: decision, Kris; KB-DOTFILES-UE-086): a) one attended ki-self pass now, allowed ahead of B1–B5: Spark launcher, Clockology, Nitro, Mercury, Homebrew `cloudflare-wrangler`; Prime Video and BlueStacks only after Kris keeps or discards their data; Creative Cloud only after an at-screen product, sign-in and sync check (recommended, medium, reviewed); b) leave all to a dedicated KB-DOTFILES-UE-086 session; c) Wrangler alone now, the rest later.
- NUDGE-SIMPLIFY (Needs: decision, Kris): a) retire `rig-tower-save-nudge` from chezmoi (left over from the retired scheduled job; Tower Assistant has its own timer; `.chezmoiremove`, guide and tests) (recommended, high); b) simplify it to `~/Applications`; c) leave it.
- Not raised: CORE-SET-COMMENTS (stays in the worksheet).

## Parked

- ORCA-ADOPT (Needs: decision, Kris): a) evaluate on the laptop to 5 November after Kris turns off permission bypass, folder auto-trust and telemetry, with named checks and one retirement trial: CodexBar (blind review) or Delta (orca-eval) (recommended, high, reviewed); b) adopt now on every Mac; c) laptop-only, no trials.
- RADAR-DESIGN (Needs: decision, Kris): where the radar ring lives. a) both: tools-rig owns the vocabulary, review fields, doctor's `review-overdue` finding and export field; chezmoi owns the values and ring-and-profile rules; the site owns display (recommended, high - only option that serves doctor, the site and the single-catalogue rule); b) personal sidecar `dot_config/rig/radar.toml`, no tools-rig change, can drift, doctor blind; c) interim radar view profiles with dates in roadmap records.
- RADAR-PUBLIC (Needs: decision, Kris): how much radar rig.midnight.ninja shows. a) ring and Hold replacement for public tools; no review dates, checks or retired list; Trial tools only when opted into `public`; a private replacement is never named (recommended, high, reviewed); b) rings, dates and checks for every public tool; c) rings only.
