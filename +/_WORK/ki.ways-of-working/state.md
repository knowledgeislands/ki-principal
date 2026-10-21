---
id: ki.ways-of-working
state: with-worker
since: 2026-10-21T00:40:30Z
received: 2026-10-21T00:40:30Z
beat: null
mark: 2026-10-21T00:40:30Z
method_read: eff6163b
---

# ki.ways-of-working state

## Now

- 01:40 BST mark: Kris answered the overnight queries (all a)); this work controls KI overnight. A Codex planning run writes the overnight briefs; the coordinator dispatches about three at a time.

## Next steps

- Overnight burndown of the tools-, mcp- and apps- roadmaps under the 01:40 answers: rig CORE-048 and CORE-067 against fixtures; CORE-056 investigation once the Rig hook fix lands; CLI-140 offline planning; CLI-156 with read-only CI; BRG-006 headless check and acceptance; release candidates prepared for Kris to tag; ki.tools-burndown and ki.observatory authorised queue lines; verified overtaken parked queries struck.
- Email routing: Kris resumes hnr.email-routing with priority on its 11 records; this work leaves them alone.
- ENACTMENT-ADMIN narrowing (Admin only) comes back to Kris soon.
- Deferred from the 01:40 mark: decisions strike and design/ review.
- Blocked: KI-PRINCIPAL-ECO-013 re-review on other works' audits; KI-TOOL-RIG-CORE-056 merge on RIG-PRECOMMIT-BATS; KI-HARNESS-GOV-224 rework with ki.observatory.

## Writers

Each repository lane has one active writer at a time; the designation passes to the next run in the chain once its predecessor reports DONE with its outcome committed, or on an explicit blocked handoff. Designated at 02:00 BST under the 01:40 and 01:55 grants:

- ki-agentic-harness: wow-night-harness-files10 (DONE, 7dc5bb8a). The queue dispatcher is stalled behind a blocked dependency, so at 03:39 BST the coordinator launched wow-night-harness-queue-d directly as the current writer, then launches wow-night-harness-224-accept-d directly. The queued wow-night-harness-queue-c and wow-night-harness-224-accept-c are superseded.
- tools-ki: wow-night-tools-ki-queue-d (DONE, pushed f95bc710); wow-night-toolski-close-flake (DONE); wow-night-cli-140-plan-f (DONE 04:25 BST, CLI-140 Ready, d6e8f369 pushed). Current writer: wow-night-cli-156-d, launched directly 04:25 BST; then wow-night-cli-156-accept-d, then wow-night-tools-ki-release-candidate-d. Every queued tools-ki run and earlier suffix is superseded. LAUNCH-DEFAULTS deferred to Kris (DEFAULTS-CONTRACT).
- apps-observatory.local: wow-night-observatory-queue-b (DONE, 92c51a6b) and wow-night-brg-006-accept-d (DONE, BRG-006 accepted); wow-night2-obs-vis-042-g DONE 04:46 BST (VIS-042 awaiting review, c9a03fd4 and c5d49f22). Current writer: wow-night2-obs-vis-042-accept-g, launched directly 04:47 BST; its one roadmap writing checkout is its owned worktree `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-night2-obs-vis-042-accept-g.work/worktrees/apps-observatory.local`. Earlier suffixes and queued runs are superseded.
- tools-rig: wow-night-rig-048-g and wow-night-rig-048-accept-c DONE (CORE-048 accepted, 52d0d8b2 pushed); wow-night-rig-067-c and wow-night-rig-067-accept-d DONE (CORE-067 accepted, 3cc18f65 pushed); wow-night-rig-056-d stopped 04:54 BST on RIG-056-EVIDENCE. Current writer: wow-night-rig-056-e, launched directly 04:55 BST; then wow-night-rig-056-accept-e, wow-night-tools-rig-release-candidate-d, each launched directly in turn. Earlier suffixes and queued runs are superseded.
- ki-principal (work packages only): wow-night-principal-queue-d DONE 04:38 BST (0b1a0c7f; 15 lines received, 25 pending). Then wow-night-parked-queries-d after every lane's final run, also routing AUDIT-OUTSIDE-LANE findings. The queued -b and -c runs are superseded.
- tools-techne: none. KI-TOOL-TECHNE-CLI-006 (wow-night2-techne-006) is held for Kris under TECHNE-006-REVIEW: it builds guarded host stop and destroy commands, and Kris asked to review that plan.
- Any run name not listed here is superseded and stops on this designation.

## Held

- PAPERCLIP-REQ, on hold while Kris gets KI stable; not tied to a Wave (2026-10-19).
