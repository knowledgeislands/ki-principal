# Unparked queries, 20 October 2026

Kris unparked five queries at 02:55 BST: NO-GATE, PKGLESS-GATE, GFM-HOSTING-RULES, HARNESS-TRIAGE and PRINCIPAL-TRIAGE. The unpark-draft run checked each against local state at 02:56 BST, with no network calls, and drafted the live ones below in owner-report shape.

## Check against current state

- **NO-GATE**: partly overtaken. ki.tools-burndown applied a) at 00:21 BST after qreview9, so all three repositories already commit the staged, check-only `ki repo audit --skill ki-repo` pre-commit hook (apps-dafacts.org `c946b73`, apps-kris.me.uk `a5104b6`, acquire `33b4244`, all from 00:32 BST). What is left is declaring a content owner for that gate in the harness, which ki.tools-burndown sent to this work. It is redrafted below as that residual question.
- **PKGLESS-GATE**: partly overtaken, and taken with NO-GATE. ki.tools-burndown took a) after qreview10 and kept the homebrew-tap and ki-specifications gates; their shape ownership came to this work with NO-GATE. It is folded into NO-GATE below, and answering NO-GATE answers it.
- **GFM-HOSTING-RULES**: live. The harness `.ki.toml` still declares no `branch-protection`. One correction to the earlier draft: the override key lives under `[skills.ki-repo.checks]`, not `[skills.ki-repo]`.
- **HARNESS-TRIAGE**: live. All eight records are still `triage` on harness `main` (`b852835a`), which now includes lane-triage and ci-green. Three more triage records have arrived since; they are outside this query.
- **PRINCIPAL-TRIAGE**: half overtaken. [KI-PRINCIPAL-GOV-035 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/a54cd93183e931cd0f302cbf330384a7cbcf36eb/Streams/Roadmap/KI-PRINCIPAL-GOV-035-turn-the-techne-programme-hold-into-a-focus-rule.md) was accepted at 00:30 BST and pruned at 02:02 BST (`e6d04024`), so its prune half is done. Both blockers on [KI-PRINCIPAL-OPS-014](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md) have also landed since the query was written, which changes the recommendation.

## Blind review status

- NO-GATE was blind-reviewed by qreview9 (00:19 BST), which agreed a) at medium. PKGLESS-GATE was blind-reviewed by qreview10 (01:53 BST), which agreed a) at medium; ki.tools-burndown logged that as reviewed high. Both reviews covered the earlier question, which was whether to install the hooks. The residual question below, where the content owner is declared, has not been reviewed, so it goes in `briefs/unpark-review.md` too.
- GFM-HOSTING-RULES, HARNESS-TRIAGE and PRINCIPAL-TRIAGE have not been reviewed. All three go to unpark-review.

## Queries

### NO-GATE - Name an owner for the package-less commit gates (takes PKGLESS-GATE with it)

**Context:** Five repositories have no package and now commit a check-only pre-commit hook:

- apps-dafacts.org, apps-kris.me.uk and acquire declare `ki-repo-project` and run `ki repo audit --skill ki-repo --staged`.
- homebrew-tap runs its two Ruby tests and then `ki repo audit --skill ki-repo-homebrew-tap --staged`.
- ki-specifications runs `ki repo audit --skill ki-repo-specifications --staged`.

[ADR-KI-HARNESS-SKILLS-017](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-017-commit-gate-existence-and-content-are-owned-separately.md) puts a hook's existence with `ki-repo` and its content with the shape skills. It leaves the remaining shapes to "gain content criteria as follow-ons". None of `ki-repo-project`, `ki-repo-homebrew-tap` or `ki-repo-specifications` declares one yet, so these five hooks meet `HOOK-1` (the hook exists) but nothing owns what they run.

Section 2.2 of the [hooks-standard design](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/design/hooks-standard.md) gives these repositories one row: a staged audit over all declared skills, owned by `HOOK-1` alone. The Project hooks actually run `ki-repo` alone, so the design and the installed hooks disagree.

