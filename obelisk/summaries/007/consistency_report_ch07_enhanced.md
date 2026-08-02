# Consistency Report — Chapter 07: Deception

---

## 1. Skeleton Count (Summary, Scenes, NPCs, Spells)

**Issue:** The recap consistently states there were **four** skeletons in the crypt fight ("two of the four skeletons recoiled in supernatural terror").

**Evidence:** `redbrand_hideout.md` (R4), `campaign_state.md` ("Six skeletons; Maela turned several, the rest destroyed"), and `world_state.md` (Ch. 6 cliffhanger: "oak-tree columns, six skeletons") all establish **six** skeletons. The campaign_state aftermath — "two surviving skeletons now stand down for red-cloak wearers" — is only coherent if four were destroyed in combat, implying the fight involved all six.

**Suggested fix:** Replace every instance of "four skeletons" / "two of the four" with "six skeletons" / "two of the six." The two that fled and returned are the two surviving guardians; four were destroyed.

---

## 2. Skeleton Wisdom Modifier (Summary → Scenes → NPCs → Spells)

**Issue:** The recap repeatedly states the skeletons had a **+2 wisdom modifier** when making Turn Undead saving throws.

**Evidence:** A standard D&D 5e skeleton has Wisdom 8 (−1 modifier). No modified stat block is referenced in any campaign document. The +2 is most likely a transposition of the skeleton's Dexterity modifier (+2, from DEX 14).

**Suggested fix:** Change "+2 wisdom modifier" to "−1 wisdom modifier" throughout, or omit the modifier entirely and state only the DC.

---

## 3. Pip's Action Surge at Level 1 (Summary, Scenes, NPCs)

**Issue:** Pip uses **Action Surge** during the crypt fight.

**Evidence:** `party.md`, `campaign_state.md`, and `world_state.md` all explicitly state Pip is **Level 1** with a "long-overdue level-up." Action Surge is a 2nd-level Fighter feature — unavailable at Level 1 under both standard rules and the Tasha's Cauldron sidekick Warrior progression. (Even if the "sidekick level = Zenvon's Level 2" rule is applied, Action Surge remains a Level 2 standard-fighter feature, but the documents uniformly describe all sidekicks as still at Level 1.)

**Suggested fix:** Remove the Action Surge reference. Describe Pip's two attacks as part of the normal combat flow or flag it as a DM ruling that should be noted in `characters/pip.md`.

---

## 4. Cure Wounds Formula "2d8+2" (Summary, Scenes)

**Issue:** Cure Wounds is described as healing "ten hit points via Cure Wounds (2d8+2)."

**Evidence:** Maela is a **Level 1** cleric sidekick. Cure Wounds at 1st level is **1d8 + spellcasting modifier**, not 2d8+2. The 2d8+2 formula is a 2nd-level casting, which requires a 2nd-level spell slot unavailable at Level 1. A roll of 10 on 1d8+2 is possible (max 10); the result is plausible with the correct formula.

**Suggested fix:** Change "2d8+2" to "1d8+2" (or 1d8 + spellcasting modifier) in Summary, Scenes, and Spells sections.

---

## 5. Firebolt "2-Point Result in the Crypts" (Spells)

**Issue:** The Spells section states: *"The DM noted after the 2-point result in the crypts that it 'does a lot less damage than the sound effects.'"*

**Evidence:** Veyra did **not use Firebolt in the crypts** — she used Magic Missile there (her last slot). The DM's "less damage than the sound effects" comment is explicitly tied to the **8-point Firebolt in the slave pens** in the Summary section ("she and the DM agreeing it did 'a lot less damage than the sound effects'"). No 2-point Firebolt result exists anywhere in the Summary or Scenes sections.

**Suggested fix:** Move the DM quote to the slave pens context. Delete the "2-point result in the crypts" reference.

---

## 6. Firebolt "3 Points During the Barracks Skirmish" (Spells)

**Issue:** The Spells section claims Veyra used Firebolt for **3 points of damage during the barracks skirmish**.

