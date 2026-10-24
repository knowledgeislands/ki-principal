VERDICT: inconsistent · confidence high - Defaults and preview flags differ across tools; the current written repair rule also conflicts with write-by-default.

# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-dryrun-survey

**🤖 → 👤 Handoff to supervisor · Run report at 01:04 BST · last mark 02:10 BST**

---

## Done

Read-only survey completed; no repository edits or commits. Help check: all 114 `ki` leaf commands, 32 other command routes and 10 safe installer/harness entry points returned success. Source check: command parsers, execution branches, manifests and conventions inspected; no mutating operation, test suite or remote call executed.

Defaults below assume valid required operands and existing safeguards. **W** writes/acts; **P** previews; **V** verifies and exits non-zero on drift; **R** reads/prints. `none` means no preview or opt-in write flag. Authority, overwrite and target-selection flags are not preview switches. Each command has its own row; conditional modes stay in that row. `mgit repair` is deliberately recorded as the requested imminent behaviour, although the inspected checkout still advertises `--apply`.

### Command inventory

| Command | Default | Preview / verification | Opt-in write | `-n` |
| --- | --- | --- | --- | --- |
| `ki acquire import` | W | `--dry-run` | none | no |
| `ki acquire images` | W | `--dry-run` | none | no |
| `ki acquire mark` | P | none | `--confirm` | no |
| `ki agent launch` | W | `--dry-run` | none | no |
| `ki agent queue` | W | `--dry-run` | none | no |
| `ki agent dispatch` | W | none | none | no |
| `ki agent stop` | W | none | none | no |
| `ki agent dequeue` | W | none | none | no |
| `ki agent recover resolve` | W | none | none | no |
| `ki agent status` | R; W with run† | none | none | no |
| `ki agent send` | W | none | none | no |
| `ki agent watch` | W† | none | none | no |
| `ki agent wait` | W† | none | none | no |
| `ki agent new` | W | none | none | no |
| `ki agent home` | R | none | `--work <id>` | no |
| `ki agent decide` | W | none | none | no |
| `ki agent reconcile` | W | none | none | no |
| `ki agent close` | W | none | none | no |
| `ki agent sweep` | P | none | `--write` | no |
| `ki bootstrap` | W | none | none | no |
| `ki territory open` | opens local target | none | none | no |
| `ki dev local set` | W | none | none | no |
| `ki dev local on` | W | none | none | no |
| `ki dev local off` | W | none | none | no |
| `ki dev skill generate` | V | none | `--write` | no |
| `ki dev skill rubric` | V | none | `--write` | no |
| `ki estate converge` | P‡ | none | `--apply` | no |
| `ki harness install` | W | none | none | no |
| `ki harness reinstall` | W | none | none | no |
| `ki harness uninstall` | W | none | none | no |
| `ki kb index` | W | none | none | no |
| `ki markdown gfm` | W, guarded§ | `--dry-run` | none | no |
| `ki registry add` | W | `--dry-run` | none | no |
| `ki registry remove` | W | `--dry-run` | none | no |
| `ki repo batch prepare` | W | none | `--approved` required | no |
| `ki repo batch run` | W | none | none | no |
| `ki repo batch close` | W | none | none | no |
| `ki repo trade standing capture` | W | none | none | no |
| `ki repo trade prepare` | W | none | none | no |
| `ki repo trade submit` | W | none | none | no |
| `ki repo trade abandon` | refuses without grant | none | `--yes` required | no |
| `ki repo trade receive` | W by ID; P `--all` | none | `--yes` for batch | no |
| `ki repo trade release` | W by ID; P `--eligible` | none | `--yes` for batch | no |
| `ki repo trade prune` | W by ID; P `--eligible` | none | `--yes` for batch | no |
| `ki repo open` | opens local target | none | none | no |
| `ki repo roadmap prune` | W, including commit | `--dry-run` | none | no |
| `ki repo roadmap promote` | W | none | none | no |
| `ki repo roadmap demote` | W | none | none | no |
| `ki repo roadmap migrate` | P | none | `--apply` | no |
| `ki repo store create` | P | none | `--write` | no |
| `ki repo store bind` | P | none | `--write` | no |
| `ki repo store unbind` | P | none | `--write` | no |
| `ki repo store absent` | P | none | `--write` | no |
| `ki repo repair` | W | `--dry-run` | none | no |
| `ki repo skill add` | W | none | none | no |
| `ki repo skill remove` | W | none | none | no |
| `ki repo upgrade` | W | none | none | no |
| `ki repo init` | W | none | none | no |
| `ki repo conform` | W | `--dry-run` | none | no |
| `ki skill add` | W | none | none | no |
| `ki skill remove` | W | none | none | no |
| `ki cleanup` | P only; no writer | none | none | no |
| `ki mcp install` | W | none | none | no |
| `ki mcp update` | W | none | none | no |
| `ki mcp rollback` | W | none | none | no |
| `ki mcp uninstall` | W | none | none | no |
| `ki repair` | P | `--dry-run` | `--apply` | no |
| `ki update` | W | none | none | no |
| `ki vscode sync` | V | none | `--write` | no |
| `tools-ki/install.sh` | W | none | none | no |
| `mgit register` | W | `--dry-run` | none | yes |
| `mgit register add` | W | `--dry-run` | none | yes |
| `mgit register rm` | W | `--dry-run` | none | yes |
| `mgit repair` (imminent) | W | `--dry-run` | none | yes |
| `mgit structure nested` | W | `--dry-run` | none | yes |
| `mgit structure standard` | W | `--dry-run` | none | yes |
| `mgit worktree add` | W | none | none | no |
| `mgit worktree remove` | W | none | none | no |
| `mgit sync` | W, fetch/pull/push | none | none | no |
| `mgit learn` / `--learn` | runs Git; prompts to save | none | interactive answer | no |
| `mgit learn --forget` | W | none | none | no |
| `mgit <git-command>` / `--raw` | Git-dependent | Git-dependent | Git-dependent | Git-dependent |
| `tools-mgit/install.sh` | W | none | none | no |
| `rig init` | W | `--dry-run` | none | yes |
| `rig repair` | P | none | `--output PATH`¶ | no |
| `rig capture` | P | `--dry-run` | `--output PATH`¶ | yes |
| `rig apply` | W | `--dry-run` | none | yes |
| `rig remove` | P | `--dry-run` | `--apply` | yes |
| `rig upgrade` | W | `--dry-run` | none | yes |
| `rig export` | W | none | `--output` required | no |
| `tools-rig/install.sh` | W | none | none | no |
| `techne auth login` | W, interactive | none | none | no |
| `techne controller bootstrap` | W, interactive session | none | none | no |
| `techne host add` | W, local binding only | none | none | no |
| `techne host setup` | W | `--dry-run` | none | no |
| `techne host start` | W | `--dry-run` | none | no |
| `techne host stop` | W | `--dry-run` | none | no |
| `techne host rebuild` | W, interactive guard | `--dry-run` | none | no |
| `techne host withdraw` | W, interactive guard | `--dry-run` | none | no |
| `techne host connect` | opens editor | `--dry-run` | none | no |
| `tools-techne/install.sh` | W | none | none | no |
| `git almanac calendar` | stdout; W with output | none | `--output`, `--output-dir` | no |
| `git almanac authors` | stdout; W with output | none | `--output` | no |
| `git almanac contributors` | stdout; W with output | none | `--output` | no |
| `git almanac report` | W | none | none | no |
| `git almanac config init` | W | none | none | no |
| `git almanac ignore` | W | none | none | no |
| `git almanac init` | W | none | none | no |
| `git almanac repair` | P | none | `--apply` | no |
| `tools-git-almanac/install.sh` | W | none | none | no |

