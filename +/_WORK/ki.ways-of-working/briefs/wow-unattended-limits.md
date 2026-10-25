# wow-unattended-limits - criticality test for unattended windows

## Goal

Write Kris's 2026-10-25 decision into `ki-delegation` in the KI Agentic Harness. It settles UNWRITTEN-RULES-CLOUDFLARE and UNWRITTEN-RULES-CONFIG. Kris's words: "the point here is to exclude certain things in unattended mode ... DNS, Cloudflare, configuration ... I'm happy ... to make any alignments to GitHub ... from a Cloudflare perspective, I'm happy for you to do anything to get the builds passing ... I'm happy for you to do releases ... So it's more like any critical things that might break, that I can't then reconnect or deal with sites that go down." On chezmoi: "we should have an extra judgmental check on it instead to make sure that we're making changes ... that we need to make". On libraries: "If we need to install a new version of a library ... such as our own releases, then [approval] doesn't need to happen." On confirming the read-back: "critically we should never install new software. We could upgrade existing ones, but never new software as well."

## The rule to write

Replace the unattended deny list's blanket line ("DNS, Cloudflare, GitHub settings, machine, scheduler, credential or connection-critical changes") with a criticality test:

1. **Never in a window:** any change that could cut Kris off or take a site down. That means DNS, Cloudflare Access, routes, Zero Trust, credentials, and connection-critical machine configuration. The existing restore-path rule for connection-critical work stays.
2. **Allowed in a window:** aligning GitHub settings with the declared standard; changing Cloudflare build settings to get builds passing; cutting releases under the repository's release process.
3. **chezmoi and dotfiles, attended or not:** a needed rollout goes ahead after an independent judgement check. That is a blind review of the `chezmoi diff` confirming each change is needed and safe, and it stands in for Kris's approval. Reconcile this with the machine grant's existing wording.
4. **Software:** upgrading an already installed library or tool, our own releases included, needs no check. No session ever installs new software.

Nothing else becomes a standing rule outside a window. Keep the existing grant structure and authority tiers, and change only what the rule above requires. Update the rubric criteria, examples and any generated surfaces (the ki-coordinator output style restates the window exclusions; regenerate it if its source changes).

## Do

- Work in `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`, starting after wow-perm-prompts has pushed: pull first, then use a clean temporary clone or the primary checkout if it is clean. Run the tests and audits until they pass.
- Commit by explicit path as Conventional Commits ending with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`, pull with rebase and push fast-forward only.
- Append one REFRESH line naming the revision and the change to `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/messages.md`, then commit and push it by explicit path.

## Do not

Change Claude Code or chezmoi settings, change any other standard, release anything, force-push, use `--no-verify`, or touch another session's uncommitted files.

## Report

The owner report: Done with commits and checks, In Progress, and Queries, each with Context, Query and Options, the recommended option first with its confidence and reason.
