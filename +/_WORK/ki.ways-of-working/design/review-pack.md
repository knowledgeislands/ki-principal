---
note_type: streams/design
updated: 2026-10-26T21:55:00Z
author: Written with Claude
---

# Review pack - Ways of working, 26 October 2026

**For:** Kris Brown · **Work:** `ki.ways-of-working` (KI > Model > Ways of working) · **Written:** 26 October 2026, 21:55 GMT · **Replaces:** the 25 October review pack, which was written for a chat model to read aloud

This is the one document to read. It says where the Ways of working work stands tonight, what has been done since 24 October, what you decided today, what is running now, and what is still waiting on you, with every term explained the first time it appears. You should not need to open anything else to decide; the links are there if you want to check.

A word on the vocabulary before the detail. **Knowledge Islands** is the family of repositories and tools you work in. A **work** is one piece of coordinated effort; this document is about the work called `ki.ways-of-working`, which defines how you and the agents work together. Each work lives in a **work package**, a folder of five files in the Knowledge Islands Principal repository (`+/_WORK/ki.ways-of-working/`): `work.md` says what it is, `state.md` where it stands, `queries.md` what it is asking you, `messages.md` what others have sent it and `decisions.md` what you have decided. A **query** is a question put to you with a recommended answer. A **run** is a background agent launched to do one bounded unit of work and report back. The **harness** is the `ki-agentic-harness` repository that holds the **skills**, the written rules the agents follow. The **ki** command is the tool from `tools-ki` that installs the harness, runs the audits and launches runs. The full glossary is at the end.

## Contents

