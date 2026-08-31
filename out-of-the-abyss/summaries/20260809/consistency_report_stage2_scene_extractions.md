# Consistency Report — Stage 2, `scene_extractions/`

**Session:** 2026-08-03 (played), exported 2026-08-09 — Chapter 63
**Run:** `/staged-consistency`, 2026-08-29, artifact mode.

---

## Method — the attribution audit

Every `> "quote"` line in all three scene files was normalised, matched back to a cue in
`GMT20260804-005646_Recording.transcript.cleaned.vtt`, and its tape speaker compared with the
`**[Speaker]**` block header it sits under. 262 verbatim blocks, ~460 quoted spans.

**Scenes 02 and 03 came back clean. All five misattributions were in scene 01.** After the
fixes below the audit returns **zero flags across all three files**.

This is the check that a summary-only pass cannot do, and it is why this stage exists.

---

## Findings

| # | Severity | Finding | Ruling |
|---|---|---|---|
| 1 | Critical | Five quotes in scene 01 filed under the wrong speaker | **approved** |
| 2 | Moderate | Scene 03 heading "his High Tower key" vs stage 1 "the High Tower keys" | **approved** |
| 3 | Moderate | Stage 1 lost the "*claims*" hedge on the Menzoberranzan name | **approved** |
| 4 | Moderate | Stage 1 "attempts to negotiate a surrender" vs "explicitly *not* a surrender" | **approved** |
| 5 | Minor | Carried from stage 1: A'lai's shriek rendered two ways | **KEEP** (see below) |

### Finding 1 — the five, with their tape lines

| Scene-01 line | Quote | Filed under | Tape says |
|---|---|---|---|
| L87 | "I assume his AC is higher than 9." | `[Thorin]` | **Grygum** `:923` |
| L91 | "Because my first girlfriend in high school was named Dawn." | `[GM]` | **Thorin** `:943` |
| L114 | "somebody is going to be upset later. I'm… I had a premonition to." | `[GM]` | **Daz** `:1265` |
| L133 | "Do you think the fireball was a hint?" | `[GM]` | **Grygum** `:1391` |
| L144 | "You take notes. Exactly." | `[GM]` | **Grygum** `:1441` (the GM then echoes it) |

⭐ **Two of these were already correct at stage 1** — `session-summary.md:62` credits the Dawn
line to Thorin and `:255` credits the fireball line to Grygum. For these five the scene layer
was the stale one, the reverse of everything else this run found. **Staleness does not live
at a fixed depth; check both directions every time.**

### Finding 5 — the shriek, and a ruling that went both ways

`session-summary.md:57` had the raw `"KAK THAT THING AWAY FROM ME!"`; `:102` and
`scene_extractions/02_*.md` had the corrected `[KEEP]`. Sequence on 2026-08-29:

1. Carded as an internal inconsistency; GM marked **discuss** with the note "Ack ".
2. Re-asked at stage 2. GM said in chat: *"the word A'lai said was Aack! Not KAK"*.
3. Applied as `AACK!` in 4 sites; the 08-19 glossary row was struck through as overturned.
4. GM corrected himself the same day: *"the ACK was wrong it should have been KEEP"*.
5. **Reverted. `[KEEP]` restored in all 4 sites**, and
   `notes/vtt_transcription_corrections.md:473` now records the row as *challenged and
   re-confirmed*, so no future pass re-opens it.

The sibling transcript `session_20260809_transcript.vtt` at `01:28:40.899` reads
*"Alei is like, **kick** that thing away from me"*. **A second ASR hearing the same short
monosyllable is not evidence against KEEP** — it is what made "Aack!" look plausible. The GM
voiced the line and is the authority. Recorded here because the tempting inference is wrong.

---

## Applied without asking

- Scene 01: quote tense `prepare` → `preparing their monographs` (the same file quotes it
  correctly at L142).
- Scene 02: Hill Strike bullet and its block header annotated — **Strike of the Giants
  (Hill Strike)**, GotG 19, on Thorin's sheet.
- Scene 02: guardian-ability bullet rewritten to the approved Sentinel wording. Its previous
  note claimed *"no such feature appears on his sheet"*, which was wrong.
- Scene 02: Street Justice and passive-Investigation corrections mirrored down from stage 1.
- Scene 02 L487: `"we should find out, Zalthir"` → `[Glabbagool]` — the third `Gabriel` hit,
  settled by the sibling transcript at `01:28:39.139`: *"We should find out, Glabbagool."*

## Upward propagation

`gm-assist.md:57` still carried the old scene heading after finding 2 was approved. Since
`enhance` reads that file, the next pipeline run would have re-injected both the plural key
and the non-simulacrum Manshoon. **Aligned in place** — gm-assist has been edited by two
prior passes, so it is not a preserved original. All three layers now carry the identical
heading. One word; revert freely if unwanted.
