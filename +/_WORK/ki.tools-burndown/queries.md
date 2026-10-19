# ki.tools-burndown queries

## Open

### SYNC-CATEGORIES - Outcome categories

since 2026-10-19 · from mgitplan.report.md in the run state folder · reviewed by qreview6 (Codex, high)

**Context:** Today sync prints one line for each checkout that changed or has a problem, but it adds none of them up. The record needs a fixed set of outcomes that every repository falls into. Reviewer adds: specify precedence for dirty checkouts whose fetch also failed, retaining both reasons.

**Query:** Which outcomes should the tally count, and where does each kind of skip fall?

**Options:**

a) (recommended, confidence medium - every checkout gets exactly one outcome, and "failed" means Git itself went wrong) Use five outcomes: in sync, pulled, pushed, skipped and failed. Skipped covers local changes, detached HEAD, no upstream, diverged, failed fetch, bare repositories and your own `-i` refusals. Failed covers only `status failed`, `cannot compare`, `pull failed` and `push failed`.

b) Add a sixth outcome, "need attention", as `overview` has. It would take diverged, dirty, detached and no-upstream checkouts, and leave skipped for bare repositories and your refusals.

c) (reviewer's view, confidence high - A fetch error belongs with operational failures within five exclusive outcomes) Count a failed fetch as failed, not skipped.

### SYNC-STREAMS - Standard streams

since 2026-10-19 · from mgitplan.report.md in the run state folder · reviewed by qreview6 (Codex, high)

**Context:** Today every sync line goes to standard output. The `ki-repo-tools` command-line conventions put warnings and progress on standard error. [KI-TOOL-MGIT-CLI-029](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-029-cli-convention-departures.md) owns departures from those conventions across the commands. Reviewer adds: include prompts and diagnostic detail on standard error; the proposed deferral record currently excludes new departures.

**Query:** Should this record move sync's warning lines to standard error?

**Options:**

a) (recommended, confidence medium - this keeps the record bounded, and lets one record settle streams for every command) Leave the streams as they are, and record the departure on KI-TOOL-MGIT-CLI-029.

b) (reviewer's view, confidence medium - Apply the existing stream convention while changing this output contract) Do it here: move the skip, warning and progress lines to standard error, and keep the tally and the per-repository result lines on standard output.

### YORK-YARN - apps-yorkphotosoc.org is a Yarn repository

since 2026-10-20 · estmig-org.report.md in run state folder · at qreview9

**Context:** apps-yorkphotosoc.org locks Husky in `yarn.lock` and has no `core.hooksPath` set. Conform refuses until Husky is removed through Yarn, and that removal rewrites `yarn.lock` and may need the network.

**Query:** How should apps-yorkphotosoc.org leave Husky?

**Options:**

a) (recommended, confidence medium - it matches the brief's no-network rule and keeps the lockfile honest) Hold it for a run that is allowed to run `yarn remove husky`, which may need the registry, and then conform.

b) Leave it on Husky until it moves to Bun.

### PKG-NO-HUSKY - Package-backed repositories without Husky

since 2026-10-20 · estmig-org.report.md in run state folder · at qreview9

**Context:** hnr-principal has a metadata-only `package.json`, with no dependencies or lockfile. legal-principal is an npm package with no Husky and no commitlint. HOOK-3 expects a `commit-msg` hook in any package-backed repository, but neither repository has a commit-message tool installed.

**Query:** Should these two get the Knowledge Base pre-commit gate now, with `commit-msg` waiting for KI-TOOL-KI-CLI-161?

**Options:**

a) (recommended, confidence medium - both are Knowledge Bases, so the gate is already declared and needs no install) Write the ki-repo-kb pre-commit as in va-principal and bind it. Add a `prepare` binding to legal-principal. Leave HOOK-3 as a WARN until `ki git check-message` ships.

b) Add commitlint and lint-staged to each repository so that it matches the package-backed form. This needs installs from the network.

### NO-GATE - Project repositories without a package or a declared gate

since 2026-10-20 · estmig-org.report.md in run state folder · at qreview9

**Context:** apps-dafacts.org, apps-kris.me.uk and acquire are `ki-repo-project` repositories without a package. No shape skill they declare names a pre-commit command, so a hook would only have the frame and nothing to run.

**Query:** Should these three get a committed hook now?

**Options:**

a) (recommended, confidence low - it closes HOOK-1 with a real check-only command, but no skill declares it yet) Write a pre-commit that runs `ki repo audit --skill ki-repo --staged` check-only, and record in the harness that this is the project-shape gate.

b) Leave them without a hook until `ki-repo-project` declares a gate criterion.

## Parked

### ASK-B - Coarse acquisition kind in the public export

since 2026-10-19 · from rigsite-config.report.md in the run state folder · parked: ASK-B a), under HIGH-CONFIDENCE on 19 October; release: the rig.midnight.ninja side asks

**Context:** Ask B has no go-ahead. If it goes ahead, a `kind` or `form` field derived as application or command-line would get past the site's forbidden-field check. Platform variants complicate it, because one tool can install differently on macOS and Linux. It would widen the public export (RIG-PUB-002).

**Query:** Keep Ask B parked?

**Options:**

a) (recommended, confidence high - there is no go-ahead, and it widens the public boundary) Keep it parked and raise it only when Kit asks.

b) Capture it at triage now, marked as waiting for Kit's go-ahead.
