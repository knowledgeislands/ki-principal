# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › managed-coverage-audit

**🤖 → 👤 Handoff to supervisor · Run report at 09:06 BST · last mark 18:57 BST**

---

## Done

Completed the two-way, read-only coverage audit requested in Decision 94; no chezmoi source, live configuration, application, credential, scheduler, service or completion changes occurred.

Confirmed prior apply-owned-drift is DONE: its report records four approved targets matching rendered sources, the renamed user skill links repaired, and KI doctor at 17 passing checks with no warnings or failures; its report and protected before/after evidence remain untouched.

Confirmed current source Git is clean; native status contains only the previously separated app-owned `~/.codex/config.toml` drift. This audit did not render or print that configuration or reopen its project-trust choice.

Updated only [the owned work-file next step](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md), preserving mark `2026-10-18T17:57:57Z`, all Messages, migration holds, decisions, reports and unrelated work.

Committed `df40b08c4cd32c9854efe6c1a8c4f80370b6c5e7` (`docs(work): record managed coverage audit proposal`), inspected its sole actual path, fetched and inspected every unpublished ancestor, and pushed this owned documentation commit fast-forward to origin/main.

Native matcher verification passed using installed chezmoi v2.73.2, empty configuration and content-free fixtures outside repositories: all 213 existing managed leaf paths remain included; five selected mGit templates become included; a hypothetical additional template and sibling runtime file remain excluded.

The chezmoi dotfiles audit has zero failures and one existing authoring warning: `.rumdl.toml` differs from the house template; changing that file is outside this read-only scope.

The Principal knowledge-base audit has zero failures and six existing warnings: three Project close-out assessments and three roadmap size fields; the hook's staged-path gate passes for the one owned work-file path.

Work-file and report Markdown checks pass with the repository configuration; work-file whitespace and the commit's normal formatting and commit-message hooks pass without bypass.

No source commit was made, so the source repository's implementation gate and application verification were not represented as having run.

### Method and boundaries

Read repository AGENTS.md and CLAUDE.md, `ki-repo-dotfiles-chezmoi` and its ignore-negation standard, `ki-authoring`, the runtime-mutated configuration guide, current work-file Messages and decisions, roadmap, source Git and native status. The roadmap's existing work remains out of scope.

Used `chezmoi managed --path-style all --include files,symlinks` for the 213 declared leaf mappings, `chezmoi ignored` for excluded source entries, and `chezmoi unmanaged` only on named bounded roots and leaves. Shallow directory inventories were limited to 25-60 names per selected root; no cloud store, Library subtree, cache content or live repository contents were crawled for configuration. A preliminary filename discovery crossed the territory's repository trees; that was broader than necessary, was stopped after its first bounded output, and was not used as coverage evidence. The substantive configuration audit used the bounded locations below.

File-shape checks reported key names, types, counts and portability predicates, never configuration values. Authentication/session files, private-key contents and credential values were not inspected. `mgit learn --list` read only the learned-template inventory; no Git command was dispatched through mGit.

Classification below means effective inclusion in chezmoi's normal source/inventory traversal. An explicit `chezmoi unmanaged ~/.config/gh/config.yml` or mGit leaf can list that path even though its excluded parent hides it from the normal `~/.config` inventory; such output alone does not prove that a future source would be included.

Proved matching with content-free fixture files and the exact current `.chezmoiignore` bytes using the installed binary, then with the proposed appended rules. No fnmatch approximation was used. Ignore line references below refer to the unchanged [current source](/Users/krisbrown/.local/share/chezmoi/.chezmoiignore).

### Unmanaged machine/runtime state to ignore

The following verified paths have no declared source and no effective ignore rule. Add the exact home-relative rules shown to `.chezmoiignore`; they filter inventory only and do not secure, delete or modify these files.

