# Voice Critique — Zalthir, scene 04: The Opening of Alkrist's Safe

**Narration:** `summaries/20260629/gm-assist-doc.md` (§ *Zalthir — The Opening of Alkrist's Safe*) — fixes belong in `narration/session_doc_scene_04_the_opening_of_alkrist_s_safe.scrubbed.md`
**Voice spec:** `voice/zalthir_voice.md`
**Per-char examples:** `examples/zalthir.md`

> **Note on this scene:** scenes 03 and 04 narrate the *same* event (the safe-opening in Bookwyrm's office) from Zalthir's POV twice. Two of the three flags below are duplications *of scene 03*, not independent problems — they are the cost of rendering one beat from one narrator twice.

## Flags

### [1] Voice-spec violation / cross-scene repetition — the duplicate half of the document's strongest flag

> The Garden Shadow had a saying — or possibly Brother Quellin did, I don't remember which — that the most dangerous person in a room isn't the one with the blade drawn. It's the one who has already decided they've won.

**Why:** This is the near-verbatim twin of scene 03 (`gm-assist-doc.md:218`) — same aphorism, same "Garden Shadow / Brother Quellin" attribution. The spec forbids exactly this: *"Use a different monk name every time this surfaces… The uncertainty about which monk taught what is the point"* (`zalthir_voice.md:64`). Firing the identical canonical example (`zalthir_voice.md:62`) twice in one document converts a signature device into a repeated catchphrase and drains the "he doesn't remember who said it" texture the second time — the reader *does* remember, because they just read it.
**Suggested rewrite:** Scene 03 earns the aphorism (it introduces the Bookwyrm read). **Cut it here** and let this scene's own, better line do the work — the room's collective certainty is already rendered cleanly by *"The Avowed had all decided they'd won"* two clauses later. If the beat feels bare without a saying, re-key to a *different* aphorism and a *different* uncertain source per the spec's latitude (e.g. *"Brother Heslin used to say — or maybe it was the quiet one with the ink-stained hands — that a locked box only tells you what a man wanted found. This one told the truth by having nothing in it."*).

### [2] Structural overlap with scene 03 — Glabbagool flying-skill beat

> Glabbagool was pleased with himself. *I like the flying skill,* he offered. *That was a good skill.*

**Why:** scene 03 already renders this exact beat — *"Under the skin of my arm, Glabbagool liked the flying skill. He thought it was a good skill."* (`gm-assist-doc.md:276`). Both the potion-grift and Glabbagool's reaction are told twice across the two Zalthir POVs. More structural than a voice defect (the line is in-voice both times — the marked-growth-said-silently pattern from `zalthir_voice.md:44-46`), but flagged so the duplication is visible: the reader meets the same ooze-approves-of-flying joke twice.
**Suggested rewrite:** No line-level rewrite — resolve at the structural level. If both scenes ship, let only one carry the flying-skill approval; here, since scene 03 already lands it, trim this to the grift alone and drop the ooze's verdict.

### [3] Tell-then-name (minor)

> Clean. Not lucky — clean. The kind of move where the hand knows before the mind does and there is nothing to correct after.

**Why:** Borderline, noted for completeness. The clipped "Clean. Not lucky — clean." is dead-on Zalthir (declarative full-stops, `zalthir_voice.md:104`), but the trailing gloss "the hand knows before the mind does" edges toward explaining the discipline rather than just marking it — and the spec is firm that *"the reasoning is the action; the action is already done"* (`zalthir_voice.md:163`).
**Suggested rewrite:** Optional trim to the part that already works: "Clean. Not lucky — clean. Nothing to correct after." (Keeps the cadence, drops the explanation.)

## Verdict

In-voice at the sentence level, but this scene is where the document's repetition problem concentrates — the aphorism and the Glabbagool beat both duplicate scene 03. The one decisive fix is to surrender the monk aphorism here (03 keeps it); the flying-skill duplication is a structural call about whether two Zalthir POVs of one event should both ship. (Em-dashes handled systemically — see `voice_critique_summary.md`.)
