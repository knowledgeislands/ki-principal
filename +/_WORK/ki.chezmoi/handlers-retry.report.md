# [Rig](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/README.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) › handlers-retry

**🤖 → 👤 Handoff to supervisor · Run report at 01:15 BST**

---

## Done

- `.sh` now opens in Zed (was Ghostty). Undo: Finder › Get Info on a `.sh` file › Open with › Ghostty › Change All.
- `.zsh` now opens in Zed (was Ghostty). Undo: Finder › Get Info on a `.zsh` file › Open with › Ghostty › Change All.
- The first apply reported both as failed. Rig checks the handler straight away, before the macOS prompt had been accepted. A minute later both resolved to Zed. The one authorised retry then completed for both with no prompt, which cleared their failed-apply records.
- Pre-checks passed: `~/.local/bin/rig` resolves to tools-rig at `87fa261`, and the dry run planned only `default-application:sh` and `default-application:zsh`.
- `rig doctor` went from 7 findings to 3 and still exits non-zero.
- Before (7): drift on `sh`, `zsh` and `toml`; `firewall.screen-sharing-tailnet` drifted (`anchor-changed,exposed-beyond-tailnet`); and failed-apply records for `sh`, `zsh` and `toml`.
- After (3): `default-application.toml` drifted (VS Code, expected Zed), held under KI-TOOL-RIG-CORE-069 and not targeted; its failed-apply record from 19 October; and `firewall.screen-sharing-tailnet` drifted, which is outside this grant and connection-critical, so it was left alone.
- No source change, no commit, no `chezmoi apply`. Temporary files have been cleared.

## In Progress

Nothing.

## Queries

**Context**: Rig's macOS handler apply checks whether the change worked immediately after asking macOS. When macOS shows a confirmation prompt, that check runs before Kris can answer it, so a change that does take effect is recorded as a failure. A re-run is then needed to clear the record. This probably applies to `.toml` too once KI-TOOL-RIG-CORE-069 is released. **Query**: Should this be captured as tools-rig work? **Options**: a) (recommended, confidence medium - seen on this run and very likely the cause of the earlier failures as well) capture a tools-rig triage record so that the handler apply waits, or polls for a bounded time, for the prompt before it checks; b) leave it and re-run after each prompted apply.

**Context**: `firewall.screen-sharing-tailnet` reports `anchor-changed,exposed-beyond-tailnet`, which means Screen Sharing may be reachable from beyond the tailnet. It was present before this run and is connection-critical. **Query**: Should it be investigated in its own run? **Options**: a) (recommended, confidence high - possible exposure beyond the tailnet, and the change needs a tested restore path) brief a separate read-only investigation, with a restore path, before any firewall apply; b) leave it for the next drift survey.
