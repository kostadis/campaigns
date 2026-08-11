# Consistency Report — Session 2026-08-09

---

## 1. NPC NAME: A'lai Aivenmore vs. A'lai Avainmore

**Location:** Summary, Memorable Moments, Scenes (all three), NPCs section ("A'lai Avainmore")

**Issue:** The recap consistently spells the wizard's name **"A'lai Avainmore"** (with a "v" before the "a"). The canonical spelling across all campaign documents is **"A'lai Aivenmore"** (or sometimes "Aivenmore").

**Evidence:** campaign_state.md: "A'lai Aivenmore"; world_state.md: "A'lai Aivenmore"; entity_registry.yaml: `A'lai Aivenmore` with aliases `Aivenmore, A'lai`; vtt_transcription_corrections.md glossary: wrong form "A'lai Avonmore, A'lai Ivanmore" → right form **"A'lai Aivenmore"**; player_npc_tracker_candlekeep.md: "A'lai Aivenmore."

**Suggested fix:** Replace every instance of "A'lai Avainmore" / "Avainmore" with **"A'lai Aivenmore"** / **"Aivenmore"** throughout the recap.

---

## 2. ITEM: "Conjured Hand of Compact Soil" — spell name nonstandard / possibly wrong

**Location:** Spells section

**Issue:** The recap names a spell **"Conjured Hand of Compact Soil"** as cast by Daz to seize and hold A'lai Aivenmore. No such spell appears in Daz's ability list. The canonical spell that creates a grasping earth hand is **Maximilian's Earthen Grasp** (confirmed in Daz's world_state.md and party.md ability lists).

**Evidence:** world_state.md (Daz abilities): "Maximilian's Earthen Grasp"; party.md (Daz items/abilities): same. "Conjured Hand of Compact Soil" does not appear in any campaign document or the D&D 5e SRD.

