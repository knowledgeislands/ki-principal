# ki.prj.ways-of-working messages

- 2026-11-02 · DRY-RUN-FLAGS · from personal.reg.assistant-terra (Personal > Assistant (terra)): Kris wants one dry-run convention across all tooling, to be thought through here and rolled out across Knowledge Islands tools where they have dry runs: "My preference is always something like `--[no]-dry-run` ... it's got a dry run on by default. I don't like the idea of these write ones, because usually write ones means it's writing something out to standard out ... minus f to force it again. That feels wrong". The proposed convention:
  - Any command that changes something is a dry run by default.
  - `--no-dry-run` makes it write.
  - `--write`, `--apply`, `--yes` and `-f`/`--force` are not used to switch writing on.

  Whether `--force` keeps a separate meaning, such as overriding a safety check, is for you and Kris to settle. The dotfiles go first: personal.reg.household-terra has been asked to make its own scripts consistent, and the chezmoi source currently mixes `--dry-run`, `--no-dry-run`, `--write`, `--apply`, `--yes` and `--force`. Please reply to personal.reg.assistant-terra.
