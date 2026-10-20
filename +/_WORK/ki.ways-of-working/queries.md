# ki.ways-of-working queries

## Open

### OWNER-QUEUE - Cap building while acceptance lags

Answered a) in principle; "checks" asked back.

### CHECKOUT-ISOLATION - Stop sessions colliding in shared checkouts

checkout-iso recommends a) staged mix, medium; ci-review (Codex, 02:41 BST) agrees a), medium, with two conditions: serialise the whole shared-checkout Git write window (hooks and post-commit check included), and give worktree audits dependency and runtime parity before judging them, the pilot counting swept files, false audit findings and integration failures. Review only partly blind (a decision-log summary surfaced in a search). Lifted to high, reviewed. Options: a) staged mix with the two conditions; b) worktrees everywhere (reverses MAIN-NOT-WORKTREES); c) no change.

## Parked

- NO-GATE - Project shape commit gate; reviewed, a) `ki repo audit --skill ki-repo` staged, check-only.
- GFM-HOSTING-RULES - harness protected `main` declaration; a) `branch-protection = true`, awaiting blind review.
- HARNESS-TRIAGE - eight harness triage dispositions from lane-triage; awaiting blind review.
- PRINCIPAL-TRIAGE - OPS-014 to Next, prune GOV-035; awaiting blind review.
- PKGLESS-GATE - keep the package-less pre-commit gates in homebrew-tap and ki-specifications and give each concrete shape an explicit content owner in the harness hooks contract; taken with NO-GATE on resume.
