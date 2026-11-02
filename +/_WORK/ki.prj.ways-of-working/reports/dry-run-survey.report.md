# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › dry-run-survey

**🤖 → 👤 Handoff to supervisor · Run report at 02:04 GMT · last mark 01:41 GMT**

---

## Done

- Read-only survey of every write-switching flag across tools-ki, tools-rig, tools-mgit, tools-git-almanac, tools-techne, ki-techne-harness, packages-stoa, the eight `mcp-*` servers and the ki-agentic-harness scripts and skill documents: about 45 commands or tools listed below with flags, defaults and the change each needs.
- Found the convention's home: it is **ki-repo-tools**, not ki-engineering. ki-repo-tools already owns the command-line flag table and a house rule that says the opposite of DRY-RUN-FLAGS (preview by default with `--apply`, and `--dry-run` as opt-in for commands that act by default).
- Drafted the convention text, the rollout order by owner with draft message lines, the tolerance-window handling, and two queries (FORCE, as asked, and SCOPE, which the survey showed is needed before the text can be adopted).
- Nothing changed: no commits, no files written outside this report and the status file. The brief named no finding file, so findings are in this report only. No checks were run; this was a reading survey.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- When Kris answers FORCE and SCOPE, the convention text below needs its two marked sentences filled in, then one run to put it into ki-repo-tools (and the cross-reference into ki-repo-mcp) under this work.
- The reply to personal.reg.assistant-terra that DRY-RUN-FLAGS asks for is the coordinator's to send once the convention is settled.
- Revisions surveyed: tools-ki `573207b6`, tools-rig `8f77dd5`, tools-mgit `e84b055`, tools-git-almanac `e00938b`, tools-techne `ee97b67`, ki-techne-harness `f523233`, ki-agentic-harness `f4723b70`, MCP servers at their 27 October to 1 November heads. Local checkouts only; no fetch was made, so remote heads may be newer.

## Findings

### DRYRUN-SURVEY - Every flag that switches writing on or off

**Goal:** list each command that changes something, its current write flags and default, and what the convention would change.

**Scope:** KI-owned command-line tools, MCP servers and harness scripts and skill documents under `/Users/krisbrown/kis/knowledge-islands/`. Third-party tools' own flags (Biome `--write`, `git push --force`, kubectl `--dry-run=client`, `mise install --yes`, Headroom `--force`) are out of scope even where KI scripts call them. The dotfiles are excluded (with personal.reg.household-terra).

**As of:** 2 November 2026, 02:00 GMT, local checkouts at the revisions in In Progress.

Legend: "writes" means it changes things when run plainly; "previews" means it does not. "Flip" means the default changes to a dry run and `--no-dry-run` is added. "Rename" means the existing write switch becomes `--no-dry-run`. † marks a command that only falls in scope under SCOPE option b.

**tools-ki** (owner ki.prj.tools-burndown)

