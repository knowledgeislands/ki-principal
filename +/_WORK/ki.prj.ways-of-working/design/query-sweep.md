---
title: Query sweep
status: draft
---

# Query sweep

**Goal:** sort every open query in [queries.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/queries.md) into one of four buckets so Kris can clear most of them in a few bulk lines.

**Scope:** the 35 queries under `## Open` on 27 October 2026 at 00:10 GMT, including REL-X64-TIMEOUT, which arrived while the sweep ran; the one parked query (PERM-PROMPTS-SETTINGS) stays parked and is not sorted. Settled against [decisions.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md) up to its 23:42 GMT entry of 26 October and Kris's steer that night: "consistency and simplification ... less concerned with doing releases ... everything should be linked locally".

**As of:** 2026-10-27 00:10 GMT.

Nothing in this note changes `queries.md`. Each bucket ends with one bulk decision Kris can give in a line; the coordinator then applies it to `queries.md` and the decisions log.

## Totals

| Bucket | Count |
| --- | --- |
| Q1. Stale or overtaken: drop | 4 |
| Q2. Not worth deciding now: park | 16 |
| Q3. Take the recommendation | 12 |
| Q4. Needs Kris's real attention | 3 |
| Total open | 35 |

## Q1. Stale or overtaken: drop

| Tag | Subject | Reason |
| --- | --- | --- |
| STRUCTURE-1 | `ki.specifications` holds no regular work file | Overtaken by SPEC-ORPHAN-OWNER, which traced the same folder in full: `work.md` was renamed to `ki.portable-specifications` and the folder holds only untracked copies of run reports. |
| BIO-1 | A separate BIO-1 configuration unit | Neither audit raised a BIO-1 finding, so there is nothing to bound; the query's own recommendation is to drop it. |
| CI-WATCH | How a run observes CI when the GitHub API is closed to it | Overtaken by Kris's 23:42 GMT steer on 26 October: releases and CI are deprioritised, and CI may be disabled rather than watched. |
| BASELINE-COMMITS | Whether a baseline commit may sweep in work-folder reports | Already answered by the standing `ki-git` rule, which forbids whole-tree staging with no baseline exception; the sweeping commits are past, and tracing which tool made them is overhead the steer does not want. |

**Bulk decision:** drop Q1 as listed.

## Q2. Not worth deciding now: park

Each is parked with one line and comes back only if it bites.

| Tag | Subject | Reason |
| --- | --- | --- |
| STEWARD-FIELD | Where a package records who looks after it | Reviews disagree; the harness carries the model with a marked placeholder, MOD-011 carves it out, and the Valle Armonia pilot can run on `worker` as it is. Comes back if the pilot needs it. |
| LEGACY-PREFIX | Whether a `repo_code` rename stays a one-sweep change | Renames are rare and Personal's is running as one sweep already; an allowance costs two checkers and tools-ki. Comes back at the next rename. |
| PARTIAL-REPOS | How a repository with only Pillars and Resources fits the model | Kris's own words defer it, and HNR's tracked-notes workaround holds. Comes back when Kris opens it. |
| UNATTENDED-FIELD | Recording unattended eligibility on records | A new record field, with reviews disagreeing, while the roadmap is being cut to next to nothing. Comes back if a window plan needs it. |
| UNATTENDED-AND-DUE-DATES | Adopting the eight criteria as the unattended assessment | Same subject as UNATTENDED-FIELD; the due-date half is done and the criteria stay Personal's prototype. Comes back with UNATTENDED-FIELD. |
| CLI-PREVIEW | Whether public state-changing commands write by default and preview with `--dry-run` | A fleet-wide tool convention while tools are "not ready yet" and releases are deprioritised; `mgit repair` is decided. Comes back when a repair command is next touched. |
| AREA-COLUMN | How the skill catalogue shows functional areas | The inline finder is live and works; the recommendation needs a harness change, a sync change and a new pin. Comes back if a harness refactor breaks the sync. |
| REPO-STANDARDS-SET | Which skills the Repository standards area lists | The live twelve serve; the difference is one box on one docs page. Comes back if a reader is misled. |
| MGIT-CACHE-SCOPE | What to build first for the mgit cache | Kris asked for the concept in plain language before answering; a new tool feature while tools are "not ready yet". The design note keeps the six routes. Comes back when Kris wants the cache built. |
| MGIT-CACHE-FAILED | Whether a failed checkout goes into the cached set | Same feature as MGIT-CACHE-SCOPE; Kris said "deal with concept first". Comes back with it. |
| RECORD-2 | Work-package schema failures in thirteen folders | Forty judgement fixes across live packages, with reviews disagreeing on who makes them; the full audit now runs only in CI. Comes back when the work-package standard settles or a package is next tidied. |
| FOLDER-1 | Extras in two work folders | A rename of ten old reports and a script's home; the review found the counts wrong, so it is not safe to bulk-accept. Comes back when those packages are next tidied. |
| COORD-7-REST | Fifty-one identifiers in reports with no local target | A known floor in old run reports that marks will prune; fixing it needs a fetch and a rewrite run. Comes back if the reports survive pruning. |
| LINT-WHERE | Where generated Markdown gets linted | The check-only staged hook that landed on 26 October (COMMIT-VS-CI, FORM-VS-RUMDL) now stops a bad report at commit, with CI the backstop; a generator check is extra machinery. Comes back if bad reports still reach `+/_WORK`. |
| MISSING-TOOLS | Installing the missing hook tools in three package repositories | The recommendation is itself to wait for the second convergence; installing would add new software. Comes back at that convergence. |
| REL-X64-TIMEOUT | darwin-x64 packaging fails on three five-second test timeouts | A test-only fix and a v0.14.2 release, while Kris deprioritised releases on 26 October; the query's own note says it stands or falls with the releases-and-CI decision. Park with v0.14.1 unpublished; comes back if Kris reopens releases. |

