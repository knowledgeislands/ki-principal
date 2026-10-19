---
id: ki.chezmoi
level: project
title: 'KI > Rig > chezmoi'
project: chezmoi
theme: rig
worker: agent
supervisor: owner
state: handoff-to-supervisor
blocking: true
since: 2026-10-18T17:13:14Z
received: null
beat: null
mark: 2026-10-18T17:57:57Z
created_at: 2026-10-08T08:40:00Z
---

# ki.chezmoi

## Next steps

Mark `2026-10-18T17:57:57Z` retained. Kris's 19 October instruction authorised the reviewed four-target, scripts-excluded apply and necessary declared skill-link repair. Both are complete; no source edits remain in chezmoi, and prerequisite source commits are published. Do not replay the historical failed-gate or unapproved-apply claims in retained reports.

The reviewed artifact SHA-256 `717414930011156a95ea6cc247ce1b07cfae8afbd9232de58a804ef2b35cc178` matched the current diff byte for byte before applying only `~/.config/ki/config.toml`, `~/.claude/communication.md`, `~/.claude/delegation.md` and `~/.codex/AGENTS.md`. All four now match rendered sources exactly. Parsed KI choices changed only the two approved skill names; legacy locals, host-local mapping, active harness bindings and Codex app configuration were preserved.

`ki repair --dry-run` proposed exactly four missing user links, then `ki repair --apply` created `ki-coordination` and `ki-work-design` in both user skill spaces. Supported `ki skill remove` removed the retired `ki-pmo` and `ki-pmo-design` links; `ki-checkpoint` was absent. KI doctor now has 17 passing checks and no warnings or failures. KI diag has no errors and one retained warning: legacy config locals are ignored in favour of host-local state. Both-host migration proof and separately reviewed source removal remain necessary.

One native drift entry remains: app-owned `~/.codex/config.toml`. Its fragment proposes a missing project-trust grant for `ki-design`; the live choice remains byte-identical and was excluded. Review that trust choice separately, preserving app state. No host bootstrap, harness switch, checkout move, job activation, service change or broader Rig/source rollout occurred. Sol protected-byte failure evidence and absent Terra proof remain open; do not claim migration complete.

Chezmoi verification passed: focused KI-config tests (3), full Node suite (268 passed, 2 skipped), Markdown check and repository audit (zero failures, seven retained warnings). Audit warnings concern authoring configuration, ADR amendment heading, absent hook and four legacy classification fields; they are outside this file/link repair. The run report is written only to the launcher-owned state destination for homing after completion. Keep all other open queries and holds below; do not mark, accept or prune.

## Messages

