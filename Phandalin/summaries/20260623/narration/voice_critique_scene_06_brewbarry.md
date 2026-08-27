# Voice Critique — Brewbarry, scene 06: The Exotic Armorer of Neverwinter

**Narration:** `summaries/20260623/narration/session_doc_scene_06_the_exotic_armorer_of_neverwinter.scrubbed.md`
**Voice spec:** `voice/brewbarry_new_pipeline.md` (authoritative)
**Supplementary spec:** `voice/v1/brewbarry_voice.md`
**Per-char examples:** `examples/brewbarry.md` (40 lines, two passages only)
**Genre:** `voice/_genre.md`

## Flags

### [1] Banned tic + generic reach — line 119

> The proprietor was not a bad man. He was a happy man, praising his god's work. But the shape of his joy was a thing I'd been cut by before, and I felt the old wound ache in my chest.

**Why:** Two problems in one sentence. `the shape of his joy` is banned outright by `voice/_genre.md` line 43. `I felt the old wound ache in my chest` is stock emotional shorthand — and it is *tell-not-show* in a character whose entire spec is "He feels something and then he acts. There is very little space between the two."
**Suggested rewrite:** `The proprietor was not a bad man. He was a happy man, praising his god's work. I had heard happy men say things like that about Uthgardt.` The comparison at line 117 is already doing this work; the sentence only needs to point at it.

### [2] Voice spec conflict — ideological argument, line 115

> He was praising Valphine for escaping something he didn't understand. He was praising me for accepting her. And all of it was a cage made of words about what drow were and what they couldn't be.

**Why:** Failure-prevention rule 3: "Do not give him complex moral arguments about systems, factions, or ideology. He responds to specific people and specific moments." `a cage made of words about what drow were and what they couldn't be` is a thesis about the mechanics of prejudice. His examples make the same point by refusing to argue it — "I am so sorry that the Uthgardts hurt you. They were mean to me, too." One person, one moment, no framework.
**Suggested rewrite:** Cut the third sentence. `He was praising Valphine for escaping something he didn't understand. He was praising me for accepting her. He did not know he was doing it.`

### [3] Voice spec conflict — narrating shame at length, line 133

> The thought didn't sit heavy. It felt fine. Respect is respect. A god's light is a god's light. I'd been carrying guilt for my people's sins for years. If this little man needed me to be proof that his god's warmth could reach anyone — even a drow, even a barbarian — I could carry that, too.

**Why:** The first four sentences are exactly right — short, flat, declarative. Then it turns into a paragraph of interior justification. Failure-prevention rule 8: "Do not make him narrate his own shame at length. He references it briefly when it surfaces; he does not return to it." Rule 6: "If a paragraph of inner monologue is needed, it is too long."
**Suggested rewrite:** Stop after the fourth sentence, then go straight to line 135. `The thought didn't sit heavy. It felt fine. Respect is respect. A god's light is a god's light. I just hoped his god would carry it back.`

### [4] Attribution failure — GM narration inside character dialogue, lines 45 and 51

> The proprietor did not hear it. Or pretended not to. "No, he didn't say that." (45)

> "So he says: but Valphine, as much as I would like to do this for free and gratis, unfortunately, it takes time and money." (51)

**Why:** Both are the GM speaking out-of-fiction. Line 51 carries the GM's own speech tag `So he says:` inside the proprietor's quoted line. Line 45 is worse — the GM correcting Vukradin's joke has been *assigned to the proprietor*, and the narration then invents a justification for it (`did not hear it. Or pretended not to.`). Same root cause as scene 02: the voice spec's constraints 1–8 forbid altering anything between quotation marks, so the pass could not fix what the extraction handed it.
**Suggested rewrite:** Line 51 → strip the tag: `"But Valphine, as much as I would like to do this for free and gratis, unfortunately, it takes time and money."` Line 45 needs the quote removed entirely and Vukradin's aside left unanswered.

### [5] Structural — missing POV heading — ~~FLAG WITHDRAWN~~

> **Correction (2026-08-09):** wrong flag. `session_doc/assemble.py` lines 165–167 build the section header from the frontmatter `narrator:` field, which is correct here; the in-body `### <Name>` heading is never read. Adding one would have duplicated the narrator's name in the assembled document. Per GM ruling the three that existed were removed instead. See the correction in `voice_critique_summary.md`.

### [6] Mechanical scan A — 11 narration-level em-dashes

Lines 9, 27, 35, 37, 39, 79, 87, 101, 119, 127, 133. Excludes em-dashes inside `"..."` and `*...*`.

**Why:** Same note as scene 01 — the period is Brewbarry's punctuation. Line 87 (`His gaze swung to me — and I was used to being looked at`) and line 133 (`— even a drow, even a barbarian —`) are the two doing real damage, because both splice a qualifier into a beat that should land flat.
**Suggested rewrite:** Line 87 → `His gaze swung to me. I am used to being looked at.`

## Not flagged (working as intended)

Line 17 (`He looked at Valphine like she was a plate of warm bread`) is the best single line in the session — concrete, bodily, funny without trying. Line 89 (`I tend to be quiet in shops. Too many pretty things to break`) and line 79 (the wrestling-margin comparison, `by fall rather than by points`) are both exactly the register the spec asks for. Line 105's third-person self-reference (`"Brewbarry works for no one"`) is canon speech, not a defect.

## Verdict

The scene's interior passages keep explaining a point its images have already made — lines 115, 119 and 133 each add a paragraph of argument to a beat that landed two sentences earlier. Spot-edit by deletion rather than rewriting; almost every flag here resolves by cutting the explanatory tail.
