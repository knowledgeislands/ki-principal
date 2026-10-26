# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › harness-followups

**🤖 → 🧑 Handoff to supervisor · Run report at 10:07 BST · last mark 10:06 BST**

---

## Done

- REPO-OWNERSHIP and COV-1 now share one record, [KI-HARNESS-GOV-212 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/406226abdd7d555db897c0d503041b48881d44ae/docs/roadmap/KI-HARNESS-GOV-212-work-area-ownership.md), which is built and awaiting review (6d349be3, 5527b917). ki-repo now names `+/_WORK/` and `+/_WORK_REVIEW/` and their owners, and either area counts as the ki-checkpoint coverage marker. `+/_CHECKPOINTS/` is still accepted, and it and `+/_THREADS/` each give one COV-1 warning that names the new home. In ki-principal, the "stale opt-in" warning has gone and only the expected `+/_THREADS/` warning remains.
- PMO-CODE is [KI-HARNESS-GOV-213 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/406226abdd7d555db897c0d503041b48881d44ae/docs/roadmap/KI-HARNESS-GOV-213-pmo-7-code-spans.md), built and awaiting review (a506075a, c42093de). PMO-7 now skips inline code spans, but a link whose label is a code span still has its target checked. `settle-model.report.md` in ki-principal is no longer flagged.
- MARK-RULE-SPLIT: the mark rule has moved to [KI-HARNESS-GOV-214 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-214-working-area-marks.md), a triage record that carries the field-name question below (e50ca40f). [KI-HARNESS-GOV-175 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/218b8e3df7c67412382c34960cf4edfc3c7a9152/docs/roadmap/KI-HARNESS-GOV-175-delegation-run-events.md) is now awaiting review, with a review packet for requirements 1 to 10 (402d8b4b, 0b95efbb).
- PMO12-LEVEL: the note is on [KI-HARNESS-GOV-175 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/218b8e3df7c67412382c34960cf4edfc3c7a9152/docs/roadmap/KI-HARNESS-GOV-175-delegation-run-events.md). The promotion to FAIL is captured as [KI-HARNESS-GOV-215 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-215-pmo-12-to-fail.md) (ad4bbf5b). The roadmap has no Later horizon, so "Later" is a draft on hold, waiting until the older work folders are pruned.
- IDENTITY-TIMING: Kris's words are on [KI-HARNESS-GOV-199 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-199-thread-identity-role-native-sessions.md), and the "may still move it to Phase 3" line is gone. Phase 3 waits on [KI-TOOL-KI-CLI-145](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-145-thread-session-bindings-role.md) and [KB-DOTFILES-UE-096 (pruned)](https://github.com/krisb/dotfiles/blob/2584fffb3a60f41fbe82e19be0ec5b27362ed410/docs/roadmap/KB-DOTFILES-UE-096-thread-identity-hook-registration.md) (73c227f2).
- UPDATE-SHAPE is captured, not built, as [KI-HARNESS-GOV-216 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-216-three-part-updates.md) at Soon, for the report-shape review around 21 October (d76d2485).
- RECORD-LINKS needs no harness record, because [KI-HARNESS-GOV-210 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/218b8e3df7c67412382c34960cf4edfc3c7a9152/docs/roadmap/KI-HARNESS-GOV-210-work-model-write-in.md) is done and the plan lives in the ki-principal migration brief. Eight records in mcp-m365, mcp-gsuite and tools-ki link into their own territories' `+/_THREADS/`. Each territory repoints its links when it migrates.
- One fix was needed outside the brief's items (d1ad2722). The ki-delegation rubric never showed as current, because the Markdown fixer stripped a leading space that RUN-4's source puts in a code span. The source now drops that space.
- The ledger was advanced to 216 earlier (4cae8271, pushed then). All eleven commits since were mine; they were pulled with rebase and pushed fast-forward. No other session's commits were stacked, and origin had not moved.
- Checks:
  - `bun run test` passes, 1253 tests.
  - `bunx tsc --noEmit` passes.
  - The ki-repo, ki-checkpoint, ki-pmo, ki-delegation, ki-authoring and ki-work-roadmap audits pass.
  - The ki-skills audit has no failures and the same three LONG-3 warnings as before.
  - The rubrics for ki-repo, ki-pmo, ki-delegation and ki-checkpoint are current, and the generated surfaces for ki-pmo are in sync.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Records [KI-HARNESS-GOV-212 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/406226abdd7d555db897c0d503041b48881d44ae/docs/roadmap/KI-HARNESS-GOV-212-work-area-ownership.md), [KI-HARNESS-GOV-213 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/406226abdd7d555db897c0d503041b48881d44ae/docs/roadmap/KI-HARNESS-GOV-213-pmo-7-code-spans.md) and [KI-HARNESS-GOV-175 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/218b8e3df7c67412382c34960cf4edfc3c7a9152/docs/roadmap/KI-HARNESS-GOV-175-delegation-run-events.md) need an independent review before acceptance. None of them was accepted.
- The new checks reach other repositories only when `ki` loads the harness's updated catalogue. Nothing was released.
- Findings in ki-principal outside this change:
  - Its ki-repo audit fails the Markdown mechanical gate because of its own working tree.
  - Its ki-pmo audit still reports bare record identifiers in reports across other work folders.
  - `check-pass.report.md` writes one decision identifier bare in prose. That is a true PMO-7 finding, not a code span.

## Queries

### [KI-HARNESS-GOV-214 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-214-working-area-marks.md) - names for the working-area mark

**Context:** The mark rule moved to [KI-HARNESS-GOV-214 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-214-working-area-marks.md). It says every file written into a `+/` working area records who wrote it and when. It cannot be planned until three names are settled:

1. Whether an interactive session writes `session` where a background run writes `run` and `agent`, or one `writer` field covers both.
2. Whether the field naming the unit is `work`, as in the work model, or `thread`, as in the two hand-written sidecars.
3. Whether a folder's sidecar is `mark.toml` or a Markdown file holding only front matter.

**Query:** Which names should the mark use?

**Options:**

a) (recommended, confidence medium - this matches the work model and the existing sidecars, and a reader can tell whom to ask) Use `work`, with `run` and `agent` for a background run and `session` for an interactive one, and keep `mark.toml` as the sidecar.

b) Use `work` with a single `writer` field for both kinds of writer, and keep `mark.toml`.

c) Use `work`, `run`, `agent` and `session`, with a front-matter-only `mark.md` sidecar so that every mark is Markdown front matter.
