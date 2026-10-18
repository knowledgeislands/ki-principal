# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › skills-audit

**🤖 → 🧑 Handoff to supervisor · Run report at 05:04 BST · last mark 22:34 BST**

---

## Done

- I audited the skills in ki-agentic-harness at `80144e72`, read-only, against the work model in [GDR-KI-PRINCIPAL-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md) and the [Work Process](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) note. For each skill I asked whether its job is still needed, whether its name is right, and whether it overlaps another skill. I changed nothing in the harness or in tools-ki. The only commit is this report.
- This answers SKILL-NAMES, which Kris took on 18 October as "keep the skill names the same for now ... let's come back to the naming of the skills and the naming of the agents", and Kris's words on 18 October: "I'm wondering what the checkpoint one does anymore". It also answers WORKER-CLI, Kris's idea of 18 October that `ki agent` "should become KI worker", and UPDATE-SHAPE of 18 October, which left open whether ki-pmo should adopt the three-line update.
- Every skill I was asked to cover still does a job the work model needs. I found no skill to retire. The problems are names that come from the thread model, and three rules written out in two skills at once.
- Recommendations, one line each. The ones that need a decision are under Queries:

  | Skill or command | Recommendation | Confidence | Reason |
  | --- | --- | --- | --- |
  | [ki-pmo](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-pmo/SKILL.md) | Keep the job. Rename it `ki-coordination` | medium | "PMO" is not a word in the work model. Its standard already calls itself the "Coordinating-work standard", which pairs with `ki-delegation` |
  | ki-pmo reply forms and owner report | Keep them in ki-pmo for now | medium | Every session uses them, but moving them out now would churn the generated surfaces before the report-shape review around 21 October |
  | [ki-checkpoint](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-checkpoint/SKILL.md) | Keep the job. Rename it `ki-work-file` and make it the one owner of `+/_WORK/` | medium | It owns the work file that `ki work status` reads. "Checkpoint" now means only a move, and the ownership of the work folder is split across three skills |
  | [ki-delegation](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/SKILL.md) | Keep the job and the name. Cut it back to the run side | high (keep), medium (cut) | Its Decisions log section also holds the rules for pruning the work folder and closing finished work, which ki-pmo restates |
  | [ki-pmo-design](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-pmo-design/SKILL.md) | Keep the job. Rename it `ki-work-design` | low | It does not depend on ki-pmo, and it shapes work before any record exists. A `ki-design-*` name would clash with the website design skills |
  | [ki-repo-kb-streams](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-kb-streams/SKILL.md) | Keep it and slim it | medium | The container and the Enactment gate are real jobs. The PROPOSE, READY, ROLLOUT and ITERATE modes only point to ki-next, ki-plan and ki-implement, and its status table repeats ki-work-roadmap's |
  | `ki agent` and `ki worker` | Keep `ki agent` and drop the rename idea | medium | An agent is a party and a worker is a role. A coordinator is a worker that `ki agent` never launches, and `ki worker` would sit one letter from `ki work` |
  | `ki agent` help text | Correct it through a tools-ki trade | high | `decide` says it appends a "numbered ... owner decision" to "the thread's" log, which contradicts the rule that entries carry no numbers. `home` says "thread home" |
  | [ki-recap](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-recap/SKILL.md) | Keep it. Change `checkpoint <thread>` to `checkpoint <id>` | high | Only the argument uses the old word. The line between a single-session recap and ki-pmo's recap since the mark is clear |
  | [ki-batch](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-batch/SKILL.md) and `+/_BATCHES/` | Keep for now. Review it at the next mark | low | `+/_BATCHES/` is a second working area outside `+/_WORK/`, but its records carry authorisation evidence that its tests depend on |
  | [ki-subagents](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/agentic-systems/ki-subagents/SKILL.md) | Keep the name for now | low | The background-run standard says an "in-session subagent is not a background agent", which reads awkwardly next to a skill that defines subagent roles. That is worth a later look, not a rename now |
  | ki-trade and ki-trades | Keep both | medium | The split between a process skill and a governance skill is deliberate, and their descriptions tell them apart |
  | ki-pmo three-line update (UPDATE-SHAPE) | Adopt it for every coordinator | medium | Kris asked for it in plain terms, and nothing in it is specific to this Project |

