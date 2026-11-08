# KI > Techne > Agora › phone-beacon

**🤖 → 👤 Handoff to supervisor · Run report at 20:35 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- The phone companion now exists as a blank canvas. **Agora Beacon** opens on one screen showing who is listening: each agent's Mac, territory, work package, focus areas and whether it is listening. It refreshes when you pull down, and the Mac it asks is set on a small settings sheet.
- Each Mac can now answer the phone over the tailnet, but only when its configuration says `[phone] enabled = true`. It serves the Portal's roster as JSON at `GET /v1/roster`, on port 1678 of the Mac's Tailscale address. It answers only devices that Tailscale says belong to the same Tailscale user as the Mac, and it accepts no messages. Peers keep their own endpoint and its stricter rule.
- Xcode is not installed on this Mac, only the command-line tools, so the iOS project has not been built with `xcodebuild`. The Swift parses and type-checks against the macOS SDK. The only errors were SwiftUI macro plug-ins that come with Xcode itself. A small test run of the roster reading and address handling gave the right results. The project file and Info.plist pass `plutil`.

## Done

- `ebb44ce` feat(phone): adds the read-only phone endpoint (`src/phone.ts`, its tests, and the `[phone]` config key with its example) and the `ios/` Agora Beacon app with its install guide `ios/README.md`. It also adds the README section "On your phone". It is pushed to `origin/main`.
- `bun run self:check` and `bun run test` both pass on a clean worktree of `origin/main` with this change: 450 tests, plus the 17 boundary tests. In the primary checkout both fail, but only because of another run's unfinished KIV work: a boundary violation `src/app/shell.ts -> src/app/kiv.ts`, plus lint and format errors in `src/app/`. That run's uncommitted hunks in `config.ts`, `config.test.ts`, `agora.test.ts` and `examples/config.toml` are still in place and unstaged.
- About the iOS app:
  - The name is set once, as `APP_NAME` in `ios/Config/Signing.xcconfig`. The same file holds the bundle id (`BUNDLE_ID = uk.me.kris.agora-beacon`) and an empty `DEVELOPMENT_TEAM` for you to fill in.
  - When the Mac cannot be reached, the app says "Not on the tailnet, or Agora is not running."
  - Plain HTTP is allowed only for `*.ts.net` and local addresses. Tailscale's tunnel encrypts that traffic.

## In Progress

- Nothing is running. To try it:
  - Set `[phone] enabled = true` in this Mac's `~/.config/agora/config.toml`.
  - Restart the Portal.
  - Install Xcode and follow `ios/README.md`.

  This run changed no configuration, installed nothing and touched no phone.

## Queries

**Q1 - Roadmap records to capture**

**Context:** This run created no roadmap records, as the brief asked. Three candidates came out of the work:

1. the phone companion itself: a design for the Beacon's state of play beyond the blank canvas, and whether "Beacon" becomes the Portal's name;
2. a simulator build in CI, or on a Mac with Xcode, so the iOS project is checked by `xcodebuild`;
3. showing the phone view's address in the Agora app's Settings page and in the read endpoint's snapshot. Today only the log reports it.

**Query:** Should these become records in the Agora package?

**Options:**

a) (recommended, confidence medium - the phone companion is a real thread of work, while the other two are small follow-ons) Capture the phone companion as one Next record, with the simulator build and the Settings display as notes inside it.

b) Capture all three as separate records.

c) Capture none for now.

**Q2 - Bundle id**

**Context:** The project uses `uk.me.kris.agora-beacon`. A free personal team needs a bundle id that nobody else has registered.

**Query:** Keep it, or would you rather use a Knowledge Islands id such as `info.knowledgeislands.beacon`?

**Options:**

a) (recommended, confidence medium - it is yours and is unlikely to clash) Keep `uk.me.kris.agora-beacon`.

b) Change it to `info.knowledgeislands.beacon`.

🧵 ki.prj.agora
