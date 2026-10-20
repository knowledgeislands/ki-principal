# ki.tools-burndown queries

## Open

### CANCEL-MERGE-BURNKI

since 2026-10-20 · burnki.report.md in run state folder · at qreview10 **Context:** CAPTURE-GATE allowed no new records, so these candidates are listed without action. [KI-TOOL-KI-CLI-160](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-160-work-status-routing-view.md)'s routing view and [KI-TOOL-KI-CLI-149](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-149-work-status-views-contract.md)'s views contract both reshape `ki work status` output. [KI-TOOL-KI-CLI-140](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-140-git-hygiene-estate-audit.md) has waited at Next on the ki-git rubric dependency, and since ESTATE-HOME a) it only reads mgit's JSON. [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-125-ki-release-contract.md) is on hold with no ARM host planned. The `ki work message` and `ki work prune` scope left KI-TOOL-KI-CLI-152, with its findings recorded in that record's Discussion.

**Query:** Which of these should a later run act on?

**Options:** a) (recommended, confidence medium - each follows from the records' own Discussion, but merging and cancelling are the owner's call) merge KI-TOOL-KI-CLI-160 into KI-TOOL-KI-CLI-149, return KI-TOOL-KI-CLI-140 to an idea, treat KI-TOOL-KI-CLI-125 as an idea candidate at its hold review, and capture a new record for `ki work message` and `ki work prune`; b) capture the message and prune record only and leave the rest; c) leave everything as it is.

### HOOK-LOCAL

since 2026-10-20 · burnki.report.md in run state folder · at qreview10 **Context:** KI-TOOL-KI-CLI-165 composes committed hooks from shape-skill claims. ki-principal and ki-agentic-harness carry repository-specific lines that no shape skill would claim, such as staged-skill functions. Nothing can be built before [KI-HARNESS-GOV-225](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-225-hook-content-claims.md) settles the claim shape.

**Query:** How should a repository's own hook lines be kept?

**Options:** a) (recommended, confidence medium - keeps composition deterministic without forcing a claim for every local line) a marked local block that the host preserves verbatim after the claimed lines; b) a repository-level claim in `.ki.toml`; c) refuse to write until a skill claims each line.

### CLI-OUTPUT

since 2026-10-20 · burnki.report.md in run state folder · at qreview10 **Context:** [KI-TOOL-KI-CLI-151](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-151-cli-conventions-departures.md) has two open choices. AGENTS.md forbids compatibility paths without authority. In this repository, the only consumer of `ki repo audit` output is the CI workflow, which reads only the exit code; no committed hook reads the output. Consumers in other repositories are unchecked.

**Query:** Should `--format <text|json>` give way to `--json`, and may audit and conform progress move to standard error?

**Options:** a) (recommended, confidence medium - meets the conventions with no alias, but consumers in other repositories are unchecked) replace `--format` with `--json` outright and move progress to standard error; b) add `--json` beside `--format` as a documented house form; c) keep `--format` and record it as a departure.

### SRC-PLACEMENT

since 2026-10-20 · burnki.report.md in run state folder · at qreview10 **Context:** [KI-TOOL-KI-CLI-139](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-139-ebu-sources-sync.md) mirrors EBU SharePoint documents into a store copy. That is not a Knowledge Exchange Package import, yet ADR-KI-TOOL-KI-004 keeps acquisition inside `ki`, with adapters discovered from Harness skill metadata. Either route needs a specification change first.

**Query:** Where should the SharePoint mirror command sit?

**Options:** a) (recommended, confidence low - reuses adapter discovery, but stretches what acquisition means) a new `ki acquire` adapter with a matching Harness skill; b) a separate command group with its own specification.

### VALIDATOR-HOME

since 2026-10-20 · burnki.report.md in run state folder · at qreview10 **Context:** [KI-TOOL-KI-CLI-157](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-157-validator-parity.md) needs one field rule table that both `ki` and the harness roadmap checker read.

**Query:** Where should the table live, and how should tools-ki take it?

**Options:** a) (recommended, confidence medium - the harness owns the wording, and the sharing preference favours a vendored copy) in ki-agentic-harness beside the checker, vendored into tools-ki under a drift check; b) a KI Specifications contract that both consume.

### CI-EVIDENCE

since 2026-10-20 · burnki.report.md in run state folder · at qreview10 **Context:** [KI-TOOL-KI-CLI-156](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-156-ci-runs-local-gate.md) starts by reading the latest CI runs to find out why the audit gate let the Biome drift through. This run could make no network call.

**Query:** Can a connected session read the CI evidence?

**Options:** a) (recommended, confidence high - the record cannot be planned without the evidence) a connected session reads the latest runs and plans the record from them; b) assume the audit gate is broken and plan the fix without the evidence.

### CANCEL-MERGE-ACCEPTKI

since 2026-10-20 · acceptki.report.md in run state folder · at qreview10

**Context**: I read all 18 open records in tools-ki and tools-mgit. Three are candidates; the rest have a live purpose and stay as they are.

