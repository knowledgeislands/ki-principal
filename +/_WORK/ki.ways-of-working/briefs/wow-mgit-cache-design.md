# wow-mgit-cache-design - design a short-lived result cache for mgit

## Goal

Kris on 2026-10-25, an idea for in due course: "when you do git commands often, especially on large sets, there's almost a wish to ... use some kind of cache mode ... if I could do an git st followed by an git push, realistically speaking, I just got the latest status ... mgit --to-cache st && mgit --from-cache push ... say there was 17 repos and only 3 of them had non-standard status responses, they would be added to the cache list as the candidates, and then effectively the from cache on the second request is filtering the push to just those repositories ... the cache should not last more than 5 minutes ... if the cache [has] expired ... you can still do [mgit st] and it works as standard ... if you've got an idea around how that could work or be improved on it, you could do a bit of a design mode on that."

Shape it under `ki-work-design` into `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/mgit-cache.md`: the problem, Kris's proposal, and real alternatives, for example a local ahead-of-upstream check inside `push` that needs no cache, named result sets, cache keying by command and repository set, invalidation by HEAD or index change, what happens when the cache has expired under `--from-cache`, and how agents as well as Kris would use it. Get one independent review on a different runtime, merge it, and end with a recommendation and the queries Kris must answer.

## Do

- Read `/Users/krisbrown/workspaces/knowledge-islands/tools-mgit` (its README, commands and options, tests, any roadmap) read-only to ground the design in how mgit works today. Change nothing there.
- Commit the design note by explicit path in ki-principal as `docs(work): ki.ways-of-working mgit cache design` ending with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`, pull with rebase, push fast-forward only.

## Do not

Change `tools-mgit` or send it any message, change any other file, force-push, use `--no-verify`, or touch another session's uncommitted files.

## Report

The owner report: Done, In Progress, Queries with Context, Query and Options, recommended first with confidence and reason.
