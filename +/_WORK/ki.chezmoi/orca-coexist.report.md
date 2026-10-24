# chezmoi › orca-coexist

**🤖 → 👤 Handoff to supervisor · Run report at 00:48 BST**

---

## Done

- **Codex hooks coexist** (`5bfaa32`). `~/.codex/hooks.json` is now a `modify_` fragment binding. It owns only the coordinator-reminder groups and keeps every other hook. Our groups go first in each event because Codex keys trust records by group index, and our declared hashes assume index 0. The change adds a `transform-codex-hooks-fragments` command, a merge test, the `config-fragments/codex-hooks.yaml` declaration and a guide update. Gate: audit pass (0 FAIL), tests 356/356, rumdl clean. The scoped diff was empty, so none of Orca's hooks are removed. The scoped apply left the file byte-identical, and `chezmoi status` no longer lists it. Undo: `git revert 5bfaa32`.
- **Codex config applied** (no commit needed). The existing binding already merges `hooks.state` additively, so all 11 trust entries survive, 9 of them Orca's. The render was byte-identical to the live file and no secret was printed. The scoped apply left the checksum unchanged. The TOML parses, `codex --version` reports 0.163.0, and `codex features list` exits 0. Undo: not needed, because nothing changed.
- **`rig-tower-save-nudge` retired** (`c5776b9`). The source and its 17 tests are removed and the target is added to `.chezmoiremove`. The wrapper text is dropped from the Tower Assistant guide and from operational-resources, keeping the `d47acf8` edits. The old LaunchAgent was already gone from launchd. Gate: audit pass, tests 339/339, rumdl clean. The scoped apply removed `~/bin/scheduled/rig-tower-save-nudge`. Undo: `git revert c5776b9`, then apply that target.
- **Final `chezmoi status`** has three entries. `.config/rig/conf.d/10-applications.toml` and `40-macos.toml` were already known: they wait for the Tower Assistant move from `d47acf8`. `bin/chezmoi/json` is new: it is this run's helper change, not applied because the brief scoped applies to named targets. The hooks binding calls the source copy, so nothing depends on it. Working tree clean, no Git locks, no push.

### How Orca's hooks run

1. **What Orca writes and where.** When Orca starts, it writes three hook scripts to `~/.orca/agent-hooks/` (`claude-hook.sh`, `codex-hook.sh`, `copilot-hook.sh`) plus a Claude status-line script. It then adds an entry for every event to your global `~/.claude/settings.json` and `~/.codex/hooks.json`. In Claude that is SessionStart/End, UserPromptSubmit, Pre/PostToolUse, Stop, Subagent*, PermissionRequest, PostCompact and others. In Codex it is nine events, including Interrupt. It also trusts the Codex entries in `config.toml` `hooks.state`.
2. **What fires.** Every Claude Code or Codex session on the machine runs a small inline `/bin/sh` snippet on each of those events, whether or not the session is in Orca.
3. **How it detects an Orca pane.** Orca gives each terminal pane environment variables: `ORCA_PANE_KEY`, `ORCA_TAB_ID`, `ORCA_WORKTREE_ID`, `ORCA_AGENT_HOOK_PORT`/`_TOKEN`, or an `ORCA_AGENT_HOOK_ENDPOINT` file that holds them. If the snippet finds none of these, it prints `{}` and exits.
4. **What it sends.** Inside a pane, the script posts the event's JSON payload over curl to `http://127.0.0.1:<port>/hook/codex` (or `/hook/claude`). The request carries a token header and the pane, tab and worktree identifiers, with a 0.5 s connect limit and a 1.5 s total limit. If Orca is unreachable, it appends the event to a per-pane spool file (mode 600, 5 MB cap) beside the endpoint file. Orca uses these events to show each pane's agent state: working, waiting for permission, done.
5. **What it costs outside Orca.** About one `/bin/sh` start and a few environment checks per event, a few milliseconds each. On Pre/PostToolUse that adds up to a small, constant tax on every tool call. Nothing leaves the machine and no file is written.
6. **How Orca could scope hooks to its own sessions.** For Claude, Orca could start each pane's agent as `claude --settings <orca-hooks.json>`; that flag layers an extra settings file onto one session only. For Codex, it could give each pane its own `CODEX_HOME`, holding a `hooks.json` and a `config.toml` that imports or copies yours. A lighter option would be per-launch `-c` overrides, if Codex accepts hooks that way. Either route would leave your global files alone. That change would have to come from Orca's maintainers; until then, our bindings now keep Orca's entries.

## In Progress

Nothing.

## Queries

**Context:** `~/bin/chezmoi/json` is this run's helper change and is the only new entry in `chezmoi status`. It is unapplied because the brief scoped applies to the named targets. Nothing depends on it, because the modify script runs the source copy. **Query:** Should it be applied now? **Options:** a) (recommended, confidence high - it is this change's own target and the apply is reversible) apply `~/bin/chezmoi/json` scoped in a follow-up. b) Leave it until the next full apply.
