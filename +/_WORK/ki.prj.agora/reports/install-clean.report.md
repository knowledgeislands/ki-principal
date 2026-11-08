# KI > Techne > Agora › install-clean

**🤖 → 👤 Handoff to supervisor · Run report at 20:09 GMT · last mark 00:04 GMT**

---

## New and noteworthy

`bun run self:install` now removes `dist/` once both apps are installed and the new Portal is running with its local view answering. It prints one line saying so. From the next install, Alfred and Spotlight will list only the apps in `~/Applications`.

## Done

- `feat(install)` a572beb, pushed to `origin/main`:
  - The decision lives in `cleanUp` in `src/install.ts`, with tests; the removal is in `tooling/install/install.ts`.
  - If anything fails after packaging, the installer prints "Left dist/ in place for diagnosis."
  - `dist/` is also kept, with a line saying why, in three cases: the view does not answer, the view is turned off, or a hand-started Agora app (`bun run app:start`) is running from `dist/app/`.
  - The README's install section is updated.
- Nothing else needs `dist/` to survive an install: `self:package`, `self:start`, `app:start` and `build` all rebuild what they need. Where packaging writes is unchanged.
- Checks:
  - On a clean copy of `main` with only this change: `self:check` passed and `bun run test` passed (399 of 399).
  - In the shared checkout, both currently fail. The failures are in other runs' unfinished app work (jobs and roadmap pages, `src/view.ts`, boundaries), not in this change.
- I did not run the install and did not touch this checkout's `dist/`.

## In Progress

Nothing.

## Queries

**Q1 - Local view turned off**

**Context:** The brief asks for the Portal to be "running with its local view answering" before `dist/` goes. When the configuration turns the local view off, there is nothing to ask, so the installer cannot confirm the new Portal works. Right now it keeps `dist/` in that case and says so.

**Query:** Should an install with the local view turned off still keep `dist/`?

**Options:**

a) (recommended, confidence medium - this follows the brief literally, and the local view is on by default) Keep it as now. `dist/` stays only on a Mac where the view is turned off.

b) Treat a running process as enough when the view is off, and remove `dist/` then too.

🧵 ki.prj.agora
