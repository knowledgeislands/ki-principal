# ue090-await

Work: ki.chezmoi (KI > Rig > chezmoi). Repository: /Users/krisbrown/.local/share/chezmoi, on Sol.

Authority: OVERNIGHT, Kris on 20 October at 00:30 BST; REREVIEW-SCOPE a); KB-DOTFILES-UE-090 round 3 passed its focused re-review ([r3-review4](/Users/krisbrown/.local/state/ki/agents/chezmoi/r3-review4.report.md), GATE: pass).

Task: move [KB-DOTFILES-UE-090](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md) to Awaiting review under the ki-work record rules (run `ki repo roadmap list` and read the record's status vocabulary first; use the governed status value and any horizon the audit requires). Record in Current state that rounds 1 to 3 passed review (r1-review2, r2-review, r3-review4) and that only the attended Verify checkpoints on terra and sol stay open, each under its own pull, target-review and apply approval; machine readiness remains unverified. Tick nothing that needs a live run. Change only the record.

Constraints: no `chezmoi apply`, restart, kill, `launchctl` change, push or fetch; never write `launchctl bootout` with an empty label; do not stage `bin/chezmoi/json`; never run `ki repo conform` without `--dry-run`; CAPTURE-GATE: no new records; commit by explicit path, retrying on `index.lock`; leave no `.git/*.lock`. Gate: `ki repo audit --repo .`, `node --test tests/*.test.mjs`, `rumdl check .`; the permitted baseline is the 22 warnings in `~/.local/state/ki/agents/chezmoi/ready-rest-3.baseline.json` plus `CLAUDEBIND-1`.

Report: the run report form, heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › ue090-await`, every record linked by its full identifier, each query with options, a recommendation and its confidence.
