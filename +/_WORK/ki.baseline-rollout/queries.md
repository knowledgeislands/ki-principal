# ki.baseline-rollout queries

## Open

### TERRITORY-TECHMEDIX - Techmedix audit stops on an archived, unregistered member

since 2026-10-19 · from `wave1-audit` at 23:44 BST · in blind review

**Context:** `ki territory audit -t techmedix` exits 2 because the Capital declares `techmedix/apps-childhealthyorkshire.co.uk`, which Known Lands calls archived read-only, and that repository has no local clone or registration. So the whole territory gets no audit at all. HNR's Known Lands states the territory principle that "Local unavailability does not remove an inventoried island", and this failure goes against it.

**Query:** How should the Techmedix audit be unblocked?

**Options:** a) (recommended, confidence medium - it keeps the declared inventory intact and follows the stated principle, but tools-ki owns the behaviour) Hand a record to tools-ki asking territory audit and show to report an unregistered declared member as a finding and carry on, rather than failing. Leave the declaration as it is. b) Clone the archived repository locally and register it, which needs a network fetch and a registration run. c) Take it out of `territory_members` in tmx-principal through its Enactment Process, keeping it in Known Lands as archived.

### REGISTER-HNR - Admit or exclude hnr-backend, hnr-frontend and hnr-benchmarks

since 2026-10-19 · from `wave1-audit` at 23:44 BST · in blind review

**Context:** These three active, clean Git repositories under `workspaces/humans-not-robots/` belong to `humansnotrobots`. None is declared in hnr-principal's `territory_members` or Known Lands, none is registered, and none has a `.ki.toml`, although hnr-frontend has an AGENTS.md. hnr-principal's ADR Consolidation notes already cite hnr-backend as a source of evidence. The audit reports nothing about them because it checks only declared members.

**Query:** Should these three repositories become Humans Not Robots territory members?

**Options:** a) (recommended, confidence low - I have not checked their purpose or ownership beyond the READMEs) Admit them in a later wave: hnr-principal declares them in `territory_members` and Known Lands through its Enactment Process, each repository adopts a baseline `.ki.toml`, and then they are registered. b) Leave them outside the territory as product codebases with no KI governance, and record that exclusion in Known Lands, as was done for hnr-shared. c) Decide one repository at a time, for example admitting hnr-backend and hnr-frontend and leaving hnr-benchmarks out.

### KI-BREW - Homebrew ki is one release behind

since 2026-10-19 · from `wave1-audit` at 23:44 BST

**Context:** The first `ki` on PATH (the tools-ki source runner) is at the released 0.11.5, but Homebrew's installed `ki` is 0.11.4 even though the tap formula is already at v0.11.5. Any context that resolves `/opt/homebrew/bin/ki` first runs the older release.

**Query:** Should Homebrew's `ki` be upgraded to 0.11.5?

**Options:** a) (recommended, confidence high - this is a non-destructive upgrade to the released formula) Run `brew upgrade ki` as a separate authorised step. b) Leave it as it is, since the source runner comes first on PATH for interactive sessions.

## Parked

None.
