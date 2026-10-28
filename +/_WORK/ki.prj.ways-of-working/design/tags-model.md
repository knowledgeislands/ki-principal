---
note_type: streams/design
status: draft
---

# Better use of tags in Knowledge Islands

Research date: 21 October 2026. This is a design proposal for review, not an adopted convention or migration authority.

## Recommendation

Keep optional, controlled subject tags for deliberate retrieval across folders. Treat the island's metadata as a faceted system: location, note kind, subject, lifecycle, dates and provenance each have their own job. Only subject needs a tag vocabulary by default. Start with a bounded pilot in KI Principal; retain existing metadata throughout the pilot.

Do not simply ratify the earlier proposal to keep every `topic/*`, `date/*` and `source/*` tag while removing every `card/*` and `calendar/*` tag. The survey supports separating subject from kind, but also finds both redundant date/source encodings and kind tags carrying distinctions that `note_type` does not currently preserve. Removal requires semantic mapping and consumer checks, not a namespace-wide replacement.

The strongest recommendation is a lightweight controlled vocabulary with local extensions, definitions and aliases, rather than free tags or a universal mandatory taxonomy. Actual retrieval benefit remains unmeasured. A pilot can test that benefit before the owner decides whether a wider migration is worthwhile.

## Authority and research boundary

Kris requested deeper TAGS review in the 21 October owner answers in the [Ways of working decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md). The earlier [research draft](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-tags-research.findings.md) stopped over conflicting network instructions and contains no completed census or external survey. This run's explicit grant resolves that conflict for reading public documentation only.

The earlier query was recovered with a local Git history search for `TAGS` in `+/_WORK/ki.ways-of-working/queries.md`. Its alternatives were to retain subject/date/source tags and retire kind tags, keep the full taxonomy, or retire tags altogether. The present proposal refines the first rather than assuming it has already been accepted.

Repositories were read only. Outputs are runtime-state drafts. No adoption, repository edit, commit, push, sign-in or provider mutation forms part of this research.

## What the rules say today

The canonical harness [frontmatter standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-kb/references/standards-frontmatter.md:14) makes `note_type` the sole kind classifier. Generic `type` is forbidden for governed KB notes. Tags are optional and describe subject, temporal or source labels; it explicitly retains `topic/*`, `date/*` and `source/*`, while describing legacy `card/*` as kind information to map into `note_type`. The [knowledge-base standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-kb/references/standards-knowledge-base.md:31) also separates kind, subject, lifecycle, audience and provenance.

The [ki-repo-kb skill](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-kb/SKILL.md) permits repository-specific required frontmatter and extensions. Its bundled Pillars, Resources and Calendar session templates suggest `topic/<pillar>`. That is a convenient starting point, but can encourage a tag that merely repeats the filing location.

[ki-authoring](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-authoring/SKILL.md) owns Markdown presentation, not tag semantics. Its [frontmatter rule](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-authoring/references/standards-markdown.md:98) governs scalar quoting and leaves field requirements and value meaning to domain skills. It supplies no separate controlled subject vocabulary.

KI Principal's [Tags convention](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Conventions/Notes/Tags.md:15) describes a cross-island superset using `namespace/value`, with island-specific extensions under Admin. Its reference table still includes `card/*` and `calendar/*`. [Collection Card](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Conventions/Notes/Collection Card.md>) still describes `card/*` as a type tag. [Properties](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Conventions/Notes/Properties.md) acknowledges the newer `note_type` separation but also retains older universal status/author wording. The local Obsidian templates continue emitting kind/date tags; the meeting template declares `note_type: pillars/note` while emitting `calendar/meeting`.

These are overlapping generations of guidance, not a cleanly implemented current taxonomy. Any adopted design needs one reconciled semantic authority, followed by templates and consumers, before a corpus rewrite.

## Observed practice across four principals

### Method and limits

The census used tracked `.md` paths from local `git ls-files -z`, limited to `Admin`, `Calendar`, `Pillars`, `Resources` and `Streams`. It read current working-tree bytes, not historical blobs. It excluded inbound/outbound working areas, runtime projections, hidden configuration, untracked material and submodule contents. It did not follow symlink files. HNR's separately owned `hnr-shared` tree is therefore outside this census; the result describes the principal checkout, not every note reachable in its editor.

