---
id: ki.chezmoi
state: handoff-to-supervisor
since: 2026-10-22T22:46:00Z
received: 2026-10-20T01:30:00Z
beat: null
mark: 2026-10-22T22:40:00Z
method_read: beb56729
---

# ki.chezmoi state

## Now

- Scope: resumed for terra drift and terra-specific items only (Kris, after the 22 October drain); nothing is running.
- Terra drift: resolved except `~/.codex/hooks.json` (ORCA-HOOKS) and `~/.codex/config.toml` (CODEX-CONFIG, held until ORCA-HOOKS) · with Kris.
- HOLD-LIFT (reviewed, high): APPLY-PLAN stage 3, `rig apply` of the `.sh`/`.zsh` handlers and the Dock (broken Warp tile), waits on it; `.toml` stays held until [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md); terra `rig doctor` 6 · with Kris.
- TERRA-REMOVALS ([KB-DOTFILES-UE-086](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-086-finish-software-alignment.md)): Kris is working through it at the screen, Homebrew Wrangler done · with Kris.
- NUDGE-SIMPLIFY: retire `rig-tower-save-nudge` from the source · with Kris.
- TOWER-PATH: kb.regular.site-tower's 22 October line in `messages.md` reinstates `/Applications/Tower Assistant.app` as the final home (Rig artefact, wrapper, Dock entry) · coordinator.
- Tower Save Nudge leftovers: a possible old TCC grant to remove by hand · with Kris.
- Claude Desktop relaunch to pick up the applied trust targets · with Kris.
- VS Code territory layout A: the `ki` change is with ki.tools-burndown; the chezmoi sync follows its release · waiting on ki.tools-burndown.
- `apps-sky.humansnotrobots.be` and `apps-snowflake.humansnotrobots.be` trust rests on another session's uncommitted `workspaces/humans-not-robots/dot_mgit.toml` · other session.
- MGIT-EXTERNAL-MEMBER: fixed in tools-ki `1d199a77` on local main, not yet pushed.
- Parked: ORCA-ADOPT, RADAR-DESIGN, RADAR-PUBLIC · with Kris.
- [KB-DOTFILES-UE-090](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md) and [KB-DOTFILES-UE-100](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-100-mcporter-daemon-child-leak.md): attended steps on terra and sol outstanding · with Kris.
- Sol: not yet brought level with terra's 22 October changes (GitUp and Motion removal, Starship, Ghostty, Symbols Nerd Font, Warp retirement) or its own Rig drift (TOML handler, firewall ranges, UTM) · with Kris at sol.

## Next steps

1. HOLD-LIFT, then APPLY-PLAN stage 3 on terra; sol's Rig checked against terra's before its own lift.
2. ORCA-HOOKS (Codex `hooks.json` as a `modify_`, Kris posts the Orca issue), then CODEX-CONFIG: Kris runs `chezmoi diff ~/.codex/config.toml` at the screen.
3. TERRA-REMOVALS pass with Kris; NUDGE-SIMPLIFY.
4. TOWER-PATH: act on the `messages.md` line and move the Rig artefact, wrapper and Dock entry to `/Applications`, stopping at the diff gate.
5. On sol, with Kris there: GitUp and Motion removal, the Starship, Ghostty and font apply, Warp retirement, and the Rig drift items.
6. Attended steps for KB-DOTFILES-UE-090 and KB-DOTFILES-UE-100, then their acceptance.
7. homeless: TRUST-COMPLETE, to be recorded as a chezmoi Decision Record.
8. VS Code chezmoi sync after ki.tools-burndown releases the layout.
9. Parked until Kris takes them up: ORCA-ADOPT (Orca evaluation), RADAR-DESIGN, RADAR-PUBLIC.

## Held

- Both-Mac Rig apply - until Kris lifts it.
- Privacy and rationale audits - until the owner resumes them.
- WhatsApp refresh (KB-DOTFILES-UE-035) - until Kris takes it up.
