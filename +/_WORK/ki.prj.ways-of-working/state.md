---
id: ki.prj.ways-of-working
state: with-worker
since: 2026-10-31T01:31:36Z
received: 2026-10-29T15:38:09Z
beat: 2026-10-31T01:31:36Z
mark: 2026-10-31T01:31:36Z
method_read: 6868da5a
---

# ki.prj.ways-of-working state

## Now

- Unattended window AWAY-31-OCT until 09:00 GMT Saturday 31 October 2026 (see decisions). 25 queries stay with Kris; none answered by the grant.

## Next steps

Window plan, in order:

1. **sync-all** (all workspace repositories; push tier; small to medium). Fetch every repository and fast-forward clean checkouts. Merge diverged ones, ki-principal first, in their own worktrees, then push fast-forward. Record each repository's `origin/main` and local `main` revisions before and after. Waits on nothing.
2. **embargo** (each territory's State of play `messages.md`; push tier; small). One IMPORTANT line per territory saying no changes until 09:00 GMT. Waits on sync-all.
3. **wow-tidy** (this package; push tier; small). Prune received reports and spent briefs under the existing rules, excluding the three private files, and close the stale runs. Waits on sync-all.
4. **survey** (ki-principal, read-only; small). List every Knowledge Islands work package's authorised, unblocked next steps as units, with repository, authority, tier, what each waits on and size, plus the excluded units with their reasons. Waits on sync-all.
5. **website-learn** (the Knowledge Islands website repository; push tier, no deploy; medium). Plain-English, feature-focused pages on the new capabilities. Waits on sync-all.
6. **Survey waves** (per the survey, at most about three runs at a time; push tier). Waits on survey.
7. **morning-summary** (this package; small). The plain-English capability summary. Starts about 08:15 GMT.

Excluded: every open-query decision, because silence is not consent. Also excluded: website publication, releases and installs, the Orca worker pilot (needs Kris watching), and other Capitals' package work.

## Held

- Preserve original model candidates, Tools retained refs and publication recovery evidence; reconcile published sources without overwriting unresolved overlaps or replaying stale trees. The named wow-publication recovery ref is absent from this checkout.
- Host-sync and other unchosen designs retain their decision stages; no executor, schedule or automatic takeover is selected.
- HNR remains excluded; Observatory appearance belongs to its own work. No release, deployment, installation, credential/provider operation, confidential publication, force/reset/stash or hook bypass is authorised here.
