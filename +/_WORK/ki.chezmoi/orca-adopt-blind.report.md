# Orca adoption › orca-adopt-blind

**Run report at 08:20 BST**

---

## Done

**Recommendation: choose the bounded laptop evaluation, with high confidence in that course.** Evaluate through **5 November 2026**, after correcting privacy, permissions and configuration ownership. Trial replacing only CodexBar initially, reversibly. Orca combines enough of Kris’s daily agent work to deserve a real trial, but the current unsafe launch defaults, managed-file drift and rapid changes do not justify widening installation or retiring several tools after a few hours.

Blind review completed on terra; no prior queries, decisions or run reports read; no installations, settings, hooks, repository files, credentials or remote state changed; no commits made.

Installation check: terra has Orca 1.4.237, an Electron application; the upstream project carries an [MIT licence](https://github.com/stablyai/orca/blob/main/LICENSE).

Rig check: the [source declaration](/Users/krisbrown/.local/share/chezmoi/dot_config/rig/conf.d/private_10-applications.toml:847) selects only the laptop profile and the stablyai cask; parsing every live Rig fragment found **no rendered Orca declaration**, so installation intent and rendered configuration are not yet reconciled.

### What it can replace

These are capability comparisons and adoption judgments, not completed migration tests.

- **Zed:** Orca covers agent supervision, file browsing, ordinary editing and diff review. Its [Monaco editor](https://www.onorca.dev/docs/editing/monaco) supports common editing/navigation features, but this audit establishes no equivalence for Kris’s language services, refactors, extensions or keyboard workflow. Keep Zed as the editor during evaluation.
- **Delta:** substantial overlap for solo agent threads, repository checkouts and reviewing results. [Delta’s distinguishing model](https://delta.dev/) includes shared conversations, synchronized code and conversation history, multiplayer review and cloud runners. Orca’s local workspace experience does not by itself establish replacement of those capabilities. If Kris does not use them, Delta becomes a later retirement candidate.
- **CodexBar:** the clearest small overlap. Terra’s footer already displays both Claude and Codex percentages and reset countdowns; [Orca’s usage roster](https://www.onorca.dev/docs/agents/usage-tracking) includes per-window limits and account handling. Trial living without CodexBar for seven days while retaining it installed. Check whether losing an independent menu-bar glance while Orca is closed or obscured matters.
- **GitHub Desktop:** Orca provides [staging, commits, diffs, remote actions and review creation](https://www.onorca.dev/docs/review/commit-push). That can replace routine Git work inside Orca; it does not prove replacement of Kris’s whole Desktop/Tower workflow across repositories. Keep both during this trial; do not start simultaneous Git-tool retirement trials.
- **Codex desktop app:** Orca can become the local multi-provider front end for Claude Code and Codex, with session management and review. The native chat surface is still labelled experimental in the [current release notes](https://github.com/stablyai/orca/releases). Codex’s own desktop experience also supports [persistent automations and broader tool workflows](https://openai.com/index/codex-for-almost-everything/), and its [cloud execution mode](https://learn.chatgpt.com/docs/environments/modes) is a separate capability. Keep it until the features Kris actually uses have passed equivalent tasks in Orca; migrating the interface does not retire the Codex CLI.
- **Ghostty:** Orca can absorb terminals used inside an agent workspace. Its [terminal documentation](https://www.onorca.dev/docs/terminal) identifies xterm.js and Ghostty-style configuration import, rather than Ghostty itself. Keep Ghostty for general shells, recovery and detached work; appearance and split support do not establish terminal parity.

Scriptability check: Orca has a documented [CLI for worktrees, terminals, files and automation](https://www.onorca.dev/docs/cli/overview). That is useful, but **does not establish compatibility with `ki agent`**. Keep detached runs on the existing CLI route, independently of whether Orca is open. No agent was started during this read-only audit.

### Sidebar answer

**Yes for an agent overview with recent activity; an exact Warp-style last-command list for every terminal is not established.** Orca has workspace navigation with inline agent states, an [Agents feed](https://www.onorca.dev/docs/activity) with recent-response previews and jump-to-session actions, and an optional [experimental Agent Dashboard](https://www.onorca.dev/docs/model/agents-sessions) showing task/last-message previews and Working / Needs You / Done states. Its tab hover cards identify the title and program. This is enough for “which agent was doing what?”, with a different arrangement from Warp’s vertical shell tabs.

Sidebar check limitation: terra currently has no configured projects, workspaces or terminal sessions, so populated behavior was verified against installed implementation and public documentation, not a live demonstration. The installed sidebar implementation is in [Orca’s application bundle](/Applications/Orca.app/Contents/Resources/app.asar). The settings also currently hide workspaces from Claude, GSD and other external locations; do not assume detached `ki agent` sessions will automatically appear.

### Safety findings and changes to make today

**Before the next agent launch, change Settings → Agents → Agent Permissions from Yolo to Manual.** The UI and stored profile agree that Claude and Codex currently launch with approval bypass; Codex also bypasses its sandbox. Native chats currently default to full access. Inspect per-agent/custom arguments and existing chats as well: changing the default does not retroactively change an existing chat, and custom arguments can remain. A Git worktree isolates files for version control; it is not a security boundary around the agent.

**Turn off “Trust the folder when Orca starts an agent” in the same page.** It is currently enabled and skips the initial trust question, allowing repository agent settings and hooks to run immediately. Previously trusted folders remain trusted.

**Turn off Settings → Privacy & Telemetry → Share anonymous usage data.** The live switch is on, and the stored profile records consent enabled for a new installation; installed initialization logic defaults new installations into telemetry. The [telemetry documentation](https://www.onorca.dev/docs/telemetry) describes feature/error counts sent to PostHog US and says prompts, file contents and terminal output are excluded. This audit verified configuration and code, not actual network payloads. The environment kill switches are alternatives, not required additional changes.

Hook check: both [Claude settings](/Users/krisbrown/.claude/settings.json) and [Codex hooks](/Users/krisbrown/.codex/hooks.json) contain Orca additions alongside existing hooks; Claude has 13 Orca event handlers and Codex nine. Their managed sources contain no Orca integration, and chezmoi reports drift in both targets. The scripts under [Orca’s hook directory](/Users/krisbrown/.orca/agent-hooks) relay status to a loopback endpoint, use short connection limits and gate reporting on Orca session context; they are not themselves evidence of permission bypass. Existing KI hook behavior has not been executed or proven unaffected.

Reconcile hook ownership before ordinary use: preserve existing governance hooks and give Orca’s dynamic additions a deliberate chezmoi coexistence policy. Do not copy the entire live files back into source or apply the whole unrelated chezmoi diff. If reconciliation cannot happen today, temporarily disable **Agent status hooks** in Orca; its [documented control](https://www.onorca.dev/docs/agents/hooks-memory) removes its hooks and stops reinstalling them, at the cost of status fidelity. Also reconcile the missing rendered Rig entry through the repository’s reviewed apply process.

Release-cadence check: upstream published seven desktop releases from 16–21 October, including three on 20 October; installed 1.4.237 matches the latest observed desktop release. This confirms frequent, sometimes same-day updates, not a measured defect rate. Stable releases only during evaluation, and recheck permissions, telemetry, hooks and session recovery after an update. [Release history](https://github.com/stablyai/orca/releases).

## In Progress

Nothing running.

Outstanding - no action requested now: this audit did not test session restoration, crashes, detached-run compatibility, quota accuracy, Git operations or editing on real projects. Safety changes and the trial remain proposed work for Kris or the supervising session, outside this run’s read-only authority.

Proposed acceptance checks for the 14-day trial:

1. **Configuration ownership:** after the reviewed safety changes, quit/reopen Orca and inspect only relevant chezmoi drift; privacy and permission choices persist, managed KI hooks remain intact and Orca does not fight source management. Repeat after an update.
2. **Real work:** complete one normal Claude task and one Codex task across at least three representative repositories, including an existing primary checkout; do not let Orca’s worktree defaults override repository policy. Review, navigation, search and editing must be comfortable without hidden migration costs.
3. **Detached continuity:** exercise a normal authorized `ki agent` run with Orca closed and then open; completion, status reporting, hook behavior and recovery must remain independent of the GUI.
4. **Session recovery:** check two concurrent agent sessions, an approval request, a completed turn, restart and sleep/wake; no lost work, incorrect status or silently changed permission mode.
5. **CodexBar trial only:** compare both providers’ readings/reset windows, refresh behavior and visibility outside Orca for seven days; reopen CodexBar immediately if the missing menu-bar view causes friction. Keep it installed throughout.
6. **Decision on 5 November:** widen only if the checks pass and Orca consistently reduces daily friction. A failed recovery or hook-ownership check blocks expansion; fix it or retire Orca. Consider any further retirement one tool at a time.

## Queries

### ORCA-ADOPT - Proceed with a bounded trial?

**Context:** Orca offers credible consolidation for local Claude/Codex work, but current privacy and permission defaults need correction, hooks conflict with managed configuration, and meaningful workflow/recovery testing is still absent.

**Query:** Should the supervising session arrange the safety corrections and a laptop-only trial through 5 November, with CodexBar as the sole initial retirement experiment?

**Options:**

a) (recommended, confidence high - reversible evaluation preserves working tools while testing the actual gaps) Make the safety corrections through the approved configuration workflow, run the named checks and trial CodexBar only.

b) Keep Orca laptop-only without a trial, after the same safety corrections; this preserves optionality but leaves the adoption question open.

c) Retire Orca if maintaining its configuration and hooks is not worth the expected benefit.

Widening to every Mac now is not recommended: the current evidence verifies features and unsafe defaults, not dependable replacement of the existing workflow.
