---
note_type: admin/operations/activity
tags:
  - card/note
  - topic/knowledge-islands
  - topic/work
status: current - April 2026
author: Written with Claude
---

# Activities

## Overview

This folder holds the island-specific timing configuration for Knowledge Islands Principal's automated activities. The generic activity patterns - what each automation does and why - are defined in [Activities](../../../Pillars/Philosophy/Model/Activities/Activities.md) under Knowledge Islands. What lives here is the timing model: the day-type taxonomy that automations read from daily note frontmatter to decide whether and how to run.

The authoritative record of which activities are enabled - the operational roster - lives in the [Charter](../../Governance/Charter.md). This folder is the timing model; the Charter is the activation record.

---

## Schedule

[Schedule](Schedule.md) defines the timing parameters used by all island automations. At its core is the day-type taxonomy - a classification scheme (`work-day`, `bank-holiday`, `annual-leave`, `weekend`) that automations read from each daily note's frontmatter to decide whether to run and how to behave. It also holds cron schedules for each named automation (Morning Briefing, Health Check, Knowledge Rebuild, and so on) as those automations are introduced. Currently no scheduled automations are active for Knowledge Islands Principal; entries are added here as they come online.

---

## Activity Definitions

Each activity is a flat `.md` file here. Naming follows the `[Group] [Name] Activity.md` convention.

| File                                                             | Group     | Notes                         |
| ---------------------------------------------------------------- | --------- | ----------------------------- |
| [Tending Activity](<Tending Activity.md>)                           | Tending   | Core maintenance loop         |
| [Briefings Activity](<Briefings Activity.md>)                       | Briefings | Morning briefing driver       |
| [Email Activity](<Email Activity.md>)                               | Email     | Vetoed - adoption record only |
| [Linear Activity](<Linear Activity.md>)                             | Linear    | Vetoed - adoption record only |

- [Schedule](Schedule.md)
- [Briefings](<Briefings Activity.md>)
- [Tending](<Tending Activity.md>)
- [Email](<Email Activity.md>)
- [Linear](<Linear Activity.md>)
