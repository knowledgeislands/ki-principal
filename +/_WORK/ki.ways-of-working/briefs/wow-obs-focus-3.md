# wow-obs-focus-3

## Goal

Finish and activate the Observatory Focus page that wow-obs-focus-2 built and committed locally as `2d84ebf` in `/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local`. Read its report first: `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-obs-focus-2.report.md`, and the original brief beside this one, `wow-obs-focus.md`. Finish within about 40 minutes.

## Two blockers, both decided

1. **Audit gate (PKG-6):** move the repository's lint-staged configuration in `package.json` to check-only commands, the convention the harness hook convergence set on 26 October (look at a converged repository such as `/Users/krisbrown/workspaces/knowledge-islands/tools-rig` for the shape). Commit it separately as `chore(hooks): ...`.
2. **Estate selection:** the estate reader refuses every repository because `5g-emerge/apps-5g-emerge.io` is registered as `5g-emerge/5g-emerge-apex`. Do not change the registry or any other repository. Instead, make Focus (and only Focus, unless the shared reader already supports it) show every repository it can read and list each one it cannot, by name and reason, as one calm warning line at the top. Keep the strict behaviour for any existing view that relies on it.

## Then

Run the full checks, `ki repo audit --repo .` with the linked `ki`, the browser check against the whole estate, then push fast-forward only and activate the running local service the way the repository documents, so `http://127.0.0.1:1675/` opens on Focus. Confirm in the running app that Focus is the landing page, the ways-of-working queries appear, the copy line forms, and Legacy holds every old view.

## Bounds

As in `wow-obs-focus.md`: only `apps-observatory.local`; no new software or dependencies; no network-facing, DNS, Cloudflare, tailnet or credential change; commit by explicit path with Conventional Commits; pull with rebase; push fast-forward only, never force or `--no-verify`; leave other sessions' files alone.

## Report

Owner report: Done (what changed, the live URL, how it was checked), In Progress, Queries (only a true blocker).
