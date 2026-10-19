# ki.tools-burndown queries

## Open

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
