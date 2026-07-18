---

## Consistency Report — Session 2026-06-25

---

### CONFIRMED ERRORS (contradicted by grounding documents)

---

**1. Mace of Smiting — wrong attribution**

- **Location:** Summary ("recovered powerful magical artifacts from Belsornig's corpse, including … a mace of smiting"); Scenes / Looting the Water Temple; Items / Mace of Smiting
- **Issue:** The recap treats the Mace of Smiting as a new acquisition found on Belsornig's body.
- **Evidence:** `world_state.md` party equipment: *"Mace of Smiting (Calmer, looted from Lareth)"*; `party.md` collective resources: *"Mace of Smiting (Calmer)"*; `party.md` Calmer's items of significance: *"Mace of Smiting (+6, 1d6+3; Earth Temple looted from Lareth)"*. The item was acquired in Chapter 13 and has been in Calmer's possession ever since.
- **Suggested fix:** Remove the Mace of Smiting from Belsornig's loot list entirely. If the Water Temple yielded a different striking weapon, name it distinctly; otherwise note that Calmer already carried this weapon into the fight.

---

**2. Ring of Free Action — wrong attribution**

- **Location:** Summary ("a mace of smiting, and a ring of free action"); Scenes / Looting the Water Temple; Items / Ring of Free Action
- **Issue:** Same problem as above — the recap presents the Ring of Free Action as a new find on Belsornig.
- **Evidence:** `world_state.md` party equipment: *"Ring of Free Action (from Lareth)"*; `party.md` collective resources: *"Ring of Free Action (party)"*. The ring was looted from Lareth in Chapter 13.
- **Suggested fix:** Remove from Belsornig's loot. If a second ring was legitimately present, differentiate it clearly.

---

**3. Belsornig's death is asserted but never depicted**

- **Location:** Summary ("Canon Belsornig's chambers"); Scenes / Looting the Water Temple ("the chambers of the fallen Canon Belsornig"); NPCs / Belsornig ("The deceased Prophet of Water whose corpse was looted")
- **Issue:** Belsornig is treated as already dead and looted, but no combat with him — and no account of *how or when he died* — appears anywhere in the recap. This will create confusion in future sessions.
- **Evidence:** `campaign_state.md` Active Quests: *"Belsornig (Water Temple, area 215) — Confrontation Unresolved."* NPC table: Belsornig status = *"Alive | Water Temple, Dungeon Level Two | Hostile; currently under Fire Temple assault."* The most plausible in-fiction explanation is that Alrrem's simultaneous Fire Temple assault (confirmed ongoing in campaign_state) killed him before the party reached his chambers — but the recap never states this.
- **Suggested fix:** Add a single sentence to the Summary or Looting scene noting how/when Belsornig died (e.g., "the party found Belsornig's body already slain — apparent victim of Alrrem's assault — when they broke into his chambers"). Update his NPC status to Deceased, cause noted.

---

**4. Zinnia's pronouns — inconsistent throughout**

- **Location:** Summary (multiple sentences); Scenes / Gargoyle Ambush ("uses the falling creature's body to cushion *his* landing")
- **Issue:** The Summary switches among "himself," "she," and "him" for Zinnia within the same passage. Example: *"sprinted across the chamber and launched **himself** into the air… **she** clung to the creature's back… it hissed and writhed beneath **him**."*
- **Evidence:** `party.md` lists Zinnia consistently with she/her pronoun usage (Player: George/George Kolivakis; no pronoun note, but no masculine pronoun ever appears in the grounding docs). Internal self-contradiction regardless.
- **Suggested fix:** Standardize to she/her throughout every section.

---

**5. "Sequioa" — misspelling of character name**

- **Location:** Summary (multiple uses: "Sequioa acted swiftly," "Zephyr as a deliberate distraction, positioning him nearby so *he* could strike"); Scenes / The Fall of the Juggernaut ("Zinnia and Sequioa attempt to hold a door shut")
- **Issue:** The character's name is spelled "Sequioa" rather than "Sequoia" in several places.
- **Evidence:** `party.md`, `world_state.md`, `campaign_state.md` — all use "Sequoia."
- **Suggested fix:** Global find-and-replace: Sequioa → Sequoia.

---

**6. Trident mentioned in Summary but absent from Items section**

- **Location:** Summary ("Belsornig's chambers yielded … books of lore, and a trident"); Items section (no trident listed)
- **Issue:** A trident appears in the loot narrative but is not recorded in the Items list. This leaves it in limbo for inventory tracking.
- **Evidence:** Internal inconsistency; `campaign_state.md` records a prior magical trident (tithed to Terjon in Ch.12), so a second trident needs clear distinction.
- **Suggested fix:** Either add a Trident entry to the Items section (with description and value) or remove it from the Summary loot list if it was not actually recovered.

