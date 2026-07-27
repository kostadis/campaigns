# Voice Critique — Daz, scene 04: The Death of Bookwyrm

**Narration:** summaries/20260720/narration/session_doc_scene_04_the_death_of_bookwyrm.md
**Voice spec:** voice/daz_voice.md
**Per-char examples:** examples/daz.md

## Flags

### [1] Mechanical scan A — em-dash overuse (heaviest of the six scenes)

Eleven narration-level lines, thirteen instances (one match, line 19, is inside an italic span — `*He is using the beast to—*` — and correctly excluded as a protected VTT trailing-off):

| Line | Text | Suggested |
|---|---|---|
| 9 | "...shouting it down the corridor — Bookwyrm is dead." | Colon: "...shouting it down the corridor: Bookwyrm is dead." |
| 15 | "...That was the answer that came back — torn, not cut." | Colon or period: "...came back: torn, not cut." |
| 17 | "...relaxed in the safety of her own tower — no Time Stop cast, no ward raised..." | Colon: "...her own tower: no Time Stop cast, no ward raised..." |
| 21 | "I reached for it — the way I always reach, ritually..." | Comma: "I reached for it, the way I always reach, ritually..." |
| 23 | "...it came clean — cleaner than clean, the whole architecture..." | Comma or period (see flag 3 re: "architecture" too): "...it came clean. Cleaner than clean — the whole..." or restructure entirely per flag 3. |
| 31 | "...pushed the helmed horrors through it — at *me*." | Comma: "...pushed the helmed horrors through it, at *me*." |
| 35 | "Janussi was surgical — magical, deliberate, a heart removed for a reason." | Colon: "Janussi was surgical: magical, deliberate, a heart removed for a reason." |
| 37 | "Abyssal spawn — she's a tiefling... happen — and she keeps him locked..." | Two dashes in one sentence; convert at least one. E.g. "Abyssal spawn. She's a tiefling, she was in the Abyss, bad things happen — and she keeps him locked..." |
| 41 | "...explained the defenses then — the shield that stops anyone teleporting..." | Colon: "...explained the defenses then: the shield that stops anyone teleporting..." |
| 43 | "...evaporated the instant it touched — a burning bush that refused to burn." | Colon: "...evaporated the instant it touched: a burning bush that refused to burn." |
| 45 | "Bookwyrm had one of those keys — she'd gone into...secured the key — and someone had torn..." | Two dashes; the first reads fine as a colon, the second could be a period: "Bookwyrm had one of those keys: she'd gone into Janussi's chamber, taken the heart, secured the key. Someone had torn her throat out to get it." |

**Why:** Same pattern as the other scenes — nearly every aside in this section reaches for an em-dash where a colon, comma, or period would carry the same beat without the repetition becoming visible as a tic.

### [2] Voice spec conflict — bookkeeping noun "account" repeats three times in one section

> "I noted the discrepancy immediately, because it was the whole **account** in one line."

> "I reached for it — the way I always reach, ritually, off the top of the **account**."

> "...the **account** balanced somewhere in the back of my head, off a thread I hadn't known I was holding."

...plus a fourth, different-noun instance: "I had her sorted into the **column** marked *loose ends I intended to collect from later*."

**Why:** The genre spec gives Daz a narrow exception — up to two bookkeeping-vocabulary uses per section, but only with *different* nouns ("audit ≠ ledger ≠ drawer"), and explicitly warns "never let *ledger*/*column* dominate a scene or repeat within it." This section uses four bookkeeping references total, and the same noun — "account" — three separate times. That's the exact failure mode the spec names, not the calibrated two-with-variety it allows.
**Suggested rewrite:** Keep "column" (line 9) and one "account" use; rotate the other two to different vocabulary already in the spec's list, e.g. line 21: "I reached for it, the way I always reach, off the top of the ledger" and line 35: "the whole thing balanced somewhere in the back of my head, off a thread I hadn't known I was holding" (drop the noun entirely on the third hit).

### [3] Register-wrong vocabulary — "architecture"

> "On the second pass, with his hand steadying the work, it came clean — cleaner than clean, the whole architecture snapping into place at once."

**Why:** Not on the literal scan-B word list, but the same family — analytical/structural vocabulary describing an arrangement, which the spec doesn't give Daz. Daz's register for "everything clicking into place" is bookkeeping (audit, tally, column), not engineering. "Architecture" reads as a generic intensifier for "it all made sense," not something this specific narrator would reach for.
**Suggested rewrite:** "...it came clean — cleaner than clean, every column balancing at once." (or fold into the fix for flag 2 above, since this is also a bookkeeping-noun slot.)

## Verdict

The scene nails Daz's driest lines almost verbatim ("Interesting," the firewall metaphor, "Go interview him. Or protect him. Or find out he's already dead.") — the voice is right in the dialogue and in most of the narration. The real issue is the bookkeeping vocabulary getting used enough times in one section that the calibrated rarity the spec is built on stops reading as rare. Worth a spot-edit pass on flags 2–3 before this feeds assembly; the em-dash list is mechanical cleanup, not a voice problem.
