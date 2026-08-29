# Consistency Report — Stage 0, Session 2026-08-25 GMAssist Export (Chapter 50, "The Broads of the Common Chord and the Board Laid Bare")

**Document checked:** `session_2026_08_25_chapter_50_the_broads_of_the_common_chord_and_the_board_laid.md` — the GMAssistant export, and the *input* to the `enhance` pass.

**Compared against:** session prep (`20260825_bluelake_and_the_price_that_did_not_change.md`, `20260901_the_ninth_crate.md`, `20260818_neverwinter_consolidated_live_state.md`), `docs/entity_registry.yaml`, `notes/vtt_transcription_corrections.md`, the raw VTT (`GMT20260826-035950_Recording.transcript.vtt`, speaker-label authority), the cleaned VTT, and the independent second transcription (`*_transcript.txt`).

---

## Major Issues

### 1. The clock: "ten days ago" for a payment stoppage that prep fixes at seven tendays — **the read-aloud case**
- **Location:** prose L6, scene log L36, NPC entry L139
- **Issue:** The export says Bimble's Commission payments "abruptly stopped **ten days ago**." Prep is explicit and the GM read the line aloud from it.
- **Evidence:** `20260825_bluelake_and_the_price_that_did_not_change.md:70` — *"The payments stop seven tendays ago — on the day, not the tenday."* Zoom's ASR produced `"the payments stop 7-10 days ago, on the day, not the 10-day"`; the independent second transcription produced `"The payments stop seven, ten days ago"` — decisive. All three pipeline stages then resolved the garble the same wrong way.
- **Why it matters:** the seven-tenday clock is load-bearing for the next session — `20260901_the_ninth_crate.md` uses it nine times, and it is the same clock as the Manifold going dark. A ten-day reading collapses the whole "somebody has been feeding him for seventy days" structure.
- **GM ruling:** canon is **seven tendays (70 days)**. Applied at all three sites.
- **Pattern:** this is the Ch65 read-aloud case exactly. **When the GM reads a written passage aloud, diff the quote against the source document, not against your ear.**

### 2. The Petra settlement is reported as an intimidation into a 500 gp fee. She refused it, twice.
- **Location:** prose (Common Chord section), scene log L101, NPC entry, voice caption
- **Issue:** The export read *"Brewbarry intimidates Petra into agreeing to a 500 gold piece fee for a one-night exclusive performance to settle the debt of using Vukradin's likeness."* No such agreement happened.
- **Evidence:** raw VTT l.1296 and l.1312 — Petra refuses outright, *"I can't afford 500 gold pieces for a one-night performance,"* and never accepts. What actually closed: 500 gp named as the **value** of the infringement, squared by one exclusive performance in two nights, plus a **perpetual licence on Vukradin's image and likeness**, and **no coin changed hands**. The 25 gp for signing the plaque was real and paid on the spot — a separate transaction.
- **Fix applied:** prose rewritten; the single scene-log bullet replaced with three (the twice-refusal, the revenue share, the no-coin settlement); the voice caption changed from *"demands 500 gold pieces and licensing fees"* to *"values the infringement at 500 gold pieces and takes a perpetual likeness licence in settlement."*

### 3. The courier rotation flattened into a single group
- **Location:** prose L14, scene log L63
- **Issue:** *"brought by a rotating group of six or seven men who were never quite the same from night to night"* — which reads as one crew of six or seven. Bellows described the opposite: a **two-man delivery** drawn from a larger pool.
- **Fix applied:** *"brought by two men, sometimes three, never the same two — six or seven couriers oscillating through the rotation over the last thirty days."*
- **Note:** the stage-1 file's *scene log* and *NPC dossier* already had this right; only its prose paragraph was flattened. Fixed there during the step-6 sweep.

---

## Minor Issues — auto-applied

Registry- and glossary-settled proper nouns, none inside a quoted span:

| Wrong | Right | Count | Authority |
|---|---|---|---|
| Common Cord | **Common Chord** | 14 | `entity_registry.yaml:2260` |
| Nevermember | **Neverember** | 4 | `entity_registry.yaml:312` |
| Aligander | **Alagondar** | 3 | `entity_registry.yaml:1823` |
| Morning Lord | **Morninglord** | 4 | `entity_registry.yaml:2275` |
| Zelene | **Zeleen** | 2 | `entity_registry.yaml:192` (Zeleen Varnaster) |

`Zelene` was missed on the first pass and caught by the step-6 propagation sweep. It is the **upward-propagation** case: it had been fixed at stage 1 only, leaving the error in the pipeline's own input, where the next `enhance` run would have re-injected it.

---

## Cross-section inconsistency (recorded, not an error in either half)

The prose omits Lim's denial that her supplier is the Kraken Society, while the **scene log carries it** (L70, as paraphrase). Same document, two levels of fidelity. This is a recurring shape in this file: on the courier rotation and on the Petra deal the *bullets* were more faithful than the *prose*.

---

## Summary for the GM

Three substantive findings, all ruled and applied; five spelling classes auto-applied across 27 sites. The headline is finding 1 — a prep-canonical number the ASR broke, which every downstream stage then inherited. The stage-0 file was edited in place (it had already been modified by this run, so it is not a preserved original).
