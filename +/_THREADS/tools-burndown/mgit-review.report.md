<!-- markdownlint-disable-file MD041 -->
# [Platform foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/platform-foundations.md) › [Tools burndown](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/tools-burndown.md) › mgit-review

**Run report at 22:41 BST · last mark none yet (thread opened 01:05 BST, 16 October)**

---

## Done

- **Verdict: ready for Kris's ki-accept.** [KI-TOOL-MGIT-CLI-017](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-017-unified-external-members.md) does what it says, and it meets every point of the MGIT-MEMBERS request of 22:01 BST, 16 October. I found no blocking or medium findings, only four low ones (listed below). I reviewed commit `e7511d1` on the rebased `main` (6 commits ahead of `origin/main`, working tree clean).
- **The request, point by point:**
  - **External `../` paths only for repository members.** Accepted only in direct `[members."PATH"]` entries with `kind = "repository"`. Rejected for workspace members, the grouped form, `..`, `../`, `../..`, `../a/../b`, `./` segments, `//`, a trailing `/`, and `a/../../x`.
  - **Deduplicated by real path.** Two spellings of one checkout through a symlinked folder dispatch once. So does a local member reached through a symlinked folder alongside an external member. The same path written twice in one manifest is rejected. If an external member is itself a symlink, selection rejects it.
  - **Repair never clones an external member.** In both preview and `--apply`, a missing external member is reported as "not cloning" and nothing is created. A present external member is checked.
  - **Legacy `registered.members` tables.** Still readable, with a deprecation warning and a doctor `warn`. `mgit register --dry-run` previews the rewrite, and `mgit register` rewrites them as typed, sourced members. The saved locations and the local members are kept. Mixing legacy tables with new members, including the same path in both forms, selects the checkout once. Behaviour matches v0.17.0 for a legacy entry that duplicates a local member.
  - **Dotfiles dispatched exactly once.** Tested in a disposable copy of the layout (`~/.local/share/chezmoi` with remote `krisb/dotfiles`, plus `~/workspaces/personal`). The checkout was dispatched once from `personal` and once from `~/workspaces`. That held with the `dotfiles` navigation symlink, without it, under `-L`, and under `-I -L` discovery. A `mgit register` run from `~/workspaces` kept the personal external member and its location.
- **Gate, all passing.** `ki repo audit --repo .` FAIL=0, with only the existing HOOK-1 warning. `shellcheck`, `bash -n`, `mandoc -T lint` and `git diff --check` are clean. `bats tests/` passes 98 of 98. With `MGIT_KI_PRODUCER` set to the installed `ki`, 98 of 98 pass with no skips. Bash is 3.2.57.
- **Live, read-only.** The working-tree build lists 7 repositories from `~/workspaces/personal` and 54 from `~/workspaces`, and doctor reports healthy at both levels. That matches the record. I ran no `register` or `repair` against the real manifests. The real chezmoi source has no uncommitted changes and I did not touch it. My sandbox's fake HOME stopped a `chezmoi add` call before it changed anything. Later probes used a stub `chezmoi`.
- **Docs match behaviour.** I checked the specification, the repository-sets guide, the changelog, the manual and the help against the probes.
- **Low findings (none blocks acceptance):**
  - **L1, missing external member.** If the external checkout is missing, selection fails for the whole set, including from `~/workspaces`, and repair only reports it. A missing local member behaves the same way, and the chezmoi checkout exists on every machine that applies the manifest. So this matters only if the member is ever declared on a machine without the checkout.
  - **L2, external path pointing back inside the workspace.** A hand-written path such as `../personal/acquire` is quietly deduplicated, not rejected. Registration never writes one.
  - **L3, register drops hand-written external members.** `mgit register` drops a hand-written external member that has no matching location, and `--dry-run` does not name it. The guide documents this, and it fits the generated-members model.
  - **L4, cosmetic.** `mgit repair` prints the deprecation warning twice for one manifest, once for each spelling of its path.
- **Confirmed:** v0.17.0 rejects any manifest that contains an external member. CONSUMER-MIGRATE (release first, then migrate source and live together) is the right order. As the record says, `register add --repo` refuses a navigation symlink.
- **Nothing committed.** The record needed no review notes, and this report is uncommitted. I did no ki-accept and no push.

## In Progress

Nothing is running.

- **Push held.** The six tools-mgit commits on `main` wait for Kris's ki-accept of KI-TOOL-MGIT-CLI-017. Then: fetch, check that `main` is still only ahead, and push fast-forward.

## Queries

### MGIT-REVIEW-LOWS - what to do with the four low findings

**Context:** L1 to L4 above are edge cases or cosmetic. None breaks the request or the acceptance criteria. Fixing them inside KI-TOOL-MGIT-CLI-017 would reopen a record that is ready to accept.

**Query:** Should the low findings hold up acceptance?

**Options:**

a) (recommended) Accept KI-TOOL-MGIT-CLI-017 as it stands, and capture L1 to L4 as one triage record in tools-mgit for a later `ki-next` pass.

b) Accept, and drop the findings.

c) Hold acceptance and fix L1 to L4 under KI-TOOL-MGIT-CLI-017 first.

```text
MGIT-REVIEW-LOWS
Accept KI-TOOL-MGIT-CLI-017 as it stands, and capture L1 to L4 as one triage record in tools-mgit for a later ki-next pass.
```

```text
╭─ run report · 2026-10-17T21:41:00Z ──────────────╮
│                                                  │
│  █▀▀▄ █▀▀▀ █▀▀▀ ▀▀█▀   · thread at rest          │
│  █▀▀▄ █▀▀  ▀▀▀█   █    · nothing running         │
│  █  █ █▄▄▄ ▄▄▄█   █    · push held               │
│                                                  │
╰──────────────────────────────────────────────────╯
```

- [at rest] nothing running or queued from this run
- [held] tools-mgit push, until Kris's ki-accept of KI-TOOL-MGIT-CLI-017
- [waiting] MGIT-REVIEW-LOWS; ki-accept of KI-TOOL-MGIT-CLI-017
- [committed] nothing from this run; this report uncommitted

```text
Resume Fnd: tools-burndown under current ki-pmo and ki-delegation since 2026-10-16T00:05:00Z: re-bootstrap, mark, fresh summary with carried-forward open points, take stock, restart authorised work, then banner.
```
