# starship-classic

**🤖 → 👤 Handoff to supervisor · Run report at 08:25 BST**

---

## Done

You can now switch back to your old prompt and preview every variant at once. Two local commits on `main`, not pushed, applied or installed:

- `27d524a` style(starship): only foreground, blue, red and purple text in `dev`, `two-line` and `one-line`, with italics for secondary text. `kris` and `kris-nerd` are now the kit's recoloured versions, keeping the managed ⚙ module, which is now purple. I also made the Git state label (rebase or merge in progress) red in all five, because its built-in default was still yellow. `pure` and `rainbow` are unchanged.
- `20922de` feat(zsh): adds `starship-variant classic` and `--all`/`-a`, plus their completion, guide sections and tests.

How `classic` works:

- `starship-variant classic` switches to your previous prompt, the `99_prompt` one with the ➜ arrow, directory, ⚙ count and git-radar. The fragment saves that prompt before it starts Starship.
- To switch, it puts that prompt back and removes Starship's two hooks. The shell keeps running and the ⚙ refresh hook stays.
- The session remembers the choice as `STARSHIP_CLASSIC=1`, with `STARSHIP_CONFIG` unset, so shells started from it stay classic.
- `--machine classic` writes `classic` to the machine-variant file, so new shells start without Starship.
- Switching to any variant, or running `--machine --reset`, turns Starship back on in the same shell. Starship's init still runs only once per shell.
- The variant list shows `classic` first and marks it with `*` when it is active.
- Wherever the Starship binary is missing, the fragment does nothing and the classic prompt stays as before.

`--all` renders `classic` first, then every variant, labelled and in colour, left and right prompt, without switching. It takes `--status N` and `--duration MS`.

Checks:

- Throwaway `zsh -i` with `HOME` pointed at a temporary render of the fragments and variants, using the kit's starship binary: classic, back to a variant, list marks and the ⚙ count all behaved correctly.
- `--all` took 430 to 490 ms over 5 runs in the chezmoi repository, 8 renders each.
- `ki repo audit --repo .`: PASS=17 WARN=4 FAIL=0, the same as before.
- `node --test tests/*.test.mjs`: 345 tests, 343 pass, 0 fail, 2 env-gated skips.
- `rumdl check .`: clean.

**STARSHIP-APPLY needs no extra targets.** Everything is in `~/.zsh/99_starship` and `~/.config/starship`, which the existing step 2 already applies. `~/.zsh/completions/_starship` did not change.

**Undo:**

- In the source: `git revert 20922de 27d524a`.
- On a machine, without reverting: `starship-variant --machine classic`.

Temporary area emptied. Rig files and `dot_zshrc.tmpl` untouched. Another session's uncommitted changes (Zed, Rig and the rationale review) were left alone.

## In Progress

Nothing.

## Queries

None.
