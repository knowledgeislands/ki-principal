---
id: ki.ways-of-working
state: with-worker
since: 2026-10-22T07:24:00Z
received: 2026-10-22T07:24:00Z
beat: null
mark: 2026-10-22T07:24:00Z
method_read: eff6163b
---

# ki.ways-of-working state

## Now

- 08:24 BST mark. Overnight burn-down under Kris's 02:25 and 02:28 grants and the triage-and-draft grant; the coordinator's waiter lapsed from 04:02 to 08:22.
- Awaiting fresh reviews: KI-TOOL-TECHNE-CLI-006 (after wow-fix-cli006), KI-DESIGN-ELE-001 planning (after wow-replan3-ele001), KI-OBSERVA-VIS-030 (after a591c48d), tools-ki integration range 51725e8b..a9aba774 (rereview5).
- Harness: KI-HARNESS-GOV-189, KI-HARNESS-OPS-010, KI-HARNESS-OPS-011 and KI-HARNESS-GOV-209 delivered, refused for pruning by review a; NO-GATE needs an offline fix.
- PRINCIPAL-RECONCILE: the shared ki-principal checkout blocked a run's pull; diagnose before any ki-principal push.
- `ki agent send` fails while ki.mac-studio-setup's events.jsonl has lost an observed terminal outcome.

## Next steps

- Coordinator: launch the pending reviews; a Harness fix run for NO-GATE and the surviving links; on rereview5 acceptance, admit and push tools-ki; prune only on three agreeing high-confidence accepts.
- Kris: RIG-RELEASE-REVIEW-BOUNDARY, CUSTOMS-WORDS, TAGS-NEXT, ECO013-CANCEL; the RIG-ATTENDED walk-through; visual checks for KI-OBSERVA-BRG-005 and KI-OBSERVA-VIS-030.

## Held

- PAPERCLIP-REQ, on hold while Kris gets KI stable (2026-10-19).
- Email-routing records stay with hnr.email-routing.
