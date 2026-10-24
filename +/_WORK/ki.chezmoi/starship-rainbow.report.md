# [chezmoi dotfiles](/Users/krisbrown/.local/share/chezmoi/README.md) › Starship › starship-rainbow

**🤖 → 👤 Handoff to supervisor · Run report at 01:40 BST**

---

## Done

- The new variant is called **`kris-rainbow`**. It's in [`kris-rainbow.toml`](/Users/krisbrown/.local/share/chezmoi/dot_config/starship/variants/kris-rainbow.toml), it's applied to `~/.config/starship/variants/`, and `starship-variant` lists it. `kris` is still the default.
- **Preview it:** in a Ghostty window, run `starship-variant kris-rainbow` to try it in that window, or `starship-variant --all` to see it next to all the others. **Make it the default:** `starship-variant --machine kris-rainbow` sets it for this machine; `starship-variant --machine --reset` goes back to `kris`.
- **What the prompt shows,** left to right on line one, as joined coloured segments in the Gruvbox Rainbow style:
  - an orange segment with the Apple icon and the host name;
  - a yellow segment with the folder, shown as `knowledge-islands › tools-ki/src`, with the repo name in bold;
  - an aqua segment with the Git branch and its change counts;
  - a blue segment with the bun, node or python version, only where the folder uses one;
  - a purple pill with a gear and the number of chezmoi changes waiting to be applied;
  - background jobs at the far right.
  - The right side shows a red pill with the exit code after a failure, a pill with the time a command took once it runs 2 s or longer, and the time. Line two is the rainbow arrow, which turns red after a failure.
- **What it carries over from `kris`,** beyond the stock preset:
  - the chezmoi change count;
  - the host shown all the time, with an SSH icon and the user name when you're logged in over SSH;
  - the `territory › repo` folder names, with the repo in bold;
  - `detached <hash>` instead of a branch on a detached HEAD;
  - a linked worktree's name;
  - a rebase or merge in progress, with its step count;
  - Git status with counts;
  - node only at a package root;
  - python's virtualenv name;
  - background jobs;
  - exit status, command time and the time on the right;
  - the same time limits as `kris`, a 500 ms command limit and a 30 ms folder scan.
- **One change from the stock rainbow:** the yellow and aqua segments now use dark text. The preset's cream text was hard to read on them, at a contrast of 2.2 and 2.8.
- **Checked:** Starship reads the file with no warnings. I rendered it in the chezmoi checkout, in `tools-ki` and its `src` folder, in a scratch worktree and on a scratch detached HEAD; it took about 20–30 ms per prompt. Both custom modules use dash builtins and never call git or chezmoi.
- **Also updated:** the tests, the [Starship guide](/Users/krisbrown/.local/share/chezmoi/docs/guides/tools/starship.md) (new section, variants table, colours and Nerd Font notes) and the [Ghostty guide](/Users/krisbrown/.local/share/chezmoi/docs/guides/tools/ghostty.md). The longer name pushed the `starship-variant` list out of line, so I widened its name column in `99_starship`.
- **Commits:** `a4826c9` adds the variant, and `b227850` fixes the list alignment.
- **Gate:** `node --test` passed (339 passed, 0 failed); `rumdl` found nothing; `ki repo audit` passed with no failures and 5 warnings, all about the older project registry and none from this change.
- **Applied:** only `kris-rainbow.toml` and `~/.zsh/99_starship`. Nothing was pushed.

## In Progress

Nothing.

## Queries

None.
