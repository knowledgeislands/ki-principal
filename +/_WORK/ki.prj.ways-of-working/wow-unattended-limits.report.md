# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-unattended-limits

**🤖 → 👤 Handoff to supervisor · Run report at 08:31 GMT · last mark 02:07 BST**

---

## Done

- Harness `a122a201` writes UNATTENDED-LIMITS into `ki-delegation` and is pushed to `origin/main`: the unattended deny list's blanket line on DNS, Cloudflare, GitHub settings, machine, scheduler, credential and connection-critical changes, and its exclusion of releases, give way to a new Criticality test subsection (never in a window: anything that could cut Kris off or take a site down; allowed: aligning GitHub settings, Cloudflare build settings to get builds passing, releases under the repository process), with a new Dotfiles and software subsection holding the two rules that apply attended or not (chezmoi rollout after a blind review of the `chezmoi diff` standing in for Kris's approval; upgrades need no check; no session ever installs new software). Nothing else became a standing rule outside a window.
- The machine grant's "package install or update" is narrowed to an upgrade of an installed package, with a new line banning any new install and a line requiring the cited judgement check before a chezmoi or dotfile edit; the Grants table row matches.
- RUN-1's mechanical check now requires the machine grant's new-software ban and judgement-check wording, with a new test case; the rubric catalogue is regenerated and SKILL.md's rubric sentence names the check.
- The `ki-coordination` standard and the ki-coordinator output style needed no change: they cite the deny list by link only, and `ki dev skill generate ki-coordination` reports all seven surfaces in sync.
- Checks: `bun run test` 1469 pass, 0 fail; `bunx tsc --noEmit` clean; `ki repo audit --skill ki-delegation` PASS; `--skill ki-skills` and `--skill ki-repo-harness` PASS with only pre-existing fleet warnings (other skills' refresh cadence, diagram freshness), none on ki-delegation; the pre-commit hook passed on both commits.
- ki-principal `98911024` appends the REFRESH line for harness `a122a201` to `+/_WORK/ki/messages.md` and is on `origin/main`.
- The commit trailers name Claude Fable 5.1, the model that made the commits, under the standard's commit-trailer rule rather than the brief's Opus 5.5 wording.

## In Progress

Nothing is running.

## Queries

No outstanding queries.