| Command | Current flags | Default | Change |
| --- | --- | --- | --- |
| `ki repo conform` | `--dry-run` | writes | Flip |
| `ki repo repair` | `--dry-run` | writes | Flip; it also breaks the existing "repair previews by default" rule today |
| `ki registry add` / `remove` | `--dry-run` | writes | Flip |
| `ki repo roadmap prune` | `--dry-run`, `--no-commit` | deletes and commits | Flip; `--no-commit` stays (it chooses how, not whether) |
| `ki repo roadmap migrate` | `--apply` | previews | Rename `--apply` |
| `ki estate converge` (manifest, `--rollback`, `--hooks`) | `--apply` | previews in every mode | Rename `--apply` |
| `ki manage repair` | `--dry-run`, `--apply` (mutually exclusive) | previews | Drop `--apply` for `--no-dry-run` |
| `ki manage vscode sync` | `--write` | previews | Rename `--write` |
| `ki repo store bind` / `unbind` / `absent` | `--write` (`absent` also `--clear`) | previews | Rename `--write`; `--clear` stays a selector |
| `ki trade receive` / `release` / `prune` | `--yes` ("confirm the previewed batch") | previews a batch; single `receive` writes | Rename `--yes`; flip single `receive` |
| `ki agent sweep` | `--write` | reports | Rename `--write` |
| `ki acquire import` / `images` | `--dry-run` | writes | Flip |
| `ki acquire mark` | `--confirm` | previews | Rename `--confirm` |
| `ki markdown gfm` | `--dry-run`, or `--preview <file>` with `--manifest <file>` | refuses without one | Write switch becomes `--no-dry-run`; the preview-and-manifest pair stays as its safety check |
| `ki dev skill generate` / `rubric` | `--write` | verifies | Rename `--write`; plain run becomes a dry run that also fails on drift (`--check` behaviour) |
| `ki repo skill add` / `ki skill add` | `--replace` | writes † | `--replace` is a safety override: see FORCE |
| `ki agent launch` / `queue` | `--dry-run` | launches † | Flip only under SCOPE b |
| `ki agent close` | `--delete` | archives † | `--delete` stays a selector; flip only under SCOPE b |
| No preview at all: `ki repo init`, `repo upgrade`, `bootstrap`, `harness install` / `reinstall` / `uninstall`, `manage mcp install` / `update` / `rollback` / `uninstall`, `manage update`, `batch prepare` / `run` / `close`, `trade prepare` / `submit` / `abandon`, `trade standing capture`, `kb index`, `dev local set` / `on` / `off`, `agent send` / `decide` / `stop` / `dequeue` / `new` / `home` / `reconcile` | none | writes † | Each needs a dry run under SCOPE b; none under SCOPE a |

**tools-mgit** (owner ki.prj.tools-burndown)

| Command | Current flags | Default | Change |
| --- | --- | --- | --- |
| `mgit register` (and `add`, `rm`) | `-n`, `--dry-run` | writes | Flip |
| `mgit repair` | `-n`, `--dry-run` | writes and clones | Flip; its spec also says `--apply` must be rejected, which stays true |
| `mgit structure standard` / `nested` | `-n`, `--dry-run` | converts | Flip |
| `mgit worktree remove` | `-f`, `--force` (discard a dirty linked worktree) | removes a clean one † | `--force` is an override in Git's sense: see FORCE |
| `mgit sync` | `-i`, `--interactive`, `--push` | pulls † | `--push` is a selector; flip only under SCOPE b |

**tools-git-almanac** (owner ki.prj.tools-burndown)

| Command | Current flags | Default | Change |
| --- | --- | --- | --- |
| `git almanac repair` | `--apply` | previews | Rename `--apply` |
| `git almanac config init`, `ignore`, `init`, `report` to a file | none | writes † | Flip only under SCOPE b |

**tools-rig** (owner ki.prj.mac-studio-setup)

| Command | Current flags | Default | Change |
| --- | --- | --- | --- |
| `rig apply` | `-n`, `--dry-run`, `--sudo` | applies | Flip (reconciles from state, so in scope under both SCOPE options) |
| `rig upgrade` | `-n`, `--dry-run`, `--unattended` | upgrades | Flip |
| `rig init` | `-n`, `--dry-run` | writes | Flip |
| `rig remove` | `-n`, `--dry-run`, `--apply`, then typed `remove` confirmation | previews | Rename `--apply`; the typed confirmation stays |
| `rig repair`, `rig capture` | `--output PATH` (new review file only), `-n` on capture | previews to standard output | No change: `--output` is an output destination, never an active source |
| `scripts/assemble-rig` | `--check` (default), `--write` | checks | Rename `--write` |

**tools-techne** (owner ki.prj.agent-host)

| Command | Current flags | Default | Change |
| --- | --- | --- | --- |
| `techne host setup` / `rebuild` / `withdraw` | `--dry-run`; overrides `--pull`, `--discard <repo>`, `--discard-unreadable-host` | acts | Flip; overrides stay named: see FORCE |
| `techne host start` / `stop` / `connect` | `--dry-run`; `stop --now` skips its safety read | acts † | Flip only under SCOPE b |

