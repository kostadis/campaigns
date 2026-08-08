# Voice Critique — Soma, scene 04: Cheese, Business Plans, and Departure Preparations

**Narration:** `summaries/20260623/narration/session_doc_scene_04_cheese_business_plans_and_departure_preparations.scrubbed.md`
**Voice spec:** `voice/soma_new_pipeline.md` (authoritative)
**Supplementary spec:** `voice/v1/soma_voice.md`, `voice/v1/soma-voice-addendum.md`
**Per-char examples:** `examples/soma.md` (178 lines, five passages — see the register conflict note below)
**Genre:** `voice/_genre.md`

Line 155 differs from the raw `.md` following today's scrub pass.

## Flags

### [1] Banned tic — "with the [X] of a man/someone/a woman who…" (3 occurrences)

> Vukradin, watching the proceedings with the expression of a man who was beginning to understand that prosperity was spreading, muttered, "They really are getting high on the UBT now." (37)

> I looked at Valphine, who looked back with the expression of someone who had seen a miracle and wasn't sure if it was real. (95)

> I knew the look. I'd seen it on her face before, the hunger of a woman who wanted something strange enough to be dangerous. (161)

**Why:** `voice/_genre.md` line 44 bans this construction outright, and names Soma's own lens as the alternative: "physical-world-first." Her spec says she "notices the physical world first: wounds, posture, hands, breath." All three of these skip the body and go straight to a category of person.
**Suggested rewrite:** Line 95 → `Valphine looked back at me. Her eyebrows had gone up and stayed there.` Line 161 → `I knew the look. Her hands had gone still on the counter when she said it.` Line 161 is the costliest of the three, because the tic replaces the one physical tell that would make Soma's suspicion land.

### [2] Register-wrong vocabulary — modern business diction, lines 95 and 111

> Brewbarry, the man who had once charged a dragon bare-handed, was now a textile futurist. (95)

> The collaboration had officially become a vertical integration. (111)

**Why:** *Textile futurist* and *vertical integration* are twenty-first-century business-school English. Soma's spec: short practical sentences, conclusion before explanation, wisdom from "a long coastal life — weather, hospitality, fishing, mending — not from Enclave doctrine." Failure-prevention rule 1: "Do not make Soma sound literary for its own sake." Rule 4: not "chatty, rhetorical, or philosophically abstract." These are the narrator being clever in a register Soma has no access to.
**Suggested rewrite:** Line 95 → `Brewbarry charged a dragon bare-handed once. Now he was selling robes.` Line 111 → `Vukradin would make the songs. Brewbarry would make the robes. They had worked out how to sell each other's.`

### [3] Scan B — "filed that away," line 127

> *The ID guy.* I filed that away. Somehow I doubted the Consumers' League had such a title, but for Brewbarry, it fit like a glove.

**Why:** *Filed* is clerical, and it recurs: line 65 already has `I made a note.` Soma does not keep an archive — she notices and judges. Also `fit like a glove` is a dead idiom in a voice built on specific physical observation.
**Suggested rewrite:** `*The ID guy.* Not a title anyone would print. It fit him anyway.`

### [4] Cross-narrator tic — "Linene, bless her," line 133

**Why:** The same construction appears twice in Valphine's scene 02 (lines 19 and 117). Two different narrators reaching for the same folksy warmth is convergence, not voice. Soma's affection shows up as "practical help, restraint, competence, or private concern — not comfort."
**Suggested rewrite:** `Linene took the whole thing seriously, which surprised me and shouldn't have.`

### [5] Cross-narrator tic — "ever the X" (3 occurrences)

> Vukradin, ever the enabler: "Goes well with the wine." (35)

> Valphine, ever the supply-chain mind: "The source of Phandalin cotton, or something?" (103)

> Valphine, ever the pragmatist, put her real talents to work. (157)

**Why:** Three in one scene. `ever the pragmatist` is also used of Brewbarry in scene 02 line 65 — the same epithet, two different characters, two different narrators. See the summary report: this is a corpus-level tic present in three of the four example files, so it will keep returning until `_genre.md` names it.
**Suggested rewrite:** Line 35 → `Vukradin poured. "Goes well with the wine."` Let the action do the characterising.

### [6] Mechanical scan A — 10 narration-level em-dashes

Lines 11, 17, 37, 45, 111, 133, 145, 161, 169, 185. All unspaced (`spread—rounds`), matching scene 02's convention and differing from scenes 01, 03 and 05.

**Why:** Soma's spec is "short, practical sentences. Conclusion before explanation." The em-dash defers the conclusion by splicing a qualifier in front of it.
**Suggested rewrite:** Line 17 `She gestured at the spread—rounds and wedges of every age and color` → `She gestured at the spread. Rounds and wedges, every age and color.`

## Possible fabrication (flagging, not asserting)

Line 127 refers to **"the Consumers' League"** as though it were an established body. I find no reference to it in `docs/`, and it does not appear in the entity registry. If it is not campaign canon, this is invented institutional detail entering narration. Worth a check before assembly.

## Register conflict in the inputs (not a fault of this scene)

`examples/soma.md` is internally inconsistent with `voice/soma_new_pipeline.md`. The Chapter 03, 04 and 14 passages are terse and dry — the spec's Soma. The Chapter 08 and 11 passages are lush and literary ("its subtle shimmer hinting at its significance," "impossible geometries," "a hypnotic dance"), which the spec explicitly forbids in rules 1, 5 and 10. The pipeline receives both. When the narration drifts literary, it is following half its own inputs.

## Not flagged (working as intended)

Line 27 (`I took a long, slow breath, the kind that settles under a shell`) and line 65 (`Somewhere under that thick skull, there was actual philosophy forming`) are exactly right — bodily, dry, verdict-first. Line 201's `*My bale,* I thought` uses the signature correctly and lands the scene.

## Verdict

Three banned-tic instances and two business-school phrases pull Soma toward a generic clever narrator, and the tic at line 161 costs the scene its best physical tell. Spot-edit; the frame and the closing beat are sound.
