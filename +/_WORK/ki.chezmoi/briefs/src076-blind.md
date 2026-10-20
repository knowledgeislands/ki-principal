# src076-blind

Work: ki.chezmoi (KI > Rig > chezmoi). Repository: /Users/krisbrown/.local/share/chezmoi, on Sol. Read-only blind review of three queries.

Read docs/roadmap/KB-DOTFILES-UE-076-always-run-latest-source.md (grounded in commit 1999865), bin/scheduled/executable_rig-update and the prompt's drift indicator. Agent sessions work in this same checkout; pulling never authorises `chezmoi apply`, which stays behind Kris's reviewed `chezmoi diff`.

SOURCE-CHECK-HOME. Query: where should the source freshness check live? Options: a) a step at the start of the daily `rig-update` job that fetches, reports the source's state and saves it to a file the prompt reads; b) a separate source-refresh scheduled job, perhaps hourly; c) a shell or `ki` status notice only; d) a wrapper used instead of `chezmoi apply`.

SOURCE-REFRESH. Query: should the unattended check fast-forward the source, or only fetch and report? Options: a) fast-forward only when the source is clean and strictly behind, skipping and reporting on any uncommitted change, rebase, merge or Git lock; b) fetch and report behind and ahead counts only, keeping every pull attended; c) `chezmoi update`.

SOURCE-REFUSAL. Query: when the source cannot be fast-forwarded or checked (uncommitted changes, unpushed commits, divergence, rebase or merge in progress, no network), what should `rig-update` do? Options: a) upgrade anyway and report `findings` with the reason, never `ok`, offline as `unknown`; b) skip the upgrade and report `findings`; c) report `failed`.

For each query pick one option and give your confidence (high, medium or low) with a one-line reason. Read-only: edit nothing, commit nothing, no fetch, no network, run nothing that changes state.

Report: heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › src076-blind`, Done, In Progress and Queries.
