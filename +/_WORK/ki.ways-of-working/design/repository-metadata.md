---
note_type: streams/design
updated: 2026-10-24T16:30:00Z
author: Written with Claude
---

# Repository metadata

**Status:** a nascent area of Ways of working, being pioneered on the Valle Armonia territory. Other territory threads, personal-principal first, are invited to run it on their own territory and add their findings under [Other territories](#other-territories). Nothing here is a standard yet; the shape is expected to change as runs report back.

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Date:** 2026-10-24 · **Pioneered by:** [VA > SoP](/Users/krisbrown/workspaces/valle-armonia/va-principal/+/_WORK/va/work.md), whose [decisions log](/Users/krisbrown/workspaces/valle-armonia/va-principal/+/_WORK/va/decisions.md) holds Kris's words of 24 October from 16:46 BST, under TAG-APPLY, TAG-ROUTE, TAG-FORM and PROPOSALS

Repository metadata is what a repository says about itself to the outside: its description, homepage, topics, visibility, licence and which GitHub features it uses. This note proposes that every Knowledge Islands repository says the same thing on every surface that carries it, and that its topics include a small controlled taxonomy that `ki-repo` can derive and check.

It is separate from the [tags model](tags-model.md), which is about subject tags in the front matter of knowledge-base notes. That note's tags live inside a repository; this note's topics label the repository itself.

## The problem

The [repo-align survey](/Users/krisbrown/.local/state/ki/agents/va/repo-align.report.md) found the four Valle Armonia repositories consistent on everything the `ki-repo` standard checks today, and inconsistent on what it does not:

- No repository has GitHub topics. The standard requires topics only on public repositories, and all four are private.
- Both website repositories have a homepage and keywords in `package.json` that GitHub does not show.
- The two website descriptions are terse and have no full stop, unlike the other two.

The same pattern holds across the other private territories. Only the `knowledgeislands` organisation uses topics, only on its public repositories, and only ten of its 23 repositories carry `knowledge-islands`. No repository anywhere uses a GitHub homepage, and no topic says which territory a repository belongs to or what shape it is.

## Properties in scope

Each property has one source, and every other surface mirrors it. The source is in the repository, so that a change is a commit and an audit can compare the mirror with it.

| Property | Source | Mirrors | Checked today |
| --- | --- | --- | --- |
| Description | `.ki.toml` `description` | `package.json` `description`, GitHub description | Yes, GH-3 |
| Homepage | `.ki.toml` `homepage`, proposed | `package.json` `homepage`, GitHub homepage | Only that `package.json` has one, as a warning |
| Managed topics | Derived from `.ki.toml` | GitHub topics | No |
| Discovery topics | `package.json` `keywords` | GitHub topics | On public repositories, TOPICS-1 |
| Repository URL | `.ki.toml` `repository` | `package.json` `repository.url` | Yes |
| Visibility | `.ki.toml` `visibility` | GitHub visibility, `package.json` `private` | Yes |
| Licence | `.ki.toml` `license` | GitHub licence, `LICENSE`, `package.json` `license` | Yes |
| Issues | The declared work adapter | GitHub issues, `package.json` `bugs` | Yes |
| Wiki | Off | GitHub wiki | Yes |

Two rows are new.

**Homepage.** The proposal adds an optional `homepage` to `[skills.ki-repo]` in `.ki.toml`, mirrored to `package.json` and GitHub, in the same way as the description. A repository with no public face, such as a principal knowledge base or a harness, leaves it out, and then none of the three surfaces carries one. The homepage is where the thing is live now: a website before launch points at its preview, and all three surfaces move together at launch. The alternative is to treat `package.json` `homepage` as the source where a `package.json` exists, which needs no new key but leaves repositories without one with nowhere to declare it.

**Managed topics.** These are derived from declarations already in `.ki.toml`, so nothing new is declared. They are described under [The taxonomy](#the-taxonomy).

A repository with no `package.json` has no in-repository source for discovery topics. For now they stay on GitHub alone, judged under TOPICS-2; an optional `.ki.toml` key for them is left for the standard to decide if it proves needed.

## The taxonomy

Kris, 24 October 16:46 BST: "we should have tags which meet a particular category across all of the repos that we use. And any repo, for example, which is a Knowledge Islands one, should also be tagged with that as well ... there's things that are consistent within a given organization ... but also a territory, but also in the wider knowledge islands ecosystem. And I think this should be effectively tracked in the KI-WEPO ultimately."

Every Knowledge Islands repository, public or private, carries:

- **Ecosystem:** `knowledge-islands`, bare, because it is already in use and is the ecosystem's own name.
- **Territory:** exactly one `ki-territory-<prefix>`, such as `ki-territory-valle-armonia`.
- **Shape:** exactly one `ki-shape-<shape>`, such as `ki-shape-kb`.
- **Role:** `ki-role-capital` on the territory's Capital, and on no other repository.

There is no organisation topic. GitHub's `org:` search qualifier already covers ownership, and a territory can span several organisations: Humans Not Robots spans four.

### Form

Every managed topic matches `^ki-(territory|shape|role)-[a-z0-9]+(-[a-z0-9]+)*$`. The facet names are a fixed vocabulary of single words, so the first hyphen after the facet always ends it, and a multi-word value such as `humans-not-robots` or `homebrew-tap` keeps its own hyphens without ambiguity. The `ki-` prefix is reserved for managed topics, so no discovery keyword may start with it.

GitHub allows only lowercase letters, digits and hyphens in a topic, at most 50 characters each and at most 20 topics per repository. The longest value found, `ki-territory-humans-not-robots`, is 30 characters.

Kris's view, 24 October: "KI to indicate it's a KI tag, then a dash, and then the role of the tag ... shape", with the alternative "ki_shape_kb", using underscores between parts and hyphens within multi-word parts. Kris asked for a second opinion. The [tag-proposal run](/Users/krisbrown/.local/state/ki/agents/va/tag-proposal.report.md) confirmed from GitHub's [topic documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics) that underscores and colons are not allowed, so `ki_shape_kb` and `shape:kb` cannot be topics. This note takes its recommendation because it keeps Kris's `ki-` prefix and facet order, is the only form GitHub accepts, and needs no second separator once the facet names are fixed. TAG-FORM is still Kris's to settle in VA > SoP.

### Derivation

`ki-repo` derives every managed topic from declarations, and never from a checkout name, an organisation login or a work id:

- **Territory:** resolve the repository's `capital` to the Capital's `.ki.toml` and take its `territory_prefix`. Valle Armonia's is `valle-armonia`, not its harness prefix `va`.
- **Shape:** take the repository's own `primary_shape` and remove exactly one leading `ki-repo-`, keeping the rest whole: `ki-repo-kb` gives `kb`, `ki-repo-homebrew-tap` gives `homebrew-tap`. Supporting declarations such as `ki-repo-project` or the website content and Cloudflare overlays add no shape topic. A missing or unregistered shape fails visibly rather than being guessed.
- **Role:** a repository whose `repository` equals its declared `capital` is the Capital, provided the Capital's membership list includes it.

A derivation that cannot resolve, such as an inaccessible Capital, is reported as unresolved, never passed with an empty or guessed value.

## Discovery keywords

Discovery topics stay as they are: per-repository terms, chosen by judgement under TOPICS-2, such as `cloudflare-workers`, `static-site` or `mcp`. The managed taxonomy supplements them and does not replace them. A discovery keyword that overlaps the taxonomy, such as `valle-armonia` beside `ki-territory-valle-armonia`, is not invalid and stays unless a separate content decision removes it.

## Keeping managed topics out of npm

`package.json` `keywords` holds discovery terms only. The GitHub topic set is the keywords plus `knowledge-islands` plus the managed `ki-` topics, and TOPICS-1's comparison with the keywords leaves those out. A `ki-` topic never goes into `keywords`, so it never reaches npm or any other registry. A package may list `knowledge-islands` as a keyword where it wants that term on npm.

## Private repositories

Private repositories take part fully. Their topics are visible only to those who can see the repository, but topic names themselves are public on GitHub, so a managed topic only ever carries a declared, non-secret value. Description and homepage follow the same rule: nothing goes on a private repository's metadata that should not be readable by its organisation's members.

## Checks `ki-repo` would gain

1. **TOPICS-1, extended:** on public and private repositories, the managed set is present and exact. The audit reports missing, stale, duplicated, conflicting and unknown `ki-` topics, invalid or overlong values and the 20-topic limit. Existing `topics = false` overrides stay visible as overrides.
2. **TOPICS-1, keywords:** the comparison with `package.json` `keywords` excludes `knowledge-islands` and every `ki-` topic, and any `ki-` keyword fails.
3. **Derivation:** territory, shape and Capital role computed as above, with exactly one Capital per territory, and unresolved derivations reported as such.
4. **Homepage:** where `.ki.toml` declares one, `package.json` `homepage` and the GitHub homepage equal it; where it does not, neither carries one. The existing `package.json` homepage warning becomes this rule.
5. **Conform:** shows the exact topic, description and homepage changes as a proposal, keeps unrelated discovery topics, and makes no GitHub change merely because an audit ran.
6. **Recalculation:** a change to a territory prefix, primary shape, Capital or membership recalculates the affected topics and removes obsolete ones in an approved rollout. A rename within a territory changes no topic.

GH-3 is unchanged. The skill summary, rubric and checker help that restate TOPICS-1 and TOPICS-2 change with them.

## Rollout

1. **The standard.** `ki-repo` adopts the taxonomy, the homepage rule and the checks, with tests for multi-word values, shapes against overlays, private repositories, stale topics, renames, overrides, inaccessible Capitals and the length and count limits. Nothing is tagged before this lands; Kris, 24 October: "the right way to do it is not to make the changes right now".
2. **Valle Armonia.** One bounded, authorised run applies the [pilot](#the-valle-armonia-pilot) values to the four repositories on GitHub and in `package.json`, then audits them clean.
3. **Each other territory.** Each territory's State of play applies the same to its own repositories once the check is usable, through its own authorised run, and the Knowledge Islands cross-territory sweep picks up what remains.

Changing a GitHub setting is publication, so each application needs Kris's approval. Pushes to the website repositories are Kris's: they deploy, and they may carry other sessions' commits.

## The Valle Armonia pilot

The four repositories as surveyed on 24 October, with the values this proposal would give them. All four are private and `UNLICENSED`, with issues and wiki off, and all four already agree on those.

| Repository | Property | Now | Proposed |
| --- | --- | --- | --- |
| [va-principal](/Users/krisbrown/workspaces/valle-armonia/va-principal) | Description | "The canonical community knowledge base for Valle Armonia." | Unchanged |
| | Homepage | None | None |
| | Topics | None | `knowledge-islands`, `ki-territory-valle-armonia`, `ki-shape-kb`, `ki-role-capital` |
| | `package.json` | None | None |
| [va-agentic-harness](/Users/krisbrown/workspaces/valle-armonia/va-agentic-harness) | Description | "Valle Armonia home for extracting, developing, and maintaining reusable agent skills." | Unchanged |
| | Homepage | None | None |
| | Topics | None | `knowledge-islands`, `ki-territory-valle-armonia`, `ki-shape-harness` |
| | `package.json` | None | None |
| [apps-vallearmonia.com](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com) | Description | "Website for Valle Armonia Community" | "The Valle Armonia community website, vallearmonia.com." on all three surfaces, optional |
| | Homepage | `package.json` only: `https://vallearmonia.com` | `https://vallearmonia.com` in `.ki.toml`, `package.json` and GitHub |
| | Topics | None | `knowledge-islands`, `ki-territory-valle-armonia`, `ki-shape-website`, `cloudflare-workers`, `eleventy`, `static-site`, `tailwindcss`, `valle-armonia` |
| | `package.json` keywords | `cloudflare-workers`, `eleventy`, `static-site`, `tailwindcss`, `valle-armonia` | Unchanged |
| [apps-markhowarth.com](/Users/krisbrown/workspaces/valle-armonia/apps-markhowarth.com) | Description | "Website for Mark Howarth" | "The website of Mark Howarth." on all three surfaces, optional |
| | Homepage | `package.json` only: `https://apps-markhowarth-com.valle-armonia.workers.dev` | The preview URL on all three surfaces until launch, then `https://markhowarth.com` on all three |
| | Topics | None | `knowledge-islands`, `ki-territory-valle-armonia`, `ki-shape-website`, `eleventy`, `mark-howarth`, `static-site` |
| | `package.json` keywords | `eleventy`, `mark-howarth`, `static-site` | Unchanged |

The description changes are wording only and do not depend on the taxonomy. Whichever is agreed must change in `.ki.toml`, `package.json` and GitHub together, or GH-3 fails. The markhowarth.com homepage moves under the markhowarth-launch work, not before.

## Where it came from

Kris, 24 October 2026, 16:46 BST, asked for "a table that looks at that the repos so we can see them in the different kind of groups of repositories that we have, and if they're consistent with each other, or they need improvements, such as no tags", and wondered "if there's a way of tagging things with some kind of prefix, so it could be something like shape:knowledge-base or something shape:kb". The repo-align run produced the survey.

On TAG-APPLY Kris answered "the right way to do it is not to make the changes right now", and on TAG-ROUTE asked for "a prompt to deal with that, and I'll pass it back to the state of play thread in Knowledge Islands principal itself". On TAG-FORM Kris said "I like what you've suggested, but just to maybe do a little thinking on that one, maybe ask for some second opinion", which the tag-proposal run gave.

Under PROPOSALS Kris set the scope of this note: "In the same way that we put a proposal together around tending, I suggest that we put a proposal together around these two aspects", one being repository consistency, "the topics and tagging ... and the properties", which "extends into the package.json in those repositories that have one as much as it does into the GitHub values". The other is the [findings](findings.md) proposal, whose REPO-ALIGN finding is homed here.

## Other territories

Later runs add a `### <Territory> run, <date>` section here: what the territory's repositories carry now, where the proposed values or derivation did not fit, and what was missing, noting where their territory's shape differed.
