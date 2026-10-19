---
note_type: streams/project
slug: tools-burndown
title: Tools burndown
outcome: The tools-ki, tools-mgit and tools-git-almanac roadmaps and the CLI-shaped ki-agentic-harness records are burned down to zero - every record closed, merged or rejected - ending with the ki and mgit releases.
theme: foundations
lifecycle: active
lead: Kris Brown
target: null
updated: 2026-10-19T23:16:23Z
author: Written with Claude
---

# Tools Burndown

## Outcome

Burn the `tools-ki`, `tools-mgit` and `tools-git-almanac` roadmaps, and the `ki-agentic-harness` records about the `ki` CLI, its commands, release or packaging, down to zero: every record closed, merged or rejected. No new feature record is captured, except the one `tools-ki` triage record Kris's REPO-GIT-HYGIENE decision of 16 October 2026 asks for. The Project ends with the `ki` and `mgit` releases, each cut only after Kris approves it.

This Project sits in [[Themes/foundations|Foundations]]. Kris revived it on 16 October 2026 with TOOLS-PROJECT: "Revive tools-burndown as a Project under Platform foundations, thread KI > Foundations > tools burndown, scoped to tools-ki, tools-mgit, tools-git-almanac and the CLI-shaped ki-agentic-harness records, excluding tools-rig and tools-techne, ending with the ki and mgit releases."

---

## Notes

### Scope

- **In:** `tools-ki`, `tools-mgit` and `tools-git-almanac` roadmaps; `ki-agentic-harness` records about the `ki` CLI, its commands, release or packaging.
- **Out:** `tools-rig`, which the Rig threads own, and `tools-techne`, under the [Techne Programme Focus](<../../Admin/Governance/Policies/Techne Programme Focus.md>).
- Membership is classification, not authority. Several in-scope records name another Project. Under OWNER-LANE, applied on 16 October 2026 through Kris's BURN-OVERNIGHT, this Project runs the single `tools-ki` writer for every in-scope record, because the installed `ki` runs the primary checkout and two writers would collide; the owning threads, ways-of-working and knowledge-acquisition, keep priority and acceptance input.
- **Held outside the burn-to-zero:** under RELEASE-CONTRACT, applied on 16 October 2026 through BURN-OVERNIGHT, the `tools-ki` KI release contract record stays on Hold with the agent-host Project until its 2026-11-16 review. It is excluded from this Project's burn-to-zero and from the `ki` release gate; `ki` already ships signed archives for the platforms in use, so the release proceeds without it.
- **mgit release:** under MGIT-RELEASE, applied on 16 October 2026 through BURN-OVERNIGHT, an `mgit` release is cut only if `mgit` changes land during the Project, with Kris's approval; otherwise `v0.17.0` stands as the Project's `mgit` release.
- **Coupled harness records:** four `ki-agentic-harness` records - delegation run events, the thread-folder closed list, local resolution targets and moving a thread between hosts - pair with `tools-ki` work and are sequenced alongside it, but are not burned down here. Each names its `tools-ki` pairing in its own record.

### Inventory

This note names no work records: each record carries its own Project, and in-scope membership is by the Scope above rather than by that field. The live inventory is read from each repository's roadmap; the 16 October 2026 snapshot is the thread's [inventory report](../../+/_WORK/ki.tools-burndown/inventory.report.md).

`tools-mgit` and `tools-git-almanac` held no open records on 16 October 2026, and `tools-mgit` has no change since `v0.17.0`. The open `ki-agentic-harness` records are left out because they change skills and standards or acquisition, not the `ki` CLI, its commands, release or packaging, and the CLI mechanics two of them need are already `tools-ki` records.

### Ideas

They are ideas, not records: under CAPTURE-ONLY Kris asked for capture now and a prioritisation phase later, so none becomes a roadmap record until then.

- **MGIT-ESCAPE** (Kris, 17 October 2026 intake, [ki decisions log](../../+/_WORK/ki/decisions.md)): an escape hatch from mgit's own commands, which override the git pass-through - "Git has got work tree. We've got mgit work tree, so it'd be nice to have an escape hatch". `--bare` runs the git subcommand in each child, bypassing mgit's command; `--raw` runs any command as a shell in each repository directory; mind clashes with the physical and follow-symlinks options.
- **MGIT-OUTPUT** (Kris, 17 October 2026 intake, [ki decisions log](../../+/_WORK/ki/decisions.md)): "I really want MGIT to have much better output" - a progress bar across the estate, then results at the end listing only the repositories that changed; try it first on `sync`, where a pull that hits a rebase or merge warning aborts automatically and warns instead; perhaps with code behind it, as with the Git Almanac.

### History

The earlier tools-burndown thread, run under the [Estate factorisation](estate-factorisation.md) checkpoint, is this Project's history: its folder `+/_WORK/ki.tools-burndown/`, its `decisions.md` and its `historical-decisions.md`.
