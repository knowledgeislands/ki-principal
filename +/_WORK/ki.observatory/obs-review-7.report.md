# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-review-7

**🤖 → 👤 Handoff to supervisor · Run report at 01:46 BST · last mark 22:50 BST**

---

## Done

Recommend **a)**: build [KI-OBSERVA-VIS-022](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-022-judge-overdue-against-each-job-schedule.md) as planned and request a tools-rig specification handoff alongside it, covering the existing encoding or an additive structured field.

**Confidence: high** - the declaration grammar constrains the observed encoding, and the explicit fallback preserves existing behaviour when parsing fails.

Plan check: the reviewed record matches commit `3b3c785` exactly.

Contract check: [RIG-STATE-033](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/state.md:357) promises complete declaration values; [RIG-CONF-016](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/configuration.md:153) specifies the input grammar. Neither specifies the schedule string's output encoding.

Renderer check: [the summary helper](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/30-commands.bash:1553) and [JSON projection](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/30-commands.bash:1816) confirm the context's description. No factual premise in the question is contradicted by the code. The fallback is planned Observatory behaviour, rather than behaviour supplied by Rig.

The plan's description of the entire source as a specified, stable contract overstates the encoding's status. [AGENTS.md](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/AGENTS.md:9) supports consuming machine contracts, but does not make an undocumented field encoding specified.

Read-only review completed; no repository files changed, no commits created, no tests or remote calls run.

## In Progress

Nothing is running. The supervising coordinator retains the build decision and any tools-rig handoff; neither was performed here.

## Queries

### RIG-SCHEDULE - Specify the encoding alongside delivery

**Context:** The JSON declaration and calendar grammar have specification coverage, while their string encoding has implementation evidence only. The planned strict parser and visible 26-hour fallback bound that compatibility risk. A structured field would strengthen the interface, but is not necessary to deliver this read-only improvement.

**Query:** Proceed with the build and request tools-rig specification work alongside it?

**Options:**

a) (recommended, confidence high - the visible fallback bounds the undocumented encoding dependency) Build as planned and hand off specification of the existing encoding or an additive structured field to tools-rig.

b) Hold until tools-rig supplies a structured, specified field; this delays the improvement beyond what the identified gap requires.

c) Read rendered launchd property lists; this adds platform-specific artefact coupling and still requires schedule interpretation.

### 🤖 → 👤 Handoff to supervisor · since 01:46 BST

👤 1 with you

- [with you] RIG-SCHEDULE · supervisor · since 01:46 BST
