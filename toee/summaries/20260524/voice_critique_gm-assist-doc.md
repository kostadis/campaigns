# Voice Critique — gm-assist-doc.md (Chapter 27 Dungeon Boss)

**Narration:** `summaries/20260524/gm-assist-doc.md` (single assembled file, six narrator blocks)
**Voice specs:** `voice/calmer_voice.md`, `voice/zephyr_voice.md`, `voice/zinnia_voice.md`, `voice/sequoia_voice.md` (all present)
**Per-char examples:** `examples/` exists but is organized by theme, not by character — no per-character routing available; critique grounded in voice specs.

> Review-only artifact. Nothing here is auto-applied. The source is the *gm-assist* input doc, not a `session_doc.py` `.scrubbed.md`, so there is no `assemble.py` consumer to worry about — edit `gm-assist-doc.md` directly if you act on these.

---

## Top-line

High fidelity. The signature beats land verbatim from the specs across all four narrators. The flags below are concentrated, not systemic — one genuine register hit (Zinnia), two spec-tension lines (Sequoia flourish, Zephyr arithmetic), and a cross-narrator metaphor tic. Spot-edit; do not re-narrate.

**Strongest recurring theme:** a single "weak-point" metaphor — *seam / where it gives* — is shared across three narrators (Calmer, Sequoia, Zephyr). It's the writer's image, not any one character's, and it's most wrong on Sequoia, whose spec explicitly forbids flourish.

---

## Mechanical scans

**Em-dashes:** 80 in the file. Unlike `session_doc.py` output, this gm-assist doc uses the em-dash as a deliberate, uniform cadence device, and a large share are inside `*…*` interior monologue or `"…"` dialogue (do-not-touch). I am **not** enumerating all 80. The voice-relevant observation: the dash-driven rhythm is identical across all six blocks, which slightly flattens the line between narrators — Sequoia (staccato, "no flourish") and Zinnia (terse reads) should read *choppier* than Calmer/Zephyr, and the shared dash cadence smooths that difference away. Worth watching, not a per-line fix.

**Register-wrong vocabulary scan:** three prose hits (one inside dialogue, excluded). The live one is Zinnia line 313 — see flag [6]. Zephyr's "held my shape" (141) and Zinnia's "I filed that" (323) tripped the scan but are defensible: "held my shape" is a physical imprint (he's taken the throne — strong image), and "filed" is in-register spy vocabulary for Zinnia. Not flagged.

---

## Flags

### [1] Convergence with house style — the "seam / gives way" metaphor (cross-narrator)

> *Calmer (25):* "he watched me drift through it like he was waiting to see which seam would give"
> *Sequoia (157):* "The whining was the seam."
> *Zephyr (81):* "She has a way of finding the part of a thing that doesn't hold — the place where it was already going to give."

**Why:** The same weak-point image — a *seam*, the place that *gives* — is handed to three different first-person narrators. That makes it the GM's metaphor, not a character's. It reads as a fingerprint across blocks rather than three distinct minds.
**Suggested fix:** Keep it on at most one narrator. It's most defensible on Zephyr (reading a deal's give is his trade). Strip it from Sequoia entirely (flag [4]) and reword Calmer's so he watches for *belief / drift*, which is what Zephyr is actually auditing him for per spec: e.g. "he watched me build it the way he watches me now — waiting to see how much of it I still believed."

---

### [2] Voice spec conflict — Sequoia poeticizes

> "Calmer wasn't a worrier. Calmer was a man holding a name in his mouth he wasn't allowed to say, inside a temple built to spite it. The whining was the seam." (157)

**Why:** Sequoia's spec is explicit: "no metaphors, no flourish… He doesn't poeticize." "a name in his mouth… inside a temple built to spite it" plus "the seam" is exactly the lyrical register the spec rules out — this is Calmer's or Zinnia's interiority wearing Sequoia's heading.
**Suggested rewrite:** "Calmer wasn't a worrier. He just couldn't say his own god's name in here, so it came out sideways, as complaint. But Dren didn't need that, and there was no need for him to know." (`There is no need for him to know` is verbatim spec; staccato; drops the flourish and the shared "seam.")

