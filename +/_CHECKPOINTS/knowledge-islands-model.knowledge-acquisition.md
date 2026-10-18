---
type: ki-checkpoint
thread: knowledge-islands-model.knowledge-acquisition
label: 'Knowledge Islands Model: knowledge-acquisition'
role: coordination
state: active
created_at: 2026-10-08T08:35:00Z
updated_at: 2026-10-18T00:59:00Z
---

# knowledge-islands-model.knowledge-acquisition

**Pick-up - mark 2026-10-15T14:59Z (15:59 BST)**

- **Status:** rest. 18 October to 01:48 BST, Kris's go-ahead (01:40 BST) on DISPATCH-PUSH, RETURN-ROUTE, ROUTING-SOURCE and PORTS-RENAME delivered as records, nothing built: KB-ACQUIRE-007 "Dispatch push and return" and KB-ACQUIRE-008 "Routing knowledge cards" in acquire (triage), acquire's AGENTS.md and README describe the port with durable routing knowledge (`c02f1ea`), KI-HARNESS-GOV-209 "+/_ACQUIRED/ inbound area" in the harness linked to KB-ACQUIRE-007 (`c6b6dd4b`), and the Acquisition Process note names the capability "ports", the harbour as its Arcadian register, and the push dispatch rule (`cbf5de6`). Personal's Decision 7 (pull to push) sent via the state-of-play inbox for Personal's acquire-dispatch thread. Two Haiku fix runs died mid-task; Sonnet reruns finished them. All repositories pushed. Dispatch handover from Personal taken 18 October (01:55 to 01:58 BST): dispatch-take pushed acquire `321f55f` (KB-ACQUIRE-007 carries the ChatGPT exports refresh step and the MS3 CHAT, IMAGES and MIXED-routing questions; context/chatgpt/personal/README.md routes uncertain or mixed chats to `_review`; AGENTS.md and README.md name this Project as dispatch's owner); HNR's MS3 share (COPY-HASH, ATTACH, RECEIVER, PROPOSALS, EXCLUDED) sent through the state-of-play inbox; Project note says dispatch came from Personal on 18 October (`85d5d22`, record IDs dropped under STREAM-9). Running: nothing. Queued: nothing. Waiting on state-of-play: PILOT-SEED, OBSERVATORY-FIRST, and forwarding Decision 7 to Personal. Open queries for Kris: none (PROCEED-DEFAULT).
- **Resume:** `Resume Knowledge Islands Model: knowledge-acquisition under current ki-pmo and ki-delegation since 2026-10-15T14:59:00Z: re-bootstrap, mark, fresh summary with carried-forward open points, take stock, restart authorised work, then banner.`
- **Next steps, in order:** plan KB-ACQUIRE-007, KB-ACQUIRE-008 and KI-HARNESS-GOV-209 when Kris names acquisition work next, piloting dispatch on one territory; follow state-of-play on the Observatory and PILOT-GO.

## Objective

The provider-neutral acquisition lifecycle is documented in one Pillars note, AI sessions are acquired into owning repositories with verified retirement of the source, and the browser-runtime and WhatsApp spool questions are settled ([knowledge-acquisition](../../Streams/Projects/knowledge-acquisition.md), Initiative [knowledge-islands-model](../../Streams/Initiatives/knowledge-islands-model/knowledge-islands-model.md)).

## Current state

- Running: nothing. Queued: nothing.
- Done: [KI-HARNESS-OPS-005](../../../ki-agentic-harness/docs/roadmap/KI-HARNESS-OPS-005-acquire-ai-sessions.md) and [KI-PRINCIPAL-MOD-006](../../Streams/Roadmap/KI-PRINCIPAL-MOD-006-knowledge-acquisition-lifecycle.md). In triage: [KI-PRINCIPAL-MOD-009](../../Streams/Roadmap/KI-PRINCIPAL-MOD-009-amend-adr-001-staging-wording.md) and [KI-HARNESS-GOV-209](../../../ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-209-acquired-inbound-area.md). Held: [DOTFILES-UE-035](https://github.com/krisb/dotfiles/blob/main/docs/roadmap/DOTFILES-UE-035-install-whatsapp-spool-refresh.md) with chezmoi.
- KI-PRINCIPAL-MOD-006's Granola evidence paths point at the private `acquire` repository (ACQ-PATHS, 2026-10-14). The browser-runtime question (KI-HARNESS-GOV-087) is merged into KI-HARNESS-OPS-005.
- 2026-10-17 messages acted on: OWNER-LANE (KI-TOOL-KI-CLI-128 and KI-TOOL-KI-CLI-139 delivered by tools-burndown as the single tools-ki writer; this thread gives priority and acceptance input); GOV-195-RENUMBER (keep KI-HARNESS-GOV-195, change nothing); AWAITING-REVIEW (KI-PRINCIPAL-MOD-006 presented as AUDIT-GATE).
- 2026-10-18 messages acted on: RUN-HYGIENE FIRST-STEP (this checkpoint brought to current form, `role` set) and DISPATCH-HANDOVER (taken; MS3-SPLIT as recommended under Kris's "you shouldn't need to ask me anything").
- ki-pmo read at c6b6dd4b.
- Thread folder: +/_THREADS/knowledge-acquisition/ ([thread folder](../_THREADS/knowledge-acquisition/)).
- Mark: 2026-10-15T14:59:00Z.

## Decisions made

- Thread working rules (re-read after any compaction): this thread coordinates only the knowledge-acquisition Project and runs substantive work as background agents through `ki agent` in run `knowledge-acquisition`. Coordination follows ki-pmo (three rules: never do substantive work in-thread, every unit goes to a detached background agent, an owner message never pre-empts work in flight; at most five tool calls per turn). Every report to Kris is a ki-delegation owner report (banner; What has been done; What is in progress; Outstanding queries with stable tags; closing reply block), at the quiet level: short timestamped status lines, minimal visible tool use, outcomes only, no raw output, and decisions described by what was decided and when, never by number. Standing rules from the master thread (2026-10-14): burn the roadmap down and capture no new feature records; other threads' committed work may be pushed beneath ours when checks pass, naming it; connection-critical changes need a tested restore path; follow-up releases stop and ask first.
- Standing rules: PROCEED-DEFAULT (act on the recommended course and report it; ask only where his rules require his word); FOLD-AUTHORITY; FOLD-TRIGGER; reports to Kris in plain language; a verified, pushed drop is retired as the last intake step (Kris, 23:40 BST).
- The master thread `state-of-play` owns cross-project priorities, releases and decisions; this thread works only this Project's records.
- The lifecycle note changes `Pillars/`, so Enactment Process rules apply to it.
- 2026-10-14 (ACQ-PATHS, from the master thread): repoint KI-PRINCIPAL-MOD-006's Granola paths at the `acquire` repository. Done; reading `acquire` is read-only evidence.
- 2026-10-14 (Kris): commit everything this thread does or oversees by explicit path and check finished agents' work is committed and pushed at each report; tidy the thread folder at every mark; 5-minute heartbeat while work runs.
- Earlier decisions (SPIRIT, TOWER, RESET-FIRST, GRANOLA-PLAN, BINARY-PROOF and the rest) are in [decisions.md](../_THREADS/knowledge-acquisition/decisions.md).

## Files touched

- This checkpoint.
- [KI-PRINCIPAL-MOD-006](../../Streams/Roadmap/KI-PRINCIPAL-MOD-006-knowledge-acquisition-lifecycle.md) (Granola paths repointed).

## Open questions

- Handed off (HANDED-OFF, Kris, 2026-10-15): acquire-intake owns all acquire work; ways-of-working owns DIAGRAMS and the report-heading fix. Not tracked here.
- Held: KB-DOTFILES-UE-035 with chezmoi, review 21 October.
- Parked 2026-10-11: ChatGPT territory keys move to kebab-case territory names; island-model-and-tending renames the kit-principal capture folders.

## Next step

Read the `dispatch-take` result, decide the Personal dispatch items with Kris where his rules need his word, and delegate what is authorised; commit by explicit path.
