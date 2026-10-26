# wow-roadmap-sweep

## Goal

Kris wants the Knowledge Islands roadmap brought down to next to nothing within the next few hours, and needs one good review of everything outstanding to do it. Produce that review as a decision pack Kris can go through quickly, with bulk decisions. Read-only except the pack itself. Aim to finish within about 60 minutes; give a progress line every few minutes.

Kris on 26 October 2026, 23:40 GMT: "I'm still really wanting to get the Knowledge Island stuff roadmap down to next to nothing ... So I'm wondering how I can really get a good review of everything that's outstanding ... the observatory is a bit of a mess, it's got far too many sections ... It needs to be finished in the next few hours ... we need to be less concerned with doing releases of the libraries ... or the tools, because ultimately they're not ready yet, and everything should be linked locally ... we should just be running locally. If it's down to the CI builds, I'd rather it disabled them for now".

## Scope

- Every open work record in the Knowledge Islands territory: ki-principal `Streams/Roadmap/`, and the roadmap of every KI repository the registry lists (at least ki-agentic-harness, tools-ki, ki-specifications, apps-knowledgeislands.info, apps-observatory.local, ki-design, ki-techne-harness, tools-techne, tools-mgit, tools-rig, homebrew-tap and the `mcp-*` repositories under `/Users/krisbrown/workspaces/knowledge-islands/`). Use `ki work status` where it helps, and read the records themselves for status and last change. Read the [Techne Programme Focus](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Policies/Techne%20Programme%20Focus.md) first: Techné work outside it is an idea, not live work.
- Open queries in KI work packages (`+/_WORK/*/queries.md` in ki-principal and any KI repository): a count per package, naming only the queries that block a roadmap record.
- Releases and CI: list every record or query that waits on a `ki` release, a tap update, a `KI_VERSION` pin or a red CI check, and for each say what running locally (the local harness and tools-ki checkouts, `ki` linked to them) would do instead. Say which CI workflows in KI repositories currently fail or gate anything, and what disabling them would lose (the full `ki repo audit` moved from the commit hook to CI tonight, harness d174adbc).

## The pack

Write `+/_WORK/ki.ways-of-working/design/roadmap-sweep.md`. Open with the totals per bucket and per repository. Then one section per bucket, each a table with: full record ID linked to its local file by absolute path, title, repository, proposed disposition, one-line reason. Every record goes in exactly one bucket:

- A. Already done: accept and close now (`ki-accept`).
- B. Obsolete, superseded, duplicate, or outside the Techne Programme Focus: cancel, or keep as an idea only.
- C. Small and agent-doable tonight with no decision needed (under about an hour each); group them into suggested runs, one per repository.
- D. Needs one decision from Kris: the question in one line with a recommended answer and confidence.
- E. Waits on a release or CI: the local alternative, or drop the dependency.
- F. Genuinely larger: defer to Later with one line why.

End each bucket with a one-line bulk decision Kris can say, such as "accept bucket A as listed". Then a short section on releases and CI with options for Kris (keep CI, make it non-blocking, or disable workflows for now), recommended first with confidence. Keep it scannable: no prose padding.

## Authority

Read anything under `/Users/krisbrown/workspaces/`. Change no record, repository setting or workflow; send no message. Commit only the pack, by explicit path, with `docs(work): ki.ways-of-working roadmap sweep`; pull with rebase, push fast-forward only, never force or `--no-verify`. Other sessions commit in ki-principal: leave their files alone.

## Report

Owner report: Done (the totals and the pack's path), In Progress, Queries (only anything that blocks the pack itself).
