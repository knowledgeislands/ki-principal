# hold-apply

For ki.agent-host, under Kris's OVERNIGHT authority of 20 October. Both answers were reviewed blind by query-review-6, which agreed, so they are high.

1. **CHAIN-GATE a):** under `ki-work-roadmap`, release `tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-048-signed-release-install-kind.md` from hold to `soon`, with a Shaping section covering the accepted built-in signed-release approach and its existing shared-role scope. Say that delivering it clears only the signed-install prerequisite: KI-TECHNE-OPS-018 still needs binding-owner evidence of a clean `rig status` through a pin bump, and KI-TECHNE-OPS-024 still needs the role-profile move. Keep KI-TECHNE-OPS-018 and KI-TECHNE-OPS-024 held. Create, split and merge nothing.
2. **CLI125-HOLD a):** in `tools-ki/docs/roadmap/KI-TOOL-KI-CLI-125-ki-release-contract.md`, keep the hold and reduce its condition to "An ARM host is needed", with the same review date.
3. In `ki-principal/+/_WORK/ki.agent-host/`, mark both queries answered in `queries.md`, and record each in `decisions.md` in one line: "taken under OVERNIGHT, reviewed by query-review-6".
4. Run each repository's checks (`ki repo audit` and its lint). Other sessions have uncommitted files in tools-rig and tools-ki: leave them alone, and commit only your own paths, with the paths on the commit command itself.

## Rules

- Do not push, and make no remote or host changes.
- CAPTURE-GATE: create no roadmap record. HOOKS-MIGRATION: never run `ki repo conform` without `--dry-run`, and do not touch `package.json`, `bun.lock`, `.husky/` or `.githooks/`.
- Use Conventional Commits, ending with "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>". British English, ASCII hyphens only.
- Report to the path your run packet names, as an owner report: Done, In Progress, Queries.