**Query**: Which course should each candidate take?

**Options**: a) (recommended, confidence medium - the overlaps are on the surface; neither record is planned yet) Take the course recommended for each candidate below. b) Keep all three as they stand.

1. Merge [KI-TOOL-KI-CLI-160](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-160-work-status-routing-view.md) into [KI-TOOL-KI-CLI-149](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-149-work-status-views-contract.md). Both add views to `ki work status`, and the routing view belongs in 149's new `ki/work-status/v2` schema. Recommended: plan them as one record, with 160's routing view folded into 149 and 160 cancelled as merged.
2. [KI-TOOL-KI-CLI-140](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-140-git-hygiene-estate-audit.md) is an idea candidate. It is a large estate-wide Git-hygiene rubric, and it overlaps AUDIT-CONFORMANCE, which State of play now holds as the estate conformance audit. Recommended: cancel it as an idea, carried by AUDIT-CONFORMANCE.
3. [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-125-ki-release-contract.md) is an idea candidate. It is on Hold until an ARM host is needed or vega is rebuilt, and neither is in prospect. Recommended: at its 16 November review, cancel it as an idea in the Project note unless an ARM host has come up.

### YORK-COMMITMSG - apps-yorkphotosoc.org has Commitlint but no configuration

since 2026-10-20 · estfix.report.md in run state folder · at qreview10

**Context:** The Husky setup had only a pre-commit, and the repository has no Commitlint configuration. A `commit-msg` hook would therefore reject every message, so HOOK-3 still warns.

**Query:** Should apps-yorkphotosoc.org get a Commitlint configuration and a `commit-msg` hook?

**Options:**

a) (recommended, confidence medium - the packages are installed, so this needs no network and closes HOOK-3) Add a `commitlint.config` that extends `@commitlint/config-conventional`, plus a framed `.githooks/commit-msg`.

b) Leave the warning until KI-TOOL-KI-CLI-161 ships `ki git check-message`.

### WORKTREE-GATE - Staged audit refuses commits in unregistered worktrees

since 2026-10-20 · estfix.report.md in run state folder · at qreview10

**Context:** REPO-REG-1 is not tied to a path, so `--staged` cannot scope it out. It fails in any worktree that is not registered. This affects every Knowledge Base and project gate that runs `ki repo audit --staged`.

**Query:** Should the staged verdict exclude checks that are local to the machine?

**Options:**

a) (recommended, confidence medium - the hook comment already says machine-local checks are left to the full audit) Raise a tools-ki follow-up so that `--staged` excludes REPO-REG-1 and runtime activation from its verdict.

b) Accept it: commit only from the primary checkout.

### KI-DESIGN-REFUSAL - ki-design conform blocked by GitHub settings

since 2026-10-20 · estmig-ki.report.md in run state folder · at qreview10

**Context:** Conform applies its writes only after the whole initial audit passes. ki-design fails that audit on live GitHub repository settings: an empty description, merge methods, Issues and Projects toggles, topics, Dependabot and secret scanning. These are unrelated to hooks, so Husky stays.

**Query:** How should ki-design leave Husky?

**Options:**

a) (recommended, confidence medium - it fixes the real drift and lets conform run unchanged, but needs a GitHub settings grant) Authorise a run to apply ki-design's GitHub settings, then convert it as the others were.

b) Convert ki-design's hooks by hand now, and leave the GitHub settings for later.

### PKGLESS-GATE - What the package-less repositories' hooks run

since 2026-10-20 · estmig-ki.report.md in run state folder · at qreview10

**Context:** For homebrew-tap and ki-specifications I wrote a `pre-commit` running the shape skill's staged audit, plus the Ruby tests in homebrew-tap. This is the same choice estmig-org put to Kris as NO-GATE a), for a skill that declares no gate. tools-mgit and tools-rig follow SHELL-HOOK. Their hooks run the full bats suite on every commit, which is slow.

**Query:** Should the shape-skill audit stand as the gate for package-less project repositories, decided together with NO-GATE?

**Options:**

a) (recommended, confidence medium - it gives every hook a real check-only command and one answer for both runs) Take NO-GATE a) for both runs, and have the harness record the shape-skill staged audit as the project-shape gate.

b) Strip homebrew-tap and ki-specifications back to whatever NO-GATE decides.

## Parked

### ASK-B - Coarse acquisition kind in the public export

since 2026-10-19 · from rigsite-config.report.md in the run state folder · parked: ASK-B a), under HIGH-CONFIDENCE on 19 October; release: the rig.midnight.ninja side asks

**Context:** Ask B has no go-ahead. If it goes ahead, a `kind` or `form` field derived as application or command-line would get past the site's forbidden-field check. Platform variants complicate it, because one tool can install differently on macOS and Linux. It would widen the public export (RIG-PUB-002).

**Query:** Keep Ask B parked?

**Options:**

a) (recommended, confidence high - there is no go-ahead, and it widens the public boundary) Keep it parked and raise it only when Kit asks.

b) Capture it at triage now, marked as waiting for Kit's go-ahead.
