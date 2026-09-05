# Voice fixes — 20250812 (Chapter 8), applied 2026-09-04

Applied after the GM triaged all three findings in
`voice_critique_summary.md` as **ACT**.

> ## ⚠ THESE FIXES ARE FRAGILE
>
> Every narration fix below lives in a `.scrubbed.md` file. **`/scrub` regenerates
> `.scrubbed.md` from the raw `.md`.** The next scrub run on any of scenes 02, 04,
> 05 or 06 will silently wipe every edit in this file. They are not in
> `.scrub_state.json` and nothing else remembers them.
>
> **This document is the replay record.** If a scrub run wipes them, re-apply from here.
>
> Re-rendering a scene with `sd_narrate --scene N` destroys them the same way.

## F3 — false interruption assertions (root cause, `scene_extractions_smoothed/`)

These are edits to the **smoothed extraction layer**, not the narration, and are
therefore durable. A trailing em-dash on a quote asserts the speaker was
interrupted; the verbatim layer has zero and my smoothing introduced three.

| Scene | Was (mine) | Now | Why |
|---|---|---|---|
| 04 | `"…Really? I could have —"` | `"…Really? I could have."` | tape: `kostadis: I, I could have- Well, give her the mace` — same speaker continues |
| 06 | `"…any sort of —"` | `"…any sort of..."` | raw capture has an ellipsis; prefer the pre-smoothing punctuation |
| 03 | `"So let me just —"` | **kept** | tape: `kostadis: Um, so let me just- **wade:** Disadvantage on all saving throws` — Wade genuinely speaks over him. This dash *improves* on the raw capture's period. |

Scan A2 after: verbatim 0 → smoothed **1** (the correct scene-03 one) → narration 0.

## F1 — POV lexicon breach (`04.scrubbed.md`)

| Was | Now |
|---|---|
| `…and my bale arranged around every useful escape.` | `…and the others placed across every useful escape.` |

`my bale` is Soma's signature per `_genre.md` L15/L38 and `soma_new_pipeline.md` L43.
It was in Valphine's POV. Verified: `bale` now appears only in Soma's scenes.

## F2 — attribution beats added around orphan quote runs

**Rule followed: not one word inside any quotation mark was changed.** Every beat
is new narration placed *between* quotes, and every speaker was taken from
`scene_extractions_smoothed/NN_*.md`.

Beats added, by scene:

- **02** (`.scrubbed.md`, 2): `Vukradin has reached his own conclusion about the pair of them.` · `I give him the number.` · `Vukradin does not wait for me.`
- **04** (`.scrubbed.md`, 7): `Vukradin reads the total off before I can.` · `Soma measures the gap aloud.` · `Vukradin offers his encouragement.` · `Vukradin turns to the question of his own spell.` · `Brewbarry, from inside the sphere:` · `He is asking me. I consider the arithmetic and find it favourable.` · `Soma declines to let the contribution be diminished.` · `She puts the number in its proper proportion.` · `Soma watches the method rather than the result.` · `She supplies the insult herself.` · `Vukradin suggests a larger supply.` · `Brewbarry answers without hesitation. He has never counted them.` · `Soma asks after the hour.` · `Vukradin rules it shorter.`
- **05** (`.scrubbed.md`, 2): `Confirmation comes back.` · `Soma answers from the description.` · `She is already imagining it somewhere else.`
- **06** (`.scrubbed.md`, 5): `I offer the theory some support.` · `Vukradin approves of the choice.` · `I tell Valphine what the arithmetic requires.` · `Valphine considers her options.` · `It will not be.` · `Vukradin calls it before I can look.` · `I check anyway.`

### A collision I introduced and reverted

The scene-04 beat was first written as:

> Brewbarry answers **with the confidence of a man who** has never counted them.

That is the banned portable portrait (`with the X of a man who`) from `base.md`'s
HARD BANS — introduced by the very pass that exists to remove such things. Caught
by the mandatory post-fix re-scan and rewritten to
`Brewbarry answers without hesitation. He has never counted them.`

### Attribution corrections made before tagging

Fuzzy matching mis-assigned three short quotes; each was hand-verified against
the smoothed layer before a tag was written:

| Scene | Quote | Fuzzy said | Actually |
|---|---|---|---|
| 06 | `"Dead?"` | Vukradin | **Soma** |
| 05 | `"Yeah."` (window) | Vukradin | **GM** |
| 04 | `"Four damage."` ×2 | mixed | **Vukradin** both |

No line was tagged that the smoothed layer marks `UNKNOWN`.

## Before / after

| Metric | Baseline (verbatim input) | Re-render | After fixes |
|---|---|---|---|
| orphan quote runs | 11 | 16 | **2** |
| prose words | 4,318 | 4,151 | **4,319** |
| quoted spans | 165 | 186 | **186** (unchanged — no dialogue touched) |
| `my bale` outside Soma | 0 | 1 | **0** |
| trailing `—"` in narration | 0 | 1 | **0** |
| `voice_lint` | 0 err | 0 err | **0 err / 0 warn** |
| `extra_tics` (by hand) | — | 0 | **0** |
| connective em-dashes in prose | 0 | 0 | **0** |

The two remaining orphan runs were **cleared, not fixed** — both are the
legitimate shape the skill says to clear rather than flag:

- **02 l.115** — four consecutive lines, all Vukradin. One speaker, tagged opening.
- **05 l.85** — strict two-hander, Soma / Vukradin / Soma, tagged opening.

## Files

Scenes **01** and **03** were clean and have **no** `.scrubbed.md` — correct, since
`collect_scene_files` falls back to the raw `.md`. The effective assemble set is:

```
01 raw · 02 scrubbed · 03 raw · 04 scrubbed · 05 scrubbed · 06 scrubbed
```
