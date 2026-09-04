# Chapter 08 — speaker attribution

Produced by `/speaker-attribution` on 2026-09-03. Accepted by GM at a 4.7%
residual disagreement rate; the disagreement queue was reviewed in aggregate,
not turn by turn.

## Mapping (players, not characters)

| cluster | player | PCs voiced | Descript agreement |
|---|---|---|---|
| SPEAKER_00 | Kostadis | GM | 84% |
| SPEAKER_01 | Wade | Soma | 91% |
| SPEAKER_02 | Gary | Valphine **and** Brewbarry | 81% |
| SPEAKER_03 | Dave | Vukradin | 82% |

Stéphane absent; Gary covered Brewbarry. This was established from the audio,
not from `party.md` — `Brewbarry` and `Valphine` vocatives resolve to the same
cluster (47% / 38%). Do not infer PC ownership from a label in other chapters.

Three independent lines of evidence agree: pyannote speech share, Descript's own
clustering, and vocative answer-scoring (`Dave` 100%, `Soma` 67%).
Word-level agreement between the two clusterings: **84.8%**.

## Provenance

`transcript_provenance.py` flagged all four transcripts as "sits beside audio it
does NOT transcribe". **False positive** — the stem-vouching rule found no file
named `GMT20250813-040058_*`. Settled by endpoints instead:

| | ends |
|---|---|
| `GMT20250813-040058_Recording.m4a` | 01:38:02.8 |
| `session_20250812_transcript.vtt` | 01:38:01.1 |
| `descript_transcript.md` | 01:38:02 |

All open on `Hello?` at 00:04:00. Same recording.

## Files

| file | role |
|---|---|
| `session_20250812.speakers.vtt` | **the attributed transcript.** Whisper text on a real timeline, player labels. `[?]` on 395 of 2117 cues marks clustering disagreement, mostly short crosstalk — not errors, do not bulk-fix. Feed this to `/scene-extract`. |
| `diarize_turns.json` | pyannote `community-1`, `num_speakers=4`, cuda |
| `speaker_disagreements.txt` | the accepted 202-turn / 586-word residual |

## Not independent transcripts

`Chapter 08.md` and `Chapter 08.cleaned.md` are `descript_transcript.md` with the
inline per-word timestamps stripped (`.cleaned` additionally spell-passed) —
identical turn counts and identical label tallies (kostadis 466 / dave 466 /
wade 323 / gary 202). They inherit Descript's attribution 1:1 by turn index and
carry the same residual. They have **not** been repaired.

## Residual, for whoever inherits this

586 of 12,584 words (4.7%). The bias is directional: 248 words leak *into* Wade
from the other three, more than any other direction. The largest single
disagreement is 16 words. One known real Descript error, uncorrected:

    [33:27] descript=dave  pyannote=kostadis  95%  "Spider done. Uh, brewery is up"

Calling the next turn in initiative is GM behaviour, so pyannote is right there.
