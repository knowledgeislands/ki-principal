# chezmoi › ghostty-tabs

**🤖 → 👤 Handoff to supervisor · Run report at 08:45 BST**

---

## Done

- Added `territory-set [code]` to `dot_zsh/60_territory` (commit `557af1d`, local, not pushed). It reuses the current tab as tab 1 (the territory, titled with its code, e.g. `ki`), then opens `~/workspaces` as `ws` and the chezmoi source as `dotfiles`, and returns focus to tab 1. With no code it uses the last one chosen, kept in the unmanaged `~/.local/state/territory/last`, or `ki`. Outside Ghostty it only changes directory. `territory <code>` is unchanged and still opens a single tab.
- Startup: Ghostty has no clean config option for this. `initial-command` replaces the first shell, and `input` types into every new terminal. Instead, a one-shot pre-prompt hook in the same fragment opens the set for the last code. It runs only in a shell that Ghostty started through `login` (checked against Ghostty 1.3.1's real process tree), once per Ghostty launch (recorded in `~/.local/state/territory/ghostty-launch`), and only in a window with no other tab. Restored windows, later tabs, nested shells and SSH sessions are left alone. The Ghostty config is unchanged.
- Six new tests use the AppleScript and `ps` stand-ins. No real tabs were opened. The AppleScript compiles against Ghostty's dictionary. The Ghostty guide (`docs/guides/tools/ghostty.md`) now has a "The standard set" section.
- Gate: `ki repo audit --repo .` passed, `node --test tests/*.test.mjs` passed 353/353, and `rumdl check .` was clean.
- For the terra apply plan, the only changed target is `~/.zsh/60_territory`. The guide and tests are not targets. After the apply, the next Ghostty launch opens the set, and the first use asks for macOS Automation permission if it has not been granted already.

## In Progress

Nothing.

## Queries

None.
