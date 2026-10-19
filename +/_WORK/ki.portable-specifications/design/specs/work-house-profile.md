# The Knowledge Islands work-package profile

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.portable-specifications` · **Date:** 2026-10-19

Written by the run revise under WORK-PROFILE (Kris, 19 October, "as recommended", read back: "the house work package stays a mapped profile of `work` with an explicit field and state mapping; the house rules move out of the spec into the profile"). It maps the house work package, as the `ki-work-package` [work-package standard](/Users/krisbrown/.local/share/ki/harnesses/knowledgeislands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md) defines it, onto the portable [work specification](work.md), draft 0.6. When the spec is homed, this mapping goes beside it in `ki-work-package`; the house standard itself does not change. The run revise-2 added the conversion rules and every destination key on 20 October, after the blind review of draft 0.2; the run revise-4 corrected the state file's identifier on 20 October, after the second blind review; the run revise-5 added the link rule on 20 October, after the third.

## Contents

- [Conformance today](#conformance-today)
- [Folder and files](#folder-and-files)
- [Conversion rules](#conversion-rules)
- [Work file](#work-file)
- [State file](#state-file)
- [Queries, messages and decisions](#queries-messages-and-decisions)
- [House rules the spec leaves to the profile](#house-rules-the-spec-leaves-to-the-profile)

## Conformance today

The house work package does not conform to `work` as built. The earlier claim in [specs.md](specs.md), that the `work` spec "holds nothing of the Knowledge Islands ways of working" and the house package "conforms to it as a profile", was wrong on both counts: draft 0.1 restated house practice, and the house package fails the spec's validation on:

- the entry file, `work.md` rather than `WORK.md`
- `work.md`'s identifier, `id` where the spec requires `name`
- top-level `work.md` fields outside the spec's closed list: `level`, `title`, `label`, `project`, `theme`, `worker`, `supervisor`, `created_at`
- `state.md`'s `id`, a top-level key outside its closed list; the spec requires no identifier in `state.md`, so the mapping moves it to `metadata.ki-id`
- `state.md`'s seven `state` values against the spec's four, `since` where the spec requires `updated`, and top-level `target`, `hold`, `blocking`, `received`, `beat`, `mark` and `method_read`
- links by absolute path, such as those in run reports and briefs, where the spec admits a package name, a URL or a relative path; the [link rule](#conversion-rules) converts those it can and reports the rest

Under WORK-PROFILE a), the house package stays as it is and a portable reader reads it through the mapping below. A package whose links all convert has a conforming portable reading; one with any unmapped external dependency does not, and the mapping says so rather than hiding it. The one change already decided is the entry file's case: ENTRY-NAMES (Kris, 19 October) renames `work.md` to `WORK.md`, a change routed to ki.ways-of-working. Until it lands, the mapping reads `work.md` as `WORK.md`.

## Folder and files

| House | `work` | Fit |
| --- | --- | --- |
| `+/_WORK/<id>/`, dotted id such as `ki.observatory` | Package directory named for `name`; `.` allowed between segments | Conforms |
| `work.md` | `WORK.md` | Maps; ENTRY-NAMES renames it |
| `state.md`, `queries.md`, `messages.md`, `decisions.md` | The same four files | Conforms |
| All five files from creation, `work.md` and `state.md` with their front matter and the initial state, the other three starting as `None` | All five from creation, `WORK.md` and `state.md` valid, the other three empty or `None` | Conforms |
| Run reports `<name>.report.md`, `briefs/<run>.md`, `design/` | Additional files and directories, allowed | Conforms; the spec's optional `references/` is not used |

## Conversion rules

A portable reader reads a house package through these rules, so that any two readers give the same result:

- **Destination keys:** a house field the spec does not define goes to `metadata` under `ki-` and the house field name, with `_` written as `-`: `created_at` becomes `metadata.ki-created-at`, `method_read` becomes `metadata.ki-method-read`. The tables below name every destination.
- **Strings:** copied unchanged, including holders such as `owner` or `run/<name>`.
- **Timestamps:** copied unchanged as their UTC RFC 3339 string, such as `"2026-10-19T11:25:41Z"`.
- **Booleans:** written as the string `"true"` or `"false"`.
- **Nulls and absent fields:** a field that is `null` or absent is omitted, never written as the string `"null"`. The house standard gives `null` and absence the same meaning for every field that admits `null`, `theme`, `received`, `beat` and `method_read`, so nothing is lost.
- **Mappings:** `hold` is split into its two keys, as the state file table shows.
- **Links:** a link target that is a package name, a URL or a relative path is kept unchanged. A target that is an absolute path is converted by the first of these that applies, decided from the path's text alone, whether or not it exists on the reading machine:
  1. **Internal:** the path contains `/+/_WORK/<id>/`, `<id>` being this package's own `id`. The part after it is the target's place in the package, with `work.md` read as `WORK.md`; it is rewritten as a relative path from the directory of the file that holds the link, such as `../WORK.md` from a file in `design/`. If it then does not resolve, the reading fails the spec's rule that an internal reference resolves, as any broken internal link does.
  2. **Supplied:** the reader has been given a canonical URL for the path or a directory that holds it, and the target becomes that URL with the rest of the path appended; or it has been given a package name for the path, which is then another package's directory or entry file, and the target becomes `package:<name>`.
  3. **Unmapped:** anything else, such as a path into another repository's checkout or the reading machine's own state, is left as it is and reported as an unmapped external dependency, naming the file and the target.

  A fragment is kept on the converted target. The same rules and the same supplied names and URLs give every reader the same result. A machine path cannot be made portable without one of the first two, so a package with any unmapped external dependency has no fully conforming portable reading: the reader reports each one and applies the rest of the mapping.

## Work file

| House field | `work` | Fit |
| --- | --- | --- |
| `id` | `name` | Maps by rename; the value conforms |
| `description`, at most 500 characters in the DESCRIPTION-SHAPE voice | `description`, at most 1,024 characters | Conforms; the house limit and voice are profile rules |
| `level` | `metadata.ki-level` | Maps |
| `title` | `metadata.ki-title` | Maps |
| `label` | `metadata.ki-label`, omitted when absent | Maps |
| `project` | `metadata.ki-project`, omitted when absent | Maps |
| `theme` | `metadata.ki-theme`, omitted when absent or `null` | Maps |
| `worker` | `metadata.ki-worker` | Maps |
| `supervisor` | `metadata.ki-supervisor` | Maps |
| `created_at` | `metadata.ki-created-at`, omitted when absent | Maps |
| No `spec` | `metadata.spec` absent, so `work/1` | Conforms |
| Body `# <id>`, `## Goals`, `## Scope` with `In:` and `Out:` lines | Recommended `## Goals` and `## Scope` | Conforms; the H1, the upward links and the `In:` and `Out:` form are profile rules |

