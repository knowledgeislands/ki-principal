# wow-ci-manual

Goal: Kris answered RELEASES-CI with option a on 27 October: "CI and release workflows set to workflow_dispatch only, no pin bumps". Releases are deprioritised; everything is linked locally.

Do: in each repository under /Users/krisbrown/workspaces/knowledge-islands with a checkout and GitHub Actions workflows, change every CI and release workflow's `on:` triggers to `workflow_dispatch:` only (remove push, pull_request, tag, schedule triggers). Leave site deploy workflows (Cloudflare or Pages deploys) untouched. Bump no pins, cut no release, change no GitHub settings, DNS, Cloudflare or credentials. Context: `design/query-sweep.md` and `design/roadmap-sweep.md` in /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working (search RELEASES-CI).

Per repository: skip it and say so if its checkout is dirty in `.github/` or behind its remote after a fetch; otherwise one commit `ci: run CI and release workflows on manual dispatch only`, staged by explicit path, pass the repository's own pre-commit hooks (never `--no-verify`), pull --rebase and push fast-forward only. Run actionlint where present.

Report: one line per repository (changed, skipped with reason, or nothing to change), plus any workflow you were unsure was CI, release or deploy.