---

**7. Triton's telepathic message — contradictory attribution**

- **Location:** Summary vs. Memorable Moments / "The triton is pleading to be released…"
- **Issue:** The Summary states *"a telepathic voice filled their minds"* — the party heard the triton directly. The Memorable Moments attributes the cliffhanger quote to *Brother Eelrich Vane*, with first-person phrasing ("so that **I** can prevent your deaths"), as if Eelrich is the speaker. If Eelrich was relaying a third-party message, the pronoun should be "it" or "the triton"; if the party heard the triton directly, Eelrich should not be listed as the speaker.
- **Evidence:** Internal contradiction; will determine who "knows" the triton has communicated in future sessions.
- **Suggested fix:** Decide and commit: either (a) the party heard the triton telepathically themselves (remove Eelrich as the listed speaker; attribute the quote to "The Triton") or (b) Eelrich relayed the message (fix pronoun to third-person and confirm in the Summary).

---

**8. Session date — header vs. title mismatch**

- **Location:** Document title ("Session 2026-06-25") vs. Date field ("Date: Jun 22nd, 2026")
- **Issue:** The filename implies June 25th; the header states June 22nd. At least one is wrong.
- **Evidence:** No in-world impact, but inaccurate metadata corrupts chronological session filing.
- **Suggested fix:** Confirm the actual play date and correct the header to match the title or vice versa.

---

### VERIFY BEFORE NEXT SESSION (possible errors — confirm against character sheets)

---

**9. Arcane spells credited to non-caster characters**

- **Location:** Spells / Jump ("A spell cast by Sequoia to dramatically increase their jumping height"); Spells / Silvery Barbs ("A reaction spell used by Sequoia to force the Juggernaut to reroll…"); Spells / Misty Step ("A teleportation spell considered by Zinnia")
- **Issue:** Sequoia is listed in `party.md` as a Halfling Rogue; Zinnia as an Elf Monk. Neither class has arcane spellcasting unless Sequoia is an Arcane Trickster or either character has a relevant feat. *Jump* and *Silvery Barbs* (a 1st-level enchantment spell) both require a spell slot. Arcane Tricksters can know enchantment spells, but their subclass and spell list are not documented in the grounding docs.
- **Evidence:** `party.md` — Sequoia's subclass is not specified; no spellcasting ability is mentioned. Zinnia's Monk sheet makes no reference to *Misty Step* access (normally via Shadow Monk or a feat).
- **Suggested fix:** Verify Sequoia's subclass (Arcane Trickster?) and spell list, and Zinnia's access to *Misty Step*, against the actual character sheets. If correct, add a note to `party.md` documenting the subclass and known spells so future sessions have a record. If incorrect, replace *Silvery Barbs* with the ability actually used (e.g., Uncanny Dodge, a different class feature).

---

**10. Half-Plate +1 from Belsornig — possible duplication of existing plate mail**

- **Location:** Summary; Items / Half-Plate +1
- **Issue:** The party already holds *"+1 Plate Mail (AC 20 with shield)"* attributed to Calmer in `party.md`, and `world_state.md` records *"Magical plate mail (looted from Lareth; fits no party member — disposition unresolved)."* A second piece of magical armor appearing on Belsornig the same session the Mace and Ring are also mislabeled warrants explicit verification.
- **Evidence:** `party.md` Calmer items; `world_state.md` party equipment.
- **Suggested fix:** Confirm against session notes whether Belsornig genuinely yielded distinct Half-Plate +1 armor. If the loot was the existing +1 plate mail being redistributed to Calmer, correct the attribution and remove the "new find" framing.

---

**11. Protective Zone described as "~sixty feet in range"**

- **Location:** Locations / The Protective Zone ("A shimmering yellow area of magical protection, roughly sixty feet in range, that slows enemies who enter it")
- **Issue:** If this is Calmer's *Spirit Guardians* (consistent with the scene description of a radiant aura damaging gargoyles), the spell has a 15-foot radius (30-foot diameter), not 60 feet. The location entry may inflate the area.
- **Evidence:** D&D 5e *Spirit Guardians* — 15-ft radius, self-centered. No other War Domain cleric spell that slows and damages within an aura matches a 60-ft range.
- **Suggested fix:** Verify which spell created the zone. If Spirit Guardians, correct to "roughly thirty feet across (fifteen-foot radius)" or omit the dimension. If a different spell, name it.