---

### [3] Register tic / spec-tension — Zephyr's "cold arithmetic"

> "And I had the cold arithmetic, which was the only thing in this temple that ever told me the truth: four prophets, all chaotic, all hungry for the same chair…" (51)

**Why:** Zephyr's narration spec draws a hard line: "Reading people, not counting them… He doesn't say 'the numbers favor this.'" Calling his own read "cold arithmetic" frames the thinking as math, which is the one register the spec carves out of his interior voice. (Sequoia is *allowed* to call Zephyr the math guy from the outside — flag note below — but Zephyr shouldn't narrate himself that way.) The *content* that follows is pure Zephyr; only the label is off.
**Suggested rewrite:** lean on the appetite framing the line already reaches for: "And I had the only thing in this temple that ever told me the truth: four starving prophets, all chaotic, all hungry for the same chair, and the simplest way to end a war between starving men is to let them eat each other and stab whoever's still chewing."

*Note (not a flag):* Sequoia's "the grim arithmetic of which corpse to loot first… He's better at the math" (173) is fine — that's Sequoia characterizing Zephyr from the outside, which is consistent. Only Zephyr's self-narration (51) is the issue.

---

### [4] Register-wrong vocabulary — Zinnia computes geometry instead of perceiving

> "The arrangement of the room snapped into focus, the angle of their approach, the confidence in how they had spaced themselves, and I knew." (313)

**Why:** The clearest single hit. "arrangement," "angle," "spaced themselves," "snapped into focus" is analytical/geometric vocabulary — and Zinnia's spec is built against exactly this: "This is not analysis… he's arriving at them… things land in him as finished readings, not as inputs to a process." He doesn't resolve angles; he *knows*.
**Suggested rewrite:** "Not the bugbears in front of us — the others. It landed all at once, the way a wrong room lands: they stood like men who had stood here before, easy, owning the floor — and I knew. The Greater Temple had not kept its forces below." (`landed`, `I knew` — perception verbs from the spec; drops the geometry.)

---

### [5] Lush atmospheric register vs. operational eye — Zinnia (low confidence)

> "The buttresses and arches threw a tracery of dimness across everything." … "Like standing at the bottom of the sea." (205)

**Why:** Zinnia reads rooms for *operational meaning* — threat, deference, what's wrong — not for beauty. "a tracery of dimness" and "like standing at the bottom of the sea" are aesthetic fantasy description; his eye is supposed to reach the inventory ("Four watchers in the corners. A god in the alcove. Treasure in the font." — 209, which is perfect) faster. Low confidence because this is largely the module's water-temple room and some scene-setting is load-bearing.
**Suggested fix:** trim the most decorative clause ("a tracery of dimness across everything") and let the operational read at 207–209 carry the room. No full rewrite needed.

---

### [6] Redundancy — Zephyr's interior thought restates the prose

> "…fewer chances for a war zone to introduce me to something it had been saving. *Fewer rooms. Fewer chances for whatever this war had saved for us to introduce itself.*" (237)

**Why:** The italic interior line repeats the immediately-preceding narration almost word for word. It reads as a doubled take rather than two beats. The prose version is the stronger of the two.
**Suggested fix:** delete the italic restatement; end the paragraph on "…something it had been saving. I put my ear to the brown marble and listened."

---

## Notes (not voice flags — route elsewhere)

- **Heading typo:** block 3 is headed `## sequioa — The Captain's Report` (should be `sequoia`). Cosmetic, but if any tooling keys off the narrator slug it will miss.
- **Possible VTT transcription error:** "those pompous passes known as the Obsidian Edge" (249) — "passes" is likely "asses." It's inside verbatim dialogue, so out of scope for voice-critic; raise it on a `/session-summary-consistency` pass instead.

---

## Verdict

The shared *seam / gives-way* metaphor across three narrators (flag [1]) and Zinnia's geometric read at 313 (flag [4]) are the two worth fixing; both are clean spot-edits. Everything else is low-confidence or cosmetic. Voice fidelity is high enough that re-narration would cost more than it returns — hand-edit the four lines and ship it.