**Bulk decision:** park Q2 as listed, one line each under `## Parked`.

## Q3. Take the recommendation

High confidence and low risk. Each row gives the recommended option's words, shortened only where marked.

| Tag | Subject | Recommended option |
| --- | --- | --- |
| SPEC-ORPHAN-OWNER | The orphan `+/_WORK/ki.specifications/` folder | Owner ki.portable-specifications. Send one line to its `messages.md` naming the folder and its 25 reports; when its steward next tidies, it checks each report's outcome has a durable home, its queries are carried, and live references still work, then deletes only the eligible reports, each by explicit path; nothing is deleted before that check. |
| RADAR-REPORT-HOME | `radar-confirm-2.report.md` cited from KI-HARNESS-REV-012 | Owner ki.chezmoi. A bounded run repoints REV-012's citation to the public ThoughtWorks Radar and FAQ pages plus UE-108's section, and replaces UE-108's self-citation of the dead path with the same public pages and the 24 October check date; two small `docs(roadmap)` commits, one per repository, with REV-012 kept at triage. |
| FALLBACK-DATE | The HOLD-1 fallback review date for the trades hold | Keep 2026-12-31. |
| FILENAME-0 | OPEN.md in the ki-design decisions directory | Move it to `docs/OPEN.md` and repoint the generator and links. |
| ROUTE-1 | `docs/spec` is ki-design's live design specification | Adopt ki-specs: rename to `docs/specs/`, add the ki-specs front matter in one run and repoint the links; the two hex-terrain proposals stay draft. |
| GH-LIVE | Nine GitHub settings findings in ki-design | Authorise one run with the GitHub call lifted for `knowledgeislands/ki-design` only, applying the declared settings through `ki repo conform`. |
| MIRROR-TOKEN | The Notion integration token and 1Password item | Revoke the integration in Notion and delete the 1Password item after `chezmoi apply` removes the last reference; finish any HNR Notion page removal that needs the integration first. Kris's own action. |
| MIRROR-NOTE | The Notion Mirror chapter note in ki-principal | Delete the folder and the three inbound mentions, and record the retirement as one dated line in Known Lands, all under one Enactment record. Accepting here is the owner approval that stands in for the record. |
| MIRROR-SITE | The public website's project card for the mirror | Remove the card and the two data entries, regenerate the SVGs from ki-design and rebuild. |
| MIRROR-FRONTMATTER | The 274 notes carrying mirror frontmatter in HNR | Ask HNR to strip the five keys in one bounded run after the Notion removal finishes, updating Frontmatter Conventions and the two scripts that read them. HNR owns the run. |
| EXTRA-WRITES | The `.rumdl.toml` refresh the hook convergence proposed | Accept the hook commits as made and queue one bounded run to commit the `.rumdl.toml` refresh per repository. |
| RENAMED-5G | `.ki.toml` in the four renamed 5g-emerge repositories | One run, four one-line commits repointing the repository field, then the hook commits. |

**Bulk decision:** take a) for Q3 as listed.

## Q4. Needs Kris's real attention

These three stay in `queries.md` in full.

| Tag | Why it needs Kris |
| --- | --- |
| MOD-011-ADOPT | Adopting a record into Now is Kris's call alone, and it is the one Enactment of the Work Process note the harness already runs ahead of; the roadmap sweep's bucket D names it too. |
| ANSWER-VECTOR | Medium confidence with the blind review disagreeing, and it sets the Observatory's first slice, which Kris wants finished within hours. The simplification steer favours a), the existing file effect with no tools-ki change or pin. |
| NAMING-TO-KI | An estate-wide naming convention with a message to every territory; high and reviewed, but a policy adoption rather than a repair. |

**Bulk decision:** none; answer each by tag.
