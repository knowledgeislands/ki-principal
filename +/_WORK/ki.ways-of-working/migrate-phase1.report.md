# [Knowledge Islands model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/knowledge-islands-model/knowledge-islands-model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working/ways-of-working.md) › migrate-phase1

**Run report at 03:24 BST · last mark 22:34 BST**

---

## Done

- The migration brief, `+/_THREADS/ways-of-working/work-migration.brief.md`, is amended and pushed in Knowledge Islands Principal (1a77312).
- Phase 1 is written into ki-agentic-harness and pushed, ten commits from 896828ee to ebc05eb2, under [KI-HARNESS-GOV-210](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-210-work-model-write-in.md), now at awaiting-review and not accepted:
  - `ki-pmo`: the work model, with the hook line, output style, hooks README, HARN-012 and HARN-013 regenerated or rewritten;
  - `ki-delegation`: briefs, decisions log and reports in `+/_WORK/<id>/`, plus one run-prompt line that still named `+/_THREADS/<run>/`, found and fixed late (9ced0cc7);
  - `ki-checkpoint`: the work-file standard; old checkpoints still read with a `legacy:` warning; `ki-repo-kb` exempts work files from note typing so phase-3 work files will not fail NOTE-1;
  - the Project registry, Streams and roadmap standards and checkers: themes, flat Project notes, no `design/` under `Streams/`;
  - `ki-repo-kb-activities` and `ki-work-recurring`: an Activity's home is regular work or its Project, with `theme` optional and `initiative` warning;
  - `ki-pmo-design`: design notes in `+/_WORK/<id>/design/`.
- The records are amended: [KI-HARNESS-GOV-206](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-206-activity-homes-and-coordination.md), now blocked by KI-HARNESS-GOV-210; [KI-HARNESS-GOV-200](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-200-thread-folder-closed-list.md), now about the work folder's closed list; [KI-HARNESS-GOV-199](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-199-thread-identity-role-native-sessions.md), where `level` replaces `role` and work naming replaces thread naming; [KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md), which now uses on-hold and tracked briefs, with the DONE form left to planning.
- No skill is renamed and `ki agent` is unchanged.
- Verification: `bun run test` and `bunx tsc --noEmit` pass; `ki dev skill generate ki-pmo` reports every surface current; the `ki-work-roadmap`, `ki-checkpoint`, `ki-delegation`, `ki-skills` and `ki-work-recurring` audits pass.
- The `ki-pmo` audit reports FAIL=4 and WARN=2. These are the baseline's findings, from PMO-7 and an unlinked KI-HARNESS-GOV-193 in `+/_THREADS/skill-reviews`, and none is in the contract under change. `ki-pmo-design` has no declared audit, so the staged `ki-skills` audit covered it.
- Fleet findings against Knowledge Islands Principal. None is caused by this change; all wait for phase 3:
  - `ki-checkpoint`: FAIL=8 and WARN=11. These are old-form checkpoints that already failed at HEAD: RECORD-2 in `_state-of-play.md`, `platform-foundations.tools-burndown.md` and `rig.mac-studio-setup.md`, and LIFECYCLE-1 in `platform-foundations.tools-burndown.md`.
  - `ki-repo-kb-streams`: five `design/` folders under `Streams/` fail, as expected until phase 3: the ways-of-working, paperclip-capture-and-rebuild, agent-host and mac-studio-setup Projects, and the knowledge-islands-model Initiative. The STREAM-10 warnings were already there.
  - `ki-repo-kb-activities`: three legacy `initiative` warnings, in the Briefings Activity, the Schedule and the Tending Activity.
- Pushing: no other session's commits sat beneath mine in either repository. One file is dirty from another session and was left untouched: `+/_THREADS/chezmoi/decisions.md` in Knowledge Islands Principal.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Phase 2 in tools-ki, under [KI-TOOL-KI-CLI-127](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-127-agent-status-live-threads.md), can start once KI-HARNESS-GOV-210 has been reviewed. It covers `ki work status`, the readers and a release.
- The phase-3 legacy findings listed under Done clear when the Capital moves into `+/_WORK/` and `Streams/Themes/`.

## Queries

### GOV-210-REVIEW - independent review of the phase-1 write-in