1. [In one page](#1-in-one-page)
2. [What has been done since 24 October](#2-what-has-been-done-since-24-october)
3. [Decided today](#3-decided-today)
4. [In flight](#4-in-flight)
5. [Your open decisions](#5-your-open-decisions)
6. [Glossary](#6-glossary)

## 1. In one page

- **The documentation is published.** The Knowledge Islands website now has 43 documentation pages across ten sections (skills, ways of working, the `ki` command, the harness, knowledge, standards) with 35 inline diagrams. A rendering fault that blanked every diagram was found and fixed this morning. Start at <https://knowledgeislands.info/docs/>.
- **The rules for working unattended are written down.** The skills now say what an agent may do while you are away: nothing that could cut you off or take a site down, no new software, no messages to people, no assumed answers, a question waits two minutes and then nothing is done on it. These came from your answers on 25 October.
- **Most repositories are fixed, twelve wait on one release.** Of the twenty Knowledge Islands repositories with continuous integration, the library and tool drift is fixed everywhere. Twelve are red for one reason only: the released `ki` v0.13.0 checks for a folder the repositories have since renamed. Release v0.14.0 failed on 25 October when the macOS build jobs ran out of memory. You decided this evening how to fix it, and the run to ship v0.14.1 and move the twelve onto it is working now.
- **You answered 23 questions tonight.** Three on the release chain and twenty more taken as recommended. Seven runs were launched or queued on those answers; one has finished. Section 3 lists every answer; section 4 says what each run will deliver.
- **Twelve decisions still wait on you**, plus one parked. Ten were open before tonight; two housekeeping ones arrived this evening. Two of the ten, both about the `mgit` cache, you asked to have explained from the concept up before you answer; section 5 does that first. None of the running work is blocked on any of them.
- **What you need to do:** read section 5 and answer what you can, by tag, in speech. Then the coordinator reads each answer back and launches the work it authorises.

## 2. What has been done since 24 October

Each item names the live page, commit or record, with any failure stated beside it. "Pushed" means committed and sent to GitHub; "green" and "red" are the state of a repository's automated checks on its main branch.

### Website documentation

Your instruction at 02:50 GMT on 25 October was to publish the whole of Knowledge Islands onto the website in detail, from a user's point of view, with diagrams, while you slept. The design was settled by two independent proposals (one from Claude, one from Codex) merged into one plan, [website-docs.md](website-docs.md). Ten delivery runs then built the pages in order.

- **Ten sections live.** Skills, Ways of working, Knowledge and Standards are new sections; the harness and `ki` sections were refreshed; Docs and Projects now share one navigation. Index: <https://knowledgeislands.info/docs/>.
- **Skills section.** What a skill is, how the 64 skills fit together (a skill map and ten area figures), the catalogue with a finder table, and skills by outcome. <https://knowledgeislands.info/docs/skills/how-the-skills-fit-together/>, <https://knowledgeislands.info/docs/skills/catalogue/>. Two provisional choices made here are open queries for you: AREA-COLUMN and REPO-STANDARDS-SET in section 5.
- **Ways of working section.** Ten pages: the work model, work packages, coordination, background runs, roadmap lifecycle, work design, trades, recurring work, findings and tending. <https://knowledgeislands.info/docs/ways-of-working/the-work-model/>.
- **The `ki` command.** Twelve pages refreshed to `ki` v0.13.0: 121 commands in eighteen groups, with a command-groups diagram. <https://knowledgeislands.info/docs/ki/command-groups/>.
- **Harness section.** Six pages refreshed and a new Agent environment page. <https://knowledgeislands.info/docs/ki-agentic-harness/how-the-harness-works/>.
- **Knowledge and Standards sections.** Knowledge bases; query, save and update; acquiring knowledge; recap and handover. Repository standards, decision records, engineering and Git, writing, diagrams. <https://knowledgeislands.info/docs/knowledge/knowledge-bases/>, <https://knowledgeislands.info/docs/standards/repository-standards/>.
- **Diagram pipeline.** Twelve diagrams vendored from the harness and 26 drawn for the site, with a build gate that checks them. Website commit [d547611](https://github.com/knowledgeislands/apps-knowledgeislands.info/commit/d547611).
- **Failure, fixed:** the website's deploy broke between 04:22 and 06:22 GMT on 25 October because the new diagram gate needed a harness skill the site did not carry. Fixed in the build only; readers saw nothing after 06:22.
- **Failure, fixed:** none of the 35 inline diagrams drew on any page. Each diagram's SVG contained blank lines, and the Markdown renderer treated everything after the first blank line as prose inside the drawing, so the browser abandoned it. Fixed at 08:27 GMT on 26 October in website commit [a2942ea](https://github.com/knowledgeislands/apps-knowledgeislands.info/commit/a2942ea), verified live. The run noted that its push bypassed two branch rules on the website repository (pull-request-required and a required build check) under the standing push rule; the rules themselves are yours to keep or relax.

### Unattended work: the rules

An **unattended window**, also called an away grant, is a period you authorise in which the coordinator keeps working without you. Two ran: one from 01:07 to 07:17 GMT on 25 October (you returned early) and one from 08:27 GMT on 25 October to 08:28 GMT on 26 October. Your answers before and during them became written rules in the `ki-delegation` and `ki-coordination` skills:

- **Criticality test.** A window never makes a change that could cut you off or take a site down: DNS, Cloudflare Access, routes, Zero Trust, credentials, connection-critical machine configuration. It may align GitHub settings, change Cloudflare build settings to get builds passing, and cut releases. Harness commit [a122a201](https://github.com/knowledgeislands/ki-agentic-harness/commit/a122a201).
- **Software.** Upgrading an installed library or tool is fine; no session ever installs new software. Chezmoi (your dotfiles) changes go ahead only after an independent review of the diff confirms they are needed and safe. Same commit.
- **External systems and people.** A window makes no change in a system other people see or rely on (Linear, Notion, Slack are the named examples) and sends no message to people, unless expressly part of the work. Confidential material is never made public without your word. Harness commit [6d3afe52](https://github.com/knowledgeislands/ki-agentic-harness/commit/6d3afe52).
- **Ask timeout.** A question put to you in a window waits a couple of minutes at most; unanswered, nothing is done on it and it comes back as a query. Silence is never consent. Harness commit [fdf9a604](https://github.com/knowledgeislands/ki-agentic-harness/commit/fdf9a604).
- **Window bookkeeping.** Every window end is recorded as local time with zone and as UTC (after the 25 October clocks confusion). A mark is struck at the window's start so the return report can walk through everything since. Packed questions are unpacked before you leave.
- **Design note.** The full treatment of unattended work, with the eight-criteria eligibility test and the open questions, is [unattended-work.md](unattended-work.md).

### Coordination and the work model: method changes in the harness

These are the rule changes you decided on 24 and 25 October and that runs wrote into the skills on 25 October. They govern how the coordinator and runs behave.

- **Commit cadence and push rule.** The coordinator commits the work package at every write, pulls fast-forward only into a clean checkout, and pushes everything stacked on main, other sessions' commits included, never forced. Your words on 25 October: "changes in the local working copy are blocking the pushing and pulling of the repositories". Harness commit [938c7546](https://github.com/knowledgeislands/ki-agentic-harness/commit/938c7546); the Work Process note in Principal updated in [ef668240](https://github.com/knowledgeislands/ki-principal/commit/ef668240).
- **Report shape.** The re-bootstrap report is a full report; the first reply after 30 minutes of silence gives a Summary; Done and In Progress window on the mark; the thread line is always last; an optional Findings section exists; a query below high confidence after review is split. Same harness commit.
- **Coordinator commands.** `hold`, `drain`, `resume`, `send` and `receive` are now words the coordinator understands. Same commit.
- **Work model.** The model-shape design ([model-shape-report.md](model-shape-report.md)) settled that one State of play thread looks after Project packages by explicit, committed assignment and acknowledged handover, never by inference from whether a thread is open; a record's `project` field finds its package but authorises nothing; and a host requirement constrains only device-dependent execution. Harness commit [1af72f2e](https://github.com/knowledgeislands/ki-agentic-harness/commit/1af72f2e). One piece, STEWARD-FIELD, is still open with you (section 5).
- **Due dates on records.** Roadmap records may carry an optional target date (due or milestone). Same commit.
- **Labels.** Work is named `<label> (<id>)` everywhere a session names it; roadmap sizes display as a shirt glyph with a letter. Harness commit [0404754a](https://github.com/knowledgeislands/ki-agentic-harness/commit/0404754a).
- **Skill-set definition.** [skill-set.md](skill-set.md) maps fourteen skills in five layers, the three session kinds and the bootstrap path, and found nine contradictions, ten gaps and five overlaps; six were fixed in harness commit [6f3497c5](https://github.com/knowledgeislands/ki-agentic-harness/commit/6f3497c5), the rest waited on tonight's answers (BOOT-HOME, RECAP-NAME, TRADES-FATE, now decided).
- **Findings in packages.** A work package may hold a `findings/` folder, closing a mismatch the method digest found. Harness commit [8897008f](https://github.com/knowledgeislands/ki-agentic-harness/commit/8897008f).
- **Housekeeping.** 184 stale run reports were deleted from this work package in two sweeps; 70 were kept because their outcome or query home could not be verified, and tonight's TIDY-GAPS answer traced the two remaining orphans (section 3).

### Getting the repositories green

**CI** (continuous integration) is the set of automated checks GitHub runs on every push. Every Knowledge Islands repository pins a `ki` version in its CI (the **pin**, a `KI_VERSION` or `.github/ki-version` value) and runs the `ki` audits at that version.

- **Pins moved to v0.13.0** across all twenty repositories; the install step passed everywhere. Sixteen stayed red for pre-existing reasons: library drift (**DEPS-1**: Bun 1.4.2 to 1.4.3 and two packages), a stale dependency checker version (**TEST-5**), two shell-script lint findings, document-structure rules in `ki-design` and `ki-principal`, and **DESIGN-2**.
- **Fleet fix.** A run fixed Bun, the checker version and the shell findings across sixteen repositories in clean clones, pushed fast-forward. `tools-mgit` and `ki-techne-harness` went green. Report: [wow-fleet-green.report.md](../wow-fleet-green.report.md).
- **DESIGN-2 explained.** The released `ki` v0.13.0 looks for the dependency-checker folder at `tooling/boundaries`; the repositories renamed it to `tooling/depcruise`. Every local audit against the current harness passes. Twelve repositories, and the website, fail on this alone, and it clears the moment they pin a `ki` release that knows the new name. That release is v0.14.1, in flight now.
- **`tools-ki` green** for the first time since 21 October, on 25 October at 13:23 GMT, after its own pin and a test-only fix. Commit [1d65a32e](https://github.com/knowledgeislands/tools-ki/commit/1d65a32e).
- **Harness main green** at [5cb52973](https://github.com/knowledgeislands/ki-agentic-harness/commit/5cb52973).
- **Still red:** the twelve DESIGN-2 repositories and the website (cleared by v0.14.1); `ki-design` and `ki-principal` on document rules, which a run is fixing now under your CI-RED-DOCS answer (section 4).
- **HNR checkout levelled.** The `hnr-principal` primary checkout had a published commit it could not reconcile; under your HNR-LEVEL answer it was reset to match origin tonight, nothing lost. Commit `923674cf` in that repository.

### The release

The **release chain** is how a new `ki` version reaches everything: `tools-ki` tags and publishes a release, a bot updates the **Homebrew tap** (the `homebrew-tap` repository that `brew install ki` reads), and the tap notifies the website and the harness to bump their pins.

- **Chain verified end to end.** A read-only run traced v0.11.5, v0.12.0 and v0.13.0 through every hop. The last hop had been failing silently because the website's main was red, so the bot's pull requests never auto-merged. The harness was enrolled as a consumer and a replay confirmed both consumers receive the dispatch. Tap commit [ef2ad37](https://github.com/knowledgeislands/homebrew-tap/commit/ef2ad37).
- **Failure: v0.14.0 did not publish.** Tag pushed on 25 October, but the release workflow's two macOS package jobs ran out of memory in one test file (`agent-control.test.ts`). Nothing was published; v0.13.0 remains the released version. Report: [wow-ki-pin-release.report.md](../wow-ki-pin-release.report.md). You decided the fix tonight (REL-MACOS-OOM, section 3) and the run to ship v0.14.1 is working now.

### Design work

Design notes live in this folder. Each is a brief, an independent review or two, a merged report and the queries it leaves you.

- **mgit cache** ([mgit-cache.md](mgit-cache.md)): your idea of a short-lived cache so a status sweep can feed the next command. Six routes weighed, three needing no cache, one Codex review merged. Three of its five queries you answered tonight; two remain and are explained in full in section 5.
- **Model shape** ([model-shape-report.md](model-shape-report.md)): how one State of play thread looks after several Project packages. Five of six queries decided and landed in the harness; STEWARD-FIELD remains.
- **Unattended work** ([unattended-work.md](unattended-work.md)): the window life cycle and the eligibility criteria. Eight of its ten queries decided; UNATTENDED-FIELD and UNATTENDED-AND-DUE-DATES remain.
- **Skill set** ([skill-set.md](skill-set.md)), **overview** ([overview.md](overview.md)), **tending** ([tending.md](tending.md)), **findings** ([findings.md](findings.md)), **interim cover** ([interim-cover.md](interim-cover.md)) and **repository metadata** ([repository-metadata.md](repository-metadata.md)): all of their open queries were decided tonight; the runs recording those decisions are queued.
- **Dry-run survey** ([wow-dryrun-survey.report.md](../wow-dryrun-survey.report.md)): how every Knowledge Islands command previews and writes today. Its one live recommendation is CLI-PREVIEW in section 5.

## 3. Decided today

Every answer you gave on 26 October, one line each, in the order taken. "As recommended" means option a) as it read in `queries.md`. The read-backs are in [decisions.md](../decisions.md) from 21:13 GMT.

**The three release-chain queries, taken interactively at 21:20 GMT:**

- **REL-MACOS-OOM** - "Fix test, cap heap and release v0.14.1". Cut the memory use of `agent-control.test.ts`, give the package jobs a heap ceiling, keep the full suite as the gate, tag and release v0.14.1, leave v0.14.0 unpublished. Launched wow-rel-0141.
- **TOOLSKI-DEPCRUISE** - "Fold into release run". Rename `tools-ki`'s own checker folder to `tooling/depcruise` in the same release, and bump its own pin once v0.14.1 installs. Folded into wow-rel-0141.
- **WEB-BUILD-ORDER** - "Reorder build before test" at the pin bump. When the website takes v0.14.1, the same commit runs the site build before the tests in CI. Folded into wow-rel-0141.

**The twenty high-confidence queries, answered "all" at 21:25 GMT:**

- **HNR-LEVEL** - reset the `hnr-principal` checkout to origin with `--keep`. Done tonight by wow-hnr-tidy.
- **CI-RED-DOCS** - one bounded batch fixes the mechanical document-rule failures in `ki-design` and `ki-principal`; content choices come back as queries. Running as wow-red-docs.
- **ACCEPT** - [KI-PRINCIPAL-MOD-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-MOD-009-amend-adr-001-staging-wording.md) accepted as done. Queued in wow-principal-records.
- **SUMMARY-VISIBLE** - the tap's notify job prints its dispatch line to the log; the release guide points at it. Queued as wow-tap-log, after the release.
- **TIDY-GAPS** - trace the owners of two orphan files before any repair. Done tonight by wow-hnr-tidy; the two owners became the two new queries in section 5.
- **MGIT-CACHE-EXPIRY** - a missing or expired cache set stops the command with a one-line error; a fresh empty set runs nothing. Recorded by wow-harness-b (queued).
- **MGIT-CACHE-TTL** - the cache lasts a fixed five minutes from the sweep's start. Recorded by wow-harness-b.
- **MGIT-PUSH-ALIAS** - the no-cache `mpush` guard alias goes to the chezmoi work as a message. Sent by wow-harness-b.
- **WAKE-SUBSTRATE** - write the headless coordinator-pass contract into `ki-coordination`, then hand the launchd check job to the chezmoi and Mac Studio works. wow-harness-b.
- **SINGLE-THREAD** - capture a Principal record to amend the Work Process note through the Enactment Process, and open a one-wave pilot on one Valle Armonia Project package. Queued in wow-principal-records.
- **SOP-PROJECT-CARE** - disposed as already carried by the model-shape decisions; STEWARD-FIELD is the one piece still due.
- **BOOT-HOME** - `ki-bootstrap` owns one machine-readiness checklist ending "Ready to coordinate"; `ki-coordination` cites it before the opener. Running in wow-harness-a.
- **RECAP-NAME** - the recap command's argument becomes `checkpoint <work id>`. wow-harness-a.
- **TRADES-FATE** - narrow `ki-trades` to the routes the trade policy grants, point handoffs at `messages.md`, keep existing trades. wow-harness-a.
- **DIAGRAM-PRIVATE-CITATIONS** - diagrams in private repositories may cite `path:revision:lines` with no URL. wow-harness-a.
- **INTERIM-REPAIR**, **INTERIM-FINDING-WRITER**, **INTERIM-FINDING-AGE**, **INTERIM-HOMEPAGE-OMISSION**, **INTERIM-TAG-SCOPE** - each as recommended, recorded in its design note and in the standard that already holds the topic. wow-harness-b.

**Not answered, by your choice, at 21:44 GMT:**

- **MGIT-CACHE-SCOPE** - "I need more context, what are routes?"
- **MGIT-CACHE-FAILED** - "deal with the concept first".

Both are explained from scratch in section 5 before they are asked again.

**And this pack:** "is there somewhere I can easily read and understand all of this?" Launched wow-review-pack-5, which wrote this document.

## 4. In flight

As of 21:49 GMT. A run is "running" when its agent is working, "queued" when it waits for a slot, "finished" when its report is in. About three runs work at once.

| Run | State | What it delivers |
| --- | --- | --- |
| wow-rel-0141 | Running: full test suite in its worktree | Fixes the memory use of the failing test, caps the heap in the macOS package jobs, renames `tools-ki`'s checker folder, tags and publishes `ki` v0.14.1, then bumps the pin in `tools-ki`, the twelve DESIGN-2 repositories and the website (with the build-before-test reorder), watching each CI run go green. Brief: [wow-rel-0141.md](../briefs/wow-rel-0141.md). |
| wow-harness-a | Running: tests and audits after regenerating the catalogue | Four skill changes in the harness: RECAP-NAME, TRADES-FATE, BOOT-HOME and DIAGRAM-PRIVATE-CITATIONS, with a message to `tools-ki` for a later readiness check and one to Personal for two records. Brief: [wow-harness-a.md](../briefs/wow-harness-a.md). |
| wow-red-docs | Running: repointing references to renamed `ki-design` records | Fixes the mechanical document-rule failures in `ki-design` and `ki-principal` so their CI goes green; returns the content choices (record shape, folder shape, structure) as queries. Brief: [wow-red-docs.md](../briefs/wow-red-docs.md). |
| wow-review-spec-orphan | Running: blind review | A masked independent review of SPEC-ORPHAN-OWNER (section 5), because its recommendation includes a deletion. Its verdict may raise or hold that query's confidence. |
| wow-harness-b | Queued | Writes the headless coordinator-pass contract (WAKE-SUBSTRATE) into the harness; hands the launchd check job and the `mpush` alias to the chezmoi and Mac Studio works as messages; records the two mgit answers in the mgit design note; records the five INTERIM answers in their notes and standards. Brief: [wow-harness-b.md](../briefs/wow-harness-b.md). |
| wow-principal-records | Queued | Accepts MOD-009 as done; captures the Principal record for amending the Work Process note under the Enactment Process; sends Valle Armonia's State of play the one-wave pilot proposal and asks it to name the package. Brief: [wow-principal-records.md](../briefs/wow-principal-records.md). |
| wow-tap-log | Queued, after the release | Makes the tap's release dispatch line visible in the job log and points the release guide at it. Brief: [wow-tap-log.md](../briefs/wow-tap-log.md). |
| wow-hnr-tidy | Finished 21:45 GMT | Reset `hnr-principal` to origin (HNR-LEVEL, done, nothing lost) and traced the two orphan owners (TIDY-GAPS), producing SPEC-ORPHAN-OWNER and RADAR-REPORT-HOME. Report: [wow-hnr-tidy.report.md](../wow-hnr-tidy.report.md). |
| wow-review-pack-5 | Running | This document. |

Nothing in flight is waiting on an answer from you.

## 5. Your open decisions

Twelve queries, in five themes plus housekeeping, and one parked. Each theme opens with the idea in brief: what problem it solves, how things work today, what the choice changes, with a worked example. Then each query follows exactly as it stands in [queries.md](../queries.md): Context, Query and Options, the recommendation first with its confidence. Nothing in the options or recommendations has been changed.

How to read a confidence: **high** means the coordinator and an independent reviewer agree; **medium** means they disagree, or the question rests on one territory's evidence, and both views are shown. Where a query says "a masked blind review on Codex", an independent reviewer on a different model read the question with the options unranked and no sight of the recommendation.

You can answer by tag ("STEWARD-FIELD a") or with a bare letter in order. The coordinator reads each answer back before launching anything.

### Theme: the mgit cache

#### The idea in brief

**What mgit is.** `mgit` is your multi-repository Git tool from `tools-mgit`. It runs one Git command across every repository checkout in a set (a **sweep**), for example `mgit st` to see the status of all seventeen Knowledge Islands checkouts at once. The set of checkouts it acts on is the **selection**, chosen by a workspace manifest or a **selector** such as `--territory` or `--filter`. mgit learns what a command's normal, boring output looks like (a **template**, recorded with `mgit learn`) and then hides it, so a sweep shows you only the checkouts whose output was unusual. Those are **quiet** (matched the template, or printed nothing), **with output** (printed something unusual) or **failed** (the Git command exited with an error).

**The problem.** You sweep, see that three of seventeen checkouts need something (they are ahead, or dirty), and then want to act on just those three. Today the follow-up command runs in all seventeen again. For `push` that costs network time and prints "Everything up-to-date" fourteen times. For a follow-up that is not harmless on a clean checkout, such as `commit`, `stash` or `reset`, running everywhere is a wider blast radius than you meant. The information to narrow the second run exists at the end of the first; there is just no way to hand it back to mgit.

**Your proposal.** `mgit --to-cache st && mgit --from-cache push`. The first command records the checkouts whose status was not quiet. The second runs only in those. The cache lasts no more than five minutes; plain `mgit st` keeps working as now. You also asked the design to weigh ways that need no cache at all, such as an alias.

**Worked example.** Seventeen checkouts; `ki-principal` has two unpushed commits, `tools-ki` has one, `ki-design` has uncommitted edits, the other fourteen are level and clean. Today, `mgit st` shows three lines; `mgit push` then contacts all seventeen remotes and pushes two. With the cache, `mgit --to-cache st` shows the same three lines and remembers them; `mgit --from-cache push` contacts three remotes, pushes two, and tells `ki-design` there is nothing to push. If you come back ten minutes later and type `mgit --from-cache push`, it stops with "set is 10m old (limit 5m); re-run with --to-cache" and pushes nothing, which is the answer you gave tonight under MGIT-CACHE-EXPIRY.

**What a route is.** The design note weighed six ways of getting the effect, and called each a **route**, lettered A to F. They are not steps in a plan; they are alternatives, some of which work together. The first three need no cache at all, as you asked. Here is each in a paragraph, with an example.

- **Route A: use `mgit sync`, with direction switches.** mgit already has `sync`, which fetches every checkout, pushes the ones that are only ahead, pulls the ones that are only behind, and skips dirty or diverged ones with a reason. For "status then push" it already does the job, with two gaps: it also pulls, and the fetch costs the round trips you wanted to save. Adding `mgit sync --push-only` and `--pull-only` would let you choose the direction. Example: `mgit sync --push-only` pushes `ki-principal` and `tools-ki`, leaves dirty `ki-design` alone and names it. No cache, no new state, but it only ever covers push and pull under sync's policy.
- **Route B: a one-line guard alias, no change to mgit.** mgit can run a raw shell command per checkout. A guard that asks Git "is anything ahead of upstream?" and pushes only if yes already works today, and can live in your dotfiles as an alias called `mpush`. Example: `mpush` costs no network for the fourteen level checkouts and pushes the two that are ahead. You accepted this tonight under MGIT-PUSH-ALIAS. It covers push well and nothing else; each new intent would need its own hand-written guard.
- **Route C: teach `mgit push` itself to skip locally.** Build the "anything ahead?" check into mgit's `push`. Rejected by the design and the reviewer alike: mgit has no built-in idea of what any Git command's normal state is (that is what templates are for), and the check is wrong for the many pushes that do not push the current branch, such as `push --tags` or `push origin feature`.
- **Route D: your two flags, one slot, five minutes.** `--to-cache` records the non-quiet checkouts; `--from-cache` selects only those; one implicit slot; expires five minutes after the sweep began. General across every command and reads naturally with `&&`. Its open questions were what happens on expiry (you answered: stop), how the slot is keyed so a different workspace does not inherit a foreign set, whether failed checkouts count (MGIT-CACHE-FAILED, below), and how two sessions share one slot. The design answers the keying with a selection key and a membership check: the reader refuses if the selection differs, and checks every cached path is still a member today.
- **Route E: named sets.** The same two flags with an optional name: `mgit --to-cache dirty st` and `mgit --from-cache dirty ci -am "wip"`. Names carry intent and let two terminals or an agent and you work side by side without overwriting each other's set. The design takes this into the first cut as route D's isolation: a name is optional, and the two-word form uses a default slot. Listing and forgetting sets can wait.
- **Route F: an explicit path list in, from a file or standard input.** A selector `--repos-from FILE` or `--repos-from -` that takes checkout paths, one per line. mgit can already write its results out as JSON; this is the missing way to feed a set back in with no hidden state. Example: `mgit --json st | jq -r '.[] | select(.quiet == false) | .path' | mgit --repos-from - push`. Agents prefer it because the set is visible in the transcript. For you at a prompt it needs a pipeline, so it does not replace route D; it is the primitive D is built on, with `--to-cache` meaning "write the non-quiet paths to the slot file" and `--from-cache` meaning "`--repos-from` the slot file, if fresh and from this selection".

**What is already decided.** Route C is rejected. Route B is adopted today as the `mpush` alias. The expiry stops the command (MGIT-CACHE-EXPIRY) and the limit is a fixed five minutes (MGIT-CACHE-TTL). Nothing is built in `tools-mgit` until you decide the two below; the accepted shape then goes to `tools-mgit` as a message for it to capture as its own record.

**What the two open queries choose between.** MGIT-CACHE-SCOPE asks which routes form the first thing built: F and D together with E's optional name (one record), F and A first with D later, or D alone as you first proposed. The independent reviewer agrees with everything the first cut would contain but would ship F and A first and defer D until its isolation had been used; the design says the key, membership check, stop-on-expiry and optional name are that isolation, and that F alone gives you nothing at the prompt without a pipeline. MGIT-CACHE-FAILED asks, within route D, whether a checkout the sweep failed on (an `index.lock` left behind, a missing upstream, a broken worktree) goes into the cached set. The design would include it, so the set is a superset of everything needing attention; the reviewer holds that an unknown result should not become a target for a possibly destructive follow-up, and added a middle option: exclude it from the set but keep its name and count visible and warn on every `--from-cache` that the selection is incomplete.

#### MGIT-CACHE-SCOPE - what to build first

**Context:** Six routes were weighed. The Codex review and the note agree that `--repos-from` (an explicit path-list selector, route F) is the right primitive and that teaching `push` to skip locally (route C) is wrong. They differ on timing for your two-flag cache (route D): the reviewer would ship F and the `sync` direction switches first and defer D until isolation is specified; the note says the selection key, membership check, stop-on-expiry and an optional set name specify it, and that F alone gives you nothing at the prompt without `jq`.

**Query:** Which shape goes to `tools-mgit` as the first record?

**Options:**

a) (recommended, confidence medium - reviewed blind on Codex, which disagrees on timing, agreeing on everything the first cut would contain) `--repos-from` and `--to-cache [NAME]`/`--from-cache [NAME]` together, one record; `sync --push-only` and `--pull-only` as a second record.

b) `--repos-from` and the `sync` switches first; the cache flags as a later record once the primitive has been used.

c) The cache flags alone as you proposed, one default slot, no `--repos-from` and no name.

#### MGIT-CACHE-FAILED - whether a checkout the sweep failed on goes into the cached set

**Context:** In the mgit cache design, `mgit --to-cache st` records the checkouts needing attention for five minutes, and `mgit --from-cache push` acts on just those. A sweep can fail in a checkout, for example on an `index.lock`, a missing upstream or a broken worktree. The sweep's exit status of 1 already stops an `&&` chain, so `--from-cache` is reached after a failure only by `;` or a separate command, and the follow-up may be destructive. The design note recommends including failed checkouts (medium confidence). A masked blind review on Codex disagreed at high confidence: a failed sweep is an unknown result, not a confirmed target for a possibly destructive command. Both views are shown.

**Query:** Are checkouts the sweep failed on included in the cached set?

**Options:**

a) (recommended, confidence medium - reviewed blind on Codex, which disagreed: the design favours a superset needing attention, the reviewer holds that an unknown result should not be a target) Exclude them, but keep their names and count in the set as diagnostics, and warn on every `--from-cache` that the selection is incomplete. This is the reviewer's added option.

b) Include them, and show the count of failed candidates in the age line, as the design note recommends.

c) Exclude them silently, so the set holds only checkouts that ran and printed something.

d) Make `--from-cache` refuse to run while the set records any failed checkout, until the sweep is repeated clean.

### Theme: the work model

#### The idea in brief

**The pieces.** A **territory** is one group of repositories, such as Knowledge Islands or Valle Armonia. Each has a **State of play**, the one thread that watches over the whole territory's work. Within it, a **Project** is a named, longer-lived piece of work with its own work package; Ways of working is a Project. A **thread** is a session acting on a work; a Project may have its own coordinating thread, or none.

**The problem.** You want one State of play thread to keep every Project package in its territory sorted unless the Project has its own thread open. The design settled on 25 October (CASCADE-STEWARD, decided) that this is done by an explicit, committed assignment and an acknowledged handover when you open or close a Project's own thread, never by guessing from whether a thread looks alive. The work that holds the assignment is the package's **steward**. The steward is not the **holder**: the holder is whose move it is right now (the agent, you, or nobody while on hold), derived from `state.md`'s `state` field and `work.md`'s `worker` field; the steward is who looks after the package over time, whoever's move it is.

**What is left to decide.** Only where the assignment is written. Two candidate homes. One, reuse the existing `worker` field in `work.md`: it reads `agent` today, and would read `work/va` while Valle Armonia's State of play looks after a package, and `agent` again when the Project's own thread does. No new field, and the set of fields in a package stays closed. Two, a new dedicated field, say `steward: work/va`, kept distinct from the holder so that the thing pick-up reads (who moves next) is never confused with lasting responsibility.

**Worked example.** Valle Armonia has a Project package `va.sites` and no thread of its own. Under option a) its `state.md` or `work.md` gains `steward: work/va`, and `worker` stays `agent`; if you open a `va.sites` thread, the handover removes the steward line. Under option b) `work.md`'s `worker` becomes `work/va` while va looks after it and goes back to `agent` when you open the thread. Either way the holder is read the same, and the Valle Armonia pilot you approved tonight (SINGLE-THREAD) logs the assignment in va's decisions log until this lands.

#### STEWARD-FIELD - where a package records who looks after it

**Context:** The assignment needs a committed home that names a work, never a host or session. The brief proposed a new `state.md` field, `steward: self` or `steward: work/<sop id>`. Both reviews reject `self`, which is not a holder value, and both reject reading the assignment as the holder. The Claude review would reuse `work.md`'s existing `worker` field: `worker: work/va` when the State of play looks after the package, and `agent` when the Project's own thread does. That adds no field and leaves the closed field set unchanged. Stewardship changes only when Kris opens or closes a thread, the slow rate `work.md` suits, and the holder stays derived from `state` and `worker` as today. The Codex review wants a dedicated assignment with its own vocabulary, distinct from holder and session, and leaves the exact field to the design. A separate field keeps the assignment visible beside the state, and it avoids a third sense of "steward" only if it is named with care.

**Query:** Should the assignment be recorded in a new dedicated field rather than `work.md`'s existing `worker` field?

**Options:**

a) (recommended, confidence medium - reviews disagree; the Codex review and a masked blind review on Codex want a dedicated field, as lasting responsibility should not share a field with the holder that pick-up reads, while the Claude review prefers reusing `worker` as it adds no field) A new dedicated field, taking `work/<id>` values only, never `self`, changed or removed as part of the acknowledged handover.

b) Reuse `work.md`'s `worker`: `worker: work/<sop id>` while the State of play looks after the package, `agent` while its own thread does.

### Theme: unattended work

#### The idea in brief

**The problem.** When you grant an unattended window, the coordinator needs to know which roadmap records it may progress without you. Today the skills say what a window never does (the deny list) and what a coordinator may progress, but nothing says how a single record is judged eligible. Personal's State of play built a prototype: eight ordered criteria, each citing an existing rule rather than restating one, applied to a record in order until one fails. The first failure decides the verdict: **eligible** (all pass), **near-miss** (one answer from you would make it eligible, and the criterion names the question) or **attended** (needs you). Across Personal's 76 open records it sorted 9, 21 and 46. Eligibility is not authority: an eligible record still needs a grant that covers it.

**The eight criteria, in order.** No owner judgement needed; no outward act (nothing other people see); authority in one repository; reversible; the agent can verify its own result; unblocked; scoped (a bounded change); and an agent-sized step.

**Worked example.** A record "bump Bun to 1.4.3 in mcp-gsuite" passes all eight: eligible. A record "rename the `KB` prefix to `PERSONAL` across Personal's roadmap" fails at "no owner judgement" only if the new code is not yet chosen; if you have named it, it passes and is eligible. A record "publish the Valle Armonia site" fails "no outward act": attended. A record "fix the document rules in ki-design" fails "no owner judgement" because three rule classes need content choices, with the question "which record shape?": near-miss.

**Two questions remain.** UNATTENDED-AND-DUE-DATES asks whether these eight criteria, in their order with the three outcomes, become the standard assessment in `ki-delegation` now, or are piloted on a second territory first, or stay Personal's local prototype. UNATTENDED-FIELD asks where a verdict is recorded once assessed: as an optional `unattended` mapping on each record (verdict, the criterion that failed, the question if near-miss, the date assessed), refreshed when the record's status or horizon changes; or in a per-window planning note with no record field, since eligibility depends on the grant in force and can go stale. The due-date half of the original request was decided on 25 October and is live.

#### UNATTENDED-AND-DUE-DATES - adopt the eight criteria as the unattended assessment

**Context:** Kris, 24 October, through Personal's State of play: "we need to push that into the ways of working thread as something that we need to do an assessment of", and roadmap records should carry an explicit due date or key milestone date "of what they're working towards". The due-date half is done: DUE-FIELD was decided at 01:43 GMT today and harness `1af72f2e` added the optional `target` mapping (`date`, `kind` of `due` or `milestone`, `what`) to the `ki-work-roadmap` format standard, with the nearer date ordering work within one horizon and priority. The assessment half is not. Personal's prototype tests each record against eight ordered criteria, `no-owner-judgement`, `no-outward-act`, `one-repo-authority`, `reversible`, `self-verifiable`, `unblocked`, `scoped` and `agent-step`, the first failure deciding `unattended`, `near-miss` with one question, or `attended`; across 76 open Personal records it found 9, 21 and 46. Each criterion cites an existing rule rather than restating one, and eligibility is not authority. The open query UNATTENDED-FIELD asks only where a verdict is recorded (a record mapping or a per-window note) and bundles the criteria into that choice; the Codex blind review that kept it at medium asked for the criteria to be reviewed before they are standardised. Today `ki-delegation`'s unattended deny list says what a window never does and `ki-coordination`'s unattended windows section says what a coordinator may progress, but neither says how a record is judged eligible, and the format standard states "No unattended-eligibility field is adopted".

**Query:** Should the eight criteria, in their order with the three outcomes, become the eligibility assessment in `ki-delegation`, leaving UNATTENDED-FIELD to decide only where the verdict is recorded?

**Options:**

a) (recommended, confidence medium - the criteria sorted 76 real records cleanly and rest on rules already in the standards, but they have run on one territory and one review asked for scrutiny before standardising; reviewed, views differ: a masked Codex review prefers b), piloting on a second territory first, since one territory cannot show whether near-misses really need only one owner answer or whether reviewers classify alike) Adopt them into `ki-delegation` beside the unattended deny list as the assessment every window plan uses, with a harness run writing them and the field question staying with UNATTENDED-FIELD.

b) Pilot them on one more territory's roadmap in a design note first, then adopt with the lessons.

c) Keep them as Personal's local prototype and let each territory judge eligibility in its window plan.

