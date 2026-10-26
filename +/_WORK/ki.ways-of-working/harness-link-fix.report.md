# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › harness-link-fix

**🤖 → 👤 Handoff to supervisor · Run report at 18:40 BST**

---

## Done

- Checkout: clean before and after the run, with no other session's uncommitted files; pulled fast-forward to `db30d0ca` with nothing new.
- Link changed: in [standards-work-package.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md) line 324, the [KI-TOOL-KI-CLI-150 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/4f8d97d221f98d896b642160c0561cdfd8c06b84/docs/roadmap/KI-TOOL-KI-CLI-150-work-folder-entry-points.md) citation now points to `https://github.com/knowledgeislands/tools-ki/blob/main/docs/roadmap/KI-TOOL-KI-CLI-150-work-folder-entry-points.md`. The wording is unchanged. No generated surface carries this text, so nothing needed regenerating.
- KI-LINK-2 scope: this was the only absolute local link in skill Markdown outside code. The two other `/Users/...` hits, in `ki-coordination`'s standard (fenced and inline-code examples) and its test fixture, are not checked as links, so I left them alone.
- Checks: `bun run test` passed (1286 pass, 0 fail). `bunx tsc --noEmit` passed. `ki repo audit --skill ki-work-package` passed. `ki repo audit --repo .`, the CI audit command, still fails on one other finding, FILES-10 (below).
- Commit: `ec30caaf fix(ki-work-package): repoint absolute local links`, on its own, pushed fast-forward and now on `origin/main`. The remote accepted it with its usual bypass notice for direct pushes to `main`.
- Records: no records changed in any repository (net 0). Nothing was written in tools-ki or ki-principal.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- My local `ki` is 0.11.4 while the CI pin is v0.11.3. KI-LINK-2 never fails locally, because the `/Users/...` path exists on this laptop, so I confirmed the fix by scanning rather than by a CI run. The `ki` release and pin stay with ki.tools-burndown.

## Queries

### CI-RED-FILES10 - harness CI still red on .ki.toml table order

**Context:** The CI Audit step (`ki repo audit --repo .`) fails on the harness's own `ki-repo` rubric, FILES-10. In [.ki.toml](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/.ki.toml), `[skills.ki-acquire]` was added after `[skills.ki-trades]`, which must be the last table. The addition came in `8bc9d49d feat(acquire): consolidate shared acquisition contract and provider composition`. The rule lives in the harness, not in `ki`, so CI's v0.11.3 pin still applies it and CI stays red after my link fix. The fix is to move `[skills.ki-acquire]` above the Relationships section, a one-table reorder. It was outside this run's link-only scope, so I did not make it.

**Query:** Should a follow-up run move `[skills.ki-acquire]` above `[skills.ki-trades]` so the harness CI goes green?

**Options:**

a) (recommended, confidence high - the audit message names the exact line, and the change is a non-destructive reorder) Launch a short harness run to reorder the table, rerun the audit and tests, and commit and push it as `fix(config): keep ki-trades the last skills table`.

b) Leave it for the owner of the ki-acquire consolidation to fix in their next harness change.
