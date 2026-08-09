# Voice Critique — Valphine, scene 02: A Hero's Welcome at Stonehill Inn

**Narration:** `summaries/20260623/narration/session_doc_scene_02_a_hero_s_welcome_at_stonehill_inn.scrubbed.md`
**Voice spec:** `voice/valphine_new_pipeline.md` (authoritative)
**Supplementary spec:** `voice/v1/valphine_voice.md`, `voice/v1/valphine_voice_addendum.md`
**Per-char examples:** `examples/valphine.md` (171 lines, four passages)
**Genre:** `voice/_genre.md`

This is the most damaged scene of the six. Seven separate passages of GM table-narration were passed through as in-fiction character dialogue.

## Flags

### [1] Attribution failure — GM table-narration locked into character dialogue (7 occurrences)

The dominant defect. Lines 15, 21, 43, 59, 79, 87, 111, 131 put the GM's out-of-fiction stage directions inside quotation marks as though a character said them:

> "Then he looks at Valphine and notices that she has the golden eyes. And is, for a moment, startled. Is that a condition?"

> "Holy crap. Yeah, he says… Ser Kaelen is upset. That you forgot about it."

> "And you immediately remember that that's exactly where you had gone to train to be a cleric of Lathander? And there's an opportunity for you to go chat with Brother Aldric Sunmantle."

> "Alright, well that is an amazing achievement—and as a result of that amazing achievement, Toblen hands out the good stuff. Elsa, the barmaid, is pouring out the good beer, she's handing it out…"

**Why:** This is not a voice failure by the model — it is structural. `voice/valphine_new_pipeline.md` constraints 1–8 forbid altering *any* substring between quotation marks ("Treat every substring between quotation marks as immutable text"). The upstream extraction quoted the GM's narration, so the voice pass was *prohibited* from converting it. The immutable-quote rule, which exists to protect player dialogue, propagates GM stage directions into the fiction verbatim.
**Suggested rewrite:** These must be un-quoted and rendered as narration in Valphine's POV. Line 87 → `Then his eyes found mine, and caught. A drow with golden eyes. He recovered fast, but not fast enough. "Is that a condition?"` — keeping only the genuinely spoken clause inside quotes. This is a pipeline fix, not a per-line fix: see the summary report.

### [2] Attribution failure — Valphine narrating herself in third person, line 135

> "Practically speaking," I heard myself say, the words coming from a place beneath the conversation, "the way I see it is Valphine thought that Brother Aldric was a fool who couldn't understand the real power of Lathander."

**Why:** The worst instance of flag [1]. This is the GM's out-of-character framing assigned to Valphine as speech, so she refers to herself by name in the third person while narrating in the first. The hedge `I heard myself say, the words coming from a place beneath the conversation` is the model straining to justify an impossible attribution.
**Suggested rewrite:** Convert wholly to interior narration: `Brother Aldric was a fool who never understood the real power of Lathander. I had spent months pretending to be someone I was not, to learn his rituals, with no intention of absorbing his soft, squishy, take-care-of-people ways.`

### [3] Banned tic — "with the [X] of a man who…" (3 occurrences)

> The knight's voice carried that particular officiousness of a man who organized things for a living. (43)

> It was the look of a man who had found a loose thread and could not stop pulling. (47)

> Vukradin, to his credit, responded with the grace of a man who understood he had dropped a thread. (63)

**Why:** `voice/_genre.md` line 44 bans this construction by name: "Claude tic for taxonomizing a person's behavior instead of rendering what the POV character actually saw… one Claude narrator wearing five hats." Three in one scene, and two of them reach for the same "thread" image within twenty lines.
**Suggested rewrite:** Line 47 → `Then Ser Kaelen's eyes narrowed. He had found a loose thread. He would not stop pulling.` Valphine's examples render people as systems of motive in plain declaratives, not as taxonomised character types.

### [4] Banned tic — "the shape of X" (2 occurrences)

