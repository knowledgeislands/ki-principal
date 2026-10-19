# ki.tools-burndown queries

## Open

### SCR5-CONFORM - Keep the safer install-script repair

since 2026-10-19 · from hookstd.report.md in the run state folder

**Context:** The hooks design said the SCR-5 conform step should rewrite Husky's `prepare` install script to point Git at `.githooks` in every repository. In a repository that doesn't yet have committed `.githooks/pre-commit` and `commit-msg`, that would silently switch the commit gate off. hookstd made conform keep the Husky form until the committed hooks exist. The audit warns on SCR-5 the whole time, so the gap stays visible.

**Query:** Should SCR-5 conform keep the Husky install script until the committed hooks exist?

**Options:**

a) (recommended, confidence high - it only defers a change the audit already reports, and never unbinds the gate) Keep the behaviour as committed, and note the refinement in the hooks design.

b) Rewrite unconditionally, as the design states, and rely on the waves converting the hooks before conform runs.

### HOOK-GUARD - Confine the conversion to the waves until release

since 2026-10-19 · from hcreview.report.md in the run state folder

**Context:** The installed `ki` runs straight from the tools-ki checkout, so the unreleased hooks conversion is already live. Any session that runs `ki repo conform` without `--dry-run` on a KI repository with Husky now converts it - rewriting hooks, `package.json` and `bun.lock`, deleting `.husky/` and changing the binding - outside the waves Kris grants. An IMPORTANT warning went to State of play at 23:20 BST.

**Query:** Should conform convert hooks only when explicitly asked, until the release?

**Options:**

a) (recommended, confidence high - the review verified the exposure directly, and a switch confines conversion to granted waves) A short tools-ki run, after wave1 finishes its tools-ki step, adds an opt-in switch so conform converts hooks only when asked; the waves pass it, and whether the release keeps it is decided at the release.

b) Rely on the State of play warning until the release.

### VA-HOOKS - First committed hook for va-principal

since 2026-10-19 · from hookconf.report.md in the run state folder · reviewed by hcreview (Codex, high)

**Context:** va-principal has no Husky, no `.githooks/` and no `package.json`, so the conversion gives it nothing. Composing its hook from the skills needs a claims mechanism not yet built. It is the pilot's package-less case.

**Query:** How should wave 1 give va-principal its first committed hook?

**Options:**

a) (recommended, confidence high - reviewed: a hand-written hook tests the package-less shape without waiting on the claims work) The wave run writes a frame-first `.githooks/pre-commit` running the staged KB audit, leaves out `commit-msg` until KI-TOOL-KI-CLI-161 ships, binds it with conform, and checks both the refusal without `ki` and a passing commit.

b) Capture the claims mechanism first, and hold va-principal out of wave 1 until it lands.

c) Drop va-principal from the pilot and pilot with tools-ki and ki-principal only.

### HOOK-RELEASE - When the conversion release goes out

since 2026-10-19 · from hookconf.report.md in the run state folder · reviewed by hcreview (Codex, high)

**Context:** Once released, every `ki repo conform` on a KI repository with Husky converts it, estate-wide. The pilot is the conversion's first real run. The review notes that holding the release alone does not contain it (HOOK-GUARD).

**Query:** When should the `ki` release carrying it go out?

**Options:**

a) (recommended, confidence high - reviewed: pilot before publication) Release after the wave 1 pilot passes on the local build, folding in any fixes it surfaces; KI-TOOL-KI-CLI-162 `ki markdown gfm` ships in the same release.

b) Release now, so the pilot runs on a released build.

### HOOK-CAPTURE - Record the follow-ups now

since 2026-10-19 · from hookconf.report.md in the run state folder · reviewed by hcreview (Codex, high)

**Context:** The hooks design lists two follow-ups as "to capture": a `ki estate converge` sweep that sets the hook binding on every checkout, and the claims mechanism for composing hooks from skills. The review found the claims mechanism is mostly tools-ki host code, with only the declarations and standards in the harness.

**Query:** Should they be recorded now?

**Options:**

a) (recommended, confidence high - reviewed, ownership corrected) Capture scopes now, plans refined by pilot evidence: a tools-ki record for the binding sweep, a tools-ki record for hook composition and the claims host, and a linked ki-agentic-harness record for the claim declarations and standards.

b) Leave them in the design note until the pilot reports.

## Parked

### ASK-B - Coarse acquisition kind in the public export

since 2026-10-19 · from rigsite-config.report.md in the run state folder · parked: ASK-B a), under HIGH-CONFIDENCE on 19 October; release: the rig.midnight.ninja side asks

**Context:** Ask B has no go-ahead. If it goes ahead, a `kind` or `form` field derived as application or command-line would get past the site's forbidden-field check. Platform variants complicate it, because one tool can install differently on macOS and Linux. It would widen the public export (RIG-PUB-002).

**Query:** Keep Ask B parked?

**Options:**

a) (recommended, confidence high - there is no go-ahead, and it widens the public boundary) Keep it parked and raise it only when Kit asks.

b) Capture it at triage now, marked as waiting for Kit's go-ahead.
