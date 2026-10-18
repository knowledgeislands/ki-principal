# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › fable-opinion-1

**🤖 → 🧑 Handoff to supervisor · Run report at 06:06 BST · last mark 22:34 BST**

---

## Done

An advisory opinion only, on Claude Fable 5.1, on the four queries in the [tools-burndown run report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/tools-burndown.report.md). I read the report, its Queries in full, the three linked records, the Rig specifications they cite, the tools-ki release workflow, and the ways-of-working [decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md) from PRE-APPROVALS onward. I changed no file but this report and ran nothing that writes.

The pre-approvals I weighed against, in Kris's words of 18 October: FIX-RELEASE, "Yes, one fix release", taken as "one fix release (0.10.7) through Homebrew if the apply hits a ki bug, after checks pass; a second still asks"; KEEP-PUSHING, "keep pushing and pushing and get as much done as you can"; FABLE-OPINION, an opinion may stand as provisional approval, with npm or any public registry, a second fix release, force-push or history rewrite, other territories and ki-design reserved. The thread's RELEASE-NUMBER note renamed the fix release 0.11.1 after v0.11.0 shipped.

| Query | Recommended | Confidence | Inside the pre-approvals | Coordinator may approve tonight |
| --- | --- | --- | --- | --- |
| RIG-APPLY-LOCK | a) | medium | Yes, as local roadmap delivery against fixtures | Yes, provisionally, with no live apply or upgrade |
| TOOLS-RELEASE | a) | high | No: the fix-release trigger was not met | No, wait for Kris |
| HARNESS-PATHS | a), adoption and planning only | medium | Adoption yes; the migration and chezmoi change no | Adopt and plan provisionally; deliver nothing live |
| DESK-KIT-SOP | a) | high | Yes, housekeeping inside this Project | Yes, provisionally |

### RIG-APPLY-LOCK

- **Opinion:** a), a separate per-platform operation lock that wraps the reconciliation lock, confidence medium. RIG-ORCH-037 forbids a tool-only apply from taking the reconciliation lock, so b) would amend a conforming specification to solve a different problem, and c) leaves the defect [KI-TOOL-RIG-CORE-058](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-058-apply-lock-handler-history.md) was opened for, two native package managers running side by side. A wrapping lock also keeps the refuse-only boundary the record sets. Medium, not high, because one detail is unsettled: RIG-STATE-030 says an unattended upgrade "that dispatches work" writes the last-run report, and a refused run dispatches nothing, so writing a refused report replaces the previous real run's report. I would still record the refusal, so the wrapper reading the report sees why nothing ran, but the plan should amend RIG-STATE-030 alongside RIG-STATE-025 and say so.
- **Pre-approvals:** inside. It is roadmap delivery in a Knowledge Islands tools repository under KEEP-PUSHING, tested with isolated Bats against a fixture lock, with no release and no live run. It is not connection-critical: the lock guards Homebrew and mise, not a service critical for connection.
- **Tonight:** a coordinator may approve a) provisionally, on this opinion, with two conditions in the brief: no live `rig apply` or `rig upgrade` on either Mac, and the delivered record goes to Awaiting review, not accepted. The scheduled 08:30 `rig-update` job on sol runs the installed rig, not the checkout, so a lock defect in the checkout cannot reach it tonight.

### TOOLS-RELEASE

