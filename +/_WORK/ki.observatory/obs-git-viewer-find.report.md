# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/work.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/work.md) › obs-git-viewer-find

**🤖 → 👤 Handoff to supervisor · Run report at 00:22 BST**

---

## Done

**1. Where the git viewer is.** Only one copy exists, and nothing has been lost. It is committed in `personal-principal` with nothing uncommitted:

- [Kit Git Repo Audit.html](/Users/krisbrown/workspaces/personal/personal-principal/Pillars/Productivity/Knowledge%20Management/Integrations/Claude/Live%20Artifacts/Kit%20Git%20Repo%20Audit.html) is the page (58 KB). Its last commit is `f161cc8b` on 12 October 2026, which only renamed the server ID. The last real feature work was 6 to 7 August.
- [Kit Git Repo Audit Artifact.md](/Users/krisbrown/workspaces/personal/personal-principal/Pillars/Productivity/Knowledge%20Management/Integrations/Claude/Live%20Artifacts/Kit%20Git%20Repo%20Audit%20Artifact.md) is the recipe (35 KB), last committed in the same commit.

I found no other copy in `~/workspaces`, the OneDrive source stores, the Claude Desktop app data or `~/workspaces/claude-desktop`. That last folder's `Artifacts/` is empty.

What has gone wrong is that it has stopped working where you would use it, for two reasons:

- It is no longer installed in Claude Desktop, so it has to be saved into Cowork again before it will open there.
- It still scans `~/workspaces/hnr` and `~/workspaces/kit`, which no longer exist. Every territory would show as an error line, and only chezmoi would load. [PERSONAL-PRINCIPAL-044](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/PERSONAL-PRINCIPAL-044-reground-git-audit-artifact.md) records this fix, but it is still at triage.

**2. What it has that the Observatory lacks.** The Observatory's Repositories view does three things the viewer does not:

- It reads `git` directly, splitting staged from unstaged changes.
- It raises Beacon signals and counts the agent runs working in each repository.
- It shows committed Archify diagrams.

It also offers fetch dry run, fetch, fast-forward pull and push, each confirmed and receipted. The service answers on port 1675.

The Observatory has none of the following:

- **Overview:**
  - A heatmap with one row per folder, made of small tiles coloured by severity, with the count printed on the amber and red tiles.
  - Summary tiles for needs attention, dirty, stale and clean, which you click to filter.
- **Finding repositories:**
  - A search box.
  - Filters by severity, by root and by individual folder.
  - Sortable columns (repository, status, branch, last commit).
  - All filter and sort choices are remembered across reloads.
  - The Observatory has a fixed attention order, optional grouping by owner, and the shell's filters.
- **Coverage:**
  - Grouping by root.
  - chezmoi as a repository of its own.
  - A failing root shows as one error line instead of blanking the page.
  - A 2-minute cache with a badge showing whether you are looking at cached data.
- **Detail panel:**
  - A list of the commits not yet pushed.
  - A warning when there are remote commits you have not pulled.
  - The changed files with their status letters.
  - The 5 commits before the unpushed ones.
  - A coloured diff for each file.
- **After an action:** the repository is re-audited automatically and its row flashes amber. The panel then returns to the buttons that now apply, with no Dismiss step.
- **Bulk actions per folder:**
  - Fetch, pull N and push N across a whole folder, from the heatmap or the table header.
  - A confirmation that lists the affected repositories.
  - Live progress for each repository, buttons locked while it runs, and a summary at the end.
- **Commit:**
  - A file checklist with all and none toggles.
  - Untracked files are left unticked by default.
  - A diff for each file, and a commit message suggested by Claude.
  - A dry-run preview before you confirm.
  - The draft survives the page redrawing.
- **Launchers:** open in VS Code in a new window, and open in GitHub Desktop.

**3. Whether [KI-OBSERVA-VIS-041 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/c1f008346dc085a0c25026ea5c9a08b383ef1d5b/docs/roadmap/KI-OBSERVA-VIS-041-git-view-replaces-repositories.md) covers it.** [KI-OBSERVA-VIS-041 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/c1f008346dc085a0c25026ea5c9a08b383ef1d5b/docs/roadmap/KI-OBSERVA-VIS-041-git-view-replaces-repositories.md) does point at the right artifact, since only one copy exists. It names it only as "a live artifact in `personal-principal`", though, with no path, commit or link to the recipe.

Its scope carries five of the viewer's features: grouping by root, chezmoi, the heatmap, the diff, and per-folder bulk actions with progress. These are not in its scope at all:

- The summary tiles, and clicking them to filter.
- Search, and the severity, root and folder filters.
- Sortable columns.
- Remembering filters and sort across reloads.
- Counts printed on the heatmap tiles.
- The detail panel's lists: unpushed commits, the not-pulled warning, and the 5 earlier commits.
- The automatic re-audit and row flash after an action.
- The cache and its badge.
- The one-line error for a failing root.
- The viewer's severity rules, including stale after 30 days. The Observatory uses 90 days and a different order.

These are left out on purpose, each because it is a write or needs an LLM, or (the launchers) because it would start an app on your machine:

- Commit, with its checklist, dry-run preview and saved draft.
- Bulk actions of any kind. That includes bulk fetch, even though fetch changes nothing.
- The Claude commit suggestion.
- The VS Code and GitHub Desktop launchers.

The record is still a draft, and the plan it carries puts all of this after first moving Repositories across unchanged.

## In Progress

Nothing. I changed and committed nothing.

## Queries

None.
