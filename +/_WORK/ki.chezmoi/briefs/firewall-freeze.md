# Brief: firewall-freeze

Work: KI > Rig > chezmoi (`+/_WORK/ki.chezmoi/` in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal`). Authority: read-only diagnosis, the coordinator's own; change nothing on any machine or in any repository.

What happened: at about 21:05 BST on 19 October, Kris pasted step 2 of the Terra firewall rehearsal (sequence in `/Users/krisbrown/.local/state/ki/agents/chezmoi/firewall-rehearse.report.md`) as one block into an SSH session from Sol: `sudo launchctl bootout system/uk.me.kris.rig.firewall.screen-sharing`, `sudo pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -F all`, `sudo pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -s rules`. Terra's screen went black and Kris had to hard-restart it. Because all three lines went in together, which one was running is unknown. After the restart (up about 21:07), pf is enabled, all eight anchor rules are back, the LaunchDaemon ran at load with exit 0 (runs = 1), there is no `.panic` file, and `/Library/Logs/DiagnosticReports/shutdown_stall_2026-10-19-210723_terra.shutdownStall` was written. The load average 2 minutes after boot was 348.

Over SSH from Sol to terra, without `sudo` (stop and say so where something needs root):

1. Read the shutdown-stall report if it is readable, and run `log show --style compact --start '2026-10-19 20:58:00' --end '2026-10-19 21:08:00'` filtered for `pfctl`, `pf`, `launchd`, `WindowServer`, `screensharing`, `kernel`, `watchdog`, `stall`, `hang` and the `uk.me.kris.rig.firewall` label.
2. Establish the order of events (bootout, flush, freeze, restart): what stalled, and whether pf, the anchor flush, Screen Sharing state teardown or something unrelated is the likely cause, with your confidence.
3. Check whether anything else was running heavily at the time (the WhatsApp diag at 20:08, and the load average).

Report under the owner report, with the work's report heading and `› firewall-freeze`: the timeline with its evidence, the most likely cause with your confidence, and what it means for the restore path in KI-TOOL-RIG-CORE-047 (`/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md`) and for Sol's planned `rig apply --sudo`. Write nothing to tools-rig.
