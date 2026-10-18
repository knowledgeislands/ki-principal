# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › mgit-flags

**🤖 → 🧑 Handoff to supervisor · Run report at 09:57 BST · last mark 22:34 BST**

---

## Done

- Searched again for `mgit -B` and `mgit --bare` in the chezmoi source, in every repository under `~/workspaces` and in the chezmoi-managed shell startup files. No script, alias, function or program uses either flag. The only live consumer was the chezmoi Zsh completion snapshot, which offered `-B` and `--bare`.
- Chezmoi source (`~/.local/share/chezmoi`): `dot_zsh/completions/_mgit` now offers `-R` and `--raw` in place of `-B` and `--bare`, with the same description. Committed as `0da259e` and pushed fast-forward. The pull with rebase refused because of another session's uncommitted file, but origin had not moved, so the push was a plain fast-forward. Not applied. Gate: `rumdl` and the completions test pass. Three failures were already there before this change and do not involve it: the `ki repo audit` missing `.claude/skills/ki-self` projection, the duplicate `KB-DOTFILES-UE-096` id, and the `node --test` wrapper exit-40 test.
- `chezmoi diff ~/.zsh/completions/_mgit` (scoped to this one file, so no template or secret is rendered), for you to review:

  ```diff
  @@ -20,8 +20,8 @@
       '--physical[do not follow symlinked container directories]'
       '-L[follow symlinked container directories]'
       '--follow-symlinks[follow symlinked container directories]'
  -    '-B[run an ordinary command without git prefix]'
  -    '--bare[run an ordinary command without git prefix]'
  +    '-R[run an ordinary command without git prefix]'
  +    '--raw[run an ordinary command without git prefix]'
       '-I[ignore workspace selection from .mgit.toml]'
  ```

- [KI-TOOL-MGIT-CLI-025](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-025-escape-hatch-flag-names.md):
  - Planned to Ready as `33ab1c5`.
  - Built to Awaiting review as `bac4100`. `-B` and `--bare` are now usage errors that name `-R/--raw` and run nothing. `-R` is unchanged. `-G` is marked as a temporary name until `-B` returns as the bypass-to-Git flag.
  - Pushed fast-forward.
  - Gate passes: `ki repo audit` has no failures and three warnings that were already there; shellcheck, `bash -n`, the mandoc lint and `git diff --check` pass. Bats passes 123 of 123 with the real `ki` producer and nothing skipped, all in disposable fixtures.
- Files changed, by repository:
  - chezmoi source: `dot_zsh/completions/_mgit`.
  - tools-mgit:
    - Code: `bin/mgit`.
    - Tests: `tests/mgit.bats`, `tests/territory-protocol.bats`, `tests/territory-producer.bats`.
    - Documentation: `man/mgit.1`, `README.md`, `docs/guides/user/running-commands.md`, `docs/specs/workspace-dispatch.md`, `CHANGELOG.md`.
    - Record: `docs/roadmap/KI-TOOL-MGIT-CLI-025-escape-hatch-flag-names.md`.
  - No other repository needed a change.
- Hits and files left alone:
  - Hits that are prose, not uses: [decisions.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md), [accept-mgit.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/accept-mgit.report.md), `+/_WORK/ki.tools-burndown/roadmap-overview.report.md` and `+/_WORK/ki/design/themes/theme-map.svg` in ki-principal. These are historical records and were not edited.
  - `ki-design` and `apps-knowledgeislands.info`: searched; no hits.
  - Another session's dirty file, not touched: `workspaces/knowledge-islands/dot_mgit.toml` in the chezmoi source.
- Report path: the brief's progress protocol makes this file the only report path, so nothing was written or committed to the ki-principal report path the task named.

## In Progress

- Nothing is running.
- Your interactive shell history was not searched for `mgit -B`.
- The installed `mgit` links to the tools-mgit checkout, so `-B` already fails on this machine.
- Seven older non-fatal `[[ ]]` assertions remain in the two territory Bats suites. The TEST-FATAL rule covers them, but they need their own fix.

## Queries

### MGIT-FLAGS-APPLY - the chezmoi completion change

**Context:** The completion snapshot is committed and pushed but not applied, so your shell still suggests `-B`. The `chezmoi diff` excerpt above shows the whole change.

**Query:** Should the completion change be applied?

**Options:**

a) (recommended, confidence high - two lines, no template, and the diff matches the source exactly) Yes. Run `chezmoi apply ~/.zsh/completions/_mgit` after reading the diff above.

b) Wait, and regenerate the whole snapshot from `mgit completion zsh` at the next mgit release instead. This also picks up `-G`, `-j`, `-v`, `--json` and `overview`.

### MGIT-FLAGS-ACCEPT - closing KI-TOOL-MGIT-CLI-025

**Context:** [KI-TOOL-MGIT-CLI-025](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-025-escape-hatch-flag-names.md) is at Awaiting review. The gate is green and its review packet is in the record.

**Query:** Should -025 be accepted as done?

**Options:**

a) (recommended, confidence medium - small, fully tested change, but you have not tried it by hand) Yes. Accept it now, and fold any hands-on finding into [KI-TOOL-MGIT-CLI-023](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-023-hands-on-behaviour-check.md).

b) Hold it at Awaiting review until you have tried `mgit -B` and `mgit -G` yourself.
