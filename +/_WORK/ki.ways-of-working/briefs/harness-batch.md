# Harness delivery batch (SWEEP-DELIVER a), Kris 20 October)

Nobody else is working tonight. Kris: "They're authorized, so go along with those, fine with which we integrate." Repository `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`. Start only after `/Users/krisbrown/.local/state/ki/agents/ways-of-working/harness-standards.status` ends with `DONE` (check every minute), then pull.

1. Merge KI-HARNESS-GOV-196 into KI-HARNESS-GOV-200 (SWEEP-MERGE a)): GOV-200 takes its goal and steps; GOV-196 cancelled as merged.
2. Under `ki-batch`, deliver KI-HARNESS-GOV-200, -205, -214, -215, -220 and -221, then KI-HARNESS-GOV-223 if harness-standards made it Ready. Completion target: awaiting review, with a full packet each. Expiry: 10:00 BST. Serialise edits to shared files (coordination rubric, diagrams standard). Stop only an item whose prerequisite fails; carry on with the rest. Each in a worktree on its own `run/` branch, fast-forwarded into local `main` after gates pass, then pushed fast-forward only.
3. Do not accept or prune.

Never `--no-verify` or force-push; push only commits made tonight by this programme. CAPTURE-GATE: follow-ups as `messages.md` lines. HOOK-GUARD. British English, ASCII hyphens. Report per record: state, commits, gates, pushed.
