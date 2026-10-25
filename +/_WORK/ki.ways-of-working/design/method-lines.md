---
note_type: streams/design
updated: 2026-10-25T01:05:00Z
author: Written with Claude
---

# Method lines

**Status:** draft, for the coordinator to dispose of METHOD-LINES and PERSONAL-RESERVED. No standard, skill, output style or configuration was changed.

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Date:** 2026-10-25

State of play sent its method lines here as one unit, METHOD-LINES, under RESTART-ON-SOL. The line detail is in State of play's [messages.md at fbe4ebb0](https://github.com/knowledgeislands/ki-principal/blob/fbe4ebb0/+/_WORK/ki/messages.md?plain=1#L37-L127), with REPO-METADATA at [L14](https://github.com/knowledgeislands/ki-principal/blob/fbe4ebb0/+/_WORK/ki/messages.md?plain=1#L14). Most lines were already read in [restart-consolidate.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/restart-consolidate.report.md). Each line below was checked against this work's [queries.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/queries.md), [decisions.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md) and `design/` notes, and against ki-agentic-harness `main` at `0f671e4f`.

## Dispositions

| Line | Carried by, or status | Next step |
| --- | --- | --- |
| INTERACTIVE-QUERIES, with SELF-CONTAINED and PASS-PROMPT | Open query QUERY-RULES in `queries.md`, which names hnr's prompt as the interactive-pass form. The [standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#coordinating-practices) has only its Questions bullet. Kris's personal `communication.md` already carries the rules. Kris: "the default is to log them in the summary ... But I might ask ... to go through them interactively"; "these new style prompts are amazing ... I get a lot more context from them". | None until Kris answers QUERY-RULES. On a), the coord-standard run writes an Interactive pass subsection with hnr's prompt verbatim. |
| WORK-PROCESS-NOTE | Not carried. The [Work Process note](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) never mentions a secondary State of play, though the standard's [Secondary States of play](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#secondary-states-of-play) does. hnr recommended one line, at medium confidence. | Fold the line into the Work Process note record that [model-shape-report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/model-shape-report.md) step 2 already plans under the Enactment Process. No separate query is needed. |
| KI-SOP-PATTERN | Carried: the standard's Secondary States of play, harness `111b853a`, merged to `main` in `703384eb`. Kris: "it makes the most sense to have always a main and then some secondary ones". | None. Dispose of the line. |
| SOP-SECONDARY | Carried: harness `703384eb` on `main`, and tools-ki `5da74e0a`, "secondary States of play and ki agent prompts", on `main`. | None. Dispose of the line. |
| CENTRAL-TICK | Not carried. The restart list put it on the [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) Project note as an idea, but the note has no such line. Kris: "a scheduled job that runs for each territory against its capital, and it checks to see if anything has moved past its last tick point ... Just an idea to take forwards." | Add one idea line to the Project note, beside the deferred launchd option. Under the style, the completion watcher still comes first. |
| COORD2-RUBRIC | Partly carried. The title check was fixed in harness `0aa9c4d2`. The optional `label` check at [coordination.ts:372](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/scripts/rubric/contexts/coordination.ts) still calls `projectLabel(label, project)` without the Project title, so it still compares against the slug. | Put the one-line fix, passing the Project note's `title`, into the next ki-coordination harness run (coord-standard). |
| INITIATIVES-RESIDUE | Open query THEME-CLOSE. Checked again on this run: legal-principal has 7 files in `Streams/Initiatives/`, no `Streams/Themes/` and one `initiative:` field. hnr-principal has no Initiatives folder and one `initiative:` field. Personal has migrated. Kris: "does Knowledge Islands still support initiatives? If so, we need to path that back to Knowledge Islands to get that fixed". | None until Kris answers THEME-CLOSE. On a), State of play sends the Legal and HNR migration lines. |
| THEME-REGISTRY-ENFORCE | THEME-CLOSE again, for the checker failures and their date. The every-territory registry half is State of play's own THEME-REGISTRY query in [ki/queries.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/queries.md). Kris: "make sure that that is what is happening across all the rest as well, and make sure that that is enforced mechanically now." | On the THEME-CLOSE date, one harness run turns the warnings in ki-coordination, ki-work-roadmap, ki-work and ki-repo-kb-activities into failures and closes the tolerance-window text. A line goes to ki.tools-burndown for `registry.ts`. |
| OP-CACHE-RULE | Carried: the [background-run standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md) states the `op_cache` rule with `OP_CACHE_SERVICE_ACCOUNT_ONLY=1`, enacted in harness `1ec09f15` on 23 October. Kris: "I really need the OP cache doing, please." | Narrow RUN-SECRETS to the Cloudflare half, since its option b) "1Password half now" has already landed. |
| CF-UNIFORM | Open under RUN-SECRETS. Neither the background-run standard nor `ki-repo-website-cloudflare` names `~/bin/cf_token`. Kris: "anything to do with my Cloudflare setup in reality should be uniform across whichever territory I'm working in. It shouldn't be baked into the territories information". | None until Kris answers RUN-SECRETS. Then one harness run adds a sentence beside the `op_cache` rule and the matching line in `ki-repo-website-cloudflare`. |
| MOD-LEDGER | Carried: [_ISSUES.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/_ISSUES.md) reads `MOD: 10` and reserves through `010`, set by tending-fold. | None. Dispose of the line. |
| WORK-STATUS-FORM | Not carried. The restart list routed it to ki.tools-burndown, but that work's `messages.md` holds only AGENT-SEND-NO-RUN. | Send the drafted line below to ki.tools-burndown's `messages.md`. That work brings Kris its own query. |
| PARTIAL-REPOS | Not carried anywhere. It is a model question rather than a method rule. The tooling gap, one source store per declared repository and ZONE-1's five zones, sits in `ki-repo-kb` and tools-ki. Kris: "I think we need [to] pass this concept over [to] Knowledge Islands [to] make [a] decision about effectively where we end up [with] partial repos ... Maybe we have work, like we [have] personal, we also [have a] work one ... I don't know how [the] split should be handled, really." | Query PARTIAL-REPOS. |
| CHEZMOI-REMIT's no-host rule, beside COORDINATOR-HOST | Open queries HOST-SEAT and HOST-TARGET in `queries.md`, from the model-shape report. The host requirement is piloted separately in ki.chezmoi. Kris: "coordination teams should use a hostname to understand who they're running on." | None until Kris answers HOST-SEAT and HOST-TARGET. |
| REPO-METADATA's method half | Carried by [repository-metadata.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/repository-metadata.md): its Other territories sections, short answers to the pilots' open points, and the `territory_code` pointer to `ki-repo`'s territory selection standard that PERSONAL-RESERVED asked for. Still open in the note: optional or shape-scoped tag types, and whether READMEs may restate descriptions. The `ki-repo` half waits in [ki.baseline-rollout's messages.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/messages.md), yet that work's `work.md` puts "harness skills and standards" out of its scope and with ki.ways-of-working. Kris: "Can you take this and give to WoW also?" | Query KI-REPO-HOME. The note graduates once the `ki-repo` change lands. |