† Agent observation is not wholly read-only: it records events/homes completed reports; `status <run>` also advances the inbox cursor, and `wait --next` advances `events.seen`. These are runtime bookkeeping, not apply operations.

‡ Includes move, `--hooks` and `--rollback` modes; all use the same `--apply` gate.

§ Bare invocation refuses. Apply requires a matching prior `--preview` and a new rollback `--manifest`; `--dry-run --preview FILE` intentionally writes the requested preview artifact.

¶ Rig writes a separate review proposal, never adopts it into active configuration. Capture prints the proposal when no output path is supplied.

Sources: [`ki` command factories](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/commands/root/index.ts:24), [agent observation](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:1286), [trade modes](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/commands/trade/records.ts:93), [mgit](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/bin/mgit:94), [Rig option inventory](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/00-runtime.bash:168), [Techné handlers](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/src/cli.ts:749), [Almanac parser](/Users/krisbrown/workspaces/knowledge-islands/tools-git-almanac/src/cli/parse.ts:173). Read-only checks and ordinary stdout commands are omitted unless needed to explain an output-writing variant.

### Harness and developer entry points

There is no current `ki-agentic-harness/scripts/` directory. Its executable helpers now live beneath the skills; hosted rubric/generator modules are invoked through `ki repo conform` / `ki dev skill`, already listed. Paths below are relative to the named repository. Native build, test and package-manager commands keep their own semantics; they are not aliases for an estate apply operation.

