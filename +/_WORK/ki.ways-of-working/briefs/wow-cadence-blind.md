# wow-cadence-blind

## Goal

Masked blind review of two linked questions before Kris sees them. Give your own recommendation for each, with a confidence (high, medium or low) and a one-line reason. Do not read any `queries.md`, `decisions.md`, report or design note in any work package.

## Read

Only: in ki-agentic-harness, `skills/change-management/ki-coordination/references/standards-coordination.md` sections Committing the work folder and Pushing beneath other sessions.

## Context

Kris, 25 October 01:30 BST: "when there's a lot of changes in the work folder, the work is sitting there for a while and it's not getting committed. This makes it really difficult to keep the Git repositories in sync with the origin and other things which are also modifying the work packages because it's not regularly getting updates, pushes, and pulls." Today the standard requires a coordinator to commit and push its work folder only at a send, an owner receive, a mark, a hold and finish; writes in between (message dispositions, queries, decisions, briefs, state changes) and heartbeat wakes are not covered. Separately, a session pushes only when its own commits alone are stacked (Kris, 14 October), and never pushes another session's stacked commits (Kris, 19 October). In a Capital, other sessions' stacked commits are usually only `+/_WORK/` changes (lines they route into another work's `messages.md`, or their own package), so the coordinator's push stalls until Kris pushes by hand.

## Questions (options unranked)

COMMIT-CADENCE: should a coordinator commit its work folder by explicit path at every write to it and at every wake, pulling with rebase first and pushing fast-forward, so no write stays uncommitted past the turn that made it? Options: (i) yes, adopt that cadence in the standard, the output style and the hook line; (ii) leave the standard's send/receive/mark/hold cadence as it is.

PACKAGE-PUSH: may a session push a fast-forward stack in which other sessions' commits touch only paths under `+/_WORK/`, keeping the own-commits-only rule for every other stacked commit? Options: (i) yes, for `+/_WORK/`-only commits, never forced; (ii) no, keep own-commits-only pushing for everything.

## Rules

Read only; write nothing in any repository; no network calls; launch no agents. Report in the owner-report shape with one query per question, your recommendation as a), and the banner.
