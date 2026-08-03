## Continuity Report — Chapter 07: Deception

---

### 1. PC Name Error — "Zenvon Forepot"
**Location:** Summary (multiple instances); Scenes → "Battle in the Tresendar Crypts"
**Issue:** The character is called "Zenvon Forepot" in every instance where the surname appears.
**Evidence:** `world_state.md` header note: *"Zenvon **Foreput** (Ch. 5/7 summaries say 'Forepot')"*; `party.md`, `campaign_state.md`, and `vtt_transcription_corrections.md` all use **Foreput**.
**Suggested fix:** Replace every instance of "Forepot" with "Foreput."

---

### 2. Chase Attribution Error — "Zenvon and Veyra gave chase"
**Location:** Summary (Rescue and Pursuit paragraph)
**Issue:** The Summary states "Zenvon and Veyra gave chase while Pip and Sister Maela stayed behind to free the prisoners," then two sentences later says "Pip sprinted after the fleeing bandit." These are mutually contradictory. Campaign docs confirm it was Pip who chased.
**Evidence:** `campaign_state.md`: "**Pip chases the runner into a 20-ft pit trap**, is hauled out on a rope and healed." `world_state.md` timeline: "Pip chases the runner into a 20-ft pit trap." Pip falling in the pit trap (not Zenvon or Veyra) confirms Pip was the chaser.
**Suggested fix:** Remove "Zenvon and Veyra gave chase while Pip and Sister Maela stayed behind." Retain only the accurate statement that Pip sprinted after the bandit.

---

### 3. Who Frees the Captive Women — Internal Contradiction
**Location:** Summary vs. Scenes → "Rescue and Pursuit"
**Issue:** The Summary says "Sister Maela freed the women from the adjacent cell." The Scenes section says "Veyra assists in unlocking the remaining cells to release the captive women." These directly contradict each other.
**Evidence:** Neither `campaign_state.md` nor `world_state.md` specifies which character freed the women; both only record that the captives were freed. The contradiction cannot be resolved from grounding docs alone — a VTT review is needed.
**Suggested fix:** Flag for VTT review. Until confirmed, do not promote either version as canon.

---

### 4. Who Kills the Wounded Ruffian — Scenes Wrong
**Location:** Scenes → "Deception in the Barracks"
**Issue:** The Scenes section states "one bandit named Desa Rook killing the original fleeing ruffian before being cut down himself." Per the Summary and campaign docs, it is **Wick** who kills the wounded ruffian to curry favor — Desa Rook is one of the bandits killed by the party.
**Evidence:** `world_state.md` timeline: "**Desa Rook** and another die; **Wick** kills his own wounded comrade and begs for mercy." Summary (same document, correctly): "Wick cut down the wounded ruffian himself before throwing up his hands to beg for mercy." The NPCs section also correctly attributes the kill to Wick.
**Suggested fix:** Change the Scenes entry to: Wick kills the wounded ruffian and begs for mercy; Desa Rook is killed by the party.

---

### 5. "Nick Ability to Disengage" — Mechanical Error
**Location:** Scenes → "Ambush in the Slave Pens"
**Issue:** "Zenvon strikes a Redbrand with his dagger before maneuvering for a better position using his Nick ability to disengage." Nick (weapon mastery) grants an extra light-weapon attack without expending a bonus action. It does not grant Disengage. Disengaging as a bonus action is **Cunning Action** (Rogue feature).
**Evidence:** `world_state.md`: "Cunning Action; Nick lets the second light-weapon attack land without the bonus action." These are two separate mechanics.
**Suggested fix:** Change to "using his Cunning Action to disengage" (or simply cut the ability reference if the maneuver was purely narrative).

---

### 6. Family Name "Dendars" vs. "Dendrars"
**Location:** Summary (interrogation of Wick paragraph)
**Issue:** "the Redbrands had previously 'handled' a family called the Dendars" — wrong spelling.
**Evidence:** `vtt_transcription_corrections.md`: "Dendars, The Ten Doves → **Dendrars**." `campaign_state.md`, `world_state.md`, and `entity_registry.yaml` all use **Dendrar**.
**Suggested fix:** Change "Dendars" to "Dendrars."

---

