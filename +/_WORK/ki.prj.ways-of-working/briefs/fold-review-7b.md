# Brief: fold-review-7

Work: ki.prj.ways-of-working. If `briefs/blind-review-7.packet.md` does not exist, do nothing and say so.

Otherwise, fold the blind review at `/Users/krisbrown/.local/state/ki/agents/ki-prj-ways-of-working/blind-review-7b.report.md` into `queries.md` for every query in the packet. Map the reviewer's options to the query's lettered options by their text. For each query, add a line before **Options:** reading `**Blind review (31 October, Codex, high effort):**`, saying whether it agrees or differs, its pick, its confidence and its reason.

Where it agrees, lift the recommended option's confidence one level, with the reason beginning `reviewed`, unless the agreement rests only on an earlier decision. Where it differs, show both views in the recommended option's reason. Split any query still below high into separately tagged parts where a clean split exists.

Change no other query. Commit `queries.md` alone by explicit path and push fast-forward only. Report each query's final recommendation and confidence in plain English.
