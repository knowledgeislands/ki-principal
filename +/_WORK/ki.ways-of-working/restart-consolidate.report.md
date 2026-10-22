# [Knowledge Islands model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/knowledge-islands-model/knowledge-islands-model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working/ways-of-working.md) › restart-consolidate

**Run report at 14:56 BST · last mark 14:45 BST**

---

## Done

- Wrote the [restart design report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/restart.report.md): one restart decision (RESTART-AGREE) folding STATE-AGREE, THREAD-MESSAGING, INTERIM-MESSAGING, RESTART-PROMPTS, THREAD-DURABILITY, THREADS-CHECKINS, CHURN-REMEDIES 1, 2 and 4, and ROUTING, with exact before-and-after wording for ki-pmo, ki-delegation and ki-checkpoint; three text diagrams (state model, messaging flow, restart sequence); the critical path; triage of the older Messages lines; and eight regrouped queries.
- Critical path: only RESTART-AGREE blocks the other threads. After it, one ki-agentic-harness run writes the standard, then this thread writes READY into the [state-of-play checkpoint](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_CHECKPOINTS/_state-of-play.md)'s block.
- Triage: ROUTING and SYNC-GUARD folded; KI-AGENTS-NAME done; GIT-SURFACE to an `Idea:` bullet; DIAGRAMS, DIAGRAMS-RENDER and AWAITING-REVIEW became queries; AREAS-DISPATCH kept.
- DIAGRAMS-RENDER's cause is Archify's CSS-painted dual-theme SVG export, not Mermaid; this run therefore used box-drawing text diagrams, which read in light and dark previews.
- Committed the restart report alone by explicit path and pushed it fast-forward to ki-principal `main`; no other session's commit was carried. The pull with rebase was blocked by another session's dirty `+/_THREADS/chezmoi/decisions.md`, so I fetched, confirmed origin had not moved, and pushed. That file and the untracked `+/_THREADS/desk-kit/setup-note.report.md` were left untouched.
- The commit gate passed for the staged path. Outside that scope it flags malformed frontmatter in `+/_THREADS/desk-kit/cam-check.report.md` and `webcam-compare.report.md`, both belonging to the desk-kit session.
- Changed no standard, skill, hook, record, checkpoint or Messages block. tools-ki and chezmoi were not touched. This owner report is left uncommitted, because the brief allowed only the restart report to be committed.

## In Progress

Nothing is running.

### Outstanding - no action requested now

- The 17 October Messages lines stay in the [ways-of-working checkpoint](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_CHECKPOINTS/knowledge-islands-model.ways-of-working.md) until the thread acts on RESTART-AGREE's answer; KI-AGENTS-NAME can be removed now.
- tools-ki holds five of this thread's commits unpushed, and chezmoi holds three unpushed and unapplied (TOOLS-PUSH, CHEZMOI-APPLY).

## Queries

### RESTART-AGREE - one standard for state, messaging and restart

**Context:** §1 proposes one standard edit across ki-pmo, ki-delegation and ki-checkpoint. It covers where each kind of file lives, how threads message each other and what a restart prompt is. It replaces STATE-AGREE, STATE-RECORDS, DECISIONS-HOME (deferred into SHAPE-AGREE), THREAD-DURABILITY, THREADS-CHECKINS, CHURN-REMEDIES, THREAD-MESSAGING, INTERIM-MESSAGING, RESTART-PROMPTS and ROUTING. Nothing else blocks the other threads' restart.

**Query:** Do you agree §1 as the standard, so one harness run can write it and the restart can begin?

**Options:**

a) (recommended) Agree §1 as written: one ki-agentic-harness run writes §1.4, regenerates the surfaces and pushes; this thread then writes READY.

b) Write the messaging and restart-prompt parts (§1.2, §1.3) now and leave the state model (§1.1) until after the restart.

c) As a), but keep every run report committed in the thread folder (drop remedy 1).

### RUN-HYGIENE - checkpoint fixes and the push rule

