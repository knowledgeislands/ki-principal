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

- ki-agentic-harness: wow-night-harness-queue-c, then wow-night-harness-224-accept-c (the -b runs returned blocked on HARNESS-AUDIT-HOME, fixed by wow-night-audit-home-fix). wow-night2-obs-vis-042 waits on wow-night-harness-224-accept-c.
- tools-ki: wow-night-toolski-baseline (wow-night-cli-140-plan returned blocked on ROADMAP-REGISTRY, a pre-existing audit warning), then wow-night-cli-140-plan-b, wow-night-cli-156-b, wow-night-cli-156-accept-b, wow-night-tools-ki-queue-c, then wow-night-tools-ki-release-candidate-b. All other tools-ki run names, including wow-night-tools-ki-queue-b, are superseded and stop on this designation. LAUNCH-DEFAULTS is deferred to Kris (DEFAULTS-CONTRACT).
- apps-observatory.local: wow-night-observatory-queue-b (the first run returned blocked on AUDIT-HOME, now prepared), then wow-night-brg-006-accept-b, wow-night2-obs-vis-042, wow-night2-obs-vis-042-accept.
- tools-rig: wow-night-rig-baseline (wow-night-rig-048 returned blocked on RIG-BASELINE, a red FILES-10 audit on main), then wow-night-rig-048-b, wow-night-rig-048-accept-b, wow-night-rig-067-b, wow-night-rig-067-accept-b, wow-night-rig-056-b, wow-night-rig-056-accept-b, wow-night-tools-rig-release-candidate-b. The un-suffixed first-wave rig runs are superseded and stop on this designation.
- ki-principal (work packages only): wow-night-principal-queue-b, then wow-night-parked-queries-b.
- tools-techne: none. KI-TOOL-TECHNE-CLI-006 (wow-night2-techne-006) is held for Kris under TECHNE-006-REVIEW: it builds guarded host stop and destroy commands, and Kris asked to review that plan.
- Any run name not listed here is superseded and stops on this designation.

## Held

- PAPERCLIP-REQ, on hold while Kris gets KI stable; not tied to a Wave (2026-10-19).
