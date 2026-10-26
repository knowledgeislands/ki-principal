# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › gov197-hook

**🤖 → 👤 Handoff to supervisor · Run report at 19:13 BST · last mark 19:05 BST**

---

## Done

- [KI-HARNESS-GOV-197 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/95a1ab5818d2fb38b51af391cc3927ca5b1c6e9d/docs/roadmap/KI-HARNESS-GOV-197-pmo-7-outside-checkout-links.md) is planned and delivered, and now awaits review (commit `3fc59d87`, ki-agentic-harness). It stays inside the record's boundary.
  - COORD-7 still checks that a record link's file exists when the link points inside the audited checkout, or to a folder that exists on this machine.
  - Anywhere else, such as on a CI runner, it now checks only the link's shape: the target must be a Markdown file whose name starts with the record's identifier. A link with the wrong shape gets its own `misshapen` finding.
  - The tests were written first. The record also updates the linking rule in the standard, the COORD-7 description and the generated rubric.
- SCR-11 in `ki-engineering` now accepts `bunx lint-staged --quiet || exit 1` as the hook's first line, and CONFORM keeps that choice (commit `0a349e4e`, ki-agentic-harness). Tests were written first, and the standard says this in one sentence. The harness hook, which already used `--quiet`, now passes SCR-11.
- ki-principal's pre-commit hook has `--quiet` back, undoing `12ce215` (commit `6b6eb13`). Locally, `ki repo audit --skill ki-engineering` passes, SCR-11 included.
- Checks: `bun run test` passed (1260 tests). `bunx tsc --noEmit` passed. Both rubrics are in sync. The `ki-coordination`, `ki-skills` and `ki-engineering` audits pass in the harness. `ki-work-roadmap` fails only on [KI-HARNESS-GOV-210 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/218b8e3df7c67412382c34960cf4edfc3c7a9152/docs/roadmap/KI-HARNESS-GOV-210-work-model-write-in.md)'s Review section, which existed before this run.
- COORD-7 in ki-principal on this machine:
  - No `misshapen` findings.
  - 8 `missing` findings, all real. They are pruned records in other checkouts on this machine, linked from reports in the ki.chezmoi, ki.mac-studio-setup and ki.tools-burndown folders.
  - On a CI runner those links get the shape check and pass.
- Pushed fast-forward: ki-agentic-harness to `0a349e4e`, with only my commits stacked. ki-principal went to `4306e42`, which also carried the mark-tidy run's commit "docs(work): ki.tools-burndown tidy at mark" from ki.tools-burndown, stacked on top of mine.
- A grouping error: `6b6eb13` also contains 43 report deletions in `+/_WORK/ki.tools-burndown/`.
  - The mark-tidy run had already staged them when I committed. I committed without restricting the commit to my own path, so they were swept in.
  - The content is what that run meant to do, and its own commit followed straight after. I left the history as it is because the brief forbids resetting shared `main`.
  - Its work file was uncommitted at the time, so I did not write a Messages line to it.
- Net records: 0 in ki-agentic-harness ([KI-HARNESS-GOV-197 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/95a1ab5818d2fb38b51af391cc3927ca5b1c6e9d/docs/roadmap/KI-HARNESS-GOV-197-pmo-7-outside-checkout-links.md) moved from triage to awaiting review) and 0 in ki-principal.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- ki-principal CI picks up the COORD-7 change only once the next `ki` release pins this harness. The ki-release run is waiting for this report.
- At the time of the run, ki-principal had these untracked files from other sessions, all left alone: `+/_WORK/ki.chezmoi/mark-tidy-current.report.md`, `+/_WORK/ki.tools-burndown/briefs/mark-tidy.md`, `+/_WORK/ki.tools-burndown/briefs/mgit-prune.md`, `+/_WORK/ki.tools-burndown/mgit-prune.report.md` and `+/_WORK/ki.ways-of-working/mark-prune-3.report.md`.

## Queries

### GOV-197-ACCEPT - Review and accept [KI-HARNESS-GOV-197 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/95a1ab5818d2fb38b51af391cc3927ca5b1c6e9d/docs/roadmap/KI-HARNESS-GOV-197-pmo-7-outside-checkout-links.md)

**Context:** [KI-HARNESS-GOV-197 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/95a1ab5818d2fb38b51af391cc3927ca5b1c6e9d/docs/roadmap/KI-HARNESS-GOV-197-pmo-7-outside-checkout-links.md) is delivered, verified, and awaiting review in commit `3fc59d87`. Its author cannot accept it, and the pattern you approved for [KI-HARNESS-GOV-194 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f7982a616236486ac9c944671a636cfcf319b0c8/docs/roadmap/KI-HARNESS-GOV-194-review-verification-effects.md) and -201 was an independent review followed by acceptance with you.

**Query:** Should [KI-HARNESS-GOV-197 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/95a1ab5818d2fb38b51af391cc3927ca5b1c6e9d/docs/roadmap/KI-HARNESS-GOV-197-pmo-7-outside-checkout-links.md) get the same independent review and then acceptance?

**Options:**

a) (recommended, confidence high - it follows the review pattern you already approved and does not hold up the release) Have one review run check `3fc59d87` against the record, then accept it with you. The `ki` release can carry it in the meantime.

b) Accept it now on the evidence recorded in the record.
