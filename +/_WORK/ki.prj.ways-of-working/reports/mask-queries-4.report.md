# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › mask-queries-4

**🤖 → 👤 Handoff to supervisor · Run report at 06:31 GMT · last mark 06:31 GMT**

---

## Done

- Wrote the masked packet [blind-review-4.packet.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/briefs/blind-review-4.packet.md) with four sections: WORKER-WAIT-GATED, HOST-CADENCE, HOST-COVERAGE and HOST-READBACK; options listed unranked in shuffled order with every recommendation, confidence and reason stripped; the ADR link in HOST-COVERAGE repointed for the `briefs/` folder.
- Excluded HOST-SECONDARY-PUBLISH, PUBLIC-REPORT-AUDIENCE and PUBLIC-REPORT-RECOVERY because their recommendations are already high confidence.
- Committed the packet alone by explicit path as d5af8677; the commit gate passed and `main` is level with `origin`.
- Limitation: as the brief asked, each Context is copied in full. The HOST-CADENCE, HOST-COVERAGE and HOST-READBACK Contexts still name the Claude and Codex design reviewers' preferred courses and confidences, and HOST-CADENCE and HOST-READBACK mention an earlier blind review. A reviewer reading them is not fully blind to those views.

## In Progress

Nothing is running.

## Queries

### MASK-CONTEXT - Strip reviewer views from the packet Contexts

**Context:** Three of the packet's Contexts, copied in full as the brief required, say which course the Claude and Codex design reviewers preferred and at what confidence, and two also mention an earlier blind review's view. That can anchor the blind reviewer. The packet's option lists themselves are fully masked.

**Query:** Should the packet be sent as committed, or revised first to neutralise the reviewer views in those Contexts?

**Options:**

a) (recommended, confidence medium - the reviewers' views are evidence the owner weighs, but a blind review is meant to be independent of them) Revise the three Contexts to state the disagreement's substance, the arguments on each side, without saying who recommended what or at what confidence, then launch the review.

b) Send the packet as committed, accepting that the reviewer sees the earlier views.
