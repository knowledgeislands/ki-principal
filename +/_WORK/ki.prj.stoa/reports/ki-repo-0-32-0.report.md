# [Foundations](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Stoa](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/stoa.md) › ki-repo-0-32-0

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 04:18 GMT · last mark 02:46 GMT**

---

## Done

- `packages-stoa` is now a Knowledge Islands repository. It has title Stoa, repository code `STOA`, the `ki-repo-project` shape, private visibility, the Capital, the harness and the local `roadmap` adapter over `docs/roadmap/`. The `ki-repo-tools` shape needs one command under `bin/` with an installer, which Stoa does not have, so `ki-repo-project` is the nearest shape. The code `STOA` keeps [STOA-CMD-001](/Users/krisbrown/kis/knowledge-islands/packages-stoa/docs/roadmap/STOA-CMD-001-command-k-palette.md) and the existing `ADR-STOA-052` to `055` as they are.
- Five commits, stacked on the 0.32.0 release commit `d534135`:
  - `2a99117` declares the repository: `.ki.toml`, `CLAUDE.md`, the README title and root package metadata.
  - `f5e2ee2` adds the managed ignore rules and the `+` and `-` working areas.
  - `c6dcac4` moves the two guides into `docs/guides/site/` with indexes.
  - `fc35058` adds the house Markdown settings and applies formatting-only fixes to root documents and decision records.
  - `119d6ad` gives [STOA-CMD-001](/Users/krisbrown/kis/knowledge-islands/packages-stoa/docs/roadmap/STOA-CMD-001-command-k-palette.md) a four-word title, the `now` horizon, a Current state and a Discussion section, and puts the ledger in its standard form. Scope and review evidence are unchanged.
- Nothing in `packages/stoa/` or `consumers.json5` changed.
- `ki-accept` would accept the record. It is `awaiting-review`, all five steps are ticked, its review packet sits directly before Discussion, and its governing checks pass: the roadmap audit with one warning (no assignee), the Markdown audit, and test, typecheck and lint. Nothing was closed.
- Checks on `119d6ad`: `bun run test`, `bun run typecheck` and `bun run lint` pass, and `git status` is clean.
- `ki repo audit`: the roadmap, Markdown, guides, work, Git and runtime audits pass. Three audits still fail, all named in the queries below: decision records (293 findings), engineering (18) and repository (2, the licence).
- The commits were pushed, but not by me: a scheduled `mgit sync --push` job on this machine pushed them at 04:16 GMT, seconds after the last commit. It also pushed the release commit at 03:59. The tag `v0.32.0` is probably local only, because `mgit` pushes branches, not tags.
- My first audit read the live GitHub settings once. After that I ran every audit with GitHub calls blocked.
- The repository fix wrote two commit hooks that need tools that are not installed. They would have blocked every later commit, including the release run's, so I removed them and unset the local hook setting. That left `ki repo init`'s entry in the local repository registry and the ignored skill links under `.claude/skills` and `.agents/skills`.
- No inbox arrived during the run.

## In Progress

Nothing.

## Findings

### STOA-SHAPE - How a package repository differs from the tools shape

**Goal:** give the work that will write a skill for this repository shape a list of each way `packages-stoa` does not fit the `ki-repo-tools` shape.

**Scope:** `packages-stoa` at `119d6ad`, compared with the `ki-repo-tools` skill and its reference repositories `tools-ki` and `tools-mgit`. No other package repository was examined.

**As of:** 7 November 2026, 04:20 GMT.

