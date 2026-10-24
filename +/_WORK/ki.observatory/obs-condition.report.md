# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-condition

**🤖 → 👤 Handoff to supervisor · Run report at 19:52 BST**

---

## Done

- [KI-HARNESS-GOV-223](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-223-island-maturity-declaration.md) Island maturity declaration, triage: the `ki-repo` standard defines the maturity scale and the `.ki.toml` key, proposed as `maturity` in `[skills.ki-repo]`; a rubric criterion checks it; the standard states how audit health maps to decline and ruin. The draft scale is marked as a proposal for Kris. Committed in ki-agentic-harness as `26ccb96b` (number reserved) and `d100fb4d` (record).
- [KI-TOOL-KI-CLI-159](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-159-island-maturity-and-health.md) Island maturity and health, triage: `ki` exposes each island's declared maturity and its audit-derived health, through `ki territory show` or `ki work status`. It depends on KI-HARNESS-GOV-223 as build order. Committed in tools-ki as `e7f716f5` (number reserved) and `395060ae` (record).
- Both records link [KI-OBSERVA-BCN-008](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BCN-008-beacon-signal-anatomy.md) and [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) at fixed pushed revisions, following the precedent in KI-HARNESS-GOV-219. I edited nothing in apps-observatory.local.
- Checks: the pre-commit hooks passed in both repositories. `ki repo audit --skill ki-work-roadmap` has FAIL=0 in both and no finding on either new record; the existing warnings are older records. I did not run `bun run test` or `bunx tsc --noEmit`, because the change is roadmap Markdown only.
- Limitation: CLI-159 links GOV-223 at harness commit `d100fb4d`, which is not pushed yet, so that one link resolves only after the harness is pushed.

## In Progress

Nothing is running. Nothing is pushed: ki-agentic-harness `main` has 2 unpushed commits and tools-ki `main` has 2, both on this laptop.

## Queries

### MATURITY-SCALE - Names for the island maturity scale

**Context:** KI-HARNESS-GOV-223 needs a fixed, ordered set of maturity levels that each island declares in `.ki.toml`. The draft builds on your words "settled" and "thriving". Decline and ruin are not levels on this scale, because they come from audit health.

**Query:** Which names should the maturity scale use?

**Options:**

a) (recommended, confidence medium - it keeps your two words at the top and gives younger islands two clear steps below them) `founding`, `growing`, `settled`, `thriving`
b) `founding`, `settled`, `thriving`: three levels, coarser but simpler to declare
c) `outpost`, `village`, `town`, `city`: a settlement-size metaphor that fits the islands theme but drops "settled" and "thriving"
