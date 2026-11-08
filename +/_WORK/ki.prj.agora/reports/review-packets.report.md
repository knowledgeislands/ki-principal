# KI > Techne > [Agora](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.agora/work.md) › review-packets

**🤖 → 👤 Handoff to supervisor · Run report at 05:08 GMT · last mark 04:53 GMT**

---

## New and noteworthy

[KI-AGORA-NET-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-NET-001-observatory-read-endpoint.md), the read endpoint, is **not ready to accept, and the blocker is its lifecycle state rather than the build**. It runs on both Macs and every live check matched the contract: loopback only, read-only, foreign websites and hosts refused, live events stream. It is still in triage with no plan, so Kris has to adopt it before anyone can accept it. Two smaller points want his view:

- If its port is already taken, the endpoint stays off until the Beacon restarts.
- Its title names the Observatory, but its real users today are the Atlas and the KIV.

[KI-AGORA-TRY-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-TRY-001-menu-bar-identity.md), the menu-bar identity, is **not ready to accept yet**. On sol the ring, its marks, the count, the five-item menu and the notification wording all match the agreed identity document; screenshots are in the record. Four things still block it:

- terra could not be seen from here;
- the hover tooltip was not seen on either Mac;
- checkout notices repeat while a checkout flips between states (`ki-principal` was announced 20 times in 36 minutes on sol);
- its Verify section still asks for "the first two menu lines", but those moved into the tooltip under Kris's later decisions.

sol's displays are not Retina, so the record's "every Mac menu bar is 2x" no longer holds.

## Done

- Both records now carry a full six-part review packet, with each criterion's code, tests and a live check; NET-001 also has a new "Endpoint lifecycle" section. Commit `d419ab5`, pushed.
- NET-001's lifecycle: it starts with the Beacon when `[local]` is on (the default, and the setting on both Macs). It listens on `127.0.0.1:1677` only. Any program on that Mac may read it, browsers only from local pages. It stops when Kris uses Quit Agora Completely or logs out; Quit Atlas leaves it running.
- Live read-only checks on sol and on terra over SSH: all paths answered as the contract says, and the tailnet address got no answer.
- sol: captured the menu-bar ring and the open menu, and read 45 Beacon notifications from Notification Center.
- terra: no screenshot was possible over SSH (screen capture, accessibility and the notification store were all refused). The record lists exactly what Kris should look at there.
- Checks: tests pass (568), the self-check passes with knip clean, and Markdown checks are clean on both records. The roadmap audit dropped from 4 failures to 3, because NET-001's Discussion is now last.
- Neither record's status changed: NET-001 stays in triage and TRY-001 stays awaiting review. No code was changed, nothing was installed or relaunched, and the other session's dirty iOS project file was left alone.

## In Progress

Nothing running.

## Queries

**TRY-001 · Repeating checkout notices**

**Context:** The Beacon announces a checkout again each time its state changes, so one busy repository can notify many times an hour. The identity document says a thing is announced once, and again only if it settles and comes back.

**Query:** Should a checkout be announced only once until it is level and clean again?

**Options:**

a) (recommended, confidence medium - it matches the agreed design and stops the noise) Yes: capture it as a fix before accepting TRY-001.

b) No: accept the current behaviour and note it in the record.

**TRY-001 · Stale Verify line**

**Context:** Verify asks that "the first two menu lines" read as the identity document says, but Kris's later decisions moved that line into the tooltip.

**Query:** Should the review judge the tray against the current identity document?

**Options:**

a) (recommended, confidence high - the document records Kris's own later decisions) Yes: judge against the current document, and restate Verify when the record is next touched.

b) No: hold the record until Verify is formally replanned.

**NET-001 · Adoption and naming**

**Context:** The endpoint is built and checked but still in triage. Its title names the Observatory, which does not read it yet; the Atlas and the KIV do.

**Query:** Should NET-001 be adopted with the Atlas and KIV as its viewers, so it can go through readiness to review?

**Options:**

a) (recommended, confidence medium - the build already meets the goal for its real users) Yes: adopt it, retitle it to the Agora read endpoint, and leave the Observatory's reading as its own later record.

b) Adopt it as it stands, and keep it open until the Observatory reads it.

---

### 🤖 → 👤 Handoff to supervisor

0 running · 0 blocked units · 3 queries

- [handoff-to-supervisor] review packets for NET-001 and TRY-001 · supervisor · since 05:08 GMT

🧵 ki.prj.agora
