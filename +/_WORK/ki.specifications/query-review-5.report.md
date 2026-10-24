# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Portable specifications](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/portable-specifications.md) › query-review-5

**🤖 → 👤 Handoff to supervisor · Run report at 00:08 BST · last mark 23:45 BST**

---

## Done

Recommend **a), confidence high** - the existing provenance contract is sufficient; a second citation index adds synchronisation and validation obligations without a demonstrated consumer.

Decision check: consistent with [KNOWLEDGE-AS-SKILL](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/decisions.md:49); that decision removes a pipeline assumption, but does not itself rule out a generic, one-way source index. Option b) can also respect that decision.

Context correction: b) proposes a broader source-index field, rather than simply restoring the acquisition-method relationship previously removed. Its potential benefit is machine-readable discovery, which the query leaves unstated; it would not replace claim-level provenance.

Context correction: “provenance only in Sources” should be scoped to the knowledge package's citation contract; acquisition output retains its own provenance requirements in [acquire.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/acquire.md:104).

Omission: b) needs a key name, an unambiguous string encoding for multiple references, and rules for its relationship to Sources. [SPEC-LOCATION and VALID-SKILL](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/decisions.md:40) preclude introducing a YAML list as the metadata value. No concrete consumer needing this index is identified in the supplied material; a profile can establish the need before the portable core standardises it.

Draft consistency check: extensible metadata already permits profile keys, while the relation paragraphs sound like a blanket prohibition on cross-package metadata. Clarify that the core defines no such fields if a) is chosen; see [knowledge.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:108), [its relation paragraph](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:176), [acquire.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/acquire.md:162) and [specs.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/specs.md:40).

Read-only checks: reviewed the decisions and all three requested drafts; confirmed the removed field identifiers are absent. No repository changes, commits or remote calls.

## In Progress

Nothing is running.

## Queries

No outstanding queries

### 🤖 → 👤 Handoff to supervisor · since 00:08 BST

🤖 0 running · 👤 0 with you · ⛔ 0 blocked

- [handoff] LINK-FIELDS independent review complete · supervisor · since 00:08 BST
