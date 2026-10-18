# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/rig.md) › [Mac Studio setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup/mac-studio-setup.md) › setup-note

**Run report at 23:53 BST · last mark 17:47 BST**

---

## Done

- **Captured [KB-DOTFILES-UE-094](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-094-guide-continuity-check.md)** in the chezmoi repository as unadopted triage: the Mac setup guide should gain a "Continuity Camera and Universal Control" check, citing Apple's guides 102459 and 102546, with the Universal Control requirements, the one-iPhone-one-Mac rule and the terra/sol fix as you gave them. It says nothing needs declaring in Rig and links KB-DOTFILES-UE-090 as related, which still exists. Not planned, not implemented, and the guide is untouched.
- **Title shortened.** The roadmap audit allows at most four words in a title, so the record is titled "Guide Continuity check". The full name of the check is in the Goal.
- **Commits** (local, `main`): `554c2cd` reserves the number in the issue ledger, which the capture flow requires to be committed on its own first. `1c43872` adds the record. Nothing else was touched.
- **Checks:** the roadmap audit passes and `rumdl` is clean on the record. The full `ki repo audit` has one failure, the missing `.claude/skills/ki-self` projection. It was there before this run and KB-DOTFILES-UE-092 owns it.
- **Not pushed.** `main` is three commits ahead of origin: my two, plus `bd04386` "docs(roadmap): point links at the renamed mac-studio-setup Project", which another session made. The brief allowed a push only if my commits were the only ones ahead.

## In Progress

Nothing.

## Queries

**SETUP-NOTE-PUSH**

**Context:** chezmoi `main` on sol is three commits ahead of origin: `bd04386` from another session, then my `554c2cd` and `1c43872`. A fast-forward push would publish all three.

**Query:** Should the three commits be pushed together?

**Options:** a) (recommended) Push chezmoi `main` fast-forward to origin, including `bd04386`, once its author's thread confirms it is finished. b) Leave all three unpushed for the Rig: chezmoi thread to push with its own work.

```text
SETUP-NOTE-PUSH: a) Push chezmoi main fast-forward to origin, including bd04386, once its author's thread confirms it is finished.
```

```text
╭─ run report · 2026-10-15T22:53:00Z ──────────────╮
│                                                  │
│  █▀▀▄ █▀▀▀ █▀▀▀ ▀▀█▀   · run done                │
│  █▀▀▄ █▀▀  ▀▀▀█   █    · record captured         │
│  █  █ █▄▄▄ ▄▄▄█   █    · 1 query: push           │
│                                                  │
╰──────────────────────────────────────────────────╯
```

- [at rest] setup-note finished; nothing running from this run
- [unpushed] chezmoi main on sol: bd04386, 554c2cd, 1c43872
- [uncommitted] setup-note.report.md in the thread folder and the run state folder

Resume: answer SETUP-NOTE-PUSH, then adopt KB-DOTFILES-UE-094 through ki-next when you want the guide changed.