- `~/.aws/credentials` and `~/.aws/cli/cache/`: credential store and CLI cache. Current line 35 excludes only `.aws/sso`, leaving these visible. Proposed rules `.aws/credentials` and `.aws/cli/cache`; preserve managed `dot_aws/private_config`.
- `~/.ssh/kris@kris.me.uk` and `~/.ssh/config.pre-ue088`: local key material by filename and a pre-change backup. Current line 175 excludes only `.ssh/known_hosts.old`; neither candidate is managed. Proposed exact rules `.ssh/kris@kris.me.uk` and `.ssh/config.pre-ue088`; preserve both managed SSH files. No SSH configuration or connectivity change is proposed.
- `~/.claude-swap-backup/`: retired swap-tool recovery state, containing credential/configuration backups, locks and logs by filename. No matching rule; `.claude` rules at lines 49-82 do not cover this separate root. Proposed `.claude-swap-backup`; retain the backup locally.
- `~/.hermes/.env`, `~/.hermes/auth.json` and `~/.hermes/auth.lock`: environment/authentication material and lock by filename, currently unmanaged with no matching rule. Proposed those three exact rules; do not hide the whole mixed `.hermes` root.
- `~/.CFUserTextEncoding`: machine-local macOS encoding marker, currently unmanaged with no rule. Proposed `.CFUserTextEncoding`.
- `~/.adobe/`: local application digest state (`md5` child), currently unmanaged with no rule. Proposed `.adobe`.
- `~/.dgranted/log/`: tool logs, currently unmanaged; line 138 `.granted` is a different root. Proposed `.dgranted/log`, leaving any future declarative sibling visible.
- `~/.templateengine/`: .NET template-engine package/runtime state (`dotnetcli`, `packages`), currently unmanaged with no rule. Proposed `.templateengine`.
- `~/.turbo/`: daemon/cookie runtime state by filename, currently unmanaged with no rule. Proposed `.turbo`.
- `~/.wakatime/`: downloaded architecture-specific CLI binaries, currently unmanaged with no rule. Proposed `.wakatime`.
- `~/.ts_node_repl_history`: interpreter history, currently unmanaged; line 162 covers the separate `.node_repl_history`. Proposed `.ts_node_repl_history`.
- `~/.z.17224` and `~/.z.4110`: zero-byte temporary jump-history files, currently unmanaged; line 184 excludes only `.z`. Proposed `.z.[0-9]*`, retaining visibility for non-numeric siblings.

These are the 16 precise runtime/credential rules in the recommended scope. Further Hermes runtime state is visible (`cache`, `audio_cache`, `image_cache`, `logs`, `sessions`, `state`, databases and model caches); it is a verified mixed-root gap, but a wholesale `.hermes` ignore would also hide personal guidance and future configuration. Defer its broader split until the owner confirms that tool's intended use.

### Useful ignored configuration to manage

**Verified adoption proposal: `~/.config/mgit/templates/`.** All five existing files are excluded by line 92 `.config/*`; no mGit re-inclusion exists. No mGit template source currently exists. The native XDG unmanaged inventory omits the directory; content-free source fixtures also exclude its five files under the current rules.

The MGIT-CONFIG Message requests four learned files, while the live inventory and `mgit learn --list` now contain five: `branch.template`, `status.template`, `status_-sb.template`, `status_--short_--branch.template`, and the additional `pull.template`. The extra file needs inclusion in the owner's implementation decision rather than silently treating the old handoff as authority for it.

Proposed exact sources are `dot_config/mgit/templates/branch.template`, `dot_config/mgit/templates/status.template`, `dot_config/mgit/templates/status_-sb.template`, `dot_config/mgit/templates/status_--short_--branch.template`, and `dot_config/mgit/templates/pull.template`. Keep the `.template` suffix as plain files, not `.tmpl`; no chezmoi templating, secret lookup, generated completion or `.chezmoiremove` entry is needed.

Schema/portability checks: local mGit 0.17.0 reads `stdout:` and `stderr:` records as literal normalized expected output, with one `command:` row and generated comment rows; there is no explicit schema-version field. All five conform, have zero stderr rows, and contain only ASCII output with no home paths, URLs or credential markers. The branch template has one stdout row, full status four, and each other template one. Output placeholders are drawn only from `{branch}` and `{upstream}`; the header documents the six supported placeholders. Local reader/writer evidence is `tools-mgit/bin/mgit` at lines 3525-3573, 3575-3610 and 3710-3722.

These files express which successful Git output counts as quiet, so they are durable user preferences despite being learned by the app. They suppress matching successful output only; `pull.template` does not run a pull by being installed. Exact Git wording, locale and installed Git/mGit versions can affect matching on Terra or Sol: mismatches stay visible, and cross-host validation remains pending. A later `mgit learn` can rewrite them, so future changes require a deliberate reverse adoption and review rather than a blind whole-config re-add.

