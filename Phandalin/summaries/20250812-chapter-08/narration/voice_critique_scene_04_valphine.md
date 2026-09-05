# Voice Critique — Valphine Sotorra, scene 04: The Harpy's End

**Narration:** `session_doc_scene_04_the_harpy_s_end.md`
**Input shape:** per-scene

> Doc-level budgets are evaluated across the whole document and live in
> `voice_critique_summary.md`. This per-scene report cannot assess them.

## Inputs resolved

| Voice spec | `voice/valphine_new_pipeline.md` | declared in `config/party.yaml`, exact-name match |
|---|---|---|
| Examples | `examples/valphine.md` | declared |
| Genre rulebook | `voice/_genre.md` | resolved |
| `voice_lint` | ran, 0 errors / 0 warns | `extra_tics` dropped — run by hand, 0 hits |

## Flags

### [1] BREACH — rulebook (POV lexicon)

**Why:** "my bale" is Soma's signature (_genre.md L15/L38); this is Valphine's POV. Regression vs baseline, where 'bale' appears only in Soma's scenes.

### [2] Unattributed dialogue

**Why:** 7 orphan quote runs — the most in the chapter. Lines 67-74 run four quotes across two speakers with no tag and no beat.

### [3] Provenance

**Why:** Line 81 ends a quote with an em-dash asserting interruption; the tape shows the same speaker continuing. Introduced at /voice-smooth, not by the narrator.

## Verdict

See flags above; the doc-level picture is in the summary report.
