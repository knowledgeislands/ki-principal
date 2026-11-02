---
note_type: streams/design
status: current - 2 November 2026
work: ki.prj.orca-evaluation
author: Written with Claude
---

# Orca evaluation handover to the assistants

**From:** `ki.prj.orca-evaluation` · **To:** [`personal.reg.assistant-terra`](/Users/krisbrown/kis/personal/assistant/+/_WORK/personal.reg.assistant-terra/work.md) now, `personal.reg.assistant-sol` when it opens · **Authority:** Kris's ASSISTANT-NOW and FOCUS-ASSISTANT of 1 November 2026, with the quick answer PS-ORCA "Into assistants", in [Ways of working's decisions log](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/decisions.md). The `ki-delegation-orca` adapter still lands in the KI harness through `ki.prj.ways-of-working`.

## What this Project established

- **Trial log.** [orca-trial.md](orca-trial.md) is the single record of running KI work through Orca: what was tried, what is proved (nesting under the coordinator's row, the `check --wait` wake in a Claude Code chat, release from a chat, the ask path, steering, pathspec commits), what is open, the known gotchas and what Orca stores. The trial is complete apart from worker survival when the coordinator chat ends, left to first live use (TRIAL-SHAPE).
- **Launcher proposal.** [orca-launcher.md](orca-launcher.md) drafts `ki-delegation-orca`, Orca's adapter of the `ki-delegation` contract. It is with `ki.prj.ways-of-working` for adoption (ORCA-LAUNCHER), which is drafting the adapter into the harness for Kris to publish.
- **Card bug.** The question card dropping line breaks is filed as [stablyai/orca#36830](https://github.com/stablyai/orca/issues/36830) (1 November).

## Open owner questions

The full Context and Options are in this package's [discussions.md](../discussions.md); all five went to Kris on 1 November and are unanswered.

- **SCOPE-SPLIT** - hand the four method questions (TRIAL-PUBLISH, TRIAL-ASK, TRIAL-PRACTICE, ORCA-IDENTITY-LEAK) and the CODEX-WAKE test to Ways of working, keeping Orca usage here: recommended a) yes (high).
- **ORCA-UPSTREAM** - which of the four remaining feedback items go to Orca: recommended a) send the row label "Monitoring background tas..." and the hidden sidebar restore as two separate reports, hold the settings export, drop the outside-session parent (high, reviewed).
- **THREADS-TRY** - archive one finished Codex worker conversation on terra through Codex's own commands, check it leaves the ChatGPT app's list, then unarchive: recommended a) yes (high, reviewed).
- **THREADS-SWEEP** - once the test works, archive every finished worker conversation on each Mac after each Orca Run, deleting after about two weeks on Kris's go: recommended a) yes (high, reviewed).
- **THREADS-FR** - one feature request asking Orca for an opt-in setting to archive or delete a worker's Codex conversation on release: recommended a) file it now (high, reviewed).

## Unanswered request and outstanding items

- **ORCA-AUTO-RELEASE** (from Ways of working, at Kris's word via `hnr.reg.email-routing`): can Orca release a worker automatically on completion, by a setting, a flag or a feature to request? Not yet looked into. Meanwhile the method rule WORKER-LEFTOVERS (ki-agentic-harness `6b3571d0`) has coordinators run `orca orchestration worker-release` in the wake that receives `worker_done`. Reply to `ki.prj.ways-of-working`'s `messages.md`.
- **ORCA-REMOTE-VIEW**: whether terra can show sol's threads; one read-only investigation under ORCA-HOST.
- **vega's thread count**: worker conversations counted on terra (50) and sol (3), not yet on vega, feeding THREADS-SWEEP.
- **ORCA-REACH follow-up due 6 November 2026**: Kris asked for a review a week on of "Orca only on attended Macs, packages opting in by logged decision, `ki agent` only on vega".
- **Run id exception to ORCA-ROUTING**: this package's `state.md` names Orca Run `run_a30bc0d03f5b`, against the rule that package files keep no Run id; kept until a machine-local routing record exists. Find a Run by its objective, which starts with the work id.

## What stays where

- **With `ki.prj.ways-of-working`** (later `ki.sop.main`, under PS-METHOD-HOME): the method, meaning `ki-delegation-orca` and its adoption, the wake contract and CODEX-WAKE, worker close-out and routing rules, and the four method questions SCOPE-SPLIT would hand it. Send it requests as message lines.
- **With the assistants**: how Kris uses Orca day to day, the Orca evidence in this trial log, the worker-thread clear-out (THREADS-TRY, THREADS-SWEEP), ORCA-AUTO-RELEASE, ORCA-REMOTE-VIEW and all feedback to Orca upstream (ORCA-UPSTREAM, THREADS-FR, follow-up on #36830).
- **This package** goes on hold pending close-out once the line below is sent; its decisions log and Git history keep the record.

## Message line for `personal.reg.assistant-terra`

```markdown
- IMPORTANT · 2026-11-02 · ORCA-HANDOVER-ASSISTANT · KI > Techne > Orca evaluation (ki.prj.orca-evaluation), at Kris's word on 1 Nov (ASSISTANT-NOW, FOCUS-ASSISTANT, PS-ORCA "Into assistants"): the Orca evaluation is yours, and assistant-sol's when it opens. Handover note: ki-principal `+/_WORK/ki.prj.orca-evaluation/trial/handover.md`, with the trial log and launcher proposal beside it. Carry to Kris five open questions (SCOPE-SPLIT, ORCA-UPSTREAM, THREADS-TRY, THREADS-SWEEP, THREADS-FR, each recommended a), full text in that package's discussions.md); answer ORCA-AUTO-RELEASE (can Orca release a worker automatically on completion) to ki.prj.ways-of-working; and hold ORCA-REMOTE-VIEW, vega's worker-thread count, the ORCA-REACH follow-up due 6 November 2026 and the Run id exception to ORCA-ROUTING. Card bug filed as stablyai/orca#36830. The ki-delegation-orca adapter and other method questions stay with ki.prj.ways-of-working. ki.prj.orca-evaluation goes on hold pending close-out.
```