- **Opinion:** a), cut v0.11.1 only after Kris has reviewed [KI-TOOL-KI-CLI-144](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-144-older-runs-start-seen.md), [KI-TOOL-KI-CLI-142](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-142-preserve-harness-release-settings.md) and [KI-TOOL-KI-CLI-137](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-137-agent-run-tmp-home.md), confidence high. Releasing now gains nothing overnight: the -142 fix only helps once a live configuration rewrite runs on Terra and Sol, and that rewrite needs its own approval, which the record itself withholds. A release is also the least reversible step available tonight, and it would spend the only pre-approved fix release on a defect found on 16 October rather than keeping it for a bug the morning may surface.
- **Pre-approvals:** outside. FIX-RELEASE was conditional, "if the apply hits a ki bug", and the [migrate-apply report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/migrate-apply.report.md) records that apply hit no ki bug and no fix release was cut. The tools burndown's own work file also carries "ki release: due soon but only when Kris says". So v0.11.1 would be the one pre-approved fix release by number only; its trigger was never met. On the registry question: the tools-ki release workflow creates a signed GitHub release and dispatches the Homebrew tap. It has no npm or other package-registry publish step, and Kris named Homebrew as the fix-release channel and has distinguished it from npm before ("release tools-ki 0.10.3 (no npm)" on 14 October). Cutting v0.11.1 would therefore not breach the npm reservation, but that does not make it approved.
- **Tonight:** wait for Kris. Leave TOOLS-RELEASE open in the tools-burndown report for the morning. Everything else on tools-ki `main` can continue unreleased.

### HARNESS-PATHS

- **Opinion:** a), adopt [KI-TOOL-KI-CLI-143](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-143-separate-local-harness-paths.md) on a host-local file under ki's state directory, confidence medium. The state directory already holds host-local state (the local registry), the record's prerequisite -142 is delivered, and the defect is real: the chezmoi-managed `config.toml` carries two `[locals]` checkout paths today. Two refinements for the plan: the host-local file should be the single authority once migrated, with `config.toml` `[locals]` read only as one-time migration input and a warning while entries remain, because an indefinite "read first, then fall back" path is the compatibility tail the record warns against; and the plan should state what happens when the remembered checkout is absent on a host, refusing rather than guessing, as the record requires. Medium because the ownership model is a design choice Kris may want to see before code is written.
- **Pre-approvals:** split. Adopting and planning the record to Ready, and implementing it against isolated HOME and XDG fixtures, is roadmap work under KEEP-PUSHING. The migration itself is not: it rewrites live `config.toml` on both Macs and drops entries from the chezmoi source, and the decisions log holds chezmoi on hold tonight. Both need Kris.
- **Tonight:** a coordinator may approve adoption and planning provisionally, and may let the implementation proceed to Awaiting review on fixtures only, with the brief saying no live rewrite on any host, no chezmoi change, and no bootstrap run. If the run would rather not commit code before the model is confirmed, b) costs little, since nothing else waits on -143.

### DESK-KIT-SOP

- **Opinion:** a), ways of working adds the line to the Messages section of the territory work file, [KI > SoP](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/work.md), confidence high. That work is on hold, so `ki agent send` rightly refused, and the Messages section exists precisely so work on hold receives a line to act on at its next bootstrap. The line is small and fully reversible: drop the desk-kit lines from its next step 3, THREADS-ORPHANS and "KI > mics / webcams". b) only delays it with no benefit.
- **Pre-approvals:** inside. It is a note between two pieces of work in this Project's own folder, committed by explicit path, and Kris's ONE-PROJECT answer of 18 October routes every ways-of-working item through this Project.
- **Tonight:** a coordinator may do it provisionally now, logging it as "provisional, on Fable's opinion" and leaving the tools-burndown report's DESK-KIT-SOP tag open for Kris to confirm.

### The rest of the report

The tools-burndown report's provisional choices (the six parked mgit answers, the plan choices for the Rig and ki records, the -137 folder choices, the partial -134 and -058 deliveries and the `events.seen` move) raise no query; they are already recorded in their records for Kris's confirmation and none of them needs a release or a live run. The one item I would not let a coordinator touch is the live Dock run on sol for KI-TOOL-RIG-CORE-042, which the report rightly leaves with Kris.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- TOOLS-RELEASE stays with Kris in the tools-burndown report; nothing waits on it overnight.
- If the coordinator approves RIG-APPLY-LOCK or HARNESS-PATHS provisionally, each launch brief should carry the no-live-run conditions above, and the decisions log should record each as "provisional, on Fable's opinion".

## Queries

No outstanding queries.

### 🤖 → 🧑 Handoff to supervisor · since 06:06 BST

🧑 1 with you · 🏁 run finished

- [with you] fable-opinion-1 opinion, four queries answered · owner · since 06:06
- [committed] ki-principal, pushed
