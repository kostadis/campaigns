# Voice Critique Summary — session 20260727 (chapter 60, Candlekeep / High Tower)

**Narration critiqued:** 4 scenes, all re-run from `scene_extractions_smoothed/`
(01 @ 17:45, 02 @ 17:48, 03 @ 17:52, 04 @ 22:41 — no `.scrubbed.md` variants exist, raw `.md` used)
**Inputs available and used:** `voice/_genre.md`, `voice/grygum_voice.md`, `voice/daz_voice.md`, `voice/zalthir_voice.md`, `examples/grygum.md`, `examples/daz.md`, `examples/zalthir.md`, `docs/daz_backstory.md`, `narration/plan.md`
**Supersedes:** the 17:03–17:05 reports on the pre-smoothed drafts

| Scene | Narrator | Flags | Was | Heaviest issue |
|---|---|---|---|---|
| 01 Silence of Candlekeep | Grygum | 5 | 4 | Dawnbringer referent still lost |
| 02 Path to the High Tower | Daz | 6 | 6 | Two bookkeeping nouns stacked in one sentence |
| 03 Infiltration of the Lobby | Zalthir | 6 | 6 | Duplicated clause + `Whorlstone` fabrication |
| 04 Confrontation at the Tower | Daz | 6 | 6 | Opens on scene 03's closing beats |

## What the re-run fixed

**The wrong-layer bug is fully closed.** All five verbatim-only probe strings now return CLEAR across all four scenes — `who are, who are, who are here`, `than, about these raiders`, `I, sort of jumped the gun`, `let's, let's look out for somebody`, `Okay, so, and knowing what we know`. That was roughly a third of the previous flag list and it is gone at zero editorial cost.

**Em-dashes: 43 → 32 narration-level.**

| Scene | Before | After |
|---|---|---|
| 01 | 10 | **4** |
| 02 | 5 | **9** ↑ |
| 03 | 10 | **6** |
| 04 | 18 | **13** |

Scene 02 is the only regression.

**Zalthir's accounting register is entirely gone.** The previous draft opened `"I counted levels before I counted people"` and stacked four tally beats in the one narrator whose spec says an accounting-sounding section is wrong by definition. This draft has none of them, and replaces `blind arcs` with plain observation. That was the single heaviest flag last run.

**Still clean:** zero instances of `the shape of X`, `with the particular/practiced [noun] of…`, `what could only be described as`, or `the cusp of something`, across all four scenes.

## Strongest recurring theme: the model quotes the voice files instead of writing from them

New this run, and it shows up in two different narrators:

- **Scene 01** — `My old teacher had a habit of asking, at exactly the wrong moment, *what are you optimizing for?*` is `grygum_voice.md`'s illustration reproduced word for word, including "at exactly the wrong moment."
- **Scene 03** — `or possibly it was Brother Quellin` uses the exact name from `zalthir_voice.md`'s example, in defiance of that file's **IMPORTANT** instruction to invent a different monk every time. The previous draft got this right with Brother Tharusk.

What makes it diagnosable rather than ambiguous: **scene 03 gets it right four lines later** — `Brother Aldas taught it — or possibly Brother Harren` — two fresh names, correct uncertainty. The device is understood; one instance just copied the manual.

If this recurs after the next run, the cheapest fix is at the voice-file level: mark the illustrative lines as *examples of the pattern, not lines to reuse.*

## Second theme: three flags survived the re-run and will survive the next one

These are not source problems. Re-running produces them again:

1. **Scene 01 — the Dawnbringer referent.** The smoothed source preserves `"the four of you look at her"` byte-identical per your ruling. Both drafts render it as the four PCs looking at each other. Two runs, two source layers, same loss.
2. **Scene 02 — `working the same geometry I was`.** Zalthir's lexicon on Daz, same scene, same beat, both drafts.
3. **Scene 03 — `The Whorlstone entrance`.** Grygum said `"Yes. Entrance. Basically."` The model back-fills a Gracklstugh location name into the unfinished fragment. It reproduced from *two different input directories*, which rules out the source and confirms the fabrication.

All three are single-line hand-edits.

## Cross-narrator convergence worth one edit

Scene 03 and scene 04 respond to the *same* Grygum line with the same idiom:

> **Right on both counts.** …powerful wizards are more obsessed with staying alive than with fighting to the death. *(Zalthir)*
> **Correct on both counts.** …powerful wizards share one trait with Menzoberranzan matrons… *(Daz)*

Daz's is the better version — the matron comparison is his and nobody else's. Change Zalthir's to `He was right twice.`

## One mechanical defect

`scene 03 L91` — `Beside me, Daz was already weighingBeside me, Daz was already weighing the next thing`. The clause is emitted twice with no separator. Same class as the previous draft's `incomplete.I must` fusion, different location, so it is a recurring generation artifact worth grepping for after every run:

```bash
grep -nE "[a-z]{2}[A-Z][a-z]" narration/session_doc_scene_0*.md
```

## Recommended order of work

1. **Six hand-edits, no re-runs.** Dawnbringer (01), the stacked `running tally`/`arithmetic` and `geometry` (02), the duplicated clause and `Whorlstone` and `Brother Quellin` (03). None of these will be fixed by another generation pass — three have already proven that.
2. **Trim scene 04's opening to line 19.** The Bless / assessment / Guiding Bolt overlap is a **scene-boundary** problem between extractions 03 and 04, not a narration problem, so re-running cannot fix it either.
3. **Restore Milo Goodbarrel to scene 02.** He was in the previous draft, he is now absent from the whole document, and he is load-bearing for the Manshoon handout — `daz_milo_goodbarrel_the_long_play.md` assumes the party knows who he is.
4. **Em-dash sweep** across all four, heaviest in 04 (13) and 02 (9). Per-scene conversion lists are in the individual reports.
5. **Optional:** drop `*At least we have that.*` from scene 02 so scene 04's use lands undiluted; change scene 03's `Right on both counts`.

---

**This report is review-only.** Nothing in `narration/` was modified. There are no `.scrubbed.md` variants yet, so `assemble.py` will read the raw `.md` — hand-edits go there for now, or into `.scrubbed.md` if you run `/scrub` first.