**Suggested fix:** Rename to **"Maximilian's Earthen Grasp"** (Daz's confirmed spell list). If the GM used a reskinned name at the table, flag it as a known alias in the VTT corrections file; do not leave the fabricated name in the canonical recap.

---

## 3. NPC STATUS: Tadric described as "watcher and Kalan's lieutenant who held the real High Tower key" — marked "Alive" in grounding docs but killed per staleness note

**Location:** NPCs section ("Tadric")

**Issue:** The grounding docs list Tadric as "Alive" (campaign_state.md NPC table), but the grounding_docs_stale_20260803.md explicitly records that **Tadric was killed by the party** and the real key was recovered from him in the 2026-07-27 session. The recap's NPCs section correctly describes his death. However, the wording "He was killed by the party in a single round of combat, after which the real key was recovered from him" is accurate and internally consistent with the staleness note — **no error in the recap itself**, but any future document regeneration must update Tadric's status to **Dead**.

**Evidence:** grounding_docs_stale_20260803.md: "Tadric was killed by the party; the REAL High Tower key was recovered from him." campaign_state.md NPC table: "Tadric | Alive."

**Suggested fix:** Flag for grounding-doc update: change Tadric's status to **Dead** in campaign_state.md and world_state.md. The recap is not wrong; the stale grounding docs are.

---

## 4. ITEM DESCRIPTION: "Real High Tower Key" — attribution confusion in Items section

**Location:** Items section ("Real High Tower Key")

**Issue:** The Items section states: *"Grygum held this key along with the sapphire."* But the recap's own Scenes and Summary indicate that the sapphire (the stolen gem) was held by Grygum, while the key sequence is as follows: the real key was recovered from Tadric (prior session), and subsequently one key was passed from Daz to Zalthir and hidden in Glabbagool. The Items section conflates the sapphire and the key as simultaneously in Grygum's possession, which is ambiguous/inconsistent with the scene narrative.

**Evidence:** Summary: "Daz quietly slipped one key to Zalthir, and it was ultimately tucked away inside Glabbagool." Scenes ("The Capture of A'lai Avainmore..."): "Daz uses sleight of hand to secretly pass one of the keys to Zalthir." The sapphire had been passed to Grygum earlier. There is no scene where Grygum holds both the key and the sapphire simultaneously as the primary carrier.

**Suggested fix:** Clarify the Real High Tower Key's chain of custody: recovered from Tadric → held by Daz → passed (via sleight of hand) to Zalthir → stored inside Glabbagool. The sapphire remains separately with Grygum. Remove the statement that Grygum held the key.

---

## 5. GLABBAGOOL DESCRIPTION: "intelligent grey ooze" vs. established "gelatinous cube" origin

**Location:** NPCs section ("Glabbagool")

**Issue:** The NPCs section introduces Glabbagool as *"An intelligent grey ooze."* The campaign documents consistently describe Glabbagool as a **sentient gelatinous cube** (originally) who became a bonded companion. The world_state.md and player_npc_tracker describe him as a "sentient grey ooze" in some later references (after his transformation arc), but entity_registry.yaml notes "sentient ooze companion who prefers to remain in the Underdark." The glabbagool_shadow_monk_sidekick.md stat block labels him *"Medium Ooze."* This is not strictly wrong as of current state, but calling him "grey ooze" potentially conflicts with his gelatinous cube origin and the stat block's "Medium Ooze" creature type designation.

**Evidence:** world_state.md companion section: "sentient grey ooze (formerly gelatinous cube)"; party.md: "sentient grey ooze (formerly gelatinous cube)"; entity_registry: "sentient ooze companion."

**Suggested fix:** Use **"sentient ooze (formerly a gelatinous cube)"** or simply **"Glabbagool"** to avoid the "grey ooze" tag, which is a specific D&D 5e creature type distinct from a gelatinous cube. The parenthetical origin is part of his established character description.

---

## 6. GLABBAGOOL BOND: "standing just a little taller with pride" — arm bond not mentioned

**Location:** Summary, Scenes ("The Capture of A'lai Avainmore...")

**Issue:** Glabbagool is described as a free-standing companion who is "entrusted with hiding one of the High Tower keys inside his gelatinous form." The campaign documents establish that **Glabbagool is bonded to Zalthir's left forearm** — he is physically fused to Zalthir's arm, not a fully autonomous companion who moves around independently and "stands" on his own.

**Evidence:** world_state.md: "Bonded to Zalthir's left forearm, functioning as a semi-autonomous extension of his body"; party.md: "Glabbagool is bonded to his left forearm"; campaign_state.md NPC table: "Bonded to Zalthir's forearm."

**Suggested fix:** Clarify the key-hiding description to reflect the forearm bond: e.g., *"the key was tucked inside Glabbagool, who remains fused to Zalthir's forearm."* The image of Glabbagool independently "standing taller" is a charming narrative beat, but should acknowledge the fused-arm context.

---

## 7. DAWNBRINGER DESCRIPTION: "established as canonically female during this session"

**Location:** Items section ("Dawnbringer")

**Issue:** The Items section states Dawnbringer's female identity was *"established as canonically female during this session."* However, the campaign documents already record Dawnbringer as "she" / female well before this session. The world_state.md and party.md both refer to Dawnbringer as "she" and "her" as settled canon, and the thorin_dawnbringer_rituals.md file, written before this session, uses female pronouns throughout.

**Evidence:** world_state.md: "Now referred to as 'she.'"; party.md: "Dawnbringer ('she')"; thorin_dawnbringer_rituals.md: uses "she/her" throughout, predating this session.

**Suggested fix:** Remove "established as canonically female during this session." Her gender is long-settled canon. If something specific happened *in this session* that reinforced or celebrated that fact, phrase it as a *confirmation* or a *notable in-session moment*, not a new establishment: e.g., *"Dawnbringer's female identity was prominently invoked during the battle."*

---

## 8. MANSHOON: "conjured a wall of force and shattered the magical door"

**Location:** Summary, Memorable Moments, Scenes ("The Capture of A'lai Avainmore..."), NPCs ("Manshoon")

**Issue:** The recap states Manshoon used *Wall of Force* to shatter the magical door to Candlekeep's inner sanctum. This is mechanically contradictory: *Wall of Force* creates an impermeable barrier but does not deal damage or break other objects — it cannot "shatter" a door. The candlekeep_hightower_session.md prep notes describe Manshoon using overwhelming magical power to breach the wards but do not specify Wall of Force as the method for door-breaking. It is possible the GM described something that the VTT transcription or summary has misattributed.

**Evidence:** D&D 5e: Wall of Force creates a wall, it does not destroy objects. candlekeep_hightower_session.md does not specify Wall of Force as the door-breaching mechanism. The Spells section separately lists Wall of Force as what Manshoon conjured.

**Suggested fix:** Flag for GM clarification: what spell or action did Manshoon use to breach the door? If Wall of Force was used to *hold* the party while another effect destroyed the door, correct the description accordingly. If a different spell (e.g., Disintegrate, Shatter, Passwall) was used for the breach, name it correctly.

---

## 9. CANDLEKEEP WARDS: "legendary magical wards had been broken" by Daz's fireball

**Location:** Summary, Memorable Moments, Scenes, Locations ("Candlekeep")

**Issue:** The recap frames Daz's fireball as *proof* the wards failed. This is consistent with the candlekeep_hightower_session.md GM prep, which establishes that Candlekeep's wards specifically blocked fire damage (among other things), so a fireball successfully detonating would signal the wards were down. The description is internally consistent with the prep document. **No error** — flagging only to note the internal logic is confirmed by the GM document.

**Evidence:** candlekeep_hightower_session.md: "Candlekeep's wards specifically block teleportation, flight, and fire damage — that's the entire security model… Nice free beat: someone casting a fire spell for the first time in the chaos and being visibly startled it actually connects."

**Suggested fix:** No correction needed. The recap's framing is accurate.

---

## 10. AMBIGUOUS: "A'lai told the surviving Thug to go get Daz, who had the gem"

**Location:** Summary (opening sentence)

**Issue:** The Summary's opening sentence states A'lai directed the surviving thug toward Daz because *"Daz had the gem."* Per the prior session's established facts (grounding_docs_stale_20260803.md), the sapphire was **already secretly passed to Grygum** in the 2026-07-27 session before this session began. A'lai would be mistaken in this belief — which is a legitimate story beat — but the recap should clarify whether A'lai *believed* Daz had the gem (which is the dramatic irony) vs. whether the recap is presenting this as factually true.

**Evidence:** grounding_docs_stale_20260803.md: "A'lai's sapphire was seized by Daz (telekinesis) and covertly passed to Grygum." The Scenes section later correctly states: *"Daz had secretly passed it to Grygum."*

**Suggested fix:** Revise the opening to clarify it is A'lai's (mistaken) belief, not a factual statement: e.g., *"A'lai — believing Daz still held the gem — told the surviving thug to target the wizard."*