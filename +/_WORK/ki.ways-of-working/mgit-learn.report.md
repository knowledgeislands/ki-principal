# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › mgit-learn

**🤖 → 🧑 Handoff to supervisor · Run report at 18:22 BST · last mark 18:20 BST**

---

## Done

- **Learning is live.** mgit has no built-in quiet rules any more. `mgit learn <command>` and `mgit --learn <command>` are new, along with `mgit learn --list` and `mgit learn --forget <command>`. The old built-in `st` rule is gone from the code. tools-mgit `73f1f5f` (feat(cli)!), pushed. The installed `mgit` links to this checkout, so it is live on this Mac now.
- **Flags.** `-B/--bypass` is now the bypass-to-Git flag. `-G` and `--git` are gone and give an error naming `-B/--bypass`. `--bare` gives an error naming `-R/--raw`. `-R/--raw`, `-P/--physical` and `-L/--follow-symlinks` are unchanged. Help, the Bash and Zsh completions, the manual, README, guide, spec and changelog are all updated, in the same commit.
- **Records.**
  - [KI-TOOL-MGIT-CLI-024](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-024-quiet-normal-git-output.md) is rewritten for the learning design and set to Awaiting review (in `73f1f5f`).
  - [KI-TOOL-MGIT-CLI-025](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-025-escape-hatch-flag-names.md) is amended for `-B/--bypass` and accepted under ACCEPT-AND-PRUNE (tools-mgit `5d23dce`). It is not pruned.
  - Net records: tools-mgit 0 new; ki-principal 0 new.
- **Seed templates.** Four templates were learned on this Mac, from read-only commands only, in `~/.config/mgit/templates/`: `st` (`status -sb`), `status`, `status --short --branch` and `branch`.
  - `mgit --estate st` now reports 48 quiet and 2 with output: the chezmoi source and ki-principal, which have local changes.
  - `fetch --dry-run` and the log ranges `@{upstream}..HEAD` and `HEAD..@{upstream}` already print nothing on a level estate, so they needed no template.
  - Boundary slip: my first `st`, `status` and `branch` learning runs included apps-knowledgeislands.info, which I was told to stay out of. These were read-only `git status` and `git branch` runs; nothing there was written or changed. I excluded it from every later run. The templates hold only placeholders, nothing from that repository.
- **Hand-off.** The MGIT-CONFIG Messages line in [ki.chezmoi work](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) is committed and pushed (ki-principal `175a276`, with a time correction in `c8615c7`). It asks ki.chezmoi to:
  - bring `~/.config/mgit/` into the chezmoi source for Kris's `chezmoi diff` review;
  - regenerate the `_mgit` Zsh completion, which still offers the old flags.
- **Checks.**
  - Bats: 131 of 131 pass.
  - `ki repo audit`: pass, with no failures. The warnings are the missing pre-commit hook and the territory suites' non-fatal assertions, which [KI-TOOL-MGIT-CLI-027](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-027-fatal-bats-assertions.md) covers.
  - shellcheck, `bash -n`, mandoc lint and `git diff --check`: all pass.
- **Also fixed.** One territory-producer Bats case failed now and then, because of the order of parallel output. It now runs one job at a time.
- **Other sessions' commits.** None were pushed with mine. tools-mgit `ff7f44e`, `0c03d68` and `c76b4d5`, and ki-principal `bf9c9e9`, were already on origin.

### How `mgit st` decides what to hide, in plain words

When you run a command through mgit, it looks for a template for that command. It turns Git aliases into their full form first, so `st` and `status -sb` share one template. In each repository, mgit takes the command's output and swaps that repository's own details for placeholders: its branch name, upstream, remote, remote address, folder path and repository name. If the command succeeded and what is left matches the template exactly, mgit hides that repository. Anything else is shown in full: an extra line, a different line, or a failure. With no template, everything is shown. `-v` and `--json` always show the raw output.

Learning is how a template gets made. `mgit learn st` runs `st` in every selected repository, as a normal run would, and does the same swap. If every repository gave the same answer, mgit saves that answer as the template, a plain text file with an explanation at the top. If they did not, it names the repositories that were different and saves nothing. So learn on a set of repositories you know are in their normal state. You can learn any Git command this way. If a command changes things, such as `pull` or `push`, learning it really runs it, so learn those during a run you meant to do anyway: `mgit learn pull`.

## In Progress

Nothing.

## Queries

### MGIT-LEARN-FLAG - should `-L` stay "follow symlinks" or become the short flag for learn?

**Context:** Across Unix tools, `-P` and `-L` are an agreed pair. POSIX `cd` and `pwd` use `-L` for logical and `-P` for physical paths. POSIX `cp -R`, `find`, `chown -R`, `chgrp -R` and `du` use `-P` for never following symlinks and `-L` for always following them, with `-H` for following only symlinks named on the command line. `ls -L`, `stat -L`, `realpath -L/-P`, `ln -L/-P`, `fd -L` and `rg -L` follow suit, and GNU spells them `--dereference` and `--no-dereference`; rsync is the odd one out. mgit's `-P/--physical` and `-L/--follow-symlinks` match this `find`-style meaning. No script, alias or program in the workspace or the chezmoi source uses them: the only hits are your own words in the decisions log and the chezmoi `_mgit` completion, which simply lists the options. Learning does not need a short flag, because `mgit learn st` is already short.

**Query:** Should learn have no short flag, leaving `-P` and `-L` with their usual Unix meanings, or should `-L` become learn?

**Options:** a) (recommended, confidence high - keeps the meaning every Unix tool gives `-L`, and `mgit learn` is already short) Keep `-P/--physical` and `-L/--follow-symlinks` as they are, and give learn no short flag. b) Make `-L` the short flag for `--learn` and leave following symlinks as `--follow-symlinks` only. This breaks the Unix meaning and changes what any existing `mgit -L` does.
