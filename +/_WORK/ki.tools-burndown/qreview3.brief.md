# qreview3 - blind review of two queries

Blind query review under the ki-coordination standard's Query review section. Context, Query and Options only; option letters carry no ranking. Check what you can directly and read-only in /Users/krisbrown/workspaces/knowledge-islands/tools-ki (HEAD, `1cfc11a5`, `0720a053`, `c55a6c42`; run the full gate in a temporary clean worktree of HEAD and remove it), /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/work-package.md, and the reports in /Users/krisbrown/.local/state/ki/agents/tools-burndown/. No network calls; change nothing.

Write /Users/krisbrown/.local/state/ki/agents/tools-burndown/qreview3.report.md: one `### <TAG>` section per query with `**Pick:**`, `**Confidence:**`, `**Reason:**`, `**Checked:**`. Then stop.

## KI-RELEASE-GO - Cut the ki v0.11.5 patch release

**Context:** Through ki.ways-of-working you asked for one `ki` patch release "soon", carrying KI-TOOL-KI-CLI-155 so `priority` and `size` stop dropping 18 records, and a harness pin providing `ki-work-package` so ki-principal CI stops failing. Your standing rule is to ask before any `ki` release. `v0.11.5` now carries the pin (`c55a6c42`), KI-TOOL-KI-CLI-155, and KI-TOOL-KI-CLI-158, which lets `ki work status` see the migrated work packages that the released `ki` cannot see at all; the wpreader run reports the full gate green at `1cfc11a5`, with 1,354 tests at 100% coverage and `ki repo audit` FAIL=0. Another session has since added two roadmap-only commits (KI-TOOL-KI-CLI-159).

**Query:** May I tag `v0.11.5` on the current tools-ki HEAD after re-running the full gate there, push, publish, and send the tag to ki.ways-of-working?

**Options:**

a) Yes, on a green re-run at HEAD.

b) Tag `0720a053` without KI-TOOL-KI-CLI-158 and cut `v0.11.6` for it afterwards.

c) Bring the clean final candidate back to you before the tag.

### ROUTING-VIEW - A State of play routing view in ki

**Context:** Point 35 of the work-package design asks for a routing view for State of play: each work's id, state, pending count and description. KI-TOOL-KI-CLI-158 left it out because its brief did not list it; the `ki/work-status/v1` JSON now carries every field it needs.

**Query:** Should `ki` gain the routing view?

**Options:**

a) Capture it as a separate tools-ki triage record when State of play asks for it.

b) Capture it now and plan it straight after KI-TOOL-KI-CLI-158.

c) Leave it out: State of play reads the JSON.
