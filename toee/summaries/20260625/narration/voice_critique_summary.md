# Voice Critique Summary — 20260625 narration (7 scenes, 4 narrators)

**Inputs:** voice specs (`voice/{calmer,sequoia,zephyr,zinnia}_voice.md`) = authoritative.
**Per-char examples: none** — `examples/` holds only global *thematic* files, so all rewrites are `[grounded in spec]`.
**Scope:** the 7 `session_doc_scene_NN_*.scrubbed.md` files (canonical pre-assembly source).

## Headline

The narration is **strongly in-voice** — the `session_doc` pipeline's spec-hoisting is working. Across 7 scenes there is **one genuine voice-drift** and a handful of minor register reaches. The dominant cross-cutting issue is mechanical: em-dash density.

## Two systemic themes

1. **Em-dashes (Scan A) — house-style, every scene.** Counts: 01→11, 02→12, 03→12, 04→15, 05→23, 06→13, 07→6 (~92 total; most narration-level, a minority inside verbatim dialogue and must stay). I did **not** enumerate all ~70 narration dashes individually — each per-scene report gives the count + a representative conversion. The efficient fix is a per-scene sweep converting narration `—` → `;` / `:` / `.` (leave `—` inside `"…"` and `*…*`). Ask if you want the exhaustive list.
2. **Register-wrong vocabulary (Scan B) — mostly clean.** Most hits are defensible in context ("in bad shape" idiom; "shaped like sea creatures" literal; "angles clean" fits assassin Zephyr; "in the shape of" is Calmer's metaphor). Only two genuine clinical reaches: "reorganized… margin" (Zinnia, sc.01) and "reorganize you" (Sequoia, sc.03).

## Per-scene

| Scene | Narrator | Report file | Substantive flags | Verdict |
|---|---|---|---|---|
| 01 Gargoyle Ambush | Zinnia | `voice_critique_scene_01_zinnia.md` | 1 (clinical "reorganized… margin") + 1 defensible | Spot-edit |
| 02 Juggernaut's Rampage | Zephyr | `voice_critique_scene_02_zephyr.md` | 1 (cliché simile "like a floor giving way") | Spot-edit |
| 03 Fall of the Juggernaut | Sequoia | `voice_critique_scene_03_sequoia.md` | **1 real: Zephyr's ledger register bleeding into Sequoia** + 1 clinical | Spot-edit |
| 04 Looting the Water Temple | Sequoia | *(folded here)* | none substantive | Clean |
| 05 An Unexpected Petitioner | Zinnia | *(folded here)* | none substantive | Clean — strongest scene |
| 06 Belsornig's Hidden Cache | Zephyr | *(folded here)* | none substantive | Clean |
| 07 The Chamber of the Pool | Calmer | *(folded here)* | none substantive | Clean — strongest scene |

**On the folded scenes (04–07):** I wrote separate report files only for the three scenes with actionable voice flags. 04–07 carry nothing beyond em-dash density, so listing them here avoids four near-empty files.
- **04 (Sequoia)** — spec-true. Note: the closing "*By peaceful meat.*" is **in-voice**, a deliberate callback to his signature line ("How do you think we came into power? By peaceful meat?") — not a garble.
- **05 (Zinnia)** — the strongest in the set: "he'd rather be a mouse in our house than a corpse in his own", "the silence I bring into a space instead of words", "Gotcha." are all spec-perfect (perceiver + tradecraft vocab). Note its 23 em-dashes are inflated by Eelrich's long verbatim quotes, which stay.
- **06 (Zephyr)** — spec-true; "I'd taken the killing blow… I'm the one who decides how a job ends" mirrors the assassin spec almost verbatim. "Something had taken root in us" is a grounded callback to the GM's Temple-corruption quip, not generic.
- **07 (Calmer)** — the identity tension is captured exactly: "The same thing that has always wanted to charge the wrong thing alone" and "which of the two men I have become was going to move first" land his cover-becoming-real spec. "This was not a warning. It was a menu." is a keeper.

## Strongest recurring issue

**Em-dash density** (mechanical, every scene) is the only truly cross-cutting item. The single **content** issue worth acting on is Scene 03's register convergence — Sequoia narrating in Zephyr's "spend a man / cover the debt" ledger voice.

## Recommendation

All findings are **spot-edits**, not re-narrations — voice fidelity is high enough that re-running `session_doc.py` would risk more than it fixes (and would re-introduce the Zinnia pronoun bug). Review-only artifact; act on whichever flags you agree with.
