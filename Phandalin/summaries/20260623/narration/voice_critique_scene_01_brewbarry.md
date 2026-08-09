# Voice Critique — Brewbarry, scene 01: Return to Phandalin

**Narration:** `summaries/20260623/narration/session_doc_scene_01_return_to_phandalin.scrubbed.md` (re-rendered 2026-08-09, 1285 words — up from 829)
**Voice spec:** `voice/brewbarry_new_pipeline.md` (authoritative — `config/session_doc.yaml` sets `voice_dir: voice`)
**Supplementary spec:** `voice/v1/brewbarry_voice.md`
**Per-char examples:** `examples/brewbarry.md` (40 lines, two passages only)
**Genre:** `voice/_genre.md`

*Second pass. Critiques the re-rendered and scrubbed text, not the version reviewed on 2026-08-08.*

## Resolved since the previous render

- The epigram at old line 15 (`unfair is just a fight you haven't named yet`) is gone.
- The redundant customer sentence at old line 45 is gone — it now sits inside locked dialogue at line 95 and reads cleanly.
- The `*Inaudible.*` transcription artifact was removed and `[inaudible]` restored inside the quote at line 71 (scrub pass, 2026-08-09).
- **POV heading flag withdrawn.** My earlier claim that `assemble.py` needs a `### Brewbarry` heading was wrong — `session_doc/assemble.py` lines 165–167 build the section header from the frontmatter `narrator:` field and never read the in-body heading. Nothing was broken. See the correction in `voice_critique_summary.md`.

## Flags

### [1] Banned tic family — taxonomising a person instead of rendering what was seen (7 occurrences)

> I watched him walk ahead of me, his shoulders doing **that thing they do** when he's thinking too hard about what's fair. (11)

> Vukradin's face did something complicated — surprise, then calculation, then **that grin he gets** when an idea lands. (25)

> Soma **had a way of saying** things that made the whole world feel smaller and more honest at once. (57)

> She had **that look** — **the one she gets** when she's about to talk about her god and doesn't care who hears it. (63)

> That particular pinch between his eyebrows. He was about to do **that thing he does** — turn someone's sharp edges into something the town could swallow. (81)

> Vukradin turned to me, **that look in his eye. The one he gets** when he's about to argue about money. (99)

> The tortle **had a way of cutting** through philosophical knots with the simplest blade. (113)

**Why:** `voice/_genre.md` line 44 bans this construction and explains exactly why: it is "Claude tic for taxonomizing a person's behavior instead of rendering what the POV character actually saw… one Claude narrator wearing five hats." The re-render did not remove the tic — it swapped the surface form. The previous version used `with the [X] of a man who…`; this one uses `that look/thing X gets when…` and `had a way of X-ing`. Seven instances in 1285 words is roughly one per 180 words, and the spec is explicit that Brewbarry's lens is **bodies and weight**, not behavioural categories.
**Suggested rewrite:** Line 11 → `He walked ahead of me with his shoulders up around his ears. He does that when something isn't fair.` Line 63 → `Valphine's chin came up. She was going to talk about her god, and she was going to do it loud.` Line 99 → `Vukradin turned to me. Here it comes, I thought. Money.`

### [2] Banned tic — "the shape of X," line 39 — newly introduced

> I didn't understand half of it, but I understood the shape of it — two exiles building something that wasn't exile.

**Why:** `voice/_genre.md` line 43: "**'the shape of X'** — Claude tic for gesturing at pattern without naming it. Never use. If you find yourself reaching for it, name the actual thing instead." This is a **regression** — the previous render of scene 01 did not contain it. Session-wide the count is now five.
**Suggested rewrite:** `I didn't understand half of it. I understood the part that mattered — two exiles building something that wasn't exile.`

### [3] Register-wrong vocabulary — line 113

> Soma again. Three beats, like a drum. The tortle had a way of cutting through philosophical knots with the simplest blade.

**Why:** *Philosophical knots* is abstract vocabulary Brewbarry does not have. Failure-prevention rule 3: "Do not give him complex moral arguments about systems, factions, or ideology." His examples render thinking as physical contest — `examples/brewbarry.md` gives us "Order is bullies. They bully barbarians," not analytical metaphor. The `like a drum` beat before it is good and already carries the observation; the third sentence explains what the second one showed.
**Suggested rewrite:** Cut the third sentence. `Soma again. Three beats, like a drum. She does that — says the short true thing while the rest of us are still talking.` (Or simply stop after `like a drum`.)

### [4] Abstract emotional summary — line 57

> Soma had a way of saying things that made the whole world feel smaller and more honest at once.

**Why:** Two problems: it is instance three of flag [1], and *made the whole world feel smaller and more honest at once* is a writerly abstraction rather than a thing Brewbarry noticed. Failure-prevention rule 6: "Do not over-explain his interior. The reader infers from his actions and his short sentences." The `*Titan.*` beat two sentences later does the emotional work already and does it well.
**Suggested rewrite:** `Soma says things like that. Short. True. *Titan.* That was me, once.`

### [5] Mechanical scan A — 10 narration-level em-dashes

Lines 21, 25, 39, 45, 63, 81, 107, 119, 129. Excludes em-dashes inside `"..."` and `*...*`.

**Why:** Density is down from the previous render in proportion to length, but the spec is "short, declarative sentences. He feels something and then he acts. There is very little space between the two." Four of these (25, 63, 81, 99) are attached to flag [1] instances — the em-dash is what lets the taxonomising clause hang off the observation. Fixing [1] removes most of them.
**Suggested rewrite:** Line 45 `me and the halberd and the sword that hummed against cold` is a parenthetical that works as commas. Line 129 `That's the deal we made — him with his clean gold…` → period, new sentence.

## Not flagged (working as intended)

Line 29 (`Softness, measured like a contest, and I intended to win it`) uses the contest frame from `characters/brewbarry.md` correctly. Line 45 (`me and the halberd and the sword that hummed against cold`), line 97 (`That's not contradiction. That's commerce.`) and line 121 (`That the red could become cream-colored and fluffy`) are the target register — bodily, short, unintentionally funny. Line 129's `my need to be something more than the cautionary tale` earns its abstraction because it names his actual arc.

## Upstream note (locked dialogue — not a voice issue)

Lines 101 and 105: `"Green — is that what you're saying, Brewbarry? You know it's stolen."` / `"Green? It's blood."` — **Green** reads as a VTT garble; the exchange is plainly about gold being blood money. Inside quotation marks, so no pass will touch it. Candidate for `notes/vtt_transcription_corrections.md`.

## Verdict

The re-render traded one banned construction for another — seven instances of `that look X gets` / `had a way of` where the previous version had `with the [X] of a man who`, and it newly introduced `the shape of it` at line 39. Spot-edit the seven; the scene's concrete material is stronger than it was.
