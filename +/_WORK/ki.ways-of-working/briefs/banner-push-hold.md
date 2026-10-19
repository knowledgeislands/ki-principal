# banner-push-hold

Run for ki.ways-of-working, authorised by Kris on 2026-10-19 at 23:22 BST:

> By the way, I'm sick and tired of having with me saying pushing stuff, right? That's not an issue. Can we get that removed? Why'd you need to put that against me? I can just push it. Also this is on hold, but it says on hold pushed to agentic harness. You're not on hold on if you're waiting on something.

## Rules

- PUSH-NOT-WITH-YOU: a push of stacked commits is never a "with you" item, count or query. It appears only as the `[unpushed]` housekeeping item; Done names the other sessions' stacked commits once, and Kris pushes when he likes. The coordinator still never pushes another session's commits.
- HOLD-CLEAN: an On hold banner lists nothing waiting: no "with you", running or per-repository status item (no "[on hold] committed and pushed in ..."). Its counts read `⏸️ drained · 🅿️ <n> queries parked`; its items are only `[parked]`, `[unpushed]` where true, and `[release]`. Per-repository outcomes stay in the hold report's Done.

## Task

1. Harness (`/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`): work in a fresh `git worktree`, never the main checkout, and fast-forward the main checkout only once everything passes. Change the `ki-coordination` standard (Banner, hold procedure, push wording such as PUSH-STACKED, Reply forms), the coordinator output-style source and its On hold example, and the hook line only if a clause there says the push is with the owner. Regenerate surfaces with the skill's generator against the worktree. Add test assertions. Tests, type check, audits; commit by path; pull with rebase, push fast-forward only when alone; remove the worktree.
2. ki-principal: if the Work Process note (`Pillars/Philosophy/Model/Processes/Work Process/Work Process.md`) Banner section carries a push-with-you item or the old On hold example, align it in one commit by explicit path (Kris's instruction stands in for an Enactment record). Do not push ki-principal.

Never `--no-verify` or force-push.

## Report

Commits, where each rule landed, checks, pushed or why not, queries with options.
