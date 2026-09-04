# Quote Verification Report

**Generated**: 2026-09-04T07:00:32
**Transcript**: `/home/kroussos/Phandalin/Phandalin/summaries/20250812-chapter-08/session_20250812.partialmap.vtt`
**Threshold**: 0.85 (near/unverified boundary)
**Minimum tokens to score**: 4

| verdict | count | share |
|---|---|---|
| verified | 924 | 100% |
| near | 0 | 0% |
| unverified | 0 | 0% |
| unscored | 1 | 0% |
| exempt | 0 | 0% |

**Refused by the extraction contract (#250)**: 0.

## Not checked

- Inline `"…"` spans in prose — not reliably dialogue (a plaque honouring the "liberators of the Ordning" is a label, not speech). Only `> "…"` blockquotes are verified.
- Speaker attribution. This report answers *were these words said*, not *did this person say them*.
- `## Scene summary` sections — human-authored gm-assist content, not model output.

## Refused — the contract will not choose for you

Extraction contract #250 (`docs/design/ExtractionContract_proposal.md`), rules R1 and R3. A refusal is **not** a claim that the text is wrong. It is a claim that this pipeline is not the thing that should decide, so the span stays as it is until you rule on it. Nothing here was auto-corrected and nothing here will be — and nothing here is blocked either: `sd_narrate` still renders these. Refusal means flagged.

R1 scanned **28** span(s) carried by both sections: **23** consistent (identical, or verbatim in both — never a conflict), **5** settled by the transcript, **0** refused.

None. No span was refused by R1 or R3.

## Unverified — review these

None. No quote was untraceable to the transcript.

## Unscored — too short to judge

Under 4 tokens. A quote this short matches something in any transcript, so neither a high nor a low score means anything. Not an accusation.

- `01_silence_at_the_tower_of_storms.md:221` — "Critical damage even."
