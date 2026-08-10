# Transcript corrections proposed for ch46 — RESOLVED

Decision record for campaigns#156. All 16 proposals ruled 2026-08-10 — they cover 15
distinct cues, because cue 1211 was proposed twice (an R1 conflict and an R3 bracket
landing on the same cue).

The rule applied: **a correction is approved only when the corrected form is attested** —
canonical in `docs/entity_registry.yaml`, or appearing elsewhere in this same tape in the
same sense. Where the tape is garbled beyond a single attested word, the right answer is to
leave it garbled; `[inaudible]` exists for that, and approving a guess writes fiction into
ground truth.

**3 approved, 12 rejected.**

## Approved — now in `transcript_corrections.yaml`

| cue | tape said | now reads | why |
|---|---|---|---|
| 224 | `the strength of **the pandemic**` | `…of Lathander` | Lathander appears 9x in this tape and is registry-canonical |
| 1211 | `much respect for **the thunder**` | `…for Lathander` | same mishearing; merged from an R1 and an R3 proposal on one cue |
| 245 | `like a Brewbarry **bathroom**` | `…bathrobe` | the bathrobe thread runs all session; 'bathrobe(s)' appears 15x, 'bathroom' only here |

Measured effect on `scene_extractions_new/`: unverified **34 → 32**, R1 refusals **4 → 3**,
and cue 224's pair moved into `consistent` because both copies are now verbatim.

## Rejected — the tape keeps its garble

Not 'we could not be bothered'. In each case the extraction guessed at what was said, and a
guess in the transcript is worse than a garble, because everything downstream treats this
file as what happened.

### cue 299

- **tape**: `We had to kill a dragon, we had to stop an orcan game, I'll see the whole way.`
- **extraction reads**: `We had to kill a dragon, we had to stop an orc campaign, [inaudible — probable "I'll fill you in the whole way"].`
- **rejected**: 'orcan game' -> 'orc campaign': 'campaign' appears 0x in this tape. A guess.

### cue 304

- **tape**: `Who owns it at Mermaid Steph?`
- **extraction reads**: `Who owns it? [inaudible — probable "It's a mermaid, Steph(ane)"]`
- **rejected**: 'Who owns it at Mermaid Steph?' -> 'It's a mermaid, Steph(ane)': a rewrite of the whole line, not a word repair.

### cue 324

- **tape**: `Well, yes, that's our next system.`
- **extraction reads**: `Well, yes, that's our next [stop].`
- **rejected**: 'our next system' -> 'our next stop': 'stop' is a common word, so its presence in the tape is no evidence. Plausible, unproven.

### cue 672

- **tape**: `Place the socks go in the dryer.`
- **extraction reads**: `[Same place the] socks go in the dryer.`
- **rejected**: 'Place the socks' -> 'Same place the socks': adds a word nobody is shown to have said.

### cue 729

- **tape**: `Okay, so, and those, and you inform them who they are, those Elaine, the… yeah, alright, alright. Well, then we will absolutely keep them a fine round of our finest cheese, and she, and then she goes, Mr. Brewbarry.`
- **extraction reads**: `Okay, so, and those, and you inform them who they are, [those are Brin and Giles], the… yeah, alright, alright. Well, then we will absolutely keep them a fine round of our finest cheese, and she, and then she goes, Mr. Brewbarry.`
- **rejected**: 'those Elaine, the...' -> 'those are Brin and Giles': 'Brin' appears 0x in this tape. A reconstruction.

### cue 747

- **tape**: `Don't underestimate the power of Gucci's on, you know, the good people.`
- **extraction reads**: `Don't underestimate the power of [the good stuff on] the good people.`
- **rejected**: 'the power of Gucci's on' -> 'the good stuff on': a full rephrase of a garbled span.

### cue 781

- **tape**: `And, and a, you know, a little but, you know, readable.`
- **extraction reads**: `And a little [blurb], readable.`
- **rejected**: 'a little but' -> 'a little blurb': 'blurb' appears 0x in this tape.

### cue 831

- **tape**: `It literally goes, Shalim Lenny goes, Brewbarry.`
- **extraction reads**: `It literally goes, [so] Linene goes, Brewbarry.`
- **rejected**: 'Shalim Lenny goes' -> '[so] Linene goes': 'Linene' is canonical but 'Shalim' -> 'so' is a guess; the span is garbled beyond a single-word repair.

### cue 857

- **tape**: `That we're phasing in an.`
- **extraction reads**: `That were phasing in and [out].`
- **rejected**: 'phasing in an' -> 'in and out': a reconstruction of a truncated line.

### cue 1019

- **tape**: `Like, do you want to ask about it, or, like, Vugrid, you're, like, cut, or just keep moving on.`
- **extraction reads**: `Valphine, you immediately recognized the music. It was Vukradin's old music. Like, do you want to ask about it, or, like, Vukradin, you're, like, [continue?], or just keep moving on.`
- **rejected**: 'you're, like, cut, or' -> '[continue?]': 'continue' appears 0x. A conjecture the extraction should not have made either.

### cue 1106

- **tape**: `In honor of the liberators of the Orning, through whose courage and through the combined strength of the Lord's Alliance, the giant kingdoms were restored to order to north, and the secured.`
- **extraction reads**: `As you walk through the Protector's Enclave, mounted on a building, at eye level, is a carved stone plaque. In honor of the liberators of the Ordning, through whose courage and through the combined strength of the Lord's Alliance, the giant kingdoms were restored to order in the north, and [kept] secured. And then it says, beside it is a Lord's Alliance Herald in blue and gold livery distributing a broadsheet.`
- **rejected**: 'and the secured' -> 'and [kept] secured': 'kept' appears 0x in this tape.

### cue 1173

- **tape**: `Are you… are you the drow that Brother Aldrich speaks of? The one who converted to the blessed teachings of the Morning Lord?`
- **extraction reads**: `Are you… are you the drow that Brother Aldric speaks of? The one who converted to the blessed teachings of the Morning Lord?`
- **rejected**: 'Brother Aldrich' vs 'Aldric': an IDENTITY question, not a spelling one. Registry canon is 'Aldric Stone Path' but the tape says 'Brother Aldrich Sunmantle' - a different surname. Belongs in the entity registry.

## Still open

R3 refusals stay at 12. Approving a tape fix corrects the *content* of a bracketed span
but does not remove the bracket — the extraction file still carries an editorial
insertion inside a span marked verbatim. Clearing those means re-extracting ch46, which
#250 keeps out of scope: this corpus is evidence, not a migration target.