| Command | Default | Preview / verification | Opt-in write | `-n` |
| --- | --- | --- | --- | --- |
| Harness `bun run clean` | W, removes dependencies | none | none | no |
| Harness `bun run ki:deps:update` | W, package update | none | none | no |
| Harness `bun run prepare` | W, Git hook config | none | none | no |
| Harness `bun run ki:harness:eval` | W scratch; live models | none | none | no |
| Harness `bun run self:diagrams:html` | W | `--check` (V) | none | no |
| Harness `bun run test` | V; fixture writes | none | none | no |
| Harness `ki-diagrams/…/build-html.ts` | W | `--check` (V) | none | no |
| Harness `ki-diagrams/…/export-svg.ts` | W | none | none | no |
| Harness `ki-binding-chatgpt/…/render-codex.ts` | W | `--dry-run`, `--check` (V) | none | no |
| Harness `ki-repo-harness/…/skill-graph.ts` | V | `--check` | `--write` | no |
| Harness `ki-housekeeping-chatgpt/…/app-server.ts delete` | refuses without grant | inventory is separate | `--confirm` phrase | no |
| Harness `ki-repo/…/internal/remove-legacy-ki.ts` | W, deletes legacy output | none | none | no |
| Harness `hooks/plan-stamp.sh` | W, event-driven | none | none | no |
| Harness `hooks/plan-sync.sh` | W, event-driven | none | none | no |
| Harness `hooks/git-lock-check.sh` | W, guarded stale deletion | none | none | no |
| KI `scripts/generate-command-inventory.ts` | V | none | `--write` | no |
| KI `release/package.sh` | W | none | none | no |
| Rig `scripts/assemble-rig` | V; temp in repo | `--check` | `--write` | no |
| Rig `scripts/benchmark-rig` | scratch writes | none | none | no |
| Rig `scripts/smoke-native-providers` | scratch writes | none | none | no |
| Techné `release/package.sh` | W | none | none | no |
| KI `bun run build` | W | none | none | no |
| KI `bun run clean` | W | none | none | no |
| KI `bun run ki:deps:update` | W | none | none | no |
| KI `bun run prepare` | W | none | none | no |
| Techné `bun run build` | W | none | none | no |
| Techné `bun run clean` | W | none | none | no |
| Techné `bun run ki:deps:update` | W | none | none | no |
| Techné `bun run prepare` | W | none | none | no |
| Almanac `bun run build` | W | none | none | no |
| Almanac `bun run clean` | W | none | none | no |
| Almanac `bun run ki:deps:update` | W | none | none | no |
| Almanac `bun run prepare` | W | none | none | no |

Harness helper sources: [diagram build](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-diagrams/scripts/build-html.ts:283), [SVG export](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-diagrams/scripts/export-svg.ts:320), [Codex rendering](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/environment/ki-binding-chatgpt/scripts/render-codex.ts:56), [skill graph](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-harness/scripts/skill-graph.ts:24), [reviewed deletion](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/environment/ki-housekeeping-chatgpt/scripts/app-server.ts:315), [legacy cleanup](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-repo/scripts/internal/remove-legacy-ki.ts:7), [package scripts](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/package.json:1).

Help safety exceptions: lifecycle/native scripts were inspected rather than executed; several do not implement help. In particular `ki:harness:eval --help` would still run live models, legacy cleanup treats its first argument as a repository, and Rig assembly creates its repository-local temporary file before processing help. No such invocation was made. Native test/coverage/watch and release-test commands verify with fixture/report writes; they have no custom state-change preview contract.

### Outliers, grouped

- **Different defaults:** root `ki repair` previews while `ki repo repair` writes; migration, stores, sweep and trade batches require different write switches. Rig removal previews; repair/capture produce separate proposals. Almanac repair previews. The imminent mgit repair change aligns with register and structure.
- **Missing previews:** most installation, update, skill, batch, work-state and cleanup writers lack any dry-run route; mgit sync/worktrees/forget, Rig export, Almanac reports/init/ignore, several Techné commands and harness deletion/export helpers do too. No surveyed KI or Techné command offers `-n`; Rig's operational dry runs and the aligned mgit commands do.
- **Verification versus preview:** KI generated surfaces/rubrics, VS Code sync and skill-graph verify by default and require `--write`. Codex rendering aliases `--dry-run` to `--check`, returning 1 for planned differences. Diagram build's `--check` is a proper receipt verification mode, not a build preview. No custom `--plan` or `--fix` write gate was found on the surveyed public commands; native formatter flags are separate.
- **Side effects and special entry points:** GFM can explicitly save a preview artifact; agent observation writes bookkeeping. Native lifecycle scripts and event hooks do not follow a public apply/preview grammar. Terminal/stdout renderers selecting a file destination are output commands, not preview-first mutators.

### Existing written convention

The [harness command-line conventions](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-tools/references/standards-cli-conventions.md:42) already define `-n`, `--dry-run` as: “Report what would change without changing anything.” At [line 55](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-tools/references/standards-cli-conventions.md:55): “A command whose writes need review previews by default and writes only with an explicit option such as `--apply`”. The same paragraph says: “`--dry-run` remains the opt-in preview for a command that acts by default.”

