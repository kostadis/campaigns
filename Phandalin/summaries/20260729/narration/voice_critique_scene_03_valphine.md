# Voice Critique — Valphine, scene 03: Arrival at the Moonstone Mask

**Narration:** `summaries/20260729/narration/session_doc_scene_03_arrival_at_the_moonstone_mask.md` (raw — no `.scrubbed.md` exists)
**Voice spec:** `voice/valphine_new_pipeline.md`
**Genre spec:** `voice/_genre.md`
**Per-char examples:** `examples/valphine.md`

Mechanical scan A (em-dashes): **6 narration-level** (L9, L13, L31, L37, L93, L125) of 12 total.
Mechanical scan B (register vocabulary): clean.

## Flags

### [1] Genre spec conflict — the whole scene is in present tense

> We leave the Protector's Enclave, all polished stone and the quiet signs of the rich and powerful, and within a hundred steps the docks turn grungy — tar, fish, rope, the honest smells of a neighborhood that works for its coin.

**Why:** `_genre.md` is unambiguous: "**First-person past tense, always** ("I", "we")." Scenes 01, 02, 04, 06 and 07 comply; both Valphine scenes (03 and 05) are entirely present tense, so the tense flips twice mid-session in the assembled doc. This is a whole-file conversion, not a sentence edit.
**Suggested rewrite:** We left the Protector's Enclave, all polished stone and the quiet signs of the rich and powerful, and within a hundred steps the docks turned grungy: tar, fish, rope, the honest smells of a neighborhood that works for its coin. *(...and the same conversion throughout.)*

### [2] Voice spec conflict — a GM disfluency leaked into the narrator's own prose

> I simply see it, the way one sees a blade before it is drawn: everybody here is very — all the waitstaff is very pretty.

**Why:** "everybody here is very — all the waitstaff is very pretty" is the GM's false start, verbatim from the source quote at `03_arrival_at_the_moonstone_mask.md:66`, but it has been absorbed into Valphine's interior monologue rather than left in a quote. The result is Valphine stuttering, which contradicts "She narrates with cool precision" and failure-rule 2 ("Long sentences must land in a clear verdict, not drift").
**Suggested rewrite:** I simply see it, the way one sees a blade before it is drawn: all the waitstaff is very pretty. All of them.

### [3] Em-dashes — narration level (mechanical scan A)

> ...and buying something beyond coin — usually secrets.
> Everybody has a very different version of the facts — which means the facts have been scattered deliberately, seed thrown to too many birds.
> They all think it here — that I am the avatar of some good god.

**Why:** Six narration-level dashes in one scene reads as a house tic rather than a voice; her register is aristocratic and the colon or semicolon carries the same weight with more control.
**Suggested rewrite:** ...and buying something beyond coin: usually secrets. / ...a very different version of the facts, which means the facts have been scattered deliberately, seed thrown to too many birds. / They all think it here, that I am the avatar of some good god.

### [4] Awkward construction — clarity

> And she rewards his fashion courage with a very large pouring of something that tastes amazing, by the way his eyes close over the rim.

**Why:** "by the way his eyes close" is meant as *judging by*, but reads first as the parenthetical "by the way." Failure-rule 2 — her sentences must land clean.
**Suggested rewrite:** And she rewards his fashion courage with a very large pouring of something that, judging by how his eyes close over the rim, tastes amazing.

### [5] Cliché simile

> "Want his sister alive," Soma says, dry as old shell.

**Why:** "dry as old shell" is the obvious tortle simile, and the spec's register for her observations of others is motive-reading, not texture-matching ("She reads people as systems of motive, fear, vanity, self-deception, appetite, and utility"). She would note what the dryness is *for*.
**Suggested rewrite:** "Want his sister alive," Soma says, and means it as a correction, not a joke.

### [6] Lexicon drift — an invented demonym

> The Overbrighters call this an enchanting city feature.

**Why:** The spec fixes her term for the surface as "the Overbright" and lists it among the signatures to use verbatim; "Overbrighters" is a coinage extending it. Defensible, but it is the narrator inventing lexicon rather than using hers, and she has a perfectly good existing frame for surface-dwellers.
**Suggested rewrite:** The Overbright calls this an enchanting city feature.

## Out-of-scope observation — a verbatim quote was mutated upstream

> "But Dagult Neverember has declared that the death of Elara was a tragic accident..."

The source reads **"But Lord Neverember has declared..."** (`scene_extractions_smoothed/03_arrival_at_the_moonstone_mask.md:121`). See `voice_critique_summary.md` — this is `sd_narrate.py` running the alias map over quote text, not a narration choice, and it is not fixable in this file.

## Verdict

The present-tense narration is the finding that matters: it violates the genre spec's one non-negotiable and it flips twice across the assembled session. Everything else — the leaked GM stutter, six dashes, two similes — is spot-editable, and the scene's actual analysis ("Matched jewelry is issued equipment", "A body destroyed beyond raising is not misfortune; it is craftsmanship. Someone paid extra") is the strongest Valphine writing in the session.
