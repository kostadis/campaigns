# Correction Note: KP's Identity and the Kostadinious Attribution

**Status:** Staging. Needs human review before promoting any fix into grounding docs or re-mining the mempalace.
**Filed:** 2026-04-20 by Claude, at DM's direction.

## The problem

LLMs querying the mempalace repeatedly misidentify **KP** as "Kostadinious the Sage." This has happened enough that the DM has flagged it twice as a recurring hallucination.

## Ground truth

**KP = Kazneporium Ketternopappux, a gnome.**

Canonical source doc (already in the palace, phandalin/world):
- `The Self-Aggrandizing Gnome- Kazneporium Ketternopappux's Misadventures.md`

Biography (per palace contents):
- Clever librarian from the Kron Hills.
- Fought alongside Bayard, Rimardo et al. in a planar-spanning war with the Drow Empire; used a staff of power to end Lolth's reign.
- Lecture circuit → exploration of the Dark Realms → trapped in Barovia.
- Post-Barovia: pursues "cosmic engineering" / "multi-planar optimum for economic efficiency" — streamlining interplanar routes through Toril.
- His experiments coincided with Gromph Baenre's, contributing to Lolth's release. Views collateral damage as "minor miscalculations."
- Trapped mind flayers on Toril using Valentin & Bonk's artifact.
- Dispatched **Aletra Sotorra** (Valphine's sister) to Faerûn to manage "extraplanar leakage" — this drives the Planar Distortion arc.

## Why the hallucination happens

One source doc in the palace is titled:

> `KP post Barovia - Kostadinious the Sage.md`

Inside, the text reads: *"a short research note by Kostadinious the Sage a biographer."* So **Kostadinious the Sage is the in-world biographer recording KP's story** — not KP himself. The filename format (subject–author) is being read by LLMs as (alias–true name).

Additional contamination: a secondary doc (`Withering Grove.md`) spells KP's name as **Knazreponnium Ketternopappux** rather than the canonical **Kazneporium Ketternopappux**. Two spellings in the corpus increases the chance a generation pass invents a third.

Self-flag: in a prior session I hallucinated **"Knaz Pottermux"** as a "correction." That is also wrong. The only canonical spelling is **Kazneporium Ketternopappux**.

## Suggested fixes (for human review)

1. **Rename / retitle** `KP post Barovia - Kostadinious the Sage.md` to something unambiguous, e.g. `KP Post-Barovia - Biographer Note.md`, so the "Kostadinious the Sage" string no longer sits adjacent to "KP" in the filename.
2. **Normalize spelling** in `Withering Grove.md` — change `Knazreponnium Ketternopappux` → `Kazneporium Ketternopappux`.
3. Consider adding a one-line identity header to the top of `The Self-Aggrandizing Gnome...` doc: `KP = Kazneporium Ketternopappux, gnome. Aliases: "KP". Do not confuse with Kostadinious the Sage (his in-world biographer).` That header will show up in semantic search hits and vaccinate future LLM passes.
4. After any of (1)–(3), re-mine the phandalin wing so the palace reflects the corrected text.

## Do not do

- Do not silently edit or rename files in `docs/` from this note. Notes are staging. The DM reviews and promotes.
