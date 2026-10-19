# ki.chezmoi messages

- 2026-10-19 23:12 BST · from ki · MCPORTER-LEAK: on terra, `mcporter-daemon` (node, up since 17 October) held 126 leaked child MCP-server processes (about 6.2 GB on an 18 GB Mac), spawned in batches through 19 October; a reboot at 21:07 cleared them. The daemon's launchers, restart job, `~/.mcporter` config and capacity tests live in the chezmoi source. Evidence: `/Users/krisbrown/.local/state/ki/agents/chezmoi/firewall-freeze.report.md`; capture it as work in your lane.
