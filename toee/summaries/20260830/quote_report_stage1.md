# Quote Verification Report

**Generated**: 2026-09-05T15:46:20
**Transcript**: `/home/kostadis/toee/toee/summaries/20260830/GMT20260830-150238_Recording.transcript.cleaned.vtt`
**Threshold**: 0.85 (near/unverified boundary)
**Minimum tokens to score**: 4

| verdict | count | share |
|---|---|---|
| verified | 5 | 42% |
| near | 4 | 33% |
| **unverified** | 3 | 25% |
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

### `session-summary.md:75` (§ Memorable Moments)

- **Quote**: "We control the food, not you. You’re simply guarding it."
- **Attributed to**: Zephyr
- **Score**: 0.68
- **Nearest transcript line** (Thomas Kolivakis): "We control the food, not you."

### `session-summary.md:119` (§ Memorable Moments)

- **Quote**: "I’ve been doing the supply check. The Minotaur has food for 3 days. The men have pay for 4. The dead have started leaving without permission. I cannot solve… I… I can’t solve any one of these. I cannot solve all three while pretending this is a normal command."
- **Likely stitched**: contains `...` — two separate utterances joined into one quote. Usually fixed by splitting it, not by rewording.
- **Attributed to**: Dren Halveth
- **Score**: 0.70
- **Nearest transcript line** (Kostadis Roussos): "I've been doing the supply check. The Minotaur has food for 3 days. The men have pay for 4. The dead have started leaving without permission."

### `session-summary.md:114` (§ Memorable Moments)

- **Quote**: "Wake what sleeps in the iron coffin. Ask your golden friend what he’s so afraid you’ll find, then signal me."
- **Attributed to**: Falrinth
- **Score**: 0.77
- **Nearest transcript line** (Kostadis Roussos): "Ask your golden friend what he's so afraid you'll find, then signal me."

## Near — an edit happened here (traceable, not verbatim)

Most of these are disfluency edits: the extraction tidied a filler word out of a real line. Listed after the unverified section on purpose — they are the majority and should not bury the findings that matter.

**But `near` means *an edit*, not *a safe edit*.** Similarity cannot tell the two apart: a measured DeepSeek run scored `"My kind has been spreading violence"` (transcript: `"Mankind …"`) at **0.92** and the harmless `"No, I have"` for `"No, I, I have,"` at **0.94** — the meaning-changing edit ranked *below* the harmless one, and no threshold separates them, because both are edits of the same tiny size. Skim this list for changed *words*, not low scores.

### `session-summary.md:104` (§ Memorable Moments)

- **Quote**: "The orb this temple frets over, yes! I have it. I’m not giving it to Hedrack, nor to Senshock, nor to any of the holy gentlemen who would like me dead. I’m not giving it to you either, but that is a separate conversation."
- **Attributed to**: Falrinth
- **Score**: 0.90
- **Nearest transcript line** (Kostadis Roussos): "I have it. I'm not giving it to Hedrack, nor to Senshock, nor to any of the holy gentlemen who would like me dead. I'm not giving it to you either, but that is a separate conversation."

### `session-summary.md:124` (§ Memorable Moments)

- **Quote**: "We don’t have to say that we’re powerful, we just know."
- **Attributed to**: Zephyr
- **Score**: 0.96
- **Nearest transcript line** (Thomas Kolivakis): "We don't have to say that we're powerful, we just know."

### `session-summary.md:65` (§ Memorable Moments)

- **Quote**: "I’m in charge of getting shit done."
- **Attributed to**: Sequoia
- **Score**: 0.97
- **Nearest transcript line** (Nicholas Roussos): "I'm in charge of getting shit done."

### `session-summary.md:95` (§ Memorable Moments)

- **Quote**: "Just don’t blame me when your logistics breaks down."
- **Attributed to**: Sequoia
- **Score**: 0.98
- **Nearest transcript line** (Nicholas Roussos): "Just don't blame me when your logistics breaks down."
