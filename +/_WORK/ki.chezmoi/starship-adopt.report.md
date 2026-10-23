# starship-adopt

**🤖 → 👤 Handoff to supervisor · Run report at 08:18 BST · last mark 08:18 BST**

---

## Done

Starship is adopted in source on terra. It has four local commits on `main` and has not been pushed, applied or installed:

- `4b1d9e2` docs(roadmap): accepts `KB-DOTFILES-UE-104`, with adoption folded into this series rather than a new record.
- `b3195bc` feat(rig): declares the `starship` formula in the core and public profiles. The purpose worksheet gains its row and corrects counts left stale by the GitUp retirement.
- `d14cf3a` feat(zsh): adds the guarded fragment, the seven variants, `starship-variant` with completion, the ⚙ drift module, the preset refresh script, the generated `_starship` completion and the tests.
- `6243576` docs(starship): adds the guide `docs/guides/tools/starship.md` and its tools-list entry.

The default is `kris`, the plain-text two-line variant you saw in Ghostty. It renders in any font and shows the host, which matters because terra and sol share repositories; `one-line` stays closest to the old prompt.

How you switch variants:

- `starship-variant` with no argument lists the variants and marks the active one.
- `starship-variant <name>` changes this session only.
- `--machine <name>` writes `~/.config/starship/machine-variant`, which chezmoi ignores.
- `--machine --reset` clears that file.

The fragment does nothing without the binary, and in Warp the old prompt stays.

The ⚙ count reads the existing `chezmoi-prompt-status` cache with dash builtins and never runs chezmoi. `KB-DOTFILES-UE-102` still owns what the cache means.

Checks:

- `node --test tests/*.test.mjs`: 342 tests, 340 pass, 0 fail, 2 skipped (both env-gated and already skipped before this work).
- `rumdl check .`: clean.
- `ki repo audit --repo .`: PASS=17 WARN=4 FAIL=0. Of its 5 findings, 4 were already there; the fifth is CLEAN-4, `main` being 4 ahead of origin because nothing was pushed.
- `chezmoi cat ~/.zsh/99_starship` matches the source.
- `zsh -i` in a temp HOME:
  - With Starship: Starship prompt on `kris`.
  - Without Starship: old prompt, and the function is not defined.
  - Under Warp: old prompt.
- Startup costs about 11 ms more over 15 interleaved runs: about 295 ms against about 284 ms.
- Prompt render takes about 28 ms median in `$HOME`, 41 ms in the chezmoi repo and 47 ms in ki-agentic-harness, all with p95 at or under 53 ms. The ⚙ module itself takes 2 ms.
- `rig doctor` before apply: unhealthy, 6 findings, none from this change.
  - `gitup` and `gitup-formula` are missing because the GitUp retirement is not applied yet.
  - Three resources have drifted: `default-application.toml` (Warp, where Zed is expected), `dock.workstation` (order) and `firewall.screen-sharing-tailnet` (anchor changed).
  - One historical apply failure from 2026-10-19.

The scoped `chezmoi diff` shows:

| Target | Change |
| --- | --- |
| `~/.zsh/99_starship` | New, 81 lines |
| `~/.zsh/completions/_starship` | New, 486 lines |
| `~/.config/starship/variants/` | New, 7 files |
| `~/.config/rig/conf.d/16-homebrew.toml` | Adds `[tool.starship]` and removes `[tool.gitup-formula]`, the second from the already-pending GitUp retirement |

The temp area is emptied. The trial kit is untouched.

## In Progress

Nothing.

## Queries

**Needs: STARSHIP-APPLY**

**Context**: Everything is committed and proven without an apply. Applying `16-homebrew.toml` also brings in the pending GitUp retirement from commit `0ec53fa`, which should take two of the doctor's six findings with it.

**Query**: Shall I go ahead with Starship on terra by running these three steps?

1. `brew install starship`
2. `chezmoi apply ~/.zsh/99_starship ~/.zsh/completions/_starship ~/.config/starship ~/.config/rig/conf.d/16-homebrew.toml && rig doctor`
3. Open a new Ghostty window.

If you later want it gone:

- Run `brew uninstall starship`; new shells return to the old prompt.
- For a full removal, also revert `d14cf3a` and `b3195bc`, run `rm -rf ~/.config/starship ~/.zsh/99_starship ~/.zsh/completions/_starship`, then `exec zsh`.

Sol needs these steps after a push:

1. Pull the source.
2. Run `brew install starship`, or `rig apply`.
3. Apply the same four chezmoi targets.
4. Open a new terminal.
5. Optionally, run `starship-variant --machine <name>`.

Once you are happy on terra, remove the trial kit with `sh ~/.local/state/ki/trials/starship/remove.sh`.

**Options**:

a) (recommended, confidence high - tests and the temp-HOME runs pass, and the old prompt stays if Starship is missing) Run the three steps on terra now, then push when convenient so sol can follow.

b) Apply only the Zsh and Starship targets and leave `16-homebrew.toml` for the combined apply already awaiting approval; until that apply, the rendered Rig catalogue on terra does not yet declare the installed formula.

c) Hold; the source stays committed, inert and unpushed.
