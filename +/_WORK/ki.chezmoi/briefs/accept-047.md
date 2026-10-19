# accept-047

Work: ki.chezmoi (KI > Rig > chezmoi). Repository: /Users/krisbrown/workspaces/knowledge-islands/tools-rig.

Authority: Kris approved accepting KI-TOOL-RIG-CORE-047 (relayed by State of play, 19 October 23:19 BST: "Kris approved accepting KI-TOOL-RIG-CORE-047; accept it under ki-accept when your change lands"). The change has landed: Sol's apply evidence is in tools-rig `2ab9354`, and the follow-up KI-TOOL-RIG-CORE-068 (`6c06d8c`, `abb734b`) is linked from it.

Task: accept KI-TOOL-RIG-CORE-047 under the `ki-accept` skill. Read the record first. If the record still names an unmet acceptance criterion (for example the S3 gate correction it lists as a follow-up), do not accept: stop and report it as a query with options and a recommendation. Otherwise accept it, run the repository's local gate, and commit by explicit path.

Constraints:

- Do not push. Do not apply chezmoi or Rig. Do not touch other records.
- Never run `ki repo conform` without `--dry-run` (HOOK-GUARD, important: the source-linked `ki` would convert Husky to `.githooks`).
- Never use `--no-verify` or force-push. Leave no `.git/*.lock` files.
- Another session may be working in tools-rig: check `git status --short` first and commit only your own paths.

Report: the owner-report run report form, heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › accept-047`.
