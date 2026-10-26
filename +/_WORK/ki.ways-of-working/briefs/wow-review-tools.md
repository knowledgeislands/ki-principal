# wow-review-tools

You are a blind reviewer. Give an independent recommendation on one query. Do not read `+/_WORK/ki.ways-of-working/queries.md`, `decisions.md` or any report there. You may read repositories under `/Users/krisbrown/workspaces/` read-only to check facts. Change nothing.

## Context

A run is converging every Knowledge Islands repository on the canonical pre-commit hook, which is now check-only (lint-staged with Biome, rumdl, syncpack and commitlint, run from `node_modules/.bin`). Three package repositories, `humans-not-robots/hnr-principal`, `legal/legal-principal` and `techmedix/apps-yorkphotosoc.org`, have some or none of those tools in `node_modules/.bin`, so the canonical hook would refuse every commit there; the run therefore skipped them. Each repository pins these as development dependencies in its lockfile; `bun install --frozen-lockfile` would populate `node_modules` from the lockfile without changing it. The owner's standing rule is "we should never install new software"; upgrading existing tools is fine. hnr-principal was being changed by another session during the run. apps-yorkphotosoc.org and the `acquire` repository also have GitHub settings that fail the conform's live-state checks, which withholds conform's writes until the settings are aligned (aligning GitHub settings is permitted). A second convergence will happen after the next `ki` release in any case.

## Query

Should a follow-up run populate `node_modules` from the lockfile in those three repositories and then converge their hooks?

## Options (unranked)

- Leave them until the second convergence after the next `ki` release.
- Yes, run `bun install --frozen-lockfile` in all three now and converge their hooks.
- Yes, but only after hnr-principal's other session has finished, and as part of the second convergence.

## Report

Owner report. Under Queries give one query, MISSING-TOOLS, with your recommended option first as `a) (recommended, confidence <level> - <reason>)`, then the others. Say whether a frozen-lockfile install falls inside or outside "never install new software" in your reading, and note any fact in the Context you found to be wrong.
