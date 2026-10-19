# ki.ways-of-working queries

## Open

### NO-GATE - Give the general Project shape a real commit gate

**Context:** apps-dafacts.org, apps-kris.me.uk and acquire declare `ki-repo-project` and have no package; HOOK-1 asks for a committed pre-commit gate, but the Project standard declares none, and section 2.2 of [hooks-standard.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/design/hooks-standard.md) names an audit over all declared skills instead. Routed from ki.tools-burndown through State of play at 00:23 BST; blind review qreview9 (`~/.local/state/ki/agents/tools-burndown/qreview9.report.md`) agreed a) at medium. The hook installs themselves stay with ki.tools-burndown under HOOKS-MIGRATION.

**Query:** Should the `ki-repo-project` shape declare a staged, check-only gate now, and which scope?

**Options:**

a) (recommended, confidence medium - reviewed by qreview9; a shape-owned baseline satisfies HOOK-1 with no dependencies, but its scope differs from the design's 2.2) Declare a staged, check-only `ki repo audit --skill ki-repo` as the `ki-repo-project` gate criterion in ki-agentic-harness, and amend section 2.2 of the hooks design to match, before ki.tools-burndown installs it.

b) Adopt the design's existing staged audit over all declared skills as the Project gate, after checking it stays local and practical on acquire's preserved captures.

c) Keep the missing-hook warning until the Project shape declares a gate, leaving the three repositories without automatic checks meanwhile.

### GFM-HOSTING-RULES - Declare the harness's protected `main` to match GitHub

**Context:** GitHub reported at 22:09 BST on 19 October that Kris's push to ki-agentic-harness bypassed its `main` rules (pull request and required `build` check). CI does define that check: `.github/workflows/ci.yml` has one job, `build`, on pushes to `main` and on pull requests, so the rule and CI agree. The `ki-repo` standard's protected-`main` set is exactly a pull request with 0 approvals, the `build` check, linear history and "admins not enforced", so Kris's bypass is the designed behaviour. But the harness `.ki.toml` does not set `branch-protection = true`, and the standard's default is an open `main` with leftover protection stripped. `update-ki-pin.yml` auto-merges the pin pull request only when `main` has required status checks (XDR-KI-HARNESS-001), so the rule is load-bearing. Live GitHub settings were not read (no remote calls in this run).

**Query:** Should the harness declare its protected `main` so its declaration matches GitHub and the pin auto-merge?

**Options:**

a) (recommended, confidence medium - CI and the standard checked directly, live ruleset not read) Add `branch-protection = true` under `[skills.ki-repo]` in the harness `.ki.toml` by a one-line commit, leaving GitHub unchanged; the next `ki repo audit` with GitHub access confirms the live set matches, including whether a ruleset satisfies the check written for classic protection.

b) Leave the declaration off and strip the rule on GitHub to match the open-`main` default; this stops the pin pull request auto-merging.

c) Enforce the rule for admins too, so every harness change goes through a pull request; this departs from the standard and slows every agent run.

## Parked

Nothing parked.
