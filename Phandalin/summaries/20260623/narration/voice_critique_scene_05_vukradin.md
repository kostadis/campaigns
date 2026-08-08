# Voice Critique — Vukradin, scene 05: Arrival in Neverwinter

**Narration:** `summaries/20260623/narration/session_doc_scene_05_arrival_in_neverwinter.scrubbed.md`
**Voice spec:** `voice/vukradin_new_pipeline.md` (authoritative)
**Supplementary spec:** `voice/v1/vukradin_voice.md`
**Per-char examples:** `examples/vukradin.md` (162 lines, four passages)
**Genre:** `voice/_genre.md`

The strongest-voiced scene of the six. Flags are concentrated in the interior passages, not the action.

## Flags

### [1] Banned tic — "the shape of X," line 145

> He was in awe — I could see it in the way his hands shook slightly against the frets — but he was also good. He could hear the shape under the dissonance. He jammed with me.

**Why:** `voice/_genre.md` line 43 bans this by name. It is especially costly here: this is the emotional peak of the scene, another musician hearing what Vukradin actually wrote, and *the shape under the dissonance* gestures at the thing instead of naming it. Vukradin is a musician — he has real vocabulary for this.
**Suggested rewrite:** `He could hear what the dissonance was for. He jammed with me.`

### [2] Cliché simile — line 43

> "Reunion tour?" Soma asked, dry as old parchment.

**Why:** Workshop-standard. `voice/_genre.md` line 46 bans generic fantasy reach and line 38 asks for "the sensory specific… before the metaphor." Soma is a tortle; her dryness has a body available to it, and old parchment is not it.
**Suggested rewrite:** `"Reunion tour?" Soma asked, without looking up.`

### [3] Voice spec conflict — verdict register absent again

**Why:** As in scene 03: a mechanical scan finds none of the spec's signature landings ("Foolish!" / "Scandalous." / "Phonies!" / "Nope." / "Done.") anywhere in this scene. Failure-prevention rule 8: "Do not let long building sentences drift without landing in a clear verdict." The scene has three long builds (lines 119, 121, 191) and all three land in soft abstraction. Line 109 is where the verdict belongs — Vukradin realising the Common Chord has been captured by the Protector's Enclave is precisely the "corruption gets in the way of the studio" trigger the spec calls a personal injury.
**Suggested rewrite:** Line 109 → `Oh. So the Common Chord wasn't mine anymore. It was the Protector's Enclave's. The rich walling off what belonged to everyone. Scandalous.`

### [4] Repetition — the same realisation stated four times

> ...he wasn't wrong about me, exactly. I did care. (119)

> But the kid was also wrong in a way I couldn't articulate... It was caring *so much* you had to let the song do the saying. (121)

> That's when I started to realize the kid was wrong in another way. It wasn't just that I cared. It was that caring was catching. (151)

> ...I realized the music I'd written when I didn't care if anyone liked it had become the music people *needed* precisely because I'd cared enough to write it. (191)

**Why:** Four restatements of one insight, three of them announcing themselves as realisations (`the kid was wrong in a way`, `wrong in another way`, `I realized`). `voice/_genre.md` line 49 bans recap framing — "do not have characters mentally summarize what just happened for the reader's benefit." The performance at lines 141–153 already dramatises the whole idea; the prose then explains it three more times.
**Suggested rewrite:** Keep 121, cut the explanatory halves of 151 and 191. Line 191 ends better on its concrete list: `It *was* funny. All of it — the blood autograph, the sold-out debate, the kid claiming I wasn't me.` Then stop.

### [5] Cross-narrator tic — "Brewbarry, ever the showman," line 67

**Why:** The identical epithet `ever the showman` is applied to *Vukradin* in scene 02 line 13. Same two words, two different subjects, two different narrators, one session. See the summary report for the corpus-level finding.
**Suggested rewrite:** `Brewbarry did a discreet pec bounce for the crowd.` The action is already the characterisation.

### [6] Mechanical scan A — 30 narration-level em-dashes

Tied with scene 03 for the highest in the session. Excludes em-dashes inside `"..."` and `*...*`.

**Why:** Lines 119, 121 and 191 each carry a mid-sentence em-dash pair inside an already long clause-stack, which is what makes those builds drift rather than land (flag [3]). Vukradin's long register works when it accelerates toward a verdict; the em-dash parentheticals keep braking it.
**Suggested rewrite:** Line 121 `And I knew — I'd known since the tower, since the lighthouse, since every fair-trade coin I'd ever counted — that the music was the opposite.` → `And I knew better. I'd known since the tower, since the lighthouse, since every fair-trade coin I'd ever counted. The music was the opposite.`

## Not flagged (working as intended)

The fan-club sequence (lines 57–107) is the best-voiced stretch of the session: the blood-autograph bit, the guard's face falling, and especially line 101 (`There were two Vukradins now, apparently. The one I was, and the one they'd decided I wasn't`). Line 97 (`I stood right there, in front of him. And he didn't recognize me.`) is the short-landing register the spec asks for, and it works.

## Upstream notes (locked dialogue — not voice issues)

Two items inside quotation marks, correctly left verbatim by the voice pass, that may want VTT adjudication:

- Line 117: `"I'm gonna write that down on the quest tracker."` — **quest tracker** is table vocabulary sitting in in-fiction dialogue. Today's scrub pass could not catch it (no numeric or fixed-phrase pattern matches it) and the immutable-quote rule blocks the voice pass from touching it.
- Line 65: `"Sam Club has found us."` — probable VTT garble of *Sam's Club*, part of the Fan Club joke.

## Verdict

The interior passages restate one realisation four times and none of them land in Vukradin's verdict register, which leaves the scene's best material — the fan club, the performance — carrying prose that keeps explaining it afterward. Spot-edit the four interior beats; the scene does not need re-narrating.
