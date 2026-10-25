# wow-deploy-fix - find and fix why the website stopped deploying

## Goal

<https://knowledgeislands.info> still serves a build from before commit `d547611` (the diagram pipeline, 04:22 GMT on 2026-10-25). Every page and diagram pushed to `main` since (`30e53c5`, `57864b1`, `1056bb6`, `1edd468`, `beef155`, `de1b44e`, `8b4b7b7`, `076bcc4`, `31f4ba3`) returns 404 live, for example <https://knowledgeislands.info/docs/standards/writing/> and <https://knowledgeislands.info/diagrams/site/work-model.html>. Find why the deploys stopped and, where the cause lies in the repository, fix it so the current `main` goes live.

## Scope

- Website repository: `/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info` (GitHub `knowledgeislands/apps-knowledgeislands.info`). Read its deployment configuration (`wrangler` configuration, build commands, `.ki.toml`, `package.json` scripts, any GitHub Actions workflows) and its documented deploy path.
- Read-only evidence: `gh run list` / `gh run view --log-failed` for workflows, GitHub commit statuses and check runs on `d547611` and later (`gh api repos/knowledgeislands/apps-knowledgeislands.info/commits/<sha>/check-runs` and `/status`), and Cloudflare build or deployment logs if a read-only `wrangler` command reaches them (`wrangler deployments list`, `wrangler versions list`). Compare the last good commit with `d547611`.
- Reproduce the deploy build as the deploy environment runs it, in a clean temporary clone (never in the primary checkout, which holds another session's uncommitted file `apps/site/scripts/verify-diagrams.test.ts`; never touch it). A likely cause is a build step added by the diagram pipeline that needs a tool absent from the deploy environment (for example the `ki` CLI or a local diagram renderer) where committed generated output would serve.
- If the cause is in the repository, fix it with the smallest change that keeps every local gate passing (site build with every gate, tests, typecheck, the website-content, authoring and diagrams audits; DEPS-1 and CI-1 are the known baseline), commit by explicit path from the clean clone, and push `main` fast-forward. Then poll the live site for up to 15 minutes and confirm the two example addresses answer 200.

## Constraints

- No Cloudflare, DNS or GitHub settings change of any kind, no secret change, and no manual `wrangler deploy` or other out-of-band deployment: if the cause lies there, stop and report it as a query with the exact setting and evidence.
- No dependency installs, updates or lockfile changes.
- Never force-push or use `--no-verify`.

## Report

Done: the cause with its evidence, the fix commit if any, and whether the examples now answer. Queries: a setting change Kris must make, in full, with the evidence.
