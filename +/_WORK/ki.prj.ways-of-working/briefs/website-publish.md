# Brief: website-publish

Work: ki.prj.ways-of-working. Kris granted on 31 October: "publish website yes you can push it. You can make it live" (WEBSITE-LIVE in `decisions.md`). Read run `website-learn`'s report at `/Users/krisbrown/.local/state/ki/agents/ki-prj-ways-of-working/website-learn.report.md`.

Make its pages live by the site's normal route. If they are on a branch, fast-forward or merge it into `main` and push. Then run whatever the site's own documented deploy is, if the push does not deploy by itself.

Run the site's build and checks first, and stop if they fail. Never force or skip hooks. Verify the live pages load, and report their URLs.