**Preference candidate: `~/.config/gh/config.yml`.** Also excluded by line 92. It contains a GitHub CLI preference/alias key shape, including protocol, editor, pager, browser, colour, prompting and alias fields. Values were not printed; `hosts.yml` was not read. If Kris wants those preferences shared, the candidate source is `dot_config/gh/private_config.yml`, with `!.config/gh`, `.config/gh/*`, then `!.config/gh/config.yml`; keep `~/.config/gh/hosts.yml` ignored. This is outside the recommended initial implementation scope because tool preferences and portable values need owner review.

Other bounded XDG checks found no additional verified declarative file to adopt: `~/.config/zed/themes` and `~/.config/codexbar/providers` are empty; `~/.config/iterm2/AppSupport` mixes runtime binaries, sockets, saved state, dynamic profiles and scripts, with no particular portable leaf established. Do not un-ignore these roots speculatively.

### Existing source paths incorrectly excluded

No unintended exclusion was verified among the 213 current managed leaf mappings or the native excluded-source list. Existing `.warp` files, `.paperclip/runtime/mise.toml`, XDG declarations and fragment-owned client configurations remain included.

`Library/Application Support/Code/User/mcp/github/README.md` is an existing ignored source under line 267 `Library/Application Support/Code/User/mcp/github/*`; line 268 re-includes only `manifest.json`. This matches the explanatory comment at lines 256-257: package documentation stays mutable application state. Retain the exclusion; it is not a missing configuration source.

The other native excluded-source entries are repository documents, `config-fragments`, `docs`, `scripts`, `tests` and `+`/`-` working areas, intentionally excluded by lines 4-18. No restoration is proposed.

The current ignore file has no platform-template branch; this inventory is from the actual macOS host. Managed `.tmpl` and `modify_` mappings were counted without rendering their values. No claim is made that the 213-path inventory substitutes for Linux, Windows, Terra or Sol verification, or that a host-dependent source not selected here is defective.

### Intentionally ignored state to retain

- `~/.config/gh/hosts.yml`, `~/.config/op/`, `~/.config/op-cache/`, `~/.config/.wrangler/`, `~/.config/configstore/`, `~/.config/yarn/` and `~/.config/iterm2/`: line 92 excludes these credential, notifier, package-manager and application-runtime roots. Preserve that boundary, with only separately reviewed declarative leaves eligible for adoption.
- `~/.codex/*`: line 85 excludes runtime state; lines 86-88 re-include only declared guidance, config and hooks. Carry current `~/.codex/config.toml` native MM drift separately under the existing fragment-binding guide; do not ignore or re-add it to make status look clean.
- `~/.claude/` runtime/authentication/history/plugin/session content: lines 49-80, with explicit fragment re-inclusions at 81-82. Preserve shared ownership of settings and the managed guidance; the separate backup root above is the gap.
- `~/.config/paperclip/` runtime siblings: line 104, with desired state and repairs re-included at 105-106. `~/.paperclip/runtime/mise.toml` is already managed; do not blanket-ignore `.paperclip` or resume Paperclip work.
- `~/.config/techne/hosts/` undeclared siblings: line 118, with `agent-host.toml` restored at 119; keep local host bindings outside adoption.
- `~/.config/zed/prompts/` and empty themes: line 124, with guidance/settings restored at 125-126; retain the manual reverse-merge rule for app-written settings.
- `~/.config/homebrew/trust.json` and `.lock`, and `~/.config/chezmoi/chezmoistate.boltdb`: lines 234-236. A parent-only unmanaged directory entry here is not evidence that its state should be added.
- `~/.cargo/**`, `~/.rustup/**`, `~/.local/*` and Library contents: lines 45, 174, 146-150 and 252-278 preserve runtime/platform boundaries. Keep known declarations and Rig materialisation as currently owned; no wider application or service adoption is proposed.

Visible mixed roots also need owner preferences rather than blanket ignores: `~/.pi/agent/settings.json` is unmanaged and not ignored, with only model/provider/thinking/theme key types established; `~/.hermes/SOUL.md` is possible personal guidance; `~/.docker/config.json` may mix preferences and credentials and was not read. Keep these visible and outside the initial scope. Possible later sources are `dot_pi/agent/private_settings.json` and `dot_hermes/SOUL.md` only after explicit tool-usage and value review; do not propose a raw Docker credential-bearing source.

## In Progress

Nothing running; temporary fixtures and their state are removed, the runtime temporary directory is empty, and no Git locks remain. Both repositories are level with their recorded origin/main; native drift remains only app-owned Codex config. The audit is complete and implementation awaits the COVERAGE-SCOPE decision below. No record was marked, accepted, pruned or resumed.

