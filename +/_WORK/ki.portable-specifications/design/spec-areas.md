# Specification areas: knowledge, work and agent context packages

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Date:** 2026-10-19

Design note under `ki-work-design`, written by the run spec-areas-design on Kris's request at 14:17 BST on 19 October (decisions log entry "owner request, SPEC-AREAS"): three specification areas sit beside agentskills.io, the knowledge package acquire produces, the work package and the agent context package, and each is to be specified "within a skill that owns them for now, then we formalise out of them later". This note takes stock, proposes an owning skill and a spec outline for each, and proposes the runs that write them. Its open questions are in the run report, not here. It graduates when each spec has landed in its owning skill, and is deleted in the same change as the last one.

## Contents

- [Summary](#summary)
- [Common shape](#common-shape)
- [Knowledge package](#knowledge-package)
- [Work package](#work-package)
- [Agent context package](#agent-context-package)
- [One area or two](#one-area-or-two)
- [Relations](#relations)
- [Run sequence](#run-sequence)
- [Sources](#sources)

## Summary

| Area | What it is | Owning skill now | Spec file | Later KIS |
| --- | --- | --- | --- | --- |
| Knowledge package | Immutable source evidence one acquisition produces, going into an island | `ki-acquire` (exists) | `references/standards-knowledge-package.md` | Successor to the retired KIS-0002 |
| Work package | The five-file folder that holds one work's definition and state | `ki-work-package` (being rewritten) | `references/standards-work-package.md` (exists) | New KIS, after the model settles |
| Agent context package | Curated knowledge going out to an agent, revealed progressively | New skill, proposed `ki-context-package` | `references/standards-context-package.md` | New KIS; the retired KIS-0001 is input |

The acquire knowledge package and the agent context package are **two areas**: one is evidence going in, the other is curated knowledge going out ([One area or two](#one-area-or-two)).

## Common shape

Every spec follows the house references vocabulary in `ki-skills` (`standards-knowledge-islands.md`), which is closed: a spec is `references/standards-<area>.md`, its checks are `references/rubric.md`, its external basis is `references/sources.md`, and templates are in `assets/`. A `spec-<area>.md` file would break the vocabulary, so none is proposed.

Each spec carries the same five parts, so that a later KIS can lift it whole:

1. **Purpose** - what the package is for, and what it is not.
2. **Layout** - the folder, its files and what each holds.
3. **Required files and front matter** - a closed set of fields per file, with types.
4. **Conformance** - levels where they help, with each rule mirrored as a check in `rubric.md`.
5. **Versioning** - a declared format version in the package, and how the spec changes.

Versioning follows the three axes KI Specifications already sets in [versioning.md](/Users/krisbrown/workspaces/knowledge-islands/ki-specifications/docs/versioning.md): the spec document's semver, a schema `$id` major.minor where a schema exists, and the package instance's own identity. While a spec lives in a skill, its version is a `format_version` (or `format`) field in the package and a line in the skill's changelog; the KIS number comes only on formalisation.

The later path into a KIS is the same for all three: KI Specifications is dormant before v1 with no registered KIPs or KISs (the KI Specs plan stands, on hold until v1, per the decisions log entry KI-SPECS-PLAN), so each skill spec becomes a KIP when v1 opens, citing the skill file as the reference implementation, and the skill then points at the KIS instead of carrying the text.

## Knowledge package

**What it is.** The unit one acquisition run produces: a source's original content, its normalised records, assets, relationships and checksums, with a manifest saying where it came from, what was captured and what was left out. It is immutable evidence; an island triages and files from it, but never edits it.

**Where it is described today, and how current.**

- Retired [KIS-0002 Knowledge Export Package](https://github.com/knowledgeislands/ki-specifications/blob/32fc90020b218ba9c5b2704cc7649d01400247b4/specifications/KIS-0002-knowledge-export-package/README.md) and [KIP-000002](https://github.com/knowledgeislands/ki-specifications/blob/32fc90020b218ba9c5b2704cc7649d01400247b4/proposals/KIP-000002-knowledge-export-package/proposal.md) (July 2026): the layout `kep/kep.toml`, `source/originals/`, `source/records/`, `assets/`, `relationships/native.jsonl`, `checksums/sha256sums.txt`, and a deterministic `package_id = kep:sha256:<payload_sha256>`. Deleted from the repository; history only.
- [tools-ki acquisition spec](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/specs/acquisition.md): current requirements. ACQUIRE-001 calls the output a "Knowledge Exchange Package conforming to the KIS-0002 payload layout": the name drifts from "Export", and it cites a KIS that no longer exists.
- [kep.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/acquire/chatgpt/kep.ts): current code; the ChatGPT adapter still emits a KEP, and acquire holds such packages (for example `captures/knowledge-islands/chatgpt/account-export-2026-09-22/<date>-<slug>/` with `kep.toml`, `source/`, `relationships/`, `checksums/`).
- [Granola layout](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/acquire/granola/layout.ts): current code, a different shape: `captures/<territory>/granola/<date>--<slug>--<source_id>/` with `meeting.md`, `routing.json` and `source-variants/`, plus a ledger.
- [ki-acquire standards](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/acquire/ki-acquire/references/standards-acquisition.md): current common contract for acquisition, but not a package format.
- [Acquisition Process](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Acquisition Process/Acquisition Process.md>) (updated 19 October): current; its "Provenance package" section lists the required contents (original content, source identity, timestamps, assets, provenance, declared omissions, content hash, repository context), and it says "A portable specification waits until two source mechanisms are staged through a common record". [ADR-KI-PRINCIPAL-001](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-001-provider-neutral-knowledge-acquisition.md) fixes the stages.
- The July handoffs for the downstream steps, [KBEP](https://github.com/knowledgeislands/ki-agentic-harness/blob/0b4f7732640af6ceda02668d3be901751b02bc26/+/_HANDOFFS/KBEP-knowledge-base-extraction-protocol.md) and [KBIP](https://github.com/knowledgeislands/ki-agentic-harness/blob/0b4f7732640af6ceda02668d3be901751b02bc26/+/_HANDOFFS/KBIP-knowledge-base-ingress-protocol.md), and their assessments [KI-SPEC-KIN-001 (pruned)](https://github.com/knowledgeislands/ki-specifications/blob/205f744c7ddaf3507c9d9e1c51d28a2cd6c6be02/docs/roadmap/KI-SPEC-KIN-001-assess-kbep-extraction-protocol.md) and [KI-SPEC-KIN-002 (pruned)](https://github.com/knowledgeislands/ki-specifications/blob/205f744c7ddaf3507c9d9e1c51d28a2cd6c6be02/docs/roadmap/KI-SPEC-KIN-002-assess-kbip-ingress-protocol.md): history only, out of scope here.

So the description is current but scattered, and the two built sources disagree on shape. The Acquisition Process's own condition, two sources staged through a common record, is what this spec would satisfy.

**Owning skill now.** `ki-acquire`, which already owns the provider-neutral acquisition contract; the per-source skills (`ki-acquire-chatgpt`, `ki-acquire-granola`) conform to it. tools-ki keeps the implementation and its requirements, which then cite the skill spec instead of KIS-0002.

**Where the spec lives.** `skills/acquire/ki-acquire/references/standards-knowledge-package.md`, with a manifest template in `assets/` and checks in the existing `references/rubric.md`. `standards-acquisition.md` keeps the process and links to the package spec.

**Spec outline.**

- _Purpose:_ immutable, provider-neutral evidence of one capture, sufficient for triage and filing without going back to the source.
- _Layout:_ KIS-0002's layout as the base, since it is the only shape with a deterministic identity, with Granola's `meeting.md` treated as a normalised record under `source/records/` and `routing.json` as an optional routing file. Whether Granola moves to the common layout or the spec admits a source-specific layout under a common manifest is a design choice for the spec run.
- _Required files and front matter:_ the manifest (TOML, as built) with `format`, `format_version`, `package_id`, `[source]` with `capture_boundary`, `[connector]`, `[inventory]`, `omissions` and `normalisations`; checksums over the payload. These map one-to-one onto the Acquisition Process's provenance-package list.
- _Conformance:_ identity reproducible from the checksums; every declared omission present; no edits after sealing. A capture mark stays acquire's preservation boundary, as acquire's conversations guide sets it.
- _Versioning:_ `format_version` in the manifest; package identity is the content hash, so a package has no semver of its own.

**Later path into a KIS.** A KIP that supersedes the retired KIS-0002 when KI Specifications opens v1, after the second source is staged through the common manifest.

## Work package

**What it is.** The folder `+/_WORK/<id>/` holding one work's definition (`work.md`), state (`state.md`), queries, message queue and decisions log, read in four levels from register front matter down to on-demand detail. It is the work model's unit of record.

**Where it is described today, and how current.** [design/work-package.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/work-package.md) is the finalised design (19 October). The harness [`ki-work-package`](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/SKILL.md) skill, with `references/standards-work-package.md`, `rubric.md` and `sources.md`, is being rewritten to it now by the run work-package-standard. Both are current; neither was touched by this run.

**Owning skill now.** `ki-work-package`. No change.

**Where the spec lives.** `references/standards-work-package.md`, as already placed. It is a spec in substance: layout, closed front matter, size limits and progressive reveal are all in the design.

**Spec outline: what is there and what to add.**

- _Purpose, layout, required files and front matter:_ present in the design (five files, closed field sets for `work.md` and `state.md`).
- _Conformance:_ the rubric mirrors the rules; what the spec run adds is a short conformance statement naming which checks a reader such as `ki work status` relies on, so another tool could read a package.
- _Versioning:_ missing. Add a format version, either a `format` field in `work.md` front matter or the version `ki work status` already emits (`ki/work-status/v1`) declared as the package format. The Open question is whether a package declares its own version or the reader alone does; the spec run should propose, not decide.
- _Stable definition:_ the agentspecs-scan's optional sentence (query AGENTSPECS-DEFINITION, edits to the definition cite a decision) belongs here if Kris takes it.

**Later path into a KIS.** A new KIS once the model has run unchanged through a few works and the migration has landed; until then the skill is the spec.

## Agent context package

**What it is.** Knowledge prepared for an agent to load: a short manifest that says what the package covers, how relevant, authoritative and current it is and how to find more, a body read next, and detail read only on demand. It is curated output from islands, going out to agents, rather than evidence coming in.

**Where it is described today, and how current.** Nowhere as a spec. The pieces are:

- acquire's [context/README.md](/Users/krisbrown/workspaces/personal/acquire/context/README.md) and its per-territory `context/<territory>/README.md` (moved out of `context/chatgpt/` on 19 October): provider-independent routing and bootstrap summaries for external agents. Current, in use, with no declared format.
- [KB-ACQUIRE-005 (pruned)](https://github.com/krisb/acquire/blob/9f09ba2235333e982cf62835959f68f89a73bda0/docs/roadmap/KB-ACQUIRE-005-seed-and-return-loop.md): seeds at `context/chatgpt/<territory-key>/seeds/<seed-slug>.md` with return fields `ki_project`, `ki_concept`, `ki_island`, `ki_seed`. Current, open.
- The [Agent Knowledge Model capture](/Users/krisbrown/workspaces/personal/acquire/captures/knowledge-islands/chatgpt/2026-10-15-agent-knowledge-model/README.md) (15 October): a progressive, skill-like knowledge interface and a candidate Knowledge Manifest (scope, relevance, provenance, authority, currency, discovery routes), with the flow intent, discovery, relevance and authority, selective loading, reasoning, acquisition, verification, improvement. Explicitly not for implementation in acquire now.
- Retired [KIS-0001 Knowledge Package](https://github.com/knowledgeislands/ki-specifications/blob/32fc90020b218ba9c5b2704cc7649d01400247b4/specifications/KIS-0001-knowledge-package/README.md) and [KIP-000001](https://github.com/knowledgeislands/ki-specifications/blob/32fc90020b218ba9c5b2704cc7649d01400247b4/proposals/KIP-000001-knowledge-packages/proposal.md) (July 2026), with the still-present informative [schema](/Users/krisbrown/workspaces/knowledge-islands/ki-specifications/schemas/knowledge-package.schema.json) and [examples](/Users/krisbrown/workspaces/knowledge-islands/ki-specifications/examples): a "portable, self-describing, governed unit of shared cognitive work", with digests, terminology, decisions, assumptions, open questions, provenance, handover and Minimal, Standard and Extended conformance. This is the oldest agent-knowledge spec found and the likeliest meaning of "an older agent knowledge spec", but that is inferred (run report, query OLD-SPEC).
- [Google Open Knowledge Format](</Users/krisbrown/workspaces/personal/personal-principal/Pillars/Technology/AI/Google Open Knowledge Format.md>) (OKF v0.1, June 2026): an external "vendor-neutral" markdown and YAML front matter format for agent knowledge bundles. A reference shape, like agentskills.io, not ours.

**Owning skill now.** None exists. Proposed: a new harness skill `ki-context-package`, under the knowledge skills beside `ki-repo-kb`. `ki-repo-kb` owns the island's internal method and is already large; `ki-acquire` owns evidence coming in, the opposite direction. A new skill keeps each skill to one unit of comprehension.

**Where the spec lives.** `references/standards-context-package.md`, with a manifest template in `assets/`, checks in `rubric.md`, and agentskills.io, OKF and the retired KIS-0001 in `sources.md`.

**Spec outline.**

- _Purpose:_ let any agent, in any runtime, find and load the right island knowledge for a task without reading the island.
- _Layout:_ the agentskills.io shape: a directory named for the package, a manifest file read first, a body, and `references/` one level deep loaded on demand. acquire's `context/<territory>/README.md` becomes one conforming package per territory, and seeds become small packages or entries within one.
- _Required files and front matter:_ the manifest's front matter takes the Agent Knowledge Model's fields (scope, relevance, provenance, authority, currency, discovery routes), plus `name` and `description` as agentskills.io sets them, a source island and a generated-at time. KIS-0001's `digests`, `terminology`, `openQuestions` and `references` are candidate optional fields; its task, deliverable and handover fields are not, because the work package now owns those.
- _Conformance:_ the agentskills.io size bands for progressive disclosure (metadata small, body bounded, detail on demand); every claim traceable to its island source; a currency date the reader can check.
- _Versioning:_ a `format_version` in the manifest; package currency is a date, not a semver, because packages are regenerated rather than released.

**Later path into a KIS.** A new KIS that takes the retired KIS-0001's place in the numbering of ideas, not its content: it would cite KIS-0001 as prior art and OKF and agentskills.io as aligned external formats.

## One area or two

**Two.** The evidence:

- **Direction.** The knowledge package carries a source into an island (Acquisition Process steps intake to filing). The context package carries an island's knowledge out to an agent (acquire's `context/` exports, the Agent Knowledge Model's flow).
- **Mutability and identity.** A knowledge package is sealed, identified by its content hash and never edited. A context package is regenerated as the island changes and is identified by name and currency.
- **Audience and reading.** A knowledge package is read whole by a triaging agent or person. A context package is read progressively by an agent, manifest first, in the agentskills.io pattern.
- **Owner.** Acquisition is `ki-acquire`'s and the islands' ingress. Context is curated by islands for any agent; acquire hosts the exports only because external agents read them there.
- **Lineage.** The retired KIS-0002 (export package) is the knowledge package's ancestor; the retired KIS-0001 (knowledge package) is closer to the context package and the work package. The two were already separate specs in July.

They are similar in that both are folders with a manifest, provenance and checksums or dates, and they share a field vocabulary (source, provenance, currency). That shared vocabulary is worth one place, the knowledge package spec, which the context spec cites, rather than a merged area.

The name "knowledge package" is the snag: the retired KIS-0001 used it for what is here the context package, while Kris's request uses it for what acquire produces. The run report raises the names as a query.

## Relations

**To agentskills.io.** The context package is the agentskills.io pattern applied to knowledge rather than procedure, and should copy it closely: manifest with `name` and `description`, body, references on demand, size bands. The work package follows it by analogy, `work.md` read first as `SKILL.md` is, the other files on demand, as the work-package design already records. The knowledge package does not follow it: it is evidence, read whole, and its manifest is TOML for determinism.

**To the work package.** The work package records work; the other two record knowledge. A work package may cite knowledge packages as evidence in its decisions and may be given a context package as a starting load in a brief, but neither belongs inside a work folder, which is pruned and deleted at Finished. The retired KIS-0001 tried to be both a work and a knowledge unit; the split here gives its task and handover half to the work package and its digest and terminology half to the context package.

## Run sequence

1. **spec-knowledge-package** - in ki-agentic-harness `skills/acquire/ki-acquire/`, writing `references/standards-knowledge-package.md`, a manifest template and rubric checks; reads tools-ki and acquire, writes neither. Parallel-safe with the work-package runs: different files. Needs the package-name answer first.
2. **spec-context-package** - creates the new skill and its standards file. Needs the ownership, name and old-spec answers. Can run beside run 1, but is better after it so it can cite the shared provenance fields.
3. **spec-work-package** - adds conformance and versioning to `ki-work-package`'s `standards-work-package.md`. Chained after work-package-standard and no-alias-sweep, because both write the same skill.
4. **Blind review** of this note's medium and low queries, as Kris's request already authorises, before runs 1 and 2 launch.
5. Later, outside this work: a roadmap handoff to KI Specifications for the three KIPs when v1 opens, under the cross-repository choreography in root `AGENTS.md`; and a tools-ki handoff to fix ACQUIRE-001's "Exchange" wording and its citation of KIS-0002 once run 1 lands.

## Sources

Read only, on 19 October: the repositories and files linked above; ki-agentic-harness at `88cce3e5`, tools-ki at `a9571e5b`, acquire at `c8af3d4`; deleted KI Specifications text at `32fc900` and `205f744`; harness handoffs at `0b4f773`; the agentskills.io format from the local reference in `ki-skills` (`references/standards-agent-skills.md`), with no network access; the agentspecs-scan run report of 14:12 BST.
