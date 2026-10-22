# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › harness-upkeep

**🤖 → 🧑 Handoff to supervisor · Run report at 11:35 BST · last mark 11:06 BST**

---

## Done

- [KI-HARNESS-GOV-194](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-194-review-verification-effects.md) is finished and returned as Awaiting review. Before running anything, the run checked what each verification command touches; every check is local, with no network call, registry lookup or state change. Both open steps are ticked and the six-part review packet is written. The two checklist items are the only change to their section since the baseline. Commit `d0f12879`, pushed.
- KI-HARNESS-GOV-194 checks: `bun run test` passed (1253 tests, no failures); `bunx --no-install tsc --noEmit` passed; the ki-work, ki-work-roadmap, ki-trades, ki-skills and ki-authoring audits all passed with no failures or warnings.
- Model radar: the watch items now say that the next weekly refresh adds Claude Haiku 5.5 (`claude-haiku-5-5`) as a model with no route, and that Haiku 4.5 stays on the radar until it retires. They also say the Astra launch post stays retired and should be re-added when it can be fetched. ki-repo-mcp's review note records that the NSA/CISA MCP sheet stays retired. Commit `cbe77385`, pushed. Tests, type check, and the ki-model-radar and ki-skills audits passed with no warnings.
- [KI-HARNESS-GOV-201](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-201-fetch-and-machine-grants.md) is adopted, delivered and returned as Awaiting review:
  - The "Draft, not approved" lines are removed, and the wording of both grants is exactly as you approved it.
  - The background-run standard now has a Grants subsection under Authority tiers, and its prompt-shape rules let grant sections follow the footer.
  - The record asked for rubric coverage, so RUN-1 and its tests now check that each grant exists, is approved, lifts only its own ban and carries no tier grant. The rubric catalogue was regenerated.
  - Commit `ef9d275f`, pushed.
- KI-HARNESS-GOV-201 checks: `bun run test` passed (1254 tests, no failures); the type check passed; the rubric catalogue is in sync; the ki-delegation, ki-skills, ki-authoring, ki-work-roadmap and ki-coordination audits all passed with no warnings.
- [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md) now has a concrete handoff in its Dependencies section. It records that the grants are on harness `main` at `ef9d275f` and gives the grant names. It explains how to cut each grant section out of its file: start at its `## Grant: <name>` heading, not at `## Rules`. It says to append the grants after the tier footer in the order given to `--allow`, and that the harness's interim hand-append rule can go once the option ships. Commit `33964078` in tools-ki, pushed. The ki-work-roadmap audit passed.
- Every push carried only this run's commits. No other session's commit was beneath them, and the working trees were clean before and after.
- Records opened: none in either repository. ki-agentic-harness still has 2 open records from this run (KI-HARNESS-GOV-194 and KI-HARNESS-GOV-201, both Awaiting review), and tools-ki still has 1 (KI-TOOL-KI-CLI-134, In progress).
- Report path: this report is written only to the state-folder path, because the launch protocol says that path is the only one. The launcher copies it into the work folder.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Building `ki agent launch --allow <grant>` belongs to KI-TOOL-KI-CLI-134 in tools-ki, and nothing here blocks it any more.
- The weekly ki-model-radar refresh will add Haiku 5.5. This run added no model to the radar data itself.

## Queries

### GRANT-INTERIM - Hand-appended grants until `--allow` ships

**Context:** You approved the two grant texts. Until tools-ki builds `ki agent launch --allow`, though, no launcher can append them. This run added one sentence to the standard's Grants subsection: until the launcher offers the option, a brief appends the grant section by hand after its footer. That sentence is this run's own addition, not part of the approved texts. Without it, an approved grant cannot be used until KI-TOOL-KI-CLI-134 ships.

**Query:** Should briefs be allowed to append a grant section by hand until `--allow` exists?

**Options:** a) (recommended, confidence medium - it only uses wording you have already approved, unchanged, and the KI-TOOL-KI-CLI-134 handoff already says to remove the sentence) Keep the interim sentence, and remove it when `--allow` ships. b) Strike the sentence, so that grants take effect only through the launcher.

### REVIEW-GOV-194-201 - Two harness records awaiting review

**Context:** KI-HARNESS-GOV-194 (the two checklist items on checking what verification commands touch) and KI-HARNESS-GOV-201 (the fetch and machine grants) are both Awaiting review. Each has its six-part review packet, and every check passed. Accepting them needs an independent review and your approval under `ki-accept`.

**Query:** Should a review run check both records and bring them to you for acceptance?

**Options:** a) (recommended, confidence high - both are small and fully checked, and acceptance stays with you) Queue one independent harness review run for both records, which reports back for your acceptance. b) Review them yourself later.

### 🤖 → 🧑 Handoff to supervisor · since 11:35 BST

🧑 2 with you

- [with you] GRANT-INTERIM · owner · since 11:35
- [with you] REVIEW-GOV-194-201 · owner · since 11:35
- [committed] ki-agentic-harness and tools-ki, pushed
