# Resume note

An earlier run on this brief stopped at a usage limit after committing its first prune batch (`b5d3955f`) and the lesson (`55761ad1`); the lesson is done, so do not add it again. About 67 tracked reports remain: review those and finish.

## wow-prune-reports - prune received run reports from the ki.ways-of-working work folder

/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working holds about 200 tracked `wow-*.report.md` files from earlier runs. Under ki-coordination's pruning rule and ki-work-package's Tidying the work folder, delete by explicit path each report whose outcome has a durable home (a record, /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md, the work package or a commit) and whose queries were copied into /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/queries.md or have since been answered in decisions.md. Keep any report whose outcome is not yet homed, any whose queries are neither in queries.md nor answered, and any in doubt; list every kept report with a one-line reason. Do not touch the five package files, briefs, or design/. Commit the deletions by explicit path in batches with `docs(work): ki.ways-of-working prune received reports`, then sync.

### Authority and rules

Kris granted an unattended window tonight, recorded in /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md (the 25 October entries from 01:07 GMT on), ending 09:00 GMT. Within it you may edit, commit and push fast-forward only. Never force-push and never use `--no-verify`. Stage by explicit path only; never touch another session's files. After every commit, `git pull --ff-only` and then push; if the pull cannot fast-forward, stop and report. Stop starting new steps at 08:45 GMT. Write the report in the ki-coordination owner-report shape, closing with the banner and the line `🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)`. British English, ASCII hyphens only.
