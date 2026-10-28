# KI Website › wow-docs-svg

**🤖 → 👤 Handoff to supervisor · Run report at 08:27 GMT · last mark 08:27 GMT**

---

## Done

- **Cause found.** The diagrams are not external files but SVG inlined by the `figure` shortcode into each Markdown page. markdown-it treats the figure as one HTML block that ends at the first blank line, and every exported SVG, site-owned and vendored alike, carries blank lines. Everything after the first blank line was rendered as prose, so `<p>`, `<ol>` and `<h2>` landed inside the `<svg>`; the browser ends an inline SVG at the first such element, so no diagram drew. All 21 docs pages that embed figures, 35 figures in total, were affected. The standalone SVG URLs were never broken: they returned 200 with `image/svg+xml` and well-formed bodies before and after.
- **Fix, commit a2942ea on main, pushed fast-forward to origin.** `fix(site): keep inline SVG figures whole through Markdown`. The shortcode in `apps/site/eleventy.config.ts` now drops blank lines before inlining; `verify:diagrams` reads every built page back and fails the build on prose markup inside a figure; unit tests cover the pass and fail cases; the developer diagrams guide records the behaviour. Four files, explicit paths only.
- **Checks:** site build passed with all 35 built figures clean; `bun run test` passed (117 site tests, 15 boundary tests); `ki repo audit --skill ki-engineering` passed (one pre-existing warning on the CI KI_VERSION pin); `ki repo audit --skill ki-authoring` passed (one pre-existing warning on `.rumdl.toml` drift).
- **Live verification at 08:26 GMT:** the Cloudflare deploy landed within a minute of the push. The reported page and `/docs/ways-of-working/the-work-model/` both return 200 with all figures intact and no prose markup inside any inline SVG. `skill-map.svg` and `work-model.svg` return 200, `image/svg+xml`, well-formed.

## In Progress

Nothing.

## Queries

None blocking. Three observations for the owner, none acted on beyond the unit:

- The push to `main` succeeded by bypassing two branch rules the remote reported: changes must come through a pull request, and the required `build` status check. The standing push rule in the brief authorised the push; the rules themselves are the owner's to keep or relax.
- The local `tooling/depcruise` install was behind its lockfile (dependency-cruiser 18.5.0 against the pinned 18.7.0), which failed the boundary suite until I ran `bun install --frozen-lockfile` there. That is a local, untracked refresh, not a repository change. The local Bun is 1.4.2 against the repository's 1.4.3 pin; the build and tests ran fine on it, and no software was installed.
- The site build warns that Eleventy also renders the vendored viewer HTML under `src/assets/diagrams/` as pages at `dist/assets/diagrams/.../index.html`, which nothing links to. Pre-existing, harmless to readers, and outside this unit.
