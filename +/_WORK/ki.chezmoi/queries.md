# ki.chezmoi queries

## Open

- FIREWALL-REAPPLY (Needs: action, Kris at terra with sudo; KI-TOOL-RIG-CORE-047): the Screen Sharing pf anchor dates from 14 October and predates `dae10f2`. a) attended re-apply now, after preflight (pf enabled, parent anchor chain, fresh SSH) and with the corrected recovery (recommended, medium, reviewed); b) leave until the next scheduled Mac rehearsal.
- TOWER-INSTALL (Needs: decision, Kris): Tower Assistant 2.0 removed; 2.1 not yet in `/Applications`, so the Dock tile is broken and TOWER-APPLY waits. a) install 2.1 into `/Applications` now under the ki-self lifecycle, then TOWER-APPLY (recommended, high); b) leave it for kb.regular.site-tower's attended install.
- Not raised: CORE-SET-COMMENTS (stays in the worksheet).
- VA-TOKEN (reviewed, medium): the valle-armonia Cloudflare token is `account-admin` but not on v3 (15 groups, `vallearmonia.com` only, R2 Write, Access: Groups Write, no payload, no alias). Run recommended a) join v3; blind review recommends b) keep it as a deliberate exception with a committed policy snapshot, because its R2 (ingress staging bucket) and Access (`valle-armonia-admins`) uses are real and v3 would widen it to all zones and token self-administration; c) untag breaks discovery without revoking anything · Kris.

## Parked

- TERRA-REMOVALS (Needs: action, Kris; KB-DOTFILES-UE-086; parked 23 October, not urgent): Clockology, Nitro, Mercury (`sudo mas uninstall` commands given), Prime Video (17 GB media), BlueStacks (own uninstaller), Creative Cloud (at-screen check) all still installed on terra.
- ORCA-PER-PANE (Needs: decision, Kris; follow-up thought): ask Orca to add its hooks only to its own sessions (`claude --settings` per pane, per-pane `CODEX_HOME`); draft issue in orca-hooks-research's report; revisit after the orca-coexist explainer.
- ORCA-ADOPT (Needs: decision, Kris): a) evaluate on the laptop to 5 November after Kris turns off permission bypass, folder auto-trust and telemetry, with named checks and one retirement trial: CodexBar (blind review) or Delta (orca-eval) (recommended, high, reviewed); b) adopt now on every Mac; c) laptop-only, no trials.
- RADAR-DESIGN (Needs: decision, Kris): where the radar ring lives. a) both: tools-rig owns the vocabulary, review fields, doctor's `review-overdue` finding and export field; chezmoi owns the values and ring-and-profile rules; the site owns display (recommended, high - only option that serves doctor, the site and the single-catalogue rule); b) personal sidecar `dot_config/rig/radar.toml`, no tools-rig change, can drift, doctor blind; c) interim radar view profiles with dates in roadmap records.
- RADAR-PUBLIC (Needs: decision, Kris): how much radar rig.midnight.ninja shows. a) ring and Hold replacement for public tools; no review dates, checks or retired list; Trial tools only when opted into `public`; a private replacement is never named (recommended, high, reviewed); b) rings, dates and checks for every public tool; c) rings only.
