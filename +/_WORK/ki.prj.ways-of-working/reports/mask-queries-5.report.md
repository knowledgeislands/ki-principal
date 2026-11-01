# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › mask-queries-5

**🤖 → 👤 Handoff to supervisor · Run report at 06:38 GMT · last mark 06:38 GMT**

---

## Done

- The brief named the six queries but not the output. I inferred it from the queued [blind-review-5 brief](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/briefs/blind-review-5.md) and the [fold-review-5 brief](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/briefs/fold-review-5.md), which both read `briefs/blind-review-5.packet.md`, and used the shape of mask-queries-4.
- Wrote the masked packet [blind-review-5.packet.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/briefs/blind-review-5.packet.md). It has six sections: LAYOUT-SHAPE, LAYOUT-GROUP-TIDY, LAYOUT-PILOT-ORDER, REVIEW-LIFT, READ-FEEDBACK-NOW and ORCH-NAME. Each copies the Context in full and the Query, and lists the options shuffled with no ranking.
- The options are numbered so that fold-review-5 can map each "packet option N" back by text. Every recommendation, confidence and reason is removed, and so is the earlier blind-review line on ORCH-NAME.
- In ORCH-NAME's options I also removed the ranking phrases "The review's strongest alternative" and "as the earlier recommendation did".
- Committed the packet alone by explicit path as 843d21db. The commit gate passed, and `main` is level with `origin`.
- Limitation: as before, each Context is copied in full. The ORCH-NAME Context still names the independent naming review's preferred set and its confidences, and says which alternative it placed second. That can anchor the reviewer. The REVIEW-LIFT Context mentions confidence only as the subject of the query.

## In Progress

Nothing is running.

## Queries

### ORCH-NAME-MASK - Neutralise the ORCH-NAME Context before the blind review

**Context:** The packet copies ORCH-NAME's Context in full, as earlier packets did. That Context is mostly the independent naming review's findings: its pick and confidence for each unit, its runner-up and its overall confidence of medium. A blind reviewer reading it is not independent of that review. The option lists are fully masked. The earlier MASK-CONTEXT query from mask-queries-4 raised the same issue and has no recorded answer.

**Query:** Should blind-review-5 run on the packet as committed, or after ORCH-NAME's Context is rewritten to give each naming unit's arguments without the review's picks and confidences?

**Options:**

a) (recommended, confidence medium - the other five Contexts are neutral already, and for ORCH-NAME the review's picks would otherwise be the reviewer's main input) Rewrite ORCH-NAME's Context to set out the arguments for each name without saying who preferred what or at what confidence, then launch blind-review-5.

b) Launch blind-review-5 on the packet as committed.
