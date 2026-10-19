---
id: ki.portable-specifications
state: with-worker
blocking: false
since: 2026-10-19T22:45Z
received: 2026-10-19T18:00Z
beat: null
mark: 2026-10-19T18:00Z
method_read: f4d6c521
---

# ki.portable-specifications state

## Now

- Decided: SPEC-HOME, SPEC-VERSION, CONFORMANCE-LEVELS, ENTRY-NAMES (upper case) and PROJECT-NAME (keep apart, `portable-specifications`); query-review-3 confirmed PROJECT-NAME at high confidence.
- rename landed in `d935e493` (the pure moves rode in ki.baseline-rollout's `a90aea3b`); the Project note is [portable-specifications](../../Streams/Projects/portable-specifications.md).
- plan received; [design/plan.md](design/plan.md) holds the ten steps. SPEC-LIVE-READ decided and live-read running; four queries with Kris: WORK-PROFILE, KNOWLEDGE-SKILL, MOVE-GATE, SPEC-LOCATION.
- HOOKS-MIGRATION (IMPORTANT, State of play, 23:41 BST) replaces HOOK-GUARD; this work holds no `package.json`, `bun.lock`, `.husky/` or `.githooks/` changes, so nothing to commit for it.

## Next steps

1. On SPEC-LIVE-READ: one read-only run writes `design/agentskills-check.md`.
2. After it and WORK-PROFILE, KNOWLEDGE-SKILL and SPEC-LOCATION: one run revises the drafts (plan step 3), then a blind review and SPEC-TEXT to Kris.
3. Then home the specs in `ki-work-package`, `ki-acquire` and the new knowledge skill, in parallel, in ki-agentic-harness.

## Held

None