#### UNATTENDED-FIELD - recording unattended eligibility on records

**Context:** Personal's prototype assessed 76 records against eight ordered criteria, 9 eligible, 21 near-miss and 46 attended, and proposed a record field. The brief proposes an optional `unattended` mapping in `ki-work-roadmap` with `verdict` (`eligible`, `near-miss`, `attended`), `criterion`, `question` and `assessed`, an absent mapping read as attended, and the criteria owned by `ki-delegation`.

**Query:** Should records carry this optional `unattended` mapping, with the eight criteria in `ki-delegation`?

**Options:**

a) (recommended, confidence medium - reviews disagree; a masked blind review on Codex would keep the assessment in a per-window note with no record field, as eligibility depends on the grant and can go stale, and review the eight criteria before standardising them, while Personal's assessment shows the criteria sort real records, and a field spares rereading every record at each window) Adopt the mapping and the criteria, refreshed at each status or horizon change.

b) Keep the assessment in a per-window note, with no record field.

### Theme: the website

#### The idea in brief

**The problem.** The new Skills section had to show 64 skills in a way a reader can navigate. Two provisional choices were made overnight on 25 October, taken live because they were reversible, and each drew a disagreement from the independent reviewer, so each comes to you.

**Two ways skills are grouped.** Every skill has a **source concern**, one of eight folders in the harness it lives in (governance, change management, repository structure and so on). Separately, the harness's diagram generator sorts skills into ten **functional areas**, reader-facing groupings such as "work and coordination" or "knowledge bases". The concerns are published metadata; the areas exist only inside the generator's code, which calls them a reading aid for the diagram, not published metadata.