**Context:** Absorbs IDENTITY-NEXT's `role` ask, CHECKPOINT-FINDINGS, PUSH-RULE and REPORT-FILE-FORM, as the [summary draft](/Users/krisbrown/.local/state/ki/agents/ways-of-working/summary-draft.md) sets out. The checkpoint fixes travel as FIRST-STEP lines with the restart. PUSH-RULE settles the clash between the generic brief footer, which forbids any push, and briefs that allow one.

**Query:** May the checkpoint fixes go out as FIRST-STEP lines and the brief footer defer to a brief's own push rule?

**Options:**

a) (recommended) Yes: each thread fixes its checkpoint form and adds `role` on its FIRST-STEP line, and the generic footer gives way to an explicit push rule in the brief.

b) Fix the checkpoints only; keep the footer's no-push rule absolute and push from the thread.

### TOOLS-PUSH - this thread's five tools-ki commits

**Context:** tools-ki holds this thread's commits `33770a8d`, `80246ca6`, `30513f9c`, `4ef7b9c0` and `90807355` unpushed, above 26 commits from other sessions, on a detached HEAD another session holds. `90807355` carries KI-TOOL-KI-CLI-145 (IDENTITY-NEXT Phase 2). Absorbs the tools-ki state tooling, which joins KI-TOOL-KI-CLI-137.

**Query:** Should tools burndown take these commits as its first step?

**Options:**

a) (recommended) Hand them to tools burndown: it reconciles the stack, cuts v0.10.6 and bumps ki-principal's `.github/ki-version`.

b) Leave them unpushed until you review the 26 other commits yourself.

### HARNESS-ACCEPT - four harness records awaiting your review

**Context:** New; replaces IDENTITY-NEXT's acceptance half and this thread's share of AWAITING-REVIEW. [KI-HARNESS-GOV-195](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-195-granola-screenshots-markers.md), [KI-HARNESS-GOV-198](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-198-reply-forms.md), [KI-HARNESS-GOV-203](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-203-git-clean-down-criteria.md) and [KI-HARNESS-OPS-005](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-OPS-005-acquire-ai-sessions.md) are delivered and wait on acceptance. KI-HARNESS-GOV-203 has a 30-day stale threshold you never set. The IDENTITY-NEXT Phase 1 text lands with Phase 3.

**Query:** May this thread present all four in one ki-accept sitting after the restart?

**Options:**

a) (recommended) Yes: one ki-accept sitting after the restart, with the 30-day threshold put to you there.

b) Accept them one at a time as each thread reaches them.

### CHEZMOI-APPLY - three chezmoi commits unapplied

**Context:** chezmoi holds commits `673b999`, `d81a80c` and `d1a6e6d` unpushed and unapplied; they change `~/.claude/communication.md`, `~/.claude/delegation.md` and `~/.codex/AGENTS.md`. The Rig chezmoi thread has `+/_THREADS/chezmoi/` in flight.

**Query:** Should the Rig chezmoi thread review the diff, apply and push these with its own work?

**Options:**

a) (recommended) Yes: Rig chezmoi reviews `chezmoi diff`, applies and pushes them on its restart.

b) You review and apply them yourself.

### SHAPE-AGREE - nested Project folders and one naming migration

**Context:** As drafted in the [summary draft](/Users/krisbrown/.local/state/ki/agents/ways-of-working/summary-draft.md) and [thread ids](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/thread-ids.report.md): Projects nest as `Streams/Initiatives/<initiative>/<project>/<project>.md` with SHORT-NAMES (`model`, `foundations`), DESIGN-TIDY and six records. Absorbs DECISIONS-HOME, THREAD-IDS-AGREE, IDS-MIGRATE and NAMING-REST (withdraw NAME-ROOT, PILOT-LABEL `Personal > Acquire intake (sol)`, FOOTER-PROJECTS option a). Not on the restart path.

**Query:** Do you agree the shape and naming as one migration after the restart, harness checker first?

**Options:**

a) (recommended) Agree it as one migration after the restart: harness checker first, then folders, decisions logs and thread ids together.

b) Agree the shape now but migrate ids separately later.

### DIAGRAMS-EXPORT - diagrams that read in every previewer

**Context:** New; replaces DIAGRAMS and DIAGRAMS-RENDER. The cause is the Archify export's CSS, not Mermaid (see the [restart design report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/restart.report.md)). Hand-flattening each SVG does not last.