**ki-techne-harness** (owner ki.prj.agent-host): `operations/aws/agent-host/host/converge.sh` and `docs/guides/operator/agent-host.md` call `ki repo store bind|unbind ... --write`; switch to `--no-dry-run` once tools-ki ships it. kubectl `--dry-run=client` is third-party.

**MCP servers** (no current owning work; ki.prj.estate-factorisation is on hold, so route through ki.sop.main): already conform. ki-repo-mcp's rule 7 requires `dry_run`, default true, on destructive tools, and git-audit (commit, pull, push, remotes), gsuite (deletes), housekeeping-claude (14 tools), ki-kb-fs (write, delete), m365 (send, forward, reply, drafts, delete) and acquire-whatsapp (cleanup) all default to true. One exception: mcp-git-audit `git_repo_fetch` has `dry_run` default **false**; fetch with `prune` deletes remote-tracking refs. `git_repo_push force_mode` passes Git's own `--force` and m365 `auth_start force` forces re-authentication; both are overrides, not write switches. mcp-housekeeping-chatgpt's `app-server.ts delete --confirm <phrase>` is a typed confirmation with a separate `inventory` preview.

**ki-agentic-harness** (owner ki.prj.ways-of-working)

| Item | Current | Change |
| --- | --- | --- |
| `skills/repo-structure/ki-repo-harness/scripts/skill-graph.ts` | `--check` (default), `--write` | Rename `--write`; 11 `regenerate` lines in `docs/diagrams/diagrams.toml` follow |
| `skills/governance/ki-diagrams/scripts/build-html.ts` | writes; `--check` verifies | Flip; 4 skill documents follow |
| `skills/environment/ki-binding-chatgpt/scripts/render-codex.ts` | writes; `--check` or `--dry-run` previews | Flip |
| `skills/environment/ki-housekeeping-chatgpt/scripts/app-server.ts delete` | `--confirm <phrase>` | `delete` previews unless `--no-dry-run`; the phrase stays |
| Skill documents naming `ki dev skill rubric|generate --write` | 73 files | Change to `--no-dry-run` only after tools-ki ships it |
| Skill documents naming `ki repo conform --dry-run` | 29 files | No change: `--dry-run` stays valid as the explicit default |
| `ki-acquire-granola` standards (`ki acquire mark --confirm`) | 1 file | Follows the tools-ki rename |
| ki-repo-tools `standards-cli-conventions.md` and `standards-tool-repositories.md` | house rule and `repair` line say preview with `--apply`; `--dry-run` opt-in for commands that act by default | Rewrite (DRYRUN-DRAFT) |
| ki-repo-tools rubric `TOOL-CLI` | "Owned repair is preview-first with an explicit write path" | Split into a new judged item plus a static check (DRYRUN-HOME) |

Already conforming: the hook standards in ki-engineering, ki-repo and the ki-repo-* gate items forbid `--write` and `--fix` at commit time; that is about third-party formatters and needs no change.

### DRYRUN-HOME - Where the convention belongs

**Goal:** name the standard that should own the convention and the check that enforces it.

**Scope:** ki-agentic-harness skills.

**As of:** 2 November 2026, harness `f4723b70`.

| Candidate | Fit | Recommendation |
| --- | --- | --- |
| ki-repo-tools `references/standards-cli-conventions.md` | Already owns the common-options table (`-n`/`--dry-run`, `-f`/`--force`, `-y`/`--yes`) and the KI house rules; covers Bash tools (rig, mgit) as well as TypeScript | **Home** (recommended, high confidence - it is the only standard that already owns flag meanings, and leaving it unchanged would contradict the new rule) |
| ki-repo-tools `standards-tool-repositories.md#shared-cli-conventions` | Holds the `repair` rule ("default is a non-mutating preview, writing requires `--apply`") | Amend to point at the house rule |
| ki-repo-tools rubric | `TOOL-CLI` is judged; the conventions page says audit never runs a tool | Add a judged item `TOOL-DRY-RUN`, plus a static check over the manual, completions and help text that warns on `--apply`, `--write` or `--confirm` as options and on `--yes` or `--force` described as enabling a write; warning during the tolerance window, failure after |
| ki-repo-mcp rule 7 | Already requires `dry_run` default true | Cross-reference only; add "and an optional CLI's `--no-dry-run`" |
| ki-engineering | Owns TypeScript and Bun toolchains, not command-line surfaces; does not reach Bash tools | Not the home; no change |
| ki-repo-harness | Governs skill scripts in the harness | Cross-reference so skill scripts follow the same rule |

