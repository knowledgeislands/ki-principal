# Host synchronisation and request/reply trades

Status: live unadopted design input. No owner option has been chosen. This note preserves the received need; it adopts no model, schedule, transport or implementation.

## Host synchronisation

The owner wants equivalent coordinating work on Terra and Sol to synchronise regularly with offsets. Each host would publish repositories for which it is primary before consuming the other host's primary updates. How the primary subsequently reads secondary updates remains undecided. The receiving line reports that Terra's half-hourly HNR sync was stopped; this is sender evidence, not a fresh status check or authority to restart it.

The design must reconcile existing host responsibilities, `.chezmoidata/seats.yaml` and ADR-KI-PRINCIPAL-007 before selecting timing, publication boundaries, conflict handling or secondary-to-primary feedback. Read only authorised non-HNR sources when design resumes. No HNR inspection, scheduler/provider/control-store mutation, install or change to runtime bindings is authorised here.

### Full received source

- IMPORTANT · 2026-10-28 · HOST-SYNC · Personal > Rig > terra (personal.reg.rig-terra): urgent, Kris wants both machines on regular sync-ups soon and will settle the details with you. Kris (13:50 GMT): "the sync process should always be run from this equivalent thread on both Terra and Sol … each of them gets an offset … we're going to get into race conditions if both are trying to do the sync at the same time and we probably want to do a resync as well in short order after it." Shape proposed by Kris: (1) the dotfiles carry an entry naming, per territory, which host is primarily and which secondarily responsible ("I can't remember where it's gone"; the nearest today is chezmoi `.chezmoidata/seats.yaml`, which binds territories to terra as home and sol as hub under ADR-KI-PRINCIPAL-007, with no primary or secondary); (2) a regular activity registered per host: "on the hour, it should resync and publish effectively into the GitHub repos the ones which it has primary responsibility for. And then five minutes later … the secondary ones", so each primary publishes first and each secondary then pulls in the other host's primaries and adjusts; (3) "the primary then needs to be able to read the secondary updates … It shouldn't be an onerous process", which still needs deciding. Kris: "push that into the ways of working … I'll deal with the ins and outs." Terra's half-hourly HNR `mgit sync` stopped at 13:52 GMT until this lands; the Observatory side went to ki.observatory as HOST-RESPONSIBILITY.

- 2026-10-28 · HOST-SYNC-REPLY · Personal > Rig > terra (personal.reg.rig-terra): adding to HOST-SYNC: when the design is settled, send its rollout as one line each to personal.reg.rig-terra and personal.regular.rig-sol, which carry it into the chezmoi sources and Rig on their hosts.

### Unanswered choices and reply destinations

Regularity, offsets, which repositories each host publishes, how secondaries feed back and what safely resumes the stopped sync all await design and owner decision. Existing narrower task and repository push rules continue to govern every operation. HOST-SYNC is not scheduler authority.

After design is settled, send one rollout line to each actual current Rig queue, `personal.reg.rig-terra` and `personal.reg.rig-sol`; the source's tolerated older spelling is retained above. Rig owns the chezmoi-source and host rollout. Observatory owns its separately routed HOST-RESPONSIBILITY input; no completion is claimed here.

## Request/reply trades

The owner asks that the next trades design cover the sender's request for a reply, the receiver's obligation and progress visibility, and how the sender can finish without reading or tracking another package. The current method remains one authoritative incoming queue and explicit reply requests; this draft creates no acknowledgement protocol, second queue, field, polling or new record.

### Full received source

- 2026-10-28 · TRADES-REPLY · Personal > Rig > terra (personal.reg.rig-terra): Kris (14:30 GMT), on terra waiting for ki.chezmoi and this work to answer its messages: "It feels like these are getting close to the original ideas around trades. And I wonder then if we can ask ways of working to think about that when it does come back to looking at trades, how we deal with this aspect as well." The gap: a `messages.md` line is one-way, so a sender that needs an answer must ask for a reply line in its text (as DISPATCHER-REPLY and HOST-SYNC-REPLY do) and list it as awaiting. When trades are next looked at, please consider request and reply: how a line asks for an answer, how the answer comes back to the sender, and how the sender can count itself done meanwhile without tracking it.

- 2026-10-28 · WAITS-AS-TRADES · HNR > Email routing (hnr.reg.email-routing): Kris (14:25 GMT), on this work's waits on other work, SENT-PASS with ki and TRIAGE-HOURS with ki.chezmoi: "It feels like these are getting close to the original ideas around trades. And I wonder then if we can ask ways of working to think about that when it does come back to looking at trades, how we deal with this aspect as well." Please take cross-work asks into account when trades are next taken up: how an ask sent to another work is tracked as owed by the receiver, how the sender sees its progress without reading the receiver's package, and how delivery releases the sender's hold. Today both sides track it by hand: a line in the receiver's `messages.md`, a Held item and a `[waiting]` banner item in the sender's `state.md`, released only by a reply line in the sender's `messages.md`. No action needed back to hnr.reg.email-routing.

### Held home and receiving owners

These inputs remain owned by Ways of working pending the FINISH-LINE choice and any acknowledged stewardship handover. Existing trades policy and PACKAGE-FORWARDING remain separate; this note does not reopen or silently resolve their decisions. Return any eventual decision/rollout to the sender work through its queue; HNR delivery remains subject to the explicit source/write exclusion and its owner route.

## Provenance and guards

The four complete source lines were verified against Principal `3b512680dd0f756227ae37b5d8408401b6555841` at `+/_WORK/ki.prj.ways-of-working/messages.md` (SHA-256 `6f5d99a8a55fa2a515df98004c13eabec4da9d902a4985a24f4d643cb160360e`). [Committed source](https://github.com/knowledgeislands/ki-principal/blob/3b512680dd0f756227ae37b5d8408401b6555841/+/_WORK/ki.prj.ways-of-working/messages.md) preserves their original context. They were already tracked sources, not newly copied private reports.

No canonical adoption, source publication grant, cross-territory ownership transfer, held-work release or response from a receiving owner is inferred. Keep this note until the design graduates or is explicitly superseded.
