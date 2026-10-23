# chezmoi › Starship trial › starship-preview

**🤖 → 👤 Handoff to supervisor · Run report at 08:11 BST**

---

In a new Ghostty window, type:

```zsh
source ~/.local/state/ki/trials/starship/try.zsh
starship-variant --all
```

Add `--status 1 --duration 2300` to see each variant's failure and slow-command styling. `-a` works as a short form of `--all`.

## Done

- `starship-variant --all` (or `-a`) in [`try.zsh`](/Users/krisbrown/.local/state/ki/trials/starship/try.zsh) prints a bold heading for every variant, marks the current one, then shows its real colour rendering for the current directory. The left prompt is followed by the right prompt, right-aligned the same way zsh places it. The rendering uses the last command's real exit status, duration and job count, and `--status N` and `--duration MS` override them. An unknown option prints usage and returns 2. The live prompt is unchanged, because `STARSHIP_CONFIG` is set only for each `starship prompt` call. The plain `starship-variant` list now mentions `--all`.
- Fixed colours in [`kris.toml`](/Users/krisbrown/.local/state/ki/trials/starship/variants/kris.toml) and [`kris-nerd.toml`](/Users/krisbrown/.local/state/ki/trials/starship/variants/kris-nerd.toml). Host, time, duration and continuation were bright-black, dimmed or yellow; they are now italic in the terminal's own foreground colour. The territory is plain foreground instead of bright-black. The path and repo use blue and bold blue instead of cyan. Git status is red instead of yellow. The worktree and ssh markers are bold foreground instead of bold yellow. Bun, node and python are bold foreground instead of their default red, green and yellow. The success `>` is bold foreground instead of bold green. Purple for the branch and red for errors are unchanged. The colour rule is noted in each file's header.
- Undo: the original `try.zsh`, `kris.toml` and `kris-nerd.toml` are in [`backup/`](/Users/krisbrown/.local/state/ki/trials/starship/backup/). Copy them back to undo. `remove.sh` still removes the whole kit, backup included.
- Tested in an interactive zsh on a real pty, 100 columns wide, in `~/.local/share/chezmoi` and `knowledge-islands/ki-agentic-harness`. All 7 variants rendered, the failure styling showed after `false` and with `--status 1 --duration 2300`, and `STARSHIP_CONFIG` was still `kris.toml` afterwards.
- `--all` takes 0.36 to 0.58 seconds for all 7 variants, which is 14 Starship calls.
- Nothing outside the kit was changed: no commits, installs or startup-file edits.

### Contrast findings

These are WCAG contrast ratios. Below 3 is hard to read, and 4.5 is comfortable. Ghostty has no config here: `config.ghostty` is empty, so it uses its defaults. The background is `#282c34`, the palette is Tomorrow Night, `bright-black` is `#666666`, faint text is drawn at 50% opacity, and `minimum-contrast` is 1, which means off. The light themes measured were Builtin Light, GitHub Light Default, Catppuccin Latte and Apple System Colors Light.

- **Unreadable on Ghostty's default dark background:** `bright-black` (2.4), `dimmed` text (about 3.2 for dimmed white), and `black` (1.2). Red is fair at 3.8.
- **Unreadable on light themes:** yellow and bright-yellow (1.8 to 2.3), green (1.9 to 3.2), cyan (2.0 to 3.3) and white (1.9). Purple drops to 2.3 on Catppuccin Latte only.
- **Safe on every theme tested:** the terminal foreground, blue (4.3 or more), red (3.8 or more), and, apart from Latte, purple. The kris fix keeps to these colours.

Unreadable segments in the official presets, left untouched:

- **pure:**
  - On the dark default, the branch, Git state and virtualenv are `bright-black` (2.4).
  - On light themes, the dirty `*` uses colour 218, which is pink (1.5 to 1.7 contrast). The ahead/behind arrows are cyan and the duration is yellow, which are also weak.
- **rainbow (Gruvbox):**
  - The directory segment puts cream text `#fbf1c7` on yellow `#d79921` (2.2). This is probably the "depends on the background" effect you noticed.
  - Other segments with the same cream text are weak too: Git on aqua (2.8), the OS and user segment on orange (3.4), and runtimes on blue (3.7). These segments carry their own background, so they look the same on every theme.
  - Docker and conda use `#83a598` on `#665c54` (2.4).
  - The error `` is red `#cc241d` (2.6 on the dark default).
  - The time segment's `#3c3836` background is almost the same as Ghostty's own background (1.2), so the segment's edge disappears, though its text stays readable.

The kit's other variants have the same problems but were not changed, because the brief named only kris:

- **dev and two-line:** time and continuation in `bright-black`, yellow status and duration, a cyan path and a green `>`.
- **one-line:** the duration is `dimmed white` (3.2 on dark, about 1.4 on light) and the `➜` is green.

### Ghostty notes

- `ghostty +list-themes` opens an interactive previewer for its 463 built-in themes when run in a terminal. Light ones include Builtin Light, GitHub Light Default, Catppuccin Latte and Apple System Colors Light.
- `theme = light:<name>,dark:<name>` in `config.ghostty` follows the macOS appearance setting.
- `minimum-contrast = 3` makes Ghostty lighten or darken any foreground that falls below that ratio. That one line would rescue most of the preset problems above, without editing any preset.
- `faint-opacity` (default 0.5) controls how washed out `dimmed` text is.

## In Progress

Nothing.

## Queries

**Context:** Only the kris variants were fixed. dev, two-line and one-line are also the kit's own files, and they still have the bright-black, yellow and cyan problems. **Query:** Should the same colour rule be applied to dev, two-line and one-line? **Options:** a) (recommended, confidence medium - it is the same mechanical change, and it keeps the preview fair when you compare variants) Apply it in a short follow-up run. b) Leave them as they are; kris is the default you are likely to keep. c) Remove those three variants instead.

**Context:** Ghostty's `minimum-contrast` setting would fix low-contrast colours in every prompt and program, including the untouched presets. It is a change to `config.ghostty`, outside the kit, and would belong in chezmoi. **Query:** Do you want to try `minimum-contrast = 3`? **Options:** a) (recommended, confidence medium - one line that also helps other programs, and easy to undo) Try it by hand in a Ghostty window first, then decide whether chezmoi should manage it. b) Leave Ghostty at its defaults and rely on prompt colours alone.