## State file

| House field | `work` | Fit |
| --- | --- | --- |
| `id` | No field; the name is in `WORK.md` | Maps to `metadata.ki-id` |
| `since` | `updated` | Maps by rename; both are UTC RFC 3339 |
| `state` | `state`, with the house value kept as `metadata.ki-state` | Maps, by the state table below |
| `target` | `waiting-on` in `handoff`, and `metadata.ki-target`; omitted when absent | Maps |
| `hold.release` | `release` | Maps |
| `hold.reason` | `metadata.ki-hold-reason`, `"paused"` or `"more-expected"` | Maps |
| `blocking` | `metadata.ki-blocking`, `"true"` or `"false"`; omitted when absent | Maps |
| `received` | `metadata.ki-received`; omitted when absent or `null` | Maps |
| `beat` | `metadata.ki-beat`; omitted when absent or `null` | Maps |
| `mark` | `metadata.ki-mark`; omitted when absent | Maps |
| `method_read` | `metadata.ki-method-read`; omitted when absent or `null` | Maps |
| Body `## Now`, `## Next steps`, `## Held`, and `## Queue` for territory work | Free body: where the work stands and what whoever picks it up does first | Conforms; the sections and their caps are profile rules |

The seven house states map onto the four by Kris's four kinds of state in the Work Process note, "with someone", "handed off", "on hold" and "done":

| House `state` | Kind | `work` `state` | `waiting-on` or `release` |
| --- | --- | --- | --- |
| `with-worker` | with someone | `active` | - |
| `with-supervisor` | with someone | `active` | - |
| `handoff-to-supervisor` | handed off | `waiting` | `waiting-on` is `work.md`'s `supervisor`, copied unchanged |
| `handoff-to-worker` | handed off | `waiting` | `waiting-on` is `work.md`'s `worker`, copied unchanged |
| `handoff` | handed off | `waiting` | `waiting-on` is `target`, copied unchanged |
| `on-hold` | on hold | `on-hold` | `release` is `hold.release`, copied unchanged |
| `finished` | done | `done` | - |

This differs from draft 0.1's mapping, which put `with-supervisor` under `waiting`: in the house model the supervisor holds the work and the next move is theirs, which is the spec's `active`.

## Queries, messages and decisions

| House | `work` | Fit |
| --- | --- | --- |
| `queries.md`: `## Open` and `## Parked`, each query `### <TAG> - <title>` with a `since` line and **Context**, **Query** and **Options**, the recommended option first | Each query a `### <ID> - <title>` heading with its context and question; other headings allowed | Conforms; the tag style, the three parts, the recommendation and parking are profile rules. A parked tangent, a one-line list item under `## Parked`, is not a query to a portable reader |
| `messages.md`: `# <id> messages`, then lines `<date> · <TAG> · <sender title>: <message>`, `IMPORTANT` lines first | One list item per message with date, sender and message | Conforms; the tag, the `IMPORTANT` flag and the order are profile rules |
| `decisions.md` under `ki-coordination`'s decisions log: dated heading, the owner's words, the read-back and what it authorises | One entry per decision with a dated heading, who decided and the decision | Conforms; the read-back, authority and striking to a pointer are profile rules |

## House rules the spec leaves to the profile

Draft 0.1 of `work` restated these; draft 0.2 drops them, and they stay in the house standard and `ki-coordination`, where they already live:

- **The message queue:** priority order, `IMPORTANT` lines taken first and one at a time, grouping, who may place a line, the sender editing only its own line, and the commit subject (WORK-QUEUE-PRIORITY)
- **The owner-query form:** upper-case mnemonic tags, Context, Query and Options, the recommended option first with its confidence and reason, parking and putting back (QUERIES-FILE, PARKED-HOME)
- **The decisions life cycle:** the owner's words, the read-back, what an entry authorises, striking and reduction to a one-line pointer
- **The state file's caps and sections:** `## Now` at most five lines, the body at most 400 words, `## Next steps` and `## Held`, and the history check (STATE-HISTORY)
- **Routing:** the four-level progressive reveal with its Register level read by State of play, the description at most 500 characters in the "Takes ... Not for ..." voice (DESCRIPTION-SHAPE), and "Not taking new units"
- **The work folder's governance:** the closed list, entry points, tidying and close-out, the `+/_WORK_REVIEW/` holding area, holders, levels and the coordination declaration

A drift check, one rubric criterion in `ki-work-package` naming the spec's fields and this mapping, keeps the house standard and the portable spec from parting company as the house changes.
