# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Ways of working](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md>) › gfm-review

**🤖 → 👤 Handoff to supervisor · Run report at 21:40 BST · last mark 21:25 BST**

---

## Done

- Completed the independent review of the five [reviewed queries](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/queries.md:5>). Commits: none; repository files unchanged. No remote calls, environment changes or background agents.
- Inventory: reproduced 537 plain and 488 aliased non-heading wikilinks, plus 10 heading links and 15 embeds, after excluding fenced and inline code. Also confirmed two custom `todo` callouts and two Dataview blocks. These totals include `+/`; the proposed non-`+/` batches contain 975 wikilinks including heading links, and 14 embeds. The four-zone pilot contains 23 wikilinks.
- Mechanical-conversion claim: qualified. Four real image embeds specify width 800; ordinary Markdown images lose this layout instruction. Heading destinations, unresolved targets, templates and candidate collisions also require decisions or explicit exceptions before application.
- Harness checks: invoked the current LINK-1 evidence collector read-only; it passes this checkout but checks ambiguity only, excluding both working areas. Direct execution of the actual parser functions confirmed that Decision Records omit inline angle-bracket destinations containing spaces and truncate reference-definition destinations; Activities recognises wikilinks and angle-bracket Markdown links, but does not decode percent-encoded spaces.
- Compatibility checks: direct Observatory probes resolved document-relative links with both angle-bracket spaces and percent-encoded spaces. Inspection of installed Obsidian code confirmed angle-bracket destination parsing and relative-path handling. GitHub and Zed navigation, and Obsidian UI behaviour, were not tested under the no-network, read-only brief. Observatory heading fragments are discarded before navigation.
- Governance check: Enactment exempts trivial formatting, supplies no numerical scale threshold, permits bounded owner instructions instead of records, and groups related changes in one record. A substantive convention rewrite falls within its canonical-content rules.

## In Progress

Nothing running. This review authorises no implementation.

Outstanding - no action requested now: the plan needs these additions before delivery.

- **Repair consumers before enabling conversion.** The [Decision Record parser](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-decision-records/scripts/rubric/contexts/decision-records.ts:239>) fails open for the proposed space-containing link form. The [Activities parser](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-kb-activities/scripts/rubric/contexts/activities.ts:134>) supports the two syntax families, but encoded-space links still fail filename coverage. Support for multiple flavours needs fixtures for both angle-bracket and encoded destinations, reference definitions and escaped table aliases. A global percent-decoding rewrite would be unsafe for reserved characters and literal percent signs.
- **Verify heading navigation separately.** The [Observatory link conversion](</Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/knowledge-bases.ts:616>) removes the fragment from a Markdown link, and [Observatory navigation](</Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/instruments/src/prose.ts:302>) opens only the target note. Preserving edge counts cannot detect this loss. Test self-links, cross-note headings, duplicate headings and Unicode anchors across the actual clients. The claim that all four already resolve the proposed form identically is stronger than the evidence; both destination spellings are valid candidates.
- **Resolve exceptions before applying each batch.** Four width-constrained embeds contradict the scoping report's claim that none have sizing. The [image-width convention](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Conventions/Notes/Format.md:111>) explicitly requires width 800. Choose a supported replacement or an approved exception, and check the three SVG embeds against each reader's existing restrictions. Do not silently turn sizing into alt text. The two custom callouts also carry substantive definition text that must survive.
- **Fix the inventory boundary.** The 1,025 figure excludes heading links and code examples but includes working material; it is not the batch workload. A literal tracked-path scan reproduced 29 unresolved candidates: 11 in `+/`, 14 dynamic template destinations and four occurrences in Streams. Seven ambiguous occurrences were not reproducible with exact and source-relative matches taking precedence: this scan found five multi-candidate occurrences. Existing [LINK-1 implementation](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-kb/scripts/rubric/contexts/kb.ts:580>) passes because its candidate universe excludes working areas. Define the resolver's universe and precedence, snapshot actual destinations, and re-inventory at the pilot rather than adopting these counts as authority. This checkout has 20 tracked Markdown files under the Obsidian Templates folder, including its index; the reported 21 also needs reconciliation.
- **Strengthen verification beyond totals.** Compare each link's old and new target identity, fragment, label, image asset and relevant display properties. Equal link counts, rendered text or graph-edge totals can hide a wrong destination. Preserve YAML values, code examples, template expressions, list/table structure and authored prose; require idempotence, containment and exact-case checks, per-file previews, and a recorded baseline for pre-existing failures. The new audit must cover retained wikilinks as well as Markdown, not merely treat legacy syntax as tolerated and unchecked.
- **Make batch application safe in the shared checkout.** Apply only reviewed paths against unchanged input bytes; abort on concurrent edits or newly ambiguous destinations. Separate syntax conversion from formatter changes, preserve protected and generated material, and keep explicit-path commits and an exact rollback manifest. The [Enactment Process](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Operations/Processes/Enactment Process.md:26>) also requires a concrete preview checkpoint for complex or destructive rollout. Do not make a whole-file touch rule an implicit estate-wide write grant.

