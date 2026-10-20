# ki.ways-of-working queries

## Open

### OWNER-QUEUE - Cap building while acceptance lags

Answered a) in principle; "checks" asked back.

### CHECKOUT-ISOLATION - Stop sessions colliding in shared checkouts

checkout-iso recommends a) staged mix, medium; ci-review (Codex, 02:41 BST) agrees a), medium, with two conditions: serialise the whole shared-checkout Git write window (hooks and post-commit check included), and give worktree audits dependency and runtime parity before judging them, the pilot counting swept files, false audit findings and integration failures. Review only partly blind (a decision-log summary surfaced in a search). Lifted to high, reviewed. Options: a) staged mix with the two conditions; b) worktrees everywhere (reverses MAIN-NOT-WORKTREES); c) no change.

### WORKTREE-AUDIT - Write down the worktree audit recipe

From ci-green, medium; in blind review (cg-review). a) harness record adds the isolated-home plus `ki repo repair` recipe to `AGENTS.md` Verification and `ki-delegation`; b) `ki repo audit` reports it as one setup finding.

### HOOK-4-CLASS - Test every external tool a hook calls

From ci-green, medium; in blind review (cg-review). a) harness record tightens HOOK-4 at WARN after a fleet census; b) keep HOOK-4 and rely on review.

### PLANNED-READY - Settle the seven planned harness records

From ci-green, medium; in blind review (cg-review). a) take the listed answers and mark GOV-200, -205, -214, -215, -220, -221, -223 Ready; b) GOV-215 and GOV-220 now, the rest one by one.

### NO-GATE - unparked

Project shape commit gate; reviewed, a) `ki repo audit --skill ki-repo` staged, check-only. Unparked by Kris at 02:55 BST; full query drafted by unpark-draft, then blind review unless already reviewed.

### GFM-HOSTING-RULES - unparked

harness protected `main` declaration; a) `branch-protection = true`, awaiting blind review. Unparked by Kris at 02:55 BST; full query drafted by unpark-draft, then blind review unless already reviewed.

### HARNESS-TRIAGE - unparked

eight harness triage dispositions from lane-triage; awaiting blind review. Unparked by Kris at 02:55 BST; full query drafted by unpark-draft, then blind review unless already reviewed.

### PRINCIPAL-TRIAGE - unparked

OPS-014 to Next, prune GOV-035; awaiting blind review. Unparked by Kris at 02:55 BST; full query drafted by unpark-draft, then blind review unless already reviewed.

### PKGLESS-GATE - unparked

keep the package-less pre-commit gates in homebrew-tap and ki-specifications and give each concrete shape an explicit content owner in the harness hooks contract; taken with NO-GATE on resume. Unparked by Kris at 02:55 BST; full query drafted by unpark-draft, then blind review unless already reviewed.

## Parked

None.
