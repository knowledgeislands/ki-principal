# wow-external-limits - external systems in a window, and confidential never public

## Goal

Write two decisions Kris made on 2026-10-25 into `ki-delegation` in the KI Agentic Harness. They settle UNWRITTEN-RULES-DRAFTS and UNWRITTEN-RULES-CONFIDENTIAL.

1. **External systems in an unattended window.** Kris: "[it's] saying [we] shouldn't [have] effects on other systems [or] messaging around us ... like GitHub, [for] example, [are expressly included] but [we] shouldn't [be] making changes [in] Linear [or] Notion unattended unless expressly agree[d as] part [of the] piece [of] work." Write it as a window rule: an unattended window makes no change in a system other people see or rely on, and sends no message to the people around us, unless that is expressly agreed as part of the piece of work. Name Linear, Notion and Slack as examples. GitHub, and the systems the window's work is expressly about, stay allowed. Reconcile it with the deny list's existing "messages to people or new publication" line. It does not apply to attended turns.
2. **Confidential is never made public.** At any time, attended or not: a site, repository or note marked confidential is never made public without Kris's go in the thread. Changing visibility can't be undone once crawled. Write it into the authority tiers.

## Do

- Work in `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`, starting after wow-unattended-limits has pushed. That run rewrites the same deny list with a criticality test, so build on its wording. Pull first, use a clean temporary clone or the primary checkout if it is clean, update the rubric, examples and generated surfaces the change reaches, and run the tests and audits until they pass.
- Commit by explicit path as Conventional Commits ending with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`, pull with rebase and push fast-forward only.
- Append one REFRESH line naming the revision and both rules to `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/messages.md`. Find HNR's State of play `messages.md` under `/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/+/_WORK/` and append one line there asking HNR to list its confidential sites in hnr-principal's AGENTS.md under the new rule. Commit and push each by explicit path.

## Do not

Change any other standard or any setting, release anything, force-push, use `--no-verify`, or touch another session's uncommitted files.

## Report

The owner report: Done with commits and checks, In Progress, and Queries, each with Context, Query and Options, the recommended option first with its confidence and reason.
