# chezmoi › orca-hooks-research

**🤖 → 👤 Handoff to supervisor · Run report at 19:03 BST**

---

## Done

Read-only research into whether Orca (1.4.237) can add its agent hooks only while it is in use. Nothing was changed and nothing was committed. I made no network calls, so I did not read GitHub issues; the findings come from Orca's bundled code, its settings (profile DB read with `sqlite3 -readonly`) and the live files.

**1. Does Orca remove or scope its hooks?**

- **No cleanup on quit.** The quit path only removes Grok hooks, and only on Windows. Claude and Codex hooks stay in place after Orca quits, and Orca puts them back on every launch.
- **There is an off switch, but it is global.** The setting `agentStatusHooksEnabled` (currently `true`) and the per-agent list `disabledTuiAgents` (currently empty) control installation. Turning either off makes Orca remove its own entries cleanly, leaving other hooks alone, from `~/.claude/settings.json`, from `~/.codex/hooks.json` and from the Codex trust entries. But it also turns off Orca's agent status display inside Orca. The setting does not mean "only while running".
- **Scoping is partial.**
  - Claude: Orca always writes to `~/.claude/settings.json`. It ignores `CLAUDE_CONFIG_DIR` for the default account. It writes into a separate Orca-owned folder only for a "Claude managed account" created in Orca, and none exists here.
  - Codex: Orca has its own Codex home at `~/Library/Application Support/orca/codex-runtime-home/home`, but it is empty. With the system-default account selected, Orca writes to the real `~/.codex/hooks.json` and adds trusted hashes to `~/.codex/config.toml`.
  - OpenCode and Pi already get a per-pane config folder that Orca sets through environment variables. Claude and Codex do not.
- **The status line was not taken over.** Orca installs its status line only when none is set. It did so here, and outside Orca it prints nothing, which looks the same as having none.

**2. What the hooks do outside Orca, and what they cost**

- Every Orca hook is guarded by environment variables that only Orca's own panes set (`ORCA_PANE_KEY`, `ORCA_AGENT_HOOK_PORT`, `ORCA_AGENT_HOOK_TOKEN`). Outside Orca they read the hook input, print `{}` for Claude, and exit 0. They make no network call and write no spool file.
- On Claude, Orca registers one hook on each of 13 events. On Codex it registers one on each of 9.
- Measured cost per event: about 40 ms for Claude (two `sh` processes plus `cat`) and about 23 ms for Codex, whose guard runs inline before any script starts. That cost lands on every tool call, through PreToolUse and PostToolUse. It is wasteful, but harmless.

**3. How chezmoi interacts with this**

- Claude: the `modify_` for `~/.claude/settings.json` already keeps hooks it does not declare, and `statusLine` is not a key it manages. There is no conflict.
- Codex: `dot_codex/hooks.json.tmpl` replaces the whole file. Every `chezmoi apply` removes Orca's entries and Orca puts them back on its next launch, so the two keep undoing each other. `chezmoi status` shows `MM .codex/hooks.json` now.

Options for "hooks only while Orca is in use":

- **a) Coexist.** Turn the Codex `hooks.json` into a `modify_` that keeps undeclared hooks, in the same way the Claude `modify_` does. This removes the drift. It does not remove the idle cost.
- **b) A wrapper that removes the hooks when Orca quits.** This is fragile. The "Orca Terminal Host" process keeps agents running after the app quits, so removing the hooks would cut off status for agents that are still live. Orca also puts the hooks back on every launch, so the wrapper would only ever handle removal.
- **c) Give Orca its own config folder.** For Claude this works only through an Orca "managed account", meaning a separate Claude login per Orca profile. For Codex it means selecting Orca's own Codex home. Both split your auth and session history away from your normal setup.
- **d) Fix it upstream.** Orca would inject hooks per pane: `claude --settings <orca-file>` (Claude Code merges the hooks from that file for that session only), and the existing per-pane runtime home for Codex. Then nothing would be written to `~/.claude` or `~/.codex` at all. This is the only option that truly gives "only while in use".

Draft upstream issue, not posted:

> **Install Claude/Codex status hooks per Orca pane instead of in user-global config.** Orca writes 13 hook entries into `~/.claude/settings.json` and 9 into `~/.codex/hooks.json` (plus trust hashes in `config.toml`), and they stay after quit. They are inert outside Orca, but they still cost a shell spawn of about 20–40 ms on every tool call in every non-Orca session. They also fight dotfile managers that render `hooks.json`. Orca already uses per-pane overlays for OpenCode and Pi (`OPENCODE_CONFIG_DIR` and others). Could Claude panes be launched with `--settings <orca-managed settings file>`, and Codex panes with Orca's runtime `CODEX_HOME` (or a `-c` hooks overlay), so that Orca's hooks exist only in Orca's own agents? Failing that, could there be an option to remove the managed hooks on quit while no hosted agents are running?

## In Progress

Nothing.

## Queries

**Context:** Orca has no "hooks only while running" mode. The only gap on our side is the Codex `hooks.json` drift, and the only real fix for the idle cost is upstream.

**Query:** Should I capture a work record to turn `~/.codex/hooks.json` into a `modify_` that keeps Orca's entries, and file the upstream issue above?

**Options:** a) (recommended, confidence high - stops the drift and is the only clean route to "only while in use") capture the record, and you post the upstream issue yourself from the draft; b) capture the `modify_` record only and accept the idle cost; c) set `agentStatusHooksEnabled` off in Orca and give up its agent status display.