**AREA-COLUMN.** The catalogue page groups skills by concern and adds a finder table with a functional-area column. To get the areas, the website's sync script parses the generator's code directly. That works today but is brittle: a harness refactor that moves the code breaks the website's sync without any skill changing. The alternative is for the harness to publish the area table in its generated `skills/README.md` block, a stable boundary the website can read, at the cost of coordinating a harness change, a sync change and a page change and a new pin. Worked example: if next week the harness renames the generator file, under option b) the website build fails until someone fixes the parser; under option a) the harness has published the table, the sync reads it from the README, and nothing breaks.

**REPO-STANDARDS-SET.** The feature-area map gives each area a page with a "Provided by" box naming the skills behind it. The Repository standards box lists the twelve general repository skills (website, MCP, harness and the like). The four knowledge-base skills (`ki-repo-kb` and its overlays for streams, activities, principal governance and live artefacts) appear under Knowledge bases but not under Repository standards. The worker kept them out so one skill does not appear in three boxes; the reviewer would include them because a knowledge base is a governed kind of repository. Worked example: a reader on the Repository standards page who looks after a knowledge base would, under option a), see all sixteen with a note that four apply only to knowledge bases; under option b) they would need to know to go to Knowledge bases.

#### AREA-COLUMN - how the skill catalogue shows functional areas

