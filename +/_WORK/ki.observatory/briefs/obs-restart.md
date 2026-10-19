# obs-restart - Restart the Observatory service

This run is for KI > Model > Observatory (`ki.observatory`). The Observatory service in apps-observatory.local needs a restart so that it serves KI-OBSERVA-VIS-025 (commits `a9fb2ed` and `53a40b0`) and the current `main`, which Kris is about to look at.

1. Find how the service is run on this Mac. Check its README, `package.json` scripts, any launchd agent, and how it was restarted at 12:25 BST today (see the ki-principal commit `21ca69bf` and the run reports in `~/.local/state/ki/agents/observatory/`).
2. Rebuild if the service needs it, then restart it.
3. Confirm that it is up, and that the Work tab's data endpoint lists ki-principal's migrated works.

Change no source, commit nothing and push nothing.

Report in owner-report shape in a few lines: the URL, what you ran, and the result. Queries: `No outstanding queries` unless the restart fails.
