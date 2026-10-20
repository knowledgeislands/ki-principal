# unpark-review - blind review of four queries

This is a blind review, to run on the strongest model at high effort, under Codex.

Do not read any file under `+/_WORK/` in any repository, any `queries.md` or `decisions.md`, any decisions log, or any run report, status file or prompt under `~/.local/state/ki/agents/`. You may read repository source, `.ki.toml`, `.githooks/`, workflows, roadmap records, Decision Records and harness skills and standards in the repositories named below. Make no edits, commits, launches or network calls. That means no Git fetch and no `gh` or GitHub API call, and you run `ki repo audit` only as a read.

For each query, choose an option or propose another. Give a confidence (high, medium or low), a one-line reason, and any conditions the choice depends on. If you find a claim in the Context false, say so and give the evidence.

All paths are under `/Users/krisbrown/workspaces/`. The repositories are `knowledge-islands/ki-agentic-harness` (the harness), `knowledge-islands/ki-principal`, `knowledge-islands/tools-ki`, `knowledge-islands/homebrew-tap`, `knowledge-islands/ki-specifications`, `equal-remedy/apps-dafacts.org`, `personal/apps-kris.me.uk` and `personal/acquire`.

## NO-GATE

**Context:** Five repositories have no package and commit a check-only pre-commit hook:

- apps-dafacts.org, apps-kris.me.uk and acquire declare `ki-repo-project` and run `ki repo audit --skill ki-repo --staged`.
- homebrew-tap runs two Ruby tests and then `ki repo audit --skill ki-repo-homebrew-tap --staged`.
- ki-specifications runs `ki repo audit --skill ki-repo-specifications --staged`.

The harness's ADR-KI-HARNESS-SKILLS-017 (`docs/decisions/`) puts a hook's existence with `ki-repo` and its content with the shape skills, and leaves the remaining shapes to gain content criteria later. `ki-repo-project`, `ki-repo-homebrew-tap` and `ki-repo-specifications` declare none, so these hooks meet `HOOK-1` (the hook exists) but nothing owns what they run.

A hooks design held outside these repositories gives package-less repositories one row: a staged audit over all declared skills, owned by `HOOK-1` alone. The Project hooks run `ki-repo` alone.

Harness record KI-HARNESS-GOV-225 (`docs/roadmap/`, hook content claims, in triage) has shape skills declare the hook lines they require, so the `ki` host (tools-ki KI-TOOL-KI-CLI-165) can compose hooks. Its boundary names five shapes, but not these three. Policy bars creating new work records.

**Query:** Where should the content of the five package-less gates be declared?

**Options:** (unranked)

- Leave the five hooks as they are, owned by `HOOK-1` alone, until someone takes up KI-HARNESS-GOV-225 on its current boundary.
- Declare the three content criteria now, ahead of KI-HARNESS-GOV-225, as standard and rubric text in the three shape skills under an owner instruction for a bounded change. KI-HARNESS-GOV-225 turns them into claims later.
- Widen KI-HARNESS-GOV-225's boundary to give claims and content criteria to `ki-repo-project` (the staged `ki-repo` audit as installed), `ki-repo-homebrew-tap` (its staged audit plus the Ruby tests) and `ki-repo-specifications` (its staged audit). Amend the design row to match, and leave the hooks as they are.
- Switch the three Project repositories to the design's staged audit over all declared skills, once it is checked to stay local and practical on acquire's preserved captures, and declare that as the Project gate.

## GFM-HOSTING-RULES

**Context:** GitHub reported that the owner's push to the harness bypassed the `main` rules, which require a pull request and the `build` check. Harness CI (`.github/workflows/ci.yml`) defines `build`.

The `ki-repo` standard leaves `main` open by default. A repository opts into protection with `branch-protection = true` under `[skills.ki-repo.checks]`. Audit check `BP-1` then expects a pull request, the `build` check and linear history, with admins not enforced. Only then does `ki repo conform` protect `main`.

The harness `.ki.toml` declares no override, and no other repository declares one either. `.github/workflows/update-ki-pin.yml` auto-merges the pin pull request only while `main`'s rules require status checks. Nobody has read the live ruleset.

**Query:** Should the harness declare its protected `main` so its declaration matches GitHub?

**Options:** (unranked)

- Remove the rule on GitHub to match the open-`main` default. The pin pull request then stops auto-merging.
- Add `branch-protection = true` under `[skills.ki-repo.checks]` in the harness `.ki.toml` and leave GitHub unchanged. The next audit with GitHub access confirms that the live rules match `BP-1`, before any conform.
- Declare the override and enforce the rule for admins too, so every harness change goes through a pull request.

## HARNESS-TRIAGE

**Context:** Eight harness records (`docs/roadmap/`) are in triage. Harness Now holds nine records, seven planned and two awaiting review. The owner has asked for roadmaps to go down, not up; caps for that are being designed. Proposed disposition per record:

- KI-HARNESS-GOV-189, move a thread between hosts: Next.
- KI-HARNESS-GOV-196, scratch output in temp: Now, written as the launcher's `$TMPDIR/ki-agents/<work>/<run>/`. The launcher already gives every run that path, and `ki agent close` empties it. The `ki-delegation` background-run standard still says `<primary checkout>/tmp/<run>/<name>/`, a rule the owner set on 15 October.
- KI-HARNESS-GOV-202, stable stats badge: Later.
- KI-HARNESS-GOV-204, quietening hook: stays in triage until the owner's evidence review on 24 October.
- KI-HARNESS-GOV-222, timeline and calendar skill: Later.
- KI-HARNESS-GOV-225, hook content claims: Next.
- KI-HARNESS-GOV-226, banner rendered glyphs: Now, a small wording change already decided.
- KI-HARNESS-GOV-227, storage declarations: Next; it blocks one Observatory phase.

**Query:** Should the eight harness triage records take the dispositions listed?

**Options:** (unranked)

- Adopt only KI-HARNESS-GOV-226 into Now, and leave the other seven in triage until the caps are set.
- Apply all eight as listed, with KI-HARNESS-GOV-196 amending the standard's temporary-output rule to the launcher's path.
- Apply them as listed, but keep the standard's `<primary checkout>/tmp/` rule and change the launcher to match it.

Give a per-record view wherever you differ from a listed disposition.

## PRINCIPAL-TRIAGE

**Context:** ki-principal record KI-PRINCIPAL-OPS-014 (`Streams/Roadmap/`) converts its links from wikilinks to GitHub-flavoured Markdown in reviewed batches, starting with a pilot. It carries the owner's decision of 19 October, and the owner said of the conversion, "it'd be good just to do it". It is in triage.

Its two blockers have landed:

- The harness GFM linking rules are on harness `main` (`af4cb478`).
- The `ki markdown gfm` converter is released in `ki` v0.12.0, which is the installed version.

ki-principal still pins `ki` v0.11.5 (`.github/ki-version`). A dry run found 29 unresolved and 5 ambiguous links, which need a decision at the pilot. ki-principal's roadmap holds two records in Now and one in Next.

**Query:** Should KI-PRINCIPAL-OPS-014 start now that both its blockers have landed?

**Options:** (unranked)

- Adopt KI-PRINCIPAL-OPS-014 into Next, and start it once the harness Now chain has drained.
- Leave it in triage.
- Adopt KI-PRINCIPAL-OPS-014 into Now for the pilot batch only, moving the `ki` pin to v0.12.0 first. The later batches wait on the pilot's evidence.

## Report

Write an owner report: Done (pick, confidence, reason and conditions per query), In Progress, Queries.
