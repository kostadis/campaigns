# Voice Critique — Soma, scene 01: Factions and Fame in Neverwinter

**Narration:** `summaries/20260729/narration/session_doc_scene_01_factions_and_fame_in_neverwinter.md` (raw — no `.scrubbed.md` exists)
**Voice spec:** `voice/soma_new_pipeline.md`
**Genre spec:** `voice/_genre.md`
**Per-char examples:** `examples/soma.md`

Mechanical scan A (em-dashes): **0 narration-level** — the single `—` is inside Valphine's quote at L25. Clean.
Mechanical scan B (register vocabulary): 2 hits on `angle` (L45, L51), both idiomatic "motive/agenda" inside reported GM dialogue, not the geometric register. No action.

## Flags

### [1] Voice spec conflict — the signature phrase is used in the wrong sense

> I gathered my bale and my staff and followed him out into the loud.

**Why:** `soma_new_pipeline.md` defines "my bale" as *the party* — "She refers to the party as 'my bale' and treats them as hatchlings whether they like it or not" — but here it sits in a list beside the staff as a physical bundle, which inverts the one lexical item that is unmistakably hers. "Out into the loud" is also a nominalized adjective, which failure-rule 10 forbids ("If a sentence is beautiful, blunt it").
**Suggested rewrite:** I took up Meril's staff, got my bale moving, and followed him out.

### [2] Cliché / on-the-nose simile

> The statue for the Meliamne family was still wrapped in our baggage, heavy as guilt.

**Why:** "heavy as guilt" is a stock literary comparison, and it names the emotion the spec says she never names ("She does not openly state emotion... Emotion shows up in what she chooses to notice"). Soma registers weight as weight — the physical world first.
**Suggested rewrite:** The statue for the Meliamne family was still wrapped in our baggage. It had not gotten lighter in three weeks.

### [3] Voice spec conflict — philosophical abstraction where a verdict belongs

> "Great, it should not be meaningless," Valphine said, and I thought about seeds, and about how you never get to choose what the wind does with them.

**Why:** Failure-rules 4 and 9 — "Do not make her sound chatty, rhetorical, or philosophically abstract" and "Do not write long abstract moral arguments. She gives the verdict, not the lecture." The seeds-and-wind aphorism is the lecture.
**Suggested rewrite:** ...and I thought about a paladin sent alone to make orcs love a god. Somebody was going to find out how that went.

### [4] Narrator editorializing + a metaphor doing three shifts

> The only honest animal in the forest, and the whole forest squints at it. That told me more about this city than the roster did.

**Why:** The second sentence is exactly the "narrator editorializing" the genre spec bans — it announces the lesson instead of letting the observation land. The forest frame has also already carried L9 ("loud in a way a forest is never loud") and L29 ("The forest has bears, but the forest also has fire"); by its third appearance it reads as the narrator's device rather than Soma's habit of mind.
**Suggested rewrite:** The only honest animal in the room, and the whole room squints at it. *(Cut the second sentence entirely.)*

### [5] Register-wrong — lecture framing

> The talk at our long table turned to who ran this place, and the answer was a lesson in surface ecology.

**Why:** "a lesson in surface ecology" is an abstract noun phrase announcing a category. The spec has her deliver conclusions before explanations and keep the naturalist vocabulary concrete; the beaver-dam line two sentences later already does this job properly and does it well.
**Suggested rewrite:** The talk at our long table turned to who ran this place. Beavers, mostly.

### [6] Vague gesture where a specific observation belongs

> He had crossed some threshold, and there was no one in this city he could not make himself understood to.

**Why:** "some threshold" gestures at a change without naming it — the same move the genre spec bans under "the shape of X". Soma notices the physical world first; the glowing eyes are already on the page and are the concrete tell.
**Suggested rewrite:** The yellow in his eyes had come in properly now. There was no one in this city he could not make himself understood to.

## Out-of-scope observations — speaker attribution (for `/session-summary-consistency`, not this pass)

Three lines are attributed to Valphine that the source assigns elsewhere. The genre spec forbids re-attribution, and scene 02's narration gets the first one right, so these are narration-layer errors rather than source ambiguity.

| Narration | Source (`scene_extractions_smoothed/`) |
|---|---|
| L71 `"I have a feeling that's not gonna go well," Valphine said.` | **Vukradin** — `01_...md:112` (inside a `[Vukradin / GM]` block, GM lines tagged inline) and explicitly `**Vukradin**` at `02_...md:33` |
| L83 `Prutha was gone, Valphine said, sent on a quest to convert the orcs.` | **GM** — `01_...md:130` |
| L91 `"Great, it should not be meaningless," Valphine said` | **Vukradin** — `01_...md:134` |

## Verdict

The signature phrase "my bale" is used as an object rather than as the party, which is the one error that reads as the narrator not knowing Soma. Everything else is spot-editable — three metaphor blunts, one editorializing sentence to cut — and the algae-bloom and beaver-dam lines show the voice is well within reach. Spot-edit; do not re-narrate.
