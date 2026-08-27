# Voice Critique — Vukradin, scene 04: Lord Cassian and the Performance

**Narration:** `summaries/20260729/narration/session_doc_scene_04_lord_cassian_and_the_performance.md` (raw — no `.scrubbed.md` exists)
**Voice spec:** `voice/vukradin_new_pipeline.md`
**Genre spec:** `voice/_genre.md`
**Per-char examples:** `examples/vukradin.md`

Mechanical scan A (em-dashes): **7 narration-level** (L29, L35, L61, L69, L75 ×2, L85) of 14 total.
Mechanical scan B (register vocabulary): clean.

## Flags

### [1] Banned construction — taxonomizing instead of rendering

> there he sat: a sea elf, silver-skinned, wearing the kind of quiet wealth that doesn't need to announce itself.

**Why:** "the kind of X that doesn't need to Y" is the same move `_genre.md` bans under "with the [Adj] [Noun] of someone who..." — it names a category of person instead of the specific thing the POV character saw. The genre spec's own instruction is "Name specific objects... rather than gesture at categories," and Vukradin's lens is *specific corruption*, so he would price the coat.
**Suggested rewrite:** there he sat: a sea elf, silver-skinned, in a plain grey coat that cost more than the room we slept in.

### [2] Cliché / stock simile

> Brewbarry finished his drink, stood, applauded loud as a rockslide, and swept the room for anyone who wasn't clapping.

**Why:** "loud as a rockslide" is the default simile for a large person and it is the narrator's image, not Vukradin's. The spec has him celebrate allies openly and by name with cheerleader-conductor energy; he would register the *effect on the room*, which is the funnier and more in-voice observation.
**Suggested rewrite:** Brewbarry finished his drink, stood, and put his hands together hard enough that three people at the next table jumped. Then he swept the room for anyone who wasn't clapping.

### [3] Voice spec conflict — the procedural mechanical register is entirely absent

> And I did, and the words landed exactly right — I felt it leave my mouth and watched purses open across the room.

**Why:** The source has Vukradin call his own roll — "20 persuasion. How much money did we raise?" (`scene_extractions_smoothed/04_...md:193`) — and the narration converts it to pure feeling. Failure-rule 9 requires "the procedural mechanical register, the cheerleading, and the ledger reflex must all be present," and `_genre.md` says "Drop hit points, distances, spell names directly into prose. Mechanics are not separate from feeling." No dice result survives anywhere in this scene, or in fact in any scene this session.
**Suggested rewrite:** Twenty on the persuasion. I felt it leave my mouth and watched purses open across the room.
**Note:** this is in tension with the `/scrub` pass, which strips raw mechanical numbers from narration. `_genre.md` and `/scrub` disagree here and only the GM can settle it — flagging rather than assuming.

### [4] Em-dashes — narration level (mechanical scan A)

> She had waited for us at a party we never attended — because we were off saving the world from a dragon.
> And there was applause — real, sustained applause.
> ...murmured earnestly about my missed chords — the intentionality of them, the daring.

**Why:** Seven in one scene. His two registers are clause-stacking build and single-word verdict landing; the dash is a third rhythm belonging to neither.
**Suggested rewrite:** ...a party we never attended, because we were off saving the world from a dragon. / And there was applause. Real, sustained applause. / ...about my missed chords: the intentionality of them, the daring.

### [5] The scene ends on a bare quote with no narrator landing

> "It's like the lottery, right? All the money from the lottery goes to the schools. We don't need to fund the schools."

**Why:** Every other scene this session closes on its narrator. Failure-rule 8 — "Do not let long building sentences drift without landing in a clear verdict" — and the studio fund is a load-bearing ambition per the spec, so the scene's actual outcome (money raised, for the studio, honestly) never gets his verdict on it.
**Suggested rewrite:** Add a closing beat, e.g.: *Fair-trade, conflict-free gold, given freely by people who wanted to give it. Restricted. Done.*

## Out-of-scope observation — a verbatim quote was mutated upstream

> "Oh, you're a Vukradin. Sing a song! Sing us a song, come on!"

Brewbarry said **"Oh, you're a bard."** (`scene_extractions_smoothed/04_...md:96`). `docs/aliases.json` maps `Bard → Vukradin`, and `sd_narrate.py` applies that map to quote text. See `voice_critique_summary.md`; not fixable in this file.

## Verdict

The dice are gone — Vukradin's procedural register is one of three things the spec calls non-negotiable and it does not appear once, which is what makes the scene read as generic earnest-bard prose in places. The line "Honest work delivered late is still honest work. It just arrives to fewer living people." is the voice landing exactly right; the rest of the scene wants one or two more of those. Spot-edit.
