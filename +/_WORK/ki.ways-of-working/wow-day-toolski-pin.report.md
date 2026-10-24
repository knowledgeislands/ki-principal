# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-toolski-pin

**🤖 → 👤 Handoff to supervisor · Run report at 14:57 BST · last mark 14:11 BST**

---

## Done

Ready for Kris to tag `v0.13.0` at `65e062737e3efaa696c5d92aaf2f8fc8bf31d1e9`: committed `fix(bootstrap): pin the v0.13.0 Harness archive`, integrated into clean local `main` and pushed fast-forward; only this run's commit was unpublished and pushed. [Integration evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-toolski-pin.work/integration.json).

Confirmed the writer designation and followed the remaining-steps continuation under the [21 October owner answers and afternoon grant](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md); no range review, version preparation or acceptance was repeated.

Retained the preceding preparation commit as the already-published parent; its full release-range review, acceptance evidence, changelog and migrations remain in the [preceding release dossier](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-toolski-release.report.md), [review index](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-toolski-release.work/review-index.json) and [acceptance map](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-toolski-release.work/acceptance-map.json).

Pinned the newest freshly fetched Harness `origin/main` revision, including its verified codeload digest, in the separate commit required by the [release guide](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/guides/developer/releasing.md); only the [Harness pin](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/storage/registry.ts:23) and [bootstrap expectations](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/bootstrap/bootstrap.test.ts) changed.

Archive verification: PASS, one credential-free public codeload read, SHA-256 recorded and all 1,388 archive file entries matched the fetched Git revision, including content, type and mode. [Exact revision, URL and SHA-256](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-toolski-pin.work/archive-proof.json).

Real archive acquisition: PASS through the public CLI sandbox with injected saved archive bytes and external networking denied; all 1,188 installed payload files matched, and repeated bootstrap made no further fetch. [Proof](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-toolski-pin.work/bootstrap-proof.json).

Unchanged baseline gates: PASS; candidate gates: PASS, both offline under separate fresh audit-home copies with both Capital registries confined to those copies. Baseline used the README's FILES-10 overlay; candidate used the actual newly pinned Harness. [Baseline checks](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-toolski-pin.work/baseline/results.json); [candidate checks](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-toolski-pin.work/candidate/results.json).

Frozen root and boundary installs: PASS, with prepare hooks enabled and locally copied dependencies; TypeScript, Biome and manual lint: PASS. [Candidate checks](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-toolski-pin.work/candidate/results.json).

Functional tests: PASS, 1,487 tests in 90 files; coverage: PASS at 100% statements, branches, functions and lines. [Tests](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-toolski-pin.work/candidate/test.log); [coverage](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-toolski-pin.work/candidate/coverage.log).

Repository audit: PASS, 20 passes, 2 warnings, 0 failures; unchanged baseline warnings only: inline CI pin (CI-1) and undeclared maturity (MATURITY-1), passed under the recorded pre-existing-warnings allowance. [Baseline audit](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-toolski-pin.work/baseline/audit.log); [candidate audit](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-toolski-pin.work/candidate/audit.log).

Native candidate: PASS, version `0.13.0`, root/help routes, `ki agent launch --allow`, Bash/Zsh completion and syntax, command inventory, and offline bootstrap using the new digest; unsigned Darwin arm64 package contains exactly the executable and manual. GRANT-INTERIM capability is included; its Harness interim sentence remains until the release is installed. [Verification](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-toolski-pin.work/verification.json).

Hook-backed commit: PASS, explicit paths only, actual model co-author trailer, committed paths inspected and verified contents unchanged; the shared primary checkout is clean on the pushed commit. [Commit evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-toolski-pin.work/committed-paths.txt); [integration](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-toolski-pin.work/integration.json).

Exact-head CI: PASS, [CI run 39612182761](https://github.com/knowledgeislands/tools-ki/actions/runs/39612182761) completed successfully on `65e062737e3efaa696c5d92aaf2f8fc8bf31d1e9`; observed read-only through GitHub's browser page without GitHub API calls. [Recorded result](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-toolski-pin.work/ci-result.json).

Changelog and migrations: the consolidated [Pre-1.0 baseline](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/CHANGELOG.md) is already prepared for 0.13.0; migration instructions remain in [Granola acquisition](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/guides/user/granola-acquisition.md), [background agents](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/guides/user/background-agents.md) and [repository operations](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/guides/user/repository-operations.md).

### Exact tag and publication commands for Kris

The following commands are the handoff only; none was executed by this run. The live immutability check remains a publication prerequisite for Kris and must succeed before tagging.

```sh
set -eu
cd /Users/krisbrown/workspaces/knowledge-islands/tools-ki
git fetch -q origin
test "$(git branch --show-current)" = main
test "$(git rev-parse HEAD)" = 65e062737e3efaa696c5d92aaf2f8fc8bf31d1e9
test "$(git rev-parse origin/main)" = 65e062737e3efaa696c5d92aaf2f8fc8bf31d1e9
test -z "$(git status --porcelain=v1)"
test -z "$(git tag --list v0.13.0)"
python3 - <<'PY'
import json
from pathlib import Path
assert json.loads(Path('package.json').read_text())['version'] == '0.13.0'
pin = Path('src/core/storage/registry.ts').read_text()
assert 'https://codeload.github.com/knowledgeislands/ki-agentic-harness/tar.gz/52779419f518f8e5ee53ca675c9c9ecc215da2d5' in pin
assert '6dbf377bb0ac9d6536f97643ddc02df95f79ae695984445eab9e5dc56d3efb8c' in pin
PY
test "$(gh api repos/knowledgeislands/tools-ki/immutable-releases --jq .enabled)" = true
git tag v0.13.0 65e062737e3efaa696c5d92aaf2f8fc8bf31d1e9
git push origin v0.13.0
gh workflow run release.yml --repo knowledgeislands/tools-ki --ref main -f version=v0.13.0
```

The release workflow owns the three target builds, signing, draft asset verification, immutable publication and clean Linux installation proof; Kris retains tagging and publication.

## In Progress

Nothing is running. Kris owns tagging and publication using the verified commit and commands above.

Outstanding - no action requested now: the owned linked worktree, branch, copied audit homes, saved public archive, unsigned native package and reproducible verification evidence remain under [this run's work directory](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-toolski-pin.work) because deletion was prohibited; no unpushed tools-ki commit remains on `sol.local`.

Verification limits: no tag, publication, signing, installed-release update, live apply, credential access or sibling repository edit was performed. Release publication settings and post-publication proofs remain with Kris; the complete local gate and exact-head CI are green. No roadmap record was created, accepted or pruned.

## Queries

None.

### 🤖 → 👤 Handoff to supervisor · since 14:57 BST

👤 1 handoff

- [handoff] Tag and publish tools-ki v0.13.0 from the verified dossier · owner · since 14:57 BST
