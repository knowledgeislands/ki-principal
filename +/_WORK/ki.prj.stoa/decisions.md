# ki.prj.stoa decisions

## 2026-11-07 02:46 GMT - STOA-RELEASE - release 0.32.0 and accept STOA-CMD-001

home: ../packages-stoa/CHANGELOG.md

class: operational

- Kris, 7 November 2026, 02:44 GMT, opening this Project work: "Release Stoa 0.32.0 now under STOA-RELEASE: accept STOA-CMD-001 and cut the release." This confirms his STOA-RELEASE a) of 6 November 2026 relayed by hnr.sop.main (MSG-d56132fe) and answers ki.reg.main's RELEASE-GO a). Read as the repository's release process: accept STOA-CMD-001, bump to 0.32.0, date the CHANGELOG, tag v0.32.0 and push main and the tag to origin, as every earlier release was pushed.

## 2026-11-07 04:07 GMT - STOA-ADAPTER b) - Stoa becomes a Knowledge Islands repository

home: ../packages-stoa/.ki.toml

class: operational

- Kris, 7 November 2026, answering STOA-ADAPTER: "Stoa absolutely must become a Knowledge Islands repo. And I'm surprised it's the only one that we've got that's got packages in ... they're very similar to a lot of other repos that we've got across this set of islands. So maybe you can just take that on board. And get them fixed. Yeah, I think they're probably pretty similar to tools. It probably does mean that we should have a skill for whatever structure this thing might have. It seems like it's a new repo shape really, doesn't it?" Taken as option b): declare packages-stoa a KI repository, closest to the tools shape, fix what the audits find, then accept STOA-CMD-001 and release 0.32.0 under the STOA-RELEASE entry. The new repository-shape skill is routed to ki.sop.main.

## 2026-11-07 04:54 GMT - STOA-LICENCE - MIT, copyright Kris

home: ../packages-stoa/LICENSE

class: operational

- Kris, 7 November 2026, answering STOA-LICENCE: "The license should just be the same as all of the other Knowledge Islands ones, which I think are MIT copyrighted to me." Checked: the public Knowledge Islands repositories carry the MIT License, "Copyright (c) 2026 Kris Brown", as tools-mgit does.

## 2026-11-07 04:57 GMT - STOA-AUDIT-REST b) - everything is Stoa, house conventions throughout

home: ../packages-stoa/.ki.toml

class: operational

- Kris, 7 November 2026, answering STOA-AUDIT-REST, as transcribed: "Yeah, go back and fix everything so there's no such thing as portal framework or anything like that. Everything is stower. Yeah, just go over it all like that. And then with the test messages itself called on something. Again, just look for convention that we've got across our Norwich Islands repos." Read as ("stower" is Stoa, "Norwich Islands" is Knowledge Islands, and the garbled sentence is the script names): option b), all of it now. No trace of the portal-framework or earlier names remains in packages-stoa, decision records included; the scripts and developer tooling follow the conventions across Knowledge Islands repositories, adding the house development dependencies to the repository; the GitHub settings are aligned with the standard.

## 2026-11-08 12:20 GMT - STOA-WINDOW - deliver to review, no release

home: ../packages-stoa/docs/roadmap

class: operational

- Kris, 8 November 2026, answering STOA-WINDOW, chose "Deliver, no release": capture each Stoa inbox request as a roadmap record, plan it, and build the defects and small asks through to awaiting review; plan the bigger designs only, for his look; release nothing.

## 2026-11-08 12:20 GMT - STOA-ACCEPT - Kris accepts

home: ../packages-stoa/docs/roadmap

class: operational

- Kris, 8 November 2026, answering STOA-ACCEPT, chose "No, I'll accept": records stop at awaiting review and come to him as one bundle when he is back.

## 2026-11-08 12:25 GMT - STOA-WINDOW grant - unattended window while Kris is away

home: ../packages-stoa/docs/roadmap

class: operational

- Grant: Kris, 8 November 2026, "Do you want to prompt me on some things if you need that so we can get some items moving while I'm away?", then STOA-WINDOW and STOA-ACCEPT above.
- Return condition: Kris's next message in this thread, or "stop the wake". No clock end was given; none is assumed.
- Work: the 14 Stoa request lines in `messages.md`. The coordinator captures each as a roadmap record in `packages-stoa` from run-drafted text, adopts it to `next` under STOA-WINDOW, has it planned to Ready, and delivers the defects and small asks to `awaiting-review` in frozen waves in `packages-stoa`; the bigger designs (heading links, page types, print layout, diagram overlay) are planned only.
- Permitted: local commits and fast-forward pushes of `main` in `packages-stoa` and of this work folder in `ki-principal`, under the standing push rule; `bun install` of what the lock already pins.
- Excluded: any release, version bump, tag or consumer re-vendor notice; acceptance, cancellation and pruning; GitHub settings; new software or new dependencies; writes in any other repository beyond message lines this work sends. No deny-list item is lifted.
- Revisions at entry: `packages-stoa` `origin/main` and `main` `9c657a3`; `ki-principal` `origin/main` and `main` `b8439755`.
