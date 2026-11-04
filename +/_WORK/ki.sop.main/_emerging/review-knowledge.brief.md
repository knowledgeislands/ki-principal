# review-knowledge (blind review)

Independent review: you have not seen anyone's recommendation; give your own for each. Do not read any `discussions.md`, `decisions.md`, `*.report.md` or `*.design.md` in a `+/_WORK/` folder. You may read the proposal at /Users/krisbrown/kis/personal/assistant/+/_WORK/personal.reg.assistant-terra/capture/knowledge-folder.proposal.md and ki-principal's AGENTS.md and Structure note. Background as dated facts: on 4 November Kris asked Knowledge Islands Principal to take on a top-level `knowledge/` semantic graph replacing `Pillars/` over time, and agreed layered graphs: each repository keeps its own graph, declares attachment points others may pin to, and others bring them in as read-only shadow nodes.

## ATTACH-HOW - how an attachment point is declared

**Context:** An attachment point is a node this island promises not to move, so that other graphs, starting with the assistant's, can pin read-only shadow copies to it. The proposal leaves open where that promise is recorded.

**Query:** How should a node be marked as an attachment point, and what should it promise?

**Options (unranked):**

- A separate register file listing the attachment points, with nothing on the nodes themselves.

- A front matter flag `attachment: true`, listed on `knowledge/_index.md`, promising a stable id and path and retirement by pointer rather than deletion. Shadow nodes record `shadows:` (path and revision read) and `checked:` (date).

## ATTACH-SET - the first attachment points

**Context:** These are the nodes the assistant can pin to straight away.

**Query:** Which nodes should be the first attachment points?

**Options (unranked):**

- None until the first slice has settled.

- The capture funnel, the knowledge graph, and the work process once it is pulled across.

## RESOURCES-IN - Resources in other territories' graphs

**Context:** Here Resources stays outside `knowledge/`, because the island strictly enforces the split between its own knowledge and outside reference.

**Query:** May another territory bring its Resources into its graph?

**Options (unranked):**

- Yes, as each territory chooses.

- No for now. Revisit when a territory asks.

For each: your choice, confidence and a two-line reason. Read-only; no commits. Write it as your run report.
