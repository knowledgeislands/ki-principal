# ki.chezmoi queries

## Open

- MSG-UNIFY: Kris asked why `ki git check-message` exists when Commitlint is a well-defined standard (03:47 BST). Answered; re-raised with b) recommended, high.
- STRICTNESS-CONFORM: decided (Decision 171).

## Held

Batch 2, after batch 1 is answered: RAT-UNCONFIRMED, RAT-READING, RAT-SPARK-VOICE, PRUNE-ACCEPTED, UE-082-FOLLOWUPS, 077-REVIEW-PATH, PENDING-REVIEW, READY-076, RESOLUTION-084, A-PRUNE.

- RAT-UNCONFIRMED, RAT-READING, RAT-SPARK-VOICE: from [rat-write](/Users/krisbrown/.local/state/ki/agents/chezmoi/rat-write.report.md); RAT-UNCONFIRMED and RAT-SPARK-VOICE in blind review (rat-blind).
- Six Git hook recommendations from [hooks-survey](/Users/krisbrown/.local/state/ki/agents/chezmoi/hooks-survey.report.md); the four medium ones in blind review (hooks-blind).
- PRUNE-ACCEPTED, UE-082-FOLLOWUPS: from [accept-delivered](/Users/krisbrown/.local/state/ki/agents/chezmoi/accept-delivered.report.md); in blind review (accept-blind). Reviews back: hooks-blind (FRAME-EMPTY b), CHEZMOI-HOOK b) medium, GOV-GAPS a), OUT-OF-SCOPE a), three survey corrections), rat-blind (RAT-UNCONFIRMED b), RAT-SPARK-VOICE a)).
- 077-REVIEW-PATH: from [build-077](/Users/krisbrown/.local/state/ki/agents/chezmoi/build-077.report.md), high, no review needed: Kris runs the Keychain delete on Terra and Sol, then a short run ticks the step and moves KB-DOTFILES-UE-077 to Awaiting review. accept-blind back: PRUNE-ACCEPTED a) medium, UE-082-FOLLOWUPS a) medium.
- PENDING-REVIEW, READY-076: from [fold-076](/Users/krisbrown/.local/state/ki/agents/chezmoi/fold-076.report.md), both medium; fold-blind back: PENDING-REVIEW defer to a follow-up record (high, missing option: split `chezmoi status` columns, mixed cases ambiguous), READY-076 Ready once PENDING-REVIEW is answered (high).
- MAIN-PUSH (high), A-PRUNE (high, deletion; prune-blind agrees: delete locally, high, history in main, no worktree, no remote copy): from [wt-survey](/Users/krisbrown/.local/state/ki/agents/hooks/wt-survey.report.md); STASH-DROP routed to ki.ways-of-working.
- AUDIT-LINT (high), EMPTY-EXIT, HARNESS-LINES, MSG-UNIFY, STRICTNESS, CHEZMOI-TESTS (medium): from [hooks-model](/Users/krisbrown/.local/state/ki/agents/hooks/hooks-model.report.md), note [git-hooks-model.md](design/git-hooks-model.md); the five medium ones in masked blind review (model-blind).
- RESOLUTION-084 (high): from [cancel-084](/Users/krisbrown/.local/state/ki/agents/chezmoi/cancel-084.report.md); KB-DOTFILES-UE-084 cancelled as `rejected` (chezmoi `3f7c9bd`).
- model-blind back: EMPTY-EXIT before the refusal (high, eight scratch scenarios pass), HARNESS-LINES all three out (high, CI covers each), MSG-UNIFY check-message everywhere (high, ten cases agree), STRICTNESS required lines plus forbidden list (high; missing option: an ordered allowlist), CHEZMOI-TESTS manual gate (medium).