## Queries

### GFM-ORDER - convert outright in verified batches

**Context:** Agree with option a's staged approach, with revised prerequisites. The inventory supports substantial automation, but neither image presentation nor heading navigation is uniformly preserved. Judgement must precede application for affected files, rather than follow all batches.

**Query:** Proceed with zone batches once the rules, converter, consumer fixes and pilot are verified?

**Options:**

a) (recommended, confidence medium - the scale supports automation, but conversion safety depends on unresolved exceptions and a pilot) Take original option a, with fail-closed preflight and per-batch exception decisions before writes.

b) Use original option b: adopt the preference and convert on touch until the pilot supports batches.

### FLAVOUR-FIELD - omit per-note flavour metadata

**Context:** Agree with option a. A field would describe declared intent, not establish correctness. CommonMark-only notes belong to both ecosystems, while syntax inside examples can produce false positives, so the report's claim that flavour detection is mechanically definitive should be softened.

**Query:** Drop the proposed per-note field?

**Options:**

a) (recommended, confidence high - metadata would add upkeep without verifying links or conversion completeness) Drop the field. Express any repository-level preference through an explicitly defined configuration contract when needed; do not add a speculative key now.

b) Keep a per-note declaration only if a real consumer needs explicit author intent.

### GFM-LINK-FORM - prefer document-relative destinations

**Context:** Agree with option a for file destinations, subject to compatibility checks. The [existing link convention](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-authoring/references/standards-markdown.md:99>) already prefers angle brackets for paths containing spaces. Percent encoding also works in the Observatory; angle brackets are not the only viable spelling. Heading navigation is a separate unresolved issue.

**Query:** Adopt document-relative Markdown links, using angle brackets for space-containing paths?

**Options:**

a) (recommended, confidence medium - this matches the existing readable-source convention, but four-client navigation is not yet proven) Take original option a after fixing consumers and checking real clients. Normalise destination syntax structurally, preserve necessary URI escapes, and audit exact-case resolution and fragments.

b) Take original option b with percent-encoded destinations, fixing Activities coverage and applying the same navigation checks.

### GFM-ENACT - use one bounded conversion record

**Context:** Agree with option a. Convention and Activity rewrites make this more than trivial formatting. However, scale alone is not a defined threshold, and Enactment expressly allows a bounded owner instruction to stand in for a record. This review's authority is read-only.

**Query:** Carry the conversion and its policy changes in one Enactment record?

**Options:**

a) (recommended, confidence high - one scope joins the substantive policy changes, previews and mechanical batches under the existing related-change rule) Use one record covering the converter-dependent rollout, exceptions, convention notes and Activity changes.

b) Use an explicit bounded owner delivery instruction instead, or separately exempt only genuinely trivial formatting while retaining a record for substantive changes.

### TOUCH-SCOPE - convert the whole edited file

**Context:** Agree with option a's whole-file interpretation, with lower confidence than the scoping report. It matches Kris's direction and avoids indefinite mixed syntax, but a touched file can contain unresolved links, generated material or unsupported constructs. Conversion cannot silently change their meaning.

**Query:** Convert the whole authored Markdown file when edited, once the safe converter is available?

**Options:**

a) (recommended, confidence medium - whole-file conversion is coherent only when unsupported constructs and protected content stop automatic rewriting) Take original option a after preflight, keeping conversion visible in review. Escalate an unsafe file or record an approved exception; define protected/generated-file handling before enabling the rule.

b) Take original option b for the transition: convert edited lines only, retaining the rest for a reviewed batch.

### 🤖 → 👤 Handoff to supervisor · since 21:40 BST

👤 5 with you

- [with you] GFM-ORDER · owner · since 21:36 BST
- [with you] FLAVOUR-FIELD · owner · since 21:36 BST
- [with you] GFM-LINK-FORM · owner · since 21:36 BST
- [with you] GFM-ENACT · owner · since 21:36 BST
- [with you] TOUCH-SCOPE · owner · since 21:36 BST