[KI-HARNESS-GOV-225](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-225-hook-content-claims.md) (hook content claims, in triage) has each shape skill declare the hook lines it requires, so that the `ki` host ([KI-TOOL-KI-CLI-165 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/fde00e97/docs/roadmap/KI-TOOL-KI-CLI-165-hook-composition-claims-host.md)) can compose hooks. Its boundary names five shapes, but not these three. CAPTURE-GATE bars new records.

**Query:** Where should the content of the five package-less gates be declared?

**Options:** a) (recommended, confidence medium - it uses an existing record and keeps the installed hooks, but the narrower Project scope is still unreviewed against the design's all-skills row) Widen KI-HARNESS-GOV-225's boundary to give claims and content criteria to `ki-repo-project` (the staged `ki-repo` audit as installed), `ki-repo-homebrew-tap` (its staged audit plus the Ruby tests) and `ki-repo-specifications` (its staged audit). Amend section 2.2 of the design to match, and leave the five hooks as they are. b) Declare the three content criteria now, ahead of KI-HARNESS-GOV-225, as standard and rubric text in the three shape skills under an owner instruction for a bounded change. KI-HARNESS-GOV-225 then turns them into claims later. c) Switch the three Project repositories to the design's staged audit over all declared skills, once it is checked to stay local and practical on acquire's preserved captures, and declare that as the Project gate. d) Leave the five hooks as they are, owned by `HOOK-1` alone, until someone takes up KI-HARNESS-GOV-225 on its current boundary.

### GFM-HOSTING-RULES - Declare the harness's protected `main` to match GitHub

**Context:** GitHub reported that Kris's harness push bypassed the `main` rules, which require a pull request and the `build` check. The harness CI defines `build`, its only job, which runs on pushes to `main` and on pull requests, so the rule and CI agree.

The `ki-repo` standard leaves `main` open by default. A repository opts into protection with `branch-protection = true` under `[skills.ki-repo.checks]`. Audit check `BP-1` then expects a pull request with no approvals required, the `build` check and linear history, with admins not enforced, so Kris's bypass is by design. Only then does `ki repo conform` protect that `main`.

The harness `.ki.toml` declares no override, so on paper its `main` is open, while GitHub enforces rules. No repository in the estate yet declares the override. The harness's `update-ki-pin.yml` auto-merges the `ki` pin pull request only while `main`'s rules require status checks. Nobody has read the live ruleset, because that needs a network call.

**Query:** Should the harness declare its protected `main` so its declaration matches GitHub?

**Options:** a) (recommended, confidence medium - CI, the standard and the pin workflow were checked directly; the live ruleset was not read) Add `branch-protection = true` under `[skills.ki-repo.checks]` in the harness `.ki.toml` and leave GitHub unchanged. The next audit with GitHub access confirms that the live rules match `BP-1`, before any conform. b) Remove the rule on GitHub to match the open-`main` default. The pin pull request then stops auto-merging. c) Declare the override and enforce the rule for admins too, so every harness change, Kris's included, goes through a pull request.

### HARNESS-TRIAGE - Dispositions for the eight ki-agentic-harness triage records

**Context:** lane-triage adopted eight harness records into Now under TRIAGE-ALL and proposed dispositions for the other eight. All eight are still in triage on harness `main`. Harness Now holds nine records: seven drafts that ci-green planned, plus [KI-HARNESS-GOV-219](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-219-feedback-work-folder-kind.md) and [KI-HARNESS-GOV-224](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-224-diagram-viewer-receipts.md) awaiting review. Kris's FINISH-FIRST direction (02:38 BST) asks for roadmaps going down; its caps are still being designed. Proposed disposition per record:

