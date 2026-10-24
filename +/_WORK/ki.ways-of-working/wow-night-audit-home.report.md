# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-night-audit-home

**🤖 → 👤 Handoff to supervisor · Run report at 02:10 BST · last mark 01:40 BST**

---

## Done

Audit home: [`/Users/krisbrown/.local/state/ki/agents/ways-of-working/audit-home/`](/Users/krisbrown/.local/state/ki/agents/ways-of-working/audit-home/README.md). It holds a template `$HOME` seed: CI's empty runtime settings and MCP inventory, plus the canonical harness exported with `git archive` from local harness `main` at `f9a34b43`. It also holds a `sandbox-exec` profile that blocks network traffic. Nothing was downloaded.

README: names every variable to set (`HOME`, the four `XDG_*_HOME`, the four `KI_*_HOME`, `KI_MCP_SOURCE` and `GH_CONFIG_DIR`) and the tokens to unset. It makes each run copy `seed/` into its own temporary directory first: bootstrap writes absolute skill-link paths and registry state, so a shared or moved home would leak state between runs.

Proof: offline bootstrap succeeded and reported the harness "already installed", with no download. A throwaway Git repository with no worktree, made by `ki repo init`, was audited under the network block. The audit reached its verdict (31 of 60 criteria evaluated) with no REPO-REG-1 failure. Its only failures were the throwaway's own missing files and skill tables, and it left the target unchanged.

Re-run: running the README's command block word for word gave the same verdict.

Real registry: SHA-256 of `registry.toml`, `locals.toml`, `installation.toml`, `config.toml`, `~/.claude/settings.json` and the installed-harness listing matched before and after. The receipt is in [`wow-night-audit-home.proof.txt`](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-night-audit-home.proof.txt).

Limitation: the harness-only `ki dev local set` and `on` steps were not run, because doing so would have touched a real harness checkout.

Briefs edited in place: each brief's "already available offline isolated fixture home" now names the home and links its README, with no appended override.

- `wow-night-brg-006-accept.md`
- `wow-night-cli-140-plan.md`
- `wow-night-cli-156-accept.md`
- `wow-night-cli-156.md`
- `wow-night-harness-224-accept.md`
- `wow-night-harness-queue.md`
- `wow-night-observatory-queue.md`
- `wow-night-parked-queries.md`
- `wow-night-principal-queue.md`
- `wow-night-rig-048-accept.md`
- `wow-night-rig-048.md`
- `wow-night-rig-056-accept.md`
- `wow-night-rig-056.md`
- `wow-night-rig-067-accept.md`
- `wow-night-rig-067.md`
- `wow-night-tools-ki-queue-b.md`
- `wow-night-tools-ki-queue.md`
- `wow-night-tools-ki-release-candidate.md`
- `wow-night-tools-rig-release-candidate.md`
- `wow-night2-obs-vis-042-accept.md`
- `wow-night2-obs-vis-042.md`
- `wow-night2-techne-006-accept.md`
- `wow-night2-techne-006.md`

Brief added: `wow-night-observatory-queue-b.md`, which is the edited `wow-night-observatory-queue.md` with every launch-name use (heading, worktree, report and status paths, report heading) changed to `wow-night-observatory-queue-b`. A diff confirms nothing else differs.

Left as they were:

- `wow-night-rig-baseline.md` already names the home.
- The "isolated fixtures" in `wow-night-brg-006-accept.md` and `wow-night-rig-067.md` are test fixtures, not the audit home.
- The isolated-home workaround line in `wow-night-harness-queue.md` refers to the standard, not to this home.

Nothing was committed. The temporary directory is empty.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- `wow-night-observatory-queue-b` stops on its safety check unless `state.md` `## Writers` names it as the Observatory writer before launch.
- The first run's preserved worktree and branch `wow-night-observatory-queue` stay in place. The `-b` brief creates its own worktree.
- Under the network block, an audit of a code repository reports npm freshness as "registry unreachable" (a WARN). With `gh` unauthenticated, GitHub checks are skipped. Neither is a fault in the home.
- `ki repo repair` may write into the checkout it repairs. The README says a run must review and discard only what repair wrote.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 02:10 BST

🤖 0 running · 👤 0 with you

- [uncommitted] audit-home edits to 23 overnight briefs and the new `wow-night-observatory-queue-b.md`, in the ki.ways-of-working work folder