## PERSONAL-RESERVED findings

PERSONAL-RESERVED's pointer request is done: the metadata note's `territory_code` now cites the territory selection standard. Its two prefix-survey findings both concern ki-agentic-harness, which has no work package.

### The 24-character `repo_code` cap

- **Where it lives:** only in code, in the shared identifier grammar [work-identifiers.ts](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-repo/scripts/shared/work-identifiers.ts), as `REPOSITORY_CODE = '[A-Z0-9][A-Z0-9-]{1,23}'`. It is canonical in `ki-repo` under ADR-KI-HARNESS-SKILLS-015, with materialised copies such as `ki-repo-kb-streams`. The `ki-repo` [repository standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-repo/references/standards-repository.md) says only that `repo_code` is a "stable uppercase" code. No standard text states the limit, or that it includes the issuing area.
- **Owner:** the `ki-repo` standard in ki-agentic-harness. Which work carries the change is KI-REPO-HOME. Personal has already shortened its two site codes, so nothing is blocked.
- **Draft line**, for whichever work KI-REPO-HOME names:

  `- 2026-10-25 · REPO-CODE-CAP · from ki.ways-of-working, from Personal's PERSONAL-RESERVED prefix survey: the 24-character limit on a repository code, including any issuing area, exists only in ki-repo's shared grammar (skills/keystone/ki-repo/scripts/shared/work-identifiers.ts, REPOSITORY_CODE, ADR-KI-HARNESS-SKILLS-015); standards-repository.md calls repo_code only "stable uppercase". Please state the limit and that it includes the area in the ki-repo standard, with the rest of the ki-repo change. Personal has shortened its two site codes, so nothing waits on it. Not blocking.`

### The streams audit's missing legacy-prefix allowance

