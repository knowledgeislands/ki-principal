# Classification

Every checkpoint and thread folder in Knowledge Islands Principal, with the work it becomes. Confident means the work's Project and id are unambiguous and the work is live; review means it goes to `+/_WORK_REVIEW/<id>/` with this reason in that area's index note, under MIGRATION-REVIEW. `classification.tsv` is the machine-readable copy the scripts read; this table is generated from it.

| Work id | Area | Confidence | Checkpoint | Thread folder | Title | State | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ki` | `+/_WORK` | confident | `+/_CHECKPOINTS/_state-of-play.md` | `+/_THREADS/state-of-play/` | KI > SoP | on-hold (paused, after the work migration lands) | The Capital's territory work, named in the brief. |
| `ki.regular` | `+/_WORK` | confident | none | none | KI > Regular | on-hold (more-expected, new regular work arriving) | New regular work, named in the brief; no checkpoint or thread exists yet. |
| `ki.ways-of-working` | `+/_WORK` | confident | `+/_CHECKPOINTS/knowledge-islands-model.ways-of-working.md` | `+/_THREADS/ways-of-working/` | KI > Model > Ways of working | with-worker | Live Project work leading this migration, named in the brief. |
| `ki.knowledge-acquisition` | `+/_WORK` | confident | `+/_CHECKPOINTS/knowledge-islands-model.knowledge-acquisition.md` | `+/_THREADS/knowledge-acquisition/` | KI > Model > Knowledge acquisition | on-hold (paused, after the work migration lands) | Live coordination checkpoint, marked on 18 October; one registered Project. |
| `ki.observatory` | `+/_WORK` | confident | `+/_CHECKPOINTS/knowledge-islands-model.observatory.md` | `+/_THREADS/observatory/` | KI > Model > Observatory | on-hold (paused, after the work migration lands) | Live coordination checkpoint, marked on 18 October; one registered Project. |
| `ki.tools-burndown` | `+/_WORK` | confident | `+/_CHECKPOINTS/platform-foundations.tools-burndown.md` | `+/_THREADS/tools-burndown/` | KI > Foundations > Tools burndown | on-hold (paused, after the work migration lands) | Live coordination checkpoint at rest, one registered Project; held while another session has the folder in flight. |
| `ki.chezmoi` | `+/_WORK` | confident | `+/_CHECKPOINTS/rig.chezmoi.md` | `+/_THREADS/chezmoi/` | KI > Rig > chezmoi | on-hold (paused, after the ways of working reports are ready) | Live coordination checkpoint, one registered Project; held while another session has it in flight. |
| `ki.mac-studio-setup` | `+/_WORK` | confident | `+/_CHECKPOINTS/rig.mac-studio-setup.md` | `+/_THREADS/mac-studio-setup/` | KI > Rig > Mac Studio setup | on-hold (paused, after the work migration lands) | Live checkpoint marked on 18 October, five reports; one registered Project. |
| `ki.regular.registry-removal` | `+/_WORK` | confident | `+/_CHECKPOINTS/registry-removal.md` | `+/_THREADS/registry-removal/` | KI > Regular > Registry removal | on-hold (paused, sol's exact-key check) | Ad hoc work with no Project, named in the brief as ki.regular.registry-removal. |
| `ki.baseline-rollout` | `+/_WORK_REVIEW` | review | `+/_CHECKPOINTS/platform-foundations.baseline-rollout.md` | `+/_THREADS/baseline-rollout/` | KI > Foundations > Baseline rollout | on-hold (paused, Kris's review) | Drained on 15 October with no open records; may be finished rather than live. |
| `ki.estate-factorisation` | `+/_WORK_REVIEW` | review | `+/_CHECKPOINTS/platform-foundations.estate-factorisation.md` | none | KI > Foundations > Estate factorisation | on-hold (paused, Kris's review) | Drained handover with no thread folder; its recovery files sit in the tools-burndown folder. |
| `ki.agent-host` | `+/_WORK_REVIEW` | review | `+/_CHECKPOINTS/techne.agent-host.md` | `+/_THREADS/techne/` | KI > Techne > Agent host | on-hold (paused, the Techne Programme Hold lifting) | Drained for sol under the Techne Programme Hold; its thread folder is named techne, not agent-host. |
| `ki.regular.command-centre` | `+/_WORK_REVIEW` | review | none | `+/_THREADS/command-centre/` | KI > Regular > Command centre | on-hold (paused, Kris's review) | A decisions log with no checkpoint; its subject folded into the Observatory Project on 18 October. |
| `ki.paperclip-capture-and-rebuild` | `+/_WORK_REVIEW` | review | none | none | KI > Techne > Paperclip capture and rebuild | on-hold (paused, the Techne Programme Hold lifting) | Design papers only, with no checkpoint or thread, under the Techne Programme Hold. |

Counts: 9 confident, 7 of them moved by the first run, `ki.tools-burndown` and `ki.chezmoi` held while their sessions have them in flight; 5 for review. `+/_THREADS/desk-kit/` is named in the defer list but no longer exists.

Strays the closed list does not admit, each moved to its work folder's `design/` and named in the dry run:

- `+/_THREADS/state-of-play/`: `observatory-goals/`, `themes/`, `themes.md` and `personal-acquire-handover.md`, to `+/_WORK/ki/design/`.
- `+/_THREADS/ways-of-working/`: `work-model.architecture.json`, `work-model.svg` and this plan folder, to `+/_WORK/ki.ways-of-working/design/`; `work-migration.brief.md` goes to `briefs/work-migration.md`.
- `+/_THREADS/tools-burndown/` (held): `drain-sol.evidence.json`, `historical-decisions.md`, `migration-manifest.json`, `resume-stock.evidence.json` and `resume-stock.verification.json` would go to `design/`, and `next-worker.brief.md` to `briefs/next-worker.md`.
