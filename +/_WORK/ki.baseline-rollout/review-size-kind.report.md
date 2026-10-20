# [Foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Baseline rollout](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/baseline-rollout.md) › review-size-kind

**🤖 → 👤 Handoff to supervisor · Run report at 23:52 BST · last mark 23:27 BST**

---

## Done

- Recounted frontmatter in the 28 registered rollout repositories: the query's 191 missing sizes across 18 repositories and 61 missing adopted kinds are correct; done and cancelled records were excluded.
- Checked the six largest gaps directly: personal-principal 33, legal-principal 28, er-agentic-harness 22, hnr-principal 20, dotfiles 16 and apps-vallearmonia.com 15; all 22 er-agentic-harness records also lack kind.
- Verified four open dotfiles records retain `initiative`; the [migration rule](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/.agents/skills/ki-work-roadmap/references/standards-repository-roadmaps.md:198) treats its replacement as mechanical.
- Verified [size and kind meanings](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/.agents/skills/ki-work-roadmap/references/standards-work-item-format.md:102): size covers end-to-end effort including owner review; kind classifies the controlling outcome, so neither can be assigned mechanically.
- Verified [migration authority](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-016-priority-and-size-on-work-records.md:40): each repository needs owner approval, with proposed size and kind confirmed before writing.
- Corrected the deadline qualification from the [migration rule](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-016-priority-and-size-on-work-records.md:38): the backstop is 60 days after the accepting `ki` release, and a clean closure scan covers every registered repository with records; unavailable repositories remain unknown.
- Confirmed [HOOKS-MIGRATION](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/state.md) supersedes HOOK-GUARD; no conformance command, network call, repository write, commit or push was performed.
- Review limitation: the source sweep report exposed its original recommendation during evidence inspection; this report must not be counted as a fully blind review or used to lift confidence under the blind-review rule.

## In Progress

Nothing is running.

Outstanding - no action requested now: the coordinator must obtain an unexposed reviewer if it needs the prescribed blind-review confidence lift. Before any later write run, verify that the repository's installed `ki` accepts the fields and that the hook migration leaves its commit path ready; this review did not verify those prerequisites.

## Queries

### SIZE-KIND - Backfill size and kind

**Context:** Direct reading confirms 191 open records without size across 18 repositories and 61 adopted open records without kind. The standard requires judgement and owner confirmation, one repository at a time; closed records are exempt. The field window was set on 19 October and closes at the earlier of a complete gap-free scan of every registered repository with records or 60 days after the accepting `ki` release. Territory-sized proposal runs can organise the reading, but confirmation and writing must remain repository-specific. Dotfiles remains owned by ki.chezmoi. HOOKS-MIGRATION replaces HOOK-GUARD; the later write briefs must retain the conformance restriction until ki.tools-burndown explicitly changes it.

**Query:** How should the size and kind backfill run?

**Options:**

a) (recommended, confidence high - direct counts and the migration rule support bounded proposals with explicit repository confirmation) Run one read-only proposal pass per territory, with a separate table per repository showing each record, proposed size and kind, and a short reason or unresolved uncertainty. Obtain your confirmation per repository, then run one approved write pass per repository, including the four mechanical dotfiles `initiative` replacements through ki.chezmoi. Verify field acceptance and hook readiness before writing; do not run `ki repo conform` under these review runs.

b) Leave backfill to each repository's next planning pass, accepting that untouched records become failures when the window closes, potentially before the backstop if a complete clean scan closes it.

### 🤖 → 👤 Handoff to supervisor · since 23:52 BST

👤 1 with you · 🅿️ 0 parked

- [with you] SIZE-KIND recommendation and review limitation · supervisor · since 23:52 BST