| Aspect | Tools shape (`ki-repo-tools`) | Stoa (`packages-stoa`) |
| --- | --- | --- |
| What ships | One command under `bin/<tool>`, a `curl` installer, a Homebrew formula, optionally a manual and shell completion | A source tree, `packages/stoa/`, that each site copies whole into its own repository, under a SHA-256 lock (`stoa-lock.json`). There is no binary, installer, formula, manual, completion or package registry, and no site's build fetches the repository |
| Repository layout | One tool at the root | Two workspaces: `packages/stoa/`, the vendored product with its own tooling, tests, `units.json5` and `custom-elements.json`; and `apps/workbench/`, a visual check before release that sites can also export and publish as static files |
| Where the version lives | The tool's own version | `packages/stoa/package.json` and `units.json5`. The root `package.json` stays at `0.1.0` and is never released |
| Release | Release on demand: tag, build artefacts, update the formula | Bump the two version files, add a `CHANGELOG.md` section with breaking changes marked, and tag `v<version>`. Then message each consumer to re-vendor. Nothing is built or published |
| Consumers | Installed by users; no register | `consumers.json5` lists every site. Each site runs `drift`, then `sync` or `defer` with a reason. A deferral older than two releases becomes a query to the owner. Each site's `AGENTS.md` carries a fixed sync paragraph, and its `self:stoa:verify` fails the site's build on any local edit |
| Change rule | Change and release the tool | A change to `packages/stoa/` that a site would notice is a release. A behaviour-neutral change still changes every site's lock hash on the next re-vendor. Every unit change needs tests and a workbench story |
| Genericity | Not applicable | Units must stay generic. Site or organisation detail reaches a unit only through configuration, a slot, a `--stoa-*` custom property or the site's own adapter. Site names appear only in `consumers.json5` |
| Code form | TypeScript or Bash with `ki-engineering`'s toolchain | Plain ES modules, typed with JSDoc and checked by `tsc --checkJs`. They are Custom Elements in light DOM, with no runtime dependency and styles in three named cascade layers. `ki-engineering` flags `.mjs` files (BUN-2), the absence of a tsconfig in each workspace, and the script names |
| Script names | `ki:` and `self:` prefixes under the script-naming law | `test`, `typecheck`, `lint`, `workbench` and `workbench:export`. `AGENTS.md` names them and consumers' briefs rely on them. Consumers already use `self:stoa:*` for the vendoring tools |
| Required guides | `docs/guides/developer/definition-of-done.md` and `releasing.md` | No such guides. Release and change rules live in `AGENTS.md` |
| Decision records | One repository scope | Records come from two earlier repository names, with `ADR-PORTAL-FRAMEWORK-001` to `051` followed by `ADR-STOA-052` onwards |

A package-repository skill would own five things: the vendoring contract (the lock, `verify`, `drift`, `sync` and `defer`); the consumer register and its deferral rule; release-and-notify; the version locations; and the sync paragraph consumers must carry. It would also own workbench story coverage. It would say how plain JavaScript typed with JSDoc composes with `ki-engineering`, and it would replace the tools skill's binary, installer and formula checks.

## Queries

### Q1 STOA-RELEASE-STATE - 0.32.0 was already cut before this run · blocking

**Context:** The brief said `main` stood at `e37e43c` and that the release run would cut 0.32.0 from what I left. In fact the release commit `d534135` ("chore(release): stoa 0.32.0") and the annotated tag `v0.32.0` already existed, made at 03:59 GMT, apparently by the first release attempt, and `d534135` was already on `origin`. [STOA-CMD-001](/Users/krisbrown/kis/knowledge-islands/packages-stoa/docs/roadmap/STOA-CMD-001-command-k-palette.md) is still `awaiting-review`. My five commits now sit after the tag, on `origin` too, because of the `mgit sync --push` job. None of them changes `packages/stoa/`, so sites see no difference. As briefed, the release run would try to create a tag that already exists.

**Query:** How should the release run treat 0.32.0?

**Options:**

a) (recommended, confidence high - the release is already cut and published, and nothing I added reaches sites) Keep `v0.32.0` where it is. Re-brief the release run to accept STOA-CMD-001 through `ki-accept`, check the tag, and push the tag if `origin` lacks it. Leave my repository-only commits unreleased until the next real release.

b) Move `v0.32.0` to the new head so the declaration ships inside 0.32.0. This rewrites a tag that may already be published, and adds nothing sites can use.

c) Cut 0.32.1 for the repository-only commits. It adds a release with no change for sites, and every site would get a notice to re-vendor for nothing.

### Q2 STOA-LICENCE - Stoa has no licence

**Context:** The repository standard requires a `LICENSE` file and a matching `license` field in `package.json`; without a declaration it assumes MIT. Stoa has neither. Its code is copied into every site, and public sites serve it to the world. The other private Knowledge Islands app, Agora, uses an all-rights-reserved `LICENSE` with `UNLICENSED`.

**Query:** Which licence should Stoa carry?

**Options:**

a) (recommended, confidence medium - it matches Agora and changes nothing for your own sites) All rights reserved: copy Agora's `LICENSE`, and declare `license = "UNLICENSED"` in `.ki.toml` and the root `package.json`.

