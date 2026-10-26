# [Foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Baseline rollout](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/baseline-rollout.md) › va-plan

**🤖 → 👤 Handoff to supervisor · Run report at 00:09 BST · last mark 23:56 BST**

---

## Done

- [apps-vallearmonia.com](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com): commit `f0087d7` (`docs(roadmap): shape four drafts and repair the VA-WEBSITE-SITE-003 review packet`), local, not pushed, five records only; the commit gate passed, rumdl passed on all five, and the roadmap audit now has no failures, down from 7 (26 size and kind warnings are left for SIZE-KIND).
  - [VA-WEBSITE-CONT-005](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-CONT-005-resolve-image-review-flags.md): got Current state, Files touched, Dependencies / blocks and Documentation impact, plus a Verify command; still a draft. The sidecars show 25 of 31 flagged images are on pages. The third-party photos are on five pages, not only Paid Guests as the old Context table said.
  - [VA-WEBSITE-SANC-009](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-009-close-the-editorial-audit.md): got the same sections; still a draft. The audit itself is a Claude doc private to Kit, so this repository cannot show which commit fixed each finding.
  - [VA-WEBSITE-SANC-008](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-008-package-the-sanctuary.md): got the same sections and a Size topic in its Discussion; still a draft. Only stage 1 has shipped. The image store in the ADR is not assigned to any stage.
  - [VA-WEBSITE-SITE-004](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SITE-004-choose-the-home-page-layout.md): got the same sections plus Steps and Verify for the decision; still a draft.
  - [VA-WEBSITE-SITE-003](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SITE-003-consolidate-the-design-system.md): repaired and still awaiting review. Current state, Files touched, Dependencies / blocks, Change Summary, Post-change review, Mini recap and a final Discussion were added from baseline `f3118f5` and delivery commits `a91c77d`, `6bafac3` and `e186f6b`. The repository confirms the 50 colour literals and Google Fonts at baseline, and the 29 JPEG banner copies the record claims. The token guard test passed 26 of 26 at today's HEAD. Not recoverable: the delivery-time results for the unit tests (1,344), end-to-end tests (58 of 58) and screenshots were never committed, so they cannot be checked. The record now says so.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- All five records still lack `size`, and [VA-WEBSITE-CONT-005](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-CONT-005-resolve-image-review-flags.md) and [VA-WEBSITE-SANC-009](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-009-close-the-editorial-audit.md) also lack `kind`. The read-only SIZE-KIND run covers these, so this run did not set them.
- `f0087d7` is unpushed in apps-vallearmonia.com.

## Queries

### SITE003-CONCERN - Give the Sanctuary style gap its own record

**Context:** Under Outstanding concerns, [VA-WEBSITE-SITE-003](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SITE-003-consolidate-the-design-system.md) notes that the Sanctuary's `.webc` styles are outside the SITE-RT-033 token guard. The roadmap standard says such a concern needs its own identifier before acceptance, because the concern disappears when the record is pruned. No record carries it today.

**Query:** Should a triage record be captured in apps-vallearmonia.com to extend the token guard to Sanctuary `.webc` styles before [VA-WEBSITE-SITE-003](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SITE-003-consolidate-the-design-system.md) is accepted?

**Options:** a) (recommended, confidence high - capture is unadopted and reversible, and the standard requires an identifier before acceptance) Capture one triage record through `ki-next` and cite it in [VA-WEBSITE-SITE-003](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SITE-003-consolidate-the-design-system.md)'s Outstanding concerns. b) Accept [VA-WEBSITE-SITE-003](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SITE-003-consolidate-the-design-system.md) with the gap recorded as an accepted risk and no follow-on record.

### SANC008-SPLIT - Split stage 4 out of the Sanctuary packaging record

**Context:** [VA-WEBSITE-SANC-008](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-008-package-the-sanctuary.md) covers stages 2 to 4 of [ADR-VA-WEBSITE-009](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/decisions/ADR-VA-WEBSITE-009-the-sanctuary-becomes-a-shared-editorial-library.md), which means three chained runs. Stage 4 alone moves 21 components and their test suites into `packages/sanctuary/` and changes the root workspaces, `turbo.json` and `bun.lock`. A record needing several chained runs needs a Delegation section, and an `xl` record cannot become Ready.

**Query:** Before [VA-WEBSITE-SANC-008](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-008-package-the-sanctuary.md) becomes Ready, should stage 4 be split into its own record?

**Options:** a) (recommended, confidence medium - stage 4 differs in kind and risk from stages 2 and 3, but how big it is depends on how the tests move) Split stage 4 into a new record that [VA-WEBSITE-SANC-008](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-008-package-the-sanctuary.md) blocks, and keep stages 2 and 3 here. b) Keep all three stages in one record at size `l`, with a Delegation section giving one run per stage.

### VA-READY - Which plans to approve as Ready

**Context:** All four drafts now have every planning section, but none has `size` yet. [VA-WEBSITE-CONT-005](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-CONT-005-resolve-image-review-flags.md) and [VA-WEBSITE-SITE-004](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SITE-004-choose-the-home-page-layout.md) are concrete and checkable. [VA-WEBSITE-SANC-009](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-009-close-the-editorial-audit.md) needs access to Kit's private audit doc. [VA-WEBSITE-SANC-008](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-008-package-the-sanctuary.md) waits on SANC008-SPLIT.

**Query:** Which of the four drafts should be approved to Ready, and when?

**Options:** a) (recommended, confidence medium - the plans are complete, but size must be settled before Ready and each step needs Kit's input) Once SIZE-KIND has set `size` and `kind`, approve [VA-WEBSITE-CONT-005](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-CONT-005-resolve-image-review-flags.md) and [VA-WEBSITE-SITE-004](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SITE-004-choose-the-home-page-layout.md). Approve [VA-WEBSITE-SANC-009](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-009-close-the-editorial-audit.md) once Kit's audit doc is reachable, and [VA-WEBSITE-SANC-008](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-008-package-the-sanctuary.md) after SANC008-SPLIT. b) Keep all four in draft until each is next selected for delivery.

### 🤖 → 👤 Handoff to supervisor · since 00:09 BST

👤 3 with you

- [with you] SITE003-CONCERN · owner · since 00:09
- [with you] SANC008-SPLIT · owner · since 00:09
- [with you] VA-READY · owner · since 00:09
- [committed] apps-vallearmonia.com five roadmap records
- [unpushed] apps-vallearmonia.com
