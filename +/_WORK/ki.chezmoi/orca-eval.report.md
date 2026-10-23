# ki.chezmoi › orca-eval

**🤖 → 👤 Handoff to supervisor · Run report at 08:13 BST**

---

## Done

| Tool | What it does for you today on terra | What Orca covers | What Orca lacks | Verdict |
| --- | --- | --- | --- | --- |
| **Delta** (Zed's agent workspace, private beta 0.1.0) | Lets you run coding agents and review their changes. It is pinned in the Dock and its CLI is at `/usr/local/bin/delta`. Spotlight shows 16 launches, the last on 2 October. Laptop profile. | The same job, but much broader: parallel Claude Code and Codex in their own worktrees, a diff viewer, AI-diff notes, commit, push and PRs, orchestration, and a CLI. | Nothing that matters for this job. Delta's beta feature set isn't public, so I can't compare them in detail. | **Replaceable** |
| **Zed** | Your main editor: 927 launches, in the Dock, and the `.md` handler. Rig wants it as the `.toml` handler too (that is still Warp, an existing Rig finding). It also runs agents. | A Monaco editor with find across the worktree, multi-cursor, a Markdown editor and viewers. "Open in" sends files to an outside editor. | No language server, completion, diagnostics or formatters. It says it is "editor-first, not IDE-first" and leaves type-checkers to a terminal. It can't open files you double-click outside it, and works inside Orca workspaces only. | **Partly**: it covers quick edits inside an agent worktree, not general editing |
| **CodexBar** | Shows Claude and Codex usage in the menu bar. It is a login item and always running. It warns at 50% and 20%, chezmoi manages its provider settings (`.chezmoidata/codexbar.yaml`), and it has a CLI. | The status-bar footer shows Claude and Codex 5-hour and weekly windows, reset times and credits, warns at 80%, and estimates cost. | It shows only while Orca is open, and only for the active account. It has no menu-bar view, the warnings you set up or a CLI. Usage from `ki agent` runs and Ghostty sessions shows only if Orca happens to be open. | **Partly**: only if Orca is open all day |
| **Ghostty** | Your terminal, replacing Warp. Every declared launchd agent appears as Ghostty in Login Items. | Terminal panes (xterm.js, the VS Code engine) that keep running in the background, plus a Ghostty theme and font import. | It isn't a general terminal. It isn't Ghostty's engine, and it isn't the host the launchd agents present as. | **No** |
| **Warp** (being retired) | 218 launches, a login item and in the Dock. It has per-territory tab configs in chezmoi. | Terminal panes and a Warp theme import. | Ghostty is already the replacement. | **No**: Ghostty takes its place |
| **GitHub Desktop** | Your actual Git GUI: 285 launches, in the Dock, and it handles the `x-github-client` link. | Staging by hunk, commit, amend, push, pull and sync, PRs and stacked PRs, resolving conflicts with AI, and aborting a merge or rebase. | No history graph, blame, stash, branch management or tags. It covers the "review, stage, commit, push" path only. | **Partly** |
| **Beyond Compare** | `git merge.tool = bc3`: 8 launches. | AI conflict resolution. | A three-way visual merge and folder compare. | **No** |
| **Codex desktop** (`ChatGPT.app`, `com.openai.codex`) | 87 launches and in the Dock. It is the Codex workspace. | Running Codex in parallel worktrees, Codex account hot-swap, and Codex credits. | The ChatGPT chat surface. | **Partly** |
| **claude-swap / codex-multi-auth** | Multi-account management (ADR-KB-DOTFILES-007). | Its own managed accounts and account switcher. | — | **Overlap risk**: it might conflict with these, rather than replace them |

The coordinator's readings, checked against the Rig catalogue:

- **"Z" is Zed.** Confirmed.
- **"Delta" is not `git-delta`.** `git-delta` isn't declared or installed, and Git has no pager configured. Delta is `[tool.delta]`, "Zed's workspace for coding with agents and reviewing their changes". That fits "Z and Delta" as a pair.
- **The footer remark means CodexBar.** Confirmed.
- **"Tower for Git" doesn't match terra.** Neither the catalogue nor terra has Tower the Git client. In Rig, "Tower" is the idle game The Tower and its Tower Assistant. GitHub Desktop is the Git GUI you actually use. Sourcetree and GitButler are installed but have never been launched.
- **What Orca is (capability map).** Orca 1.4.237 is an Electron app.
  - **Editor:** Monaco, plus Markdown, HTML, Mermaid and PDF viewers.
  - **Review:** a diff viewer, AI-diff notes and change attribution.
  - **Git:** see the GitHub Desktop row.
  - **Terminal:** xterm.js panes that keep running in a background daemon.
  - **Agents:** Claude Code, Codex and about 20 others in parallel, each in its own worktree. It has an orchestration layer (tasks, dispatch, supervised workers, decision gates), scheduled automations, and `orca serve` for headless servers or servers reached over SSH.
  - **Integrations:** a per-worktree browser, Design Mode, computer use, Linear and Jira, and a mobile companion.
  - **Settings:** remappable keybindings, and an "Open in" external-editor menu (the docs name VS Code; Zed isn't named).
- **Its config and data, and what chezmoi can manage.**
  - **Settings:** 212 keys in SQLite at `~/Library/Application Support/orca/profiles/local-default/profile-state.db`. They aren't a file chezmoi can manage. Only `~/.orca/keybindings.json` could be, and that file doesn't exist yet.
  - **Other app state:** `~/Library/Application Support/orca` already holds 134 MB. That includes caches, `orchestration.db`, terminal history, the daemon's socket and token, and an E2EE keypair. `~/.orca/agent-hooks/` holds hook scripts.
  - **Telemetry:** it is **on** (`optedIn: true`), although the install plan said to decline it.
  - **Use so far:** no repository has been added and no agent has been run yet.
- **Finding 1: Orca changed two files chezmoi manages, and both now show drift (`MM`).**
  - **`~/.claude/settings.json`:** it added a `statusLine` (there was none before), and its hooks have grown from 5 events to 13. Orca kept a backup at `~/.claude/settings.json.bak`. Chezmoi's modify script keeps most of this, but would rewrite 15 lines.
  - **`~/.codex/hooks.json`:** it added 9 hooks, with a backup at `orca/codex-real-home-hooks/hooks.json.pre-orca`. The next `chezmoi apply` would **remove all 9** (95 lines), and Orca would add them back on its next launch. That loop repeats indefinitely.
  - **The hooks run everywhere:** they fire in every Claude and Codex session, including `ki agent` runs. Outside Orca they do nothing, but each one still starts a shell.
- **Finding 2: Orca turns off agent permissions by default.** Its settings launch Claude with `--dangerously-skip-permissions` and Codex with `--dangerously-bypass-approvals-and-sandbox`. So Claude's permission prompts and Codex's approvals and sandbox are bypassed for anything started from Orca. This applies until you change Settings → agent default args.
- **Risks:**
  - **Maturity:** several releases a day and it updates itself outside Homebrew, so its behaviour can change daily with no way to pin a version.
  - **Single vendor:** it depends on Stably AI (Lovecast Inc.). That is mitigated because the licence is MIT and it is very widely used (about 101k stars).
  - **Offline:** it runs locally and needs no Orca account. Agents and the usage footer still need their providers.
  - **Performance:** about 500 MB resident while idle with no repository open, compared with Zed's 134 MB and CodexBar's 17 MB.
  - **Headless runs:** `ki agent` needs detached, scriptable runs that write status and report files. Orca's agents are interactive TUIs in panes, with automations and orchestration running in Orca terminals. `orca serve` gives a headless runtime, but it is Orca's own control plane, not a drop-in for `ki agent`. Adopting it would add a second orchestration model, not replace one.
- **Checks:** everything was read-only.
  - I read state only with `sqlite3 -readonly`, `chezmoi status` and `chezmoi diff`, plus Spotlight, `ps`, LaunchServices and the web docs.
  - I made no changes: no installs, no settings, no commits.
  - I did not open any token or key files.

## In Progress

- Nothing is running. The drift from Orca's hooks in `~/.claude/settings.json` and `~/.codex/hooks.json` is still in place. Fixing it needs a decision (see the query).

## Queries

**ORCA-ADOPT (Needs: decision)**

**Context:** On the evidence, Orca clearly replaces Delta. It partly covers CodexBar, GitHub Desktop and the Codex desktop app, and it doesn't replace Zed as an editor or Ghostty as a terminal. Before any wider adoption, three things need settling:

1. Orca's hooks conflict with the chezmoi-managed `~/.codex/hooks.json`, and it has edited `~/.claude/settings.json`.
2. It launches agents with permissions and sandbox turned off by default.
3. Telemetry was left on.

It also hasn't yet been used on a real repository, so your first impressions come from the interface, not from real work.

**Query:** How should Orca proceed?

**Options:** a) (recommended, confidence medium - the interface is promising, but the hook conflict, permission bypass and daily releases need settling first, and it hasn't yet been used on real work) Keep evaluating on terra and the laptop profile for two weeks, until 5 November. Start a retirement trial for Delta only. Before then, remove the bypass from Settings → agent default args, turn telemetry off, and let chezmoi own Orca's hooks: add them to `dot_codex/hooks.json.tmpl` and the Claude settings fragments, or decide to accept the drift. The named checks are:

- Run real `ki agent` repositories through Orca worktrees for the two weeks.
- Keep CodexBar's login item but count how often you look at it rather than Orca's footer.
- Note any Zed launches you could have done inside Orca.
- Confirm that `chezmoi apply` and Orca stop rewriting each other's hooks.

b) Adopt now: widen it to the core profile. Start retirement trials for Delta, then CodexBar (by turning off its login item) and the Codex desktop app; keep Zed, Ghostty, GitHub Desktop and Beyond Compare. Do the same three fixes first.

c) Stay laptop-only, as already declared, with no fixed review date or checks. Orca re-adds its hooks every time it launches, so the drift in `~/.codex/hooks.json` stays until chezmoi owns the hooks or Orca stops being used.
