# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-pies

**🤖 → 👤 Handoff to supervisor · Run report at 12:16 BST**

---

## Done

There are four Mermaid pies in two repositories. They are one pattern used twice: each email triage activity writes a pie into its status note from a template. No other repository under `~/workspaces` has a Mermaid pie. Nothing was changed or committed.

1. personal-principal, [Email Triage Status.md](/Users/krisbrown/workspaces/personal/personal-principal/Pillars/Productivity/Knowledge%20Management/KB%20Specifics/Email/Email%20Triage%20Status.md) line 31: `_TRIAGE` message counts for 11 folders, with a Folder, Count and Unread table beside it carrying the same counts. The table already says everything the pie does, and says it better. A sorted bar chart would read better than the pie, and one total figure would be enough for a glance.
2. personal-principal, [Re-route Triaged.md](/Users/krisbrown/workspaces/personal/personal-principal/Pillars/Productivity/Knowledge%20Management/Regular%20Activities/Email/Re-route%20Triaged.md) line 76: the template that tells each run to write item 1. It changes only if the output changes.
3. hnr-principal, [Email Status.md](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Admin/Knowledge%20Management/KB%20Specifics/Email/Email%20Status.md) line 33: the same chart for HNR with 18 folders, which is too many slices to compare. The table beside it carries the counts. A bar chart or the table alone does the job better.
4. hnr-principal, [Re-route Triaged.md](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Admin/Knowledge%20Management/Regular%20Activities/Email/Re-route%20Triaged.md) line 74: the template that writes item 3.

Not Mermaid, noted for completeness: hnr-principal's [HNR Email Pulse Artifact](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Admin/Knowledge%20Management/Integrations/Claude/Live%20Artifacts/HNR%20Email%20Pulse%20Artifact.md) draws an SVG pie to match item 3, and hnr-frontend's dashboard has a `Pie` widget type in code.

## In Progress

None

## Queries

### DIAGRAM-PIES - what to do with the email triage pies

**Context:** There are only two places, personal-principal and hnr-principal, each with a status note and the template that writes it. In both notes, the table beside the pie already holds the same counts. The HNR pie has 18 slices, too many to read. Archify has no pie type.

**Query:** Should the pies stay, be dropped in favour of the table, or become bar charts?

**Options:**

a) (recommended, confidence high - the table beside each pie already carries the same counts, and 11 to 18 slices are hard to read as a pie) Drop the pie from both templates and both notes, keep the table sorted by count, and add a one-line total of messages and unread. Each repository needs one triage record to change its template.

b) (confidence medium - keeps a picture at a glance) Replace each pie with a Mermaid `xychart-beta` bar chart sorted by count, generated from the same template.

c) (confidence low - leaves the hard-to-read HNR chart as it is) Keep both pies as Mermaid and leave them out of the Archify conversion.
