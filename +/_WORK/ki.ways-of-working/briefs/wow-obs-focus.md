# wow-obs-focus

## Goal

Kris is overloaded and wants one Observatory page to work from now. In `/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local`:

1. Move every existing tab, unchanged, under one "Legacy" area (a group, menu or second-level list, whatever the app's navigation makes simplest). Nothing is deleted or rewritten; every legacy view stays reachable and working.
2. Add one new page, first in the list and the default landing page, called "Focus" (or the nearest name that fits the app's vocabulary). It answers one question: what does Kris need to help with and respond to right now.

Kris, 27 October 2026: "can I have a new page at the front of the observatory list, which is allowing me to focus on what you need me to help with and respond to, and it allows me to almost do it through that interface, even if I have to pick the answers out of that and push them back into this prompt ... set those aside under an old tabs area ... I don't want to lose anything because I think there's value in what we built."

## The Focus page

Read only, plain language, short. Reuse the app's existing readers and contracts wherever they exist (work packages, `ki agent status`, roadmaps); add no new data model where an existing reader serves.

- **Questions for Kris:** every open query (under `## Open`, not `## Parked`) in each `+/_WORK/<id>/queries.md` across the registered repositories, grouped by work, the work with most open queries first. Each shows its tag, title and options, the recommended option first, with the full Context and Query behind a disclosure so the page stays calm.
- **Answer by copying:** beside each query, pick an option (and optionally a note), and the page builds a ready-to-paste answer line such as `NAMING-TO-KI a - <note>`. One "copy all answers" button gathers the picks grouped by work, so Kris can paste them into the coordinating thread. No file is written and nothing is sent; feedback sending stays off.
- **What's in flight:** a compact list of running and queued agent runs per work, and each work's state from `state.md` (who holds it, since when).
- **Waiting on review:** records awaiting acceptance, if the app already reads them; a count with links is enough.

Keep it to one screen where possible. No new charts.

## Bounds

Change only `apps-observatory.local`. Install no new software and add no new dependencies; upgrading nothing. No network-facing, DNS, Cloudflare, tailnet exposure or credential change. Follow the repository's own conventions, tests and `ki repo audit --repo .` with the linked `ki` before the final commit. If the app runs as a local service, restart or rebuild it the way the repository documents so the new page is live, and check it in the running app (load the page, confirm queries from `ki-principal/+/_WORK/ki.ways-of-working/queries.md` appear and the copy line forms). Commit by explicit path with Conventional Commits, pull with rebase, push fast-forward only, never force or `--no-verify`; leave other sessions' files alone.

Do not capture new roadmap records. The Observatory improvements from the recent review go to a holding area later, under a separate decision; do not touch them now.

## Report

Owner report: Done (what changed, the local URL of the Focus page, how it was checked), In Progress, Queries (only what blocks or needs Kris).
