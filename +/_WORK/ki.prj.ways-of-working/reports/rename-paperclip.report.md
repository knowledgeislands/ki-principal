# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › rename-paperclip

**🤖 → 👤 Handoff to supervisor · Run report at 01:13 GMT · last mark 00:56 GMT**

---

## Done

- The Paperclip skill is now called `ki-delegation-paperclip` in KI Agentic Harness (`8a9f7409`), under ORCH-NAME-DISPATCH a) of 1 November. Its description now covers everything it does: company and repository boundaries, Company Operational Review readiness, agent memory and knowledge return, and each repository's delivery and integration policy. It also names `ki-delegation` as the owner of the shared contract. Nothing was cut. The landscape report's row 7 had said "renamed and slimmed", but the brief said not to narrow the skill, so I followed the brief.
- An alias keeps the old name working. A thin `ki-agent-coordination-paperclip` skill (the same pattern as the earlier `ki-work-folder` alias) lets `.ki.toml` files that still use the old name resolve. Its one check warns and names `[skills.ki-delegation-paperclip]` as the replacement, keeping `organisation_code`. Repositories still on the old name don't get the Paperclip checks until they switch.
- Every reference in the harness was updated: the harness's own `.ki.toml`, `AGENTS.md`, the eval scenario (renamed), Wright's subagent link, the `ki-delegation`, `ki-bootstrap`, `ki-binding`, `ki-work-roadmap` and radar references, and the skill-area grouping and its test. The rubrics, catalogue, README counts and remediation-inventory test counts were regenerated. The skill map and the Agentic-systems and Fundamentals diagrams were re-rendered in a second commit (`3634a9be`). The standard's file name, `standards-agent-coordination-paperclip.md`, is unchanged, so links that point into the skill keep their anchors.
- Checks, run in an isolated worktree and audit home: `bun run test` passed (1510 tests). `bunx tsc --noEmit` passed. The focused audits for `ki-delegation-paperclip`, `ki-skills`, `ki-delegation` and `ki-repo-harness`, and the full `ki repo audit`, show no failures. The warnings left are older fleet warnings: diagram freshness, overdue source refreshes and radar dates.
- Both commits were fast-forwarded into harness `main`.
- No `ki-delegation-orca` exists anywhere under `~/kis`. Its only traces are in this Project's design notes and in the [Orca evaluation package](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.orca-evaluation/state.md), which is with its supervisor. What creating it would take is in Findings.
- 54 repositories outside the harness declare the old name; they are listed in Findings. The rollout went to State of play as one `PAPERCLIP-RENAME` line in [its messages](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/messages.md) (`3ae27509`).

## In Progress

Nothing is running.

Outstanding - no action requested now:

- My temporary worktree for the harness, on branch `rename-paperclip` (already merged), is still registered in the harness's Git. `ki agent close` will remove its folder; after that, `git worktree prune` and `git branch -d rename-paperclip` in the harness tidy it away.
- The harness's primary checkout still links its local skill copy under the old name. Running `ki repo repair --repo .` there links `ki-delegation-paperclip` by its new name. I didn't run it because the brief allows no environment changes.
- Remove the alias once no repository declares the old name, as was done for `ki-work-folder`.

## Findings

### REFS - References to the old name outside the harness

**Goal:** list every reference to `ki-agent-coordination-paperclip` under `/Users/krisbrown/kis/` outside KI Agentic Harness, so State of play can roll out the rename.

**Scope:** all text files under `/Users/krisbrown/kis/`, excluding `.git`, `node_modules`, the installed `.claude`/`.agents` skill copies, and two other sessions' harness worktrees (`ki-agentic-harness-finished-tidy`, `ki-agentic-harness-quiet-listen`), which pick up the rename when they merge with `main`.

**As of:** 1 November 2026, 01:05 GMT, after the push.

Every repository listed declares `[skills.ki-agent-coordination-paperclip]` with its `organisation_code` in `.ki.toml`; the other files are prose or work-package history.