Frontmatter was parsed with the installed harness's `yaml` module using unique-key validation. A note counts once per distinct tag. For the one scalar `tags` value, whitespace/comma splitting supplies a clearly labelled analytical interpretation, not a claim that every client accepts that representation. No YAML parse errors occurred in the 903 tracked zone files. Eight templates in each of KI and HNR have a non-string placeholder within their tag list; these were not treated as vocabulary terms.

The primary figures below exclude any `/Templates/` path: 20 KI files and 20 HNR files. The full inventories were KI 237, HNR 580, Sacred Inquiry 59 and Valle Armonia 27 files. The primary corpus is 863 files. It includes index notes and history retained in canonical zones, rather than pretending that every file is an active leaf note.

The samples deliberately span a mature operational base, a young thematic base and a bootstrap base. They are a local convenience sample, not an estate-wide estimate. There are no search logs, reader interviews or timed retrieval tests. Frequencies establish metadata shape and maintenance exposure, not usefulness.

### Coverage and vocabulary

| Principal | Notes | Tagged notes | Unique tags | Singleton tags |
| --- | ---: | ---: | ---: | ---: |
| KI | 217 | 125 | 28 | 14 |
| HNR | 560 | 499 | 213 | 78 |
| Sacred Inquiry | 59 | 12 | 7 | 5 |
| Valle Armonia | 27 | 0 | 0 | 0 |

A singleton is a tag appearing on exactly one note within that principal's sampled corpus. It is a review signal, not proof of a bad tag. Date tags naturally create singletons, so subject-only counts are more informative:

| Principal | Subject vocabulary | Subject assignments | Subject singletons | All tag assignments |
| --- | ---: | ---: | ---: | ---: |
| KI | 21 | 196 | 9 | 332 |
| HNR | 99 | 1,014 | 39 | 2,197 |
| Sacred Inquiry | 6 | 13 | 5 | 20 |
| Valle Armonia | 0 | 0 | 0 | 0 |

KI has `card` 118, `topic` 196, `source` 15 and `date` 3 assignments. HNR has `card` 265, `calendar` 305, `topic` 1,014, `date` 315, `source` 286 and `project` 12. Sacred Inquiry has seven `card` and 13 `topic` assignments. Valle Armonia has no observed tags; that alone says nothing about its findability.

KI's dominant subjects are `topic/knowledge-islands` on 94 notes and `topic/knowledge-management` on 36. `card/note` appears on 117. HNR's leading subjects include `topic/knowledge-management` on 148 notes, `topic/admin` on 133 and `topic/slack` on 71. Its `source/claude` appears on 284 notes. These distributions mix subject, filing category, originating tool and legacy note kind in one field.

### Drift and exceptions

Fifteen of KI's 21 observed subject values, 76 of HNR's 99 and all six of Sacred Inquiry's values are outside the shared Tags reference table. These are table mismatches, not automatically unauthorised tags: local extensions are permitted, and this research did not establish a complete extension-register inventory. Even `topic/knowledge-islands` is missing from the shared table while being KI's dominant subject. The table is not an adequate closed allow-list today.

KI and HNR share seven exact subject values: `ai`, `automation`, `email`, `knowledge-management`, `mcp`, `microsoft-365` and `tools`, each with the `topic/` prefix. The small overlap argues for shared meanings plus local domain vocabularies, rather than requiring identical tag lists across islands.

HNR contains `topic/broadcast` and `topic/broadcasting`, `topic/msf` and `topic/media-streaming-federation`, and `topic/success` and `topic/customer-success`. These are candidates for scope or alias review, not verified synonyms. `topic/visualization` also differs from British spelling. Project identity appears both as `project/5g-emerge` and `topic/5g-emerge`; their meanings need checking before merging. KI's nine subject singletons include `assets`, `diagrams`, `email`, `git`, `google`, `history`, `microsoft-365`, `notion` and `work`.

All 118 KI notes with legacy kind tags also have `note_type`. In HNR, 498 notes have kind tags and 496 of these have `note_type`; two Streams documents lack it. Sacred Inquiry's seven kind-tagged notes all have `note_type`.