The [tool-repository standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-tools/references/standards-tool-repositories.md:152) is more specific: “`repair` exists only when there is a specific owned recovery operation: its default is a non-mutating preview, and writing requires an explicit option such as `--apply` or a reviewed proposal output.” Thus the requested convention would change policy, not merely correct implementations. Searching all 23 Markdown files in [Engineering Practice](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Engineering Practice/Engineering Practice.md>) found no dry-run/default-write/`--check`/`--plan` rule.

### Proposed convention and smallest changes

**Proposed convention:** A command that changes owned state writes by default and accepts both `--dry-run` and `-n` to show the same selected changes without applying them; preview succeeds unless planning fails. Reserve `--check` for a read-only verification mode that exits non-zero when the required state is absent or differs. Do not use `--apply`, `--write` or `--fix` as routine write gates, and keep `--yes` for confirmation rather than preview selection. Preserve explicit destinations, reviewed proposals, authority checks and confirmations where deletion, external publication or connection-critical changes require them; document those bounded exceptions. Native forwarded commands and event hooks retain their native contracts.

- **tools-ki:** add `-n` to existing dry runs; add the same preview pair to writers that lack it. Flip routine repair, roadmap migration, store metadata and generation/sync routes to writing where their existing safety requirements permit; give existing drift verification explicit `--check`. Unify ID/batch preview selection for trades while preserving deletion/authority confirmation. Keep cleanup reporting-only unless an actual owned writer is separately intended. No new cleanup mechanism is needed.
- **tools-mgit:** count repair's requested change as done-in-flight, not a further recommendation. Add preview pairs to owned worktree, sync and template-removal operations; sync preview must not fetch or push. Preserve Git passthrough flags and interactive learning confirmation.
- **tools-rig:** add preview pairs to export and the installer. Keep repair/capture's explicit review-file destination and remove's confirmation exception; they cannot safely be converted into automatic adoption/uninstall merely to match the routine default. Assembly may expose explicit `--check` with generation defaulting to write; its check/help should not create a repository-local temporary file.
- **tools-techne:** add `-n` to the six existing dry-run handlers; add previews to local binding creation and installer, and document that login/bootstrap open interactive sessions. Keep host targeting, interactive removal and Harness authority guards. Existing dry runs may still query providers or ping the host; they are not an offline promise.
- **tools-git-almanac:** make repair write with the preview pair; add that pair to report/config-init/ignore/init, explicit file-output variants and installer. Preserve stdout defaults and explicit output destinations.
- **ki-agentic-harness:** change the two conflicting written rules first. Add preview pairs to diagram build/export, Codex rendering and internal legacy cleanup; separate Codex dry-run success from `--check` drift failure. Make skill-graph generation write by default with `--check` retained. Keep reviewed conversation deletion, event hooks, native package lifecycle and tests as explicit exceptions; make eval help return before any model call. Apply routine generator changes in tools-ki, not duplicated skill wrappers.

All public flag changes also need their existing help, completion, manual, documentation and focused contract checks updated together. The five tool installers currently have no preview mode; add the pair through their existing installer implementations, without introducing another mechanism.

### Unsafe defaults to preserve or guard

**Bulk or irreversible deletion:** `ki agent sweep/close`, trade abandon/release/prune, roadmap prune, `rig remove`, harness conversation deletion and legacy cleanup can remove uncommitted material, whole archived runs, installed dependencies or history. Roadmap prune already writes and commits by default, including broad selection without an ID; that existing default deserves particular care. Preserve scope/refusal checks and confirmations; do not silently turn a current batch preview into deletion.

**Machine or connection effects:** estate moves/rollback/hook binding can disrupt active checkouts or execute hooks; store bindings change which external files become authoritative and require the owner's review. `rig apply/upgrade` can restart applications, retire resources and alter firewall/service state. Techné setup/stop/rebuild/withdraw can change or destroy the connected host, and withdraw removes credentials. These already have some write defaults; flag consistency must not remove their authority, target, restore-path or interactive safeguards.

**External effects:** `mgit sync` already fetches and pushes by default, so no preview implementation may perform those actions. Auth/bootstrap commands change authentication or open privileged sessions; eval spends live model quota. Explicit invocation remains meaningful authorisation, and neither help nor preview should perform the live action. Rig repair/capture must continue writing review proposals rather than overwriting active configuration; stdout renderers must not invent file destinations.

## In Progress

None. This run surveyed and proposed changes only; implementation remains with the owning repositories.

## Queries

None.

### 🤖 → 👤 Handoff to supervisor · since 01:04 BST

👤 1 with you · 🤖 0 running · 🅿️ 0 parked

- [with you] Dry-run survey and proposed convention · supervisor · since 01:04 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
