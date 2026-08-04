# Voice Critique — Valphine, scene 05: The Statue Returned, a Quest Begun

**Narration:** `summaries/20260729/narration/session_doc_scene_05_the_statue_returned_a_quest_begun.md` (raw — no `.scrubbed.md` exists)
**Voice spec:** `voice/valphine_new_pipeline.md`
**Genre spec:** `voice/_genre.md`
**Per-char examples:** `examples/valphine.md`

Mechanical scan A (em-dashes): **0 narration-level** — all 5 are inside quotes. Clean.
Mechanical scan B (register vocabulary): clean.

## Flags

### [1] Genre spec conflict — the whole scene is in present tense

> Lord Cassian Meliamne sits at it, a sea elf, still as tidewater, and he recognizes Vukradin before we have crossed half the floor.

**Why:** `_genre.md`: "**First-person past tense, always** ("I", "we")." Same violation as scene 03, and because 04 and 06 sit either side of it in past tense, the assembled doc flips tense twice. Whole-file conversion.
**Suggested rewrite:** Lord Cassian Meliamne sat at it, a sea elf, still as tidewater, and he recognized Vukradin before we had crossed half the floor. *(...and throughout.)*

### [2] Referent collision — "the Bard" used for two different men in consecutive sentences

> "I like that it's compartmentalized money," the Bard says, pleased with himself. He does not want to offend the Bard, so the donation goes to the studio and the thanks go to the traveling companions, independently.

**Why:** "He" is Cassian, but the nearest antecedent is the Bard, so the sentence reads as Vukradin not wanting to offend himself. Failure-rule 2 — her long sentences must land in a clear verdict, not a knot.
**Suggested rewrite:** "I like that it's compartmentalized money," the Bard says, pleased with himself. Cassian does not want to offend him, so the donation goes to the studio and the thanks go to the traveling companions, separately.

### [3] Tell-not-show — she names a feeling instead of analyzing it

> The grief is real, and real grief is a rarer thing than gold in either world. I find myself almost respectful.

**Why:** Two problems in one breath. "rarer thing than gold" is a stock comparison (failure-rule 5, "Do not flatten her into generic 'smart prose'"), and "I find myself almost respectful" is confession — the spec says "She does not confess emotion. She analyzes. If she names a feeling, it is because the analysis required it." Her respect should arrive as a revised estimate, not a stated mood.
**Suggested rewrite:** The grief is real. Real grief is the one thing in either world that cannot be counterfeited cheaply, which is why so few bother. I revise my estimate of him upward, and my estimate of his life expectancy down.

### [4] The narrator vanishes for six consecutive quote paragraphs

> "She was investigating the interplanar shipping device at the docks before she died. The displacement manifold. It stopped working about 7 weeks ago..."

**Why:** L83–L87 and L93–L97 are six unbroken paragraphs of Cassian speaking with no interior between them. `_genre.md` allows minimal tag lines — "often just a thought between the speech beats" — but Valphine is the most analytic narrator in the ensemble and her POV is the reason this scene is hers. She would be pricing every clause as it lands.
**Suggested rewrite:** Break the run with one-line reads between the quotes, e.g. after "*Nobody official will say why*": *Nobody official. So somebody unofficial already has, and she wrote it down.*

### [5] The faith register is absent from the entire scene

**Why:** The spec devotes three bullets to her Lathander voice — "radiant, indifferent, inexhaustible, power incarnate, power without apology" — and the party is one scene away from a dawn sermon at her own temple. Scene 05 contains no light, no pain, no Overbright, no theology of any kind; she reads here as a generically shrewd noirish observer, which failure-rule 5 names directly.
**Suggested rewrite:** Fold one into an existing beat — at the reward, e.g.: *Coin given because giving costs him nothing. My god does not ration what he gives either, and no one has yet accused the dawn of generosity.*

## Out-of-scope observation — scenes 04 and 05 narrate the same events twice

The statue handover, "For free drinks," Cassian clicking his fingers, "wrapped around their finger," and the performance all appear in **both** scene 04 (Vukradin) and scene 05 (Valphine) — not as two angles on one moment but as the same beats retold. The overlap is inherited from the source: `scene_extractions/04_meeting_lord_cassian_and_a_musical_performance.md` and `05_the_return_of_the_meliamne_statue_and_a_new_quest.md` both contain the handover. This is a scene-splitting problem upstream of narration; it cannot be fixed by editing either file, and it is the thing a reader will notice fastest in the assembled doc.

## Verdict

Present tense plus a missing faith register make this the least Valphine-sounding of her two scenes — the analysis is sharp but it could be any clever narrator's. "The Bard's temple grows on tithes he refuses to call tithes" and the manifold read at L89 are exactly right and show what the rest should sound like. Given the tense conversion and the scene-overlap problem both land here, this is the one scene worth considering for a re-run rather than a spot-edit.
