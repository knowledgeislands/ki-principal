# ki.chezmoi messages

- 2026-10-22 · TOWER-APP-PATH · KI > Rig > chezmoi: Tower Assistant now installs to `/Applications/Tower Assistant.app` rather than `~/Applications`, from apps-tower.midnight.ninja commit `85ab55a`, so the Rig `tool.tower-assistant` artefact and `~/bin/scheduled/rig-tower-save-nudge` need updating to the new path (keeping the `~/Applications` fallback until Kris completes the attended move).
