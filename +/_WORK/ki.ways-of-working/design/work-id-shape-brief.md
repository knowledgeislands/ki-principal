# Typed three-part work-package IDs: brief

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Date:** 2026-10-27

Owning work: `ki.ways-of-working`. Stage one only: this brief proposes choices; it adopts no IDs and authorises no renaming, migration, review loop or implementation.

## Problem

Current work IDs have different lengths and place their distinguishing information in different positions. The owner proposes an explicit type segment so packages group visibly by territory and kind. The design must clarify that grouping without changing what work owns or how it coordinates.

## Owner's proposal

> I'm coming back to you very soon by the way, but I was just thinking about something else which is that noticing the way that the packages are being used, the work packages that is, I'm wondering if we should maybe have first the first part being the territory, the second part being the type of work it is related to, so like a project one which would be like a PRJ, and then a state of play one, which would be SOP. We've obviously already got regular, so I think having the three parts of it would probably make the most sense, so we can see them in groups together clearly like that.

## Established facts

- **Current identity shapes:** main State of play is `<territory>` (`ki`); secondary is `<territory>.sop.<name>` (`hnr.sop.5ge`); Project work is `<territory>.<project>` (`ki.ways-of-working`); regular umbrella is `<territory>.regular` (`ki.regular`); ad hoc children are `<territory>.regular.<slug>`, including `ki.regular.registry-removal` and `personal.regular.tower`. IDs use lower-case kebab segments; the derived runtime slug replaces dots with hyphens and is never parsed backwards into an ID. Themes and hosts are absent from IDs. [Work naming][naming]
- **Levels and forms:** territory work coordinates; regular work and Project work are the two middle-level forms; work items execute. Regular work is self-coordinating, without a coordinator session, and its umbrella does not finish. Ad hoc work already uses the regular prefix. [Work Process][process]
- **Main and secondary SoP:** main remains the owner's front door and owns cross-cutting decisions; each secondary coordinates only its assigned coverage. Every package below main declares its coordinating SoP as `parent`, including ad hoc work: the regular prefix is not its parent. Main's `covers` register persists independently of package presence, and secondary coverage is an assigned subset. [Coordination][secondary]; [package identity][package]
- **Registry and sovereignty:** Project packages live in the Capital; a record's `project` remains the Project registry slug. Registry references confer no execution, priority or acceptance authority over another repository's records. [Project registry][registry]; [package identity][package]

## Reflection

1. **Recommend a common grouping grammar:** `<territory>.<type>.<name>`, with stored types `prj`, `sop` and `regular`. The owner's PRJ and SOP are display abbreviations; retaining lower-case stored segments follows the existing naming contract. This is a recommendation, not an owner decision about spelling or display titles. Themes remain display grouping only. [Work naming][naming]
2. **Proposed examples, not adopted IDs:** `ki.prj.ways-of-working` for Project work; `ki.sop.main` for main SoP; existing `hnr.sop.5ge` for secondary SoP; `ki.regular.main` for the regular umbrella. Existing ad hoc children such as `ki.regular.registry-removal` and `personal.regular.tower` already fit the proposed grammar and should provisionally retain their identities. The type segment describes grouping, not a new level or state.
3. **Leave the umbrella name choice open:** recommend `main` for both main SoP and regular umbrella for consistency, but the owner has not chosen either third segment. A descriptive name or a deliberate shorter-ID exception remains possible. Reserving `main` would require collision checks against existing secondary SoP names and ad hoc regular slugs before adoption. The regular umbrella's third segment must not turn its children into four-part IDs or imply a new parent relation.
4. **Preserve the model:** `sop` continues to mean `level: territory`, `prj` means Project work, and `regular` retains umbrella and ad hoc forms. Main/secondary responsibilities, explicit `parent` and `covers`, work-item IDs, Project registry slugs and sovereign repository ownership stay unchanged. For example, a future package ID change would leave `project: ways-of-working` and its flat Project note intact. Any changed relations would need explicit reference rewrites, not inference from prefixes. [Work Process][process]; [package identity][package]; [Project registry][registry]
5. **Compatibility is the substantial cost:** an approved rename would affect dotted folder names, identity fields and headings, `parent`/`covers` references and live links; derived runtime slugs, state folders and native-session bindings; CLI resolution, validation and openers; status/Observatory grouping; and message sender/target IDs and queued references. A later plan must define atomic boundaries, old-ID readability or alias duration and rollback, preserving historical reports and Git history. No compatibility policy is decided here. [Work naming][naming]; [package identity][package]
6. **Recommend a later bounded pilot:** after owner decisions and any separately authorised review, select one Project package and its directly dependent references/bindings. Prove lookup, resume, status and queued-message delivery, plus rollback, before any wider migration. Validate main/secondary SoP, regular umbrella and unchanged ad hoc examples as contract cases before extending the pilot. Do not rename this live owning package to demonstrate the proposal. This brief launches no pilot, reviewer or estate scan.

[naming]: <../../../../.agents/skills/ki-coordination/references/standards-coordination.md#work-naming>
[process]: <../../../../Pillars/Philosophy/Model/Processes/Work Process/Work Process.md#levels-and-forms-of-work>
[secondary]: <../../../../.agents/skills/ki-coordination/references/standards-coordination.md#secondary-states-of-play>
[package]: <../../../../.agents/skills/ki-work-package/references/standards-work-package.md#location-and-identity>
[registry]: <../../../../.agents/skills/ki-work/references/standards-project-registry.md>
