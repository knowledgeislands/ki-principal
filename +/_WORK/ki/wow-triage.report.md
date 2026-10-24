# [Knowledge Islands](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Charter.md) › State of play › wow-triage

**🤖 → 👤 Handoff to supervisor · Run report at 00:31 BST · last mark 23:46 BST**

---

## Done

- Brief overtaken: [ki.ways-of-working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/work.md) was already with its worker. At 00:23 BST Kris's "read messages" lifted the hold, and its queue was emptied then. Its own run, lane-triage (launched 00:24 BST, still running), has steps 2 to 4 of this brief: triage of the 17 lane records, delivery of [KI-HARNESS-GOV-219](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-219-feedback-work-folder-kind.md) and [KI-HARNESS-GOV-224](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-224-diagram-viewer-receipts.md) first, and the COORD-12 check for [KI-HARNESS-GOV-215](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-215-pmo-12-to-fail.md). I did not run them a second time, because two runs would have edited the same records. lane-triage's 00:29 BST milestone: the COORD-12 condition is met in all eight Capitals.
- WOW-RESUME a): Kris's 20 October words recorded in the package's [decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md), as already served by lane-triage. `state.md` stays with-worker, with a Now line and step 10 (receive lane-triage) added (`187a557c`, local, audit pass).
- NO-GATE: removed from `messages.md` at 00:23 BST with no disposition recorded. It is now the NO-GATE query in the package's [queries](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/queries.md), carrying qreview9's blind review at medium, so nothing was applied (`187a557c`).
- GFM-HOSTING-RULES: harness CI does define `build`, the only job in `.github/workflows/ci.yml`, which runs on pushes to `main` and on pull requests. The `ki-repo` protected-`main` set says "admins not enforced", so Kris's bypass is by design. But the harness `.ki.toml` does not declare `branch-protection = true`, and the pin auto-merge depends on the rule. I wrote this up as a query in the package (`187a557c`). GitHub settings unchanged, and no remote calls.

## In Progress

- lane-triage, ki.ways-of-working's run, holds the triage, GOV-219 and GOV-224 delivery to Awaiting review, the high-confidence adoptions and GOV-215's release. ki.ways-of-working receives it.
- Outstanding - no action requested now: GFM-HOSTING-RULES is medium and unreviewed, so it goes to one blind review before it reaches Kris. ki.ways-of-working's coordinator arranges that. No follow-up records proposed. Nothing pushed.

## Queries

### NO-GATE - Give the general Project shape a real commit gate

**Context:** apps-dafacts.org, apps-kris.me.uk and acquire declare `ki-repo-project` and have no package. HOOK-1 asks for a committed pre-commit gate, but the Project standard declares none. Section 2.2 of the hooks design names an audit over all declared skills instead. qreview9's blind review agreed a) at medium.

**Query:** Should the `ki-repo-project` shape declare a staged, check-only gate now, and which scope?

**Options:**

a) (recommended, confidence medium - reviewed by qreview9; a shape-owned baseline meets HOOK-1 with no dependencies, but its scope differs from the design's 2.2) Declare a staged, check-only `ki repo audit --skill ki-repo` as the `ki-repo-project` gate criterion in ki-agentic-harness, and amend section 2.2 of the hooks design to match before ki.tools-burndown installs it.

b) Adopt the design's staged audit over all declared skills as the Project gate, once it is checked to stay local and practical on acquire's preserved captures.

c) Keep the missing-hook warning until the Project shape declares a gate.

### GFM-HOSTING-RULES - Declare the harness's protected `main` to match GitHub

**Context:** GitHub reported that Kris's harness push bypassed its `main` rules (a pull request and the required `build` check). CI defines `build`, so the rule and CI agree. The `ki-repo` standard's protected set is a pull request with 0 approvals, `build`, linear history and admins not enforced, so the bypass is by design. The harness `.ki.toml` leaves `branch-protection` at its default, which is an open `main`. `update-ki-pin.yml` auto-merges only when `main` has required checks. I did not read the live ruleset.

**Query:** Should the harness declare its protected `main` so its declaration matches GitHub?

**Options:**

a) (recommended, confidence medium - CI and the standard were checked directly; the live ruleset was not read) Add `branch-protection = true` under `[skills.ki-repo]` in the harness `.ki.toml` and leave GitHub unchanged. The next audit with GitHub access then confirms the live set matches.

b) Strip the rule on GitHub to match the open-`main` default. This stops the pin pull request auto-merging.

c) Enforce the rule for admins too, so every harness change goes through a pull request.

### 🤖 → 👤 Handoff to supervisor · since 00:31 BST

🤖 1 running · 👤 2 with you

- [running] lane-triage · run/lane-triage · since 00:24
- [with you] NO-GATE · owner · since 00:31 BST
- [with you] GFM-HOSTING-RULES · blind review, then owner · since 00:31 BST
- [committed] ki.ways-of-working package, local
- [unpushed] ki-principal
