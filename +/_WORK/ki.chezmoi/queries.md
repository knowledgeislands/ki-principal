# ki.chezmoi queries

## Open

- WARP-CONTAINER (sol-tower-warp, high): Warp's `~/Library/Group Containers/2BBY89MBSN.dev.warp` is privacy-protected, so it cannot be backed up before the zap; everything else is backed up. a) retire Warp without zapping that container and leave it in place (recommended); b) Kris grants the run Full Disk Access so it can be backed up and zapped. With Kris 01:35.
- TOWER-SIGNING (sol-tower-warp, high): sol has no Tower Assistant signing identity, so the 2.1 build stops. a) create a new sol identity with `build.sh create-identity` (keychain prompt), then build, install and grant Accessibility (recommended); b) Kris exports terra's identity and imports it on sol first. With Kris 01:35.
- FIREWALL-REAPPLY (Needs: action, Kris at terra with sudo; KI-TOOL-RIG-CORE-047): the Screen Sharing pf anchor dates from 14 October and predates `dae10f2`. a) attended re-apply now, after preflight (pf enabled, parent anchor chain, fresh SSH) and with the corrected recovery (recommended, medium, reviewed); b) leave until the next scheduled Mac rehearsal.
- Not raised: CORE-SET-COMMENTS (stays in the worksheet).

## Parked

- TERRA-REMOVALS (Needs: action, Kris; KB-DOTFILES-UE-086; parked 23 October, not urgent): Clockology, Nitro, Mercury (`sudo mas uninstall` commands given), Prime Video (17 GB media), BlueStacks (own uninstaller), Creative Cloud (at-screen check) all still installed on terra.
- ORCA-PER-PANE (Needs: decision, Kris; follow-up thought): ask Orca to add its hooks only to its own sessions (`claude --settings` per pane, per-pane `CODEX_HOME`); draft issue in orca-hooks-research's report; revisit after the orca-coexist explainer.
- ORCA-ADOPT (Needs: decision, Kris): a) evaluate on the laptop to 5 November after Kris turns off permission bypass, folder auto-trust and telemetry, with named checks and one retirement trial: CodexBar (blind review) or Delta (orca-eval) (recommended, high, reviewed); b) adopt now on every Mac; c) laptop-only, no trials.
- RADAR-DESIGN (Needs: decision, Kris): where the radar ring lives. a) both: tools-rig owns the vocabulary, review fields, doctor's `review-overdue` finding and export field; chezmoi owns the values and ring-and-profile rules; the site owns display (recommended, high - only option that serves doctor, the site and the single-catalogue rule); b) personal sidecar `dot_config/rig/radar.toml`, no tools-rig change, can drift, doctor blind; c) interim radar view profiles with dates in roadmap records.
- RADAR-PUBLIC (Needs: decision, Kris): how much radar rig.midnight.ninja shows. a) ring and Hold replacement for public tools; no review dates, checks or retired list; Trial tools only when opted into `public`; a private replacement is never named (recommended, high, reviewed); b) rings, dates and checks for every public tool; c) rings only.
