# Context efficiency: bounded proposal

Draft for review, 27 October 2026, 05:50 GMT. No implementation or method change is authorised by this note. The brief explicitly authorises this working-area note; package state, queries, decisions, canonical content and runtime configuration remain outside this run.

## Recommendation

The full-read requirement dominates. Keep ordinary pick-ups change-only under the existing PICKUP-READS rule, and use the next owner-instructed mark to consolidate the decisions log under its existing guards. Do not manufacture a mark, abbreviate re-anchoring or add a cache. If an independently deliverable prose reduction is wanted, remove the duplicated origin quotation from the output-style source, retaining the original quotation and every operative rule. Its saving is real but tiny: 562 bytes per full re-anchor, about 0.13%. Do not present it as the solution to context pressure.

## Measured inputs

Physical UTF-8 bytes and newline counts from the primary checkouts at 05:50 GMT; these are file measurements, not loaded-session, provider, billing or cache metrics. No appropriate pre-existing Python tiktoken module or tiktoken executable was found; no token estimate is claimed. Live packages can change after this snapshot.

| Input | Bytes | Lines |
| --- | ---: | ---: |
| Package work.md | 1,508 | 28 |
| Package state.md | 2,808 | 36 |
| Package queries.md | 11,752 | 84 |
| Package messages.md | 30 | 1 |
| Package decisions.md | 166,331 | 905 |
| Five-file package | 182,429 | 1,054 |
| Coordination standard | 214,629 | 1,107 |
| Delegation background-run standard | 48,662 | 296 |
| Work-package standard | 47,416 | 433 |
| Generated coordinator style | 26,073 | 114 |
| All nine files | 519,209 | 3,004 |

Package paths are under `+/_WORK/ki.ways-of-working/`. Harness paths below are relative to `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/`:

- Coordination: `skills/change-management/ki-coordination/references/standards-coordination.md`.
- Delegation: `skills/governance/ki-delegation/references/standards-background-runs.md`.
- Package: `skills/governance/ki-work-package/references/standards-work-package.md`.
- Style: `output-styles/ki-coordinator.md`.

The coordination standard's Re-anchoring after compaction section, lines 377-391, requires the whole coordination standard, disk style and all five package files: 423,131 bytes, 2,275 lines, before open findings, inbox or status. The other two standards add 96,078 bytes if also read for method refresh; they are not automatically added to every compaction read by that paragraph. The decisions log alone is 39.3% of the minimum file-read payload; the coordination standard is 50.7%. Instructions already loaded by a runtime are additional and cannot be measured or changed by this filesystem audit.

Section analysis used exact heading positions and byte slices, not old transcripts. queries.md has an empty Open section, 15 bytes at lines 3-6, and Parked, 11,707 bytes at lines 7-84: parked material is still required by a full-file read. decisions.md has 79 level-two entries; its two largest heading spans are lines 377-704, 75,464 bytes, and 715-905, 35,804 bytes. Those spans include lower-level entries and operational history; size does not establish disposability or supersession. No grant or decision was reclassified by this audit. state.md and messages.md together cost only 2,838 bytes, so reducing current work or responsiveness information offers little benefit.

## Duplication and authority

Generated surfaces are embedded inside the coordination standard. Its Generated surfaces section occupies lines 578-694, 33,222 bytes, counting fenced content correctly; the output-style source body itself is 24,718 bytes over 74 lines, including a Banner heading inside that source block. The generator replaces four banner-example tokens, producing the 26,073-byte style. Across the standard and style, 25 paragraph occurrences match exactly, totalling 24,198 bytes excluding separators. This is source-to-projection overlap, not permission to omit either required read. Counts must not be added as independent possible savings.

The source-to-generated relationship is implemented by `skills/change-management/ki-coordination/scripts/generate/index.ts`: marked source blocks render the style, hook line and compaction pointer in `hooks/coordinator-reminder.sh`, the Report paragraph in `skills/governance/ki-delegation/assets/run-prompt.md`, and the report rule in assets `rules-none.md`, `rules-push.md`, `rules-prune.md` and `rules-release.md`. These are intentional delivery surfaces. Edit their source, never a deployed or generated copy. A note-only audit cannot remove instructions already loaded into this session or guarantee a future runtime loads less.

There is also a genuinely redundant 279-byte origin quotation at standard lines 95 and 638, reproduced at style line 20. Byte-level paragraph comparison establishes two identical source occurrences and one style occurrence. The quotation explains delegation and non-pre-emption; operative rules remain independently stated. Removing only the second quotation plus its blank separator saves 281 bytes in the source and 281 in the generated style, without changing behaviour.

The existing ordinary pick-up rule at coordination line 1042 already permits changed files and relevant entries after bootstrap. The work-package Progressive reveal footnote at lines 328-342 lists the four pick-up files and open findings at each wake or owner message; it is broader wording. Follow coordination's explicit read-count and changed-input qualification together with the package contract. Do not infer that this permits skipping full reads at bootstrap or compaction. If future wording is harmonised, preserve this exception explicitly rather than silently granting a new delta-only re-anchor.

Decisions life cycle, coordination lines 900-905, checks the log at each mark: strike entries wholly carried by a durable home, reduce still-live decisions homed elsewhere to dated tagged links, retain the rest. Work-package Tidying, lines 122-134, and coordination Pruning the work folder distinguish report/brief disposal at receive/send from decisions-log consolidation at the mark. Deleting homed reports can shrink on-demand material, but cannot shrink this minimum five-file input if their content has accumulated in decisions.md. The recorded mark is 25 October 2026 at 01:07 UTC; elapsed history is not authority to tidy the log now. A mark never removes unresolved queries or active authority merely to meet a budget.

## Small independent delivery

A later prose-only unit could edit exactly the coordination standard's `source output-style` block to remove its duplicate origin quotation, leaving the scope quotation, all three operative coordinator rules, re-anchor requirement, report shape, mark, approval and acceptance rules intact. Regenerate with `ki dev skill generate ki-coordination --write`; expected changed paths are only that standard and `output-styles/ki-coordinator.md`. The generator's other outputs named above must remain byte-identical. No runtime deployment, configuration, model, permission or package mutation belongs to that unit.

Verify the duplicate paragraph with exact bytes before editing; compare the two-file diff for removal of only the quotation and separator; check rendered surfaces with `ki dev skill generate ki-coordination`; run the focused `skills/change-management/ki-coordination/scripts/banner.test.ts` checks and the harness's required sequential verification under its own authority. Confirm the source and style each shrink by 281 bytes, other generated files do not change, and instructions preserving authority, current decisions, queries, active work and responsiveness still exist. Stage only the completed named paths. This run performs none of that implementation or those harness checks.

A larger reduction requires either the already-governed mark consolidation, whose safely removable bytes need entry-by-entry durable-home verification, or an explicit owner decision to alter full re-anchoring. The latter would affect the standard's Re-anchoring section, its generated hook-pointer and output-style source blocks and corresponding generated hook/style, plus any conflicting bootstrap or package guidance. It requires a separate approved plan preserving decision provenance, all open and parked queries, active grants, live work, inbox/status checks and responsiveness. No hash manifest, summary cache, new tool or speculative machinery is proposed. No new owner query is needed to receive this proposal.
