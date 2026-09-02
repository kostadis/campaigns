# Voice Critique — Vukradin, scene 05: Grave Robbers on the Quest Board

**Run:** 2026-09-02 · **Input shape:** per-scene · **Supersedes** the 2026-09-01 critique of this scene (the narration has been re-rendered since).

## Inputs resolved

| Input | Resolved to | State |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `0a3d011c5f27` | resolved — current rulebook |
| HARD BANS | `narrate/base.md` | resolved |
| Voice spec | `voice/vukradin_new_pipeline.md` | resolved (declared in `config/party.yaml`) |
| Examples | `examples/vukradin.md` | resolved |
| Global examples | none (`shared_examples:` absent) | ok |
| Party doc | `docs/party.md` | 4/4 PCs |
| `voice_lint` | 0 errors, 0 warnings | **but its bookkeeping/convergence checks silently do not run on per-scene input** (no `## Name — Scene` headings). Re-run on an assembled proxy: still 0 errors. |

**Doc-level budgets are not evaluable from a single scene.** See `voice_critique_summary.md` for the ledger.

## Prose measure

639 prose words / 1053 total — **60.7% prose**.

## Flags

### [1] A reclassified exchange was cut in half

> “Especially when we change the quest.”  *(l. 107)*
>
> *(stray blank paragraph, l. 109–110)*
>
> Soma pauses.  *(l. 111)*
>
> “Trying. Yes.”  *(l. 113)*

The trailing hatch reclassifies *"Are you trying to say something?"* as table speech, but its answer *"Trying. Yes."* stayed in the narration, answering a question the reader never sees. Line 97, *“No, that we're his favorite group of players.”*, is real-player table speech that also survived, and it sits inside a beat where it means nothing.

**Handoff:** `/scrub` — a reclassification has to take both halves or neither. Also fix the triple-newline at l. 109.
**Do not touch** the surrounding *quest / quest board / quest marker / fetch quest* vocabulary: canon per `notes/scrub_register_policy.md`.

### [2] Epigrammatic closers ×2 — contributes to the Vukradin breach

- l. 41 *"A clean exchange."*
- l. 59 *"The unwanted remainder of somebody else's belongings becomes municipal inventory."*

With scene 02's four, he is at ~6 against a budget of 1. Target 2 across both scenes; **keep 02:95**, trim these.

### [3] Unattributed dialogue — 2 runs

67–72 (*"No, no. The dwarf prospectors." / "That's honest money…" / "It just doesn't pay as much."*) and 103–110. Both are three-line and ambiguous between Vukradin and Soma. Low severity; tags from the smoothed layer would fix them.

### [4] Straight quotes

This scene uses `"` throughout while 01/02/04/07 use `“ ”`. Normalize at assembly.

## Verdict

The moral turn — fifty gold on the same sheet of paper as grave robbery, and *"Desperation wins."* — is the best beat Vukradin gets, and it is intact. The scene's problem is the broken tail at 97–113, which is a scrub-boundary defect rather than a voice one.

---
*Review only. Nothing here has been applied. Full ledger, cross-scene convergence and the GM scope calls are in `voice_critique_summary.md`.*

