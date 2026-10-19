# Options for blind review

## ESTATE-PUSH - Push the converted repositories

Context: Kris ordered Husky removed across all `.ki.toml` repositories tonight ("make it happen"). Two runs convert about 50 repositories, committing locally. The standing rule is that runs commit and Kris pushes; Kris has not said "push". A local-only conversion leaves Kris's other machines on Husky until pushed. Some repositories may carry other sessions' unpushed commits.

Query: Should the migration runs push each repository after its conversion is verified?

a) Each run pushes fast-forward only after the verified commit, and never pushes a repository carrying another session's unpushed commits, listing those instead. b) Commits stay local; Kris pushes with `mgit` when ready.

## MGIT-030-NEXT - Promote the mgit sync summary record

Context: KI-TOOL-MGIT-CLI-030 (tools-mgit `docs/roadmap/KI-TOOL-MGIT-CLI-030-sync-closing-summary.md`) is now high priority at Soon with nine open output-design choices in a Shaping section, so full Next plan sections cannot honestly be written yet.

Query: Should it move to Next now, settling its design choices at planning?

a) Settle the choices with Kris at planning under `ki-plan`, then promote it to Next. b) Leave it at Soon until the burndown reaches it.
