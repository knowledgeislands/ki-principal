# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › mgit-filter

**🤖 → 👤 Handoff to supervisor · Run report at 19:41 BST · last mark 19:08 BST**

---

## Done

- **tools-mgit `781973e`, pushed:** `--filter` has no short letter. `-f` is now a status-2 usage error that names `--filter` and runs nothing, as `-G` was handled. Help, Bash and Zsh completions, manual, README, the running-commands and repository-sets guides, the MGIT-WS-009 specification and the changelog are updated. Tests came first: a new Bats case, `-f is not a short filter and runs nothing`, failed before the change, and every test that used `-f` now uses `--filter`. CLI-025 has already been pruned, so the finding is folded into [KI-TOOL-MGIT-CLI-023](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-023-hands-on-behaviour-check.md) as a Remedial finding fixed there. The installed mgit links to the checkout, so the change is live on this Mac.
- **tools-mgit gate:** all checks pass. Shellcheck, `bash -n`, mandoc lint and `git diff --check` are clean. `bats tests/` passes, and the real-producer proof passes against the installed `ki`. `ki repo audit` passes; its 4 warnings were already there and are covered by [KI-TOOL-MGIT-CLI-027](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-027-fatal-bats-assertions.md).
- **ki-agentic-harness `eea83b52`, pushed:** the `ki-repo-tools` command-line conventions now include a third house rule. A working-set name filter is the long `--filter <prefix>` with no short letter, so `-f` stays reserved for force or file. The shared KI and mgit selection rule in `ki-repo`'s configuration standard no longer mentions `-f`. This is folded into [KI-HARNESS-GOV-218](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-218-cli-conventions.md). No other session's commits went with it.
- **Harness gate:** all checks pass. `bun run test` passes 1260 tests and `bunx tsc --noEmit` is clean. `ki dev skill rubric ki-repo-tools` is in sync. The focused audits for `ki-skills`, `ki-authoring`, `ki-work-roadmap` and `ki-repo` pass.
- **Departures:** I checked for a `-f` filter item and found none to remove. The departures Messages line in Tools burndown already left `-f, --filter` out, and GOV-218 does not list departures.
- **ki.chezmoi Messages line `MGIT-ZSH-COMPLETION`:** it asks ki.chezmoi to regenerate `dot_zsh/completions/_mgit` from `mgit completion zsh` and hold it for Kris's `chezmoi diff` review. The snapshot predates several mgit changes, so the line warns that the diff is wider than the dropped `-f` line.
- **Net records:** none opened in any repository. Both changes are folded into existing records: tools-mgit 0, ki-agentic-harness 0, ki-principal 0.
- **Out of scope:** tools-ki and the chezmoi source were not touched.
- **Other sessions' files:** I left them alone. In ki-principal these are `+/_WORK/ki.chezmoi/mark-tidy-current.report.md` and `+/_WORK/ki.ways-of-working/small-fixes.report.md`, both untracked.

## In Progress

- tools-ki's `-f` retirement rides in the queued ki-release run. Until then, `ki territory roots` still accepts `-f`, even though the harness guidance now records the house form without it. mgit sends only `--filter` to the producer, so this does not affect mgit.

## Queries

### MGIT-RELEASE - when other machines get the -f change

**Context:** `main` now carries breaking changes since v0.17.0 (`-B/--bypass`, `learn` and dropping `-f`), but only this Mac runs the checkout; Terra and Sol keep v0.17.0, where `-f` still works.

**Query:** Should mgit be released now so every machine has the same flags, or wait until Kris finishes the hands-on check in KI-TOOL-MGIT-CLI-023?

**Options:** a) (recommended, confidence medium - one release carries the hands-on fixes and avoids a second breaking bump) Wait for the KI-TOOL-MGIT-CLI-023 hands-on check, then release once under [Release mgit](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/guides/developer/releasing.md). b) Release v0.18.0 now from `main`, so the machines agree today.
