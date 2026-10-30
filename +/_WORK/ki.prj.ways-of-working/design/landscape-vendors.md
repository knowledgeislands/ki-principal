# Vendor landscape: developer and agent tools (30 October 2026)

Research for the `ki.prj.ways-of-working` landscape study. Part 1 comes from read-only version and help commands run on this Mac (Kris's MacBook, macOS Darwin 27.0.0). Part 2 comes from vendor documentation, changelogs and repositories fetched on 30 October 2026; every claim cites the page it came from, and anything not confirmed on a fetched page is marked **unverified**. Nothing was installed, logged into or changed, and no Orca state was touched.

## Part 1 - Installed on this Mac

| Tool | Installed | Latest seen upstream | Notes |
| --- | --- | --- | --- |
| Orca | 1.4.244 (`/Applications/Orca.app`, brew cask `orca`) | v1.4.244, 29 Oct 2026 | Current. Orca process listening on `*:6768` (its runtime port) and a loopback port. |
| Zed | 1.26.2 (`/Applications/Zed.app`, brew cask `zed`) | 1.26.2, 28 Oct 2026 | Current. |
| Claude Code | 2.1.308 (brew cask `claude-code`) | 2.1.314 `latest`; 2.1.308 is npm `stable` | On the stable channel. |
| Codex CLI | 0.165.0 (brew cask `codex`) | 0.166.0, 29 Oct 2026 | One release behind. |
| herdr | 0.9.5 (brew formula) | v0.9.5, 14 Oct 2026 | Current. |
| Hermes Agent | 0.22.4 (brew formula `hermes-agent`; `hermes --version` prints "vunknown (2026.9.24)") | v0.22.5, 22 Oct 2026 | One patch behind; the version string is broken in the brew build. |
| ki | 0.14.1 | - | `ki agent` launches and coordinates detached background agents (launch, queue, send, status, wait, watch, stop, recover, reconcile, sweep). |
| Paperclip | Checkout only: `knowledgeislands/paperclip` fork, server and cli `package.json` 0.3.1, last commit 25 Oct 2026 ("chore: bump libs") | v2026.1023.0, 23 Oct 2026 | **Not running**: nothing on Paperclip's port; the `node` listener on `localhost:3333` is `mcporter-proxy`, not Paperclip. No `paperclipai` CLI on PATH. |
| Cursor, Warp, Conductor, Amp, opencode, OpenClaw | Not installed | - | No app in `/Applications`, no cask or formula, no CLI on PATH. |

Other agent-adjacent installs seen (names only): casks `chatgpt`, `chatgpt-classic`, `claude`, `codexbar`, `copilot-cli`, `ghostty`, `gitbutler`, `linear`, `ollama-app`; formula `mcporter`. `/Applications` also holds Claude, ChatGPT, CodexBar and Ghostty.

### Orca CLI surface (from `orca --help`, 1.4.244)

Command groups: Startup (`open`, `serve`, `status`), Agent Discovery (`agent-context`), Agent Sessions (`search`), Accounts (`account add --agent claude|codex`; `account select` for OpenCode or Devin), Skills (`skills list|get|install|update|share`), Hosts (`host list`), Environments (`environment add|list|show|rm` for paired remote runtimes), VM recipes, Automations, Projects and host setups, Repos, Worktrees (`list|show|current|create|set|rm|ps`), `agent launch`, Files, Terminals (`list|show|read|send|wait|create|split|close`...), Orchestration, Computer Use, Linear, iOS emulator, embedded browser.

- `orca serve`: "Start an Orca runtime server without opening desktop window". Flags `--port` (default 6768), `--pairing-address` (LAN, Tailscale, SSH-forward or reverse-proxy endpoint), `--mobile-pairing`, `--no-pairing`, `--grant-desktop-control`, `--project-root`, `--recipe-json`, `--supervise` (for launchd or systemd: restarts itself with back-off, gives up after 6 failures in 15 minutes; "Not available on Windows yet"). Linux-only options cap per-terminal processes and memory through systemd user scopes.
- `orca host list`: three kinds of target - this machine, SSH targets registered on it (`--host ssh:<id>`, platform detected as linux/darwin/win32), and paired Orca servers (`--environment <name>`).
- `orca agent launch --agent <id>` and `orca worktree create --agent <id> --prompt ... --model --effort --setup run|skip|inherit --base-branch --parent-worktree|--no-parent`. Examples use `codex` and `claude`.
- `orca automations create --trigger <preset|cron|RRULE> --prompt --provider <codex|claude|gemini> [--precheck <cmd>] [--repo|--workspace|--project --host]`; `--host ssh:<target-id>` or `runtime:<environment-id>` schedules on another host.
- No merge command exists anywhere in the CLI help.

### Orca's own orchestration guide on this host

`~/.claude/skills/orchestration` and `~/.claude/skills/orca-cli` are symlinks to `~/.agents/skills/`. Both are discovery stubs that tell the agent to load the version-matched guide from the binary with `orca skills get orchestration` (references: coordinator-loop, legacy-contract-migration, low-level-topology, messaging-and-gates, placement-and-remote, recovery-and-cleanup, worker-contract) and `orca skills get orca-cli`. What the guide says:

- **Model.** A Run is a durable namespace and coordinator inbox; a Task is work; a Dispatch is one authoritative attempt at a Task. The Run "does not schedule or place workers". The coordinator loop: `status` -> `run-create --objective` -> `worker-start --spec ... --worktree current --agent codex|claude` for a full wave -> `check --wait --types worker_done,escalation,question --timeout-ms 900000`. Planned fan-out uses `task-create --deps <json>` then `worker-start --task`; prefer parallel waves over chains deeper than three or four; nested workers have a depth limit (`nested_worker_depth_exceeded`). A worker may start its own helpers on the same Run.
- **Headless.** `orca serve` runs the runtime without the desktop window; on Linux outside an Orca terminal the CLI must be called `orca-ide` because bare `orca` is the GNOME screen reader. A paired server "has no window". Server-hosted browser pages "run with no desktop attached; prefer them for long or unattended automation". If a command says Orca is not running, the guide says start it with `orca open`.
- **Connected servers (`--on`).** "The Run and Tasks remain authoritative on the current server. `--on` selects only the worker's execution server and appears only on `worker-start`." Remote placement must be `new-top-level` with an exact remote repo selector or an exact existing remote workspace (`current` and `new-child` are invalid remotely). Afterwards address the worker by Dispatch ID only. The execution host owns process, filesystem, transcript, stop and cleanup facts; contact loss yields `unverifiable`, never a synthetic exit, and Orca never falls back to local execution. `worker-list --include-remote` is needed to see remote workers.
- **Agents it spawns.** Codex and Claude in every example. Group addresses cover `@claude`, `@codex`, `@opencode`, `@gemini`, `@droid`, `@grok`, `@cursor`. Model and effort launch preferences are documented for Claude, Codex, Cursor, Antigravity and Muse, with OpenCode model override only in an existing worktree. The orca-cli guide adds `omp`, `pi`, `grok` "and other installed agents"; automations' `--extra-agent-args` covers claude, codex, codebuddy, cursor, grok and omp.
- **Worktrees.** "A fresh worker means a fresh agent terminal, not a new Git worktree." Default is `--worktree current`; `new-child` creates a stacked child worktree; `new-top-level` an independent one; both run repository setup by default (`--setup run`), honouring the repo's `start-immediately` or `wait-for-setup` policy. Folder workspaces (non-Git) are first-class via `project setup-existing-folder`. Lineage, Git base, filesystem isolation, coordination parentage and execution host are separate decisions.
- **Merging back.** Not covered. Neither guide nor CLI has a merge step; settlement means `worker_done` plus a coordinator decision to reuse, retain or release the worker terminal (`worker-release`, `worker-retain`). Merge is left to Git or the desktop app (the README describes comparing and merging in the app).
- **Gates.** `gate-create --task --question --options <json>`, `gate-resolve`, `gate-list`: coordinator-owned Task-DAG decisions. "Do not create a gate merely to answer a worker's `ask`."
- **Ask/reply.** A worker's `ask` blocks; on timeout one durable question stays pending and the worker resumes by message ID. The coordinator answers with `reply --id <message_id> --body`. Workers must never open a local question UI the coordinator cannot answer.
- **worker_done.** Sent exactly once from the dispatched terminal with a three-sentence summary, both lifecycle IDs and explicit `--outcome succeeded|failed`; optional `--files-modified`, `--report-path`. Heartbeats prove liveness, not completion. After `worker_done` the worker idles.
- **Liveness.** Layered: `worker-list`'s `projection.liveness` (fleet verdict) and `worker-show`'s PTY observation; "a live terminal can still hold a dead or stuck agent". Only positive proof of exit authorises stop, abandon or retry; after three empty waits enumerate with `worker-list` and follow its literal `nextAction`.
- **Automations.** Scheduled prompts (hourly, daily, weekdays, weekly, cron, RRULE) run by a chosen provider in a new worktree per run or an existing workspace (`--reuse-session`), with an optional shell `--precheck` gate whose skips appear in run history.
- **Wake of an idle coordinator.** "A successful `orchestration send` proves durable enqueue; its wake or nudge is best-effort attention only and does not prove the recipient read or accepted it." The reliable path is the coordinator itself blocking in `check --wait`; a coordinator whose turn has ended is only nudged.

## Part 2 - Tools

### Zed (editor) and Delta

- **What and layer.** Open-source editor with a built-in Zed Agent that also hosts external agents over ACP (Agent Client Protocol). Editor layer, not an orchestrator.
- **Installed.** 1.26.2.
- **ACP agents.** Zed lists Claude Agent, Codex, OpenCode, Copilot, Cursor, Pi, Gemini CLI and Poolside, "curated, not exhaustive", installed from the ACP Registry or a custom `agent_servers` entry ([external agents](https://zed.dev/docs/ai/external-agents)). ACP's own list adds Goose, Junie, Kiro and others ([ACP agents](https://agentclientprotocol.com/overview/agents)). ACP's maintainer and licence: **unverified**.
- **Worktrees and merge-back.** User picks worktrees in the title bar (detached HEAD); a `create_worktree` task hook runs after creation; merge-back is manual ("merge the changes through your normal Git workflow"); archiving a thread removes its worktree ([parallel agents](https://zed.dev/docs/ai/parallel-agents)).
- **Parallel agents.** Threads Sidebar runs several threads at once, each possibly a different agent; Terminal Threads wrap a native CLI such as `claude` ([terminal threads](https://zed.dev/docs/ai/terminal-threads)).
- **Queues, liveness, asking.** No task queue or dependencies; message queueing inside a thread; steer only for the Zed Agent because "Zed can't detect turn boundaries for external agents" ([agent panel](https://zed.dev/docs/ai/agent-panel)). Sidebar status indicator, states undocumented. Tool permissions allow, deny or confirm.
- **Scheduled, headless, remote.** None documented ([settings](https://zed.dev/docs/reference/all-settings)).
- **Skills, rules, MCP, hooks, memory.** `SKILL.md` in `~/.agents/skills` and `<worktree>/.agents/skills` for the Zed Agent only ([skills](https://zed.dev/docs/ai/skills)); first of `.rules`, `.cursorrules`, ..., `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` ([instructions](https://zed.dev/docs/ai/instructions)); MCP servers may be forwarded to external agents over ACP; no agent lifecycle hooks; no memory feature.
- **Maturity.** Stable 1.26.2 on 28 Oct 2026, several releases a week ([releases](https://zed.dev/releases/stable)); GPL-3.0-or-later with Apache-2.0 components ([repo](https://github.com/zed-industries/zed)).
- **Platform.** macOS, Linux, Windows; no headless mode.
- **Wake/notify.** Desktop notification or sound only (`agent.notify_when_agent_waiting`, `agent.play_sound_when_agent_done`); Terminal Threads react to BEL. No programmatic hook.
- **Delta.** Found. A separate Zed Industries app, "a multiplayer environment for coding with agents and reviewing what they build", built on DeltaDB, which "replicates the conversation and the worktree together, in real time". Agents can move to a cloud runner ("close your laptop, and the agent keeps going"); "connects to third-party agent harnesses, starting with Claude Code". Announced 12 Aug 2026 as a private beta ([Introducing Delta](https://zed.dev/blog/introducing-delta)). Roadmap shows remote runtime, Delta CLI, MCP, @mentions, ACP support and GitHub access in progress; sandboxing and branching next; no API, notification system, self-hosting or licence stated ([roadmap](https://delta.dev/roadmap)). A September public beta appears only in search results: **unverified**.

### Claude Code (agent runtime and platform)

- **Installed.** 2.1.308 (npm `stable`); `latest` is 2.1.314 (30 Oct). Releases every one to three days ([releases](https://github.com/anthropics/claude-code/releases)); licence "SEE LICENSE IN README.md", proprietary ([npm](https://registry.npmjs.org/@anthropic-ai/claude-code)).
- **Worktrees and merge-back.** `claude --worktree <name>` creates `.claude/worktrees/<name>` on `worktree-<name>`; subagents can set `isolation: worktree`; `.worktreeinclude`, `worktree.baseRef`, `WorktreeCreate`/`WorktreeRemove` hooks; isolation enforced; no automatic merge ([worktrees](https://code.claude.com/docs/en/worktrees.md)). Background sessions get a worktree, commit and push, may open a draft PR, never merge or push to main ([agent view](https://code.claude.com/docs/en/agent-view.md)).
- **Parallel agents.** Subagents, background sessions (`claude --bg`, `/bg`, `claude agents`), and experimental agent teams (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`).
- **Task queues and dependencies.** Agent teams share a task list with dependencies, blocked state, file-locked claiming and auto-unblock; one team per session, no nesting ([agent teams](https://code.claude.com/docs/en/agent-teams.md)).
- **Liveness.** `claude agents --json --all` reports `state` (working, blocked, done, failed, stopped), `status` and `waitingFor`; `claude logs|attach|stop|respawn`, `claude daemon status`.
- **Asking the human.** `PermissionRequest`/`PreToolUse` hooks return allow, deny, ask or defer; in `-p` an unapproved request is denied unless a hook or `--permission-prompt-tool` approves ([headless](https://code.claude.com/docs/en/headless.md), [hooks](https://code.claude.com/docs/en/hooks)).
- **Scheduled/background.** Cloud scheduled tasks (routines, research preview) triggered by schedule, API fire or GitHub events ([routines](https://code.claude.com/docs/en/routines.md)); desktop scheduled tasks, GitHub Actions, `/loop` ([common workflows](https://code.claude.com/docs/en/common-workflows)).
- **Headless.** `claude -p` with exit codes, `--output-format json|stream-json`, `--json-schema`, `--resume`; Agent SDK in Python and TypeScript.
- **Remote.** `claude --cloud`, `--teleport`, self-hosted environments ([web](https://code.claude.com/docs/en/claude-code-on-the-web.md)); cross-session messaging (`ListAgents`, `SendMessage`) over a Unix socket locally and through Remote Control across machines ([cross-session](https://code.claude.com/docs/en/cross-session-messaging.md)).
- **Skills, rules, memory.** Skills in `~/.claude/skills`, `.claude/skills`, plugins; `.agents/skills` not mentioned ([skills](https://code.claude.com/docs/en/skills.md)). CLAUDE.md, `.claude/rules/`, imports, auto memory; AGENTS.md read only when no CLAUDE.md exists ([memory](https://code.claude.com/docs/en/memory)).
- **MCP.** Client; Channels (research preview) are MCP servers that push events into a running session and can relay permission prompts ([channels](https://code.claude.com/docs/en/channels.md)).
- **Hooks.** 33 events including Stop, SubagentStop, Notification, TaskCreated, TaskCompleted, TeammateIdle, StopFailure, WorktreeCreate; handlers command, http, mcp_tool, prompt, agent.
- **Platform.** macOS, Linux, WSL, Windows; headless supported.
- **Wake/notify.** Stop, SubagentStop and Notification hooks (with `agent_needs_input` and `agent_completed` matchers) as command or http handlers; `claude agents --json` polling; `SendMessage` `notify_when_idle` starts a new turn in an idle asker; the session inbox socket; `-p` exit code and stream-json `result`; team idle notifications to the lead. Richest of all tools surveyed.

### OpenAI Codex CLI

- **Installed.** 0.165.0; latest stable 0.166.0 (29 Oct), every two to four days ([releases](https://github.com/openai/codex/releases), [changelog](https://learn.chatgpt.com/docs/changelog)). Apache-2.0; macOS, Linux (x86_64, arm64), Windows ([repo](https://github.com/openai/codex)). Docs moved to learn.chatgpt.com.
- **Worktrees and merge-back.** Global `--worktree` starts in a managed Git worktree (interactive, `exec`, `fork`; not `resume`); merge-back manual; `codex apply` applies a cloud diff ([commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli)). App worktree retention details from a search snippet only: **unverified**.
- **Parallel agents.** Subagents (`default`, `worker`, `explorer`, custom TOML in `.codex/agents/`), capped by `agents.max_concurrent_threads_per_session`; they share the parent sandbox ([subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)).
- **Task queues.** None documented.
- **Liveness and asking.** App-server emits `thread/status/changed` (incl. `waitingOnApproval`), `turn/started`, `turn/completed`, approval requests ([app-server](https://learn.chatgpt.com/docs/app-server)); `approval_policy` on-request, never or granular; `PermissionRequest` hook; in non-interactive runs a subagent's approval fails back to its parent.
- **Scheduled.** Desktop-app and web scheduled tasks and cloud Team Tasks (RRULE, Gmail, Slack, GitHub triggers); the CLI has none ([automations](https://learn.chatgpt.com/docs/automations?surface=app)).
- **Headless.** `codex exec --json` JSONL (`turn.completed`, `turn.failed`...), `--output-schema`, `exec resume`; exit codes undocumented ([non-interactive](https://learn.chatgpt.com/docs/non-interactive-mode)). App-server (experimental) over stdio, WebSocket or Unix socket.
- **Remote.** `codex --remote` to an app-server (non-loopback listeners unauthenticated by default during rollout); Codex Cloud ([cloud](https://learn.chatgpt.com/docs/cloud)).
- **Skills, AGENTS.md, MCP.** Skills in `.agents/skills`, `~/.agents/skills`, `/etc/codex/skills` ([skills](https://learn.chatgpt.com/docs/build-skills.md)); AGENTS.md native, root to cwd, 32 KiB default ([AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)); MCP client; **`codex mcp-server` has been removed**, use the app-server.
- **Hooks.** SessionStart, SubagentStart/Stop, PreToolUse, PermissionRequest, PostToolUse, Pre/PostCompact, UserPromptSubmit, Stop, Interrupt, SessionEnd; hash-based trust required ([hooks](https://learn.chatgpt.com/docs/hooks)).
- **Memory.** **Unverified** (not researched in depth).
- **Wake/notify.** `notify = [cmd]` receives a JSON payload ([config](https://learn.chatgpt.com/docs/config-file/config-reference)); TUI osc9 or bel notifications; Stop/SubagentStop hooks; app-server and `exec --json` events. "Agent-message wakes" in 0.165 changelog are undocumented: **unverified**.

### Orca (multi-agent manager / orchestrator)

- **Installed.** 1.4.244; vendor repo [stablyai/orca](https://github.com/stablyai/orca), docs [onorca.dev](https://onorca.dev/docs). MIT, roughly daily releases ([releases](https://github.com/stablyai/orca/releases)). Desktop app with editor, terminal and browser; iOS and Android companions.
- **Platform.** macOS, Windows, Linux (AppImage, .deb, .rpm; CLI `orca-ide`) ([install](https://onorca.dev/docs/install)).
- **Worktrees.** First-class (`worktree create`, `new-child`, `new-top-level`, setup hooks). **No merge command** in CLI or docs reference; the README describes comparing and merging in the app.
- **Parallel agents.** "If it runs in a terminal, it runs in Orca"; about 34 agents including Claude Code, Codex, OpenCode, Gemini ([README](https://github.com/stablyai/orca)).
- **Task queues and dependencies.** Orchestration Runs, Tasks with `--deps`, Dispatches, decision gates; marked experimental in Settings ([orchestration](https://onorca.dev/docs/cli/orchestration)).
- **Liveness.** Status hooks it installs into agents (working, waiting, done; `orca agent hooks status|on|off`), heartbeats (default 5 min), `worker-list` liveness projection ([hooks and memory](https://onorca.dev/docs/agents/hooks-memory)).
- **Asking the human.** Worker `ask` blocks on coordinator `reply`; Allow/Deny prompts reach remote and phone clients.
- **Scheduled.** `automations` with cron/RRULE, precheck, `--host` for another host ([automations](https://onorca.dev/docs/cli/automations)). Whether the desktop must be running for automations on a laptop: **unverified**; on a server the runtime runs them.
- **Headless/remote.** `orca serve` for "a headless Linux box, VM, or managed service"; `orca serve service install` creates a systemd user unit or LaunchAgent (docs; not in this host's local help, which shows `--supervise` instead); beta, LAN or tailnet only ([remote servers](https://onorca.dev/docs/remote-servers)); SSH worktrees ([ssh](https://onorca.dev/docs/ssh)).
- **Skills, MCP, memory.** Ships `orca-cli`, `orchestration`, `computer-use` skills ([skills](https://onorca.dev/docs/cli/skills)); configures MCP servers for agents but runs none itself; does not modify CLAUDE.md or AGENTS.md; no memory feature.
- **Wake/notify.** Coordinator blocks on `orchestration check --wait`; workers must send `worker_done`, `ask` or escalation; `terminal wait --for tui-idle`; desktop notification, sound, Dock badge, inbox bell, mobile push. No webhook or event-subscription API ([notifications](https://onorca.dev/docs/notifications)). Wake of an idle coordinator is best-effort only.

### Paperclip (agent platform)

- **Installed.** Fork checkout only (0.3.1 package versions, 25 Oct commit); not running. Upstream [paperclipai/paperclip](https://github.com/paperclipai/paperclip), MIT, v2026.1023.0 on 23 Oct, weekly to fortnightly ([releases](https://github.com/paperclipai/paperclip/releases)).
- **What.** Self-hosted Node.js server and React UI running a "company" of agents: org chart, goals, budgets, governance. "If OpenClaw is an employee, Paperclip is the company."
- **Adapters.** claude_local, codex_local, gemini_local, cursor, opencode_local, pi_local, hermes_local, grok_local, kimi_local; openclaw_gateway, process and http not yet selectable in UI ([adapters](https://docs.paperclip.ing/reference/adapters/overview/)).
- **Worktrees.** Optional isolated execution workspaces (experimental) with branch template, base ref, provision and teardown; no automatic merge ([projects](https://docs.paperclip.ing/guides/projects-workflow/projects/)).
- **Queues and dependencies.** Issues with atomic checkout, execution locks, "first-class blocker dependencies", per-agent max concurrent runs.
- **Liveness.** Heartbeat runs from a DB-backed wakeup queue; timer heartbeats off by default; watchdogs page not read (**unverified**).
- **Asking.** Blocked inbox with named unblock owner; board approvals; budget hard stops ([blocked inbox](https://docs.paperclip.ing/guides/day-to-day/blocked-inbox/)).
- **Scheduled.** Routines by cron, signed webhooks or API, with concurrency and catch-up policies ([routines](https://docs.paperclip.ing/guides/projects-workflow/routines/)).
- **Headless/remote.** Server by design; Docker Compose image bundling claude, codex, opencode, gemini ([docker](https://docs.paperclip.ing/reference/deploy/docker/)); local_trusted, private and public modes ([deploy](https://docs.paperclip.ing/reference/deploy/overview/)); sandbox providers (e2b, Daytona, Modal). Supported OS not stated: **unverified**.
- **Skills, MCP, hooks, memory.** Company skill library synced from GitHub; MCP Tool Gateway, and Paperclip reachable as an MCP server since v2026.1012.0; in-process plugins and inbound plugin webhooks; memory "in progress".
- **Wake/notify.** Agents are woken by assignment, comment, "Wake now", hand-off, routine or unblock request (`PAPERCLIP_WAKE_REASON`). No outbound webhook: issue [#1790](https://github.com/paperclipai/paperclip/issues/1790) confirms "there is no native HTTP outbound surface"; plugins only.

### Hermes Agent (Nous Research)

- **Installed.** 0.22.4 via brew; upstream v0.22.5 (22 Oct), several releases a week; MIT ([repo](https://github.com/NousResearch/hermes-agent), [releases](https://github.com/NousResearch/hermes-agent/releases)).
- **What and layer.** Self-improving agent runtime plus personal agent platform (gateway, kanban, cron); any model provider.
- **Platform.** Linux, macOS, WSL2, Windows, Termux; terminal backends local, Docker, SSH, Modal, Daytona, Vercel Sandbox.
- **Worktrees.** `hermes -w`/`--worktree`, `/worktree new` on `hermes/<name>`; kanban `--workspace worktree`; no automatic merge; completion contract can require PR checks to pass ([worktrees](https://hermes-agent.nousresearch.com/docs/user-guide/git-worktrees), [kanban](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban)).
- **Parallel and queues.** `delegate_task` subagents (3 concurrent default); in-process teammates; SQLite kanban with dependencies (`link`), atomic claim, `swarm` graphs (parallel workers -> verifier -> synthesizer), dispatcher in the gateway. Local `hermes kanban --help` confirms `link`, `claim`, `block`, `heartbeat`, `notify-subscribe`, `swarm`, `decompose`, `daemon`, `dispatch`.
- **Liveness and asking.** `kanban_heartbeat`; stale workers reclaimed; exit without terminal call leads to nudges then auto-block; `kanban_block kind=needs_input`; approval hooks ([hooks](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks)).
- **Scheduled.** `hermes cron` inside the gateway, delivered to messaging channels ([cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)).
- **Headless/remote.** Gateway under systemd; OpenAI-compatible API server; A2A in and out ([A2A](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a)); `hermes peer` for cross-machine bot DMs (local help).
- **Skills, rules, MCP, hooks, memory.** agentskills.io skills; loads AGENTS.md, CLAUDE.md, `.hermes.md`, SOUL.md, `.cursorrules`; MCP client (MCP serve moved to a plugin in 0.22.5); gateway, plugin and shell hooks plus outbound signed webhooks; MEMORY.md, USER.md, Honcho, Mem0 ([overview](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)).
- **Wake/notify.** Kanban subscriptions with `notify+wake` give the subscriber a real turn; plugin hooks `kanban_task_completed`, `kanban_task_blocked`, `on_kanban_worker_exited`; gateway `agent:end`; outbound webhooks (event list **unverified**); A2A push.

### herdr

- **Installed.** 0.9.5 (current); Apache-2.0; stable every 2 to 3 weeks plus previews ([repo](https://github.com/herdrdev/herdr), [herdr.dev](https://herdr.dev)). Also a desktop app ([herdr-app](https://github.com/herdrdev/herdr-app)) and `herdr-core` runtime (`hc`, no releases yet) ([core](https://herdr.dev/core/)).
- **What and layer.** Terminal workspace manager for AI coding agents: a Rust TUI multiplexer with a persistent background server.
- **Platform.** TUI on macOS, Linux, Windows; app on Apple Silicon macOS and Linux with a desktop session.
- **Worktrees.** `herdr worktree list|create|open|remove` (local help); remove never deletes the branch; no merge-back ([socket API](https://herdr.dev/docs/socket-api/)).
- **Parallel agents.** "22 agents detected out of the box" including Claude Code, Codex, OpenCode, Cursor, Grok, Copilot, Pi, Hermes ([tui](https://herdr.dev/tui/)); `herdr integration install` installs status integrations.
- **Queues, scheduling, MCP, memory.** None documented.
- **Liveness and asking.** Panes report working, blocked, idle, done or unknown from process, screen and hooks; "when an agent stops and needs an answer, herdr says so".
- **Headless/remote.** `herdr server` runs headless and outlives the shell (processes do not survive reboot); `herdr machine` over SSH merges remote agents into one list; `--remote <ssh-target>` attaches; `hc run --on <host>`.
- **Skills.** Ships an agent skill (`herdr --skill`).
- **Wake/notify.** `herdr agent wait <pane> --until done|blocked` is server-owned and event-driven; `events.subscribe` delivers `pane.agent_status_changed` (filterable to `blocked`); `notification.show`; ntfy.sh mod for phone ([guide](https://herdr.dev/guide/)).

### OpenClaw

- **Installed.** Not installed. MIT; OpenClaw Foundation, no paid tier; v2026.10.9 on 29 Oct plus an LTS line ([repo](https://github.com/openclaw/openclaw), [releases](https://github.com/openclaw/openclaw/releases), [docs](https://docs.openclaw.ai)).
- **What and layer.** Self-hosted personal assistant gateway connecting 20+ chat channels to agents; agent platform. Paperclip treats it as an "employee" via `openclaw_gateway`; Hermes can import an OpenClaw setup.
- **Coding agents.** Claude Code, Cursor, Copilot, OpenCode, Gemini CLI as ACP harnesses; Codex via a native path ([ACP agents](https://docs.openclaw.ai/tools/acp-agents)).
- **Parallel and worktrees.** Multi-agent routing ([multi-agent](https://docs.openclaw.ai/concepts/multi-agent)); `sessions_spawn` background sub-agents with `worktree` parameters whose behaviour is undocumented; no merge-back ([subagents](https://docs.openclaw.ai/tools/subagents)).
- **Queues.** Shared Tasks ledger and TaskFlow API "have been removed"; replaced by Lobster pipelines, sub-agents or ACP ([automation](https://docs.openclaw.ai/automation)).
- **Liveness, asking, scheduling.** Subagents panel (Running/Finished); heartbeat as a 30-minute automation ([heartbeat](https://docs.openclaw.ai/gateway/heartbeat)); exec and plugin approvals; cron and webhook triggers.
- **Headless/remote.** Gateway as a service on macOS and Linux; clients over `wss://` with token.
- **Skills, MCP, hooks, memory.** ClawHub skills; AGENTS.md "standing orders"; `openclaw mcp serve` ([mcp serve](https://docs.openclaw.ai/cli/mcp/serve)); `openclaw hooks` and plugin hooks; local memory.
- **Wake/notify.** Sub-agents announce results to the requester; MCP `events_wait` long-poll (300 s) for messages and approval requests; Claude channel push notifications; cron results to a channel or webhook.

### Warp and Oz

- **Installed.** Not installed. Client open source under AGPL since 28 Apr 2026 ([blog](https://www.warp.dev/blog/warp-is-now-open-source)); weekly releases, latest `v0.2026.10.21.08.25` ([changelog](https://docs.warp.dev/changelog/2026.md)). Oz is a commercial cloud platform (launched 10 Feb 2026) for running and orchestrating agents ([Oz](https://www.warp.dev/blog/oz-orchestration-platform-cloud-agents)); runs Warp Agent, Claude Code and Codex harnesses since May 2026 ([multi-harness](https://www.warp.dev/blog/multi-harness-cloud-agent-orchestration)). Whether Oz is open source: **unverified**.
- **Layer.** Terminal plus agent runtime (Warp), agent platform and orchestrator (Oz).
- **Worktrees.** Detects worktrees you create; automatic creation and merge-back not described ([worktrees](https://docs.warp.dev/code/git-worktrees/)); Oz delivers branches and PRs from Docker environments.
- **Parallel, queues, liveness.** Unbounded cloud agents; parent/child orchestration; run states INPROGRESS, SUCCEEDED, BLOCKED, FAILED, ERROR, CANCELLED ([notifications](https://docs.warp.dev/agents/capabilities/agent-notifications/)); tasks with descendants in the API, no explicit dependency graph (**unverified**) ([OpenAPI](https://docs.warp.dev/openapi.yaml)).
- **Asking.** "Request" notification when blocked; unattended runs end as blocked; follow-up and interrupt API.
- **Scheduled/headless/remote.** `oz schedule --cron`; `oz` CLI for CI and servers; REST API and SDKs; self-hosted runners on Enterprise ([platform](https://docs.warp.dev/agent-platform/cloud-agents/platform/)); Warp Agent CLI on Mac, Linux, Windows ([agent CLI](https://www.warp.dev/agent-cli)).
- **Rules, MCP, hooks, memory.** AGENTS.md default (WARP.md wins) ([rules](https://docs.warp.dev/agents/capabilities/rules/)); MCP stdio, HTTP, SSE, reads Claude Code and Codex configs ([MCP](https://docs.warp.dev/agents/capabilities/mcp/)); no hook API found (**unverified**); Agent Memory research preview.
- **Wake/notify.** Human-facing Complete, Request and Error notifications; parent run sees child BLOCKED; programmatic supervision by polling `GET /agent/runs/{id}`; no outbound webhook found (OpenAPI only partly read: **unverified**).

### Cursor

- **Installed.** Not installed. Editor 3.27; macOS, Windows, Linux ([download](https://cursor.com/download)); proprietary (licence not stated: **unverified**); changelog shows Agent SDK GA 20 Oct 2026 ([changelog](https://cursor.com/changelog)).
- **Layer.** Editor, CLI agent runtime and cloud agent platform.
- **Worktrees.** Agents Window native worktrees; `/worktree`, `/best-of-n`, and `/apply-worktree` to bring changes back; `.cursor/worktrees.json` setup ([worktrees](https://cursor.com/docs/configuration/worktrees)). Only tool with a documented merge-back command.
- **Parallel and cloud.** Cloud agents in isolated VMs, own branch, PRs; launched from editor, web, iOS, Slack, GitHub, Linear or API; self-hosted machines ([cloud agent](https://cursor.com/docs/cloud-agent)); `@cursor/sdk` with `run.stream()` and `wait()` ([SDK](https://cursor.com/blog/typescript-sdk)).
- **Queues.** None documented.
- **Scheduled.** Automations by cron, GitHub, Slack, Linear, PagerDuty or webhook ([automations](https://cursor.com/docs/cloud-agent/automations)).
- **Headless.** `agent -p --output-format stream-json`, `CURSOR_API_KEY`, macOS, Linux, WSL, Windows ([headless](https://cursor.com/docs/cli/headless), [CLI](https://cursor.com/docs/cli/overview)); in `-p` mode it has full write access ([using](https://cursor.com/docs/cli/using)).
- **Rules, skills, MCP, hooks.** `.cursor/rules`, nested AGENTS.md, CLAUDE.md ([rules](https://cursor.com/docs/context/rules)); skills from `.agents/skills`, `.cursor/skills`, `.claude/skills`, `.codex/skills` ([skills](https://cursor.com/docs/context/skills)); MCP client ([MCP](https://cursor.com/docs/cli/mcp)); `hooks.json` with stop, subagentStop and others, stop can return a follow-up message ([hooks](https://cursor.com/docs/agent/hooks)). Memory: **unverified**.
- **Wake/notify.** Cloud Agents API `statusChange` webhook on FINISHED or ERROR, HMAC-signed ([webhooks](https://cursor.com/docs/cloud-agent/api/webhooks)); SDK `wait()`; stop and subagentStop hooks; `-p` result event and exit code.

### Amp (Sourcegraph)

- **Installed.** Not installed. Proprietary ([licence](https://unpkg.com/@sourcegraph/amp/LICENSE.md)); continuous builds, latest npm build about 30 Oct 2026 ([npm](https://registry.npmjs.org/@sourcegraph/amp/latest)); near-daily news ([news](https://ampcode.com/news)).
- **Layer.** Agent runtime and platform: CLI/TUI, web, desktop and mobile with shared threads; orbs (cloud machines) and runners (your machines); Puck meta-agent coordinates agents ([manual](https://ampcode.com/manual)).
- **Worktrees.** Runner "New Worktree" and safe archive-and-remove; no merge-back command ([runners](https://ampcode.com/docs/cli/runners)).
- **Parallel.** Task subagents ([subagents](https://ampcode.com/docs/models-and-subagents)); agent-to-agent parallel threads on orbs or runners ([agent-to-agent](https://ampcode.com/docs/orbs/agent-to-agent)). Queues: none documented.
- **Liveness and asking.** Stream JSON `subagent_finished` ([streaming](https://ampcode.com/docs/cli/streaming-json)); plugin `ctx.ui.confirm`; MCP "Ask First".
- **Scheduled.** Per-thread schedules and event subscriptions wake the orb ([automations](https://ampcode.com/docs/orbs/automations)).
- **Headless/remote.** `amp -x`, `--stream-json`, headless runners, TypeScript and Python SDKs ([execute](https://ampcode.com/docs/cli/execute-mode), [SDK](https://ampcode.com/docs/sdk)); self-hosted orbs; macOS, Linux, WSL ([CLI](https://ampcode.com/docs/cli)).
- **Rules, MCP, hooks.** AGENTS.md with CLAUDE.md fallback ([AGENTS.md](https://ampcode.com/docs/customize/agents-md)); MCP with per-tool policies ([MCP](https://ampcode.com/docs/customize/mcp)); TypeScript plugins with `agent.end`, `tool.call` ([plugins](https://ampcode.com/docs/customize/plugins)). Memory: **unverified**.
- **Wake/notify.** Stream-json `result` is "the only signal that the run is over"; `subagent_finished`; plugin `agent.end`; app alerts when a thread is ready; no outbound completion webhook.

### opencode

- **Installed.** Not installed. MIT; v2.2.2 on 29 Oct 2026, near-daily; GitHub "Latest" still 1.x ([releases](https://github.com/anomalyco/opencode/releases), [changelog](https://opencode.ai/changelog)); repo moved from sst to anomalyco. opencode.ai docs may lag 2.x.
- **Layer.** Agent runtime with server and SDK; moving into multi-agent management (worktree picker, inbox, schedules).
- **Worktrees.** 2.2 worktree picker and Code Mode `worktree_create/list/remove`; merge-back undocumented.
- **Parallel and queues.** Build and Plan primary agents, General and Explore subagents, background subagents ([agents](https://opencode.ai/docs/agents/)); `/goal` loop; no dependency graph.
- **Liveness and asking.** `GET /session/status`, permissions ask/allow/deny, `question` tool, permission-response endpoint ([server](https://opencode.ai/docs/server/)).
- **Scheduled.** Experimental `/schedule` and SDK schedule API (2.2.1); GitHub Action cron ([GitHub](https://opencode.ai/docs/github/)).
- **Headless/remote.** `opencode serve` (OpenAPI, basic auth, mDNS); `opencode run --attach`; multi-server session search; pairing ([CLI](https://opencode.ai/docs/cli/)).
- **Rules, MCP, hooks, ACP.** AGENTS.md with CLAUDE.md fallback, reads `~/.claude/skills` ([rules](https://opencode.ai/docs/rules/)); MCP client; plugins with `session.idle`, `permission.asked` and tool events ([plugins](https://opencode.ai/docs/plugins/)); `opencode acp` ([ACP](https://opencode.ai/docs/acp/)). Memory: **unverified**.
- **Wake/notify.** SSE `/event` bus; plugin `session.idle` handler can run any command; terminal and desktop notifications.

### Other comparable orchestrators (brief)

- **Conductor** ([docs](https://www.conductor.build/docs/), [changelog](https://www.conductor.build/changelog)): Mac app running Claude Code, Codex, Cursor, OpenCode in parallel workspaces with diff review, PR, merge and archive; 0.92.0 "Remote control" 23 Oct 2026; API since 0.77. Licence and notify mechanism **unverified**.
- **Claude Squad** ([repo](https://github.com/smtg-ai/claude-squad)): TUI over tmux and worktrees for Claude Code, Codex, Gemini, Aider, OpenCode, Amp; AGPL-3.0; latest v1.0.20 (year **unverified**).
- **Vibe Kanban** ([repo](https://github.com/BloopAI/vibe-kanban), [shutdown](https://www.vibekanban.com/blog/shutdown)): kanban to agent workspaces with review and PR; Apache-2.0; bloop shut down 10 Apr 2026, now community-maintained, local only.
- **Paradev, formerly Superset** ([site](https://paradev.com/)): desktop app, any CLI agent in its own worktree, SSH hosts, automations, CLI, SDK, MCP server, "waiting on you" view; Elastic License 2.0.
- **cmux** ([repo](https://github.com/manaflow-ai/cmux)): macOS terminal on libghostty with per-agent attention rings; `cmux notify` wired into Claude Code and OpenCode hooks; socket control; GPL-3.0-or-later.
- **Crystal -> Nimbalyst** ([repo](https://github.com/stravu/crystal)), **Sculptor** ([site](https://imbue.com/sculptor/)): worktree or container isolated parallel sessions; details **unverified**. Terragon not researched.

## Capability matrix

Y = native and documented; P = partial, experimental, preview or limited; N = not offered or not documented; U = unverified. "Merge" means a native step that brings worktree changes back, not just a PR.

| Tool | Layer | Worktree isolation | Merge-back | Parallel agents | Task queue / deps | Liveness / status | Ask human | Scheduled / background | Headless / server | Remote / multi-host | Skills / AGENTS.md | MCP | Hooks | Memory | Linux | Supervisor wake |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Zed | Editor | P (manual) | N | Y | N | P | Y | N | N | N | Y | Y (forwarded) | N | N | Y | N (desktop alert only) |
| Delta (Zed) | Agent collaboration app | P (replicated worktree) | N | U | N | U | U | P (cloud runner) | N | P (roadmap) | U | N (roadmap) | N | N | U | N |
| Claude Code | Agent runtime / platform | Y | N (PR only) | Y | P (teams, experimental) | Y | Y | Y | Y | Y | Y (AGENTS.md only without CLAUDE.md) | Y | Y | Y | Y | Y (hooks, notify_when_idle, socket) |
| Codex CLI | Agent runtime | Y | P (`codex apply` for cloud) | Y | N | Y (app-server) | Y | P (app/cloud, not CLI) | Y | Y (app-server, cloud) | Y | Y (client; server removed) | Y | U | Y | Y (`notify`, Stop hook, events) |
| Orca | Orchestrator | Y | N (in-app only, U) | Y | Y (experimental) | Y | Y (ask/reply, gates) | Y | Y (`orca serve`, beta) | Y (SSH, paired servers, `--on`) | Y (ships skills) | P (configures only) | P (status hooks) | N | Y (`orca-ide`) | P (blocking `check --wait`; idle wake best-effort) |
| Paperclip | Agent platform | P (experimental) | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | P (plugins) | P (in progress) | Y (Docker) | P (wakes agents; no outbound webhook) |
| Hermes Agent | Runtime + platform | Y | N | Y | Y | Y | Y | Y | Y | Y (A2A, peers) | Y | Y | Y | Y | Y | Y (notify+wake, hooks, webhooks) |
| herdr | Terminal / agent manager | Y | N | Y | N | Y | P | N | Y (server) | Y (SSH machines) | P (own skill) | N | P (integrations) | N | Y | Y (`agent wait`, `events.subscribe`) |
| OpenClaw | Agent platform / gateway | P | N | Y | P (Lobster; ledger removed) | P | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y (announce, `events_wait`) |
| Warp / Oz | Terminal + cloud platform | P (detects) | N | Y | P | Y | Y | Y | Y (`oz`) | Y | Y | Y | U | P (preview) | Y | P (human alerts; API polling) |
| Cursor | Editor + CLI + cloud | Y | Y (`/apply-worktree`) | Y | N | Y | P | Y | Y | Y (cloud, self-hosted) | Y | Y | Y | U | Y | Y (cloud webhook, SDK wait, hooks) |
| Amp | Runtime + platform | Y (runners) | N | Y | N | Y | Y | Y | Y | Y | Y | Y | Y (plugins) | U | Y | P (stream-json, plugin `agent.end`) |
| opencode | Runtime + server | P (2.2) | N | Y | N | Y | Y | P (experimental) | Y | P | Y | Y | Y (plugins) | U | Y | Y (SSE bus, `session.idle`) |
| Conductor | Orchestrator (Mac) | Y | Y | Y | U | U | U | U | N | P (remote control) | U | U | U | U | N | U |
| Claude Squad | Orchestrator (TUI) | Y | N | Y | N | P | N | P (`-y`) | N | N | N | N | N | N | Y | N |
| Vibe Kanban | Orchestrator (kanban) | Y | Y (PR flow) | Y | Y (kanban) | P | U | U | P (local server) | N | U | Y | U | U | Y | U |

## Unverified points carried forward

- Orca: whether automations run while the desktop app is closed on a laptop; the in-app merge flow; `orca serve service install` (documented on the web, absent from this host's local help, which offers `--supervise`).
- Delta: public beta status and platforms; any API or licence.
- Codex: exit codes for `exec`; "agent-message wakes"; memory.
- Paperclip: supported OS list; watchdog behaviour; plugin event names.
- Hermes: full outbound webhook event list; `hermes peer` details.
- Warp/Oz: Oz licence; any completion callback in the remaining OpenAPI spec; hooks.
- Cursor: licence, CLI version cadence, memory, local desktop notification settings.
- Amp and opencode: memory features; opencode merge-back.
- Conductor, Claude Squad year, Nimbalyst, Sculptor, Terragon: largely unverified.
