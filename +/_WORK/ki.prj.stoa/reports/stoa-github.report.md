# [Foundations](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Stoa](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/stoa.md) › stoa-github

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 05:20 GMT · last mark 05:20 GMT**

---

## Done

- Started from what `stoa-toolchain` left: its report has no blocking query and no failing check, and `main` was clean and level with `origin` at `5da3fb0` after a fetch and fast-forward pull.
- `ki repo audit --repo .` fails on 8 GitHub-settings findings, all on `knowledgeislands/packages-stoa`:
  - the GitHub description is empty (GH-3);
  - merge commits and rebase merges are allowed as well as squash, where the standard wants squash only (MERGE-1);
  - branches are not deleted automatically after a merge (MERGE-1);
  - Issues are on, where the standard wants them off because `.ki.toml` does not declare GitHub Issues as the work tracker (TOGGLE-1);
  - Projects are on, where the standard wants them off (TOGGLE-1);
  - Dependabot alerts are off (DEP-1);
  - Dependabot security updates are off (DEP-1);
  - pull requests are not offered the "update branch" button (DEP-1).
- The audit also keeps one warning that is not a GitHub setting: TURBO-2, which wants a `build` script for the workbench. The workbench has none on purpose, as the `stoa-toolchain` report explains.
- The repository stays private, and the licence field raises no finding.
- `ki repo conform --repo . --dry-run` (also tried with `--allow-commands`) proposes no change. Conform only repairs local files, and only after the audit passes. It has no step that writes GitHub settings. The `ki-repo` skill says the same: live GitHub settings are applied by hand with `gh` commands, after showing the change and getting explicit confirmation.
- No file changed, so there is no commit. `git status` is clean. No GitHub setting was changed.

## In Progress

- Blocked: the 8 GitHub-settings findings stay open until you answer the query below. The final audit, the `bun` checks and the push were not run, because nothing has changed since `stoa-toolchain` checked them.
- Candidate for a roadmap record, not created: `ki repo conform` could apply the GitHub settings that `ki repo audit` checks, rather than leaving them to hand-written `gh` commands. That would belong in `tools-ki`.

## Queries

### STOA-GITHUB-APPLY - Apply the GitHub settings with `gh` commands

**Context:** Your decision STOA-AUDIT-REST b) authorised only the GitHub reads and writes that `ki repo audit` and `ki repo conform` make for `knowledgeislands/packages-stoa`. Conform makes no GitHub writes, so none of the 8 findings can be fixed under that wording. The `ki-repo` standard's own way to apply them is a short set of `gh` commands (GitHub's command-line tool) on this one repository. The description it would set is the one already in `.ki.toml` and `package.json`: "Canonical source of Stoa, vendored into each site built on it". The repository stays private.

**Query:** May a run apply these settings to `knowledgeislands/packages-stoa` with exactly these commands, then rerun the audit, check and push?

```zsh
gh repo edit knowledgeislands/packages-stoa \
  --description "Canonical source of Stoa, vendored into each site built on it" \
  --enable-merge-commit=false --enable-rebase-merge=false --enable-squash-merge=true \
  --delete-branch-on-merge=true --allow-update-branch=true \
  --enable-issues=false --enable-wiki=false --enable-projects=false
gh api -X PUT repos/knowledgeislands/packages-stoa/vulnerability-alerts
gh api -X PUT repos/knowledgeislands/packages-stoa/automated-security-fixes
```

**Options:**

a) (recommended, confidence high - these are the standard's own commands, limited to this one private repository, and they change only what the audit flags) Yes, apply exactly these commands and finish the run.

b) Yes, but leave the Dependabot settings off for now, and accept that DEP-1 stays failing.

c) No; leave the settings until `ki repo conform` can apply them itself.

### 🤖 → 👤 Handoff to supervisor · at 05:20 GMT

🤖 0 running · 👤 1 with you

- [blocked] stoa-github · supervisor · since 05:20 GMT

🧵 ki.prj.stoa
