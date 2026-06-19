# VTT transcription corrections — obelisk

**Single source of truth** for Zoom/Otter/Whisper proper-noun garbles in this
campaign's session transcripts. Wrong→right; the canonical (right) is **bolded**.

- The `vtt-spell-pass` skill reads and appends here
  (`add_to_glossary.py --glossary notes/vtt_transcription_corrections.md`).
- `docs/ensemble/aliases.json` is **generated** from this file (plus the
  bundling-only short forms in `docs/ensemble/build_aliases.py`) — never hand-edit
  aliases.json; re-run the generator.
- This file holds **only true garbles** — forms that are safe to substitute into
  transcript text. Entity short-forms, titles, and player→character mappings
  (e.g. `Sildar`→`Sildar Hallwinter`, `Nikhil Reddy`→`Zenvon`) must **not** be
  substituted into text (the word-boundary applier would double-expand them), so
  they live in the generator's `BUNDLING_ALIASES`, not here.

Canonical spellings are verified against `docs/background/name_glossary.md` and `characters/`.

## PCs

| Wrong | Right |
|---|---|
| Xenophon, Xenobon, Zenovon | **Zenvon** |
| Vera | **Veyra** |
| Sister Mela, Mela | **Sister Maela** |

## NPCs and creatures

| Wrong | Right |
|---|---|
| Clarg | **Klarg** |
| Toblin | **Toblen** |
| Glastaff | **Glasstaff** |
| Darren Edermeth | **Daran Edermath** |
| Oren Voss | **Orryn Voss** |
| Ruth exceeds | **Ruxithid** (garbled whispered name in "You're not what Ruxithid wants") |

## Locations

| Wrong | Right |
|---|---|
| Tresender Manor, Tressander Manor | **Tresendar Manor** |
| Eldermath Orchard | **Edermath Orchard** |
| Nethrel | **Netheril** |
| Tribor Trail | **Triboar Trail** |
