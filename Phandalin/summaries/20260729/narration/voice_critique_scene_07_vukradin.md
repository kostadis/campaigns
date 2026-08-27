# Voice Critique — Vukradin, scene 07: A Summons from the Lord Protector

**Narration:** `summaries/20260729/narration/session_doc_scene_07_a_summons_from_the_lord_protector.md` (raw — no `.scrubbed.md` exists)
**Voice spec:** `voice/vukradin_new_pipeline.md`
**Genre spec:** `voice/_genre.md`
**Per-char examples:** `examples/vukradin.md`

Mechanical scan A (em-dashes): **11 narration-level** (L9, L21 ×2, L27 ×2, L37, L49, L63 ×2, L83 ×2) of 26 total — the highest count in the session by a wide margin.
Mechanical scan B (register vocabulary): clean.

## Flags

### [1] Structural — the narrator disappears into a chain of quotes glued by em-dashes

> "Yeah, we've got sacred rites to perform, we've got other treasures we need to return to their rightful owners, I need to stop by my old…" — "I'm always up for a second," said Brewbarry, helpfully. "Performance, it's gonna be a late night, yeah. Are you arresting me?"

**Why:** L49, L63, L83 and L89 are paragraphs in which four or five speakers are spliced together with dashes and Vukradin contributes only "I said." `_genre.md` asks for minimal tag lines, "often just a thought between the speech beats" — this has gone past minimal into transcript, and it is the direct cause of the 11-dash count. The dashes are a symptom; the missing interior is the problem.
**Suggested rewrite:** Break each chain into its own paragraph and put one Vukradin beat between them, e.g. after the wine exchange: *He wrote down Chateauneuf du Pape without knowing what it was. That is the mark of a good household.*

### [2] Voice spec conflict — arch, knowing register where sincerity belongs

> I chose to take it as a statement that my name required no ornament, which is true, but someone in Neverwinter's heraldry office should be spoken to.

and:

> Marketing is a discipline, and she refuses to study it.

**Why:** Failure-rules 1 and 2 — "Do not make Vukradin sound cynical, smirking, or sardonic. He is sincere." / "If a sentence reads as winking, blunt it into sincerity." Both lines are dry-wit constructions that put him above the moment. The underlying observations are fine; the delivery is a wit's, not his.
**Suggested rewrite:** Valphine of the Blessed. Soma, protector of the Glades. Vukradin, apparently, just Vukradin. My name has never needed one. Still — the Blessed is a good one. I should find out who writes these. / She has been trying to get people to say the Searing Light for weeks. Nobody says it. I keep telling her a name has to be sung a hundred times before it sticks.

### [3] Voice spec conflict — hardboiled aphorism

> A summons dressed as an invitation is still a leash, and I have had enough of leashes from Ser Kaelen alone to know the feel of one.

**Why:** Failure-rule 6 — "Do not give him hardboiled realism. 'That's just how the world works' is not in his grammar; the world keeps disappointing him, and he has not concluded that disappointment is its nature." The maxim-plus-world-weary-clause construction is exactly that grammar.
**Suggested rewrite:** Tomorrow morning, before the noon bell. He asked it like a favor. It was not one. I have had about enough of people telling me where to be, and Ser Kaelen already has that job.

### [4] Music metaphor deployed twice in three paragraphs

> And here I saw the whole thing clearly, the way a progression resolves.

then:

> I made the pitch and felt it land, the way you feel a chord settle into a room.

**Why:** Failure-rule 5 — "Do not deploy music metaphors in every paragraph. The metaphor surfaces where it earns its place." Two identical resolution-images back to back cancel each other; the second is the stronger one.
**Suggested rewrite:** Cut the first. *And here I saw the whole thing clearly.* Keep "the way you feel a chord settle into a room."

### [5] Em-dashes — narration level, outside the quote chains (mechanical scan A)

> The steward — Aldus Hern, tidy, careful hands — squared his shoulders and delivered the thing properly.
> ...announced, "I found you!" — as if we had been hiding...

**Why:** These two are ordinary narration dashes independent of flag [1] and convert cleanly.
**Suggested rewrite:** The steward, Aldus Hern, tidy and careful with his hands, squared his shoulders and delivered the thing properly. / ...announced, "I found you!" as if we had been hiding...

## Out-of-scope observation — verbatim quotes were mutated upstream

> "On behalf of Lord Dagult Neverember, Dagult Neverember of Neverwinter, I extend a formal welcome to your group. The Dagult Neverember has followed your recent activities with considerable interest."

The source reads **"Lord Dagult Neverember, Lord Protector of Neverwinter"** and **"The Lord Protector has followed..."** (`scene_extractions_smoothed/07_...md`). `docs/aliases.json` maps `Lord Protector → Dagult Neverember` and `sd_narrate.py` applies it to quote text. Note the doubling ("Lord Dagult Neverember, Dagult Neverember") — the standard find-and-replace tell. See `voice_critique_summary.md`; not fixable in this file.

## Verdict

Vukradin stops narrating for four long stretches and the scene becomes a transcript with dashes for punctuation — that is where all 11 em-dashes live and it is the only structural problem here. The Alducia passage ("a lie built out of shyness is not plunder. There is no victim in it except his own pride, and I saw no reason to add one.") is the best thing in the session and is pure spec-compliant Vukradin. Break the quote chains, blunt two arch lines, and this is finished.
