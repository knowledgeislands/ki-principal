# wow-review-deps - blind review of one maintenance choice

Read-only review. Make no edits, installs or commits in any repository.

## Context

The KI website repository (`/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info`) fails one check in its engineering audit (`ki repo audit --skill ki-engineering --repo <repo>`): DEPS-1, the dependency-age rule, which expects declared dependency updates to be adopted within 14 days of release. `@types/node` (wanting 26.6.5), `rumdl` (0.2.79) and Bun (1.4.3) are past that window. Every other site gate, test and audit passes, and tonight's documentation units have committed under this known failure. The website deploys on push to `main`. The repository's `package.json` scripts include `ki:deps:update`. The owner has excluded configuration changes and package releases from tonight's unattended window.

## Query

How should the DEPS-1 failure be cleared?

## Options (unranked)

- A separate small maintenance unit runs `ki:deps:update`, bumps the Bun pin, re-runs every gate and commits, at a time the owner chooses.
- Record an adoption deferral for these three updates, with a reason and an expiry, and leave the versions as they are for now.

## Report

Give your recommendation, its confidence (high, medium or low) and a one-line reason, plus any risk the other option avoids. Inspect the repository's `package.json`, lockfile, Bun pin and the engineering standard in `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/` as you see fit.