**Context:** The website's skill catalogue (`/docs/skills/catalogue/`) now groups the 64 skills by their 8 source concerns and adds a finder table (skill, source concern, functional area), rendered as inline HTML because the site's Markdown gate does not accept a generated row loop as a table. The 10 functional areas exist only inside the harness's generator code, which calls them a diagram reading aid rather than published metadata; the website's sync parses that code directly, so a harness refactor could break the sync without any change in membership. The inline finder is live now, taken provisionally. A masked blind review on Codex disagreed with the worker: the worker recommended keeping the inline finder (medium confidence) as it needs no upstream change; the reviewer recommended the harness publish the area table in its generated `skills/README.md` block (high confidence) as a stable boundary, at the cost of a coordinated harness, sync and page change and a new pin.

**Query:** Should the area finder stay as the website's own inline table, or should the harness publish the area table for the website to consume?

**Options:**

a) (recommended, confidence medium - reviewed, views differ: a stable published boundary outlasts parsing generator code, and the live finder serves until it lands) Keep the live finder now and send the harness a message to publish the area table in its README block, then switch the sync to it at the next pin.

b) Keep the inline finder as the lasting form and accept the coupling to the generator's code.

#### REPO-STANDARDS-SET - which skills the Repository standards area lists

**Context:** The website's new feature-area map gives each reader-facing area a docs page and a "Provided by" box naming the harness skills behind it. Repository standards lists the twelve general `ki-repo-*` skills (website, MCP, harness and similar). The four knowledge-base skills, `ki-repo-kb` and its overlays for streams, activities, principal governance and live artifacts, are listed under Knowledge bases and, for some, Recurring work, but not under Repository standards. That is live now, taken provisionally. A masked blind review on Codex disagreed with the worker: the worker preferred leaving them out (medium confidence), so that one skill does not appear in three boxes; the reviewer preferred including them (high confidence), because a knowledge base is a governed kind of repository and the shared membership links the two concerns, at the cost of a longer box that might suggest every repository needs knowledge-base conventions.

