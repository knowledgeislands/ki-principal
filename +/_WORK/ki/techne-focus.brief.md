# techne-focus

Kris answered TECHNE-FOCUS a) on 19 October: revise the Techne Programme Hold policy through the Enactment Process into a focus rule. In Kris's words of 14 October: "the hold is gone, but for now we're only focusing on setting up and running the Mac Studio and the agent host [...] keep them as ideas". Kris approves the exact wording before anything canonical changes.

1. Read `Admin/Governance/Policies/Techne Programme Hold.md`, `Admin/Governance/Decisions/GDR-KI-PRINCIPAL-004-standing-agent-host-exemption-from-the-techne-programme-hold.md` and the Enactment Process.
2. State of play captures one Enactment record in `Streams/Roadmap/` through you, at Kris's request, under `ki-repo-kb-streams`. This is the only record you may create.
3. In that record, draft the exact replacement policy wording:
   - Mac Studio and agent host only, with all other Techné work kept as ideas.
   - Carry forward the hold's operating bounds: host scope, owner-opened sessions only, access controls, kill switch, teardown, protection of other remote services.
4. Also draft the wording of a successor Decision Record that supersedes GDR-KI-PRINCIPAL-004, under `ki-decision-records`.
5. Do not change the policy, the GDR, the Charter or any other canonical note. Commit the record only.
6. Raise one query, TECHNE-WORDING, that shows Kris the exact policy and GDR wording to approve.

## Rules

- CAPTURE-GATE (Kris, 19 October): create no roadmap record except one this brief names. List follow-ups in your report.
- HOOKS-MIGRATION: never run `ki repo conform` without `--dry-run`. Do not touch `package.json`, `bun.lock`, `.husky/` or `.githooks/`.
- Commit only your own changes, staged by explicit path under `ki-git`, using Conventional Commits and ending with "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>". Do not push. If another session has uncommitted changes in a file you need, leave that file alone and name it in your report.
- British English, ASCII hyphens only.
- Report to the path your run packet names, as an owner report: Done, In Progress, Queries. Each query needs Context, Query and Options, with a) recommended and its confidence.
