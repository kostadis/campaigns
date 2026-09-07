# Quote Verification Report

**Generated**: 2026-09-06T02:24:31
**Transcript**: `/home/kostadis/phandalin/Phandalin/summaries/20260902/GMT20260902-040118_Recording.transcript.cleaned.vtt`
**Threshold**: 0.85 (near/unverified boundary)
**Minimum tokens to score**: 4

| verdict | count | share |
|---|---|---|
| verified | 9 | 39% |
| near | 9 | 39% |
| **unverified** | 3 | 13% |
| unscored | 2 | 9% |
| exempt | 0 | 0% |

**Refused by the extraction contract (#250)**: 0.

## Not checked

- Inline `"…"` spans in prose — not reliably dialogue (a plaque honouring the "liberators of the Ordning" is a label, not speech). Only `> "…"` blockquotes are verified.
- Speaker attribution. This report answers *were these words said*, not *did this person say them*.

## Refused — the contract will not choose for you

Extraction contract #250 (`docs/design/ExtractionContract_proposal.md`), rules R1 and R3. A refusal is **not** a claim that the text is wrong. It is a claim that this pipeline is not the thing that should decide, so the span stays as it is until you rule on it. Nothing here was auto-corrected and nothing here will be — and nothing here is blocked either: `sd_narrate` still renders these. Refusal means flagged.

None. No span was refused by R1 or R3.

## Unverified — review these

### `session-summary.md:80` (§ Memorable Moments)

- **Quote**: "I don’t know. Where am I?"
- **Attributed to**: Vukradin
- **Score**: 0.63
- **Nearest transcript line** (David Mendenhall): "I don't know."

### `session-summary.md:85` (§ Memorable Moments)

- **Quote**: "Because I’m not over there."
- **Attributed to**: Vukradin
- **Score**: 0.74
- **Nearest transcript line** (David Mendenhall): "And then I say, Because I'm not over there."

### `session-summary.md:111` (§ Memorable Moments)

- **Quote**: "I thought turtles carried their house on their shoulders, so they didn’t need a place to stay."
- **Attributed to**: Uncle Tom
- **Score**: 0.84
- **Nearest transcript line** (Kostadis Roussos): "No, she's not racist. She's like, I thought turtles carried their house on their shoulders, so they didn't need a place to stay."

## Near — an edit happened here (traceable, not verbatim)

Most of these are disfluency edits: the extraction tidied a filler word out of a real line. Listed after the unverified section on purpose — they are the majority and should not bury the findings that matter.

**But `near` means *an edit*, not *a safe edit*.** Similarity cannot tell the two apart: a measured DeepSeek run scored `"My kind has been spreading violence"` (transcript: `"Mankind …"`) at **0.92** and the harmless `"No, I have"` for `"No, I, I have,"` at **0.94** — the meaning-changing edit ranked *below* the harmless one, and no threshold separates them, because both are edits of the same tiny size. Skim this list for changed *words*, not low scores.

### `session-summary.md:116` (§ Memorable Moments)

- **Quote**: "I can’t live in this thing. It merely protects me."
- **Attributed to**: Soma
- **Score**: 0.88
- **Nearest transcript line** (Wade Brown): "I see what you think of us. I can't live in this thing. It merely protects me."

### `session-summary.md:127` (§ Memorable Moments)

- **Quote**: "It’s not about progressive, it’s like, money’s money, man, I don’t care who’s got it."
- **Attributed to**: Uncle Tom
- **Score**: 0.89
- **Nearest transcript line** (Kostadis Roussos): "He goes, it's not about progressive, it's like, money's money, man, I don't care who's got it."

### `session-summary.md:121` (§ Memorable Moments)

- **Quote**: "We’re an equal opportunity housing establishment."
- **Attributed to**: Uncle Tom
- **Score**: 0.94
- **Nearest transcript line** (Kostadis Roussos): "he goes, well, look, you know, I mean, first of all, you know, we'll take… we don't care. We're an equal opportunity housing establishment."

### `session-summary.md:93` (§ Memorable Moments)

- **Quote**: "Exactly. And Lim’s a fan."
- **Attributed to**: Vukradin
- **Score**: 0.96
- **Nearest transcript line** (David Mendenhall): "Exactly. And Lim's a fan."

### `session-summary.md:98` (§ Memorable Moments)

- **Quote**: "You know what, we’re gonna do one better, we’re gonna take you there."
- **Attributed to**: Rsolk
- **Score**: 0.97
- **Nearest transcript line** (Kostadis Roussos): "You know what, we're gonna do one better, we're gonna take you there."

### `session-summary.md:59` (§ Memorable Moments)

- **Quote**: "This is too commer— this is too commercial."
- **Attributed to**: Old Hesp
- **Score**: 0.98
- **Nearest transcript line** (Kostadis Roussos): "This is too commer… this is too commercial."

### `session-summary.md:68` (§ Memorable Moments)

- **Quote**: "Only a 1 in 400 chance of disaster. It’ll be fine."
- **Attributed to**: Vukradin
- **Score**: 0.98
- **Nearest transcript line** (David Mendenhall): "Only a 1 in 400 chance of disaster. It'll be fine."

### `session-summary.md:101` (§ Memorable Moments)

- **Quote**: "We don’t want you to get lost again, Mr. Vukradin."
- **Attributed to**: Rsolk
- **Score**: 0.98
- **Nearest transcript line** (Kostadis Roussos): "We don't want you to get lost again, Mr. Vukradin."

### `session-summary.md:47` (§ Memorable Moments)

- **Quote**: "There are different tiers of giving levels, actually. 10 gold pieces puts you at the—"
- **Score**: 0.99
- **Nearest transcript line** (David Mendenhall): "There are different tiers of giving levels, actually. 10 gold pieces puts you at the,"

## Unscored — too short to judge

Under 4 tokens. A quote this short matches something in any transcript, so neither a high nor a low score means anything. Not an accusation.

- `session-summary.md:124` — "It’s so progressive."
- `session-summary.md:132` — "You’re a drow."
