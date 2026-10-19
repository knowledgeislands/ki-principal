# estmig-org options

## YORK-YARN - apps-yorkphotosoc.org is a Yarn repository

**Context:** apps-yorkphotosoc.org locks Husky in `yarn.lock` and has no `core.hooksPath` set. Conform refuses until Husky is removed through Yarn, and that removal rewrites `yarn.lock` and may need the network.

**Query:** How should apps-yorkphotosoc.org leave Husky?

**Options:**

a) Hold it for a run that is allowed to run `yarn remove husky`, which may need the registry, and then conform.

b) Leave it on Husky until it moves to Bun.

### PKG-NO-HUSKY - Package-backed repositories without Husky

**Context:** hnr-principal has a metadata-only `package.json`, with no dependencies or lockfile. legal-principal is an npm package with no Husky and no commitlint. HOOK-3 expects a `commit-msg` hook in any package-backed repository, but neither repository has a commit-message tool installed.

**Query:** Should these two get the Knowledge Base pre-commit gate now, with `commit-msg` waiting for KI-TOOL-KI-CLI-161?

**Options:**

a) Write the ki-repo-kb pre-commit as in va-principal and bind it. Add a `prepare` binding to legal-principal. Leave HOOK-3 as a WARN until `ki git check-message` ships.

b) Add commitlint and lint-staged to each repository so that it matches the package-backed form. This needs installs from the network.

### NO-GATE - Project repositories without a package or a declared gate

**Context:** apps-dafacts.org, apps-kris.me.uk and acquire are `ki-repo-project` repositories without a package. No shape skill they declare names a pre-commit command, so a hook would only have the frame and nothing to run.

**Query:** Should these three get a committed hook now?

**Options:**

a) Write a pre-commit that runs `ki repo audit --skill ki-repo --staged` check-only, and record in the harness that this is the project-shape gate.

b) Leave them without a hook until `ki-repo-project` declares a gate criterion.
