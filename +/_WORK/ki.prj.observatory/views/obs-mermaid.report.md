# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-mermaid

**🤖 → 👤 Handoff to supervisor · Run report at 20:23 BST · last mark 20:20 BST**

---

## Done

- I lifted the Mermaid hold. The exact pin in `apps/site/package.json` was the only place it was held. I found no Renovate, syncpack or other update-tool pin, and Mermaid and the lockfile now resolve to 12.2.0.
- I updated `THIRD-PARTY-NOTICES.md` by hand to Mermaid 12.2.0, because the repository has no notices generator. The bump's only transitive change is that the bundled KaTeX moves from 0.16.47 to 0.18.11, and it is still MIT. KaTeX's command-line dependency, commander, drops out of the lockfile, but it was never bundled or listed. The licence table and redistribution notes needed no change.
- Gate: Biome passed, rumdl passed, syncpack format passed, knip passed, typecheck passed, `bun run test` passed (the third-party notices test in `apps/site/src/mermaid.test.ts` passed 10 of 10), and the build passed. The browser smoke check was skipped because Chromium is not installed for Playwright on this machine. Nothing the bump broke needed a fix.
- Commit `58efa99` `chore(deps): lift the Mermaid hold to 12.2.0` stages only those three paths. It was the only commit stacked on origin, so I pushed it fast-forward to `origin/main`, and the checkout is level with origin.

## In Progress

- The Observatory service restart is still to be done. The running service still serves Mermaid 12.1.0 until you restart it in an interactive session: `launchctl kickstart -k "gui/$(id -u)/uk.me.kris.rig.observatory"`, then check that `http://127.0.0.1:1675/` answers.

## Queries

None.