b) MIT, as the public tools use, which lets anyone reuse the code they can read on a public site.

c) Leave it for now, and accept two failing repository findings.

### Q3 STOA-DECISIONS - Bring the 55 inherited decision records to the standard

**Context:** `docs/decisions/` holds 55 records named `ADR-`, `PDR-` and `GDR-PORTAL-FRAMEWORK-NNN` from the repository's two earlier names, followed by `ADR-STOA-052` to `055`. The decision-records standard wants every record in the repository's own scope (`STOA`), in one unbroken numbered series per type, with frontmatter, Context and Consequences sections, and a complete index. That accounts for 293 failing findings. Renaming the records to `ADR-STOA-001` to `051` keeps their numbers and closes the gap before `052`. But it renames record ids, which the brief reserved for you, and some sections need content, not just formatting.

**Query:** Should the decision records be migrated?

**Options:**

a) (recommended, confidence medium - it clears most failing findings and keeps every number) Capture a roadmap record in `packages-stoa` to rename the records to the `STOA` scope with their numbers kept, add the missing frontmatter and sections, and complete the index. A candidate area is `DOC`.

b) Turn the decision-records coverage check off in `.ki.toml`, and leave the records as they are.

c) Leave the findings standing.

### Q4 STOA-TOOLCHAIN - Adopt the engineering toolchain

**Context:** `ki-engineering` reports 18 failures. Fixing them needs:

- new development tools (commitlint, knip, rumdl, lint-staged, syncpack), installed from the network;
- commit hooks that need those tools;
- renaming the scripts `test`, `typecheck`, `lint` and `workbench` to the `ki:` or `self:` naming;
- a TypeScript config in each workspace, and a module-boundary ruleset;
- dependency updates;
- converting a test fixture in `packages/stoa/` from `.mjs`.

The renames would change commands that `AGENTS.md` and the release brief name. The fixture lives in the vendored tree.

**Query:** Should Stoa adopt the toolchain, and when?

**Options:**

a) (recommended, confidence medium - it is real work that touches the commands everyone uses, so it should be planned) Capture a roadmap record to adopt the toolchain after 0.32.0, planned with the package-repository skill from STOA-SHAPE so that the script names and the JSDoc-typed JavaScript are settled once.

b) Turn the engineering checks that do not fit a package repository off in `.ki.toml`.

c) Leave the findings standing.

### Q5 STOA-GITHUB - Issues and Projects are switched on

**Context:** My first audit read the live GitHub settings. Issues and Projects are on, and the standard wants both off unless the repository declares GitHub Issues as its work tracker. Changing live settings was outside this run.

**Query:** Should an attended session switch them off?

**Options:**

a) (recommended, confidence high - Stoa's work lives in `docs/roadmap/` and the Capital, not in GitHub Issues) Yes: switch both off with `ki repo conform` in an attended session.

b) Keep them on and record a check override in `.ki.toml`.

### Q6 STOA-PUSH - A scheduled job pushes run commits

**Context:** A `mgit sync --push` job on this machine runs every few minutes. It pushes any clean repository that is ahead of `origin`, so a brief's "push nothing" cannot hold. It published my commits and the 0.32.0 release commit within seconds.

**Query:** Should runs that must not push be protected from the sync job?

**Options:**

a) (recommended, confidence medium - briefs keep promising no push when the machine pushes anyway) Raise it with the Rig work: either the sync job skips repositories with an active run, or briefs stop promising no push.

b) Accept it: a run's commits are published as soon as they land.

### 🤖 → 👤 Handoff to supervisor · blocked · at 04:18 GMT

👤 6 with you

- [blocked] Q1 STOA-RELEASE-STATE, 0.32.0 already tagged before this run · Kris · since 04:18 GMT
- [with you] Q2 STOA-LICENCE · Kris · since 04:18 GMT
- [with you] Q3 STOA-DECISIONS · Kris · since 04:18 GMT
- [with you] Q4 STOA-TOOLCHAIN · Kris · since 04:18 GMT
- [with you] Q5 STOA-GITHUB · Kris · since 04:18 GMT
- [with you] Q6 STOA-PUSH · Kris · since 04:18 GMT

🧵 ki.prj.stoa
