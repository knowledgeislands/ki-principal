---
note_type: streams/design
updated: 2026-10-24T16:46:00Z
author: Written with Claude
---

# Repository metadata

**Status:** a nascent area of Ways of working, being pioneered on the Valle Armonia territory. Other territory threads, personal-principal first, are invited to run it on their own territory and add their findings under [Other territories](#other-territories). Nothing here is a standard yet; the shape is expected to change as runs report back. Two of its questions are settled: Kris decided TAG-FORM and HOMEPAGE-SOURCE on 24 October, under [Decisions](#decisions).

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Date:** 2026-10-24 · **Pioneered by:** [VA > SoP](/Users/krisbrown/workspaces/valle-armonia/va-principal/+/_WORK/va/work.md), whose [decisions log](/Users/krisbrown/workspaces/valle-armonia/va-principal/+/_WORK/va/decisions.md) holds Kris's words of 24 October from 16:46 BST, under TAG-APPLY, TAG-ROUTE, TAG-FORM, HOMEPAGE-SOURCE and PROPOSALS

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

`.ki.toml` is the master. Description, topics and homepage are declared there or derived from it, and mirrored to `package.json` where one exists and to GitHub, never the other way round: conform never reads a GitHub or `package.json` value back into `.ki.toml`, a mirror that differs is drift corrected at the mirror, and a deliberate change starts as a commit to `.ki.toml`. Kris, 24 October, under HOMEPAGE-SOURCE: "things like the description, the tags, all these kinds of things should first and foremost be in the knowledge island config file, and then the request is that those things are then preserved into the package.json or into the github repos configuration. The master here is definitely the .ki.toml".

| Property | Source | Mirrors | Checked today |
| --- | --- | --- | --- |
| Description | `.ki.toml` `description` | `package.json` `description`, GitHub description | Yes, GH-3 |
| Homepage | `.ki.toml` `homepage`, proposed | Root `package.json` `homepage`, GitHub homepage | Only that `package.json` has one, as a warning |
| Managed topics | Derived from `.ki.toml` | GitHub topics | No |
| Territory topics | `.ki.toml` `territory_tags`, proposed, against the Capital's declared types | GitHub topics | No |
| Discovery topics | `.ki.toml` `keywords`, proposed | `package.json` `keywords`, GitHub topics | On public repositories, TOPICS-1, against `package.json` |
| Repository URL | `.ki.toml` `repository` | `package.json` `repository.url` | Yes |
| Visibility | `.ki.toml` `visibility` | GitHub visibility, `package.json` `private` | Yes |
| Licence | `.ki.toml` `license` | GitHub licence, `LICENSE`, `package.json` `license` | Yes |
| Issues | The declared work adapter | GitHub issues, `package.json` `bugs` | Yes |
| Wiki | Off | GitHub wiki | Yes |

Three rows are new, and the discovery row changes its source.

**Homepage.** Settled under HOMEPAGE-SOURCE: an optional `homepage` in `[skills.ki-repo]` in `.ki.toml`, mirrored to `package.json` where one exists and to GitHub, in the same way as the description. A repository with no public face, such as a principal knowledge base or a harness, leaves it out. The homepage is where the thing is live now: a website before launch points at its preview, and all three surfaces move together at launch. Kris took the independent review's four cautions with it:

1. **One landing page per repository.** `homepage` is the repository's single landing page, mirrored to the root `package.json` only. A workspace package's own `package.json` `homepage`, such as a published package pointing at its documentation, is that package's and is left alone.
2. **Validate the URL.** The value is an absolute `https://` URL with a host, no credentials and no whitespace, and the check fails anything else rather than mirroring it.
3. **Decide what omission means.** The proposal is that omission means no homepage: an audit reports a mirrored value left on `package.json` or GitHub as stale, and conform proposes clearing it, never clearing it unasked. This is for the standard to confirm before the check lands, since a repository that drops the key would otherwise lose a live homepage silently.
4. **Review before migrating.** Existing `package.json` and GitHub homepages are reviewed one by one before any is copied into `.ki.toml`, rather than guessed: a preview URL, a stale domain or a package-specific page may each be wrong to promote. The [pilot](#the-valle-armonia-pilot) shows both cases in Valle Armonia.

**Managed topics.** These are derived from declarations already in `.ki.toml`, so nothing new is declared. They are described under [The taxonomy](#the-taxonomy).

**Territory topics.** Declared per repository in `.ki.toml`, against the types its Capital declares, described under [Territory tags](#territory-tags).

**Discovery topics.** Declared in an optional `keywords` array in `[skills.ki-repo]`, so that a repository with no `package.json` has an in-repository source too. Where a `package.json` exists, its `keywords` mirror the array exactly. Migration copies each repository's reviewed `package.json` `keywords` into `.ki.toml` once; after that, `.ki.toml` leads.

## The taxonomy

Kris, 24 October 16:46 BST: "we should have tags which meet a particular category across all of the repos that we use. And any repo, for example, which is a Knowledge Islands one, should also be tagged with that as well ... there's things that are consistent within a given organization ... but also a territory, but also in the wider knowledge islands ecosystem. And I think this should be effectively tracked in the KI-WEPO ultimately."

`ki-repo` mandates these facets: every Knowledge Islands repository, public or private, carries:

- **Ecosystem:** `knowledge-islands`, bare, because it is already in use and is the ecosystem's own name.
- **Territory:** exactly one `ki-territory-<prefix>`, such as `ki-territory-valle-armonia`.
- **Shape:** exactly one `ki-shape-<shape>`, such as `ki-shape-kb`.
- **Role:** `ki-role-capital` on the territory's Capital, and on no other repository.

There is no organisation topic. GitHub's `org:` search qualifier already covers ownership, and a territory can span several organisations: Humans Not Robots spans four.

The facet vocabulary belongs to `ki-repo` alone; a territory adds its own types under its own code, as [Territory tags](#territory-tags) sets out, never a new `ki-` facet.

### Form

Settled under TAG-FORM, 24 October: hyphens only. Kris: "This is fine, but then if we expect, for example, to have particular tags, something like ki-territory and ki-shape and ki-role, for example, they should be mandated by the KI repo skill. And the KI repo skill should also say that any principal island can then define additional ones it expects. And we should say that any contextualization of the tag, for example, should be kept to a single word so that we can deal with this. And what that would mean, for example, would be if Valle Armonia had its own tags that it expected to be added, they would be something like va-<type>-<value>. Or more generally it would be <territory-code>-<type>-<value>".

Every managed topic matches `^ki-(territory|shape|role)-[a-z0-9]+(-[a-z0-9]+)*$`. The general form for every expected tag is `<namespace>-<type>-<value>`: the namespace, `ki` or a territory code, and the type are each a single word, so the first two hyphens always end them, and a multi-word value such as `humans-not-robots` or `homebrew-tap` keeps its own hyphens without ambiguity. The `ki-` prefix is reserved for managed topics, so no discovery keyword may start with it.

GitHub allows only lowercase letters, digits and hyphens in a topic, at most 50 characters each and at most 20 topics per repository. The longest value found, `ki-territory-humans-not-robots`, is 30 characters.

Kris's view, 24 October: "KI to indicate it's a KI tag, then a dash, and then the role of the tag ... shape", with the alternative "ki_shape_kb", using underscores between parts and hyphens within multi-word parts. Kris asked for a second opinion. The [tag-proposal run](/Users/krisbrown/.local/state/ki/agents/va/tag-proposal.report.md) confirmed from GitHub's [topic documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics) that underscores and colons are not allowed, so `ki_shape_kb` and `shape:kb` cannot be topics. This note took its recommendation because it keeps Kris's `ki-` prefix and facet order, is the only form GitHub accepts, and needs no second separator once the facet names are fixed, and Kris chose it.

### Derivation

`ki-repo` derives every managed topic from declarations, and never from a checkout name, an organisation login or a work id:

- **Territory:** resolve the repository's `capital` to the Capital's `.ki.toml` and take its `territory_prefix`. Valle Armonia's is `valle-armonia`, not its harness prefix `va`.
- **Shape:** take the repository's own `primary_shape` and remove exactly one leading `ki-repo-`, keeping the rest whole: `ki-repo-kb` gives `kb`, `ki-repo-homebrew-tap` gives `homebrew-tap`. Supporting declarations such as `ki-repo-project` or the website content and Cloudflare overlays add no shape topic. A missing or unregistered shape fails visibly rather than being guessed.
- **Role:** a repository whose `repository` equals its declared `capital` is the Capital, provided the Capital's membership list includes it.

A derivation that cannot resolve, such as an inaccessible Capital, is reported as unresolved, never passed with an empty or guessed value.

## Territory tags

`ki-repo` lets a principal island, a territory's Capital, declare further tags it expects its members to carry, in the form `<territory-code>-<type>-<value>`, as Kris set under TAG-FORM. Valle Armonia's would be `va-<type>-<value>`.

### The territory code

No existing `.ki.toml` field supplies a single-word code reliably. Across the eight Capitals in `~/workspaces`:

- `territory_prefix` is the right value for `ki-territory-`, but it is a slug and often several words: `valle-armonia`, `humans-not-robots`, `equal-remedy`, `sacred-inquiry`. A multi-word namespace would break the single-word rule that makes the form parse.
- `repo_code` without `-PRINCIPAL` gives `VA`, `HNR`, `KI`, `LGL`, `ER`, `SI` and `TMX`, but Personal's is `KB-PRINCIPAL`.
- `organisation_code`, under `[skills.ki-agent-coordination-paperclip]`, is Paperclip's: Valle Armonia declares none, Knowledge Islands' is `KIS` and Personal's is `KIT`.
- The harness capability prefix, Kris's `va`, is what [Derivation](#derivation) already advises against: territory is never derived from it, and `ki-repo-harness` keeps capability prefixes separate from territory identity.

The proposal is a new optional Capital key, `territory_code`, in `[skills.ki-repo]` beside `territory_prefix`: a single lower-case word matching `^[a-z][a-z0-9]*$`, required once the Capital declares any tag type, and governed by TERR-2 like the other territory keys. Valle Armonia would declare `territory_code = "va"`. This keeps the earlier advice intact: the code is declared, never derived from the harness prefix, even where, as in Valle Armonia, the declared value happens to equal it. `territory_prefix` keeps supplying the `ki-territory-` value.

Two values need care. Knowledge Islands' natural code is `ki`, which would put its territory types in the namespace `ki-repo` reserves; its Capital must therefore either declare a different code or never declare a type that `ki-repo` uses or may use, and the standard should say which. And codes must be unique across registered Capitals, as territory handles already are.

### Declaring the types

The Capital declares its expected types in `[skills.ki-repo]`:

```toml
territory_code = "va"
territory_tag_types = ["audience"]
```

Each type is a single lower-case word, unique, sorted, and never `territory`, `shape` or `role`. The example type is illustrative only: Valle Armonia declares none yet. A Capital that declares no types has no territory tags, and its members declare none.

Each member, the Capital included, declares its values in its own `.ki.toml`, so that the tags stay with the repository they label:

```toml
territory_tags = { audience = "community" }
```

A value is a slug matching `^[a-z0-9]+(-[a-z0-9]+)*$` and may hold hyphens. The repository then carries `va-audience-community` on GitHub. Territory tags are GitHub topics only and never reach `package.json` `keywords`.

### How `ki-repo` checks them

1. **Declaration:** on the Capital, `territory_code` and `territory_tag_types` are well formed, the code is unique across registered Capitals, and no type reuses a `ki-repo` facet; elsewhere, neither key appears.
2. **Membership:** each member declares exactly one value for every type its Capital declares, and no type its Capital does not. A repository whose Capital is inaccessible reports its territory tags as unresolved.
3. **Mirror:** the GitHub topics hold exactly the declared territory tags, with missing, stale, duplicated and undeclared `<territory-code>-` topics reported, and each topic within GitHub's 50-character limit.
4. **Keywords:** no `keywords` entry starts with `ki-` or with the territory's code and a hyphen.

## Discovery keywords

Discovery topics stay free: per-repository terms, chosen by judgement under TOPICS-2, such as `cloudflare-workers`, `static-site` or `mcp`, now declared in `.ki.toml` `keywords`. The managed taxonomy and any territory tags supplement them and does not replace them. A discovery keyword that overlaps the taxonomy, such as `valle-armonia` beside `ki-territory-valle-armonia`, is not invalid and stays unless a separate content decision removes it.

## Keeping managed topics out of npm

`.ki.toml` `keywords`, and the `package.json` `keywords` that mirror it, hold discovery terms only. The GitHub topic set is the keywords plus `knowledge-islands` plus the managed `ki-` topics plus any territory tags, and TOPICS-1's comparison with the keywords leaves those out. Neither a `ki-` topic nor a territory tag ever goes into `keywords`, so neither reaches npm or any other registry. A package may list `knowledge-islands` as a keyword where it wants that term on npm.

## Private repositories

Private repositories take part fully. Their topics are visible only to those who can see the repository, but topic names themselves are public on GitHub, so a managed topic only ever carries a declared, non-secret value. Description and homepage follow the same rule: nothing goes on a private repository's metadata that should not be readable by its organisation's members.

## Checks `ki-repo` would gain

1. **TOPICS-1, extended:** on public and private repositories, the managed set is present and exact. The audit reports missing, stale, duplicated, conflicting and unknown `ki-` topics, invalid or overlong values and the 20-topic limit. Existing `topics = false` overrides stay visible as overrides.
2. **TOPICS-1, keywords:** the GitHub topics compare with `.ki.toml` `keywords`, excluding `knowledge-islands`, every `ki-` topic and every territory tag; `package.json` `keywords`, where present, equal `.ki.toml` `keywords`; and any `ki-` or territory-code keyword fails.
3. **Derivation:** territory, shape and Capital role computed as above, with exactly one Capital per territory, and unresolved derivations reported as such.
4. **Territory tags:** the four checks under [How `ki-repo` checks them](#how-ki-repo-checks-them).
5. **Homepage:** where `.ki.toml` declares one, it is a valid URL and the root `package.json` `homepage` and the GitHub homepage equal it; where it does not, a mirrored value is reported stale, under the four cautions. Workspace packages' homepages are not checked. The existing `package.json` homepage warning becomes this rule.
6. **Direction:** every mirror is compared with `.ki.toml`, and drift is always remedied at the mirror, never by writing a mirror's value into `.ki.toml`.
7. **Conform:** shows the exact topic, description and homepage changes as a proposal, keeps unrelated discovery topics, and makes no GitHub change merely because an audit ran.
8. **Recalculation:** a change to a territory prefix, territory code, tag type, primary shape, Capital or membership recalculates the affected topics and removes obsolete ones in an approved rollout. A rename within a territory changes no topic.

GH-3 is unchanged. The skill summary, rubric and checker help that restate TOPICS-1 and TOPICS-2 change with them.

## Rollout

1. **The standard.** `ki-repo` adopts the taxonomy, territory tags, the `.ki.toml` keys, the homepage rule and the checks, with tests for multi-word values, territory codes and types, shapes against overlays, private repositories, stale topics, renames, overrides, inaccessible Capitals and the length and count limits. Nothing is tagged before this lands; Kris, 24 October: "the right way to do it is not to make the changes right now".
2. **Valle Armonia.** One bounded, authorised run declares the [pilot](#the-valle-armonia-pilot) values in each of the four repositories' `.ki.toml`, mirrors them to `package.json` and GitHub, then audits them clean.
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
| | Homepage | `package.json` only: `https://vallearmonia.com` | `https://vallearmonia.com` in `.ki.toml`, mirrored to `package.json` and GitHub, once reviewed as the live landing page |
| | Topics | None | `knowledge-islands`, `ki-territory-valle-armonia`, `ki-shape-website`, `cloudflare-workers`, `eleventy`, `static-site`, `tailwindcss`, `valle-armonia` |
| | Keywords | `package.json` only: `cloudflare-workers`, `eleventy`, `static-site`, `tailwindcss`, `valle-armonia` | The same in `.ki.toml` `keywords`, mirrored to `package.json` unchanged |
| [apps-markhowarth.com](/Users/krisbrown/workspaces/valle-armonia/apps-markhowarth.com) | Description | "Website for Mark Howarth" | "The website of Mark Howarth." on all three surfaces, optional |
| | Homepage | `package.json` only: `https://apps-markhowarth-com.valle-armonia.workers.dev` | The preview URL in `.ki.toml`, mirrored to both, until launch, then `https://markhowarth.com`, after review rather than by copying |
| | Topics | None | `knowledge-islands`, `ki-territory-valle-armonia`, `ki-shape-website`, `eleventy`, `mark-howarth`, `static-site` |
| | Keywords | `package.json` only: `eleventy`, `mark-howarth`, `static-site` | The same in `.ki.toml` `keywords`, mirrored to `package.json` unchanged |

The description changes are wording only and do not depend on the taxonomy. Whichever is agreed changes first in `.ki.toml` and is mirrored to `package.json` and GitHub in the same run, or GH-3 fails. Valle Armonia declares no territory tag types yet, so the pilot carries no `va-` topics; `territory_code = "va"` would be declared in va-principal only when a type is. The markhowarth.com homepage moves under the markhowarth-launch work, not before.

## Where it came from

Kris, 24 October 2026, 16:46 BST, asked for "a table that looks at that the repos so we can see them in the different kind of groups of repositories that we have, and if they're consistent with each other, or they need improvements, such as no tags", and wondered "if there's a way of tagging things with some kind of prefix, so it could be something like shape:knowledge-base or something shape:kb". The repo-align run produced the survey.

On TAG-APPLY Kris answered "the right way to do it is not to make the changes right now", and on TAG-ROUTE asked for "a prompt to deal with that, and I'll pass it back to the state of play thread in Knowledge Islands principal itself". On TAG-FORM Kris said "I like what you've suggested, but just to maybe do a little thinking on that one, maybe ask for some second opinion", which the tag-proposal run gave. Kris then settled TAG-FORM and HOMEPAGE-SOURCE, under [Decisions](#decisions).

Under PROPOSALS Kris set the scope of this note: "In the same way that we put a proposal together around tending, I suggest that we put a proposal together around these two aspects", one being repository consistency, "the topics and tagging ... and the properties", which "extends into the package.json in those repositories that have one as much as it does into the GitHub values". The other is the [findings](findings.md) proposal, whose REPO-ALIGN finding is homed here.

## Decisions

Both settled by Kris in VA > SoP on 24 October 2026, and folded into this note above.

- **TAG-FORM, settled:** "a) Hyphen-only": `ki-territory-<prefix>`, `ki-shape-<shape>` and `ki-role-capital` on Capitals only, beside bare `knowledge-islands`, with no organisation tag; the `ki-` facets mandated by `ki-repo`, and a principal island free to declare further expected tags as `<territory-code>-<type>-<value>`, each type a single word. Kris's words are under [Form](#form).
- **HOMEPAGE-SOURCE, settled:** "a) .ki.toml": an optional `homepage` in `.ki.toml`, mirrored to GitHub and to `package.json` where one exists, with the independent review's four cautions; `.ki.toml` is the master for description, tags and homepage. Kris's words and the four cautions are under [Properties in scope](#properties-in-scope).

## Other territories

Later runs add a `### <Territory> run, <date>` section here: what the territory's repositories carry now, where the proposed values or derivation did not fit, and what was missing, noting where their territory's shape differed.
