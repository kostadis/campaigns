# Consistency Report — Stage 1, Session 2026-08-25 Recap (Chapter 50)

**Document checked:** `session-summary.md` — the `enhance` output, built from the stage-0 export + the VTT.

**Run order:** AFTER stage 0 was ruled and applied, with the corrected export as context. That is what let this pass distinguish *inherited* errors from ones the enhancement layer invented.

---

## Major Issues

### 1. An enchantment that was never cast — **enhancement-layer fabrication**
- **Location:** scene log, second-performance bullet
- **Issue:** The recap had Vukradin casting a spell to boost the second performance. He offered; nothing was cast.
- **Evidence:** the GM checks on tape at l.1452 — *"You're not doing a special magical performance tonight, right?"* The performance then resolves on dice alone: raw rolls of 14 and 7, lifted to 19 and 13.
- **GM ruling (verbatim):** *"It was just bardic inspiration and bless"*
- **Fix applied:** bullet rewritten to state that no enchantment is ever cast, that the GM checked, and that the roll was boosted only by Bardic Inspiration and Bless.

### 2. The revenue share was reported as floated, not taken
- **Location:** L24
- **Issue:** The recap left the 50% share as an unaccepted proposal. It closed on screen.
- **GM ruling (verbatim):** *"Petra took the revenue share for the concert"*
- **Fix applied:** *"A revenue-share gambit floated by Brewbarry — fifty percent of the house on the night of the concert, gross, the band insisted, never net — Petra took, shaking on it before anyone could change their mind."*
- **Why it matters:** this is the **planned-vs-resolved** failure mode. Next session's opening state depends on whether Petra is contractually on the hook.

### 3. A prep contradiction that does not exist — **the audit was wrong** ⚠️
- **Location:** carded as s1-02
- **What the card claimed:** that prep contradicted itself, using "seven weeks" (49 days) in some places and "seven tendays" (70 days) in others.
- **GM ruling (verbatim):** *"In Faerun a week is ten days"*
- **Resolution:** there is no contradiction. A week **is** a tenday; both phrasings denote the same seventy days and the prep was self-consistent throughout. The card should never have been written.
- **Consequence:** acting on the false premise, six lowercase "seven weeks" in `notes/session_prep/20260825_bluelake_and_the_price_that_did_not_change.md` (l.33, 48, 62, 183, 210, 612) were rewritten to "seven tendays" — same meaning, but it flattened the GM's own prose. Two capitalised instances (l.181, l.216) were missed by the lowercase match and survive in the original wording. **Reversible from `scratchpad/prep20260825.bak`.**
- **Note:** the separate s0-01 fix ("ten days ago" -> "seven tendays ago") was correct and independent of this error.

---

## Minor Issues

### 4. Quote normalisation only — no substantive change (**rejected as a finding**)
- `"Lord Nevermember is our ally against Margaster"` — the card proposed a substantive rewrite; the GM rejected it. Only the proper-noun spelling was normalised, twice, to `"Lord Neverember is our ally against Margaster"`.

### 5. A negation dropped from a quoted line
- *"This is Lathander's Death... really our style"* inverts the band's actual verdict.
- **Fix applied:** `"This is Lathander's Death... [not] really our style,"` with the bracket marking the reconstruction.

### 6. Voice caption did not match the beat it captioned
- **Fix applied:** replaced with *"I remember it was the horse that was outside of the service where that charming cleric gave a speech"*

---

## Auto-applied

38 proper-noun sites: `Common Cord`->**Common Chord** x17, `Morning Lord`->**Morninglord** x4, `Aligander`->**Alagondar** x4, `Zelene`->**Zeleen** x4, `Nevermember`->**Neverember** x9 (prose only). The carded quote was protected by token-swap during the batch so the substitution could not reach inside it.

---

## Summary for the GM

Six findings: two enhancement-layer fabrications fixed, one planned-vs-resolved corrected, one rejected, two minor quote repairs. **Finding 3 is the one worth remembering — the audit invented a contradiction out of a Faerûnian calendar assumption, and a prep file got edited on that false premise before the GM caught it.** That is the failure mode the human gate exists for, working as intended.
