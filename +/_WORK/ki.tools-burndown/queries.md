# ki.tools-burndown queries

## Open

### SCR5-CONFORM - Keep the safer install-script repair

since 2026-10-19 · from hookstd.report.md in the run state folder

**Context:** The hooks design said the SCR-5 conform step should rewrite Husky's `prepare` install script to point Git at `.githooks` in every repository. In a repository that doesn't yet have committed `.githooks/pre-commit` and `commit-msg`, that would silently switch the commit gate off. hookstd made conform keep the Husky form until the committed hooks exist. The audit warns on SCR-5 the whole time, so the gap stays visible.

**Query:** Should SCR-5 conform keep the Husky install script until the committed hooks exist?

**Options:**

a) (recommended, confidence high - it only defers a change the audit already reports, and never unbinds the gate) Keep the behaviour as committed, and note the refinement in the hooks design.

b) Rewrite unconditionally, as the design states, and rely on the waves converting the hooks before conform runs.

### VA-HOOKS - First committed hook for va-principal

since 2026-10-19 · from hookconf.report.md in the run state folder · blind review hcreview pending

**Context:** va-principal has no `.husky/` and no `.githooks/`, so this conversion gives it nothing. A first composed hook needs the shape-skill claims mechanism, which is outside this record.

**Query:** How should wave 1 give va-principal its first committed hook?

**Options:**

a) (recommended, confidence medium - it unblocks the pilot without waiting on harness work) The wave run adds a hand-written frame-first `.githooks/pre-commit` (and `commit-msg` if va-principal has a package), then runs conform to bind it.

b) Capture the claims-mechanism record in ki-agentic-harness first, and hold va-principal out of wave 1 until it lands.

c) Drop va-principal from the pilot and pilot with tools-ki and ki-principal only.

### HOOK-RELEASE - When the conversion release goes out

since 2026-10-19 · from hookconf.report.md in the run state folder · blind review hcreview pending

**Context:** Once `6c386801` ships in a release, every `ki repo conform` with `ki-repo` selected converts a Husky repository, estate-wide.

**Query:** When should the `ki` release carrying it go out?

**Options:**

a) (recommended, confidence high - the pilot is the conversion's first real run) Release after the wave 1 pilot passes on the local source build, folding in any refusal fixes it surfaces.

b) Release now, so the pilot runs on a released build.

### HOOK-CAPTURE - Capture the two follow-up records now

since 2026-10-19 · from hookconf.report.md in the run state folder · blind review hcreview pending

**Context:** The design note still lists the claims mechanism and the `ki estate converge` binding sweep as "To capture". The second is tools-ki work; the first belongs to the harness.

**Query:** Should they be captured now?

**Options:**

a) (recommended, confidence medium - both are known follow-ups that the pilot will need to plan against) Capture the binding sweep as a tools-ki triage record and the claims mechanism as a ki-agentic-harness triage record, each in its own short run.

b) Leave both in the design note until the pilot reports.

## Parked

### ASK-B - Coarse acquisition kind in the public export

since 2026-10-19 · from rigsite-config.report.md in the run state folder · parked: ASK-B a), under HIGH-CONFIDENCE on 19 October; release: the rig.midnight.ninja side asks

**Context:** Ask B has no go-ahead. If it goes ahead, a `kind` or `form` field derived as application or command-line would get past the site's forbidden-field check. Platform variants complicate it, because one tool can install differently on macOS and Linux. It would widen the public export (RIG-PUB-002).

**Query:** Keep Ask B parked?

**Options:**

a) (recommended, confidence high - there is no go-ahead, and it widens the public boundary) Keep it parked and raise it only when Kit asks.

b) Capture it at triage now, marked as waiting for Kit's go-ahead.