**Query:** Should the knowledge-base skills also appear under Repository standards?

**Options:**

a) (recommended, confidence medium - reviewed, views differ: the reviewer's point that a knowledge base is a governed repository kind is sound, and a short line can say these apply only to knowledge bases) Include all sixteen, with the knowledge-base skills marked as applying only to knowledge bases.

b) Keep the live twelve and leave the knowledge-base skills to their own areas.

### Theme: standards

#### The idea in brief

Three unrelated questions about written standards, each with its own short explanation.

**CLI-PREVIEW: how commands that change things offer a preview.** On 24 October you said `mgit repair` should just repair, with `--dry-run` to preview, and not need `--apply`, "the other command line tools that can do a repair don't need a --apply, so why does this one?". That was done. But the two harness standards for tools still say a repair must preview before it writes, so they contradict your decision, and the fleet is inconsistent: `mgit repair`, `ki repo repair` and `ki repo conform` act by default; `ki repair` and Almanac's repair still gate behind a preview. A survey of every command is in the dry-run survey report. The question is whether to make "write by default, `--dry-run` or `-n` to preview" the convention for all public commands that change state they own, reconcile both standards now, and change each tool later through its own work. Named exceptions keep their safeguards: anything that deletes data (Rig remove), a reviewed proposal file (Rig repair), firewall and service changes, and remote host removal. Worked example: today `ki repair` shows a plan and stops; under option a) `ki repair` would fix and `ki repair -n` would show the plan, and `--check` would stay a read-only verification that fails when it finds something.

**LEGACY-PREFIX: how a repository code rename passes the audits.** Every roadmap record's identifier starts with its repository's code, such as `KI-PRINCIPAL-MOD-009`. The audits fail any record whose prefix is not the current code. So a rename has to happen in one sweep: every record and every reference in one commit, or the repository fails its audit until the sweep finishes. Personal is renaming `KB` to `PERSONAL` that way now. The alternative is a legacy-prefix allowance: an optional list of former codes that existing records may keep while new records take the new code, which would need both checkers and the `tools-ki` readers to change. The case for the allowance is that identifiers are cited outside the repository and a sweep breaks those links; the case against is that renames are rare and a one-paragraph rule costs less than two checkers. Worked example: under option a) Personal's rename is one commit touching 76 records and every link, and `KB-DOTFILES-UE-108` ceases to exist as a name; under option b) old records keep `KB-` and new ones take `PERSONAL-`, both passing.

**PARTIAL-REPOS: a repository with only Pillars and Resources.** A knowledge base is expected to have five zones (Calendar, Pillars, Resources, Streams and the working areas). Humans Not Robots keeps `hnr-shared`, which has only Pillars and Resources, beside `hnr-principal`. The structure rule requires all five, and the registry binds one OneDrive source store per declared repository, so `hnr-shared` cannot be declared and its store is invisible to the store commands and audits; it is written up only in tracked notes. You asked Knowledge Islands to decide where partial repositories fit, and whether a person keeps a personal "work" knowledge base beside a person-agnostic company Capital, adding "there's a kind of weird thing here we maybe need to come back to." The question is whether to record it as an idea until you open it, or start a design brief now. Nothing is broken beyond HNR's workaround.

