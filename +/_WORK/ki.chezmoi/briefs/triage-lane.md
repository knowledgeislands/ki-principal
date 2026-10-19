# triage-lane

Work: ki.chezmoi (KI > Rig > chezmoi). Repository: /Users/krisbrown/.local/share/chezmoi, on Sol.

Authority: TRIAGE-ALL, Kris on 19 October via State of play: "I need them all triaging ... anything which is High confidence recommended. Let's move it into now and get it done." Triage every unadopted triage record in this lane under `ki-next`: KB-DOTFILES-UE-098 (workspaces git-audit roots), KB-DOTFILES-UE-099 (subject links, service paths) and KB-DOTFILES-UE-100 (mcporter daemon child leak).

Task:

1. For each, give a recommended disposition and its confidence (high, medium or low), with the reason.
2. Adopt every high-confidence adoption straight into Now and deliver it through `ki-plan` and `ki-implement` to Awaiting review, one record at a time, committing by explicit path.
3. Do not act on medium or low recommendations, or on any cancellation, merge or deletion: list them as queries for one lane query, each with options and a recommendation.
4. CAPTURE-GATE holds: create no new records.
5. Run the gate before each commit: `ki repo audit --repo .`, `node --test tests/*.test.mjs`, `rumdl check .`. The 23 existing warnings recorded in `~/.local/state/ki/agents/chezmoi/ready-rest-2.baseline.json` plus `.rumdl.toml` drift, the ADR-KB-DOTFILES-003 amendment heading and the absent `.githooks/pre-commit` are a permitted baseline; stop on anything new.

Constraints:

- `bin/chezmoi/json` carries a change that is not yours: leave it alone and do not stage it.
- No `chezmoi apply`, `rig apply`, push or fetch. Anything that needs a live apply, a restart or a change on Terra stops at Awaiting review with the attended steps written out. Never run `ki repo conform` without `--dry-run`. Write any `launchctl` label literally; never `bootout` with a computed or empty label.
- Leave no `.git/*.lock` and no temporary files.

Report: the run report form, heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › triage-lane`, every record linked by its full identifier.
