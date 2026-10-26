# wow-notion-mirror-refs - list what still points at the deleted notion-mirror repository

Kris deleted `knowledgeislands/mcp-ki-kb-notion-mirror` on GitHub and locally on sol and terra on 26 October 2026 ("I deleted `knowledgeislands/mcp-ki-kb-notion-mirror` both on github and locally on sol and terra").

Read-only. Find every live reference to it that is now stale: the local KI registry, Known Lands and other ki-principal governance and Pillars notes, `mcp-servers.yaml` and mcporter configuration, chezmoi source (`~/.local/share/chezmoi`), Claude and Codex MCP settings, the harness (skills, specs, capability catalogue), tools-ki, homebrew-tap, ki-specifications, the website, other principals that consume it (hnr-principal and the others under ~/workspaces), launchd agents, and any mgit or workspace manifests. Use `rg` across ~/workspaces and the chezmoi source; ignore Git history, `+/_WORK` reports and Calendar notes.

Change nothing, commit nothing, install nothing, call no GitHub API. Do not touch Notion.

Report: under ## Done, a table per owner (repository or surface) of file, line and what the reference does (live config that will fail, documentation, inventory entry, historical), and for each owner the change you would propose and whether it is chezmoi or settings (needing an independent `chezmoi diff` review) or ordinary repository content. Under ## Queries, one query per owner whose fix needs Kris, with options and the recommended one first with its confidence.
