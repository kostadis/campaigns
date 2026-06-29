# Continuity Report — Chapter 57: "The Colloquium was well received"

---

## 1. NPCs Section — Irony entry: action misattributed to Alkrist

**Location:** NPCs / Irony

**Issue:** The Irony NPC entry reads: *"Alkrist arrived carrying a basin of water to lay the table for supper and washed his hands 'in case I got any midnight tears about them.'"* — it says **Alkrist** arrived with the basin, but Alkrist was already at the Dead Winter tree burning the label. Irony is the one who arrived and interrupted him.

**Evidence:** The Scenes section (Interrogation of Alkrist) correctly states: *"'Irony' arrived carrying a basin of water to lay the table for supper."* The NPC entry inverts the subject.

**Suggested fix:** Change to: *"A staff member who nearly caught Alkrist tampering with the gift near the Dead Winter tree. Irony arrived carrying a basin of water to lay the supper table; Alkrist washed his hands to conceal any contact with the poison ('in case I got any midnight tears about them')."*

---

## 2. NPCs Section — Jezebel: wrong audience for the mage hand

**Location:** NPCs / Jezebel

**Issue:** The entry reads *"used a mage hand to open the door for the party."* Only Daz went alone to Sylvira's quarters; the party did not accompany him.

**Evidence:** Summary: *"Daz went by himself to the quarters of Sylvira."* Scenes (Interview with Sylvira): *"Daz enters Sylvira's quarters."* The Splitting the Leads scene confirms the split: Grygum to Janussi's chambers, Daz to Sylvira, others to Alkrist prep.

**Suggested fix:** Change to *"used a mage hand to open the door for Daz."*

---

## 3. Spells Section — Polymorph: Grygum cannot cast this spell

**Location:** Spells / Polymorph

**Issue:** The entry states *"Grygum noted he can cast Polymorph himself and considered using it to interview someone in disguise."* Polymorph (4th-level Transmutation) is not on the Cleric spell list and is not in the Life Domain's bonus spells. No context document lists it among Grygum's spells.

**Evidence:** world_state.md lists Grygum's notable spells as *"Revivify, Mending, acid breath, Spirit Guardians."* party.md: *"Cleric 8 (Life Domain)."* Polymorph appears nowhere.

**Suggested fix:** Verify whether Grygum has a scroll of Polymorph, a magic item, or whether this was a misclaim at the table. If neither, remove the claim and note a different character (Daz as Wizard 8 / Evoker — Polymorph is on the Wizard list) or remove it entirely.

---

## 4. Summary & Scenes (Interview with Sylvira) — Bookwyrm vs. Janussi as primary blocker of Kalan's methodology

**Location:** Summary (paragraph 3) and Scenes / Interview with Sylvira

**Issue:** The recap twice asserts, via Sylvira, that *"it had been Bookwyrm, not Janussi, who had pushed hardest against Kalan Strongbranch's investigative proposals."* The existing campaign documents say the opposite: Janussi was the one who suppressed it, and Bookwyrm acted at his instigation.

**Evidence:** campaign_state.md (NPCs / Kalan Strongbranch): *"which Janussi moved to suppress; Bookwyrm removed him from the murder investigation at Janussi's instigation."* world_state.md (suspects / Kalan): *"removed from the case by Bookwyrm."* campaign_state active quest #1: *"Kalan believes she's protecting the killer or was manipulated into firing him"* — framing Bookwyrm as a secondary actor, not the primary one.

**Suggested fix:** If Sylvira's claim is new in-session information that reframes prior facts, flag it explicitly as Sylvira's potentially unreliable testimony. If it was a GM slip, correct to: Janussi moved to suppress the methodology; Bookwyrm executed that decision. Update the Sylvira NPC entry accordingly and add a note that her characterization diverges from other evidence.

---

## 5. Memorable Moments & Scenes (Interrogation of Alkrist) — Book location inconsistency

**Location:** Memorable Moments (bolded entry on the bookshelf) and Scenes / The Interrogation of Alkrist

**Issue:** The Memorable Moments section describes Alkrist's hand drifting *toward the bookshelf* during the interrogation — implying the book is still on the shelf. But the Scenes section states *"Zalthir dramatically shows the section of the book. He had discovered it earlier in his searches"* — implying Zalthir had already retrieved it. A book Zalthir removed from the room in a prior search cannot be on the shelf during the interrogation.

**Evidence:** The two passages directly contradict each other on where the book physically is at the time of the interrogation. No context document resolves this.

**Suggested fix:** Clarify in both sections. Most consistent reading: Zalthir located the book during an earlier search of Alkrist's chambers but left it in place, then retrieved and opened it dramatically during the interrogation when Alkrist's body language confirmed its significance. Update Memorable Moments to reflect *"Zalthir, who had already found it, dramatically retrieves and opens it"* rather than leaving the impression it simply fell open by itself on the shelf.

