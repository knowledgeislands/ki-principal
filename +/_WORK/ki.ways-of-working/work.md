---
id: ki.ways-of-working
level: project
title: 'KI > Model > Ways of working'
project: ways-of-working
theme: model
worker: agent
supervisor: owner
state: with-worker
since: 2026-10-18T17:03:00Z
received: null
beat: null
mark: 2026-10-18T17:12:06Z
created_at: 2026-10-09T20:58:00Z
---

# ki.ways-of-working

## Next steps

Resumed 18 October 17:39 BST after a hold from 12:40 BST; parked queries back with Kris. The mark stays at 11:06 BST (`2026-10-18T10:06:05Z`) so Kris can review from it; every run report since the mark is kept in this folder, and the Summary of 11:47 BST is rebuilt from them.

Done since the mark (reports here): mgit-st-quiet (`mgit st` quiet, live, KI-TOOL-MGIT-CLI-024; a `git stash` slip, restored), mark-prune, work-folder-rename (`ki-work-folder`, §4 division, GOV-200 checks recorded, KI-TOOL-KI-CLI-150 at triage), config-preserve (KI-TOOL-KI-CLI-143 follow-up), release-ki-0112 (v0.11.2 released, Homebrew, ki-principal pins it), harness-upkeep (KI-HARNESS-GOV-194 and -201 awaiting review, grants adopted, Haiku 5.5 noted), rumdl-upgrade (harness on 0.3.0), territory-rename (seven other-territory `.ki.toml` renamed and pushed). Nothing is running or queued.

On resume:

1. Give Kris the Summary since the mark with the parked queries below, in batches.
2. Restarts with Kris: KI > Rig > chezmoi (Messages carry the rename, then the Sol and Terra re-runs on v0.11.2); KI > Foundations > Tools burndown (since 2026-10-18T03:30:38Z) and KI > Model > Observatory (since 2026-10-18T01:27:13Z), prompts given at 11:41 BST; then KI > SoP; Mac Studio setup and Knowledge acquisition when wanted.
3. Owed launches: DESK-KIT-SOP (remove the desk-kit lines); RIG-LOCK-FOLLOWUP independent review, then a Rig ki-accept sitting and the Rig release (RIG-LOCK-RELEASE a).
4. Outstanding, no action: KI-HARNESS-GOV-200 checks and KI-TOOL-KI-CLI-150 unbuilt; the thread-model diagram and two `ki agent` "thread home" strings still carry old names; ki-engineering SCR-11 fails in the harness (pre-existing).

## Messages

None

## Parked

- MGIT-QUIET-RULES - how mgit knows no-news replies for other commands (decisions log 11:14). a) built-in rules for common Git commands with alias expansion, plus your own rules in `~/.config/mgit/` kept in chezmoi, after a run proposes rules from the commands you use.
- PRINCIPAL-AUDIT-RED - ki-principal CI audit has 75 failures, 72 unlinked identifiers in old `+/_WORK/` reports (release-ki-0112 report). a) one run tidies under `ki-work-folder`, links the rest, fixes the three single findings.
- GRANT-INTERIM - a brief may hand-append an approved grant until `ki agent --allow` ships (harness-upkeep report). a) keep the sentence until KI-TOOL-KI-CLI-134 ships.
- REVIEW-GOV-194-201 - KI-HARNESS-GOV-194 and -201 await review (harness-upkeep report). a) one independent review run, then acceptance with Kris.
- RUMDL-ESTATE - 28 repositories still pin rumdl 0.2.78 (rumdl-upgrade report). a) move them through their gates, then switch MD005 and MD075 back on and add `--preflight`; the website after Claude Design.
- ACQUIRE-RENAME - `personal/acquire/.ki.toml` line 89 still declares `ki-checkpoint` (territory-rename report). a) the same one-line rename, repair, commit and push.
- MGIT-FLAGS-ACCEPT - close KI-TOOL-MGIT-CLI-025 (mgit-flags report). a) accept now, hands-on findings into KI-TOOL-MGIT-CLI-023.
- MGIT-017-CONFIRM - KI-TOOL-MGIT-CLI-017 accepted provisionally (accept-mgit report). a) record it confirmed.
- MGIT-FLAGS-CONFIRM - read-back of the `-B` answer, as built (accept-mgit report). a) yes.
- BATS-CLEANUP - 71 non-fatal Bats assertions in tools-mgit and tools-rig (bats-rule report). a) one triage record in each.
- MARK-FIELDS - field names for the working-area mark, KI-HARNESS-GOV-214 (harness-followups report). a) `work`, with `run`/`agent` or `session`, sidecar `mark.toml`.
- SYNC-GUARD - where the level-before-resume check lives (sync-telemetry report). a) fold into KI-HARNESS-GOV-189 using `mgit fetch` and `mcp-git-audit`.
- CHANNEL-TELEMETRY - cross-Mac channel (sync-telemetry report). a) ntfy on Sol, tailnet-only, behind KI-TOOL-KI-CLI-123 phase 2; telemetry deferred.
- None open. Kris answered the 16 October queries, regrouped in the [restart design report (deleted)](https://github.com/knowledgeislands/ki-principal/blob/ab526abed0d493bddd9c44ddb48c104d7fa2c846/+/_THREADS/ways-of-working/restart.report.md) as RESTART-AGREE, RUN-HYGIENE, TOOLS-PUSH, HARNESS-ACCEPT, CHEZMOI-APPLY, SHAPE-AGREE, DIAGRAMS-EXPORT and IDEAS-ROOTING, with option a) at 22:50 BST on 17 October, with QUIET-GATE, QUIET-STYLE, QUIET-HOOK, ACT-HOME, ACT-THREAD, ACT-NAMES and ACT-WORK (decisions log); STATE-AGREE, IDENTITY-NEXT and NAMING folded into them. Their follow-ons are the pick-up block's next steps. The thread-states design will bring new queries.
- Answered on 15 October and held in the decisions log, their reports deleted: DEPS-HOLD, PMO-7-BACKLOG, AREAS-REFRESH, RECORD-NAME, THREADS-CONTENT, THREADS-TMP-HOME, THREADS-TELL, THREADS-CLEAR, IDEA-STAGE, IDEA-CAP, REGISTRY-RECORD, PAUSE-CONDITION, PRIORITY-FIELD, STREAMS-INDEX, SOP-DROPPED, HEADING-LASTING and AREAS-OVERTAKE. Overtaken: PUSH-OTHERS, PUSH-CARRY, PUSH-LINKS, CHECKPOINT-PUSH, CHECKPOINT-LINKS and ECO014-BRIEF.
- Held: PAPERCLIP-REQ, until Wave F. Waves A to D and F, re-anchoring, the thread status line, the inbox channel and messaging follow the pilot's lessons.
- Parked 2026-10-09: a gradual move from Obsidian-style to GitHub-flavoured Markdown, starting with a front-matter field declaring a note's flavour.
