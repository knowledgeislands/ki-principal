<!-- markdownlint-disable-file MD041 -->
# [Platform foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/platform-foundations.md) › [Tools burndown](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/tools-burndown.md) › mgit-diverge

**Run report at 22:31 BST · last mark none yet (thread opened 01:05 BST, 16 October)**

---

## Done

- **No fetch needed.** The brief asked for a fetch, but the run rules forbid any remote call. Local `origin/main` already held the other session's two commits (`b206b8d` and `4070e62`), so I rebased onto that. Origin may have moved again since, so fetch again before the push.
- **Rebased.** The four local commits now sit on `origin/main` with no conflicts and no force. The local reservation `438722c` made the same ledger change as origin's `b206b8d`, so Git dropped it as already applied. The three remaining commits were rewritten as `02782fd` (Ready), `e7511d1` (feature, formerly `bcac3d1`) and `1f9c9e8` (submit for review).
- **One KI-TOOL-MGIT-CLI-017.** In tools-mgit `4389fb3`, [KI-TOOL-MGIT-CLI-017-unified-external-members.md](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-017-unified-external-members.md) is now the only record with that number. It keeps the delivered status (awaiting-review), design, evidence and slug, and takes in the origin capture's material: the dotfiles remote, the earlier registration shape, the boundary exclusions (no checkout rename or remote change, no general symlink discovery, no selection-scope change, no new dependency, no authority over dotfiles or live workspaces) and its six requirements, each noted as met by the delivery. The origin's `…-unify-repository-members.md` file is deleted. The record's baseline is now `4070e62`, and its review text gives both the old and the new commit identifiers.
- **Verification gate on the rebased tree, all passing.** `ki repo audit` FAIL=0, with the existing HOOK-1 warning only. `shellcheck`, `bash -n`, `mandoc -T lint` and `git diff --check` are clean. `bats tests/` passes 98 of 98. With `MGIT_KI_PRODUCER` set to the installed `ki`, all 98 pass with no skips. I fixed one rumdl emphasis finding in the merged record before committing.
- **Two new records.** tools-mgit `4dea9fb` reserves CLI-018 and CLI-019 in the ledger. `a12b96f` captures both records as `triage` and quotes Kris's words verbatim:
  - [KI-TOOL-MGIT-CLI-018 Estate-scale output](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-018-estate-scale-output.md) (MGIT-OUTPUT) covers a progress bar, a summary at the end that names only changed or failing repositories, piloting on `sync` first, and stopping instead of merging or rebasing on pull. It includes a flow diagram. It also records what `sync` already does: `--ff-only`, and a count of repositories that were already current.
  - [KI-TOOL-MGIT-CLI-019 Pass-through escape hatch](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-019-pass-through-escape-hatch.md) (MGIT-ESCAPE) covers `--bare` as a Git bypass, `--raw` in place of `-B`, and clearer `-P`/`-L` options. It includes a dispatch diagram. It flags that `--bare` changes meaning: today `-B, --bare` runs a shell command, so the change breaks existing invocations and needs a migration.
- **Committed locally only.** Commits used explicit paths and the co-author trailer, with no `--no-verify`. `main` is 6 commits ahead of `origin/main` and the working tree is clean. Nothing was pushed or released. This report is not committed.

## In Progress

Nothing is running.

- **Push held.** The six tools-mgit commits on `main` (Terra) wait for MGIT-ACCEPT, the acceptance of KI-TOOL-MGIT-CLI-017. When that comes: fetch, check that `main` is still only ahead, then push fast-forward.

## Queries

### MGIT-DRAFT - status of the two new records

**Context:** The brief asked for "draft" records. Under `ki-next`, an agent may capture a record only as `triage` with no horizon. Moving it to `draft` with a horizon and `kind` needs explicit approval of the exact horizon. So both records are `triage`.

**Query:** Should KI-TOOL-MGIT-CLI-018 and KI-TOOL-MGIT-CLI-019 move to draft now?

**Options:**

a) (recommended) Leave both as triage until the next tools-mgit `ki-next` pass picks one for planning.

b) Adopt both now as `draft`, `kind: deliver`, `horizon: next`.

### MGIT-OUTPUT-ROUTE - how to build the output work

**Context:** Kris suggested building the output work "like we did with Git Almanac", which is TypeScript/Bun with a separate adapter, model and renderers. The tools-mgit `AGENTS.md` requires pure Bash, with only `bash` and `git` at runtime, and forbids an npm toolchain, `package.json` and TypeScript. KI-TOOL-MGIT-CLI-018 records this as a decision needed before planning.

**Query:** Which route should planning assume?

**Options:**

a) (recommended) Keep `mgit` in pure Bash and borrow only Git Almanac's adapter, model and renderer separation. Settle the choice in a Decision Record when KI-TOOL-MGIT-CLI-018 is planned.

b) Allow a TypeScript/Bun rewrite or output layer, amending `AGENTS.md` and taking on the distribution and Homebrew changes, through a Decision Record at planning.

```text
MGIT-DRAFT
Leave KI-TOOL-MGIT-CLI-018 and KI-TOOL-MGIT-CLI-019 as triage until the next tools-mgit ki-next pass picks one for planning.

MGIT-OUTPUT-ROUTE
Keep mgit in pure Bash and borrow only Git Almanac's adapter, model and renderer separation; settle the choice in a Decision Record when KI-TOOL-MGIT-CLI-018 is planned.
```

```text
╭─ run report · 2026-10-17T21:31:44Z ──────────────╮
│                                                  │
│  █▀▀▄ █▀▀▀ █▀▀▀ ▀▀█▀   · thread at rest          │
│  █▀▀▄ █▀▀  ▀▀▀█   █    · nothing running         │
│  █  █ █▄▄▄ ▄▄▄█   █    · push held               │
│                                                  │
╰──────────────────────────────────────────────────╯
```

- [at rest] nothing running or queued from this run
- [held] tools-mgit push, until MGIT-ACCEPT
- [waiting] MGIT-DRAFT, MGIT-OUTPUT-ROUTE
- [committed] tools-mgit 02782fd, e7511d1, 1f9c9e8, 4389fb3, 4dea9fb, a12b96f, not pushed; this report uncommitted

```text
Resume Fnd: tools-burndown under current ki-pmo and ki-delegation since 2026-10-16T00:05:00Z: re-bootstrap, mark, fresh summary with carried-forward open points, take stock, restart authorised work, then banner.
```