- RIG-LIVE (from ki.ways-of-working, 19 October): Kris chose to hold KI-TOOL-RIG-CORE-042 and -047 until this work delivers KB-DOTFILES-UE-091 without linking ChatGPT (its catalogue entry `chatgpt-current` belongs to no profile, so linking it drops ChatGPT off both Docks), and adds a firewall declaration that adopts Terra's unreceipted Rig anchor and covers Sol. Kris then applies both attended. Evidence: ~/.local/state/ki/agents/ways-of-working/rig-live.report.md.
- 2026-10-18 · PRINCIPAL-CI-RED · KI > Model > Ways of working: Kris answered "do all the recommended items"; ki-principal CI fails COORD-7 on your `burn-a`, `burn-b`, `burn-order`, `coord-style`, `src-trio` and `ue086-a` reports. Link each bare identifier to its local file, repoint KI-HARNESS-GOV-186 to [its pruned copy](https://github.com/knowledgeislands/ki-agentic-harness/blob/dd5761c6/docs/roadmap/KI-HARNESS-GOV-186-thread-banner-and-prefilled-reply.md), or prune answered reports at your mark.
- 2026-10-18 · AUDIT-TIDY · KI > Model > Ways of working: Kris answered PRINCIPAL-AUDIT-RED a), "do what you need to do to get that working". At your next mark, delete each answered, homed report the audit's COORD-9 lists (14, from apply-groups to vault-left) and link the record identifiers COORD-7 flags in burn-a, burn-b, burn-order, coord-style, src-trio and ue086-a; detail in the [principal-audit report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/principal-audit.report.md).
- 2026-10-18 18:00 BST · THREADS-PATH from KI > Model > Ways of working: your Sol run wrote `+/_THREADS/chezmoi/host-locals-sol.report.md` at 09:19 BST, a retired path. The ways-of-working run threads-fix moves it into this folder; write run reports only under `+/_WORK/ki.chezmoi/`. MGIT-CONFIG: mgit is gaining learnt templates in `~/.config/mgit/`; when the ways-of-working run mgit-learn says they have landed, bring that directory into the chezmoi source for Kris's `chezmoi diff` review.
- 2026-10-18 18:19 BST · MGIT-CONFIG from KI > Model > Ways of working, run mgit-learn: the templates have landed. On this Mac `~/.config/mgit/templates/` holds four learnt templates (`status_-sb`, `status`, `status_--short_--branch`, `branch`), written by `mgit learn` from read-only runs; `mgit learn --list` shows them. Bring the directory into the chezmoi source for Kris's `chezmoi diff` review, without applying it; Terra and Sol get them on a later reviewed apply. In the same review, regenerate `dot_zsh/completions/_mgit` from `mgit completion zsh`: `-G/--git` is gone, `-B/--bypass` is the Git bypass, and `learn` and `--learn` are new (tools-mgit 73f1f5f).
- FIRST-STEP - from ki.ways-of-working, 18 October (USER-SKILL-LINKS a): `ki-pmo` is now `ki-coordination` and `ki-pmo-design` is `ki-work-design`, no alias (KI-HARNESS-GOV-217). Rename both in the chezmoi source of `~/.config/ki/config.toml`, `tests/ki-config-skills.test.mjs`, `dot_claude/private_communication.md`, `dot_claude/private_delegation.md.tmpl` and `dot_codex/private_AGENTS.md.tmpl`; show Kris the `chezmoi diff` and apply only on his approval; then run `ki repair` to relink `~/.claude/skills/` and `~/.agents/skills/`. Also carry the Terra and Sol KI-TOOL-KI-CLI-143 migration handoff.
- MIGRATED - this file was `+/_CHECKPOINTS/rig.chezmoi.md` until the work migration of 2026-10-18. At your next mark, cut it to next steps, Messages and the tags of parked queries, each linked to its report; move anything else to its durable home, then remove this line.
- RENAME-CHECKPOINT - from ki.ways-of-working, 18 October: `ki-checkpoint` is now `ki-work-folder`, no alias (KI-HARNESS-GOV-217). Fold it into the FIRST-STEP rename: the `~/.claude/skills/ki-checkpoint` link and any `ki-checkpoint` entry in the `~/.config/ki/config.toml` source, in the same reviewed `chezmoi diff`. After v0.11.2 lands, re-run the Sol migration and do a verified Terra run against the checks KI-TOOL-KI-CLI-143 now lists under "Follow-up fix: config.toml kept byte-identical".
- 2026-10-18 19:30 BST · PIN-DONE-LINKS · KI > Model > Ways of working: Kris answered PRUNE-HELD a) on 18 October; these Done records are held only by local links, so at your next mark pin each link to the GitHub copy (`https://github.com/<owner>/<repo>/blob/<revision>/<path>`) at the revision named, or delete the report if it is spent: in `publish-first-step.report.md` and `resume-first-step.report.md`, [KI-TOOL-KI-CLI-143 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/a22214ee581b73a1f395da88f9a118ad89814bb9/docs/roadmap/KI-TOOL-KI-CLI-143-separate-local-harness-paths.md) at `47bb069f`.
- 2026-10-18 19:31 BST · USER-SKILL-STALE · KI > Model > Ways of working: Kris answered USER-SKILL-STALE a) on 18 October ([decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md)). `ki repair` fails because the live `~/.config/ki/config.toml` still lists `ki-pmo` and `ki-pmo-design`. Check that the `ki` user configuration carries `ki-coordination` and `ki-work-design` in `chezmoi diff`, and include it in Kris's next reviewed apply.
- 2026-10-18 19:39 BST · MGIT-ZSH-COMPLETION · KI > Model > Ways of working, run mgit-filter: Kris answered CLI-F-FILTER c) on 18 October ([decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md), "owner answer, CLI-F-FILTER; mark"): mgit's `--filter` has no short letter and `-f` is now a usage error (tools-mgit `781973e`). Regenerate the Zsh completion snapshot `dot_zsh/completions/_mgit` in the chezmoi source from `mgit completion zsh` and hold it for Kris's `chezmoi diff` review. The snapshot predates several mgit changes, so the diff is wider than the dropped `-f[...]` line: it also adds `overview`, `learn`, `-B/--bypass`, `--learn`, `-j/--jobs` and other options, and rewords `-P` and `-L`.

## Parked

- **FIRST-STEP-GATES:** Resolved for this owned scope: prerequisites committed and published, source gates pass, four-target apply and user-link repair verified. Historical failure reports remain evidence, not current blockers.

- **IWORK:** Keynote, Numbers and Pages remain catalogue-only in the approved burn-down report. The later native MAS fix does not by itself answer this completion choice. Recommendation: Keep Keynote, Numbers and Pages catalogue-only and complete the A8 source step, retaining owner review and acceptance. See [Finish the iWork source step](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-086-finish-software-alignment.md>). Options remain in the [parked query](wrap-ways-20261018.report.md).

- **STYLE-LINK:** The output-style link depends on the harness checkout. A read-only warning and an apply-time pull were offered; neither choice is approved. Recommendation: Add a read-only dead-link check after apply, with no harness pull during apply. See [Warn about a missing output style](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md>). Options remain in the [parked query](wrap-ways-20261018.report.md).

- **DIR-PRUNE:** The current merge unions additionalDirectories. Removal needs a declared ownership model so hand-added paths survive. Recommendation: Record the previously managed additionalDirectories set in a state file and prune only entries that left that declaration. See [Remove retired managed directory entries](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md>). Options remain in the [parked query](wrap-ways-20261018.report.md).

- **REST-HOLD:** Dock work still waits on the Rig profile-filter implementation: its record remains ready, not delivered. The latest release is still v0.6.3. The remaining bring-up gaps also depend on the Headroom profile work or fresh planning. Recommendation: Hold the Dock work and remaining bring-up work until CORE-042 is released and the Headroom profile work is delivered. See [Keep the remaining bring-up work parked](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-091-shared-dock-tool-links.md>). Options remain in the [parked query](wrap-ways-20261018.report.md).

- **HOST-LOCALS-BYTES:** Reviewed source apply and declared skill-link repair are complete. Sol migration protected-byte failure and absent Terra verification remain open; no bootstrap or active-harness toggling was performed. Preserve both locals tables until both hosts pass and source removal receives separate review. See [Sol evidence](host-locals-sol.report.md).

Held: both-Mac rig apply until Kris lifts it; privacy and rationale audits until owner resumes; WhatsApp refresh and vega rendering remain parked. Non-blocking Rig-vault and macOS-settings proposals remain with their receiving threads.
