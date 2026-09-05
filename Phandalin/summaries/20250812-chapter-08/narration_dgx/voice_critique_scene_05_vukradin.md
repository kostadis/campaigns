# Voice Critique — Vukradin, scene 05: Exploring the Tower of Storms

**Narration:** `session_doc_scene_05_*.md` (raw `.md` — no `.scrubbed.md` exists)
**Input shape:** per-scene
**Prose words:** 759 · **quoted spans:** 60

> Doc-level budgets are evaluated across the whole directory in
> `voice_critique_summary.md` and are **not** evaluable from this file alone.
> Inputs-resolved table and the `voice_lint` skipped-check finding also live there.

## Flags

**Worst attribution in the chapter.** 60 quoted spans against 759 prose words, and **4 orphan quote runs** (L25-30, L47-58, L73-78, L105-114). The L47-58 run cycles three speakers, so alternation identifies nobody.

**Real player name in narration:** `Gary's voice cuts across the table — not Valphine, not anyone in the fiction.` This states the break from fiction outright. It also evaded `find_residue.py`, which loaded only the full name `Gary Young`.

**Fix is non-destructive:** `scene_extractions/05_*.md` labels every one of these quotes, including the Gary->Valphine/Brewbarry rulings settled in the Stage 2 pass. Add tags and beats around the quotes; change no word inside them.

**Verdict:** do not re-render — the prose is fine and the dialogue is verbatim. It needs attribution added, which is an edit pass against the extraction.