Presence is not semantic equivalence. HNR has `calendar/annual-leave`, `calendar/bank-holiday` and `calendar/standup` on five notes classified only as `calendar/meeting`; four `card/system` notes have `admin/note`; five `calendar/digest` notes have `calendar/daily`; one `calendar/weekly` tag sits on a `calendar/index` note. These 15 assignments expose distinctions or mismatches that a blanket deletion could erase. Some `note_type` values themselves are legacy values, so merely checking that the field exists is insufficient.

### Overlap with folders and links

The overlap check compared each subject slug with normalised ancestor folder names and explicit body link target basenames. Normalisation lowercased and joined punctuation/spacing with hyphens. These are lexical proxies, not a resolved link graph or a test of conceptual equivalence; examples and unresolvable targets can affect them.

| Principal | Subject assignments | Folder-name matches | Body-link-name matches |
| --- | ---: | ---: | ---: |
| KI | 196 | 13 on 12 notes | 6 on 6 notes |
| HNR | 1,014 | 180 on 102 notes | 3 on 2 notes |
| Sacred Inquiry | 13 | 11 on 11 notes | 2 on 2 notes |
| Valle Armonia | 0 | 0 | 0 |

Examples are `topic/aesthetics` below `Pillars/Aesthetics`, `topic/admin` below HNR's Admin zone, and `topic/religion` on Sacred Inquiry's Religion index. Conversely, Sacred Inquiry's [Aliens note](/Users/krisbrown/workspaces/sacred-inquiry/si-principal/Pillars/Research/Aliens.md) carries `topic/spirituality` outside that Pillar, showing a cross-folder application. KI's [August meeting note](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Calendar/2026/2026-08 August/2026-08-24 Ancient Civilisations Insights.md>) combines a subject, date and capture-source tag.

The low link-name match counts do not show that tags add unique knowledge: a link can express the same subject using another name, or express a stronger relationship. Equally, a folder-name match does not make a tag useless: a single query may need the same subject across several folders. The design question is which useful retrieval set the tag creates.

## Comparison with other systems

The factual descriptions below come from public documentation read during this run. The proposed limits and KI lessons are design inferences, not claims that every product forbids other uses.

### Obsidian: lightweight grouping beside typed properties

