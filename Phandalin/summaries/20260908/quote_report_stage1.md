# Quote Verification Report

**Generated**: 2026-09-12T14:23:19
**Transcript**: `Phandalin/summaries/20260908/session_2026_09_08_chapter_52_combat_at_last_transcript.cleaned.vtt`
**Threshold**: 0.85 (near/unverified boundary)
**Minimum tokens to score**: 4

| verdict | count | share |
|---|---|---|
| verified | 15 | 94% |
| near | 1 | 6% |
| unverified | 0 | 0% |
| unscored | 0 | 0% |
| exempt | 0 | 0% |

**Refused by the extraction contract (#250)**: 0.

## Not checked

- Inline `"…"` spans in prose — not reliably dialogue (a plaque honouring the "liberators of the Ordning" is a label, not speech). Only `> "…"` blockquotes are verified.
- Speaker attribution. This report answers *were these words said*, not *did this person say them*.

## Refused — the contract will not choose for you

Extraction contract #250 (`docs/design/ExtractionContract_proposal.md`), rules R1 and R3. A refusal is **not** a claim that the text is wrong. It is a claim that this pipeline is not the thing that should decide, so the span stays as it is until you rule on it. Nothing here was auto-corrected and nothing here will be — and nothing here is blocked either: `sd_narrate` still renders these. Refusal means flagged.

None. No span was refused by R1 or R3.

## Unverified — review these

None. No quote was untraceable to the transcript.

## Near — an edit happened here (traceable, not verbatim)

Most of these are disfluency edits: the extraction tidied a filler word out of a real line. Listed after the unverified section on purpose — they are the majority and should not bury the findings that matter.

**But `near` means *an edit*, not *a safe edit*.** Similarity cannot tell the two apart: a measured DeepSeek run scored `"My kind has been spreading violence"` (transcript: `"Mankind …"`) at **0.92** and the harmless `"No, I have"` for `"No, I, I have,"` at **0.94** — the meaning-changing edit ranked *below* the harmless one, and no threshold separates them, because both are edits of the same tiny size. Skim this list for changed *words*, not low scores.

### `session-summary.md:116` (§ Memorable Moments)

- **Quote**: "Your mother only laid one egg."
- **Attributed to**: GM, joking in the Rift Weaver Prime’s voice
- **Score**: 0.97
- **Nearest transcript line**: "Your mother only laid one egg, it says."
