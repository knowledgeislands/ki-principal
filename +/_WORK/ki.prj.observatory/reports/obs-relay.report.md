# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-relay

**🤖 → 👤 Handoff to supervisor · Run report at 08:18 BST · blocked**

---

## Done

- ROOTS-DOTFILES: I added [KB-DOTFILES-UE-098](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-098-workspaces-git-audit-roots.md) "Workspaces git-audit roots" to the dotfiles roadmap as a non-blocking triage handoff. It follows the same route as the earlier handoffs: first a commit that reserves the identifier, then the record. It collapses `MCP_GIT_AUDIT_SAFE_ROOTS` in `.chezmoidata/mcp-servers.yaml` to `~/workspaces:~/.local/share/chezmoi` and cites EXT-ROOTS, ROOTS-DOTFILES, [KI-MCP-GIT-FND-006](/Users/krisbrown/workspaces/knowledge-islands/mcp-git-audit/docs/roadmap/KI-MCP-GIT-FND-006-ground-roots-in-workspaces.md) and [KB-PRINCIPAL-044](</Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-044-reground-git-audit-artifact.md>). It also notes that the change gives the server more reach, including write access to any folder directly under `~/workspaces`. Before I wrote anything, the target file and the repository had no uncommitted changes. I did not run `chezmoi apply` or touch any deployed file.
- Commits `2f9c210` (reserves the identifier) and `4ec75f1` (the record) were pushed fast-forward to origin. Only my own commits were on top.
- Repository audit: no failures. My first record title broke the four-word title limit, so I shortened it before committing. The 7 warnings were already there and none concerns the new record.
- DESIGN-THREAD-HOME: nothing sent. The trade route does not exist yet (see Queries).

## In Progress

Nothing is running.

## Queries

### DESIGN-THREAD-HOME - no trade route to ki-design exists yet

**Context:** The Capital's trade policy grants no routes at all: none in the whole territory, so none from apps-observatory.local or ki-principal to ki-design. ki-design is also not registered in the local repository registry, so `ki repo trade prepare` cannot create the trade. Opening a route would mean changing the Capital's policy, which needs your authority, so I stopped. The relay still waits to go: the 14-point "app wins" list, the ask to reconsider the banner glyphs, and the ask for a Capital glyph, each linked to its source record in apps-observatory.local. When the design thread sent the original handoff, it put the file in its own outbound folder, `ki-design/-/observatory-handoff/INSTRUCTION.md`.

**Query:** How should the design-thread relay travel, now that no trade route exists?

**Options:** a) (recommended, confidence medium - it mirrors how the design thread sent its handoff, needs no change to the Capital policy, and writes only to Observatory) Write it as a handoff file in apps-observatory.local's outbound folder `-/design-handoff/`, and you point the design thread at it. b) Register ki-design and grant an apps-observatory.local to ki-design work route in the Capital's trade policy through the Enactment Process, then send it as a trade with `ki-trade`. c) You pass it to the design thread in person.
