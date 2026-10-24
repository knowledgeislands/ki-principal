# chezmoi › codex-drift

**🤖 → 👤 Handoff to supervisor · Run report at 20:21 BST**

---

## Done

- Cause: not a runtime write. The only difference was a stale target — the `apps-trip.midnight.ninja` Codex trusted-folder project that commit `7dccce4` added to the source after orca-coexist's apply. Orca's and the managed `hooks.state` entries (11) were untouched by the diff and remain after apply.
- Change: scoped `chezmoi apply ~/.codex/config.toml` only; outcome: `chezmoi status` no longer lists `.codex/config.toml`, and the target differs from before only by the one project block. Undo: remove the `[projects."…/apps-trip.midnight.ninja"]` block (the next apply would restore it).
- No source change, so no commit, gate run or push was needed. The held Rig files were not touched.

## In Progress

Nothing.

## Queries

None.
