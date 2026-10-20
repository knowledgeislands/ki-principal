# [Foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Baseline rollout](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/baseline-rollout.md) › review-checker-gaps

**🤖 → 👤 Handoff to supervisor · Run report at 23:55 BST · last mark 23:27 BST**

---

## Done

- Verified the [Streams checker](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-kb-streams/scripts/rubric/contexts/streams.ts:616) builds STREAM/GATE/CONFIG evidence without the roadmap configuration or issuing-area validation.
- Verified the [roadmap checker](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/scripts/rubric/contexts/roadmap-evidence.ts:360) rejects slug-valued area titles under ROAD-6 and checks record areas against declared areas at line 779.
- Parsed the affected declarations directly: [hnr-principal](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/.ki.toml) has six slug-valued titles, [tmx-principal](/Users/krisbrown/workspaces/techmedix/tmx-principal/.ki.toml) has two, and [va-principal](/Users/krisbrown/workspaces/valle-armonia/va-principal/.ki.toml) has no roadmap area declaration while its record filenames use GOV and KNW.
- Verified personal/dotfiles is a symlink to the chezmoi checkout; the [tools-ki selector](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/repository/selection.ts:49) reaches an [explicit symlink rejection](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/repository/location.ts:10), before realpath resolution.
- Verified [ki.baseline-rollout](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/work.md) excludes harness and CLI changes, [ki.ways-of-working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/work.md) owns method standards, and [ki.tools-burndown](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/work.md) owns CLI changes and the tools-ki writer.
- Verified the [current rollout state](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/state.md) records HOOKS-MIGRATION replacing HOOK-GUARD at 23:41 BST and retains the prohibition on running conform in these review runs.
- Read the query-review and owner-report rules; the original recommendation was exposed in the project's query file during evidence lookup, so this review was not fully blind.
- Read-only source review completed; no audit or conform executed, no network calls, no repository writes, and no commits or pushes.

## In Progress

Nothing is running.

Outstanding - no action requested now: the supervisor owns routing and any replacement blind review required because of the exposure above. Findings were checked statically; command behaviour was not reproduced. No handoff messages have been written.

## Queries

### CHECKER-GAPS - Report audit blind spots to the harness

**Context:** Direct source inspection confirms the Streams checker omits the issuing-area checks present in the roadmap adapter, and the affected repository declarations contain the reported examples. This is a coverage gap to assess against the Streams contract, which currently describes a limited structural floor. The dotfiles path is genuinely a symlink, and tools-ki explicitly requires a physical directory; accepting symlinks is therefore a contract decision, not an established bug fix. These changes belong outside this Project. HOOKS-MIGRATION supersedes HOOK-GUARD; routing these findings grants no implementation, migration or conform authority.

**Query:** Should these blind spots go to the harness and tools-ki as handoff items?

**Options:**

a) (recommended, confidence high - direct source checks confirm the findings and ownership; routing leaves design and delivery with the receivers) Route the two Streams checker gaps together to [ki.ways-of-working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/messages.md), and the symlink refusal to [ki.tools-burndown](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/messages.md), one messages.md line per receiver through territory work. Ask the receivers to assess checker coverage and symlink policy, with no presumption that symlinks must be accepted.

b) Note them in this Project only and take them up after the territory rollout.

### 🤖 → 👤 Handoff to supervisor · since 23:55 BST

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [with you] CHECKER-GAPS recommendation and review limitation · supervisor · since 23:55 BST
