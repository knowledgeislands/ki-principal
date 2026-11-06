# KIV handover from personal.reg.inbox-sol

Received 6 November 2026, 20:15 GMT (MSG-64e9236e), under KIV-TO-AGORA. The KIV's code is in the Inbox repository at `packages/kiv`; nothing was in flight.

## Open items

1. **The viewer's queue**, in order: [designer-queue.md](https://github.com/krisb/inbox/blob/34906ffa/+/_WORK/personal.reg.inbox-sol/kiv/designer-queue.md), with the [1 November handoff](https://github.com/krisb/inbox/blob/34906ffa/+/_WORK/personal.reg.inbox-sol/kiv/handoff-2026-11-01.md), the [focus note](https://github.com/krisb/inbox/blob/34906ffa/+/_WORK/personal.reg.inbox-sol/kiv/kiv.md) and the [Workers design report](https://github.com/krisb/inbox/blob/34906ffa/+/_WORK/personal.reg.inbox-sol/kiv/workers-design.report.md).
2. **PRO-002-ACCEPT** (with Kris): he chose to look at the viewer himself before PERSONAL-INBOX-PRO-002 is accepted; all five asks are delivered.
3. **E2E-FIXTURES** (with Kris): the browser tests in `packages/kiv/e2e/focus.e2e.ts` still read live packages, including the closed `personal.reg.inbox-terra.kiv`, so they fail; recommended a short run giving them the unit tests' sample data.
4. **VIEWER-DEFER** (from ATER-030): the KIV's defer accepts action cards in view folders, `knowledge/actions/<territory>/<view>/<id>.md` with an `_index.md` per view.
5. **KIV-ELECTRON** waits on Agora's send side and on AGORA-FOCUS, the overall design of Agora, the KIV and the Observatory; KIV-TO-AGORA and run kiv-embed now answer the embedding part.
