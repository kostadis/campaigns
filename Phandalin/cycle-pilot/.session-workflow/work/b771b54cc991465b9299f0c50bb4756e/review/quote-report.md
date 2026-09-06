# Quote Verification Report

**Generated**: 2026-09-05T14:42:11
**Transcript**: `/home/kroussos/src/campaign-cycle-worktrees/Phandalin/Phandalin/cycle-pilot/.session-workflow/work/2e66921867eb46fd980e1be73bf0ab57/outputs/transcript.derived-draft.vtt`
**Threshold**: 0.85 (near/unverified boundary)
**Minimum tokens to score**: 4

| verdict | count | share |
|---|---|---|
| verified | 18 | 72% |
| near | 2 | 8% |
| **unverified** | 5 | 20% |
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

### `session-summary.md:384` (§ Memorable Moments)

- **Quote**: "That is not how a contract ends.… That is how a contract is abandoned!"
- **Likely stitched**: contains `...` — two separate utterances joined into one quote. Usually fixed by splitting it, not by rewording.
- **Attributed to**: Aurelan Vance
- **Score**: 0.53
- **Nearest transcript line** (Kostadis Roussos): "He struggles to about, say, Mr. Brewbarry, but then realize that, you know, we're on friendly terms. Brew, that is how a contract is abandoned!"

### `session-summary.md:412` (§ Memorable Moments)

- **Quote**: "I don't like your music."
- **Attributed to**: Lim
- **Score**: 0.59
- **Nearest transcript line** (Wade Brown): "I don't know why."

### `session-summary.md:394` (§ Memorable Moments)

- **Quote**: "Why don't we talk to strangers? Stop talking to strangers, please."
- **Attributed to**: Vukradin
- **Score**: 0.68
- **Nearest transcript line** (David Mendenhall): "Stop talking to strangers, please."

### `session-summary.md:452` (§ Memorable Moments)

- **Quote**: "The Lim I knew wouldn't… get in so deep with criminals."
- **Likely stitched**: contains `...` — two separate utterances joined into one quote. Usually fixed by splitting it, not by rewording.
- **Attributed to**: Soma
- **Score**: 0.76
- **Nearest transcript line** (Wade Brown): "the, the Lim I knew wouldn't, wouldn't get in, you know, get in so deep with criminals."

### `session-summary.md:447` (§ Memorable Moments)

- **Quote**: "You've changed. You're different. I remember a different Soma."
- **Attributed to**: Lim
- **Score**: 0.79
- **Nearest transcript line** (Kostadis Roussos): "She goes, you've changed, and you're different. You're different. I remember a different soma."

## Near — an edit happened here (traceable, not verbatim)

Most of these are disfluency edits: the extraction tidied a filler word out of a real line. Listed after the unverified section on purpose — they are the majority and should not bury the findings that matter.

**But `near` means *an edit*, not *a safe edit*.** Similarity cannot tell the two apart: a measured DeepSeek run scored `"My kind has been spreading violence"` (transcript: `"Mankind …"`) at **0.92** and the harmless `"No, I have"` for `"No, I, I have,"` at **0.94** — the meaning-changing edit ranked *below* the harmless one, and no threshold separates them, because both are edits of the same tiny size. Skim this list for changed *words*, not low scores.

### `session-summary.md:379` (§ Memorable Moments)

- **Quote**: "And since we're on such friendly terms, my friends call me Ori."
- **Attributed to**: Aurelan Vance
- **Score**: 0.95
- **Nearest transcript line** (Kostadis Roussos): "And since we're on the… since we're on such friendly terms, my friends call me Ori."

### `session-summary.md:432` (§ Memorable Moments)

- **Quote**: "It does not come inside. It is set down, and it is not there in the morning. I have not asked. It is not billed to us."
- **Attributed to**: Bellows
- **Score**: 0.99
- **Nearest transcript line** (Kostadis Roussos): "It does not come inside. It is set down, and it is not therein in the morning. I have not asked. It is not billed to us."
