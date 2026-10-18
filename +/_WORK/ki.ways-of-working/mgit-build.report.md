# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › mgit-build

**🤖 → 🧑 Handoff to supervisor · Run report at 07:41 BST · last mark 07:41 BST**

---

## Done

I worked in tools-mgit's main checkout and tested only in disposable fixtures: Bats repositories with local bare origins and isolated Git configuration. Each commit below was green and was pushed fast-forward to `main`. Nothing live was touched. I made no release or version bump, ran no real-estate sync and changed no other repository apart from this report.

- [KI-TOOL-MGIT-CLI-017](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-017-unified-external-members.md), unified external members, is accepted provisionally on Fable's opinion of 18 October, for Kris to confirm (`f62d555`).
- [KI-TOOL-MGIT-CLI-018](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-018-estate-scale-output.md) to [KI-TOOL-MGIT-CLI-022](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-022-external-member-review-findings.md) are adopted into Next and planned to Ready, provisionally on the same opinion (`b359876`).
- [KI-TOOL-MGIT-CLI-022](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-022-external-member-review-findings.md), the external member review findings, is built to Awaiting review (`088c2f4`).
  - Inward external paths are rejected.
  - A dropped external member is reported with a re-add hint.
  - Checks: the gate passes.
- [KI-TOOL-MGIT-CLI-021](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-021-estate-overview.md), the read-only overview, is built to Awaiting review (`b8e5911`).
  - `mgit overview` reports, without fetching or writing, what is outstanding in each checkout.
  - It covers upstream, ahead and behind, the working tree, stashes, extra worktrees and obsolete branches. It also has `--json` and `--stale-days`.
  - Checks: the gate passes.
- [KI-TOOL-MGIT-CLI-018](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-018-estate-scale-output.md), the shared runner, is built to Awaiting review (`022ce41`).
  - Ordinary commands run in up to eight checkouts at once (`-j`), with no prompts.
  - Only checkouts with output or a failure are shown, in order, followed by one counting line.
  - `-v` streams one checkout at a time, and `--json` gives one document.
  - Checks: the gate passes.
- [KI-TOOL-MGIT-CLI-019](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-019-pass-through-escape-hatch.md), the pass-through escape hatch, is built to Awaiting review (`177557d`).
  - `-G/--git` sends names mgit owns to Git.
  - `-R/--raw` runs a command directly.
  - `-B/--bare` still works and warns that it is deprecated.
  - Checks: the gate passes.
- A suite fix, `test: make Bats assertions fatal under Bash 3.2` (`00ef0de`).
  - Under macOS Bash 3.2, a failing `[[ ]]` or `!` assertion in the middle of a Bats test did not fail it.
  - Every such assertion now ends `|| false`.
  - The five latent assertions this exposed were wrong in the tests, not in mgit.
  - Checks: the suite passes against the code it was committed with.
- [KI-TOOL-MGIT-CLI-020](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-020-safe-parallel-sync.md), safe parallel sync, is built to Awaiting review (`67d94e0`).
  - `mgit sync` fetches in parallel, then one checkout at a time fast-forwards a branch that is only behind or pushes a branch that is only ahead.
  - Diverged, dirty, detached, untracked and fetch-failed checkouts get a warning and are left untouched.
  - It never merges or rebases, and only checkouts that need attention are named.
  - Checks: the gate passes, 122 of 122 Bats tests, and the new sync cases fail against the old code.

The gate for each build was `ki repo audit` (passes with the existing HOOK-1 warning), `shellcheck`, `bash -n`, `bats tests/`, `mandoc -T lint` and `git diff --check`, all clean.

## In Progress

Nothing. All five records are at Awaiting review, and none is accepted.

## Queries

### ACCEPT-017-ADOPT - provisional acceptance and adoption

**Context:** I took both steps on Fable's opinion of 18 October and logged them as provisional:

- the acceptance of [KI-TOOL-MGIT-CLI-017](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-017-unified-external-members.md);
- the adoption of [KI-TOOL-MGIT-CLI-018](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-018-estate-scale-output.md) to -022 into Next.

Either can be reopened by editing its record.

**Query:** Do you confirm both?

**Options:**

a) (recommended, confidence high - -022 settled -017's review findings and the gate is green) Confirm both. b) Reopen -017 for your own review. c) Return some of -018 to -022 to Later.

### ACCEPT-022 - external member findings

**Context:** Two choices are provisional:

- The inward-path check needs the external checkout to exist, so a missing inward path is still reported as missing.
- The drop hint's `register add --repo PATH` is relative to the manifest, which matches the working directory only in the top-level workspace.

**Query:** Do you accept [KI-TOOL-MGIT-CLI-022](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-022-external-member-review-findings.md) with them?

**Options:**

a) (recommended, confidence high - both are edge cases with a clear message) Accept as built. b) Make the hint path relative to the working directory first. c) Hold it for your own review.

### ACCEPT-021 - read-only overview

**Context:** Five choices are provisional:

- A branch without an upstream counts as needing attention.
- Obsolete branches go on indented lines under their checkout.
- A branch checked out in any worktree is never called obsolete.
- Under `-W`, repository-wide findings are reported once.
- The criteria follow the `ki-git` clean-down state, which waits on [KI-HARNESS-GOV-203](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-203-git-clean-down-criteria.md).