#### CLI-PREVIEW - How public commands that change state offer a preview

**Context:** You settled that `mgit repair` writes by default, and on 24 October left the wider convention open. Today the two harness standards for tools ([tool repositories](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-tools/references/standards-tool-repositories.md) and [CLI conventions](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-tools/references/standards-cli-conventions.md)) still require a preview step before a repair writes, contradicting that decision. `mgit repair`, `ki repo repair` and `ki repo conform` already act by default; `ki repair` and Almanac repair keep preview gates. Some writes must keep their safeguards: Rig remove (deletes data), Rig repair (a reviewed proposal file), firewall and service changes, and remote host removal. The command inventory is retained in [wow-dryrun-survey.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-dryrun-survey.report.md).

**Query:** Should public commands that change owned state write by default and offer `--dry-run`/`-n` as the preview, with both standards reconciled now and each tool changed later through its own work?

**Options:**

a) (recommended, confidence medium - reviewed; a masked blind review on Codex recommended it, keeping medium because your decision settled `mgit` only, not every shipped command) Write by default; `--dry-run` and `-n` show the same changes without applying them, and must prevent local and provider changes, not just the final write; `--check` is a read-only verification that fails on findings; `--apply`, `--write` and `--fix` are not routine write gates, and `--yes` only confirms. Keep named, documented exceptions for data deletion, publication, reviewed proposals and connection-critical changes. Reconcile both standards first, then change each tool through its owning work, with no fleet-wide flag migration.

b) Keep the current convention with `mgit repair` as the one exception, and hold the survey for a later decision.

#### LEGACY-PREFIX - how a `repo_code` rename passes the streams and roadmap audits

**Context:** the `ki-repo-kb-streams` streams audit and `ki-work-roadmap`'s checks fail every record not prefixed with the current `repo_code`. A rename therefore has to happen in one sweep, or the repository fails its audit until every record has moved. Personal is renaming KB to PERSONAL that way now. An allowance, an optional list of former codes that existing records may keep while new records take the new code, would allow a gradual path. It would need both checkers and the tools-ki readers to change.

**Query:** Should a `repo_code` rename stay a one-sweep change, written into `ki-work-roadmap`, rather than gaining a legacy-prefix allowance?

**Options:**

a) (recommended, confidence medium - reviews disagree; a masked blind review on Codex would add the former-code list, since issued identifiers are cited outside the repository and a sweep breaks those links, while renames are rare and Personal's runs as one sweep, so documenting the sweep costs one paragraph where the allowance costs two checkers and tools-ki) Write the rename into `ki-work-roadmap` as one sweep: every record and in-repository reference in one commit, pruned links keeping their pinned revisions.

b) Add an optional legacy-prefix list accepted by both audits for existing records only, with new records required to use the current code.

#### PARTIAL-REPOS - how a repository with only Pillars and Resources fits the model

**Context:** HNR keeps hnr-shared, which holds only Pillars and Resources, beside hnr-principal. ZONE-1 requires all five zones, and the registry binds one source store per declared repository, so hnr-shared cannot be declared. Its store is written up only in tracked notes, so `ki repo store` and the source audits do not see it. Kris asked Knowledge Islands to decide where partial repositories fit, and whether a person keeps a personal "work" knowledge base beside a person-agnostic company Capital, adding: "there's [a] kind [of] weird thing here we maybe need to come back to." The question reaches the Structure note, `ki-repo-kb` and tools-ki, beyond this work's method scope.

**Query:** Should PARTIAL-REPOS wait as an idea until Kris opens it, rather than starting a design now?

**Options:**

a) (recommended, confidence medium - reviews disagree; a masked blind review on Codex would start the design now, as your explicit question and the store-audit gap justify a bounded look, while your own words defer it, and nothing is broken beyond HNR's tracked-notes workaround) Record it as an idea on the Ways of working Project note with the HNR evidence linked, and start a `ki-work-design` brief when Kris opens it.

b) Start a `ki-work-design` brief now covering partial repositories, the personal "work" knowledge base and the store-binding gap.

### Housekeeping: two new queries from tonight's TIDY-GAPS answer

#### The idea in brief

On 25 October a tidy run found two files in this repository that no work claimed: a whole orphan folder `+/_WORK/ki.specifications/` holding 25 old run reports, and a citation in a harness record to a run report that no longer exists. You answered TIDY-GAPS tonight by asking for the owners to be traced before any repair. The run traced both. RADAR-REPORT-HOME is ready for you at high confidence, since nothing is deleted. SPEC-ORPHAN-OWNER recommends a deletion, so it is with a masked blind reviewer now; its confidence may change when the review returns, but its wording below is as it stands.

#### SPEC-ORPHAN-OWNER - the orphan `+/_WORK/ki.specifications/` folder belongs to ki.portable-specifications

**Context:** `+/_WORK/ki.specifications/` was opened on 19 October 2026 as the Project work package for KI Specifications (`cd388627`). That day the Project was renamed under its PROJECT-NAME decision: the rename run's own report (`rename.report.md`, in the orphan folder) records that the whole package became [`+/_WORK/ki.portable-specifications/`](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/work.md), Project [Portable specifications](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/portable-specifications.md) under theme Model; Git confirms every tracked file moved as a pure rename in `a90aea3b`, and the renamed package has been on hold since 20 October (`release: Kris says resume`). The 25 `*.report.md` files left in the old path were run reports that nobody had ever tracked, so the rename did not carry them; all 25 are byte-identical copies of the run reports still held in `/Users/krisbrown/.local/state/ki/agents/specifications/`, and they were swept into Git by the `chore: baseline` commit `e78fff63` on 24 October. The renamed package holds no reports and had already pruned its only tracked one (`create-project.report.md`, `5b8ac0f3`) as homed. The orphan folder therefore has no identity of its own and carries nothing that its run packets do not.

**Query:** Do you accept ki.portable-specifications as the owner, with the repair being a bounded run that removes `+/_WORK/ki.specifications/` by explicit path once that package confirms its reports are homed?

**Options:**

a) (recommended, confidence high - every file is a verified byte-identical copy of a run report still in the specifications run directory, and the rename report names the new package) Owner ki.portable-specifications. Send one line to its `messages.md` naming the 25 reports; when it resumes, it checks each against its decisions log and deletes the folder by explicit path in a `docs(work)` commit; nothing is deleted before that check.

b) Owner ki.portable-specifications, but delete the folder now in a bounded run, relying on the run packets as the surviving copy, without the package's own homing check.

c) Keep the folder as it is until the Project resumes, with no message sent.

#### RADAR-REPORT-HOME - `radar-confirm-2.report.md` came from ki.chezmoi and its evidence already lives in UE-108

**Context:** [KI-HARNESS-REV-012](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-REV-012-thoughtworks-radar-input.md) cites `/Users/krisbrown/.local/state/ki/agents/chezmoi/radar-confirm-2.report.md` as a "verified source check". That path is a run packet of the [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) work (Project [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md), theme Rig). Its decisions log shows the chain on 24 October 2026: radar-confirm launched at 12:28 BST (`b5c6c299`), relaunched as radar-confirm-2 at 12:31 BST with a read-only fetch grant for the public ThoughtWorks pages under Kris's 12:25 instruction (`230aadc8`), its finding that the fourth ring is Caution recorded at 12:35 BST (`1d9613dd`), and radar-confirm-3 then homing that finding at 12:41 BST in two places: the chezmoi record [PERSONAL-DOTFILES-UE-108](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/PERSONAL-DOTFILES-UE-108-decide-tool-radar.md), whose "Confirmed scope and ring vocabulary" section carries the source URLs, the check date and the verbatim FAQ ring excerpts, and the harness record REV-012 (`7a759440`, `c4285065` in the log). The report file itself was never copied into the ki.chezmoi package, never tracked in any repository, and no longer exists in the chezmoi run directory or the archive; both records cite a dead local path. UE-108 holds everything the citation stood for.

