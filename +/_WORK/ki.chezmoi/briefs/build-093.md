# build-093

Work: ki.chezmoi (KI > Rig > chezmoi). Repository: /Users/krisbrown/.local/share/chezmoi, on Sol.

Authority: OVERNIGHT, Kris on 20 October at 00:30 BST; 093-PREFLIGHT a), reviewed (blind review [pre093-blind](/Users/krisbrown/.local/state/ki/agents/chezmoi/pre093-blind.report.md) agreed).

Task: build the remaining planned step of [KB-DOTFILES-UE-093](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-093-restore-emerge-test-prerequisites.md): a read-only dependency preflight in `tests/scheduled-emerge-session.test.mjs`, so an incomplete checkout fails with a clear setup remedy instead of an opaque error. The preflight only reads; it installs nothing and runs no package manager. Prove it with a test that simulates a missing dependency. Move the record through Ready and In progress to Awaiting review under the ki-work rules, with its Review packet; record that Kris's acceptance is outstanding. Touch only that test, any helper it needs and that record (another run is editing KB-DOTFILES-UE-076; KB-DOTFILES-UE-077 has another session's uncommitted edit). Note: if `ki repo audit` still shows ITEM-3 on KB-DOTFILES-UE-076, that belongs to run fix-076-steps; say so and do not treat it as yours.

Constraints: no `chezmoi apply`, restart, kill, `launchctl` change, push or fetch; never write `launchctl bootout` with an empty label; do not stage `bin/chezmoi/json`; never run `ki repo conform` without `--dry-run`; CAPTURE-GATE: no new records; commit by explicit path, retrying on `index.lock`; leave no `.git/*.lock`. Gate: `ki repo audit --repo .`, `node --test tests/*.test.mjs`, `rumdl check .`; the permitted baseline is the 22 warnings in `~/.local/state/ki/agents/chezmoi/ready-rest-3.baseline.json` plus `CLAUDEBIND-1`.

Report: the run report form, heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › build-093`, every record linked by its full identifier, each query with options, a recommendation and its confidence.
