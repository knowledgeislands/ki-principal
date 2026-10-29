# wow-host-sync-design - HOST-SYNC merged report and owner decisions (ki-work-design)

You work for ki.prj.ways-of-working (coordinator on terra). Follow `ki-work-design`: the brief and independent reviews exist; your job is the single merged report and the owner decision set, so Kris can decide in one pass. Kris's decisions of 2026-10-29 (HOST-SYNC-DESIGN, RECOMMENDED-ALL) are in the package's `decisions.md`; under FINISH-LINE option a, HOST-SYNC is finished here as this Project's last design, so keep the decision set as small as the evidence allows.

Inputs (read from the levelled primary checkout, /Users/krisbrown/workspaces/knowledge-islands/ki-principal):

- `+/_WORK/ki.prj.ways-of-working/design/host-sync-and-reply-trades.md` - live unadopted design, with Kris's full HOST-SYNC and HOST-SYNC-REPLY words.
- `+/_WORK/ki.prj.observatory/design/observatory-sync-report.md`, especially `#host-meaning---receiver-owned-responsibility-semantics` - Observatory's independent HOST-SYNC-REVIEW and design report (agrees: independent per-host responsibility, offsets as cadence only, no automatic takeover; read-back timing and seat/failover are separate owner decisions).
- The HOST-SYNC query in `+/_WORK/ki.prj.ways-of-working/queries.md` and the HOST-SYNC-REVIEW line in its `messages.md`; Git history for the original HOST-SYNC message line if the design note does not carry it verbatim.
- Read-only context as needed: personal.reg.rig-terra and personal.reg.rig-sol (`/Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/`), tools-rig, chezmoi. Do not edit them.

Write `+/_WORK/ki.prj.ways-of-working/design/host-sync-report.md`:

1. The merged design in plain language: the two hosts (terra, sol), who publishes, in what sequence and offset, how a primary consumes a secondary's updates, what happens when one host is off, and the reply-trade destinations. Name each unit, its boundary and hand-offs.
2. Where the reviews agree, state it as settled by review. Anything undecided becomes a tagged decision (stable mnemonic tag, e.g. HOST-SEQUENCE) with **Context:**, **Query:**, **Options:** - lettered, `a) (recommended, confidence <high|medium|low> - <reason>)` first. Never invent concurrency, scheduler or seat authority Kris has not given; mark which decisions need Rig or chezmoi execution.
3. Draft, not send, exactly one rollout line each for personal.reg.rig-terra and personal.reg.rig-sol `messages.md`, in the queue line shape (`- 2026-10-29 · HOST-SYNC · KI > Model > Ways of working (ki.prj.ways-of-working): ...`), conditional on the recommended options.

Do not change queries.md, decisions.md, state.md or any other repository. Commit only the report by explicit path (`docs(work): ki.prj.ways-of-working HOST-SYNC merged report`), pull ff-only and push ff-only; stop on divergence. British English, ASCII hyphens only.
