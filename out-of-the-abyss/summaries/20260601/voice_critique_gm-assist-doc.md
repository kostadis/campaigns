# Voice Critique — gm-assist-doc.md (Candlekeep crime-scene, 6 narrator blocks)

**Narration:** `summaries/20260601/gm-assist-doc.md`
**Voice specs:** `voice/daz_voice.md`, `voice/grygum_voice.md`, `voice/zalthir_voice.md`, `voice/thorin_voice.md` (all present)
**Per-char examples:** `examples/daz.md`, `examples/grygum.md`, `examples/zalthir.md`, `examples/thorin.md` (all present)

> Single assembled doc, so one report with a section per `## <Name>` block. Review-only — every "Suggested rewrite" is a suggestion, not an edit. Nothing in `gm-assist-doc.md` was touched.

## Headline: three systemic tics fire across the whole document

These recur in more than one block and tie directly to standing feedback memory. Fixing the pattern is worth more than any single flag below.

1. **Bookkeeping-verb convergence.** "I filed that / I filed it / I filed both," "column," "ledger," "balance to" now appear in *all four* narrators. The vocabulary is **canonical for Grygum** (`it's what I do` / `I took notes`) and **identity for Daz** — but Daz's spec explicitly says *rotate it, don't let one noun dominate a scene*, and **Thorin and Zalthir should not sound like clerks at all.** "I filed it" on Thorin (block 4) is the clearest off-voice instance: Thorin reads terrain, he doesn't keep books. See `[[feedback-oota-narration-systemic-tics]]`.
2. **"the shape of X"** — banned Claude tic, three occurrences (Daz block 1, Grygum block 2, Daz block 6). See `[[feedback-narration-banned-words]]`.
3. **"with the [quality] of a man / someone who…"** — banned construction, three occurrences (Daz block 1, Grygum block 2, Daz block 6). See `[[feedback-oota-narration-systemic-tics]]` ("with the particular X of someone who…").

---

## Block 1 — Daz: Investigation of the Keeper's Body

### [1] Banned construction
> with the unhurried hands of someone who had nowhere to be.

**Why:** The "with the [quality] of someone who…" template is the OOTA-flagged tic; Daz's actual register is flat declarative assessment, not appositive characterization.
**Suggested rewrite:** "He had not been in a rush. He had been desecrating a corpse at his leisure, with nowhere to be."

### [2] Banned phrase — "the shape of"
> I sat with the shape of it.

**Why:** "the shape of X" gestures at a pattern instead of naming it; Daz names. He reconstructs sequences, he doesn't sit with shapes.
**Suggested rewrite:** "I ran the sequence one more time." (Daz audits; he re-checks the account.)

### [3] Bookkeeping density (spec says rotate, don't stack)
> I thought it was the likeliest column to balance to. But thinking it and proving it are different ledgers

**Why:** Two ledger-metaphors in one sentence, on top of "I filed that" and "auditor of other people's competence" earlier in the same block. The spec wants the bookkeeping *rotated* across a scene, not clustered — and names "ledger" as the noun to keep from dominating.
**Suggested rewrite:** "I thought it the likeliest answer. But thinking it and proving it are different things, and we had no one who could read the substance."

---

## Block 2 — Grygum: Forensic Investigation of the Keeper's Chamber

### [1] Banned construction
> Daz worked the body over with the careful attention of a man reading the last page of someone else's diary.

**Why:** Same "with the [quality] of a man who…" template. Grygum's narration is paratactic and plain; this is a nested literary appositive he wouldn't build.
**Suggested rewrite:** "Daz worked the body over carefully. He had the eye for it, and the recent education — Milo's murder mystery, fresh in his head."

### [2] Banned phrase — "the shape of"
> An hour of his evening I could suddenly see the shape of, even if I couldn't see the face that did it.

**Why:** "see the shape of" is the banned gesture. Grygum's instinct is to *account for* a span of time, not to see its shape.
**Suggested rewrite:** "An hour of his evening I could suddenly account for, even if I couldn't see the face that did it."

### [3] Elevated/purple for Grygum
> The chain remembered the weight even though the man no longer could.

**Why:** Grygum does use a biblical-formal flourish, but it drops back to plain in the next breath; this line stays lyrical past his register and personifies the chain. "there is a particular grief in an empty setting" in the prior sentence is already carrying the feeling.
**Suggested rewrite:** "The links were worn where it had hung. Whatever it was, he'd carried it a long time."

**Not flagged (correct as written):** "I filed it. A bruised nose into a timeline — it's what I do." This is canonical Grygum — do **not** strip "filed" here. `[[feedback-oota-narration-systemic-tics]]` specifically protects it for him.

---

## Block 3 — Zalthir: Clues in the Ink and Parchment

### [1] Workshopped simile
> We came back to it the way you come back to a knot you've half-untied — not because anything was new, but because we hadn't yet looked at it in the order it had happened.

**Why:** Zalthir's examples are terse and observational; he registers the world and stops. The extended knot simile is more decoration than he carries. The *content* after the dash is pure Zalthir and should survive.
**Suggested rewrite:** "We came back to the desk. Not because anything was new — because we hadn't yet read it in the order it happened."

