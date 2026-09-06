# Quote Verification Report

**Generated**: 2026-09-05T16:40:12
**Transcript**: `/home/kroussos/src/campaign-cycle-worktrees/Phandalin/Phandalin/cycle-pilot/.session-workflow/work/2e66921867eb46fd980e1be73bf0ab57/outputs/transcript.derived-draft.vtt`
**Threshold**: 0.85 (near/unverified boundary)
**Minimum tokens to score**: 4

| verdict | count | share |
|---|---|---|
| verified | 983 | 99% |
| near | 10 | 1% |
| unverified | 0 | 0% |
| unscored | 3 | 0% |
| exempt | 0 | 0% |

**Refused by the extraction contract (#250)**: 0.

## Not checked

- Inline `"…"` spans in prose — not reliably dialogue (a plaque honouring the "liberators of the Ordning" is a label, not speech). Only `> "…"` blockquotes are verified.
- Speaker attribution. This report answers *were these words said*, not *did this person say them*.
- `## Scene summary` sections — human-authored gm-assist content, not model output.

## Refused — the contract will not choose for you

Extraction contract #250 (`docs/design/ExtractionContract_proposal.md`), rules R1 and R3. A refusal is **not** a claim that the text is wrong. It is a claim that this pipeline is not the thing that should decide, so the span stays as it is until you rule on it. Nothing here was auto-corrected and nothing here will be — and nothing here is blocked either: `sd_narrate` still renders these. Refusal means flagged.

R1 scanned **34** span(s) carried by both sections: **23** consistent (identical, or verbatim in both — never a conflict), **11** settled by the transcript, **0** refused.

None. No span was refused by R1 or R3.

## Unverified — review these

None. No quote was untraceable to the transcript.

## Near — an edit happened here (traceable, not verbatim)

Most of these are disfluency edits: the extraction tidied a filler word out of a real line. Listed after the unverified section on purpose — they are the majority and should not bury the findings that matter.

**But `near` means *an edit*, not *a safe edit*.** Similarity cannot tell the two apart: a measured DeepSeek run scored `"My kind has been spreading violence"` (transcript: `"Mankind …"`) at **0.92** and the harmless `"No, I have"` for `"No, I, I have,"` at **0.94** — the meaning-changing edit ranked *below* the harmless one, and no threshold separates them, because both are edits of the same tiny size. Skim this list for changed *words*, not low scores.

### `06_planning_the_stakeout.md:221`

- **Quote**: "Zeleen, you're aware he is a wererat, so that's just an angle you might want to keep in mind."
- **Score**: 0.92
- **Nearest transcript line** (Kostadis Roussos): "Zeleen, you're aware we're at, so that's just an angle you might want to keep in mind."

### `01_a_banker_s_revelation.md:185`

- **Quote**: "Yes, the payments stop seven tendays ago, on the day, not the tenday, no severance, no final reconciliation, no forwarding instruction. That is not how a contract ends."
- **Score**: 0.95
- **Nearest transcript line** (Kostadis Roussos): "Yes, the payments stop 7-10 days ago, on the day, not the 10-day, no severance, no final reconciliation, no forwarding instruction. That is not how a contract ends."

### `06_planning_the_stakeout.md:44`

- **Quote**: "Yes, and so, like, what you kind of pieced together is that 7 ten-days ago, the displacement manifold went dark."
- **Score**: 0.96
- **Nearest transcript line** (Kostadis Roussos): "Yes, and so, like, what you kind of pieced together is that 7 weeks ago, the displacement manifold went dark."

### `05_lim_s_secret_supplier.md:305`

- **Quote**: "This is not the Lim I once knew. Roll for initiative."
- **Score**: 0.96
- **Nearest transcript line** (Wade Brown): "This is not the lab I once knew. Roll for initiative."

### `08_return_to_the_common_chord.md:783`

- **Quote**: "Humming away, like, it's… they've picked it up."
- **Score**: 0.97
- **Nearest transcript line** (Kostadis Roussos): "Thumbing away, like, it's… they've picked it up."

### `05_lim_s_secret_supplier.md:149`

- **Quote**: "You know, multiple times that there is a 9th crate that stays in the street and then disappears in the morning."
- **Score**: 0.98
- **Nearest transcript line** (Stéphane Bourdeaud): "You know, multiple times that there is a 9th grade that stays in the street and then disappears in the morning."

### `01_a_banker_s_revelation.md:176`

- **Quote**: "Well… he pulls out a piece of paper, shows you the correct spelling, B-I-M-B-L-E."
- **Score**: 0.99
- **Nearest transcript line** (Kostadis Roussos): "Well… he pulls out a piece of paper, shows you the correct spelling, B-I-N-B-L-E."

### `04_dining_with_lim_and_interrogating_bellows.md:60`

- **Quote**: "Leilon, yeah, we haven't gone there yet. We've been, you've probably seen a bunch of the, the…"
- **Score**: 0.99
- **Nearest transcript line** (Wade Brown): "Leilan, yeah, we haven't gone there yet. We've been, you've probably seen a bunch of the, the…"

### `08_return_to_the_common_chord.md:288`

- **Quote**: "Well, I mean, your old fee, does that sound fair?"
- **Score**: 0.99
- **Nearest transcript line** (Kostadis Roussos): "Well, I mean, your old feet, does that sound fair?"

### `05_lim_s_secret_supplier.md:77`

- **Quote**: "The sword of dragon slaying in one arm is, his halberd in the other, and the bathrobe. I presume you're still wearing the…"
- **Score**: 0.99
- **Nearest transcript line** (Kostadis Roussos): "The sword of dragons laying in one arm is, his halberd in the other, and the bathrobe. I presume you're still wearing the…"

## Unscored — too short to judge

Under 4 tokens. A quote this short matches something in any transcript, so neither a high nor a low score means anything. Not an accusation.

- `03_arrival_at_the_board_laid_bare.md:248` — "Aasimar."
- `05_lim_s_secret_supplier.md:125` — "the 9th crate."
- `08_return_to_the_common_chord.md:825` — "What? Cymbals."