- The three overlaps:
  - **Work-folder ownership.** ki-pmo owns the work folder, its closed list and its pruning. ki-checkpoint owns the work file and audits `+/_WORK/`. ki-delegation's Decisions log section repeats the pruning rule and the close-out. The [ki-pmo standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-pmo/references/standards-pmo.md) writes both out again, under Pruning the work folder and Finishing Project work.
  - **The decisions log.** ki-delegation holds the capture rules: log the decision in the turn it arrives, then verify it from the file. ki-pmo holds the decision classes and the life cycle. A coordinator has to read both skills to handle one log entry.
  - **Picking work up.** ki-checkpoint's RESUME mode and ki-pmo's "Picking work up" both describe pick-up. They agree with each other, but neither one points to the other as the owner.
- What a rename would cost: ki-pmo is declared in 9 repositories' `.ki.toml`, ki-checkpoint in 10, and ki-repo-kb-streams in 8. tools-ki source names ki-pmo in 9 files and ki-checkpoint in 2. The coordinator hook and the ki-coordinator output style look for the `[skills.ki-pmo]` declaration. A rename therefore needs a harness change, a tools-ki release, and a declaration sweep in each territory. That is why it fits before the other territories migrate, in the order Kris set under AUDIT-WHEN on 18 October: "Before other territories (Recommended)".
- Checks: I ran no `ki repo audit`, because this was a judgement review of each skill's job and name and changed no skill. My sweep for thread-model words found most remaining hits in tolerance-window readers and their tests, which is expected until phase 5.

## In Progress

Nothing is running. Any rename or merge waits for Kris's answers below.

Outstanding - no action requested now:

- A tools-ki release for a rename would go past the 0.11.1 release ceiling set for the night. It is reserved for Kris and is not scheduled.
- The `ki agent` help-text correction is a tools-ki change, sent by trade once WORKER-CLI is answered.

## Queries

### PMO-NAME - Rename ki-pmo for the work model

**Context:** ki-pmo governs coordinating work: the coordinator, the report forms, the banner, decisions and design. The work model has no word "PMO", and Kris said on 18 October, "I was thinking similar about `ki-pmo`". The skill's standard is titled "Coordinating-work standard", the output style is `ki-coordinator` and the hook is `coordinator-reminder.sh`. A rename touches 9 declaring repositories and 9 tools-ki source files. It would also need a tools-ki release, and the readers would accept the old name for the tolerance window. **Query:** Should ki-pmo be renamed before the other territories migrate? **Options:** a) (recommended, confidence medium - the name then matches its standard and pairs with ki-delegation, and a rename is cheapest before the remaining territories migrate) Rename it `ki-coordination`, with `ki-pmo` accepted as an alias for the tolerance window. b) Rename it `ki-coordinator`, to match the output style and the hook. c) Keep `ki-pmo`.

### CHECKPOINT-FATE - What ki-checkpoint is for now

**Context:** ki-checkpoint now owns the work file `+/_WORK/<id>/work.md`: its front matter, which the observatory and `ki work status` read, its body, and RESUME, UPDATE and REMOVE. It also reads old `+/_CHECKPOINTS/` records for the tolerance window. The job is real, but the name describes a record the work model has replaced. The work folder itself is owned by ki-pmo, and ki-delegation also describes it. **Query:** Should ki-checkpoint be renamed and made the single owner of the work folder, merged into ki-pmo, or kept? **Options:** a) (recommended, confidence medium - one skill then owns `+/_WORK/` and `+/_WORK_REVIEW/` for every level, including regular and ad hoc work that ki-pmo does not coordinate) Rename it `ki-work-file`, and move into it the work-folder closed list, the pruning and the review area from ki-pmo and ki-delegation. b) Merge it into ki-pmo, so that the coordinating-work standard also owns the work file. c) Keep `ki-checkpoint` as it is.

### WORK-FOLDER-DEDUP - One home for the decisions log, pruning and close-out

