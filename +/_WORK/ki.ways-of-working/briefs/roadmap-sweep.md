# roadmap-sweep - get Knowledge Islands roadmaps to single figures

Kris: "The key thing for me now is to get this roadmap under control and get us down to single-figures. ASAP." The sweep covers the roadmap items ("webmoth -> roadmap").

## Task

Read-only across every Knowledge Islands repository with a roadmap (ki-principal, ki-agentic-harness, tools-ki, ki-specifications, apps-observatory.local, ki-techne-harness, tools-techne, tools-rig, tools-mgit, tools-git-almanac, homebrew-tap, mcp-*). For each open record propose one disposition: accept (awaiting review, evidence met), close as done, merge into named record, convert to a messages.md line (rollouts and handoffs, which Kris says are not roadmap items), cancel (with reason), keep. Write `design/roadmap-sweep.md`: counts per repository now and after the proposals, then batches Kris can answer in one word each: one ACCEPT bundle per owning work (oldest first, each record linked, one line outcome and concern), then merge, convert, cancel batches, then what stays. Say which repositories reach single figures and what still blocks the rest. Write `briefs/sweep-review.md`: a masked blind review brief for the cancel, merge and convert batches (Context and Query only, unranked options, no reads of `+/_WORK/` or reports). Commit both by explicit path.

## Limits

- CAPTURE-GATE: create no new roadmap records. HOOK-GUARD: never run `ki repo conform` without `--dry-run`.
- Harness edits only in a worktree, never the primary harness checkout. Never `--no-verify`, never force-push, push only your own commits fast-forward. Stay out of ki-design and apps-knowledgeislands.info.
- Nothing destructive (cancel, prune, delete, GitHub setting change) without it coming back as a query.
- British English, ASCII hyphens, they/them. Read Kris's words in `decisions.md` ("owner answers on the 03:08 BST send") first.

## Report

Owner report: Done, In Progress, Queries (Context, Query, Options; a) recommended with confidence).
