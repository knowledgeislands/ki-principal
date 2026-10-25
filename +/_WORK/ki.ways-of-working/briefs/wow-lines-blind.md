# wow-lines-blind

## Goal

Masked blind review of three questions before Kris sees them. Give your own recommendation for each, with a confidence (high, medium or low) and a one-line reason. Do not read any `queries.md`, `decisions.md`, run report or `design/` file in any work package.

## Read

Only: in ki-agentic-harness, the `ki-repo`, `ki-work-roadmap` and `ki-repo-kb-streams` standards; in ki-principal, `+/_WORK/ki.baseline-rollout/work.md` and `+/_WORK/ki.ways-of-working/work.md`.

## Context and questions (options unranked)

KI-REPO-HOME. A change to the `ki-repo` standard and checker is pending: hyphen-only `ki-` topics, `territory_code` and `territory_tag_types` keys, and wording for the 24-character `repo_code` cap, which today exists only in the shared identifier grammar. State of play queued it with ki.baseline-rollout, but that work's `work.md` puts harness skills and standards out of scope and gives them to ki.ways-of-working, whose scope is the work model, coordination, delegation and work-record standards. Nothing is blocked. Question: should ki.baseline-rollout carry `ki-repo` standard and checker changes, its Out line narrowed to the work-model skills; or should ki.ways-of-working carry it, widening its scope to the repository contract?

LEGACY-PREFIX. The streams audit and `ki-work-roadmap`'s checks fail every record not prefixed with the current `repo_code`, so a rename must move every record in one sweep; Personal is doing so now. Question: should a rename stay a documented one-sweep change in `ki-work-roadmap` (every record and in-repository reference in one commit, pruned links keeping pinned revisions); or should both audits and the tools-ki readers accept an optional list of former codes for existing records, new records taking the current code?

PARTIAL-REPOS. HNR keeps hnr-shared, holding only Pillars and Resources, beside hnr-principal. ZONE-1 requires all five zones and the registry binds one source store per declared repository, so hnr-shared cannot be declared and its store is invisible to the source audits. Kris asked Knowledge Islands to decide where partial repositories fit, and whether a person keeps a personal "work" knowledge base beside a company Capital, adding "there's [a] kind [of] weird thing here we maybe need to come back to". Question: should it wait as an idea on the Ways of working Project note until Kris opens it; or should a `ki-work-design` brief start now on partial repositories, the personal work knowledge base and the store-binding gap?

## Rules

Read only; write nothing in any repository; no network calls; launch no agents. Report in the owner-report shape with one query per question, your recommendation as a), and the banner.
