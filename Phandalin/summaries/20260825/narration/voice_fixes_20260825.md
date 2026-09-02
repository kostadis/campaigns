# Voice-critic fixes applied — session 20260825 (Chapter 50)

Applied 2026-08-31 after GM triage of `voice_critique_summary.md`. All nine findings
were marked **Act on it**; f9 needed no edit (scene 01 had already been re-narrated on
fable) and f8 resolved itself once f1 landed.

## ⚠ These edits live only in `.scrubbed.md`

`/scrub` regenerates `<scene>.scrubbed.md` from the raw `<scene>.md` via
`apply_scrub.py`. **A future scrub run on any of these scenes will silently wipe the
edits below**, because they are narration fixes rather than scrub decisions and are not
in `.scrub_state.json`. Re-apply from this file, or fold them into the raw `.md` first.

## 24 edits across 6 scenes

| Finding | Scene | Was | Now |
|---|---|---|---|
| f1 | 07 L103 | `I feel it land, clean, the way a good swing lands and nothing gets back up.` | `Nothing gets back up.` |
| f1 | 08 L129 | `I feel it land clean, the way a phrase lands when the room stops chewing to listen.` | `and the room stops chewing to listen.` |
| f3 | 02 L33 | `the way you square up to a magistrate` | `Shoulders back, chin out, feet planted.` |
| f3 | 04 L81 | `I hold the fact the way one holds a hot coal by choice` | `I close my hand around the fact and let it burn` |
| f3 | 06 L59 | `the way noble houses keep each other's secrets` | `Noble houses keep each other's secrets on the same principle.` |
| f3+f6 | 06 L71 | `The surface dwellers perform this ritual … the way a house understands shared poisonings` | `They finish each other's jokes, and finishing them is the point. In my mother's house we shared poisonings for the same reason.` |
| f4 | 01 L141 | `A small-business woman knows how food moves in a city.` | `Lim feeds people. She buys the food. She would see who buys too much for one mouth.` |
| f4+f7 | 04 L25 | `A tortle who counts what leaves a building is a tortle worth listening to. I file it.` | `She counts what leaves a building. Somebody taught her to, or something did. I keep it.` |
| f5 | 01 L79 | `Then Vukradin himself:` | `Then:` |
| f6 | 06 L17 | `because a party of surface dwellers will chase whatever glitters most recently` | `because Vukradin has already moved on to the next bright thing and Brewbarry follows Vukradin` |
| f7 | 06 L15 | `I file the observation as accurate.` | `The observation is accurate. I let it stand.` |
| f2 | 06 L87–L111 | past-tense flashback framed `Earlier, while we still pressed Lim, the calendar had been weighed.` | present tense throughout, framed `Then the calendar gets weighed.` — **12 edits** (1 frame + 11 speech tags) |

One further edit not from a finding: `I set it beside the rest` (04 L25, my first
replacement) echoed `I set it on the shelf` in 06 L71 — both Valphine. Changed to
`I keep it.`

## Deliberate keeps

The two doc-level frame findings are **cap breaches, not N defects**. The strongest
instances were kept, per the critique's own recommendation:

- **`the way X …`** — kept `Still the way a lute peg is still` (03 L37; Vukradin's own
  instrument, doing real work on a warforged) and `the way my mother taught me to
  assemble a rival house's supply lines` (06 L21; names a specific person and lesson).
  8 → 2 genuine instances.
- **`A [class] [verb]s …`** — cut the two that use a class to explain or judge a specific
  person (`A small-business woman…`, `A tortle who counts…`). Kept `A warrior checks his
  straps before battle` (01 L31; Brewbarry mapping the unfamiliar onto what he knows,
  and `Same thing.` is his syntax), `A performer knows the difference…` (03 L13;
  Vukradin about his own profession, not someone else's behaviour), `A being who counts
  your days deserves to be addressed properly` (03 L83; a normative claim, not an
  explanation), and `A merchant whose costs do not twitch…` (06 L21; economic deduction
  about a hypothetical, not a person).

**Scene 03 was therefore not edited at all** and still has no `.scrubbed.md`. That was
not a foregone conclusion — it was the only scene where the fix might have forced one
into existence.

## Correction to the critique

**Finding f2's ordering claim was wrong.** The critique asserted the scene 06 calendar
block had been moved ahead of material that preceded it in the extraction. Checking the
source sequence properly:

| `scene_extractions_smoothed/06_*.md` | material | narration |
|---|---|---|
| 240 | `"No, I'm going to have a rat familiar."` | L85 |
| 245–293 | the calendar / tea block | L87–L111 |
| 296 | `"Alright, so that's 3 in the morning…"` | L113 |

The block is **already in its correct source position**. The original comparison was
against the stakeout planning at 105–141 without noticing that the familiar discussion
at 207–240 also sits between them. Nothing was reordered, so nothing was moved.

The other two parts of f2 hold and were fixed: the past-tense shift (11 speech tags) and
the false `Earlier, while we still pressed Lim` frame, which asserted a flashback to
scene 05 for material that belongs to scene 06's own conversation.

## Verification after the pass

| Check | Before | After |
|---|---|---|
| `the way X …` genuine instances | 8 | **2** (both deliberate keeps) |
| `A [class] [verb]s` used to explain a person | 2 | **0** |
| `I file` | 2 | **0** |
| s06 past-tense speech tags | 11 | **0** |
| connective em-dashes in prose | 0 | **0** |
| `voice_lint` across all 8 scenes | 0 errors | **0 errors, 0 warnings** |
| narration prose, whole doc | 5,704 w | **5,909 w** |

**A word-count correction:** `voice_critique_summary.md` and the review artifact both
stated **6,704** words of narration prose. The per-scene figures in that same table sum
to **5,704** — the total was a transcription error, not a measurement error. Every
per-scene number and every ratio derived from them was correct.
