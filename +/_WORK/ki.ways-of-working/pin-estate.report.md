# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › pin-estate

**🤖 → 👤 Handoff to supervisor · Run report at 20:55 BST · last mark 20:20 BST**

---

## Done

- KI-PIN-ESTATE: every pin below v0.11.3 moved to v0.11.3 in 18 repositories, one `chore(ci): move KI_VERSION pin to v0.11.3` commit each, through each repository's hooks, pushed fast-forward. Each CI run watched with `gh run watch`: 13 green, 5 red. All 5 were red on the run before the move, with the same failures, so the pin added no new findings and nothing needed a mechanical fix.
- Four repositories (homebrew-tap, ki-specifications, tools-mgit and tools-rig) took the subject `ci: ...` before commitlint's type list rejected it elsewhere. Those four commits are pushed as they stand.
- No pins were found in kw-website or paperclip. apps-knowledgeislands.info and ki-design were left out, as the brief required. ki-principal was already at v0.11.3 and was not touched.
- The apps-observatory.local tree holds 23 dirty files from another session. Only `ci.yml` was staged. `pull --rebase` refused because of those files, but origin had not moved, so the push was still fast-forward.
- Net record count: 0 in every repository. No other session's commits were pushed with mine.

| Repository | Old pin | Commit | Result |
| --- | --- | --- | --- |
| apps-observatory.local | v0.8.4 | 93df0cd | red, same as before: ITEM-1 title too long on [KI-OBSERVA-VIS-022 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/c1f008346dc085a0c25026ea5c9a08b383ef1d5b/docs/roadmap/KI-OBSERVA-VIS-022-judge-overdue-against-each-job-schedule.md) |
| homebrew-tap | v0.8.4 | 8fafaa5 | green |
| ki-agentic-harness | v0.10.4 (`.github/ki-version`) | 8f10f40c | red, same as before: 4 KI-LINK-2 broken links to the pruned [KI-HARNESS-GOV-210 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/218b8e3df7c67412382c34960cf4edfc3c7a9152/docs/roadmap/KI-HARNESS-GOV-210-work-model-write-in.md) in ki-coordination, ki-work, ki-work-roadmap and ki-work-folder references, the last one an absolute `/Users/...` path |
| ki-specifications | v0.8.4 | 37937fa | green |
| ki-techne-harness | v0.8.4 | b6c1173 | red, same as before: `techne-controller` typecheck fails |
| mcp-acquire-whatsapp | v0.8.4 | 2926b9f | green |
| mcp-git-audit | v0.8.4 | aef369b | green |
| mcp-gsuite | v0.8.4 | fb6c043 | green |
| mcp-housekeeping-chatgpt | v0.8.4 | de30242 | green |
| mcp-housekeeping-claude | v0.8.4 | 0133e7a | green |
| mcp-ki-kb-fs | v0.8.4 | 6a79b7b | green |
| mcp-ki-kb-notion-mirror | v0.8.4 | e76c3c6 | green |
| mcp-m365 | v0.8.4 | 6f39946 | red, same as before: ITEM-5 on [KI-MCP-M365-TOOL-012](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/roadmap/KI-MCP-M365-TOOL-012-judged-mail-recheck.md), whose dependency [KI-MCP-M365-TOOL-010 (pruned)](https://github.com/knowledgeislands/mcp-m365/blob/8791e726582ac5ae0d276e868b4f77fea2772522/docs/roadmap/KI-MCP-M365-TOOL-010-category-aware-rules.md) has been pruned |
| tools-git-almanac | v0.8.4 | f210fe8 | green |
| tools-ki | v0.8.4 | b263ca45 | green |
| tools-mgit | v0.8.4 | 2400d96 | red, same as before: shellcheck SC2015 at `bin/mgit` lines 3182 and 3208 (not linked to the pin) |
| tools-rig | v0.11.2 | 424727c | green |
| tools-techne | v0.8.4 | 40ba334 | green |

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The four ki-agentic-harness links to the pruned [KI-HARNESS-GOV-210 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/218b8e3df7c67412382c34960cf4edfc3c7a9152/docs/roadmap/KI-HARNESS-GOV-210-work-model-write-in.md) come under PRUNE-FOLLOW-UP's link-pinning run.
- The other red repositories have failures that existed before this run, and each belongs to its own repository's owner. Each repository can pick these up in its next session:
  - the overlong apps-observatory.local title
  - the dangling dependency in mcp-m365
  - the shellcheck findings in tools-mgit
  - the ki-techne-harness typecheck, which falls under the Techne Programme Hold for anything beyond local work

## Queries

No outstanding queries

### 🤖 → 👤 Handoff to supervisor · since 20:55 BST

👤 0 with you · ⛔ 0 blocked

- [committed] 18 pin commits, pushed
- [unpushed] none
