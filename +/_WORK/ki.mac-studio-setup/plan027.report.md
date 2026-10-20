# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [Mac Studio setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup.md) › plan027

**🤖 → 👤 Handoff to supervisor · Run report at 23:53 BST · last mark 23:36 BST**

---

## Done

- [KI-TOOL-RIG-CLI-027](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CLI-027-command-line-convention-departures.md) adopted to Now and planned to Ready under Kris's RIG-ORDER a) decision of 23:27 BST; its status is now Ready, size m. Nothing was implemented.
- Commit `cc4e993` docs(roadmap): plan KI-TOOL-RIG-CLI-027 to Ready.
- A sandboxed, read-only probe confirmed all four departures: `--format=json`, `--json`, `-n` and `--` are each rejected with exit 2.
- The plan adds one shared argument normaliser, driven by Rig's existing option inventory, so that every command accepts `--opt=value`, `--json`, `-n` for `--dry-run` and `--` as end of options. It adds a new portability requirement, RIG-PORT-014, plus help, completion, manual, guide and changelog updates, and isolated tests.
- Format question settled from the ki-repo-tools command-line conventions, not guessed: `--json` becomes the documented form because Rig offers only one machine format, and `--format text|json` stays accepted as an equivalent, so no shipped flag is removed.
- Roadmap audit: no finding on the record. Markdown lint: clean. Commit is local only in tools-rig on `main`; nothing pushed, applied live or touched elsewhere.

## In Progress

Nothing is running. Pending handoff: tools-rig `main` on sol holds `cc4e993` unpushed, one commit ahead of `origin/main` by the last local view.

## Queries

No outstanding queries