**Query:** Do you accept ki.chezmoi as the owner, with the durable home being UE-108's ring-vocabulary section rather than a recreated report, and the repair a repointing of both citations?

**Options:**

a) (recommended, confidence high - the report's content is carried verbatim in UE-108 and the file is gone, so no provenance is invented) Owner ki.chezmoi. A bounded run repoints REV-012's citation to the public ThoughtWorks Radar and FAQ pages plus UE-108's section, and replaces UE-108's self-citation of the dead path with the same public pages and the 24 October check date; two small `docs(roadmap)` commits, one per repository, with REV-012 kept at triage.

b) Owner ki.chezmoi, and ask it to recreate the source check as a tracked note under the harness `ki-model-radar` sources reference, then cite that from both records.

c) Leave both citations as they are, treating the dead path as historical.

### Parked

- **PERM-PROMPTS-SETTINGS** - whether to change the chezmoi-managed permission settings so agents meet fewer permission prompts. You said on 25 October "can we come back to it later?". Recommended when you do: not now; revisit if you leave bypass mode.

## 6. Glossary

Terms in the order a reader is likely to meet them.

- **Knowledge Islands (KI).** The family of repositories, tools and conventions you work in. **Knowledge Islands Principal** (`ki-principal`) is its Capital, the repository that holds governance and this work package.
- **Island.** One repository treated as a structured knowledge base: folders of Markdown notes in five zones (Calendar, Pillars, Resources, Streams, and the `+` and `-` working areas).
- **Territory.** One group of repositories under a shared State of play, such as Knowledge Islands, Humans Not Robots (HNR), Valle Armonia (VA), Legal or Personal. Its **Capital** is its principal repository.
- **State of play.** The one coordinating thread for a whole territory; it watches every Project package and routes messages.
- **Project.** A named, longer-lived piece of work with its own package and a Project note under `Streams/Projects/`; it belongs to a **theme** (Ways of working is under the theme Model).
- **Work.** One piece of coordinated effort, at territory or Project level, identified like `ki.ways-of-working`.
- **Work package.** The folder `+/_WORK/<id>/` of five files: `work.md` (definition), `state.md` (state), `queries.md` (questions for you), `messages.md` (incoming queue) and `decisions.md` (your decisions, read back). Git is its logbook.
- **Work Process note.** The model of work in Principal: seven states, two moves (send and receive), worker and supervisor.
- **Coordinator / coordinating thread.** The session that dispatches runs, decides with you and reports; it never does substantive work itself.
- **Thread.** A session acting on a work. Three kinds: conversational, coordination and State of play.
- **Run.** A detached background agent launched with `ki agent` to do one bounded unit, from a **brief** (its instructions, in `briefs/`), ending in a **run report**. Runs are named like `wow-rel-0141`.
- **Owner report.** The report shape every session uses to you: Done, In Progress, Queries, closing with a glyph banner showing whose move it is.
- **Query.** A question for you with Context, Query and lettered Options, the recommendation first with a confidence. A **tag** such as STEWARD-FIELD is its stable name.
- **Blind review / masked review.** An independent reviewer, usually on Codex (OpenAI's agent, "Astra" in your words), reads a query with the options unranked and no sight of the recommendation. Agreement lifts confidence; disagreement shows both views.
- **Confidence.** High: coordinator and reviewer agree. Medium: they disagree, or the evidence is thin. Low: a weak course.
- **Mark.** A timestamp struck in the work's state so the next report can walk through everything since.
- **Unattended window / away grant.** A period you authorise for the coordinator to keep working without you, with a stated end, permitted actions and exclusions. The **deny list** is what a window never does.
- **Eligible / near-miss / attended.** The three verdicts of the eight-criteria unattended assessment.
- **Steward.** The work that looks after a package over time, set by committed assignment and handover. Distinct from the **holder**, whose move it is right now.
- **Roadmap record.** One work item in a repository's `Streams/Roadmap/` or `docs/roadmap/`, identified by repository code and serial, such as `KI-PRINCIPAL-MOD-009`. Moves through triage, Now or Next, Ready, awaiting review, done; **accept** closes it; **prune** removes a closed record.
- **Enactment Process.** Principal's gate for changing canonical content: a record in the roadmap, planned and reviewed before the change lands.
- **Message / handoff.** A line in another work's `messages.md`. Handoffs and rollouts travel as messages, never as roadmap records in another repository.
- **Harness (`ki-agentic-harness`).** The repository that holds the skills, standards, output styles and hooks the agents run under.
- **Skill.** One written unit of method the agents follow, such as `ki-coordination` (coordinating work), `ki-delegation` (background runs), `ki-work-package` (the five files), `ki-work-roadmap` (records), `ki-bootstrap` (first-time set-up) or `ki-trades` (moving work between repositories).
- **`ki` / `tools-ki`.** The command-line tool that installs the harness, runs audits, manages repositories and launches runs. Released as versions such as v0.13.0.
- **Release chain / fan-out.** `tools-ki` publishes a release; a bot updates the **Homebrew tap** (`homebrew-tap`, the formula `brew install ki` reads); the tap dispatches to **consumers** (the website and the harness), which bump their pins.
- **Pin.** The `ki` version a repository's CI installs, held in `KI_VERSION` or `.github/ki-version`.
- **CI.** Continuous integration, the automated checks GitHub runs on each push. **Main** is the default branch. **Green** passes, **red** fails.
- **DESIGN-2, DEPS-1, TEST-5.** Named audit findings: the checker-folder name mismatch cleared by v0.14.1; library drift (Bun and two packages), fixed; a stale dependency-checker version, fixed.
- **`tooling/depcruise`.** The folder holding each repository's dependency-boundary checker, renamed from `tooling/boundaries`.
- **Fast-forward only.** A pull or push that adds commits in a straight line, never rewriting history. Never force-pushed, never with `--no-verify`.
- **Checkout.** One local copy of a repository. A **worktree** is an extra checkout of the same repository for isolated work.
- **mgit / `tools-mgit`.** Your multi-repository Git tool. A **sweep** runs one command across the **selection** of checkouts chosen by a **selector**. A **template**, recorded by `mgit learn`, is the normal output mgit hides; a checkout is then **quiet**, **with output** or **failed**.
- **Route.** In the mgit cache design, one of six lettered alternatives (A to F) for narrowing a follow-up command, not a step in a plan.
- **Cache set.** The list of non-quiet checkout paths `--to-cache` writes and `--from-cache` reads, with a **selection key** that stops a different workspace reusing it, and a five-minute life (the **TTL**, time to live).
- **`--repos-from`.** The proposed selector that takes checkout paths from a file or standard input.
- **Archify.** The diagram tool that draws the website's explorable diagrams from a description.
- **Tending.** The interim practice of periodic repository care: audits, drift checks and small repairs.
- **Findings.** A report section and package folder for open investigation results carried until you are content.
- **Interim.** Practices (tending, findings, repository metadata) adopted provisionally while their lasting home is decided.
- **Chezmoi.** Your dotfiles manager; the `ki.chezmoi` work owns changes to it. **Rig** is the workstation tool and theme that covers it.
- **Codex / Claude / Fable / Astra.** The agent runtimes: Codex is OpenAI's; Claude is Anthropic's, Fable its current strongest model; "Astra" is your name for Codex's strongest model.
- **MOD-009.** `KI-PRINCIPAL-MOD-009`, a Principal record amending an architecture decision's staging wording, accepted tonight.
- **GDR.** A Governance Decision Record in Principal's `Admin/Governance/Decisions/`, such as `GDR-KI-PRINCIPAL-009`.