### DRYRUN-DRAFT - Convention text, rollout and tolerance window

**Goal:** give Kris a draft to adopt: the text, who changes what in which order, and how existing flags are handled meanwhile.

**Scope:** the KI-owned tools and the harness in DRYRUN-SURVEY.

**As of:** 2 November 2026, 02:04 GMT; two sentences wait on FORCE and SCOPE.

| Part | Draft |
| --- | --- |
| Convention text | See the fenced draft below the table |
| Rollout order | 1. This work: the standard in ki-repo-tools and its rubric item (warning only), the ki-repo-mcp and ki-repo-harness cross-references, and the four harness scripts. 2. Message lines, in parallel: ki.prj.tools-burndown (tools-ki, tools-mgit, tools-git-almanac; tools-ki first because the harness documents and ki-techne-harness depend on it), ki.prj.mac-studio-setup (tools-rig), ki.prj.agent-host (tools-techne, then ki-techne-harness's `--write` call after tools-ki ships), ki.sop.main (route `git_repo_fetch` to whichever work owns mcp-git-audit). 3. This work: the 73 skill documents and the granola standard, after tools-ki's release. 4. Window end: rubric item moves from warning to failure. The dotfiles proceed already with personal.reg.household-terra. |
| Tolerance window | Step A, each tool's next release, non-breaking: add `--no-dry-run` and accept `--dry-run`/`-n` on every in-scope command; old write switches (`--write`, `--apply`, `--confirm`, `--yes` used as a write switch) keep working as hidden aliases of `--no-dry-run`, each printing one line on standard error naming the replacement; help, completions, manual and README show only the new form. A command that writes by default today keeps writing but prints one notice line when run with neither flag: "from <version> this previews by default; pass --no-dry-run to keep writing". Step B, callers: every script, hook, brief and skill document passes `--dry-run` or `--no-dry-run` explicitly, which means the same before and after the flip. Step C, the following release: the default flips to a dry run and the old aliases become usage errors (exit 2) naming `--no-dry-run`. One window end date for all KI tools, set when the standard lands; the tools are pre-1.0, so a minor release may carry the flip, recorded in each changelog. |
| Draft message line (tools-burndown) | `2026-11-02 · DRY-RUN-FLAGS · from ki.prj.ways-of-working: adopt the dry-run house rule in ki-repo-tools for tools-ki, tools-mgit and tools-git-almanac in the order Step A, B, C; tools-ki first, since harness skills and ki-techne-harness wait on its --no-dry-run. Command list: dry-run-survey report.` |
| Draft message line (mac-studio-setup, agent-host, sop) | Same shape, naming tools-rig; tools-techne and the converge.sh call; and the `git_repo_fetch` default respectively |

Draft convention text, to replace the first house rule in ki-repo-tools `standards-cli-conventions.md`:

```markdown
**Dry run by default.** A command that changes anything - files, configuration, Git state, a remote service or the machine - is a dry run unless told otherwise. Run plainly, it reports what it would change, in the same words as the change ("would remove ..."), and changes nothing, preparatory steps included: no lock, staging, temporary or cache write, or remote call with effects. `--no-dry-run` makes it write. `--dry-run`, short `-n`, is accepted as the explicit default so that a script can say either; `--no-dry-run` has no short letter.

- No other option switches writing on: not `--write`, `--apply`, `--confirm`, `--yes` or `-f`/`--force`.
- `--yes` only answers a confirmation prompt in advance and never causes a write by itself. A typed confirmation before a destructive change is still asked after `--no-dry-run`.
- `--check` is a dry run that exits 1 when anything would change, for hooks and continuous integration; it never writes.
- An option that chooses what to change, such as `--rollback <log>`, `--clone` or `--delete`, is previewed like any other change until `--no-dry-run` is given.
- A dry run ends with one line saying nothing changed and naming `--no-dry-run`, and exits 0 when the preview succeeded.
- `--force`: [FORCE answer].
- Scope: [SCOPE answer].
- MCP tools follow the same rule through a `dry_run` argument defaulting to true, under ki-repo-mcp. Flags of third-party tools keep their own meaning, including where a KI tool passes them through.
```

## Queries

### FORCE - What `--force` should mean once it no longer switches writing on

**Context:** DRY-RUN-FLAGS settles that `--force` and `-f` never switch writing on, and leaves open whether `--force` keeps any meaning. The existing KI command-line guidance already gives `-f`/`--force` one meaning: override a refusal or safety check, such as a dirty working tree or an existing file, as `rm -f` and `git push -f` do. The tools use it that way today: `mgit worktree remove -f` discards changes in a dirty linked worktree. Other overrides already have specific names: `ki skill add --replace` (re-point an existing link), `techne host rebuild --discard <repository>` (allow losing a repository's unpushed work), `techne host stop --now` (skip a safety read) and `ki estate converge --allow-busy`. Kris's objection, as relayed, was to `-f` being used to make a command write. This recommendation has not been through a blind review.

**Query:** Should `--force` remain in KI tools, and if so with what meaning?

**Options:**

a) (recommended, confidence medium - it matches the existing guidance, Git and mgit's current use, and only removes the meaning Kris objected to; not yet blind-reviewed) Keep `--force`, short `-f`, only as "override a refusal or safety check". It never writes on its own: without `--no-dry-run` a forced command still only previews, showing what the override would allow. Prefer a specific name, such as `--replace` or `--discard`, where the override is about one thing; use `--force` only for a general override.

b) Retire `--force` and `-f` from KI tools altogether: every override gets its own specific name, and `-f` is never used.

c) Leave `--force` to each tool to define, so long as it never switches writing on.

