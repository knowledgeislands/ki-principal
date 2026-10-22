# ki.chezmoi queries

## Open

- HOLD-LIFT (Needs: decision, Kris; in blind review: hold-blind): Rig 0.8.0 on terra (checkout, untagged) contains cask fix `671c864`; a targeted apply worked today. Lift for terra now and sol once confirmed / both now / keep until v0.8.0 is a tagged release.
- ORCA-HOOKS (Needs: decision, Kris; kept open until an outcome, Kris 19:01): a) make `~/.codex/hooks.json` a `modify_` that keeps Orca's hooks (as Claude's does), ending the drift with Orca untouched; Kris posts the drafted Orca issue asking for per-pane hooks so they exist only in Orca's agents (recommended, high); b) the `modify_` only, accept about 20–40 ms per tool call outside Orca; c) give Orca its own Claude and Codex config (splits logins and history).
- CODEX-CONFIG (Needs: action, Kris; a) chosen 18:44, awaiting his apply-or-hold): `~/.codex/config.toml` changed on both sides and its render reads 1Password, so no run diffs it; at the screen run `chezmoi diff ~/.codex/config.toml` and say apply or hold (9 of its 11 hook-trust entries are Orca's).
- TERRA-REMOVALS (Needs: decision, Kris; KB-DOTFILES-UE-086): a) one attended ki-self pass now, allowed ahead of B1–B5: Spark launcher, Clockology, Nitro, Mercury, Homebrew `cloudflare-wrangler`; Prime Video and BlueStacks only after Kris keeps or discards their data; Creative Cloud only after an at-screen product, sign-in and sync check (recommended, medium, reviewed); b) leave all to a dedicated KB-DOTFILES-UE-086 session; c) Wrangler alone now, the rest later.
- NUDGE-SIMPLIFY (Needs: decision, Kris): a) retire `rig-tower-save-nudge` from chezmoi (left over from the retired scheduled job; Tower Assistant has its own timer; `.chezmoiremove`, guide and tests) (recommended, high); b) simplify it to `~/Applications`; c) leave it.
- Not raised: CORE-SET-COMMENTS (stays in the worksheet).

## Parked

- ORCA-ADOPT (Needs: decision, Kris): a) evaluate on the laptop to 5 November after Kris turns off permission bypass, folder auto-trust and telemetry, with named checks and one retirement trial: CodexBar (blind review) or Delta (orca-eval) (recommended, high, reviewed); b) adopt now on every Mac; c) laptop-only, no trials.
- RADAR-DESIGN (Needs: decision, Kris): where the radar ring lives. a) both: tools-rig owns the vocabulary, review fields, doctor's `review-overdue` finding and export field; chezmoi owns the values and ring-and-profile rules; the site owns display (recommended, high - only option that serves doctor, the site and the single-catalogue rule); b) personal sidecar `dot_config/rig/radar.toml`, no tools-rig change, can drift, doctor blind; c) interim radar view profiles with dates in roadmap records.
- RADAR-PUBLIC (Needs: decision, Kris): how much radar rig.midnight.ninja shows. a) ring and Hold replacement for public tools; no review dates, checks or retired list; Trial tools only when opted into `public`; a private replacement is never named (recommended, high, reviewed); b) rings, dates and checks for every public tool; c) rings only.
