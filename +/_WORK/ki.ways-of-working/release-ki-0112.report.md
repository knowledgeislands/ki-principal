# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › release-ki-0112

**🤖 → 🧑 Handoff to supervisor · Run report at 11:40 BST · last mark 11:06 BST**

---

## Done

- I waited for `config-preserve` to finish. v0.11.2 includes its `config.toml` fix (tools-ki `296634e1`), and the CHANGELOG already names it: `ki` writes `config.toml` only when a value it owns changes.
- Harness pin: ki-agentic-harness `main` at `0828bd06` (pushed) carries both renames. `ki-coordination` and `ki-work-design` replace `ki-pmo` and `ki-pmo-design`, and `ki-work-folder` replaces `ki-checkpoint`. Two downloads of the archive gave the same digest, `0b2bf10b…e9e7`, and every bootstrap skill is present in it.
- tools-ki `e037e2ac` `fix(bootstrap)`: repins `canonicalHarnessRelease` with its test and CHANGELOG entry. The pin concern in [KI-TOOL-KI-CLI-148](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-148-coordination-rename-cli-side.md) is now marked resolved.
- tools-ki `1b6d5f97` `chore(release): prepare v0.11.2`.
- Gate: 1346 tests passed with coverage. `tsc`, `biome`, `knip` and the manual lint passed. `ki repo audit` gave FAIL=0 WARN=2. CI on `main` passed.
- v0.11.2 is tagged and pushed. The Release workflow passed every job: the three archives, signing and publishing, the clean Linux install check, and the tap notification. No npm or other public registry was used.
- Homebrew: the tap bot opened and merged PR #44 (`788755a`), the same automated path v0.11.1 took. The local tap checkout is now level. `brew upgrade` ran on this Mac only, and `brew list` shows `ki 0.11.2`. `ki` on PATH is still the existing `~/.local/bin` local runner, which also reports 0.11.2.
- ki-principal `4df0b1d` `chore(ci): install ki v0.11.2` is pushed. It replaces v0.11.0; v0.11.1 was never pinned there.
- ki-principal CI: the "Install released KI" step, which contains `ki repo repair --repo .`, now passes. The two runs before mine failed at that step. The run is still red, at the next step, `ki repo audit`; see the query.
- I pushed no other session's commits; every repository was level with origin when I pushed. Dirty files from other sessions in ki-principal are untouched: `+/_WORK/ki.chezmoi/decisions.md`, `+/_WORK/ki.ways-of-working/config-preserve.report.md`, the untracked `+/_THREADS/`, and four untracked reports in `+/_WORK/ki.ways-of-working/`.
- New open records: 0 in tools-ki, 0 in ki-principal, 0 in homebrew-tap, 0 in ki-agentic-harness.

## In Progress

None. The temporary folder is empty.

## Queries

**PRINCIPAL-AUDIT-RED**

**Context:** With v0.11.2, ki-principal CI gets past the repair step, but `ki repo audit` reports 75 failures. 72 are COORD-7 failures in `+/_WORK/` reports: record identifiers without links, mostly in old run reports. The counts are ki.tools-burndown 31, ki 13, ki.chezmoi 9, ki.ways-of-working 9, ki.mac-studio-setup 6, and 2 each in ki.knowledge-acquisition and ki.observatory. The other three are:

- BODY-11 in GDR-KI-PRINCIPAL-010, which has a `[[Symbol Library]]` link.
- SCR-11: the `.husky/pre-commit` hook is missing the `syncpack format --check` step.
- RECORD-2: the ki.ways-of-working `work.md` has an empty Messages section.

My authority covered none of these.

**Query:** How should ki-principal's audit get back to green?

**Options:**

a) (recommended, confidence medium - most failures sit in old reports that the work-folder tidy rules would remove anyway) Launch one ki-principal run. It tidies old reports under the `ki-work-folder` rules, links record identifiers in the reports that remain, and fixes the three single findings. It leaves alone the work folders that other sessions have in flight.

b) Link every identifier in place and keep all reports, plus the three fixes.

c) Leave CI red until each work's close-out tidy reaches it.
