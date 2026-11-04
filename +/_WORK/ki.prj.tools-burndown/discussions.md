# ki.prj.tools-burndown discussions

## Open

### WATCH-AGORA - Whether `ki work watch` is still wanted now Agora rings a doorbell

focus: _emerging · since 2026-11-04 · from burndown-sweep · needs a blind review before it reaches Kris (medium)

**Context:** On 1 November Kris decided INBOX-VERB: a read-only `ki work watch <work id>` command that waits quietly and wakes a thread when a message lands or a run finishes (the WATCH-VERB line). On 3 November Agora began waking threads itself through a doorbell file (AGORA-DOORBELL), and State of play's own wake now uses it. The method intake of 3 November thought the command probably overtaken, but its question never reached Kris.

**Query:** Should tools-ki still build `ki work watch`?

**Options:**

a) (recommended, confidence medium - Agora's doorbell already does the waking, and a second watcher would duplicate it) Drop WATCH-VERB as overtaken by Agora's doorbell, keeping the design for reference.

b) Build it anyway, as a fallback for runtimes or hosts without Agora.

### HELD-ROADMAP-KNIP - Knip commits stacked on the held roadmap commits

focus: _emerging · since 2026-10-29 · from estpush2.report.md · moved back to Open at the release of 3 November

**Context:** In 5g-emerge-apex, 5g-emerge-demos, 5g-emerge-testbed and apps-vallearmonia.com, the Knip commit sits on estmig-org's hook commit and other sessions' unpushed roadmap commits. These are the same stacks estpush held under HELD-ROADMAP.

**Query:** Should these four be pushed together with the decision on HELD-ROADMAP?

**Options:**

a) (recommended, confidence medium - one decision clears both, and all four trees are clean and level) Take HELD-ROADMAP a) and push `main` whole in all four, Knip commit included.

b) Leave all four for their owning sessions to push.

### ASK-B - Coarse acquisition kind in the public export

focus: rig-site · since 2026-10-19 · from rigsite-config.report.md in the run state folder · parked: ASK-B a), under HIGH-CONFIDENCE on 19 October; release: the rig.midnight.ninja side asks

**Context:** Ask B has no go-ahead. If it goes ahead, a `kind` or `form` field derived as application or command-line would get past the site's forbidden-field check. Platform variants complicate it, because one tool can install differently on macOS and Linux. It would widen the public export (RIG-PUB-002).

**Query:** Keep Ask B parked?

**Options:**

a) (recommended, confidence high - there is no go-ahead, and it widens the public boundary) Keep it parked and raise it only when Kit asks.

b) Capture it at triage now, marked as waiting for Kit's go-ahead.

- focus: _emerging · SRC-PLACEMENT - where KI-TOOL-KI-CLI-139's SharePoint mirror command sits. Recommended a) (medium, reviewer view): a separately specified source-maintenance command group in `ki`.

## Parked

None.
