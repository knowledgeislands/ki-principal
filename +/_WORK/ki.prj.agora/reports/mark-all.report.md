# KI > Techne > Agora › mark-all

**🤖 → 👤 Handoff to supervisor · Run report at 03:51 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- From the tray, **Mark all → Mark and summarise** has every listening agent, on every Mac, strike its mark and reply with its Summary. **Mark only** asks for the mark with no summary, and the **No art** tick drops the art from the footer.
- **Broadcasts** now shows each mark as `mark: 5 marked, 2 silent`, so Kris can see at once which agents did not mark and say "mark" to them directly.
- A Mac still running the old Agora no longer holds back later broadcasts: it misses the mark, the menu shows it as `refused; install the new Agora there`, and every later broadcast still reaches it.

## Done

- **The `mark` broadcast is built and pushed** (`58c5c5d`), following the scope and Kris's answers of 6 November:
  - **Tray only:** a **Mark all** submenu under Ping threads, with **Mark and summarise**, **Mark only** and a **No art** tick. There is no command line.
  - **What it carries:** the broadcast is of kind `mark`, with `only` and `noArt` flags that are checked on receipt. Orca threads are woken with the fixed reason word `mark`.
  - **Acknowledgements** use the ping's path, so the Broadcasts menu shows `mark: <n> marked, <n> silent` and lists each agent that marked or stayed silent.
  - **Fixed words** sit in one place, `MARK_WORDS` in `src/broadcast.ts`, so they are easy to change while MARK-WORDS stays open.
  - **The words ask each agent:**
    - to date its mark at the sending time, even when it reads the mark late (MARK-LATE b);
    - when on hold, to strike its mark and give its hold report (MARK-HOLD b);
    - to only acknowledge when its own mark is already later, when a newer mark is waiting, or when it coordinates no work;
    - in every case, to acknowledge the mark.
  - **Older Macs (MARK-ROLLOUT):** the README says the households install the new Agora on every Mac before the first mark. This was a small change, so I also made it: a peer that refuses a broadcast now has it marked as refused and skipped, and the broadcasts queued after it still go through.
  - **README:** a new Mark section explains what an agent does on reading a mark. I also updated the Broadcast, waking and read-endpoint text, the view contract (`docs/api/view-v1.md`) and the CHANGELOG.
- **Choices I made:**
  - **Refused means not sent again.** A mark refused by an older Mac is not re-sent once that Mac is upgraded. A late mark would be stale by then, and Kris can mark again.
  - **How a refusal is recognised.** Only the peer's "does not fit" answer (HTTP 400) counts as a refusal. A Mac that cannot be reached keeps the broadcast queued, as before.
  - **Mark only with No art.** The words say "leave the art out of the footer" in both cases. A hold report given under Mark only may still have a footer.
  - **No art** is kept only while Agora runs. It is not saved in the configuration.
  - **Late or several marks.** The words tell an agent to act on the newest mark and acknowledge each, and to skip a mark when its own mark is later. This is the scope's late-pickup rule, combined with dating the mark at the sending time.
- **Checks:** `bun run self:check` passed (type check and Biome). `bun run test` passed, with 232 tests including the new mark and refusal tests, both before and after rebasing onto `main`.

## In Progress

- **Another session's commit.** While I worked, another session committed `docs(spec)` (the specification and How Agora works) to this checkout. Both its changes and mine are intact. I left `docs/how-agora-works.md` alone: it describes Ping, and a sentence on Mark should be added by whoever owns that page next.
- **Candidate record:** `KI-AGORA-TRY-002-mark-broadcast`, in the tray area. I did not create it.
- **Rule text for the coordination standard,** owned by personal.reg.inbox-sol, updated for Kris's answers. Under Striking, after "by saying "mark"", add: "or through a `mark` broadcast from Agora, which is the owner's own instruction to strike, with `only` and `noArt` read as "mark only" and "no art"; the mark is dated at the broadcast's sending time even when read late, the broadcast's id is recorded beside it, it is skipped when the thread's own mark is later, and only the newest of several is acted on; a thread on hold strikes and gives its hold report; every mark is acknowledged as a ping."
- **Before the first mark,** the households install this build on every Mac. Nothing has been installed, and the running `~/Applications/Agora.app` is unchanged.

## Queries

None.

🧵 ki.prj.agora