- **equal-remedy**
  - `apps-dafacts.org`: `.ki.toml`
  - `er-agentic-harness`: `.ki.toml`
  - `er-principal`: `.ki.toml`, `Admin/Governance/Conformance.md`
- **humans-not-robots**
  - `5g-emerge-testbed`: `.ki.toml`
  - `apps-be.humansnotrobots.bbc`: `.ki.toml`
  - `apps-be.humansnotrobots.cs`: `.ki.toml`
  - `apps-be.humansnotrobots.eit`: `.ki.toml`
  - `apps-be.humansnotrobots.home`: `.ki.toml`
  - `apps-be.humansnotrobots.hr`: `.ki.toml`
  - `apps-be.humansnotrobots.pt`: `.ki.toml`
  - `apps-be.humansnotrobots.sky`: `.ki.toml`
  - `apps-be.humansnotrobots.sm`: `.ki.toml`
  - `apps-be.humansnotrobots.snowflake`: `.ki.toml`
  - `apps-io.5g-emerge`: `.ki.toml`
  - `apps-io.5g-emerge.demo`: `.ki.toml`
  - `apps-io.5g-emerge.p2ms3`: `.ki.toml`
  - `apps-io.5g-emerge.phase2`: `.ki.toml`
  - `apps-io.5g-emerge.phase3`: `.ki.toml`
  - `hnr-agentic-harness`: `.ki.toml`
  - `hnr-principal`: `+/_WORK/hnr.sop.sites/design/sites-ki-plan.md`, `+/_WORK/hnr.sop.sites/design/sites-standard.md`, `+/hnr-principal/repository-snapshot/.ki.toml`, `.ki.toml`
  - `infoschematics`: `.ki.toml`
- **knowledge-islands**
  - `apps-knowledgeislands.info`: `.ki.toml`, `apps/site/src/_data/skillCatalogue.json5`, `apps/site/src/docs/skills/by-outcome.md`, `apps/site/src/docs/skills/how-the-skills-fit-together.md`
  - `apps-observatory.local`: `.ki.toml`
  - `homebrew-tap`: `.ki.toml`
  - `ki-design`: `.ki.toml`
  - `ki-principal`: `+/_WORK/ki.prj.paperclip-capture-and-rebuild/design/paperclip-rebuild-structure.md`, `+/_WORK/ki.prj.ways-of-working/briefs/rename-paperclip.md`, `+/_WORK/ki.prj.ways-of-working/decisions.md`, `+/_WORK/ki.prj.ways-of-working/design/change-management-decisions.md`, `+/_WORK/ki.prj.ways-of-working/design/change-management-report.md`, `+/_WORK/ki.prj.ways-of-working/design/inbox-wake/design.md`, `+/_WORK/ki.prj.ways-of-working/design/landscape-review-codex.md`, `+/_WORK/ki.prj.ways-of-working/design/landscape-skills-inventory.md`, `+/_WORK/ki.prj.ways-of-working/design/landscape.md`, `+/_WORK/ki.prj.ways-of-working/design/repository-metadata.md`, `+/_WORK/ki.sop.main/reports/skills-assessment.report.md`, `.ki.toml`, `Pillars/Engineering Practice/Operating Model/Paperclip Operating Lessons.md`, `Pillars/Philosophy/Introduction/Background/Influences Along the Way/Influences Along the Way.md`, `Streams/Projects/paperclip-capture-and-rebuild.md`
  - `ki-specifications`: `.ki.toml`
  - `ki-techne-harness`: `.ki.toml`
  - `mcp-acquire-whatsapp`: `.ki.toml`
  - `mcp-git-audit`: `.ki.toml`
  - `mcp-gsuite`: `.ki.toml`
  - `mcp-housekeeping-chatgpt`: `.ki.toml`
  - `mcp-housekeeping-claude`: `.ki.toml`
  - `mcp-ki-kb-fs`: `.ki.toml`
  - `mcp-m365`: `.ki.toml`
  - `tools-git-almanac`: `.ki.toml`
  - `tools-ki`: `.ki.toml`
  - `tools-mgit`: `.ki.toml`
  - `tools-rig`: `.ki.toml`
  - `tools-techne`: `.ki.toml`
