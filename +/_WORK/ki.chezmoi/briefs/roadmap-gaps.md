# roadmap-gaps

Work: ki.chezmoi (KI > Rig > chezmoi). Repository: /Users/krisbrown/.local/share/chezmoi, on Sol.

Authority: OVERNIGHT, Kris on 20 October at 00:30 BST; recommended by the read-only survey [next-scan](/Users/krisbrown/.local/state/ki/agents/chezmoi/next-scan.report.md) - read it first.

Task: fix the mechanical roadmap gaps only. On KB-DOTFILES-UE-027, -082, -086 and -087, replace `initiative: knowledge-islands/rig` with `theme: rig`, matching the form sibling records use. Set `size` on 082 (s), 088 (m), 092 (s), 093 (s), 084 (s), 097 (s), 086 (l) and 035 (m), checking each against the record's own scope first and leaving any where the size is not plain. Leave 076, 077, 087, 027, 071, 094 and 089 unsized. Change no status, horizon or body. Rerun `ki repo roadmap list` and report the gap count before and after. One local `docs(roadmap)` commit.

Constraints: no `chezmoi apply`, restart, kill, `launchctl` change, push or fetch; never write `launchctl bootout` with an empty label; do not stage `bin/chezmoi/json`; never run `ki repo conform` without `--dry-run`; CAPTURE-GATE: no new records; commit by explicit path, retrying on `index.lock`; leave no `.git/*.lock`. Gate: `ki repo audit --repo .`, `node --test tests/*.test.mjs`, `rumdl check .`; the permitted baseline is the 22 warnings in `~/.local/state/ki/agents/chezmoi/ready-rest-3.baseline.json` plus `CLAUDEBIND-1`.

Report: the run report form, heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › roadmap-gaps`, every record linked by its full identifier, each query with options, a recommendation and its confidence.
