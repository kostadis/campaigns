# /no-mech manifest — session 20260830, Chapter 34 "The Sleeper in the Iron Coffin"

Run 2026-09-05, immediately after `/voice-smooth` and **before `sd_narrate` has ever run** on this
session. That ordering is the recommended one: there was no `plan.md` and no `narration/`, so Phase 4
(re-narrate) did not apply and no seams needed walking.

Layer edited: `scene_extractions_smoothed/` only. `scene_extractions/` and both VTTs verified
unmodified (`git status` reports 0 changed files in either).

## Result

| Scene | Before | After | Cut | Mode | Ruling |
|---|---:|---:|---:|---|---|
| 01 The Missing Prisoners | 56 | 52 | 4 | spans | cut the one Investigation roll exchange |
| 02 The Garbage Room and the Fire Temple | 249 | 180 | 69 | spans | cut the fight, **keep** the dice meltdown |
| 03 The Supply Room Ambush | 314 | 82 | 232 | spans | cut the combat block, **keep** 37 beats |
| 04 Administrative Headaches | 47 | 47 | 0 | — | no table speech; left alone |
| 05 A Message from the Shadows | 54 | 54 | 0 | — | no table speech; left alone |
| 06 Return to Nulb | 36 | 36 | 0 | — | no table speech; left alone |
| **total** | **756** | **451** | **305** | | |

(Counts are `apply_cut.py`'s, which counts `> "…"` quote lines. A raw `grep -c '^> '` gives
799 → 469 because it also counts italic-only stage-direction lines such as `> *Calmer nods.*`.)

## Why the triage signal was dead, and what replaced it

`scan_quotes.py --party-config` triaged **all six scenes** as
`REVIEW CLOSELY — no NPC speaker labels; may be all-mechanical`. That is a false signal here, and
it is **structural for this campaign**, not a one-off:

> toee's extractor never breaks NPCs out into their own speaker label. Every NPC line is
> `**GM** — *as Varek Solain, …*`. The label is always `GM`; the identity lives in the italic
> stage direction.

So the NPC-label signal will be dead on every future toee run. **Use the italic direction instead** —
`*as <NPC>,*` marks in-character speech reliably, and this session had 87 such blocks
(Varek Solain 30, Calmer 20, Dren Halveth 17, Falrinth 11, the hooded figure 9).

Pattern-flag recall was likewise a floor: 68 of 314 flagged in scene 03, where the true figure was
232. And a keyword-level cut of scene 03 left orphan rubble behind — `"Me?"`, `"Yes, you are up."`,
`"Pistol?"`, `"Did you?"`, `"How much?"`, bare numbers — while still keeping the Stunning Strike
rules lecture. **The cut that worked was the inverse: cut the combat block, keep an explicit
hand-read list of beats.**

## The Calmer complication

`**GM**` is not only the GM. Kostadis plays Calmer, so his lines carry the GM label and are split
only by the italic direction. Cutting on the `GM` label alone would have destroyed a PC's entire
performance. Every `*as Calmer,*` block was excluded from the cut by construction.

## Deliberately kept inside otherwise-mechanical stretches

Scene 02 — Calmer proposing Hold Monster; Sequoia's 20-line dice meltdown (`"HOLY DICE!"`,
`"WHAT THE F!"`, `"I averaged two."`, `"Average of bloody two, bro!"`); `*Sequoia curses at
Frostbrand.* "You had one job."`; `"This new spell of mine is very effective."`; the kill.

The meltdown was put to the GM as its own decision precisely because it is pure table speech by the
classifier — a player swearing at dice, not a character speaking. **Ruled KEEP**: it is the session's
funniest sustained run and it is about his intelligent sword.

Scene 03 — 37 beats: the creature read-aloud; `"May the blessing of the Earth God be with you."`;
the GM's characterisation of Calmer's spellcasting; the five-limbed assault and `"misses all five
times. Wow."`; the healing argument (`"Are you okay, Sequoia?"` / `"My guess is not an answer. Yes
or no."` / `"Just don't blame me when your logistics breaks down."`); `"Nice and hungry."` /
`"Vicious little predators."`; and the whole aftermath through Zephyr's Undercommon attempt.

## Orphans

`apply_cut.py` reported **zero** orphaned acknowledgements across all three files, and a
post-apply sweep found **zero** orphaned speaker labels.

Two residues were found by reading and **deliberately left alone**, because folding them in would
have widened a ruling the GM had already given:

1. **`"24? You immediately recognize this as the equipment of the Greater Temple."`** (scene 03) —
   the `24?` is a surviving roll result inside a line that is otherwise read-aloud. Trimming it is a
   word change to a *kept* quote, not a cut, so `/voice-smooth`'s "no card, no change" applies.
2. **`"Alrighty. So, unless you figure it out as players, you don't figure anything out. Okay."`**
   (scene 03) — squarely GM-to-player-as-player and squarely in the class the GM ruled CUT, but it
   was not on the list presented, and generalising a ruling past its stated scope is itself a
   judgment call.

Both are open proposals, not defects.

## Scrub-register consequence

Cutting scene 03's combat block removed **two of the four scrub-flagged real-world player names**
from this layer: cue 750 (`"Alright, Nick, good for avoiding the surprise round."`) and cue 1023
(`"George."`). `scrub_flags.md` still tracks both, because that file covers the tape, not the derived
layer. The two that remain in the smoothed layer are cue 200 (`"Nick, you're the completionist."`,
scene 02) and cue 1265 (`"Sorry, Thomas, I forgot."`, scene 06).

## Carry forward

- `sd_narrate` has still never run for this session (CF1). When it does, it should read
  `scene_extractions_smoothed/`.
- Re-running `scene_extract` discards both this pass and `/voice-smooth` (CF22).
- Standing rulings from this run are recorded in `notes/scrub_register_policy.md` (created
  2026-09-05, closing CF20).
