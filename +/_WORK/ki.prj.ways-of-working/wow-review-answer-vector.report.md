# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-review-answer-vector

**🤖 → 👤 Handoff to supervisor · Run report at 22:47 GMT · last mark 25 October 01:07 GMT**

---

## Done

### ANSWER-VECTOR - wait for the command

**Pick:** Wait for tools-ki to provide `ki work answer`, and declare that vector in the Observatory's first slice.

**Confidence:** Medium.

**Reason:** Centralising answer validation, message composition and repository effects in the command avoids a temporary second implementation; the existing feedback effect proves the mechanism, not an answer contract.

**Verified or refuted claims:**

- Verified: the Observatory already declares a backend file effect and an explicit-path Git commit in [feedback.ts](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/feedback.ts:367). Its [tests](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/feedback.test.ts:278) cover messages.md writes, preserving work.md, queue order, refusal and restoration. This was source inspection; tests were not executed.
- Verified: the Observatory's [working contract](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/AGENTS.md:8) favours stable ki contracts. The [tools-ki engineering standard](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/.agents/skills/ki-self/references/standards-product-engineering.md:7) assigns validation, transactions and repository effects to the command host. Its [work command registration](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/commands/work/index.ts:49) currently offers status, with neither answer nor queries. Waiting therefore introduces a real tools-ki dependency; an exact future pin and migration are prospective, not verified deliveries.
- Material qualification: [OBS-ACT-014](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/specs/authority.md:139) describes feedback specifically, and [FEEDBACK_SENDING](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/contracts/src/feedback.ts:29) remains false. [KI-OBSERVA-BRG-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-004-turn-feedback-sending-on.md) remains draft/on hold, although its cited harness prerequisite is now present in the standard. An implemented and tested path is not an enabled operation.
- Material qualification: the [work-package entry points](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md:95) permit the owner through the Observatory to commit a feedback package and its linking message together. They do not grant a standalone answer-line write. Either option needs that authority settled explicitly; introducing a command alone does not grant it.
- No literal Context claim was refuted. Reusing the generic effect could avoid a tools-ki change, but it still requires new answer-specific implementation, specification and authority. No KI-OBSERVA-INT-005 record exists in the current roadmap; the option correctly presents its capture as future work. The preference for commands is not an absolute prohibition on local effects, which limits confidence in choosing to wait.

Read-only review completed; no repository files changed, no commits made and no remote calls performed. The excluded files were not read.

## In Progress

Nothing.

## Queries

None.

---

### 🤖 → 👤 Handoff to supervisor · since 22:47 GMT

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [with you] ANSWER-VECTOR review complete · supervisor · since 22:47 GMT

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
