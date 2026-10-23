# ki.chezmoi queries

## Open

- FIREWALL-REAPPLY: Kris chose a) (00:47 BST); run firewall-apply.
- TOWER-INSTALL (Needs: decision, Kris): Tower Assistant 2.0 removed; 2.1 not yet in `/Applications`, so the Dock tile is broken and TOWER-APPLY waits. a) install 2.1 into `/Applications` now under the ki-self lifecycle, then TOWER-APPLY (recommended, high); b) leave it for kb.regular.site-tower's attended install.
- Not raised: CORE-SET-COMMENTS (stays in the worksheet).
- VA-TOKEN (reviewed twice, medium): narrowed after va-recheck. After VA's TOKEN-ROLL: a) named v3 variant (v3 + R2 Write + Observability Read, drop CI Read; drop Access: Groups Write only once Access group operations are proven under v3), before-policy saved, PUT in an approved run (run and second review recommend); b) recorded exception with a live-policy snapshot. Register's 15-group count is stale either way · Kris.
- ORCA-PER-PANE (Needs: decision, Kris; follow-up thought): ask Orca to add its hooks only to its own sessions (`claude --settings` per pane, per-pane `CODEX_HOME`); draft issue in orca-hooks-research's report; revisit after the orca-coexist explainer. (unparked 24 October)
- ORCA-ADOPT (Needs: decision, Kris): a) evaluate on the laptop to 5 November after Kris turns off permission bypass, folder auto-trust and telemetry, with named checks and one retirement trial: CodexBar (blind review) or Delta (orca-eval) (recommended, high, reviewed); b) adopt now on every Mac; c) laptop-only, no trials. (unparked 24 October)
- RADAR-DESIGN (Needs: decision, Kris): where the radar ring lives. a) both: tools-rig owns the vocabulary, review fields, doctor's `review-overdue` finding and export field; chezmoi owns the values and ring-and-profile rules; the site owns display (recommended, high - only option that serves doctor, the site and the single-catalogue rule); b) personal sidecar `dot_config/rig/radar.toml`, no tools-rig change, can drift, doctor blind; c) interim radar view profiles with dates in roadmap records. (unparked 24 October)
- RADAR-PUBLIC (Needs: decision, Kris): how much radar rig.midnight.ninja shows. a) ring and Hold replacement for public tools; no review dates, checks or retired list; Trial tools only when opted into `public`; a private replacement is never named (recommended, high, reviewed); b) rings, dates and checks for every public tool; c) rings only. (unparked 24 October)

## Parked

None (Kris unparked everything, 24 October).