**Evidence:** Neither the Summary nor the Scenes section (Deception in the Barracks / The Bandit's Gambit) mentions Veyra attacking at all during the barracks fight. The Summary describes only Pip and Zenvon dealing damage in that engagement.

**Suggested fix:** Remove this claim from the Spells section. If Veyra did act in the barracks, add supporting detail to the relevant scene; otherwise it is an unverified addition.

---

## 7. Pip's Kill Count in the Barracks Brawl (Summary vs. Scenes)

**Issue:** The Summary states "Pip killed two of the bandits." The Scenes section (Deception in the Barracks) states "Pip kills another" — singular.

**Evidence:** These are internally contradictory. The Scenes section gives Zenvon one kill (12 damage) and Pip one kill; Wick kills the ruffian. The Summary adds a second kill for Pip without any additional combat narration to support it.

**Suggested fix:** Reconcile to a single count. The Scenes section's one-for-Pip / one-for-Zenvon breakdown is more granular and should be treated as authoritative. Amend the Summary accordingly.

---

## 8. Cure Wounds Timing for Zenvon (Summary vs. Scenes)

**Issue:** The Summary places Maela's Cure Wounds on Zenvon **after** the killing blow and after the fight ends. The Scenes section places it **mid-fight**, before the killing blow ("keeping him in the fight").

**Evidence:** Both sections are describing the same single Cure Wounds cast. They cannot both be accurate. The Scenes section's "keeping him in the fight" framing is more consistent with the narrative logic (he's at 4 HP with active enemies).

**Suggested fix:** The Summary's placement ("Sister Maela then laid her hands on Zenvon…before the party turned their attention to the sarcophagi") should be revised to reflect that the heal occurred mid-combat, before Zenvon's killing blow.

---

## 9. Unverified Cure Wounds: Pip After the Slave Pens Fight (Spells)

**Issue:** The Spells section claims a **second Cure Wounds**: "restoring 10 hit points to Pip after the slave pens combat (voiced as a second Cure Wounds)."

**Evidence:** No healing of Pip after the slave pens fight appears anywhere in the Summary, the Scenes section (Ambush in the Slave Pens), or the NPCs section for Sister Maela, which names only two specific Cure Wounds instances (10 HP for Zenvon after the crypt fight; 6 HP for Pip after the pit fall). If this cast occurred, it is absent from the narrative record and should not appear in the spell log.

**Suggested fix:** Remove this third casting from the Spells section unless the VTT transcript confirms it. If confirmed, add the event to the corresponding Scenes section.

---

## 10. Magic Missile Slot Count (Summary / Spells)

**Issue:** The Summary states Veyra had "already expended two prior castings" before the crypt fight and then used her "last remaining slot" in the crypts — **three total** first-level slot uses with no rest between sessions.

**Evidence:** A Level 1 Spellcaster sidekick has **2 first-level spell slots** (Tasha's Cauldron sidekick rules). Three castings with no intervening long rest is mechanically impossible at Level 1. If the "sidekick level equals Zenvon's Level 2" rule is in force, a Level 2 Spellcaster sidekick has 3 first-level slots, which would fit — but all context documents (`party.md`, `campaign_state.md`, `world_state.md`) explicitly describe Veyra as still Level 1.

**Suggested fix:** Either reduce "two prior castings" to "one prior casting" (consistent with Level 1 = 2 slots), or note in the session record that Veyra was run as effectively Level 2 for slot purposes. Confirm against the VTT and amend `characters/veyra.md` accordingly.

---

## 11. Cistern Satchel Contents Incomplete (Summary, Items)

**Issue:** The recap records the cistern satchel as containing only a potion of healing and a potion of invisibility.

**Evidence:** `redbrand_hideout.md` specifies the satchel also contains **50 gp** and **clean travel clothing** (Glasstaff's emergency escape kit). Neither the recap nor the parallel `gm-assist.md` accounts for these items. If the DM changed the satchel's contents at the table, that should be noted; if not, 50 gp is missing from the party's loot ledger.

**Suggested fix:** Verify against the session VTT. If the 50 gp and travel clothing were present, add them to the Items section and the party's coin total in `campaign_state.md`.

---

## 12. Column Description (Locations — Tresendar Crypts)

**Issue:** The Locations section describes "three stone sarcophagi and **false columns**."

**Evidence:** `world_state.md` (Ch. 6 timeline) and `redbrand_hideout.md` describe them as **"oak-tree columns"** — decorative carved pillars, not false/hollow constructions.

**Suggested fix:** Change "false columns" to "oak-tree columns" or "carved stone pillars."

---

*No issues found with: NPC names (Dosa Rook, Wick, Glasstaff, the Dendrars) or their factions; the bracelet value (140 gp); the pit trap depth (20 ft, 3 HP fall damage); the deception sequence and its roll with advantage; the Dendrar family composition (two women + young boy = Mirna, Nilsa, Nars); the bandit loot breakdown; or the broad sequence of the session's events.*