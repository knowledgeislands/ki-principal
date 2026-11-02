# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › withdraw-adr-007

**🤖 → 👤 Handoff to supervisor · Run report at 14:22 GMT · last mark 14:22 GMT**

---

## Done

- ADR-KI-PRINCIPAL-007 (territory seats on hosts) is removed from ki-principal in commit `e53abb63`. The Decision Records standard handles a withdrawn record by deleting it rather than marking it with a status. It was the last record in its series, so no other records needed renumbering. Its entry is gone from [Decisions](/Users/krisbrown/kis/knowledge-islands/ki-principal/Admin/Governance/Decisions/Decisions.md).
- [Known Lands](</Users/krisbrown/kis/knowledge-islands/ki-principal/Admin/Governance/Known Lands.md>) no longer has a Seat column. Its text now says that which machine looks after each territory is personal Rig setup, kept in chezmoi's `.chezmoidata/rigs.yaml`, not Knowledge Islands governance.
- [Host network](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/host-network.md) has a new dated note, "Seats withdrawn, 2026-11-01", quoting Kris. Its earlier seat notes stay as history, without links to the removed record.
- [Paperclip capture and rebuild](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/paperclip-capture-and-rebuild.md) and [Known World](</Users/krisbrown/kis/knowledge-islands/ki-principal/Pillars/Philosophy/Emerging Concepts/Known World.md>) now point to rigs.yaml. Known World's Seat entry now says seats are not Knowledge Islands governance and quotes Kris.
- The [Observatory away-sync review](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.observatory/sync/away-sync-query-review.report.md) now treats seats as personal Rig setup and links to rigs.yaml instead of the old seats.yaml.
- In the five ways-of-working host-sync design notes, the links to the record now go to its last copy on GitHub, labelled "withdrawn".
- Checks: the Decision Records audit passed with no failures. Its 6 warnings were already there before this change and concern the order of other records in the index. The commit checks passed, and no other repository file still links to the removed record.
- I added one line to [personal.reg.household-terra messages](/Users/krisbrown/.local/share/chezmoi/+/_WORK/personal.reg.household-terra/messages.md) in the chezmoi source, saying the work is done and citing `e53abb63`.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Another session has a file that is not yet in Git, [blind-review-stocktake.report.md](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.observatory/blind-review-stocktake.report.md), which still mentions ADR-KI-PRINCIPAL-007. I left it alone.
- The [ways-of-working decisions log](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/decisions.md) still names the record in its past entries. That is history, and I did not edit it.

## Queries

### PEER-CITE - Clear the seat reference in ki-design

**Context:** One reference to ADR-KI-PRINCIPAL-007 sits in another repository: [concept-atlas.md](/Users/krisbrown/kis/knowledge-islands/ki-design/docs/briefs/concept-atlas.md) in ki-design. It lists "Seat, standby" as a map concept and gives the withdrawn record as its source. The Decision Records standard says references in peer repositories should be cleared at the same time. This run could only write to ki-principal and the household's message queue, so it left that file alone.

**Query:** How should the ki-design reference be cleared?

**Options:**

a) (recommended, confidence medium - this follows the agreed rule that work passes between repositories as messages, but it has not been through a blind review) The ways-of-working coordinator sends one line to ki-design's work queue. The line asks ki-design to drop the seat concept from the concept atlas, or to point it to rigs.yaml as personal Rig setup.

b) Leave it as it is. The atlas is a design brief and an old reference there does no harm.
