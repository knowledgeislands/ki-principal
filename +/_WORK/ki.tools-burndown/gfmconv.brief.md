# gfmconv - build the GitHub-flavoured Markdown converter in tools-ki

Work: ki.tools-burndown (/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown). Authority: Kris approved at 22:00 BST, 19 October (GFM-ORDER a, GFM-LINK-FORM a), routed by ki.ways-of-working; GFM-CONVERTER in /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/decisions.md. In /Users/krisbrown/workspaces/knowledge-islands/tools-ki, under ki-work-roadmap and ki-self:

1. Capture a record for the converter from the Converter requirements in /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/gfm-migration.md, noting it blocks KI-PRINCIPAL-OPS-014 in ki-principal (in prose, cross-repository). Choose its host (`ki repo conform --skill ki-authoring` or its own `ki` command) in planning and record the reason.
2. Plan and implement it to every requirement listed there, with fixture tests on ki-principal shapes; run against ki-principal only with `--dry-run` and never write to ki-principal.
3. Run the full gate (coverage suite, TypeScript, Biome, lint, command inventory, `ki repo audit`) and move the record to Awaiting review. Commit by explicit path, locally only. Do not tag or release. Report the record, the dry-run summary for ki-principal, the gate result and any query as your footer says.
