# Voice Critique — Zalthir, scene 03: Infiltration of the High Tower Lobby

**Narration:** `session_doc_scene_03_infiltration_of_the_high_tower_lobby.md` (re-run 17:52 from `scene_extractions_smoothed/`)
**Voice spec:** `voice/zalthir_voice.md`
**Per-char examples:** `examples/zalthir.md`
**Genre spec:** `voice/_genre.md`
**Supersedes:** the 17:04 critique of the pre-smoothed draft

## Flags

### [1] Duplicated text — generation defect, blocks assembly

> Beside me, Daz was already weighing**Beside me, Daz was already weighing** the next thing — some working that would set the wizard's mind against his own craft.

**Why:** The clause is emitted twice with no separator. This is the same class of defect as the previous draft's `incomplete.I must` fusion — a generation artifact, not a voice problem. It will ship into the assembled document as-is.

**Suggested rewrite:** `Beside me, Daz was already weighing the next thing — some working that would set the wizard's mind against his own craft.`

### [2] "The Whorlstone entrance" survived the re-run — confirmed fabrication

> Then, working it out: "Oh, okay, it's the… the… yes. **The Whorlstone entrance.** Basically."

**Why:** The smoothed source reads `"Oh, okay, it's the… the… Yes. Entrance. Basically."` Grygum did not say *Whorlstone*. The previous draft produced the identical fabrication from a **different** input directory, so it has now reproduced deterministically across two runs from two sources — the model is back-filling a Gracklstugh location name into an unfinished fragment. Another re-run will produce it a third time.

Unlike last time, no narrator beat is built on top of it, so the fix is a two-word deletion.

**Suggested rewrite:** `Then, working it out: "Oh, okay, it's the… the… yes. The entrance. Basically."`

### [3] "Brother Quellin" is the spec's own example name — the one thing the voice file says not to reuse

> The Garden Shadow had a saying — or possibly it was **Brother Quellin** — that the most dangerous person in a room isn't the one with the blade drawn.

**Why:** `zalthir_voice.md` marks this **IMPORTANT**: *"Use a different monk name every time this surfaces… The uncertainty about which monk taught what is the point."* Quellin is the literal name in the spec's illustration, and the previous draft correctly invented Brother Tharusk instead. This run reverted to quoting the example.

What makes it clearly a lapse rather than a preference: **four lines later the same scene gets it right** — `Brother Aldas taught it — or possibly Brother Harren` — two fresh names, correctly uncertain. The device is understood; one instance just copied the manual.

**Suggested rewrite:** Swap Quellin for a name not yet used — `or possibly it was Brother Vesh`.

### [4] Two monastery-uncertainty intrusions four lines apart

> The Garden Shadow had a saying — or possibly it was Brother Quellin… *(L33)*

> There was a monastery class on inventorying a room before your foot crosses its threshold. Brother Aldas taught it — or possibly Brother Harren. I remember the light through the shutters. Not the content. *(L37)*

**Why:** Both are canonical devices, and the L37 one is *excellent* — it converts the GM's out-of-character bow retcon into the character's defining flaw, without spending Zalthir's competence the way the previous draft did. But `zalthir_voice.md` says *"Use this sparingly"* and *"Keep it brief."* Back-to-back, the same "…or possibly Brother ___" cadence fires twice in five lines and the second one lands as a formula.

**Suggested rewrite:** Keep L37 verbatim — it is the better of the two and it does structural work. Convert L33's aphorism to the unattributed form: `I watched the wizard wait. Unhurried. Comfortable. The most dangerous person in a room isn't the one with the blade drawn. It's the one who has already decided they've won. A'lai Aivenmore had decided.`

### [5] "geometry" again, for the same referent as scene 02

> Grygum was working his **geometry**.

**Why:** Defensible in isolation — *geometry* is Zalthir's lexicon. But scene 02 already used it (`working the same geometry I was`) for the identical beat: Grygum computing firing angles. Two sections, two narrators, one word, one referent. `_genre.md` treats a figure shared across narrators as convergence.

**Suggested rewrite:** Since scene 02's use is the register-wrong one, fix that one and keep this. If you'd rather vary both: `Grygum was working the angles out loud.`

### [6] Em-dash — 6 narration-level, moderate

- L11 `For once a name was honest — shelves climbing into lamplight` → colon
- L87 `The wizard hadn't noticed us — he'd heard feet on the stairs` → semicolon or period

**Leave:** L33 and L37 (the source-uncertainty pairs — the voice file's own punctuation), and L91 once de-duplicated.

## Held correctly (no action)

- **The accounting register is gone.** The previous draft opened `"I counted levels before I counted people"` and stacked four tally beats; `_genre.md` says a Zalthir section that reads like accounting is wrong by definition. This draft has none. That was the heaviest flag in the whole document last run and it is fully resolved.
- `"They weren't looting. They were shopping."` — four words, and it reframes the entire room.
- `"The wizard had two. Nobody asked where Thorin had met one with three."` — dry, declarative, moves on. Textbook Zalthir humour.
- `"I had cheaper ways up. The enthusiasm was new, though. I marked it."` — Glabbagool love-language exactly per spec: mark the growth, approve silently, say nothing.
- `"Sound economy. Remove the cheap pieces first; isolate the expensive one. I said nothing, which was approval."`
- `"Rooms like this are never as empty as their visible portion, and the empty portion of this one was large."` — replaces the previous draft's `blind arcs` geometric abstraction with plain observation.
- `"Months of tunnel ceilings teach you that vertical rooms are honest about nothing except how far you can fall."` — Underdark-native, sensory, no metaphor reach.

## Verdict

Two mechanical defects — the duplicated clause and the fabricated *Whorlstone* — are the only things standing between this section and clean, and both are single-line hand-edits. The voice work itself improved more than any other section in the re-run: the accounting register that dominated the previous draft is entirely absent.