---

## 6. Items Section — The Poisoned Book / The Golden Ass: evidence status contradiction

**Location:** Items / The Poisoned Book and Summary (opening paragraph)

**Issue:** The recap describes Daral "reclaiming" the poisoned book in this session. But two context documents establish the book as already disposed of: campaign_state.md item #46 says *"Murder weapon book secured into evidence,"* and world_state.md (Stolen/missing) lists *"the annotated book The Golden Ass"* as unrecovered. The book cannot be simultaneously secured into evidence, listed as stolen/missing, and available for Daral to reclaim in the same arc.

**Evidence:** campaign_state.md Completed Encounters #46; world_state.md Section 5 Stolen/missing list.

**Suggested fix:** Reconcile the chain of custody before next session. Determine whether: (a) Daral reclaimed it before it was secured into evidence (and this recap covers that earlier moment), (b) the campaign_state "secured into evidence" entry is premature, or (c) the world_state "stolen/missing" entry is stale. Add a note to Items clarifying when the book passed to evidence and whether it is still recoverable.

---

## 7. Scenes (Interrogation of Alkrist) — Ambiguous hand-washing attribution

**Location:** Scenes / The Interrogation of Alkrist

**Issue:** The Scenes section states *"Irony arrived carrying a basin of water to lay the table for supper — Irony washed his hands 'in case I got any midnight tears about them.'"* The quoted words *"in case I got any midnight tears about them"* are first-person Alkrist speech, strongly implying it was **Alkrist** who washed his hands in Irony's basin, not Irony washing Irony's own hands.

**Evidence:** Internal: the first-person voice is Alkrist's throughout the confession passage. Logically: Alkrist burning the label would be the one with potential poison contact, not Irony who arrived to set a table.

**Suggested fix:** Revise to: *"Irony arrived carrying a basin of water to lay the supper table — Alkrist quickly washed his hands in it 'in case I got any midnight tears about them,' and Irony apparently noticed nothing amiss."*

---

## 8. Summary & Title — Inconsistent terminology for Grygum's academic event

**Location:** Session title, Summary (opening sentence), and campaign_state.md Ch. 56 reference

**Issue:** The session is titled *"The Colloquium was well received"*; the Summary calls it *"his wildly successful public lecture"*; campaign_state.md (Ch. 56 reference for Kalan's key handoff) calls it *"the disputation."* Three different terms for what appears to be the same event.

**Evidence:** campaign_state.md Key resources: *"Kalan's — held by Daz, passed from Grygum before he left for the disputation, Ch. 56."*

**Suggested fix:** Standardize on one term (the title uses "Colloquium"; academic context suggests this is the most formal and probably correct). Update the Summary's "public lecture" to "colloquium" for consistency, and verify whether the Ch. 56 campaign_state reference should also be updated to "colloquium."

---

## 9. NPCs Section — Kalan Strongbranch: "Gate Warden" title vs. "recently fired" status

**Location:** Summary (paragraph 3) and NPCs / Kalan Strongbranch

**Issue:** The Summary calls Kalan *"the recently fired Kalan Strongbranch,"* but the NPCs section still identifies his title as *"Gate Warden at Candlekeep."* If he was fired from his Gate Warden position, the title is no longer accurate. If he was only removed from the murder investigation, "recently fired" overstates the situation.

**Evidence:** campaign_state.md active quest #1: *"Kalan believes she's protecting the killer or was manipulated into firing him"* — implies he was fired from a position, not merely reassigned. world_state.md: *"removed from the case by Bookwyrm."* These describe two separate actions (job termination and case removal) that the recap conflates.

**Suggested fix:** Clarify whether Kalan retains the Gate Warden title or was fully dismissed. Update the NPC entry to reflect his actual current status (e.g., *"Former Gate Warden, dismissed at Bookwyrm's direction; removed from the murder investigation"*).

---

## 10. Summary (Concluding the Investigation) — A'lai's race: undeclared in most of recap, confirmed only once

**Location:** Summary, Scenes (multiple), NPCs / A'lai; cross-referenced with memory note

**Issue:** The recap refers to A'lai throughout without naming his race, then identifies him as *"a drow"* only once, in the final scene: *"particularly from A'lai, who as a drow might have knowledge Daz needs."* The memory note explicitly records a table override: *"A'lai Aivenmore is a drow — OOTA Candlekeep arc table call; overrides module-human / stale 'dragonborn' prep."* The NPCs section never states his race.

**Evidence:** Auto-memory `alai-aivenmore-is-drow.md`: *"A'lai Aivenmore is a drow … overrides module-human / stale 'dragonborn' prep."*

**Suggested fix:** Add A'lai's race (drow) explicitly to his NPCs section entry so future session prep and NPC dossiers don't revert to the stale module-human default. A single sentence in the NPCs entry is sufficient: *"A drow with connections to the Underdark…"*