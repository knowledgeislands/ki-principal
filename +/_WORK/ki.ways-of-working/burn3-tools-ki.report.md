# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › burn3-tools-ki

**🤖 → 👤 Handoff to supervisor · Run report at 08:29 BST · last mark 05:20 BST**

---

## Done

- [KI-TOOL-KI-CLI-159](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-159-island-maturity-and-health.md), Island maturity and health, is delivered and now awaiting review, with a review packet. No owner decision was needed: the record left the design to tools-ki, and the reader imports no harness code, so it does not have to wait for the harness to be pushed.
- What it does: `ki territory show` now shows each island's declared maturity and its health (sound, in decline or in ruin) on its row. `--verbose` adds the evidence. `--format json` publishes `ki/territory/v1` for the Observatory. Health comes from the latest whole-repository `ki repo audit`, which is now recorded on each machine. An undeclared maturity or an unrecorded audit reads as unknown.
- Commits: `b4f8a100` planned the record to Ready, and `5aebeb9d` delivered it. Both were fast-forwarded onto local `main` and pushed to `origin/main`. Only this run's commits were above `origin/main`.
- Tests: 1,405 passed at 100% coverage.
- TypeScript: passed.
- Biome, rumdl, knip, the manual lint and the command-inventory check: all passed.
- Pre-commit and commit-msg hooks: passed.
- `ki repo audit --skill ki-work-roadmap`: passed.
- Clean-up: the worktree and its branch are removed, and the temporary directory is empty.
- Follow-up: one line, ISLAND-CONDITION, added to [messages.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/messages.md). It is uncommitted in ki-principal, so the coordinator can take it.

## In Progress

Nothing. Still open:

- No island declares `maturity` yet, so every island reads unknown for maturity.
- Health reads unknown on each machine until a whole-repository audit runs there.
- The harness work for KI-HARNESS-GOV-223 is still not pushed.

## Queries

None.
