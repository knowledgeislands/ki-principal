# ki.ways-of-working queries

## Open

### OWNER-QUEUE - Cap building while acceptance lags

Answered a) in principle; "checks" asked back.

### CHECKOUT-ISOLATION - Stop sessions colliding in shared checkouts

checkout-iso recommends a) staged mix, medium; ci-review (Codex, 02:41 BST) agrees a), medium, with two conditions: serialise the whole shared-checkout Git write window (hooks and post-commit check included), and give worktree audits dependency and runtime parity before judging them, the pilot counting swept files, false audit findings and integration failures. Review only partly blind (a decision-log summary surfaced in a search). Lifted to high, reviewed. Options: a) staged mix with the two conditions; b) worktrees everywhere (reverses MAIN-NOT-WORKTREES); c) no change.

### WORKTREE-AUDIT - Write down the worktree audit recipe

Reviewed (cg-review agrees, on condition it is validated against CI's pinned v0.11.3 and repair cannot touch the real registry): high. a) harness record adds the isolated-home plus `ki repo repair` recipe to `AGENTS.md` Verification and `ki-delegation`; b) `ki repo audit` reports it as one setup finding.

### HOOK-4-CLASS - Test every external tool a hook calls

Reviewed (cg-review agrees, on condition coverage includes conditional gate tools and the census measures fleet impact first): high. a) harness record tightens HOOK-4 at WARN after a fleet census; b) keep HOOK-4 and rely on review.

### PLANNED-READY - Settle the seven planned harness records

Review disagrees (cg-review, high: listed answers are not approved decisions; Ready only GOV-215 and GOV-220, rest one by one): medium, both views shown. a) take the listed answers and mark GOV-200, -205, -214, -215, -220, -221, -223 Ready; b) GOV-215 and GOV-220 now, the rest one by one.

### NO-GATE - unparked

Project shape commit gate; reviewed, a) `ki repo audit --skill ki-repo` staged, check-only. Unparked 02:55 BST; drafted in `design/unparked-queries.md`. Review disagrees (widen KI-HARNESS-GOV-225 to own the three shapes' content, medium).

### GFM-HOSTING-RULES - unparked

harness protected `main` declaration; a) `branch-protection = true`, awaiting blind review. Unparked 02:55 BST; drafted in `design/unparked-queries.md`. Review disagrees (settle the intended policy and read live GitHub rules before declaring, medium).

### HARNESS-TRIAGE - unparked

eight harness triage dispositions from lane-triage; awaiting blind review. Unparked 02:55 BST; drafted in `design/unparked-queries.md`. Reviewed, agrees with corrections (Future not Later; adoption is not permission to implement): high.

### PRINCIPAL-TRIAGE - unparked

OPS-014 to Next, prune GOV-035; awaiting blind review. Unparked 02:55 BST; drafted in `design/unparked-queries.md`. Reviewed, agrees (high, reviewer's own confidence high): high; KI-PRINCIPAL-OPS-014 pilot into Now after the pin move.

### PKGLESS-GATE - unparked

keep the package-less pre-commit gates in homebrew-tap and ki-specifications and give each concrete shape an explicit content owner in the harness hooks contract; taken with NO-GATE on resume. Unparked 02:55 BST; drafted in `design/unparked-queries.md`. Folded into NO-GATE by unpark-draft; answering NO-GATE answers it.

### NET-DOWN - Weekly direction target, not a cap

From finish-first (`design/finish-first.md`), medium; review disagrees (counts only, medium).

### WIP-CAP - Per-work cap and what it counts

From finish-first (`design/finish-first.md`), medium; review disagrees (two caps, three in progress and eight awaiting, as a bounded trial, medium).

### CAPTURE-ORIGIN - Checkable capture gate with an origin field

From finish-first (`design/finish-first.md`), medium; review disagrees (prose only with an exact authority reference, medium).

### HANDOFF-AS-MESSAGE - Handoffs and sweeps stop creating records everywhere

From finish-first (`design/finish-first.md`), medium; review disagrees (messages for routing; receiver records only at real acceptance boundaries, high).

### STALE-SWEEP - Re-decide drafts untouched for 30 days

From finish-first (`design/finish-first.md`), medium; review disagrees (60 days, no default cancel, medium).

### ACCEPT-BUNDLE - One acceptance answer per work

From finish-first (`design/finish-first.md`), medium; reviewed, agrees with conditions: high.

### STASH-DROP - Drop two old ki-principal stashes

From ki.chezmoi's wt-survey (02:18Z): `stash@{1}` (17 October, Rig Decision 80, reached main in `a3156df3`) and `stash@{0}` (19 October, overtaken `state.md` line) look safe to drop. Deletion, so blind review stash-review first.

## Parked

None.
