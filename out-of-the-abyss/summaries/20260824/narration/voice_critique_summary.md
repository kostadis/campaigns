# Voice Critique — Summary, session 20260824 (Chapter 65)

Five scenes, four narrators. Source: the `.scrubbed.md` variants (canonical pre-assembly input for `assemble.py`).

## Mechanical rule checks — all pass

| Genre-spec rule | Result |
|---|---|
| Portable tic `the shape of X` (doc cap 1, target 0) | **0** |
| Portable tic `with the [quality] of [someone who…]` (cap 1) | **0** |
| `the cusp of` / `what could only be described as` | **0** |
| Bookkeeping verbs, unlicensed narrators (Thorin, Zalthir) | **0** — correct |
| Bookkeeping per-section cap (1) | Daz `audit` s02, `tallied` s05 — within cap, nouns rotated |

The systemic failures the genre spec warns about are absent from this run.

## Flag counts

| Scene | Narrator | Flags |
|---|---|---|
| 01 The Long Descent | Zalthir | 2 |
| 02 The Lava Chamber and the Obsidian Tower | Daz | 2 |
| 03 Riddles of the Iron Guardian | Thorin Giantfriend | 2 |
| 04 The Spectral Silver Dragon's Trial | Gyrgum | 3 |
| cross-scene | — | 3 |

## Cross-scene findings

### [1] Cross-narrator image convergence — 03+05

> s03 L9 — "the air did that thing where a room is holding its breath at you"  ·  s05 L91 — "The dead air settled over me like a held breath."

**Why:** Two different narrators reach for the same held-breath image in one session. The genre spec calls cross-pollination the #1 cross-narrator failure: it collapses distinct voices into one. Thorin's version is the more developed of the two.
**Suggested action:** Keep Thorin's (s03 L9). Rewrite Daz's (s05 L91) in his own register: "The dead air closed over me. Nothing of mine reached past it."

### [2] Em-dash density (scan A) — all

> 33 narration-level em-dashes across the five scenes: s01 ×5, s02 ×9, s03 ×5 (one is a legitimate truncation), s04 ×5, s05 ×9.

**Why:** The genre spec licenses em-dash "for interrupted speech or thought." Most of these are appositive or parenthetical instead, which is a house-style default rather than a per-narrator choice. s02 and s05 (both Daz) carry nine each.
**Suggested action:** Run a targeted pass converting appositive em-dashes to commas, colons, or sentence breaks per narrator — keep the genuine interruptions (e.g. s03 L115 "and a new one—").

### [3] Scrub coverage gap (not a voice flag) — 01+02

> "Five hundred feet down the shaft…" (s01 L31), "another five hundred feet" (s01 L43), "two hundred feet floor to ceiling, a hundred across" (s02 L9), "a thousand feet below anything Candlekeep had a map for" (s01 L87).

**Why:** These are the same `foot_count` category you just ruled on, but `find_residue.py`'s NUMBER_WORDS table stops at *forty*, so spelled-out hundreds are invisible to the scanner and never reached the scrub artifact.
**Suggested action:** No prose change proposed — these read well as written. Flagging so you know the scrub pass did not consider them, and can widen NUMBER_WORDS if you want them offered next time.

## Strongest recurring theme

**Em-dash density.** 33 narration-level em-dashes across five scenes, concentrated in the two Daz scenes (nine each). The genre spec licenses the em-dash for interrupted speech or thought; most instances here are appositive, which is a house-style default rather than a per-narrator choice. That is the one pattern worth a systematic pass — everything else on this list is a single-sentence spot-edit.
