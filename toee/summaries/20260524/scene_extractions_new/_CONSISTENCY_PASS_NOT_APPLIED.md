# Quote-consistency pass — REPORT ONLY, NOT APPLIED

**Date:** 2026-06-26
**Skill:** `/session-summary-consistency`
**Status:** ⚠️ Pass was **run as a report only**. **No edits were applied** to any scene file in this directory.

## What happened

A full quote-level consistency check was performed against
`notes/vtt_transcription_corrections.md` across all six scene files
(`01_…` through `06_…`). The findings were delivered to the user as a
report in conversation. The user elected **not** to apply the fixes.

The scene-extraction `.md` files in this directory therefore still contain
the original raw-VTT garbles, mishears, proper-noun errors, and player-name
speaker labels identified in that report. The `.reviewed` marker files
present here predate this pass and do **not** indicate these corrections
were made.

## Headline findings (not fixed)

- ~12 proper-noun / glossary errors (e.g. `Elsnor, Nick → Belsornig`,
  `bug beers → bugbears`, `ballmer → Calmer`, `hearts → Hartsch`).
- ~9 VTT mishears, ~6 garbled phrases, ~10 unrecoverable lines.
- 4 player-name speaker labels (`[george] → [Zinnia]`,
  `[Nicholas Roussos] → [Sequoia]`).
- 2 cross-scene duplicates (`She's dead`, `pompous passes`) that WERE
  resolved in the upstream `../gm-assist-doc.md` but were NOT propagated
  down here.

## ⚠️ Caution for any future apply

- `Elmo → Kelno` (scene 02): "Elmo" is also a live campaign NPC (the
  Verbobonc ranger). Do not blind find/replace.
- Two misattributions were flagged but NOT changed (a `[Zephyr]`-labelled
  Insight roll that is Zinnia's; a `[GM]`-labelled line that reads as a
  player's). Re-attribution requires confirmation.

To run the pass for real, invoke `/session-summary-consistency` on this
session dir and approve the fixes.