### 7. Bandit Name "Desa Rook" vs. "Dosa Rook"
**Location:** Summary; Scenes → "Deception in the Barracks"; NPCs → "Desa Rook"; Items (loot paragraph)
**Issue:** The recap spells the bandit's name "Desa Rook." The canonical normalization document gives a different spelling.
**Evidence:** `vtt_transcription_corrections.md`: "| Dessa | **Dosa Rook** (session 7: Redbrand-handled bandit, full name confirmed from retranscription)." `vtt_known_additions.md` also records the name as "**Dosa Rook**." Note: `campaign_state.md` and `world_state.md` also use "Desa Rook" — they may need correction too.
**Suggested fix:** Normalize to "Dosa Rook" throughout this document and flag the grounding docs for the same correction.

---

### 8. Scene Timeline — Cistern Discovery Out of Order
**Location:** Scenes → "The Hidden Satchel and the Rescue" (placed after "The Bandit's Gambit")
**Issue:** The scene "The Hidden Satchel and the Rescue" begins with the party investigating the cistern and discovering the waterproof satchel. This happened **before** the barracks encounter — the party found the satchel in the cellar, then climbed the stairs to the barracks, then ran the deception. Placing this scene after "The Bandit's Gambit" implies the satchel was found after the fight, which contradicts the Summary.
**Evidence:** Summary (same document): "The party investigated the cistern and discovered a waterproof satchel hidden beneath the water's surface… The party climbed the stairs and pressed their ears to the door at the top [barracks]." `world_state.md` timeline confirms this order.
**Suggested fix:** Move the cistern-discovery bullet points to "The Pit Trap and the Cellar" scene, where they belong chronologically. Rename or reframe "The Hidden Satchel and the Rescue" to cover only the return to the cells.

---

### 9. Glasstaff "Answers to a Higher Power in Phandalin" — Misleading Phrasing
**Location:** Scenes → "The Bandit's Gambit" (bullet 2); NPCs → "Glasstaff"
**Issue:** Both the Scenes and the NPCs entry describe Glasstaff as answering "to a higher power in Phandalin." The phrase "higher power" implies something divine or supernatural. Wick's actual intel was that Glasstaff takes orders from **a person** in town — an unidentified local handler.
**Evidence:** `campaign_state.md`: "Glasstaff 'answers to somebody… orders from town… I don't think Glasstaff's the big boss.'" `world_state.md`: "A Phandalin-resident handler sits between Glasstaff and the Spider." No supernatural element was implied.
**Suggested fix:** Change to "answers to someone in Phandalin" (or "takes orders from an unknown figure in Phandalin").

---

### 10. Freed Captives Not Identified in NPCs Section
**Location:** NPCs → "Human Boy"
**Issue:** The NPCs section lists "Human Boy" as an unnamed captive. He is Nars Dendrar (13). The two women are Mirna Dendrar and Nilsa Dendrar (18) — they receive no entry at all, despite being freed and having open plot hooks (Mirna will ask about Thel; Nilsa is relevant to the family arc).
**Evidence:** `campaign_state.md` NPC table: "Mirna Dendrar — Alive, freed;" "Nars Dendrar (13) — Alive, freed;" "Nilsa Dendrar (18) — Alive, freed." `world_state.md` identifies all three by name.
**Suggested fix:** Replace "Human Boy" with "Nars Dendrar (13)." Add entries for Mirna Dendrar and Nilsa Dendrar with their dispositions and open threads.

---

### 11. Minor — "A bolt" from a Shortbow
**Location:** Summary (first paragraph)
**Issue:** "One of the undead creatures raised a shortbow and loosed a **bolt** at the group." Shortbows fire **arrows**; crossbows fire bolts. The Scenes section correctly says the skeleton "firing a shortbow" without the word "bolt."
**Evidence:** Standard D&D 5e ammunition terminology; the skeleton stat block uses arrows.
**Suggested fix:** Change "loosed a bolt" to "loosed an arrow."

---

### 12. Minor — "Red Cloaks" vs. "Scarlet Cloaks"
**Location:** Summary; Scenes; Locations; NPCs; Items (throughout)
**Issue:** The recap consistently calls the Redbrand garments "red cloaks." Campaign documents uniformly call them "scarlet cloaks" or "scarlet Redbrand cloaks."
**Evidence:** `campaign_state.md`: "scarlet cloaks acquired (disguise + skeleton pacifier)." `world_state.md`: "scarlet Redbrand cloaks." `redbrand_hideout.md`: "scarlet cloaks."
**Suggested fix:** Normalize to "scarlet cloaks" throughout. Low priority, but worth standardizing before promotion to canon docs.