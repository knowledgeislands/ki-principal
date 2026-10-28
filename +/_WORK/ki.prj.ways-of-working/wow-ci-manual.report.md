# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-ci-manual

**🤖 → 👤 Handoff to supervisor · Run report at 02:02 GMT · last mark 02:07 BST 25 October**

---

## Done

Applied RELEASES-CI option a, Kris's 27 October answer "as recommended": every CI and release workflow in the knowledge-islands checkouts now runs on `workflow_dispatch:` only. Existing dispatch inputs were kept; push, pull_request, tag, schedule, release and repository_dispatch triggers were removed. No pin bumped, no release cut, no GitHub setting, DNS, Cloudflare or credential touched. No site deploy workflow exists in these repositories, so none was changed.

One deviation from the brief: the commit subject uses the `chore` type, not `ci`, because every repository's own commit-msg hook (ki commitlint, type-enum chore, docs, feat, fix, refactor, test) rejected `ci` and `--no-verify` is forbidden. Subject used: `chore: run CI and release workflows on manual dispatch only`.

Each repository: one commit staged by explicit path, hooks passed, actionlint clean, pulled fast-forward and pushed to `origin/main`, level with remote at close.

- apps-knowledgeislands.info: changed, `06f322c` (ci.yml; update-tool-release.yml lost repository_dispatch, kept its dispatch inputs).
- apps-observatory.local: changed, `c3eb8b0` (ci.yml).
- homebrew-tap: changed, `fe65adc` (ci.yml kept its formula dispatch input; propose-tool-releases.yml lost repository_dispatch and the daily schedule).
- ki-agentic-harness: changed, `bc6873c4` (ci.yml; update-ki-pin.yml lost repository_dispatch and the daily schedule).
- ki-design: changed, `b77da38` (ci.yml, update-ki-pin.yml).
- ki-principal: changed, `235398d1` (ci.yml, update-ki-pin.yml); the 43 other uncommitted files in `+/_WORK/` and `ki-repo-tools.out` belong to other sessions and were not touched.
- ki-specifications: changed, `17dda1a` (ci.yml).
- ki-techne-harness: changed, `f2d93cf` (ci.yml, inline `on: [push, pull_request]` form).
- mcp-acquire-whatsapp: changed, `643c5de` (ci.yml, update-ki-pin.yml).
- mcp-git-audit: changed, `58ffe47` (ci.yml, update-ki-pin.yml).
- mcp-gsuite: changed, `be3636d` (ci.yml, update-ki-pin.yml).
- mcp-housekeeping-chatgpt: changed, `96d670f` (ci.yml).
- mcp-housekeeping-claude: changed, `d1a3639` (ci.yml, update-ki-pin.yml).
- mcp-ki-kb-fs: changed, `b989558` (ci.yml, update-ki-pin.yml).
- mcp-m365: changed, `78f43ad` (ci.yml, update-ki-pin.yml).
- tools-git-almanac: changed, `087154e` (ci.yml; release.yml lost its `v*.*.*` tag push; update-ki-pin.yml).
- tools-ki: changed, `900d2788` (ci.yml only; release.yml was already dispatch only).
- tools-mgit: changed, `0a4fc2c` (ci.yml; notify-homebrew-tap.yml lost its release-published trigger).
- tools-rig: changed, `4944b1b` (ci.yml lost push to main, `v*` tag push and pull_request; notify-homebrew-tap.yml lost its release-published trigger).
- tools-techne: changed, `0f19a28` (ci.yml only; release.yml was already dispatch only).
- paperclip: skipped, see PAPERCLIP-WORKFLOWS below.
- kw-website, packages-portal-commons: nothing to change, no workflows.

Workflows whose class I was unsure of, all changed under the brief's "CI and release" reading:

- `tools-rig/ci.yml` is CI and release in one file: its final job publishes on a `v*` tag (`startsWith(github.ref, 'refs/tags/')`). On dispatch it can still be run against a tag ref.
- `update-ki-pin.yml` (ten repositories), `propose-tool-releases.yml`, `update-tool-release.yml` and `notify-homebrew-tap.yml` are release receivers rather than release producers; the roadmap-sweep option a named them, so they went with it. The daily schedules on `propose-tool-releases.yml` and `update-ki-pin.yml` are gone.
- Dead guards remain in place: the `repository_dispatch` and `push` conditions inside `update-ki-pin.yml`, `propose-tool-releases.yml`, `update-tool-release.yml` and `homebrew-tap/ci.yml` now only ever see `workflow_dispatch`. actionlint accepts them; they were left rather than refactored.

## In Progress

Nothing is running.

## Queries

### PAPERCLIP-WORKFLOWS - whether the paperclip fork's upstream workflows are in scope

**Context:** `paperclip` is the knowledgeislands fork of the upstream Paperclip project, checked out on `ki/stable`, clean and level. Its `.github/workflows/` holds twenty upstream workflows (pr.yml, release.yml, docker.yml, e2e.yml, storybook-deploy.yml, runner evals and more), none of them KI-authored. Rewriting their triggers would put twenty edited upstream files on `ki/stable` and conflict at every upstream sync; the roadmap-sweep's option a counted thirteen `ci.yml` repositories and the pin and tap receivers, not this fork. I left it untouched.

**Query:** Should the paperclip fork's upstream workflows also be set to manual dispatch only?

**Options:**

a) (recommended, confidence high - the fork tracks upstream, the sweep's option a never counted it, and its workflows run in the knowledgeislands org only when the fork's branches are pushed) Leave paperclip's workflows as upstream ships them; disable Actions for that repository in GitHub settings instead if its runs are unwanted, as a separate decision since this run changes no GitHub settings.

b) Run a follow-up that sets all twenty paperclip workflows to `workflow_dispatch:` only on `ki/stable`, accepting conflicts at the next upstream sync.