- [KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md), move a thread between hosts: Next. Queue export and host-bound agents are still open, and it does not block the Mac Studio setup.
- [KI-HARNESS-GOV-196](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-196-scratch-output-in-temp.md), scratch output in temp: Now, written as the launcher's `$TMPDIR/ki-agents/<work>/<run>/`. The launcher already gives every run that path, and `ki agent close` empties it. The `ki-delegation` standard still says `<primary checkout>/tmp/<run>/<name>/`, which Kris set on 15 October, so the record would amend that rule.
- [KI-HARNESS-GOV-202](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-202-skill-area-stable-stats-badge.md), stable stats badge: Later. It is cosmetic, and it is unclear whether the viewer needs a change.
- [KI-HARNESS-GOV-204](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-204-pretooluse-quietening-hook.md), quietening hook: stays in triage until Kris's evidence review on 24 October.
- [KI-HARNESS-GOV-222](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-222-timeline-and-calendar-skill.md), timeline and calendar skill: Later. It is large, and where it lives and where it is served are still open. The HANDOFF-GOV-222 shaping text goes in with the next harness delivery run, and the skill name stays with Kris.
- [KI-HARNESS-GOV-225](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-225-hook-content-claims.md), hook content claims: Next. Planning decides whether the contract belongs in KI Specifications; NO-GATE a) widens its boundary.
- [KI-HARNESS-GOV-226](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-226-banner-rendered-glyphs.md), banner rendered glyphs: Now. It is a small wording change in the Banner section, and BANNER-GLYPHS a) is decided.
- [KI-HARNESS-GOV-227](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-227-repository-storage-declarations.md), storage declarations: Next. The schema is still to be designed, and it blocks one Observatory phase.

Not in this query: [KI-HARNESS-GOV-228](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-228-home-work-spec.md), [KI-HARNESS-GOV-229](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-229-home-acquire-spec.md) and [KI-HARNESS-GOV-230](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-230-knowledge-package-skill.md). They arrived in triage at 01:15 BST from ki.portable-specifications' HOMING-REVIEW a), and that work disposes them.

**Query:** Should the eight harness triage records take the dispositions listed?

**Options:** a) (recommended, confidence medium - each medium disposition rests on that record's own open questions, and GOV-196 reverses a rule Kris set) Apply all eight as listed, with KI-HARNESS-GOV-196 amending the standard's temporary-output rule to the launcher's path. b) Apply them as listed, but keep the standard's `<primary checkout>/tmp/` rule and change the launcher to match it. c) Adopt only KI-HARNESS-GOV-226 into Now and leave the other seven in triage until the FINISH-FIRST caps are set.

### PRINCIPAL-TRIAGE - Start the ki-principal GFM conversion

**Context:** [KI-PRINCIPAL-OPS-014](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md) converts ki-principal's links from wikilinks to GitHub-flavoured Markdown in reviewed batches, starting with a pilot of Resources, Calendar, the root and the `-` area. It carries Kris's "Do all recommended" of 19 October, and Kris said of GFM, "it'd be good just to do it". It is still in triage.

When lane-triage proposed Next, two blockers in other repositories stood in its way. Both have now landed:

- The harness GFM linking rules and exact-case link audit are on harness `main` (`af4cb478`).
- The `ki markdown gfm` converter ([KI-TOOL-KI-CLI-162 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/a9d46d49c81ccb02c865af41f92782e7f56440a1/docs/roadmap/KI-TOOL-KI-CLI-162-gfm-converter.md)) was accepted and released in `ki` v0.12.0, which is the installed version.

ki-principal still pins `ki` v0.11.5. Its dry run found 29 unresolved and 5 ambiguous links that need a decision at the pilot. ki-principal's roadmap is small: two records in Now and one in Next. The other half of the original query, pruning KI-PRINCIPAL-GOV-035, has already been done.

**Query:** Should KI-PRINCIPAL-OPS-014 start now that both its blockers have landed?

**Options:** a) (recommended, confidence medium - both blockers were verified landed and Kris wants it done, but the pilot's open links need decisions and the FINISH-FIRST caps are not yet set) Adopt KI-PRINCIPAL-OPS-014 into Now for the pilot batch only, moving the `ki` pin to v0.12.0 first. The later batches wait on the pilot's evidence. b) Adopt KI-PRINCIPAL-OPS-014 into Next, and start it once the harness Now chain has drained. c) Leave it in triage.