- **legal**
  - `legal-agentic-harness`: `.ki.toml`
  - `legal-principal`: `.ki.toml`, `Admin/Governance/Conformance.md`
- **personal**
  - `apps-ninja.midnight`: `.ki.toml`
  - `apps-ninja.midnight.legal`: `.ki.toml`
  - `apps-ninja.midnight.rig`: `.ki.toml`
  - `apps-ninja.midnight.tower`: `.ki.toml`
  - `apps-ninja.midnight.trip`: `.ki.toml`
  - `apps-uk.me.kris`: `.ki.toml`
  - `personal-agentic-harness`: `.ki.toml`
  - `personal-principal`: `.ki.toml`, `Admin/Governance/Conformance.md`
- **sacred-inquiry**
  - `si-agentic-harness`: `.ki.toml`
  - `si-principal`: `.ki.toml`, `Admin/Governance/Conformance.md`
- **techmedix**
  - `tmx-agentic-harness`: `.ki.toml`
  - `tmx-principal`: `.ki.toml`, `Admin/Governance/Conformance.md`

### ORCA - What creating `ki-delegation-orca` would take

**Goal:** say what creating the Orca adapter would involve, without creating it.

**Scope:** KI Agentic Harness, this Project's landscape report (homing rows 6, 8, 17), and the Orca evaluation package.

**As of:** 1 November 2026, 01:05 GMT.

| Part | What it takes |
| --- | --- |
| Skill shell | A new `skills/agentic-systems/ki-delegation-orca/` with `SKILL.md`, a standard, sources, a rubric with its generated publication, tests, a catalogue and diagram refresh, and an eval scenario. It would be about the size of this rename's alias plus a short standard. |
| Content | How Orca carries out `ki-delegation`'s contract verbs (start, queue, status, recover), including the Orca-first queue route (ORCA-QUEUE a), launching through `orca orchestration worker-start`, removing the `ORCA_*` variables the runs inherit (ORCA-ENV-LEAK), whether report paths are reachable on remote workers, the narrowed trigger scope, and cleaning up workers. |
| Dependencies | The slimmed `ki-delegation` contract (landscape row 4) should land first, so the adapter has a stable contract to follow. ORCA-REACH has a follow-up due 6 November 2026. Loading Orca skills only where a package has chosen Orca (row 8) belongs to `ki.prj.chezmoi`. |
| Evidence gap | No remote Orca run has been tested; the server mode is documented as beta and LAN-only, and that hasn't been checked locally. |

## Queries

### ORCA-ADAPTER-WHEN - When to create the Orca adapter

**Context:** Kris chose the delegation family on 1 November: `ki-delegation` as the shared contract, with an Orca adapter and a Paperclip adapter. The Paperclip adapter now exists under its new name. The Orca adapter doesn't exist yet. Writing it means describing how Orca carries out the shared contract (launch, queue, status, recovery, cleanup). That contract is still being slimmed, and the [Orca evaluation](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.orca-evaluation/state.md) hasn't yet tested a remote run.

**Query:** Should `ki-delegation-orca` be written now, or after the slimmed `ki-delegation` contract and the Orca evaluation's trial have landed?

**Options:**

a) (recommended, confidence medium - the adapter would otherwise describe a contract that is still changing and Orca behaviour nobody has tested) Wait: commission it as one harness run once the slimmed `ki-delegation` contract has landed and the Orca evaluation has reported, and write it from that evidence.

b) Write a minimal skeleton now: a skill that names its boundary, points to `ki-delegation` and records the open questions, then fill it in after the trial.