**Context:** [KI-HARNESS-GOV-210](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-210-work-model-write-in.md) is at awaiting-review. Its Review section lists what was delivered and how it was verified. Phase 2 builds on this record.

**Query:** Should an independent review run check KI-HARNESS-GOV-210 against its baseline before it is accepted?

**Options:**

a) (recommended, confidence high - acceptance needs a review by someone other than the author) Launch one review run on `be65ccad..ebc05eb2` against the record's Verify, and accept the record when it passes. b) Accept it on this report.

### GOV-206-CLOSE - whether KI-HARNESS-GOV-206 closes with the write-in

**Context:** Phase 1 wrote in every item of [KI-HARNESS-GOV-206](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-206-activity-homes-and-coordination.md): Activity homes, an optional theme, and self-coordinating regular work. Its Discussion leaves the outcome to planning.

**Query:** Should KI-HARNESS-GOV-206 close as delivered by KI-HARNESS-GOV-210?

**Options:**

a) (recommended, confidence medium - the boundary is covered, but its review evidence lives in another record) Close KI-HARNESS-GOV-206 as delivered by KI-HARNESS-GOV-210 once that record is accepted. b) Keep it open for a separate delivery and review.

### REPO-OWNERSHIP - ki-repo still names the thread-model paths

**Context:** `ki-repo` sat outside the phase-1 boundary. It still names `+/_CHECKPOINTS/` and `+/_THREADS/<run>/` as owned paths in `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-repo/references/standards-repository.md` (lines 128-130) and `standards-configuration.md` (line 241), and in its COVERAGE detect, `scripts/rubric/contexts/audit.ts` (lines 724-729). Once the Capital moves, `+/_WORK/` would go uncovered.

**Query:** How should `ki-repo` take up `+/_WORK/` and `+/_WORK_REVIEW/`?

**Options:**

a) (recommended, confidence high - the change is small and must land before phase 3) Capture one ki-agentic-harness record that adds `+/_WORK/` and `+/_WORK_REVIEW/` to `ki-repo`'s ownership and COVERAGE, accepts the old paths with a warning, and lands before phase 3. b) Fold it into the review run for KI-HARNESS-GOV-210.

### REPORT-SHAPE - this report follows the brief, not the live style

**Context:** The brief asked for the thread-model run-report shape, with a reply block and a block-letter footer. Partway through the run, the live output style changed under REPLY-BLOCK to the work-model shape, which has a glyph handoff line and no reply block. This report follows the brief.

**Query:** Which report shape should later phase briefs ask for?

**Options:**

a) (recommended, confidence high - the live standard now sets it) Phase 2 and later briefs ask for the work-model run report from the current `ki-delegation` and `ki-pmo`. b) Keep the thread-model shape until phase 5.

```text
GOV-210-REVIEW

Launch one review run on ki-agentic-harness be65ccad..ebc05eb2 against KI-HARNESS-GOV-210's Verify, and accept KI-HARNESS-GOV-210 when it passes.

---

GOV-206-CLOSE

Close KI-HARNESS-GOV-206 as delivered by KI-HARNESS-GOV-210 once KI-HARNESS-GOV-210 is accepted.

---

REPO-OWNERSHIP

Capture one ki-agentic-harness record adding +/_WORK/ and +/_WORK_REVIEW/ to ki-repo's ownership and COVERAGE detect, accepting +/_CHECKPOINTS/ and +/_THREADS/ with a warning, to land before phase 3.

---

REPORT-SHAPE

Phase 2 and later briefs ask for the work-model run report from the current ki-delegation and ki-pmo.
```

```text
╭─ run report · 2026-10-18T02:24:20Z ──────────────╮
│                                                  │
│  █▀▀▄ █▀▀▀ █▀▀▀ ▀▀█▀   · thread at rest          │
│  █▀▀▄ █▀▀  ▀▀▀█   █    · nothing running         │
│  █  █ █▄▄▄ ▄▄▄█   █    · nothing queued          │
│                                                  │
╰──────────────────────────────────────────────────╯
```

- [at rest] nothing running or queued
- [waiting] GOV-210-REVIEW
- [waiting] GOV-206-CLOSE
- [waiting] REPO-OWNERSHIP
- [waiting] REPORT-SHAPE
- [committed] ki-agentic-harness and this report, pushed
