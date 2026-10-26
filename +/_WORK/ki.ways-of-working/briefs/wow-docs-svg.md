# wow-docs-svg - fix the broken SVG diagrams on the public docs

## Goal

Kris reported on 26 October 2026: "the SVGs don't look to be working" on <https://knowledgeislands.info/docs/skills/how-the-skills-fit-together/>. Find out why the diagrams on that page do not render, fix the cause at its source, and get the corrected page live.

## Scope

- First, establish the facts. Fetch the live page and its SVG URLs. Record the HTTP status, the content type and whether each SVG body is valid. Find where the page and its diagrams come from: the website repository `apps-knowledgeislands.info`, and any docs source it pulls in, such as the `ki-agentic-harness` docs published under DOCS-PUBLISH.
- Fix the cause in the repository that owns it. Possible causes include a wrong path or base URL, an asset missing from the build output, the wrong content type or headers, or the way the SVG is embedded. Check every other docs page that embeds SVGs, and fix them in the same change if they share the cause.
- Run the repository's own build and tests locally before pushing. Commit by explicit path and push fast-forward only. Never force-push and never use `--no-verify`.
- After the push, wait for the deploy and confirm on the live page that the diagrams render: fetch the SVG URLs and confirm they now return valid SVG with an image content type.

## Limits

- You may fix Cloudflare Pages build settings if the build needs it. Do not touch DNS, Cloudflare Access, routes, Zero Trust or credentials.
- Do not install new software. Do not make any change in Linear, Notion or other people-facing systems.
- If the fix needs anything outside these limits, stop and raise it as a query.

## Report

Write the run report in the owner-report shape: Done, In Progress and Queries. Give the cause found, each commit, and the live verification result.