The proposed implementation envelope is exactly `.chezmoiignore` plus the five named `dot_config/mgit/templates/*.template` source files; the 16 new runtime rules above and the nine mGit traversal/allowlist rules below are the complete proposed ignore change. It is not yet an agreed implementation scope.

Append the mGit block after line 110, preserving other application boundaries: first `!.config/mgit`, then `.config/mgit/*`, then `!.config/mgit/templates`, then `.config/mgit/templates/*`, followed by one `!` rule for each of the five exact target files above. This admits neither future mGit runtime siblings nor unreviewed future templates. Append the 16 runtime rules in their corresponding commented sections without restructuring unrelated rules.

The shared skill describes negation through broadly ignored parents without intermediate re-inclusions. The installed binary's exact `.config/*` fixture excluded `status.template` when only `!.config/mgit/templates/status.template` was appended, but included it with the explicit parent block. This report therefore follows the observed matcher for this concrete case; the general skill wording was not used as proof and was not changed.

After scope approval, add only the five named files, never the entire `.config/mgit` directory recursively. Review their source diff and the narrow ignore diff; rerun the native matcher assertions and verify all current managed leaf paths still resolve. Run the source repository's complete required gate before committing any implementation.

For the subsequent target-review gate, propose `chezmoi diff --exclude=scripts` with the five exact absolute template file paths as arguments, plus a byte comparison of each `chezmoi cat <exact target>` result against its live file without printing content. On this host the newly adopted files should already match and target diff may be empty; source/ignore review remains necessary. Do not render the whole home or include app-owned Codex drift.

Only after Kris reviews that bounded diff and explicitly authorises application, run `chezmoi apply --exclude=scripts` with exactly those five file arguments. Then verify byte equality, the five `chezmoi managed` mappings, unchanged `mgit learn --list`, absence of a bounded template diff, and native status still showing only the separately owned Codex drift. Use `mgit learn --list` for verification; do not execute `mgit pull`, `mgit learn`, estate-wide Git dispatch or a completion generator. On other hosts the same reviewed five-file apply needs a pre-apply existence/backup check and the installed mGit reader version; no cross-host apply is authorised here.

The old MGIT-ZSH-COMPLETION Message remains intact for its separately scoped work; this proposal deliberately does not regenerate or adopt that snapshot.

The pre-commit pull attempt was refused because unrelated work was unstaged; no stash, reset or rebase occurred. Fetch and explicit ancestry/path checks established a level origin before the owned commit and only that one owned commit before the fast-forward push.

Existing audit warnings remain outside this scope: Principal close-out assessments for chezmoi, mac-studio-setup and paperclip-capture-and-rebuild; missing size on KI-PRINCIPAL-ECO-013, KI-PRINCIPAL-MOD-008 and KI-PRINCIPAL-MOD-009; and the chezmoi authoring-config drift named above. No wider clean-gate claim is made.

## Queries

### COVERAGE-SCOPE - agree the bounded implementation

**Context:** Five portable mGit learned-output preference files are hidden by the XDG ignore rule; the handoff names four and the current fifth is `pull.template`. Sixteen precise inventory rules can hide verified local runtime/credential paths without concealing mixed personal configuration roots. Matcher fixtures preserve all 213 existing managed leaves and exclude future unreviewed mGit files. Source and live configuration remain untouched.

**Query:** Should the next run implement the exact `.chezmoiignore` and five-template source scope above, then present its bounded target diff and application verification for review?

**Options:**

a) (recommended, confidence high - native matching and file portability were checked directly, and the scope is reversible) adopt all five mGit files, including `pull.template`, and the 16 precise runtime ignore rules; retain the listed intentional exclusions, leave preference candidates for later, and stop before apply for diff review.

b) Adopt only the four mGit files in the original MGIT-CONFIG handoff, leaving `pull.template` and the runtime-ignore changes pending; use the same exact-file traversal boundary and review gate.

c) Keep this as an audit proposal and make no source changes; optionally name which GitHub CLI, Pi or Hermes preferences should receive a separate focused review.

### 🤖 → 👤 Handoff to supervisor · since 09:06 BST

👤 1 new query · 🤖 0 running · ⏳ 0 queued

- [verified] Bounded two-way coverage audit and matcher proof complete · managed-coverage-audit · since 09:06 BST
- [published] Owned work-file next step committed and pushed; mark retained · managed-coverage-audit · since 09:06 BST
- [awaiting decision] COVERAGE-SCOPE: exact mGit adoption and runtime ignores · Kris · since 09:06 BST
