# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › drift-fix

**🤖 → 👤 Handoff to supervisor · Run report at 05:05 BST**

---

## Done

`chezmoi status` on sol showed six drifted targets. Four are committed source changes that were never applied (a). The other two are Rig `conf.d` targets that the rig-purpose run owns. None are in-place edits that need to come back into source (b), there are no pending `run_` scripts (c), and nothing is in (d).

| Target | Status | Class | Source commit | Change on apply |
| --- | --- | --- | --- | --- |
| `~/.mcporter/mcporter.json` | `M` | (a) | `85e36b8` fix(mcp): ground git-audit roots in workspaces | Template that holds secrets, so no diff is shown. Only `mcp-git-audit` `MCP_GIT_AUDIT_SAFE_ROOTS` changes, from ten per-territory roots to `~/workspaces:~/.local/share/chezmoi`. No other key differs. |
| `~/Library/Application Support/Claude/claude_desktop_config.json` | `MM` | (a) | `85e36b8` | Fragment binding that holds secrets, so no diff is shown. The same single `SAFE_ROOTS` value changes. The first `M` is only Claude Desktop rewriting its own state at 04:25. The live value matches the source before `85e36b8` exactly, so it was not hand-edited. The trusted folders already match, and the binding keeps all app state. |
| `~/bin/chezmoi/json` | `M` | (a) | `d5ac9c9` feat(claude): prune trusted directories that leave the declaration | Plain file with no secrets. Review it with `chezmoi diff ~/bin/chezmoi/json` (+39/−5). It adds `pruneStringArray` and `recordManagedDirectories`, and an optional fourth state-path argument for `transform-claude-code-settings-fragments`. Your re-add hook runs this applied copy. |
| `~/bin/rig-bringup-check` | `A` | (a) | `55ac30b` feat(bringup): report Rig bring-up readiness read-only, plus later fixes up to `4cca49b` | New executable rendered from a template, so no diff is shown. It is the read-only Rig bring-up readiness reporter and does not exist on the machine yet. |
| `~/.config/rig/conf.d/10-applications.toml` | `M` | — | rig-purpose commits | In progress elsewhere; not touched. |
| `~/.config/rig/conf.d/16-homebrew.toml` | `M` | — | rig-purpose commits | In progress elsewhere; not touched. |

Nothing needed to come back into source, so I made no commit and ran no gate. The working tree is clean as I found it, and no `.git/*.lock` file is left.

## In Progress

Nothing. The two Rig `conf.d` targets wait for the rig-purpose run and its own apply.

## Queries

**APPLY**

**Context:** These four targets differ from source only by committed changes: one directory-scope value in two MCP configs, an updated helper script, and a new read-only script. No app state is lost, because the Claude Desktop binding preserves everything outside `mcpServers` and the trusted folders. The command leaves out the Rig `conf.d` targets. Both MCP files render through the cached 1Password service account, which `chezmoi status` used here without prompting. Claude Desktop and the mcporter daemon pick up the new roots only when they next start. I will not restart them.

**Query:** May I run `chezmoi apply ~/.mcporter/mcporter.json "$HOME/Library/Application Support/Claude/claude_desktop_config.json" ~/bin/chezmoi/json ~/bin/rig-bringup-check`? After it I would verify: `chezmoi status` shows only the two `conf.d` lines; `jq -r '.mcpServers["mcp-git-audit"].env.MCP_GIT_AUDIT_SAFE_ROOTS'` on both MCP files returns `~/workspaces:~/.local/share/chezmoi`; `cmp ~/bin/chezmoi/json ~/.local/share/chezmoi/bin/chezmoi/executable_json` matches; and `test -x ~/bin/rig-bringup-check` passes.

**Options:** a) (recommended, confidence high - only committed and reviewed source changes, with app state preserved) apply the four targets as written; b) apply only `~/bin/chezmoi/json` and `~/bin/rig-bringup-check`, and hold the MCP root widening until you have reviewed `KB-DOTFILES-UE-098`; c) hold everything until the rig-purpose run finishes, then do one apply that includes `conf.d`.
