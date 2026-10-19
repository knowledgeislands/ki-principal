# bringup-fold

Work: ki.chezmoi (KI > Rig > chezmoi). Repository: /Users/krisbrown/.local/share/chezmoi, on Sol.

Authority: BRINGUP-CHECK a), taken under Kris's standing authority for high-confidence work after the blind review agreed with high confidence ([ue090-plan](/Users/krisbrown/.local/state/ki/agents/chezmoi/ue090-plan.report.md), [bringup-review](/Users/krisbrown/.local/state/ki/agents/chezmoi/bringup-review.report.md)). This run changes records and nothing else.

Task:

1. In KB-DOTFILES-UE-090, fold the review's safeguards into the plan for gaps 2, 7 and 8: the `rig-bringup-check` wrapper is read-only and only reports; it never installs, signs in, unlocks, builds, prunes or applies; it reports manual, unknown and failed apart; any 1Password probe is attended, optional, bounded and silent on both streams; harness health comes from the native doctors (`ki`, `rig doctor`), not a second implementation; gap 8 checks the effective `claude` in a fresh interactive shell and compares runtimes against declarations rather than "anything but the global pin"; the attended screen checks and the end-to-end trial stay in the guide. Reconcile the record's older text with the guide's existing Stage 3 App Store and pruning steps. Add the review's test list (missing tools, doctor failures, timeouts, manual/unknown states, secret-canary suppression).
2. Hand gap 9 to KB-DOTFILES-UE-076 explicitly: add to UE-076's scope that "source is current" and "pulled changes still need target review" are distinct, that a notice must never render the whole target diff at shell start, and that pulling never authorises applying. Mark gap 9 in UE-090 as handed over, not delivered.
3. Keep both records' lifecycle status as it is; do not mark either Ready.
4. Run the gate: `ki repo audit --repo .`, `node --test tests/*.test.mjs`, `rumdl check .`. Commit by explicit path.

Constraints:

- `bin/chezmoi/json` has a change that is not yours: leave it alone and do not stage it.
- Do not push, apply or fetch. Never run `ki repo conform` without `--dry-run` (HOOK-GUARD). Leave no `.git/*.lock`.

Report: the run report form, heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › bringup-fold`. If UE-090 could then move to Ready apart from held gap 1, raise that as a query with a recommendation.