**Context:** The rules for capturing decisions, pruning the work folder and closing finished work are written out in both ki-delegation's Decisions log section and ki-pmo's Decisions and design and Working rules sections. The two copies agree today, but every change has to be made twice. **Query:** Should each of these rules have one owner, with the other skill linking to it? **Options:** a) (recommended, confidence medium - it ends the double maintenance, and ki-delegation keeps only what a run needs) Put the decisions log and its life cycle in ki-pmo, put pruning and close-out with the work-folder owner (ki-work-file under CHECKPOINT-FATE a, otherwise ki-pmo), and leave ki-delegation with the run packet, tiers, queue, monitoring and the `ki agent close` gate, plus links. b) Leave both copies, and add a test that holds them identical.

### DESIGN-NAME - Rename ki-pmo-design

**Context:** ki-pmo-design runs the design loop that shapes a new Project, theme or shared model before any work record exists. It does not depend on ki-pmo. If ki-pmo is renamed, the `pmo` in this skill's name stops pointing at anything. `ki-design-inspiration` and `ki-design-system` already use `ki-design-*` for website and interface design. **Query:** Should ki-pmo-design be renamed along with ki-pmo? **Options:** a) (recommended, confidence low - it names what the skill shapes and stays clear of the website design skills, but no name is an obvious fit) Rename it `ki-work-design`. b) Rename it `ki-coordination-design`, to follow PMO-NAME a). c) Keep `ki-pmo-design`.

### STREAMS-SLIM - Slim ki-repo-kb-streams

**Context:** ki-repo-kb-streams owns the KB `Streams/` container (`Roadmap/`, `Projects/` and `Themes/`) and the Enactment gate on canonical zones. Both are still needed. Its PROPOSE, READY, ROLLOUT and ITERATE modes only send the reader to ki-next, ki-plan and ki-implement, and its status table repeats ki-work-roadmap's lifecycle. **Query:** Should ki-repo-kb-streams lose its routing modes and its copy of the status table? **Options:** a) (recommended, confidence medium - the routing modes duplicate the process skills' own descriptions, and one lifecycle table removes the risk of the copies drifting apart) Keep the skill and its name, retire the four routing modes, and replace the status table with a link to ki-work-roadmap. b) Merge it into ki-repo-kb as that skill's Streams section. c) Keep it as it is.

### WORKER-CLI - `ki agent` or `ki worker`

**Context:** Under the work model, worker and supervisor are roles in a handoff. The coordinator is the worker to Kris and the supervisor of its runs. `ki agent` launches and tracks runs, which are agents, the party that a work file records as `worker: agent`. It does not launch the coordinator, which is also a worker. `ki work status` already exists and reads work files, so `ki worker` would sit one letter away from it. Separately, `ki agent decide --help` describes a "numbered" decision in "the thread's" log, and `ki agent home --help` says "thread home". **Query:** Should `ki agent` keep its name? **Options:** a) (recommended, confidence medium - the command acts on agents and runs, not on the worker role, and keeping it avoids a confusing neighbour to `ki work`) Keep `ki agent`, close the WORKER-CLI idea, and trade the help-text corrections to tools-ki. b) Rename it `ki worker`, keeping `ki agent` as an alias for the tolerance window. c) Rename it `ki run`, since most of its subcommands act on a run.

### UPDATE-SHAPE - Three-line timed updates for every coordinator

**Context:** On 18 October Kris said, "Every update, I want to know what's outstanding, what's left on the plan, and what's been done". This thread applies it now, but ki-pmo's Coordinator responsiveness section still asks only for one or two timed lines. **Query:** Should ki-pmo require the Done, Left on the plan and Outstanding lines in every coordinator's timed updates? **Options:** a) (recommended, confidence medium - it is a general preference with nothing specific to this Project in it, and it lands with the report-shape review around 21 October) Adopt it in ki-pmo and regenerate the hook line and the output style at the report-shape review. b) Keep it as a rule for this thread only.

### 🤖 → 🧑 Handoff to supervisor · since 05:04 BST

🧑 7 with you

- [with you] PMO-NAME · owner · since 05:04
- [with you] CHECKPOINT-FATE · owner · since 05:04
- [with you] WORK-FOLDER-DEDUP · owner · since 05:04
- [with you] DESIGN-NAME · owner · since 05:04
- [with you] STREAMS-SLIM · owner · since 05:04
- [with you] WORKER-CLI · owner · since 05:04
- [with you] UPDATE-SHAPE · owner · since 05:04
- [committed] skills-audit report, ki-principal
