# ki.tools-burndown queries

## Open

### COMMIT-MSG - Message checks in package-less repositories

since 2026-10-19 · from hooksstd.report.md in the run state folder

**Context:** Commitlint needs Node and an install, so the 21 package-less repositories have no message check. A shell pattern in each stub would copy the `ki-git` vocabulary 21 times and drift.

**Query:** How should package-less repositories check commit messages?

**Options:**

a) (recommended, confidence high - reviewed, one source for the vocabulary and no Node dependency, though it adds a tools-ki command) Add `ki git check-message` for `.githooks/commit-msg` to call; until it ships, those repositories have `pre-commit` only.

b) A shell pattern in `.githooks/commit-msg`, generated from the `ki-git` vocabulary by conform.

c) No message check outside Bun repositories.

### ROLLOUT-AUTHORITY - Who writes the stubs in other repositories

since 2026-10-19 · from hooksstd.report.md in the run state folder

**Context:** The current decision makes adding a stub "that repository's change, raised as a receiver-owned trade", and the Charter gives territory selection no cross-repository write authority. Rolling out through `ki repo` and the estate repair means runs writing stubs in about 47 repositories. The blind review prefers b): ADR-KI-HARNESS-SKILLS-017 explicitly requires receiver-owned trades and the Charter denies inferred cross-repository authority, though an explicit bounded wave grant could authorise a different arrangement.

**Query:** Should one owner grant per wave cover `ki repo conform` writing and committing the stubs in every listed KI repository?

**Options:**

a) (recommended, confidence medium - review disagrees, it matches "through `ki repo`" and the change is mechanical, but each wave writes to repositories this work does not own) One grant per wave; a run commits the stubs and the `prepare` change by explicit path in each listed repository, local only, and you push.

b) Receiver-owned trades: this work ships the standard and the tool, and each repository's owning work runs `ki repo conform` itself.

## Parked

### ASK-B - Coarse acquisition kind in the public export

since 2026-10-19 · from rigsite-config.report.md in the run state folder · parked: ASK-B a), under HIGH-CONFIDENCE on 19 October; release: the rig.midnight.ninja side asks

**Context:** Ask B has no go-ahead. If it goes ahead, a `kind` or `form` field derived as application or command-line would get past the site's forbidden-field check. Platform variants complicate it, because one tool can install differently on macOS and Linux. It would widen the public export (RIG-PUB-002).

**Query:** Keep Ask B parked?

**Options:**

a) (recommended, confidence high - there is no go-ahead, and it widens the public boundary) Keep it parked and raise it only when Kit asks.

b) Capture it at triage now, marked as waiting for Kit's go-ahead.
