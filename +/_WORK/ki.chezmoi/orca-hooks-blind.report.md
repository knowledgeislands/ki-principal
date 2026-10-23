# Orca hooks configuration review › orca-hooks-blind

**Run report at 08:15 BST**

---

## Done

Completed the blind, local review of Orca 1.4.237; no queries, decisions or previous run reports were read, and no network calls were made.

Read the repository instructions, the [configuration-patterns guide](/Users/krisbrown/.local/share/chezmoi/docs/guides/agents/config-patterns.md:25), and the applicable chezmoi, delegation, coordination and authoring standards.

JSON comparison — passed: both live files and both `chezmoi cat` results parsed successfully; no secret values were printed.

Claude comparison — all twelve Orca hook commands and their metadata survive rendering, as does Orca’s `statusLine`; only the ordering of existing SessionStart and UserPromptSubmit groups changes. The supplied premise that apply removes Orca’s hooks from both files is therefore incorrect for the current checkout.

Codex comparison — rendering removes all nine Orca registrations and retains the two KI coordinator registrations. The events removed are SessionStart, UserPromptSubmit, PreToolUse, PermissionRequest, PostToolUse, SubagentStart, SubagentStop, Stop and Interrupt.

Ownership check — Claude already uses a [fragment binding](/Users/krisbrown/.local/share/chezmoi/dot_claude/modify_private_settings.json.tmpl:1) that preserves undeclared hooks. Codex still uses a [whole-file template](/Users/krisbrown/.local/share/chezmoi/dot_codex/hooks.json.tmpl:1). The guide and shared standard support managing declared fragments while preserving application-owned state.

Behaviour trace — the installed [Claude hook](/Users/krisbrown/.orca/agent-hooks/claude-hook.sh:51) and [Codex hook](/Users/krisbrown/.orca/agent-hooks/codex-hook.sh:49) forward event payloads and pane/session attribution to Orca’s authenticated loopback service. They use bounded requests, fail harmlessly, and can spool selected lifecycle events locally when delivery fails. They are status reporting integrations, not permission-approval bypasses. The token is supplied at runtime; its value does not belong in source.

Impact trace — Orca maps those events into working, waiting for approval, completed and interrupted states, tool details, and child-agent tracking; see its [Codex state normalizer](/Applications/Orca.app/Contents/Resources/app.asar.unpacked/out/shared/agent-hook-listener/providers/codex-state.js:121). Removing the registrations cuts off that native-hook evidence and can leave Orca’s terminal-agent status absent or stale. It does not establish that agent execution itself stops. Structured sessions have separate journal-based observations, so this is not evidence that every Orca mode breaks. Claude’s separate [status-line integration](/Users/krisbrown/.orca/agent-hooks/claude-statusline.sh:14) reports rate-limit usage and reset information; removing it would remove that feed too, but current rendering preserves it.

Read-only verification — both live-file hashes remained unchanged; no Git locks were present. Only this run’s requested status and report artifacts were written. No commits, applies or configuration changes were made.

## In Progress

Nothing is running.

Outstanding - no action requested now: this review establishes rendering behaviour and shipped-code intent, not a live Orca regression test. Hooks were not executed, and no agent was relaunched or interrupted. Repository gates were not run because no repository change was made.

## Queries

### ORCA-HOOKS - Preserve application ownership during evaluation

**Context:** Orca is being evaluated on the laptop profile. Claude already preserves its runtime additions, while Codex’s whole-file ownership conflicts with them. Copying Orca’s generated commands into source would add another owner for vendor-managed integration code, with upgrade and retirement drift. Codex also trusts individual hooks by hash and array position; any preservation change must keep the KI trust mapping correct and retain Orca’s own trust entries.

**Query:** Should a separate, narrowly scoped Codex fragment-preservation change be prepared, with only Codex’s hooks file held pending that change?

**Options:**

a) (recommended, confidence high - direct rendering proves the Codex conflict and Claude already demonstrates the preservation pattern) Prepare a separate change that manages KI’s declared registrations and preserves Orca’s undeclared hooks, following Pattern C. Keep Orca responsible for installing, upgrading and removing its commands rather than copying them into machine-conditional source. Verify preservation, idempotence and Codex’s positional trust mappings before seeking apply approval. Until then, hold Codex’s hooks target; Claude needs no Orca-specific hold, although its pending changes still require the normal review and apply approval.

b) Merge Orca’s hooks into laptop-conditional source. This protects the evaluation but risks stale vendor command copies, two competing owners, and leftover registrations after retirement. Profile filtering alone does not solve those ownership problems.

c) Let the next apply overwrite Orca’s hooks. On the current checkout that damages Codex’s hook-fed status integration during the evaluation and may distort the evaluation itself. Orca has installation and launch-preparation repair paths, but this review does not establish immediate recovery for existing sessions; repeated overwrites would remain a conflict.

d) Leave both files unapplied until evaluation ends. This temporarily preserves live state but unnecessarily holds Claude’s unrelated pending changes and defers Codex’s ownership conflict. Adoption would still require a durable solution; retirement would require deliberate cleanup rather than assuming overwrite covers every Orca registration and script.
