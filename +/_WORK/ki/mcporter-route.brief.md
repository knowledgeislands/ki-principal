# Brief: mcporter-route

You are a detached background agent for KI > SoP, the territory's dispatch coordinator (work package `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/`).

## Task

Rig: chezmoi reported MCPORTER-LEAK: on terra, `mcporter-daemon` (node, up since 17 October) held 126 leaked child MCP-server processes (about 6.2 GB on an 18 GB Mac), spawned in batches through 19 October; a reboot at 21:07 cleared them. Evidence: `/Users/krisbrown/.local/state/ki/agents/chezmoi/firewall-freeze.report.md`.

Find the one work that owns the mcporter daemon and its configuration: read the `work.md` description of each `+/_WORK/*/` package in ki-principal, and check where the daemon's code and configuration live (`ki-binding` skill, `~/.config` and the chezmoi source, tools-ki or another repository). Add one line to that work's `messages.md` in the form `- 2026-10-19 <HH:MM BST> · from ki · MCPORTER-LEAK: <facts above, evidence path>; capture it as work in your lane.` Commit only that file by explicit path with the subject `docs(work): route MCPORTER-LEAK to <work id>`. Do not push. If the index is locked, wait and retry. If no work clearly owns it, write nothing and raise a query instead.

## Report

Report to the path your run packet names: the owner chosen and why in one line, or the query with Context, Query and Options, a) recommended with its confidence.