**Query:** Should the harness add a static light export and a rule for diagrams in designs?

**Options:**

a) (recommended) Add a ki-agentic-harness triage record: a static, flattened light option in `export-svg.ts`, and a rule in ki-pmo-design and ki-diagrams that design reports use text diagrams inline or exported static SVGs beside a Project note.

b) Keep the dual-theme SVG and accept flattening by hand when a previewer fails.

### IDEAS-ROOTING - where ideas start

**Context:** As drafted in the [summary draft](/Users/krisbrown/.local/state/ki/agents/ways-of-working/summary-draft.md): Rig stays a KI Initiative and a concept starts as an `Idea:` bullet in its owning Project or Initiative note. Absorbs GIT-SURFACE's capture.

**Query:** Do ideas start as `Idea:` bullets in the owning note, GIT-SURFACE first?

**Options:**

a) (recommended) Yes: a ki-principal run adds GIT-SURFACE as an `Idea:` bullet in the ways-of-working Project note, and later ideas follow the same rule.

b) Keep ideas in a separate scratch note until each is given a record.

```text
RESTART-AGREE

Agree the restart design §1 as written: one ki-agentic-harness run writes the §1.4 wording into ki-pmo, ki-delegation and ki-checkpoint, regenerates the surfaces with ki dev skill generate ki-pmo --write and pushes; ways of working then converts its checkpoint, writes READY into the state-of-play Messages block and tells me.

---

RUN-HYGIENE

Yes: each thread fixes its checkpoint form and adds role on its FIRST-STEP line at restart, and the generic brief footer gives way to an explicit push rule in the brief.

---

TOOLS-PUSH

Hand the five tools-ki commits (33770a8d, 80246ca6, 30513f9c, 4ef7b9c0, 90807355) to tools burndown: it reconciles the stack, cuts v0.10.6 and bumps ki-principal's .github/ki-version; the tools-ki state tooling joins KI-TOOL-KI-CLI-137.

---

HARNESS-ACCEPT

Present KI-HARNESS-GOV-195, KI-HARNESS-GOV-198, KI-HARNESS-GOV-203 and KI-HARNESS-OPS-005 to me in one ki-accept sitting after the restart, with the KI-HARNESS-GOV-203 30-day stale threshold put to me there.

---

CHEZMOI-APPLY

Rig chezmoi reviews chezmoi diff for 673b999, d81a80c and d1a6e6d, applies and pushes them on its restart.

---

SHAPE-AGREE

Agree the nested Project shape, SHORT-NAMES, DESIGN-TIDY, DECISIONS-HOME, THREAD-IDS-AGREE, IDS-MIGRATE and NAMING-REST as one migration after the restart: harness checker first, then folders, decisions logs and thread ids together.

---

DIAGRAMS-EXPORT

Add a ki-agentic-harness triage record for a static flattened light export option in export-svg.ts and a ki-pmo-design and ki-diagrams rule that design reports use inline text diagrams or exported static SVGs beside a Project note.

---

IDEAS-ROOTING

Ideas start as Idea: bullets in the owning Project or Initiative note; a ki-principal run adds GIT-SURFACE to the ways-of-working Project note first.
```

```text
╭─ run report · 2026-10-17T13:56:20Z ──────────────╮
│                                                  │
│  █▀▀▄ █▀▀▀ █▀▀▀ ▀▀█▀   · thread at rest          │
│  █▀▀▄ █▀▀  ▀▀▀█   █    · nothing running         │
│  █  █ █▄▄▄ ▄▄▄█   █    · nothing queued          │
│                                                  │
╰──────────────────────────────────────────────────╯
```

- [at rest] nothing running or queued
- [waiting] RESTART-AGREE
- [waiting] RUN-HYGIENE
- [waiting] TOOLS-PUSH
- [waiting] HARNESS-ACCEPT
- [waiting] CHEZMOI-APPLY
- [waiting] SHAPE-AGREE
- [waiting] DIAGRAMS-EXPORT
- [waiting] IDEAS-ROOTING
- [committed] restart.report.md, pushed
- [uncommitted] restart-consolidate.report.md, this owner report
