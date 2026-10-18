# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › config-preserve

**Run report at 11:27 BST**

---

## Done

- **Cause found.** On every run, plain `ki bootstrap` reaches the configuration writer. That writer re-rendered the whole of `config.toml` and passed every table it does not own, such as `[territories]`, back through the TOML library. So Sol's chezmoi-managed file lost its comments, blank lines and multi-line arrays even though no value had changed. `ki harness install` and `uninstall` also rewrote the ids line by pattern.
- **Fixed in tools-ki, under SOL-CONFIG-REFORMAT a).**
  - The writer now compares the values it owns with the file and writes nothing when they already match.
  - When a value does differ, it edits only that statement or table in place. It writes only after checking that every other value is unchanged.
  - A file it cannot edit safely is laid out afresh, as before, keeping every table it does not own. That means an owned value written inline or dotted, or a file that does not parse.
  - Harness install and uninstall now edit only the harness ids, and only when they change.
  - `ki repair` was already minimal and is unchanged.
  - The paths covered are bootstrap and `--refresh`, the one-time `[locals]` move, `ki dev local set|on|off`, skill and agent changes, the retired repository-paths move, and harness install and uninstall.
- **Tests.**
  - Eleven new public-CLI tests use a fixture `config.toml` with comments and a multi-line `territories` array, plus one new harness uninstall test.
  - They check that the file is byte-identical after bootstrap, refresh, the locals migration, `ki dev local on` and a set/on/off round trip, and that a real change edits only its own lines.
  - All seven byte-identity tests failed on the old code.
  - The canonical `ki dev local off` cannot run in the test sandbox because it needs the pinned release archive. The round trip therefore uses a second harness, which goes through the same writer.
- **Recorded** in [KI-TOOL-KI-CLI-143](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-143-separate-local-harness-paths.md) under "Follow-up fix: config.toml kept byte-identical". It covers the cause, the files, the verification and six checks for the Sol and Terra re-runs: version, the `config.toml` hash before and after bootstrap and `dev local on|off`, the `[locals]` move, the binding and harness identity, `ki doctor` and `ki diag --full`, and `chezmoi diff`. Each host needs its own evidence. A changelog line was added as well.
- **Gate:** the full coverage suite passes at 100% (1346 tests). tsc, Biome and the man-page lint pass. The repository audit has no failures; its two warnings, CI-1 and HOOK-1, were already there.
- **Pushed to tools-ki `main`.** Another session's commit, "fix(work): follow the ki-work-folder rename", landed on top of my fix commit and pushed it with its own push. My record and changelog commits followed.
- Nothing was released. I touched no real `~/.config/ki` file, no chezmoi source, and neither Sol nor Terra.
- **Net open records:** tools-ki 0 new, ki-principal 0 new.

## In Progress

- Nothing. release-ki-0112 can cut v0.11.2, and then ki.chezmoi re-runs Sol against the checks in the record.

## Queries

### CONFIG-PRESERVE-REVIEW: does the fix need its own review before release?

- **Context:** [KI-TOOL-KI-CLI-143](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-143-separate-local-harness-paths.md) was already accepted as done. I folded the fix in as instructed and left its status at done.
- **Query:** should the fix ship in v0.11.2 on its tests and the gate, or get an independent review first?
- **Options:**
  - a) **Recommended (confidence: medium).** Ship it on the tests and the gate. The Sol and Terra re-runs then serve as the live proof. The change is limited to the writer, and it falls back to the old layout whenever it cannot verify an edit.
  - b) Run a short independent review of the fix before release-ki-0112 cuts v0.11.2.
