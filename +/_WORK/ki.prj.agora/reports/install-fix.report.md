# KI > Techne > Agora › install-fix

**🤖 → 👤 Handoff to supervisor · Run report at 04:24 GMT · last mark 00:04 GMT**

---

## Done

- `bun run self:install` now always packages Agora from the current source before installing, then checks the built app is no older than any file it is built from, and refuses with a message naming both if it is. That closes the stale `dist/` snag from sol (MSG-56069c04).
- After quitting and replacing the running copy, it starts the new one under its launch agent if one is registered, and opens the app if no process appears within 20 seconds. It always opened by `open` as the fallback; before, a `launchctl kickstart` that started nothing went unnoticed. It then waits for the process and for the local view on 127.0.0.1 to answer, and says in one line whether it started, such as "Agora started by open (pid 4242); its local view answers on 127.0.0.1:1677." If nothing starts, it says what to do and exits non-zero.
- The decisions are in a new pure module, `src/install.ts`, added to the pure core the boundary rules enforce, with tests in `src/install.test.ts`. The shell installer `tooling/install-app.sh` is replaced by `tooling/install/install.ts`. The README's install section, its scripts table and the changelog are updated, and the install command no longer needs a separate `self:package`.
- Commit `ddac28c` fix(install): package from source first and confirm the new app started.
- Checks: `self:check` passed; `test` passed (291 tests, the new suite included); knip clean. A dry freshness probe against this Mac's `dist/` correctly called it stale. I did not run the install or touch `~/Applications/Agora.app`.

Choices I made:

- I chose to always package rather than only refuse, with the freshness check as a backstop for a failed or skipped build.
- "Fresh" means the built app's `app.asar` is no older than the newest source file. Source files are `src/` without suites, `assets/tray/`, `assets/app/`, `packaging/`, `package.json`, `bun.lock` and `electron-builder.json`.
- A process that starts but whose local view stays silent counts as started, with a warning in the line. The view check is skipped when the configuration turns it off.

## In Progress

- The new installer's real run is untested until a household installs. On sol, the next `bun run self:install` should end with the one start-up line. If it says it started "by open", the launch agent registered by the old build started nothing, which matches the snag.

## Queries

None.

## New and noteworthy

- One command, `bun run self:install`, now builds and installs Agora from what is in the checkout, so a stale build can no longer slip in.
- The install ends by telling you, in one line, whether the new Agora is running and its local view is answering, instead of leaving you to check and open it by hand.

🧵 ki.prj.agora