### SCOPE - Which commands must dry-run by default

**Context:** DRY-RUN-FLAGS says "any command that changes something dry-runs by default", while the relayed message says it is to be rolled out "where they have dry runs". The survey shows the difference is large. About 20 commands already preview or have a `--dry-run` and convert cleanly. About 40 more change things with no preview at all because their name is the change itself: `ki agent launch`, `ki repo init`, `ki harness install`, `ki agent send`, `techne host start`, `mgit sync`. Read literally, every one of these, and every brief, script and coordinator step that calls them, would need `--no-dry-run` added. `rig apply` and `rig upgrade` sit between: they reconcile the machine against declared state, like a repair, so they fall in scope either way. This recommendation has not been through a blind review.

**Query:** Should the dry-run default apply to every command that changes anything, or only to commands that work out a set of changes from current state?

**Options:**

a) (recommended, confidence medium - it covers every command where a preview tells you something you did not already ask for, including `rig apply`, without adding `--no-dry-run` to every agent launch and install; not yet blind-reviewed) Apply it to commands that compute what to change from current state: repair, conform, converge, sync-style reconcile, apply, upgrade, migrate, prune, sweep, register, receive or release in batches, and bulk delete. A command whose name is one explicit action the caller asked for (launch, queue, send, init, install, start, stop, commit) acts by default and keeps `--dry-run` as an opt-in preview where it has one.

b) Apply it literally to every command that changes anything, including launch, init, install and send, so the rule has no exceptions.

### 🤖 → 👤 Handoff to supervisor · since 02:04 GMT

👤 2 with you

- [with you] FORCE · owner · since 02:04
- [with you] SCOPE · owner · since 02:04

🧵 ki.prj.ways-of-working