- **Where it lives:** two checks fail any record whose identifier does not start with the current `repo_code`. One is `ki-repo-kb-streams`'s [streams.ts](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-kb-streams/scripts/rubric/contexts/streams.ts) (`matchesRoadmapArea`, near line 297). The other is `ki-work-roadmap`'s [roadmap-evidence.ts](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/scripts/rubric/contexts/roadmap-evidence.ts) (`id.startsWith`, line 56). Neither standard describes how a code is renamed.
- **Owner:** work-record identifiers and their migration are in this work's scope ("work-record fields and their migration" in [work.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/work.md)). So this work owns the rule, and ki-agentic-harness receives the change. Because it is this work's own, no message is needed. The decision is query LEGACY-PREFIX, and the change rides a harness run under this work.
- **Draft line**, only if Kris routes it elsewhere:

  `- 2026-10-25 · LEGACY-PREFIX · from ki.ways-of-working, from Personal's PERSONAL-RESERVED prefix survey: the ki-repo-kb-streams streams audit (streams.ts, matchesRoadmapArea) and ki-work-roadmap's ROAD checks (roadmap-evidence.ts:56) fail every record not prefixed with the current repo_code, so a repo_code rename has no gradual path. Please write a repo_code rename into ki-work-roadmap as one sweep that renames every record and in-repository reference in one commit, pruned links keeping their pinned revisions; add a legacy-prefix allowance only if a later rename needs one. Not blocking: Personal's KB to PERSONAL rename runs as one sweep.`

## Other draft lines

WORK-STATUS-FORM, for ki.tools-burndown's [messages.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/messages.md):

`- 2026-10-25 · WORK-STATUS-FORM · from ki.ways-of-working, routed by the restart list: under TOOLS-KI-SHAPES a) (Kris, 20 October 23:16 BST), the work-status form that KI-TOOL-KI-CLI-160 and KI-TOOL-KI-CLI-149 wait on is yours to settle with Kris: --view routing beside the text views, full lines or keys, and whether v1 JSON compatibility is kept. Bring Kris the query from your own package. Not blocking.`

## Queries

### KI-REPO-HOME - which work carries `ki-repo` standard and checker changes

**Context:** State of play has queued REPO-METADATA's `ki-repo` change, the hyphen-only `ki-` topics and the `territory_code` and `territory_tag_types` keys, with ki.baseline-rollout. But that work's `work.md` puts "harness skills and standards" out of scope and gives them to ki.ways-of-working, while this work's scope covers the work model, coordination, delegation and work-record standards, not repository metadata. The repo-code cap wording would ride with whichever work carries the `ki-repo` change.

**Query:** Should ki.baseline-rollout carry `ki-repo` standard and checker changes, with its Out line narrowed to the work-model skills?

**Options:**

a) (recommended, confidence medium - needs blind review; repository metadata is baseline conformance across every repository, and State of play already routed it there) ki.baseline-rollout carries the `ki-repo` change, REPO-CODE-CAP included. Its `work.md` Out line reads "work-model harness skills and standards (ki.ways-of-working)".

b) ki.ways-of-working carries it, and its scope widens to `ki-repo`'s repository contract.

### LEGACY-PREFIX - how a `repo_code` rename passes the streams and roadmap audits

**Context:** both audits fail every record not prefixed with the current `repo_code`. A rename therefore has to happen in one sweep, or the repository fails its audit until every record has moved. Personal is renaming KB to PERSONAL that way now. An allowance, an optional list of former codes that existing records may keep while new records take the new code, would allow a gradual path. It would need both checkers and the tools-ki readers to change.

**Query:** Should a `repo_code` rename stay a one-sweep change, written into `ki-work-roadmap`, rather than gaining a legacy-prefix allowance?

**Options:**

a) (recommended, confidence medium - needs blind review; renames are rare and Personal's runs as one sweep, so documenting the sweep costs one paragraph where the allowance costs two checkers and tools-ki) Write the rename into `ki-work-roadmap` as one sweep: every record and in-repository reference in one commit, pruned links keeping their pinned revisions.

b) Add an optional legacy-prefix list accepted by both audits for existing records only, with new records required to use the current code.

### PARTIAL-REPOS - how a repository with only Pillars and Resources fits the model

**Context:** HNR keeps hnr-shared, a repository holding only Pillars and Resources, beside hnr-principal. ZONE-1 requires all five zones, and the registry binds one source store per declared repository, so hnr-shared cannot be declared. Its store is written up in tracked notes only, and `ki repo store` and the source audits do not see it. Kris asked Knowledge Islands to decide where partial repositories fit, and whether a person keeps a personal "work" knowledge base beside a person-agnostic company Capital, adding: "there's [a] kind [of] weird thing here we maybe need to come back to." This touches the Structure note, `ki-repo-kb` and tools-ki, beyond this work's method scope.

**Query:** Should PARTIAL-REPOS wait as an idea until Kris opens it, rather than starting a design now?

**Options:**

a) (recommended, confidence medium - needs blind review; Kris's own words defer it, and nothing is broken beyond HNR's tracked-notes workaround) Record it as an idea on the Ways of working Project note, with the HNR evidence linked, and start a `ki-work-design` brief when Kris opens it.

b) Start a `ki-work-design` brief now covering partial repositories, the personal "work" knowledge base and the store-binding gap.
