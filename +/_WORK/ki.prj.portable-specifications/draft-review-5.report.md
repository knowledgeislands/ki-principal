# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Portable specifications](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/portable-specifications.md>) › draft-review-5

**🤖 → 👤 Handoff to supervisor · Run report at 00:56 BST · last mark 23:45 BST**

---

## Done

1. Partly fixed - carried earlier N1: format validity is correctly separated from demonstration-validator checks, but the parser consequence remains overstated; see new N1 below.
2. Fixed - carried earlier N2: knowledge's area and boundaries are consistently required; audience, depth and answer examples remain recommendations.
3. Fixed - carried earlier N3: knowledge's mapped-file set, exclusions and collective directory coverage are consistently defined.
4. Fixed - carried earlier N4: the house profile now applies entry renames to relative targets as well as absolute ones.
5. Fixed - carried earlier N5: ASCII names are explicitly the drafts' restriction, and all package-reference grammars admit the three name forms.
6. Fixed - previous R1: [work-house-profile.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work-house-profile.md:50>), Conversion rules / Links, preserves fragments, rewrites this package's entry targets and applies supplied sibling mappings; an unmapped sibling entry is reported as a conversion dependency.
7. Fixed - previous N1: [acquire.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/acquire.md:101>), metadata / omissions and Validation, requires the metadata declaration for every method gap within Scope, permits absence only when there are none, and distinguishes run failures from method omissions.

### N1 - [should-fix] An embedded delimiter can silently truncate metadata, rather than necessarily fail parsing

Files and sections: [work.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work.md:228>), [knowledge.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:195>) and [acquire.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/acquire.md:192>), Relation to Agent Skills / Skill validity; [specs.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/specs.md:25>), Shared conventions / validator claim.

All four say a value containing three consecutive hyphens causes a parse failure. The saved upstream [parser source](/var/folders/6b/b4c73j8s6w12g2k9_yl652_h0000gn/T/ki-agents/specifications/live-read/src/parser.py:44) splits the content before YAML parsing. With an unquoted description containing an embedded delimiter after a non-empty prefix, that split leaves a valid mapping containing the name and shortened description. Its field checks accept those values; the remainder becomes body content. Failure is therefore one possible outcome, while silent truncation is another. This matters because the current wording suggests the validator reliably rejects this input.

Proposed fix: in all four places, describe premature termination as causing either a parse failure or silent truncation, depending on the resulting YAML. Retain the distinction between the portable format and this validator limitation. This is a factual correction requiring no owner decision.

Review coverage and checks:

- Coverage: read the work definition, every owner decision, the live-check note, all five draft 0.7 documents and the previous report; no further owner-decision conflict or KI-context dependency identified in the three portable contracts.
- Upstream evidence: the saved specification, validator and parser hashes match the live-check note; claims were checked offline, without another live read.
- Examples: all six front-matter examples parse as YAML with string metadata; source-extracted validator field functions give the claimed results, including rejection of the dotted work name.
- Delimiter check: source splitting leaves a valid truncated mapping in the counterexample, and upstream field checks accept it; the full upstream parser and CLI were not executed because `strictyaml` is unavailable, and nothing was installed.
- Exact predicates: draft identities, permanent version-1 defaults, revised entry-link handling and the conditional omissions contract pass.
- Repository and authority: no repository file changed; no Git, conform, remote, commit, push or publication operation performed; commit identifiers: none. Only the required status and report files were written.

Not ready for the owner's read: correct the one repeated validator-behaviour claim; the two corrections requested by the previous review are otherwise complete.

## In Progress

Nothing running.

Outstanding - no action requested now: the supervising worker owns the factual correction and the final text handoff; full upstream parser execution remains outside this run's verification.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 00:56 BST

🤖 0 running · 🤝 1 handoff · ⛔ 0 blocked

- [handoff] Draft 0.7 review and one factual correction · supervisor · since 00:56 BST
