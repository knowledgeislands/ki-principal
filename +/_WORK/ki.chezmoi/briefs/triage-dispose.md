# triage-dispose

Work: ki.chezmoi (KI > Rig > chezmoi). Repository: /Users/krisbrown/.local/share/chezmoi, on Sol.

Authority: TRIAGE-LANE a), Kris on 20 October, 00:16 BST: "go ahead" ([triage-lane](/Users/krisbrown/.local/state/ki/agents/chezmoi/triage-lane.report.md), [triage-review](/Users/krisbrown/.local/state/ki/agents/chezmoi/triage-review.report.md)).

Task, records only:

1. KB-DOTFILES-UE-099: record the triage disposition. It stays at triage until a released Rig supports service and job subject links (KI-TOOL-RIG-CORE-065), and its Paperclip launch-path repair comes forward within this record only if Paperclip is re-enabled before then. Note the review's caution: the path fix must keep listener ownership detection (no bare mise shim).
2. KB-DOTFILES-UE-100: adopt into Now under `ki-next` and plan, under `ki-plan`, a bounded diagnostic stage: read-only on Sol, attended on Terra, recording installed and running versions, key and process growth over a fixed window, caller identities, idle and active-call state, one consistent memory metric, and Terra's exit evidence, with no new server launches and no secret-bearing output. Any mitigation is a separate, reviewed decision with a tested restore path; note the review's candidates (caller-key stabilisation, mcporter 0.15.0's `idleTimeoutMs` idle retirement) and that Sol may proceed without waiting for Terra. Mark it Ready only if the readiness checks pass. Do not run the diagnostics.
3. Gate: `ki repo audit --repo .`, `node --test tests/*.test.mjs`, `rumdl check .`. The permitted baseline is the 22 warnings in `~/.local/state/ki/agents/chezmoi/ready-rest-3.baseline.json` that remain, plus `CLAUDEBIND-1` for KB-DOTFILES-UE-098's pending apply; stop on anything else. CAPTURE-GATE holds: no new records. Commit by explicit path.

Constraints: no apply, restart, push or fetch; do not stage `bin/chezmoi/json`; never run `ki repo conform` without `--dry-run`; leave no `.git/*.lock`.

Report: the run report form, heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › triage-dispose`.
