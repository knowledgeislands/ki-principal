# Brief: query-review

Blind review of three queries for KI > Rig > chezmoi, under the `ki-coordination` Query review rule. For each, check the claims directly in the repositories and files named, then return your own recommended option, a confidence (`high`, `medium` or `low`) and a one-line reason. Read-only: change nothing and commit nothing.

Repositories: chezmoi source `/Users/krisbrown/.local/share/chezmoi`; `/Users/krisbrown/workspaces/knowledge-islands/tools-rig`, `ki-agentic-harness`, `tools-ki`, `ki-principal`.

## RIG-LIVE-DELIVER

**Context:** Kris chose to hold KI-TOOL-RIG-CORE-042 and -047 (tools-rig `docs/roadmap/`) until this work delivers KB-DOTFILES-UE-091 (`docs/roadmap/KB-DOTFILES-UE-091-shared-dock-tool-links.md` in the chezmoi source) without linking ChatGPT (catalogue entry `chatgpt-current` belongs to no profile, so linking it drops ChatGPT off both Docks), and adds a firewall declaration that adopts Terra's unreceipted Rig anchor and covers Sol; Kris then applies both attended. An earlier parked query, REST-HOLD, held the Dock work until CORE-042 was released. Evidence: `/Users/krisbrown/.local/state/ki/agents/ways-of-working/rig-live.report.md`.

**Query:** Plan and deliver UE-091 source-side now, with the firewall declaration, and no apply?

**Options:** a) Launch a plan-then-implement run for UE-091 and the firewall declaration, source only, `rig doctor` before and after, then show the diff for an attended apply. b) Keep the Dock work held until CORE-042 is released.

## TRIAGE-CUT

**Context:** The chezmoi source roadmap has 20 open records; 3 are triage: KB-DOTFILES-UE-095 (guide continuity check), KB-DOTFILES-UE-096 (thread identity hook registration, waiting on KI-HARNESS-GOV-199 Phase 3 in ki-agentic-harness and KI-TOOL-KI-CLI-145 in tools-ki), KB-DOTFILES-UE-098 (workspaces git-audit roots). Kris asked for at least half of triage records to be cancelled or merged, each with a reason, confirmed by Kris. Cancelling is destructive.

**Query:** Which cuts go ahead?

**Options:** a) Merge UE-095 into KB-DOTFILES-UE-090 (close Rig bring-up gaps) and cancel UE-096 until GOV-199 Phase 3 lands; keep UE-098. b) Merge UE-095 only and move UE-096 to Hold. c) Cut neither.

## CARRY-DIRECTIONS

**Context:** Kris authorised these between 15 and 17 October and none is delivered: SEAT-BIND and SEAT-HOSTS as SEAT-CHANGE amends them (each host's seat role and territories in chezmoi host data); PAPERCLIP-OFF (keep the Paperclip declaration, neither Mac applies or loads it); TOML-OPENER (`.toml` opens in Zed, not Warp); SSH-CONSOLE (physical-console fallback in the macOS workstation guide). Kris's words are in the ki-principal work file at revision 541a5d91, `+/_WORK/ki.chezmoi/work.md` (`git -C ki-principal show 541a5d91:+/_WORK/ki.chezmoi/work.md`). A 19 October run dropped them undelivered.

**Query:** How should these four be delivered?

**Options:** a) One source-only run after RIG-LIVE-DELIVER, `rig doctor` before and after, no apply. b) Put each back to Kris before any run.

## Report

Owner report with heading `# KI > Rig > chezmoi › query-review` and, under `## Done`, one line per query: `<TAG>: <option>) confidence <level> - <reason>`, plus any claim in a Context you found false.
