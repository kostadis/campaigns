# Consistency Report — Stage 2, Session 2026-08-25 Scene Extractions (Chapter 50)

**Documents checked:** all eight files in `scene_extractions_new/` — the layer holding the **verbatim quotes the narrator reads literally**. This is the load-bearing stage: fixes applied only at the recap layer are silently undone the next time the narrator runs.

**Adjudicated in:** the Chapter 50 Rulings artifact, saved 2026-08-28 14:26 UTC. **All seven cards approved.**

Every finding sat inside a quote block, so nothing was auto-applied at this stage.

---

## Findings

### 1. `Pero` — a third spelling of the Bellows garble, and it reads as a person
- **Location:** `05_lim_s_secret_supplier.md:84`
- **Quote:** Brewbarry, confronting Lim about the ninth crate — *"Pero was telling me about it."*
- **Evidence:** the second transcription renders the same cue *"Bella was telling me about it"*, and `vtt_transcription_corrections.md:123` already maps `Bella -> Bellows` from the 2026-08-26 round. The referent was settled by an existing rule; only this third spelling escaped it.
- **Why it matters:** "Pero" is a plausible Neverwinter name with no entity behind it — the **Bucherton pattern**, a garble that synthesis promotes into a person, sitting in the scene that sets up the stakeout.
- **Applied:** corrected to Bellows with an editorial note; `Pero` added to the Bellows glossary row.

### 2. `Valfinier` x2 — survived because the glossary rule was dead
- **Locations:** `01:117`, `08:669`
- **Evidence:** the second transcription reads Valphine at both points. They survived because the Valphine row at `vtt_transcription_corrections.md:15` listed the wrong-form as **"Or Valfinier"** — with a leading "Or" — so a bare `Valfinier` could never match.
- **Applied:** both quotes corrected; the glossary row repaired (the "Or" stripped) earlier in the run; both cues patched in the cleaned VTT.

### 3. `Shapal says` is not a name — it is speech framing the ASR mangled
- **Location:** `04_dining_with_lim_and_interrogating_bellows.md:47`
- **Evidence:** Zoom (l.497) has *"wait, Shapal says, you are the great Vukradin?"*; the second transcription has **no such word at all**, rendering the cue as bare *"You are the great Vukradin?"*, and elsewhere renders the same construction cleanly as *"She pauses and goes…"* Lim is the speaker; there is no fourth person at that table.
- **Pattern:** the Ch65 **"Alyss"** case — a name-shaped token with no referent, present in one transcription only, one step from being resolved to the nearest real NPC.
- **Applied:** rendered as framing — *"wait, she pauses, says, you are the great Vukradin?"*

### 4. `Bourd` x2 — the establishment, and a ruling that had been left half-finished
- **Locations:** `01:282`, `03:53`
- **Not a fresh question.** `vtt_transcription_corrections.md:340`, GM-ruled 2026-08-26, had already established that `Bourd -> Brewbarry` fired 3x on this tape and **2 of the 3 were the establishment**: *"we go to the Bourd bear"* and *"you arrive at the Bourd laid bare"*. The rule was correctly narrowed and the one true Brewbarry hit (l.693) was fixed — but the two establishment hits were left as raw `Bourd` rather than corrected to `Board`, so the residue outlived the ruling.
- **Applied:** both corrected to **The Board Laid Bare** (canonical, `entity_registry.yaml:1733`), finishing the job the 2026-08-26 ruling started.

### 5. `Oral and Vance` — and the standing instruction not to silently normalise it
- **Location:** `01:69`
- **The tension:** `entity_registry.yaml` carries an explicit instruction that *"Aurum Bee Vance" is NOT AN ALIAS — a one-time in-fiction mishearing, blessed as a comic beat, and a future consistency or spell pass must not silently normalize it to Aurelan.*
- **The distinction the GM drew:** that exemption covers the **party mishearing his name**. This line is the GM's own narration of Aurelan arriving — a plain ASR garble with no joke attached. Carded rather than auto-fixed precisely because the instruction says *must not silently*.
- **Applied:** corrected to **Aurelan Vance**. Note this was already the settled pattern: `Oral B. Vance, Orlin Vance -> Aurelan Vance` has been a glossary row since 2026-08-13. The registry's "not aliases" statement governs *entity identity*, not *text repair* — two different mechanisms.

### 6. `Mark Gordon on stage` — most likely "marching on"
- **Location:** `08_return_to_the_common_cord.md:186`
- **Evidence:** Valphine, l.5009. The second transcription produces no name either, but a different non-name (*"we are going on stage"*). Two independent passes, two readings, no referent in canon.
- **Confidence:** explicitly lower than the other five, and flagged as such on the card.
- **Applied:** *"Marching on stage. Who's stopping us?"* with an editorial note.

### 7. Four real-world names inside verbatim quote blocks
- **Locations:** `Stephane` (`03:123`, `04:353`), `Gary` (`06:182`), `Claude` (`03:68`)
- **Ruling:** left in the extractions as the raw record, **flagged for `/scrub`** before narration.
- **Explicitly not touched:** the table's in-fiction comedy — Airbnb, Kickstarter, Hollywood, Yoko, Bud Light, Raspberry Pi, Discord, "Organic Fair Trade", and the Board/Broad/Bored running gag (verified on tape at l.408, l.1585, l.1589, l.2573). That vocabulary is the table's and the skill says not to strip it.

---

## Verified clean — checked, no action (recorded so future passes don't re-flag)

- **`AVTA`** in the GM's read-aloud recap is *naïveté*. The tape self-corrects: Gary read the same line off the same document and the ASR got his right (*"It is naivete"*). Never reached any artifact; glossary candidate only.
- The Board/Broad/Bored gag is deliberate table comedy, not a garble.

---

## Summary for the GM

Seven findings, all approved, all applied and verified by full-phrase grep. Two were **prior rulings that had been left half-applied** (4 and 5) rather than new questions — which is the argument for `.sources.yaml` existing at all. The stage-2 layer justified itself: four of the seven (1, 3, 5, 6) existed *only* here, because lifting a quote verbatim from the tape is the one thing stages 0 and 1 never do.
