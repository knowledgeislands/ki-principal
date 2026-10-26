# wow-review-naming

You are a blind reviewer. Give an independent recommendation on one query. Do not read `+/_WORK/ki.ways-of-working/queries.md`, `decisions.md` or any report there. You may read repositories under `/Users/krisbrown/workspaces/` read-only to check facts. Change nothing.

## Context

Humans Not Robots (HNR), one territory of the Knowledge Islands estate, renamed its nine site repositories on 26 October 2026 from host order to reverse-domain order, for example `apps-bbc.humansnotrobots.be` → `apps-be.humansnotrobots.bbc`, so that sites sort by domain. Hostnames, Cloudflare Worker names, work ids and record prefixes did not change. HNR now proposes `apps-<tld>.<domain>.<sub>` as the estate-wide Knowledge Islands convention and asks that the proposal go to the other territories.

The other territories' site repositories still use host order, for example `apps-knowledgeislands.info`, `apps-observatory.local`, `apps-kris.me.uk`, `apps-midnight.ninja`, `apps-rig.midnight.ninja`, `apps-vallearmonia.com`, `apps-dafacts.org`, `apps-yorkphotosoc.org`. Each repository has a checkout on two machines, an entry in the local registry, and in most cases a Cloudflare build connected to the GitHub repository. A rename touches GitHub, both checkouts, the registry and possibly the Cloudflare connection; the owner's standing limit is never to make a change that could take a site down. Territories own their own repositories; a convention lives in the harness `ki-repo` standard, and a proposal reaches a territory as a message line its State of play acts on.

## Query

Should Knowledge Islands adopt reverse-domain site repository names as its convention, and what should happen to the other territories' existing site repositories?

## Options (unranked)

- Decline: keep host-order names as the convention; HNR's renames stand as HNR's local choice.
- Adopt as the convention and send each territory a line to rename its existing site repositories now.
- Adopt as the convention for new site repositories, record it in the `ki-repo` standard, and send each territory the proposal as a message, leaving any rename of its existing repositories to that territory's own decision, with no change to DNS, Cloudflare or hostnames.

## Report

Owner report. Under Queries give one query, NAMING-TO-KI, with your recommended option first as `a) (recommended, confidence <level> - <reason>)`, then the others. Note any fact in the Context you found to be wrong.