**Strongest block in the doc.** The monk-uncertainty device lands perfectly ("The Garden Shadow had a saying about that — or possibly Brother Tharusk did, the tall one who always smelled of incense; I wasn't listening to either of them closely"), and "A room tells you most by what it is missing" is exactly his terse-aphorism register. One flag only; not worth re-narrating.

---

## Block 4 — Thorin: The Rivalry Revealed

### [1] Bookkeeping bleed (off-voice for Thorin)
> Two keys. One around a dead man's neck, gone. One with a gate warden. I filed it.

**Why:** "I filed it" is a Daz/Grygum verb. Thorin doesn't keep books — he reads terrain, and the very next sentence ("That's the terrain now") proves he knows his own idiom. The imported "I filed it" sits on top of his actual voice.
**Suggested rewrite:** Delete "I filed it." and run straight into the terrain line: "Two keys. One around a dead man's neck, gone. One with a gate warden. That's the terrain now — not bridges and pits, just keys and grudges, but it works the same."

### [2] Generic mystery prose
> And there it was. The satisfying click of a thing dropping into place.

**Why:** "click of a thing dropping into place" is stock detective-prose, and it converges with the same "click/tumblers" image in Daz's cat block. Thorin's vocabulary is concrete and load-bearing — stone, ground, weight.
**Suggested rewrite:** "And there it was. A name with weight to it."

**Not flagged (well-deployed canon):** "Rage that's had time to set is a vector. It points somewhere," and "a rock in the right place is a wall, and Daral Yashenti had just walked himself into being the wall" — both straight from the giant-saying / rage-as-vector material in his spec, used correctly.

---

## Block 5 — Grygum: The Housekeeper's Testimony

### [1] Literary simile outside Grygum's image vocab
> Hollypocket's apartment sat below the Keeper's tower like a footnote below the text — modest, but with room to breathe

**Why:** Clever, but a bookish "footnote below the text" simile isn't in Grygum's concrete, paratactic image bank; it reads as the narrator-persona being witty rather than Grygum noticing a room.
**Suggested rewrite:** "Hollypocket's apartment sat below the Keeper's tower — modest, but with room to breathe, and warm in a way the chamber above us had not been." (keep the second clause, drop the simile)

### [2] Mild generic tag
> I wrote it down — slowly, the way you write the thing that matters.

**Why:** "the way you write the thing that matters" is a soft generic flourish; Grygum's note-taking is canonical but lands harder when it's plain.
**Suggested rewrite:** "I wrote it down slowly. That one mattered."

Otherwise strongly on-voice: the verbatim "These relationships are so complicated," the casual-Bahamut aside ("even Bahamut, who has rarely volunteered an opinion on anything, would not call that nothing"), and "They do not want to be interrogated. They want permission" are all dead-on.

---

## Block 6 — Daz: Interrogating the Tower Cat

### [1] Banned construction + bookkeeping
> "Well, that saves me money on potions," said Grygum, relieved in the way of a man who has just had an expense removed from his account by someone else's labor.

**Why:** "in the way of a man who…" is the banned template, *and* it's a fourth account/expense metaphor. Double tic in one sentence.
**Suggested rewrite:** "'Well, that saves me money on potions,' said Grygum — relieved, the way a man is when someone else's work has just taken an expense off him."

### [2] Banned phrase — "the shape of"
> A negotiation, then. I know the shape of those.

**Why:** Third "shape of" in the doc; the banned gesture. Daz would name it as a con he's run.
**Suggested rewrite:** "A negotiation, then. I have run a few of those."

### [3] Generic mystery simile (+ convergence with Block 4)
> It clicked the way a lock gives when your fingers find the tumblers before your mind does.

**Why:** Stock lock-and-tumblers simile, and it echoes Thorin's "click of a thing dropping into place" two blocks earlier — house-style convergence. The next sentence ("The right question, at the right weight, landing exactly where I aimed it") already does the work cleanly.
**Suggested rewrite:** Cut the simile; let "It clicked. The right question, at the right weight, landing exactly where I aimed it." carry it.

### [4] Bookkeeping density
> I filed the obvious solution where it belonged: in my own column.

**Why:** Plus "I filed both" later in the same block — Daz is "filing" twice and using "column," in a document where every other narrator is also filing. Keep at most one filing image per block and rotate the noun.
**Suggested rewrite:** "So I put the obvious solution where it belonged: in my own column."

Strong on-voice lines to keep: "The con never stops; I only ever recognize someone else running mine," and "I have been insulted by archpriests. This one landed cleaner."

---

## Verdict

The dominant issue is **cross-narrator convergence on bookkeeping vocabulary** — "filed / column / ledger" has leaked out of Daz (where it's identity, but over-stacked) and Grygum (where it's canonical) into Thorin and Zalthir, flattening four distinct voices toward one clerk. Layered on top are two repeating banned forms — "the shape of X" (×3) and "with the [quality] of a man who…" (×3). These are systemic, not per-sentence: the cheapest durable fix is a find-pass for those three patterns across the whole doc, then spot-edits from the rewrites above. **Zalthir (block 3) is clean and not worth re-narrating; Thorin (block 4) needs only the two edits above to stop sounding like he keeps a ledger.** If you'd rather re-run than hand-edit, the bookkeeping convergence is a voice-file/genre-prompt problem (it's the same tic in every section), so re-running individual scenes won't fix it — tighten the anti-tic guidance first.