> The rest was lost, but the shape of it was an apology wrapped in a reminder. (63)

> I smiled, tasting the shape of the trap before it closed. (105)

**Why:** `voice/_genre.md` line 43: "**'the shape of X'** — Claude tic for gesturing at pattern without naming it. Never use. If you find yourself reaching for it, name the actual thing instead."
**Suggested rewrite:** Line 63 → `The rest was lost. It was an apology with a reminder folded inside it.` Line 105 → `I smiled. I could see the trap, and I could see where it closed.`

### [5] Voice spec conflict — sentimentality, line 29

> The surface world's memory was mercifully short, and I found I did not mind being forgotten so quickly.

**Why:** Spec: "She does not confess emotion. She analyzes. If she names a feeling, it is because the analysis required it." Failure-prevention rule 1: "Do not make Valphine sound sentimental, confessional, or soft." `I found I did not mind` is a confession with no analytic payload, and `mercifully` grants the surface world a grace she does not extend.
**Suggested rewrite:** `The surface world's memory is short. A useful property, and one I intend to use.`

### [6] Voice spec conflict — sympathetic read of Vukradin, line 31

> "I bought everybody a beer, so that's something," Vukradin said, and I could hear the smallness in it—the way he measured himself against deeds that should have weighed more than they did.

**Why:** Spec line 51: "She reads Vukradin's sincere moral optimism as expert manipulation, because in her grammar there is no other category for it. She admires the maneuver while misidentifying the motive." Hearing *smallness* and self-measurement is pity — a category she does not have for him.
**Suggested rewrite:** `He said it lightly, the way a man does when he wants the room to argue him out of it. It worked. Brewbarry argued him out of it.`

### [7] Cross-narrator tic — "bless his/him", lines 19 and 117

> Brewbarry, bless his simple heart, picked up the thread without missing a beat. (19)

> Brewbarry, bless him, was still circling the question. (117)

**Why:** Twice in one scene, and once more in Soma's scene 04 (`Linene, bless her`, line 133). It is a warm, folksy indulgence that belongs to neither narrator, and it reads as one voice wearing two hats. Valphine's care "shows up as exact intervention," never as affectionate commentary.
**Suggested rewrite:** Line 19 → `Brewbarry picked up the thread without missing a beat. He is simple, not slow; the distinction escapes most people.`

### [8] Cliché simile and generic reach — lines 109 and 57

> The words landed in my chest like a stone in still water. (109)

> *The mermaid statue.* I remembered it—a small, beautiful thing, carved with a longing that had seemed almost alive. (57)

**Why:** Both are workshop-standard fantasy images. `voice/_genre.md` line 46 bans "generic fantasy reach"; the spec demands her body be present as "burn, sting, pulse, the edge of light on skin." A stone in still water is nobody's specific sensation. `carved with a longing that had seemed almost alive` names beauty without seeing the object.
**Suggested rewrite:** Line 109 → `The Spire of the Morninglord. Of course. The one place on the surface that could still summon me.` Line 57 → `A small thing, scaled, the tail worked fine enough to catch a thumbnail. Elven work. Someone had wanted it badly enough to pay for that much detail.`

## Also present

- ~~Missing `### Valphine` POV heading~~ — **withdrawn 2026-08-09.** `assemble.py` builds the section header from frontmatter, not from the in-body heading; nothing was broken. See the correction in `voice_critique_summary.md`.
- **13 narration-level em-dashes**, all unspaced (`Toblen—Spider-Man`), where scenes 01, 03 and 05 use spaced ` — `. Inconsistent within the same run.
- **Extraction artifact leaking into prose**, line 105: `"Well, yes, that's our next [stop]."` — the bracketed reconstruction from the smoothed layer was carried through into narration.

## Verdict

Seven passages of GM stage direction are sitting inside quotation marks as character speech, and the immutable-quote rule means no re-run of the voice pass can fix them — the upstream extraction has to stop quoting GM narration first. Do not re-narrate this scene until that is addressed; the same defect will come back.
