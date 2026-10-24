# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Portable specifications](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/portable-specifications.md) › live-read

**🤖 → 👤 Handoff to supervisor · Run report at 23:48 BST · last mark 23:48 BST**

---

## Done

- Findings written to [agentskills-check.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/agentskills-check.md), uncommitted, as the brief asked; every answer is quoted with its URL and source line, and the source files are identified by SHA-256, since `main` was read without the GitHub API.
- Case of other files: Agent Skills sets no case rule beyond `SKILL.md`, and its own examples use upper-case `references/REFERENCE.md` and `FORMS.md` beside `finance.md`; `skills-ref` even accepts a lower-case `skill.md`. The plan's claim that Agent Skills keeps every other file lower-case (ENTRY-NAMES) is wrong.
- A skill's own version: in `metadata.version`, shown by example (`version: "1.0"`), not as a rule; Agent Skills has no top-level version field and no spec-version field.
- Closed fields: the page lists six fields without saying in words that no others are allowed, but `skills-ref` rejects any other top-level key ("Unexpected fields in frontmatter"). `metadata` is string-to-string in the specification; `skills-ref` converts values to strings rather than rejecting them.
- Licence: the specification text is CC BY 4.0 (the documentation directory) and `skills-ref` is Apache 2.0. The drafts may follow the wording closely with attribution and a note that it has been changed; the note proposes an attribution line.
- Effect on the drafts: "a conforming package is also a valid skill" (`knowledge.md` line 138) and "an acquire package is a skill" (`acquire.md` line 148) are both false as written, because their extra top-level fields fail `skills-ref`. The "reader ignores unknown keys" rule and the "upper-case entry file" rule belong to the drafts, not to Agent Skills.
- Drift from the harness reference: six items. Two are material: the reference understates the validator, which rejects every top-level key outside its six, Claude Code fields included; and it does not record the licence. Four are minor. Nothing was edited in the harness.

## In Progress

Nothing is running.

Outstanding - no action requested now:
- The temp folder `/var/folders/6b/b4c73j8s6w12g2k9_yl652_h0000gn/T/ki-agents/specifications/live-read/src/` still holds three public source files downloaded for line-exact quotation. My delete needed a permission I did not have. Nothing in them needs keeping, so `ki agent close` or a manual delete may clear them.
- The harness drift items D1 and D2 are for the next `ki-skills` REFRESH in ki-agentic-harness.
- The note is uncommitted in the work folder, for the coordinator to commit at receive.

## Queries

### VALID-SKILL - Keep "also a valid skill" by moving added fields into `metadata`?

**Context:** `skills-ref validate` rejects any top-level key except `name`, `description`, `license`, `compatibility`, `metadata` and `allowed-tools`. As drafted, `knowledge` adds `updated`, `acquired-with` and `spec` at top level, and `acquire` requires `source` and `mutation` and adds `omissions`, `produces` and `spec`. So no package using them is a valid skill, and every conforming acquire package fails. Moving them into `metadata` as quoted strings keeps the claim true at the cost of nesting. Agent Skills itself suggests `metadata` "to store additional properties not defined by the Agent Skills spec". `omissions` would become one comma-separated string. `work` makes no such claim and its dotted names fail anyway.
**Query:** For revise-drafts (step 3), should `knowledge` and `acquire` move their added fields into `metadata` so the valid-skill claim holds, or drop the claim?
**Options:**
a) (recommended, confidence medium - interoperability with existing skill tooling is the point of following Agent Skills, and `metadata` is its stated home for extra properties; not blind-reviewed) Move them into `metadata` for `knowledge` and `acquire`, keep the claim, and leave `work`'s top-level fields as they are, listed under "Different".
b) Keep the fields at top level, drop both sentences, and say the packages share Agent Skills' layout but are not valid skills.