Tags retrieve groups of notes through search and the Tags view. Slash-separated nested tags provide prefix grouping: searching a parent can include children. Tags can be inline or in the special `tags` property, whose YAML representation should be a list. The documented syntax does not establish an editorial vocabulary; authors must supply that governance. A slash hierarchy is therefore a retrieval convention, not a controlled concept scheme. [Obsidian tags](https://help.obsidian.md/tags).

Properties separately hold structured text, lists, links, numbers, booleans and dates. Their editor assigns types by property name. KI should use that distinction for dates and lifecycle fields rather than making every property a tag. Repeating `#` in arbitrary text properties does not create tags. [Obsidian properties](https://help.obsidian.md/properties).

### Logseq: distinguish file graphs from database graphs

The file-graph Properties documentation permits properties on pages and blocks, values containing links and tags, and property queries. It offers a graph-centred model rather than KI's folder-centred one. Its standalone Tags documentation is still a stub, so it cannot support a detailed universal claim about tag/link equivalence. [Logseq Properties](https://raw.githubusercontent.com/logseq/docs/master/pages/Properties.md), [Tags stub](https://raw.githubusercontent.com/logseq/docs/master/pages/Tags.md).

The database-graph documentation describes tags as grouping nodes across pages and supplying inherited Tag Properties. Parent tags can supply additional inherited properties. Here tags can act like classes, a materially different job from Obsidian subject labels. Authors configure tag definitions; specialised properties can constrain values. KI should not import these class semantics into `tags` while retaining `note_type` as its sole kind classifier. [Logseq database graphs](https://github.com/logseq/docs/blob/master/db-version.md#tags), [property/tag configuration guide](https://github.com/logseq/logseq/blob/master/libs/guides/db_tag_property_idents_guide.md).

### Notion: a vocabulary scoped to a named property

Select and multi-select properties offer one or several options. Users can create, rename, recolour and remove options in their property menus. Status, date, relation and person properties are separate mechanisms. The useful pattern is a named facet with a reusable local option set; a menu by itself does not prevent uncontrolled growth. KI can borrow explicit field meanings without adopting Notion or pretending a multi-select value is an entity relationship. [Notion database properties](https://www.notion.com/help/database-properties).

### Zettelkasten practice: retrieval entry points and meaningful connections

Sascha Fast's account distinguishes broad topic tags from tags identifying the actual object or concept discussed, favouring more precise tags and explicit structure-note connections. This is one influential practice, not a universal Zettelkasten standard. It supports a useful KI discipline: assign a subject because the note substantively concerns it, and write links/prose when the relationship itself carries knowledge. A bag of broad labels is a poor substitute for those connections. Vocabulary develops with the writer's thinking and deliberate maintenance. [The Difference Between Good and Bad Tags](https://zettelkasten.de/posts/object-tags-vs-topic-tags/).

### Diataxis and documentation sites: purpose and subject are separate

Diataxis organises documentation around tutorials, how-to guides, reference and explanation, derived from reader needs. It is not a tag system and does not prescribe a subject vocabulary. Its lesson is to keep document purpose distinct from subject. KI need not turn those four forms into compulsory tags or remodel the whole KB around them. [Diataxis](https://diataxis.fr/).

Docusaurus offers document tags alongside sidebar navigation, with inline values or reusable definitions in `docs/tags.yml`; definitions can carry labels, descriptions and permalinks. This is a practical small-registry pattern. Tags support supplementary discovery rather than determining the entire documentation structure. [Docusaurus document tags](https://docusaurus.io/docs/create-doc#doc-tags).

### GitHub labels: maintained operational categories

Labels classify issues, pull requests and discussions within a repository. Defaults can be edited, and organisation owners can customise defaults for new repositories. Labels in one repository do not automatically govern those in another. They can cover operational state as well as subject; that flexibility suits work tracking, but does not justify duplicating KI's authoritative lifecycle fields. Borrow maintained descriptions and local scope, with explicit cross-island mapping where needed. [GitHub managing labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels).

### Dublin Core and schema.org: subject description and interchange

Dublin Core's `subject` describes the resource's topic. It recommends a URI where feasible and preferably a controlled vocabulary for either URI or literal. Subject metadata has a clear semantic job; it does not encode every other property of the resource. Vocabulary ownership comes from the chosen scheme. [DCMI Subject](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/subject/).

Schema.org `keywords` accepts descriptive keywords/tags, including text, URLs and DefinedTerm values. It supplies an interchange property rather than a ready-made subject taxonomy. Exporting KI subjects through it would still require KI definitions and mappings; it does not justify treating a comma-separated export string as the canonical YAML representation. [schema.org keywords](https://schema.org/keywords).

### SKOS: concepts, names and relationships

SKOS distinguishes concepts from their labels, allows preferred and alternative labels, scope documentation, broader/narrower and related relations, and concept schemes. That is useful when synonyms or cross-scheme mappings matter. It is not an automatic vocabulary steward, and related concepts should not be merged merely because they co-occur. KI can adopt a preferred slug, aliases and a short scope note without installing RDF infrastructure or reproducing a full ontology. Scheme maintainers still decide meaning and change policy. [W3C SKOS Primer](https://www.w3.org/TR/skos-primer/).

### Faceted classification: independent questions, combinable answers

Faceted retrieval narrows a collection using distinct categories and their values. Nielsen Norman Group's research emphasises appropriate, predictable and understandable filters chosen around user needs; its taxonomy guidance distinguishes controlled metadata from navigation structure. KI's existing zone, kind, date and subject information can therefore supply different facets. Putting every facet into one tag list creates no automatic benefit. Which combinations are useful must be tested with real queries. [Filter categories and values](https://www.nngroup.com/articles/filter-categories-values/), [Taxonomy 101](https://www.nngroup.com/articles/taxonomy-101/).

## Proposed KI model

### Give each mechanism one job

| Mechanism | Question answered | Proposed use |
| --- | --- | --- |
| Folder/zone | Where does this belong? | Ownership and canonical home |
| `note_type` | What kind of note is this? | Governed, location-constrained kind |
| Links and prose | How does this relate? | Named entities, arguments and explicit relationships |
| `tags` | What subjects should retrieve this? | Optional controlled `topic/*` values |
| Lifecycle fields | What state is it in? | Owning instrument's existing fields |
| Date properties | When did this happen/change? | Explicit date semantics, not interchangeable timestamps |
| Provenance properties | Where did this come from? | Existing author/source/mirror contracts |

This is faceted classification across metadata, with one default subject vocabulary in `tags`. It is not a proposal to add several new namespaces or required fields. A richer facet, such as audience, would need an actual retrieval need and its own approved field contract.

Keep `tags` optional. For new or substantively revised notes in a future pilot, use zero to three carefully chosen subject tags as a working guideline, allowing justified exceptions. Do not tag every mentioned word, invent missing tags to satisfy a quota, or copy all ancestor folder names. A singleton may be a valid precise entry point. A subject can still deserve a tag when it matches a folder if it enables a useful cross-folder query.

Use lowercase ASCII kebab-case slugs under the existing `topic/` namespace, stored as a YAML string list. Retain the shallow current form initially. Further slash nesting should express an agreed subject hierarchy, not encode several independent facets into one path. Parent expansion is client-specific; portable searches must explicitly include mapped descendants rather than assume every engine understands Obsidian nesting.

### Govern a small vocabulary without flattening island autonomy

The portable contract belongs with `ki-repo-kb`; `ki-authoring` continues to own formatting. KI Principal's model notes explain the accepted method. Each island owns its subject extensions under Admin, as the existing convention already allows. Other principals require their own acceptance and execution authority.

A small register should record each preferred slug, human label, inclusion/exclusion scope, aliases, owner, and active/deprecated state with replacement where applicable. Existing approved conventions can host it initially; do not create one note per tag or a new service merely to run the pilot. Only add a broader/related relation where it helps real retrieval. Keep an alias distinct from a related or broader subject.

Start KI's pilot with approximately 10-20 justified concepts selected from its 21 observed subjects, rather than promulgating that numeric range as a permanent limit. Retain precise domain terms where they serve a question. Review broad `knowledge-islands`, `knowledge-management` and `tools` definitions; review potential overlaps such as `assets`/`diagrams` rather than merging them automatically. HNR's 99 subjects need its domain owner's judgement, not a cap copied from KI.

An author can select an existing term directly. A proposed new term needs a retrieval example and a scope distinction from existing terms, then the island's normal change authority. New terms remain proposals in the existing work/intake mechanism until accepted; no new mandatory `candidate/*` tags are needed. Small shared vocabularies can be mapped between islands without assuming that same spelling proves same meaning.

### Handle other tag families through evidence-preserving mapping

Treat `card/*` and `calendar/*` as legacy kind encodings. Retire a value only when its meaning is represented by a valid `note_type` or another already governed property and every relevant consumer has been considered. Annual leave, bank holidays and standups demonstrate why this cannot be a blind deletion. The existing `day_type` property applies to daily notes; do not automatically reuse it for unrelated notes without an agreed contract.

Prefer explicit, semantically correct date properties and Calendar placement to new `date/*` tags. A source event date is not `created` or `updated`, and a weekly period is not a single date. Preserve period/event meaning before retiring an existing date tag. Keep legacy tags where a demonstrated date-prefix query still depends on them until that query has a replacement.

Prefer existing provenance mechanisms to new `source/*` tags. `source/claude` may describe authorship, assistance or ingestion; `source/granola` may describe a capture tool. Neither necessarily identifies the original source. Do not infer a specific source from `author: Mixed` or discard capture information merely because an author field exists. Map it explicitly or retain it pending a separate provenance decision.

For `project/*`, prefer a link or the work adapter's project identity where it carries the intended relation. A subject about a project and membership of project work are different facts. Do not merge the HNR encodings without checking that difference.

## Audit and migration

### What a useful audit would check

Mechanical checks should validate YAML list/string shape, duplicate values, recognised active slugs, approved aliases and legacy namespaces. Report unknown values and deprecated usage during the transition; fail malformed metadata and, once approved, invalid new writes. Do not make old notes fail merely because the pilot has introduced a stricter vocabulary.

Editorial checks should review singleton and high-frequency terms, potential synonym splits, near-duplicate scopes, and tags that mostly mirror folders. They should also ask whether tags improve named retrieval tasks. None of these frequency measures warrants automatic removal. Run checks on touched notes and a bounded vocabulary review during existing maintenance; this proposal creates no schedule.

Audit consumers before deletion: templates, saved searches, Obsidian views/queries, scripts, MCP retrieval, mirrors and publishing transforms. This run confirmed tag-emitting templates and found no explicit `tag:`/`file.tags`/`contains(...tags)` consumers in its bounded KI authored-note search; that is not proof that no consumer exists. Hidden plugin state, private saved searches, other repositories and providers were not exhaustively audited. The harness's derived-search contract also warns against assuming the pinned REST search interface supports metadata filtering. Do not promise faceted UI behaviour without checking the actual retrieval surface.

### Recommended staged pilot

1. Agree the semantic model and pilot boundary. Reconcile portable guidance, KI's Tags/Properties/Collection Card conventions and templates through their owners before changing ordinary notes.
2. Define 10-20 initial KI subjects with aliases and scope notes, and five owner-relevant retrieval questions. Select 20-30 notes spanning Pillars, Resources, Calendar and Admin, including matched-folder and cross-folder examples.
3. Compare existing folders/links/full-text with explicit subject filters on the same questions. Record expected relevant notes, missed notes, irrelevant results, and time/steps to recover useful notes. Include an untagged-note case; absence must not exclude otherwise relevant results.
4. Keep existing tags while testing new definitions. Produce a dry-run mapping with per-note before/after values, preserved date/provenance/kind semantics and affected consumers. This is the reviewable migration proposal.
5. Proceed only if the pilot shows a useful retrieval improvement and manageable author effort, or a clearly valuable equivalent retrieval with lower maintenance cost. Otherwise revise the vocabulary, reduce tagging, or choose no new tags. Wider migrations remain separately approved work owned by each receiving repository.

### Cost and concrete exposure

| Principal | Kind-tagged notes | Also have `note_type` | Date-tagged notes | Source-tagged notes |
| --- | ---: | ---: | ---: | ---: |
| KI | 118 | 118 | 3 | 15 |
| HNR | 498 | 496 | 313 | 286 |
| Sacred Inquiry | 7 | 7 | 0 | 0 |
| Valle Armonia | 0 | 0 | 0 | 0 |

These are overlapping review sets, not additive file-edit totals. A topic-only end state would require reviewing up to 125 currently tagged KI notes, 499 HNR notes and 12 Sacred Inquiry notes, plus untagged notes only where the chosen retrieval tasks justify additions. Twenty KI and twenty HNR template files require a separate assessment, not necessarily changes to every file. The eight non-string placeholder lists per template set and KI's scalar tag field also need correction if those files enter an approved migration.

The simple mechanical work is small; meaning and consumer review dominate. As a planning judgement, allow one to two focused working days for a KI vocabulary/consumer review and pilot with owner input, followed by a separately estimated migration. Do not treat this as a measured delivery estimate or extrapolate it to the estate. HNR is materially more expensive because it combines 99 subjects, several kind distinctions, date/provenance tags and a separately owned shared tree outside this census.

The pilot can preserve all existing values and consumers. A later migration should retain a reviewed mapping manifest and use ordinary explicit-path Git commits for rollback; avoid indefinite dual authoring of equivalent fields. No migration is authorised by this note.

## Evidence record

The local corpus was sampled around 15:29-15:31 BST on 21 October 2026. Current working-tree files were read at these local HEADs, which identify the surrounding checkout history but do not assert a clean or immutable working tree:

- KI Principal: `896382bffe906c407d26b8d06320b5d38cc20590`.
- HNR Principal: `a6bf4ca3144c65ff6dd9f5c3e5dfff60b667341e`.
- Sacred Inquiry Principal: `fc879c0d914388d68844ef4f046d6c8ea326c97d`.
- Valle Armonia Principal: `94ccc7b368591209f6de3d19bc2b9d8bc9eb6cd6`.

Reproduction uses the five-zone tracked-file selection, YAML unique-key parsing, per-note tag sets and template exclusion described above. Counts are per repository; identical slugs in different repositories are not combined into a single singleton denominator. Subject-table comparisons use the literal `topic/*` values in KI's Tags table, not prose mentions. Folder/link overlap uses normalised lexical equality and should be replaced with resolved graph analysis before any deletion decision.

Public citations identify the documentation actually consulted. Logseq's main documentation application exceeded the web reader's size limit; the official documentation repository supplied the readable file-graph and database-graph sources. The distinction between those graph models is retained in the comparison. No third-party forum claim supplies the product conclusions.

## Pilot, 22 October 2026

Kris answered TAGS a) at 02:25 BST on 22 October, "I agree with what you said about tags", recorded in the [Ways of working decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md), and the overnight run `wow-burn-principal` planned and ran the bounded pilot below in KI Principal. It is additive and reversible: one commit adds 23 `topic/*` lines to 21 notes and removes nothing, so reverting that commit restores every note exactly. No `card/*`, `date/*` or `source/*` tag, `note_type`, date, lifecycle or provenance field was touched, and no `updated` value was moved, because the change is metadata for the trial rather than a revision of the notes.

### Plan

1. Fix five owner-relevant retrieval questions and, for each, the notes a reader would want, before any tag is added, so that the expected sets do not follow the tags.
2. Use a pilot vocabulary of the existing observed subjects plus one new term, with a scope and aliases for each subject the questions test.
3. Tag every expected note that can carry tags with the question's subject, zero to two subjects per note, leaving decision records untagged as the control.
4. Run the same questions three ways before and after: full-text search for the term a reader would type, following links from the obvious entry note, and a tag filter.
5. Record expected notes found, results returned and notes missed; keep the existing tags throughout.

### Pilot vocabulary

| Slug | Scope: tag a note when it is substantially about | Not for | Aliases | State |
| --- | --- | --- | --- | --- |
| `topic/governance` | Who holds authority, how canonical change is approved, charters, councils, conformance | Notes that merely pass through Enactment | authority, enactment | existing, extended |
| `topic/agents` | How AI agents and Avatars act in the model, their roles and limits | AI as technology in general, which stays `topic/ai` | avatars, delegation | new |
| `topic/acquisition` | How outside material enters an island: the Port, acquisition, routing on arrival | Trade between islands | capture, intake, port | existing, extended |
| `topic/history` | Where the model's ideas come from: the history of knowledge systems, prior art, influences and lineage | The history of a single note or repository | lineage, influences | existing, extended |
| `topic/work` | How forward work is recorded and moved: work records, Streams, Activities, the Work Process | Notes that merely cite a work record | roadmap, streams | existing, extended |

The other observed subjects stay as they are and are not tested here: `topic/knowledge-management`, `topic/productivity`, `topic/automation`, `topic/aesthetics`, `topic/mcp`, `topic/ai`, `topic/tools`, `topic/brand`, `topic/symbols` and the precise singletons. `topic/knowledge-islands`, on 93 of 180 notes in this island, retrieves nearly everything and is a candidate for deprecation here, though not for removal in this pilot.

### Sample

Twenty-seven notes across 20 Pillars, 6 Admin and 1 Calendar notes; 21 gained a tag and 6 already carried the one they needed. Resources holds only the Productivity pair, already tagged `topic/productivity` under a matching folder, so it adds no new case. The six decision records in the expected sets were not tagged: their front matter belongs to `ki-decision-records` and has no `tags` field, which makes them a natural untagged control.

| Question | Subject | Expected notes |
| --- | --- | ---: |
| Who holds authority on an island, and how is canonical change approved? | `topic/governance` | 9 |
| How do AI agents act in the model, and within what limits? | `topic/agents` | 8, 2 of them decision records |
| How does outside material enter the island? | `topic/acquisition` | 6, 2 of them decision records |
| Where do the model's ideas come from? | `topic/history` | 5 |
| How is forward work recorded and moved through its states? | `topic/work` | 6, 2 of them decision records |

### Retrieval comparison

Corpus: the 180 tracked Markdown notes in Admin, Calendar, Pillars and Resources, excluding templates. "Found" counts expected notes returned; "results" counts everything returned, which a reader has to sift.

| Question | Best full-text query: found, results | Links from the entry note: found | Tag before: found, results | Tag after: found, results |
| --- | --- | --- | --- | --- |
| Governance | `governance`: 9/9, 127 | Governance: 1/6 | 3/9, 5 | 9/9, 11 |
| Agents | `agents?`: 8/8, 93 | Model Agents: 2/7 | 0/8, 0 | 6/8, 6 |
| Acquisition | `port`: 4/6, 19 | Acquisition Process: 2/5 | 1/6, 1 | 4/6, 4 |
| History | `history`: 4/5, 22 | Background: 4/5 | 1/5, 1 | 5/5, 5 |
| Work | `roadmap`: 5/6, 32 | Work Process: 0/5 | 1/6, 1 | 4/6, 4 |

The narrower full-text alternatives did worse on recall: `enactment` found 8/9 in 49 results, `avatars?` 2/8 in 11, `acquisition` 2/6 in 15, `lineage|influences?|inspirations?` 3/5 in 9 and `work records?` 3/6 in 14. The two extra governance results by tag are the Conformance notes, which were already tagged and are relevant.

### Findings

- **Tags cut the sifting, not the recall.** Broad full-text queries already reach almost every expected note, but in 19 to 127 results; the tag returns 4 to 11, nearly all relevant. For broad subjects such as governance and agents, which appear in 70% and 52% of notes, full text is not a usable retrieval path on its own.
- **Tags help most where a subject crosses zones.** Governance spans the Concept, Model and Realisation chapters and Admin, and work spans the Model and Admin. These are the cases where links from the obvious entry note recovered least, 1 of 6 and 0 of 5, and where the tag recovered every expected note except decision records.
- **Where a chapter already gathers the subject, links do as well.** Background links four of the five lineage notes, so the history tag adds only the Calendar note. Tagging a subject that one index note already covers buys little.
- **Untagged notes fall out of a tag filter.** All six misses after the pilot are decision records, which carry no tags by contract. A tag filter is therefore a supplement to links and full text, not a replacement, and either `ki-decision-records` gains an optional `tags` field or tag retrieval is paired with the Decisions index.
- **The author effort is small once the scope is written.** Each tag was a one-line, one-judgement edit; the scope notes did the work, especially the "Not for" column, which kept `topic/governance` off notes that merely pass through Enactment.
- **Nothing reads these tags in a way the pilot can break.** The Observatory reads `tags` as a list of strings and stays valid; the KI Website's tag handling is for its own pages; the `mcp-ki-kb-fs` source uses tags only in tests. Obsidian's tag pane and search pick the new values up as they are.

### Limits

The same run wrote the questions, the expected sets and the tags, so recall by tag on these 27 notes is close to guaranteed; the honest measures are the result counts, the misses outside the tagged set and the effort. There were no timed searches, no reader other than the run, and no Obsidian interface test. Five questions on 180 notes is a pilot, not an estimate for HNR, whose 99 subjects and 560 notes need their own owner.

### Next decision

The pilot supports keeping optional controlled `topic/*` tags for subjects that cross zones, scoped by a short register, and not tagging subjects one chapter already gathers. Three things follow, each needing its own authority: reconcile the [Tags convention](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Conventions/Notes/Tags.md) with this register through the Enactment Process; decide whether decision records take optional tags under `ki-decision-records`; and leave the `card/*`, `date/*` and `source/*` question to the mapping step of the staged plan above. The pilot tags stay in place meanwhile and are reverted by reverting their commit.

## For Kris

### TAGS - a useful role for tags beside folders, links and note_type

Answered a) by Kris at 02:25 BST on 22 October; the pilot above ran under it.

**Context:** Current subject tags can group notes across folders, but their retrieval benefit has not been tested. The four-principal sample found substantial legacy kind tagging and uneven subject vocabularies. Some old kind tags retain meaning absent from `note_type`, and date/source tags can carry information that must be preserved. Public systems support separating subject grouping, typed properties and meaningful links; they do not establish a universal ideal taxonomy. The proposed model is optional controlled `topic/*` tags within the island's existing metadata facets, with local vocabulary ownership. This is a design and pilot decision, not approval for bulk removal or cross-island changes.

**Query:** Which tag model should Ways of working take forward for a bounded KI Principal pilot and review?

**Options:**

a) (recommended, confidence high - the local census and external patterns support testing a small subject vocabulary while preserving existing meaning and keeping the trial reversible) Take forward optional controlled subject tags, with existing fields owning kind, dates, lifecycle and provenance; approve planning a 20-30-note KI pilot and retrieval comparison before any migration decision.

b) Keep the current multi-namespace model, reconcile its contradictory guidance and govern its vocabulary more carefully; retain kind/date/source tags where useful and accept duplicate metadata maintenance.

c) Test a no-new-tags model using folders, links and typed properties alone; retain legacy tags during that comparison and decide on retirement only after equivalent retrieval and preservation of meaning are demonstrated.
