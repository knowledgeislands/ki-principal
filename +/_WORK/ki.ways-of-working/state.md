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

- ki-agentic-harness: wow-night-harness-files10 (launched directly at 02:32 BST to reconcile FILES-10 with ASSEMBLE-1 under RIG-BASELINE), then wow-night-harness-queue-c, then wow-night-harness-224-accept-c (the -b runs returned blocked on HARNESS-AUDIT-HOME, fixed by wow-night-audit-home-fix). wow-night2-obs-vis-042-c waits on wow-night-harness-224-accept-c (wow-night-audit-home-fix proved the audit home at 02:25 BST).
- tools-ki: wow-night-toolski-baseline (DONE). wow-night-tools-ki-queue-c stopped at 02:51 BST on WRITER-MISMATCH (queued with the queue-b brief). Current writer: wow-night-tools-ki-queue-d, launched directly at 02:52 BST. The coordinator then launches directly, one at a time: wow-night-tools-ki-release-candidate-c, wow-night-cli-140-plan-d, wow-night-cli-156-d, wow-night-cli-156-accept-d. Every queued tools-ki run (-b and -c) is superseded. LAUNCH-DEFAULTS is deferred to Kris (DEFAULTS-CONTRACT).
- apps-observatory.local: wow-night-observatory-queue-b (the first run returned blocked on AUDIT-HOME, now prepared), then wow-night-brg-006-accept-b, wow-night2-obs-vis-042-c, wow-night2-obs-vis-042-accept-c (re-chained at 02:31 BST; the un-suffixed vis-042 pair is superseded).
- tools-rig: wow-night-harness-files10 reported DONE at 02:39 BST (harness 7dc5bb8a; tools-rig audit PASS=16 WARN=4 FAIL=0, the warnings tools-rig-owned), so the chain below is live, wow-night-rig-baseline-b first (wow-night-rig-048-d returned RIG-BASELINE at 02:45 BST: two FILES-10 failures on tools-rig .ki.toml lines 41 and 42), then wow-night-rig-048-g (wow-night-rig-048-c and -d are superseded). wow-night-rig-baseline returned blocked on RIG-BASELINE (a harness FILES-10 rule defect, not a tools-rig fault); every queued -b tools-rig run is superseded and stops on this designation. The coordinator launches the chain run by run: wow-night-rig-048-g, wow-night-rig-048-accept-c, wow-night-rig-067-c, wow-night-rig-067-accept-c, wow-night-rig-056-c, wow-night-rig-056-accept-c, then wow-night-tools-rig-release-candidate-c. At 03:03 BST wow-night-rig-048-e stopped on RIG-PREFLIGHT-WARNINGS and RIG-AUDIT-ACTIVATION and is superseded by wow-night-rig-048-g. At 03:17 BST wow-night-rig-048-f stopped on RIG-PLAN-GATE (its own draft's findings) and is superseded by wow-night-rig-048-g.
- ki-principal (work packages only): wow-night-principal-queue-c, then wow-night-parked-queries-c (re-chained at 02:31 BST to wait on the final run of every lane; the -b runs are superseded).
- tools-techne: none. KI-TOOL-TECHNE-CLI-006 (wow-night2-techne-006) is held for Kris under TECHNE-006-REVIEW: it builds guarded host stop and destroy commands, and Kris asked to review that plan.
- Any run name not listed here is superseded and stops on this designation.

## Held

- PAPERCLIP-REQ, on hold while Kris gets KI stable; not tied to a Wave (2026-10-19).
