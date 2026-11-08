# KI > Techne > Agora › path-fix

**🤖 → 👤 Handoff to supervisor · Run report at 20:25 GMT · last mark 00:04 GMT**

---

## New and noteworthy

The app and the Portal now give every tool they run a full PATH, so `ki` no longer fails with "bun: not found" when Agora is started from Finder, the menu bar or a login item. I tested this from a bare PATH: `ki territory list` gave all 8 territories, both through the login shell and through the fallback list. The installed app picks up the fix only once it is rebuilt and installed again. This run did neither.

## Done

- `9587ac2` fix(env): adds one new module, `src/tool-env.ts`, that builds the environment for every tool Agora runs. PATH starts with the folders of the tools Agora found, including Bun's. Next comes the login shell's PATH, read once with a 5-second timeout. Then mise's shims, `~/.local/bin`, `~/.bun/bin`, `/opt/homebrew/bin` and `/usr/local/bin`, and last the PATH Agora inherited. Every place Agora runs a tool now uses it: `ki`, `git`, `orca`, `tailscale`, `cswap`, `codex-multi-auth`, `rig`, and Bun when the Portal opens the app. `findBun` now also looks in mise, both the newest installed version and the shim.
- When a source still fails, the app now names the command and the first line of its error output. This shows in four places: the status button in the toolbar ("ki territory list failed", with the full reason on hover), the Home summary line, a banner on the map, and the Roadmap page's notices. The Accounts and Jobs notices now give that error line too, instead of "did not answer".
- Tests: new tests for the environment builder (PATH order, the fallback, reading the login shell's output, finding Bun under mise, the first error line). A new test checks that `kiText` runs `ki` with the built PATH and reports its first error line. Tests never run the person's own shell.
- Checks: `bun run self:check` and `bun run test` pass on a clean copy of `origin/main` with only this change (434 tests). In the shared checkout, `self:check` fails only on another run's unfinished `app.css`. The commit is pushed.
- Another run had unfinished edits in the same checkout, including `src/app/renderer/index.ts`. I committed only my own three changes to that file and left their work untouched in the checkout.

## In Progress

Nothing.

## Queries

None.

🧵 ki.prj.agora
