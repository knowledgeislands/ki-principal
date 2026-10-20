# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [Mac Studio setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup.md) › deliver027

**🤖 → 👤 Handoff to supervisor · Run report at 01:34 BST · last mark 23:36 BST**

---

## Done

- [KI-TOOL-RIG-CLI-027](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CLI-027-command-line-convention-departures.md) delivered to Awaiting review in tools-rig commit `66c9c57` on `main`, local only, baseline `2b4e2ef`. Every Rig command now accepts `--name=value`, `--json` (same as `--format json`, which stays), `-n` for `--dry-run` and `--` as end of options, all through one normaliser driven by the option inventory.
- Help, Bash and Zsh completion, `rig(1)`, the command guide, README, the command-surface guide and the changelog baseline updated; `RIG-PORT-014 — Command-line option grammar` added to portability, conforming. The manual and command-guide synopses also gained the missing `rig remove` line.
- `status` now rejects a repeated `--format`, as the other commands already did, so `--json --format text` exits 2 everywhere. The Steps allowed this parser change.
- Full Bats suite: 600 of 600 pass. Shell gate (ShellCheck, Bash 3.2 syntax, assembly check, benchmark, native smoke, mandoc lint): clean. `git diff --check`: clean. `ki repo audit --repo .`: no failures; its warnings predate this change. The pre-commit hook passed.
- No live machine change. Manual checks used only read-only commands and `init -n` in a disposable HOME and XDG tree. No other session's changes were present.

## In Progress

Nothing.

## Queries

### Q-027-REPEATS — Repeated status options

**Context:** RIG-PORT-014 says a repeated option exits 2. `status` still accepts a repeated `--profile`, `--problems`, `--unmanaged` or `--retired`, and the last one wins. The other commands reject them. This record enforced the rule only for `--format`. The record's Outstanding concerns list this gap, along with two older ones: `remove`'s `--format` pre-scan, and `--sudo` missing from the guide and manual `apply` synopses.

**Query:** How should these three small gaps be handled, given that CAPTURE-GATE stopped me creating a record?

**Options:** a) (recommended, confidence medium - small, related fixes to the same option surface) capture one triage record in tools-rig for all three, and fix it at Rig's next change; b) fold them into the review of KI-TOOL-RIG-CLI-027 as a follow-up commit before acceptance; c) leave them as recorded concerns only.

### 🤖 → 👤 Handoff to supervisor · since 01:34 BST

👤 1 with you

- [with you] Q-027-REPEATS: repeated status options · owner · since 01:34 BST
- [committed] tools-rig `66c9c57` on `main`
- [unpushed] tools-rig `main`, 1 commit, on this machine