**Query:** Do you accept [KI-TOOL-MGIT-CLI-021](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-021-estate-overview.md) with them?

**Options:**

a) (recommended, confidence medium - the criteria may move with [KI-HARNESS-GOV-203](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-203-git-clean-down-criteria.md)) Accept now, and adjust the criteria in a follow-on if [KI-HARNESS-GOV-203](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-203-git-clean-down-criteria.md) changes them. b) Hold it until [KI-HARNESS-GOV-203](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-203-git-clean-down-criteria.md) is accepted. c) Change one of the choices first.

### ACCEPT-018 - shared runner

**Context:** Six choices are provisional:

- Captured output loses Git's colour; `-v` restores it.
- Interactive commands fail rather than wait unless run with `-v`. An SSH passphrase prompt is not suppressed.
- The closing count line goes to standard output, so scripts see one more line; `--json` is the stable interface.
- A clean status with no upstream is never quiet.
- An interrupt stops the workers, but a Git process a worker started may finish.
- The oldest running worker gates the pool, because Bash 3.2 has no `wait -n`.

**Query:** Do you accept [KI-TOOL-MGIT-CLI-018](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-018-estate-scale-output.md) with them?

**Options:**

a) (recommended, confidence medium - the change of default output is the one you asked for, but it is visible on every command) Accept as built. b) Send the closing line to standard error first. c) Hold it until you have tried it on the estate yourself.

### ACCEPT-019 - pass-through escape hatch

**Context:** Four choices are provisional:

- `-B` warns only when a command actually runs, so usage errors keep their first line.
- `-G -h` shows mgit's help; `mgit -G help` runs `git help`.
- Existing tests now use `-R`.
- No release is named for removing `-B`.

**Query:** Do you accept [KI-TOOL-MGIT-CLI-019](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-019-pass-through-escape-hatch.md) with them, and when should `-B` go?

**Options:**

a) (recommended, confidence high - small, additive and covered by tests) Accept as built, and leave the removal of `-B` until 1.0. b) Accept, and name an earlier release for removing `-B`. c) Hold it for your own review.

### ACCEPT-020 - safe parallel sync

**Context:** Six choices are provisional:

- `-i` asks only when a checkout really is behind or ahead, not about every clean branch.
- Bare repositories are counted, not named, unless `-v` is given. They still make the exit status 1.
- Under `-W`, linked worktrees of one repository share one fetch, so fetches never race for its ref locks.
- Pushes stay serial in the main shell, where a credential prompt can still appear.
- A branch whose upstream has gone is warned as having no upstream.
- The global `-v` and `-j` apply to sync, and `--json` is refused.

**Query:** Do you accept [KI-TOOL-MGIT-CLI-020](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-020-safe-parallel-sync.md) with them?

**Options:**

a) (recommended, confidence medium - it changes what sync prints, but nothing it does to a branch is less safe) Accept as built, after one supervised `mgit sync` on a small territory. b) Accept now, without the trial run. c) Change a choice first, for example naming bare repositories again.

### TEST-FATAL - Bats assertions were not failing

**Context:** Under macOS Bash 3.2, a failing `[[ ]]` or `!` assertion in the middle of a Bats test did not fail it, so some of the suite had been passing without checking anything.

`00ef0de` makes every such assertion fatal and fixes five latent test errors:

- physical temp paths;
- a manifest grep that matched a URL;
- a single-quoted newline;
- a help-text match;
- a `git-sync` on `PATH`.

None hid a fault in mgit. I committed the fix on my own judgement, provisional, for you to confirm.

**Query:** Do you keep the fix, and should the rule reach other Bats suites?

**Options:**

a) (recommended, confidence high - without it, assertions silently pass) Keep it, and add the `|| false` rule to `ki-repo-tools` for every Bats suite. b) Keep it in tools-mgit only. c) Replace it with a Bats helper or a newer Bash in tests.

```text
ACCEPT-017-ADOPT: a
ACCEPT-022: a
ACCEPT-021: a
ACCEPT-018: a
ACCEPT-019: a
ACCEPT-020: a
TEST-FATAL: a
```

```text
╭─ run report · 2026-10-18T06:41:57Z ──────────────╮
│                                                  │
│  █▀▀▄ █▀▀▀ █▀▀▀ ▀▀█▀   · thread at rest          │
│  █▀▀▄ █▀▀  ▀▀▀█   █    · nothing running         │
│  █  █ █▄▄▄ ▄▄▄█   █    · 7 queries open          │
│                                                  │
╰──────────────────────────────────────────────────╯
```

- [at rest] nothing running or queued from this run
- [waiting] ACCEPT-017-ADOPT, ACCEPT-022, ACCEPT-021, ACCEPT-018, ACCEPT-019, ACCEPT-020, TEST-FATAL
- [committed] tools-mgit f62d555, b359876, 088c2f4, b8e5911, 022ce41, 177557d, 00ef0de, 67d94e0, all pushed; this report committed in ki-principal

```text
Resume mgit-build: nothing to resume; answer the seven queries in the ways-of-working thread, then review the five records at Awaiting review.
```
