# KI > Techne > Agora › ki-portal-create

**🤖 → 👤 Handoff to supervisor · Run report at 05:20 GMT · last mark 00:04 GMT**

---

## Done

- Created the private repository `krisb/ki-portal` with the exact command in the brief, and cloned it to `~/kis/personal/ki-portal`.
- Set it up as a KI repository titled `ki-portal` (code `PERSONAL-PORTAL`, Capital `personal-principal`, Claude Code, private, same harness as the inbox). Added a README covering the planar portal, the three portals, the watchman, one portal per person and where the protocol is drafted; an AGENTS.md in the inbox's shape; and the files the audit requires (CLAUDE.md, LICENSE, ignore and editor settings, commit hooks, the `+/` and `-/` areas). No code and no work package. Commit `b0f09fe`. The audit passes on everything local; the only failures left are the GitHub settings below.
- Registered it in the Personal territory with one line in the Capital's member list (`personal-principal/.ki.toml`), the same place the inbox is listed. Commit `61fb3099`; scoped audit has no failures, and the membership check now passes in ki-portal.
- Sent `MSG-e65211b1` to [personal.reg.household-terra](/Users/krisbrown/.local/share/chezmoi/+/_WORK/personal.reg.household-terra/messages.md)'s Inbound, asking terra to clone `krisb/ki-portal` to `~/kis/personal/ki-portal`, commit after checks and push. Commit `9340e84` in chezmoi; scoped audit, tests and Markdown lint passed.
- The README names the three portals as **island portal** (on each island's summit), **principal portal** and **planar portal**. That follows Kris's later naming (PORTAL-NAMES, about 05:30 GMT, in [the decisions log](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.agora/decisions.md)), which renamed "summit portal" after this brief was written.

## In Progress

- Nothing. Terra's clone waits on its household session.

## Queries

### KI-PORTAL-GH - GitHub settings the audit wants

**Context**

The audit still fails on settings held on GitHub itself. The brief allowed no settings change: merge methods should be squash only with branch auto-delete; Issues and Projects should be off; Dependabot alerts and security updates should be on; "always suggest updating pull request branches" should be on.

**Query**

Should a follow-up run bring ki-portal's GitHub settings into line?

**Options**

a) (recommended, confidence high - the same baseline as every other KI repository, and nothing depends on the current defaults) Yes: a short run applies exactly these settings with `ki repo conform` or `gh`.

b) No: leave the defaults and accept the audit failures for now.

### KI-PORTAL-MGIT - The workspace manifest

**Context**

The inbox is also listed in the Personal workspace manifest (`.mgit.toml` under `~/kis/personal`, kept by chezmoi as `kis/personal/dot_mgit.toml`). That manifest lets each rig clone its members. The brief asked for one entry in one place, so I left it alone.

**Query**

Should ki-portal be added to the workspace manifest too?

**Options**

a) (recommended, confidence medium - so later rigs clone it with the other Personal repositories; it is a chezmoi change, so it needs the household's diff review) Yes: ask the household on sol to add it.

b) No: the Capital's member list is enough.

## New and noteworthy

- The planar portal now has its own island: `krisb/ki-portal`, kept by the watchman, registered in Personal and published.
- Terra has been asked to clone it, so both planes will soon hold the portal.

🧵 ki.prj.agora
