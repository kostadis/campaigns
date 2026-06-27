# Voice Critique Summary — Session 20260623

**Source narration:** `gm-assist-doc.md` (assembled, 6 narrator/scene blocks)
**Per-scene reports:** `voice_critique_scene_NN_<narrator>.md`
**Reviewed:** 2026-06-26

## Flag counts by scene

| Scene | Narrator | Flags | Em-dash | Register-vocab | Voice-spec conflict | Cliché/metaphor/tell |
|---|---|---|---|---|---|---|
| 01 Return to Phandalin | Brewbarry | 6 | 5 | 0 | 0 | 1 |
| 02 A Hero's Welcome | Valphine | 13 | 11 | 1 (*shape of his own gift*) | 1 (*golden and warm*) | 0 |
| 03 UBT Proclamation | Vukradin | 10 | 8 | 0 | 0 | 2 (borderline) |
| 04 Cheese / Departure | Soma | 11 | 9 | 0 | 0 | 2 |
| 05 Arrival in Neverwinter | Vukradin | 14 | 12 | 1 (*angle*) | 1 (*We both knew how that goes*) | 0 |
| 06 The Exotic Armorer | Brewbarry | 8 | 4 | 1 (*measured*, borderline) | 1 (**whole-scene POV**) | 2 |
| **Total** | | **62** | **49** | **3** | **3** | **9** |

## Strongest recurring theme

**Em-dash density — 49 of 62 flags (79%).** Every scene leans on house-style nested
parenthetical em-dash asides. They read as LLM-default cadence and, in the
declarative-rhythm narrators (Brewbarry, Soma), actively fight the voice. This is a
mechanical sweep — convert to commas / colons / periods per the per-scene
suggestions. Consistent with the standing note that em-dash removal is part of every
voice-critic fix pass.

## Highest-severity single issue

**Scene 06 (Brewbarry) is written in third person** ("Brewbarry felt large," "He
thought") while Brewbarry's voice spec and both example passages are unambiguously
first person. This is a whole-scene conflict every sentence inherits — **the one block
that warrants re-narration rather than spot-editing.** Re-run `session_doc.py --scene 6`
with the first-person voice file rather than hand-converting 30 lines.

## Genuine voice-spec conflicts (beyond em-dash)

- **Scene 02 (Valphine):** *"golden and warm at the back of my burning eyes"* — "warm"
  is a soft-Lathander comfort word the spec says Valphine rejects; her dawn *burns*.
- **Scene 05 (Vukradin):** *"We both knew how that goes."* — hardboiled-noir
  knowingness the spec explicitly bars for Vukradin (he is an earnest optimist, not
  world-weary).
- **Scene 06 (Brewbarry):** third-person POV (above).

## Register-wrong vocabulary hits

- Scene 02: *"the shape of his own gift"* → sensory rewrite.
- Scene 05: *"strapped across his back at an angle"* → plainer spatial phrasing.
- Scene 06: *"He measured the man's face, not the numbers"* — borderline; "measured"
  is arguably in Brewbarry's contest-register, see per-scene note.

## Recommendation

- **Spot-edit** scenes 01–05: an em-dash sweep clears the bulk of the flags, plus the
  three named voice-spec/register fixes. Cheapest path, no re-narration.
- **Re-narrate** scene 06 to fix the first-person POV at the source.
- All reports are review-only. Apply fixes to the `.scrubbed.md` per-scene files (not
  the raw `.md`) so `assemble.py` picks them up — and re-assemble `gm-assist-doc.md`
  afterward.
