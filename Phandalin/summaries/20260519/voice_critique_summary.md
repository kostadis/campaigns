# Voice Critique Summary — 2026-05-19 / gm-assist-doc.md

**Source:** `gm-assist-doc.md`
**Scenes critiqued:** 5 (Brewbarry × 2, Vukradin, Valphine, Soma)
**Per-scene reports:**
- `voice_critique_scene_01_brewbarry.md` — 6 flags
- `voice_critique_scene_02_vukradin.md` — 6 flags
- `voice_critique_scene_03_valphine.md` — 6 flags
- `voice_critique_scene_04_soma.md` — 6 flags
- `voice_critique_scene_05_brewbarry.md` — 6 flags

## Strongest recurring issue

**The "particular X of someone who Y" tic is systemic across the document.** Eleven hits across the five scenes, peaking in Soma's negotiation scene (5 in one section). It is a Claude-narrator default for "this character is being observant" that overwrites every POV's *specific* way of being observant:

- Brewbarry sees bodies and weight.
- Vukradin names corruption directly.
- Valphine reads people as systems of motive.
- Soma notices the physical world first.

None of them taxonomize behavior via *with the [adjective] [noun] of someone who…*. The pattern reads as one narrator pretending to be five.

Examples flagged:
- "with the cadence of someone sorting options for their own amusement" (Vukradin scene)
- "with the dry patience of someone who had seen too many apologies fail to materialize" (Vukradin)
- "with the particular quality of attention she uses…" (Vukradin)
- "with the ease of someone who had done that for decades…" (Valphine)
- "with the particular timing she has that I still haven't fully mapped" (Soma)
- "with the efficiency of someone who has made this calculation before" (Soma)
- "with that particular stillness of someone who has learned that stillness is safer than motion" (Soma)
- "with the quiet competence of people who know how to hold a position" (Soma)
- "the particular warmth of a reconciliation he'd been waiting on" (Soma)
- "the quiet particular way she has of doing it" (Soma)
- "the particular way large violent things displace the air in front of them" (Brewbarry scene 5)

**Recommendation:** add `with the [Adj] [Noun] of someone who...` to the genre-level anti-pattern list in `voice/_genre.md`, alongside the existing "the shape of X" ban. The pattern is generic enough to belong at the genre layer, not per-character. (See OOTA memory `feedback_oota_narration_systemic_tics.md` — Phandalin appears to have the same issue.)

## Second recurring issue

**"The shape of X" — three hits in this doc.** Already banned in `voice/_genre.md`. Hits:

- Brewbarry scene 1: "The shape of belief doesn't always match the thing it's built around."
- Vukradin scene 2: "the shape of the moment made it two"
- Vukradin scene 2: "The shape of it was clear enough"

The ban is in the genre file but the pipeline didn't pick it up. Worth verifying that `_genre.md` is actually being hoisted into the rewrite prompts.

## Third recurring issue

**Brewbarry over-philosophizes in both his scenes.** Spec failure-prevention #6 and #9 explicitly forbid: long inner monologues, paragraph-length essays about Vukradin or his Uthgardt past. The doc has both:

- Scene 1: full paragraph meditation on Talos, sobriety, exile.
- Scene 5: three-sentence essay on Vukradin's music vs. other people's hearing of "music."

His examples in `examples/brewbarry.md` are the entire surviving record of his POV across chapters 1–15 — *two short passages*, both bodily and immediate. The narration is treating him like a literary-fiction protagonist; the spec treats him as the character who feels and acts with no space between.

## Per-scene voice-fidelity ranking

1. **Scene 3 (Valphine, lodge arrival)** — strongest. The orcish exchange and *painful dawn* landing are pure voice. Spot-edit.
2. **Scene 5 (Brewbarry, siege)** — closer than scene 1; combat bones are good. Spot-edit.
3. **Scene 4 (Soma, negotiations)** — bones are good (shell-sprouts, the Boney handoff, the cask wail) but drowning in the particular-X tic. Consider re-run.
4. **Scene 2 (Vukradin, planning)** — two "shape of" hits + lyrical Sending paragraph + workshopped epigram. Re-run candidate.
5. **Scene 1 (Brewbarry, spoils of war)** — the most philosophical-narrator-overwriting-character. Re-run candidate.

## Recommended actions

- **Cheapest path:** spot-edit the per-scene reports' top 2–3 flags by hand. Each report's top flag is the highest-leverage cut.
- **Medium path:** re-run scenes 1 and 2 (Brewbarry/Vukradin) with the voice files re-hoisted; spot-edit the rest.
- **Systemic path:** patch `voice/_genre.md` to ban the "with the [Adj] [Noun] of someone who…" pattern, then re-run the full doc. This is the only fix that addresses the cross-scene drift at its root.

The bones of every scene are sound — verdicts, beats, dialogue. The issue is one narrator wearing five hats.
