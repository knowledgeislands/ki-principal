# [Foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Baseline rollout](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/baseline-rollout.md) › wave1-audit

**🤖 → 👤 Handoff to supervisor · Run report at 23:44 BST · last mark 23:27 BST**

---

## Done

- Humans Not Robots: `ki territory audit` healthy, 8 repositories, 0 findings. Three Git repositories on disk are neither declared by the Capital nor registered: [hnr-backend](/Users/krisbrown/workspaces/humans-not-robots/hnr-backend) (AWS CDK backend, no `.ki.toml`, no AGENTS.md), [hnr-frontend](/Users/krisbrown/workspaces/humans-not-robots/hnr-frontend) (AGENTS.md but no `.ki.toml`) and [hnr-benchmarks](/Users/krisbrown/workspaces/humans-not-robots/hnr-benchmarks) (no README, `.ki.toml` or AGENTS.md). All three are clean and committed to today.
- Legal: healthy, 2 repositories, 0 findings. The registry knows both repositories on disk.
- Personal: healthy, 8 repositories, 0 findings. `workspaces/personal/dotfiles` is a symlink to [chezmoi](/Users/krisbrown/.local/share/chezmoi), and the registry already knows that as `chezmoi`, so nothing needs registering.
- Equal Remedy: healthy, 3 repositories, 0 findings. The registry knows every repository on disk.
- Valle Armonia: healthy, 4 repositories, 0 findings. The registry knows every repository on disk.
- Techmedix: the audit failed (exit 2) before it reported any findings, because member `techmedix/apps-childhealthyorkshire.co.uk` is not registered. `ki territory show` fails the same way. The member is declared in [tmx-principal `.ki.toml`](/Users/krisbrown/workspaces/techmedix/tmx-principal/.ki.toml), and [Known Lands](</Users/krisbrown/workspaces/techmedix/tmx-principal/Admin/Governance/Known Lands.md>) lists it as archived read-only. It has no local clone. The other three members, [tmx-principal](/Users/krisbrown/workspaces/techmedix/tmx-principal), [tmx-agentic-harness](/Users/krisbrown/workspaces/techmedix/tmx-agentic-harness) and [apps-yorkphotosoc.org](/Users/krisbrown/workspaces/techmedix/apps-yorkphotosoc.org), are registered and on disk, and nothing is on disk that the Capital does not declare.
- `ki` versions: no repository pins a `ki` version in `.ki.toml`, `package.json`, mise or `.tool-versions`, so every repository uses the machine's `ki`. The first `ki` on PATH is `~/.local/bin/ki`, a Bun runner over the [tools-ki](/Users/krisbrown/workspaces/knowledge-islands/tools-ki) source, at 0.11.5. That matches the latest tag, v0.11.5, and the tap formula, which moved to v0.11.5 today. Homebrew's installed `/opt/homebrew/bin/ki` is still at 0.11.4, one release behind. I installed nothing.
- [KI-HARNESS-GOV-205](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-205-static-light-diagram-export.md) (static light diagram export, Project ways-of-working): triage, nothing blocking it, updated 19 October.
- [KI-HARNESS-GOV-221](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-221-ki-diagrams-mermaid-fence-warning.md) (ki-diagrams Mermaid fence warning, Project observatory): triage, captured 19 October.
- [KI-HARNESS-GOV-220](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-220-coord-1-undeclared-warn-level.md) (COORD-1 undeclared warn level, Project tools-burndown): triage, nothing blocking it, captured 19 October. The record observed the bug with `ki` 0.11.3 in er-principal. I did not re-run `ki repo audit` to check 0.11.5, because that is outside this run's authority.
- [hnr-shared](/Users/krisbrown/workspaces/humans-not-robots/hnr-shared): confirmed it has no AGENTS.md, `.ki.toml` or roadmap. It is clean, last committed 11 October, and unregistered. [HNR Known Lands](</Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Admin/Governance/Known Lands.md>) treats it as the linked content store, not an admitted island, and its changes go through hnr-principal. This is not a registration gap.
- I made no writes, commits or registrations in any repository and ran no `ki repo conform`.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- [hnr-principal](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal)'s remote `krisb/hnr-principal` is the renamed Capital, formerly `krisb/kit-hnr`. The earlier repository with that name was retired on 4 October. The registry, the declaration and the local remote all agree.
- Homebrew `ki` at 0.11.4 only matters where `~/.local/bin` is not first on PATH, such as launchd jobs or hooks with a minimal PATH.

## Queries

### TERRITORY-TECHMEDIX - Techmedix audit stops on an archived, unregistered member

**Context:** `ki territory audit -t techmedix` exits 2 because the Capital declares `techmedix/apps-childhealthyorkshire.co.uk`, which Known Lands calls archived read-only, and that repository has no local clone or registration. So the whole territory gets no audit at all. HNR's Known Lands states the territory principle that "Local unavailability does not remove an inventoried island", and this failure goes against it.

**Query:** How should the Techmedix audit be unblocked?

**Options:** a) (recommended, confidence medium - it keeps the declared inventory intact and follows the stated principle, but tools-ki owns the behaviour) Hand a record to tools-ki asking territory audit and show to report an unregistered declared member as a finding and carry on, rather than failing. Leave the declaration as it is. b) Clone the archived repository locally and register it, which needs a network fetch and a registration run. c) Take it out of `territory_members` in tmx-principal through its Enactment Process, keeping it in Known Lands as archived.

### REGISTER-HNR - Admit or exclude hnr-backend, hnr-frontend and hnr-benchmarks

**Context:** These three active, clean Git repositories under `workspaces/humans-not-robots/` belong to `humansnotrobots`. None is declared in hnr-principal's `territory_members` or Known Lands, none is registered, and none has a `.ki.toml`, although hnr-frontend has an AGENTS.md. hnr-principal's ADR Consolidation notes already cite hnr-backend as a source of evidence. The audit reports nothing about them because it checks only declared members.

**Query:** Should these three repositories become Humans Not Robots territory members?

**Options:** a) (recommended, confidence low - I have not checked their purpose or ownership beyond the READMEs) Admit them in a later wave: hnr-principal declares them in `territory_members` and Known Lands through its Enactment Process, each repository adopts a baseline `.ki.toml`, and then they are registered. b) Leave them outside the territory as product codebases with no KI governance, and record that exclusion in Known Lands, as was done for hnr-shared. c) Decide one repository at a time, for example admitting hnr-backend and hnr-frontend and leaving hnr-benchmarks out.

### KI-BREW - Homebrew ki is one release behind

**Context:** The first `ki` on PATH (the tools-ki source runner) is at the released 0.11.5, but Homebrew's installed `ki` is 0.11.4 even though the tap formula is already at v0.11.5. Any context that resolves `/opt/homebrew/bin/ki` first runs the older release.

**Query:** Should Homebrew's `ki` be upgraded to 0.11.5?

**Options:** a) (recommended, confidence high - this is a non-destructive upgrade to the released formula) Run `brew upgrade ki` as a separate authorised step. b) Leave it as it is, since the source runner comes first on PATH for interactive sessions.
