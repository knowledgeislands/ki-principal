---
id: ki.ways-of-working
state: with-worker
since: 2026-10-26T21:13:00Z
received: 2026-10-22T07:24:00Z
beat: null
mark: 2026-10-25T01:07:00Z
method_read: 26ad77f1
---

# ki.ways-of-working state

## Now

- 08:28 GMT 26 October: received wow-docs-svg, docs SVG figures fixed and live (a2942ea). AWAY-GRANT-2 ended; wakes stopped; waiting on Kris, chiefly REL-MACOS-OOM.
- 08:27 GMT: AWAY-GRANT-2 unattended window opened, ending at "I'm back" or about 08:27 GMT on 26 October; session cron wakes every 15 minutes; stop word "stop the wake".
- 08:58 GMT: received this window wow-ci-pins, wow-unattended-limits, wow-tap-consumer, wow-review-docs-red, wow-replay-smoke, wow-external-limits, wow-guidance-refresh, wow-hnr-resolve, wow-hnr-level, wow-ask-timeout, wow-mgit-cache-design, wow-red-main and two blind reviews. Harness main green at `5cb52973`; guidance read to `fdf9a604`.
- 10:55 GMT: received wow-fleet-green. 13:23 GMT: received wow-ki-pin-release; tools-ki main green, but ki v0.14.0 did not publish (macOS package jobs out of memory), so the fleet's DESIGN-2 reds stay until REL-MACOS-OOM is answered.
- 13:28 GMT: received wow-review-rel; nothing is running. Waiting on Kris, chiefly REL-MACOS-OOM for the release.
- 01:07 GMT: mark struck at the start of the previous window. 06:43 GMT: DOCS-PUBLISH complete and live.

## Next steps

- Coordinator: the window has ended and the wakes are cancelled; the return report has gone to Kris; strike the next mark once Kris has seen it, then launch the work each answer authorises.
- Kris on return: the open queries in `queries.md`, the website review list and the review pack.

## Held

- PAPERCLIP-REQ, on hold while Kris gets KI stable (2026-10-19).
- Email-routing records stay with hnr.email-routing.
- tools-rig v0.8.0 tag, held until the review gates settle.
