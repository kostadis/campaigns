## Consistency Report — Chapter 60 Recap

---

### 1. NPC Name Error: "Bookworm" (multiple sections)

**Location:** Locations → Bookworm's Office; NPCs → Bookworm

**Issue:** The NPC is referred to as "Bookworm" (the common noun) in both the Locations and NPCs sections of this recap.

**Evidence:** The entity registry, VTT corrections glossary, world_state, campaign_state, and party.md all give the canonical name as **Bookwyrm**. The VTT glossary explicitly lists "Bookworm, Bookform, Bookworn…" as wrong forms that must be corrected to **Bookwyrm**, and flags this as a "confirmed live landmine."

**Suggested fix:** Change "Bookworm" to "Bookwyrm" everywhere in the recap.

---

### 2. NPC Name Inconsistency: "Sylvyr" vs. "Sylvira"

**Location:** Scenes → The Silence of Candlekeep (scene bullet: "Tadric notices that Moziqodo is dead and urges that they must tell Sylvyr.")

**Issue:** The name is rendered as "Sylvyr" in the scene bullet but "Sylvira" everywhere else in the same recap (Summary, NPCs, other scenes). "Sylvyr" does not appear anywhere in the campaign documents.

**Evidence:** All campaign documents use **Sylvira Savikas**. The VTT glossary lists "Silvera salvikas, Silvira Savica, Silvara…" as wrong forms; "Sylvyr" is an unlisted variant not present in any authoritative source.

**Suggested fix:** Change "Sylvyr" to "Sylvira" in that scene bullet.

---

### 3. NPC Faction/Title Error: "two Zhentarim raiders" carrying a bow

**Location:** Summary (paragraph 2); NPCs → Zhentarim Raiders

**Issue:** The recap says one of the two raiders was "carrying the bow that had killed the guard on the walkway." However, the dead Watcher was killed by a **crossbow bolt** (confirmed by the Items section: "Foreign Crossbow Bolt"), so the weapon should be a **crossbow**, not a bow.

**Evidence:** The Items section of this very recap lists "Foreign Crossbow Bolt" and the Spells/scenes section consistently references "crossbow bolt" and "crossbow." The Summary's use of "bow" is inconsistent with the Items section's "crossbow bolt" and the scene description "killed by a crossbow bolt."

**Suggested fix:** Change "the bow that had killed the guard on the walkway" to "the crossbow that had killed the guard on the walkway" (or "the crossbow used to kill the Watcher").

---

### 4. Spell Name Error: "Guiding Bolt" vs. radiant energy bolt

**Location:** Spells → Guiding Bolt; Scenes → Confrontation at the High Tower (bullet: "Grygum attempts to surprise A'lai Avainmore with a bolt of radiant energy, but the wizard's mage armor deflects the attack.")

**Issue:** The Spells section correctly names the spell **Guiding Bolt**. However, the Summary (paragraph 2) describes Grygum launching "a bolt of radiant energy" without naming the spell, and the Scenes section also omits the spell name. This is a minor inconsistency but creates ambiguity — Grygum also has **Inflict Wounds**, **Spirit Guardians**, and a "necrotic holy-symbol blast" per the party doc. The scene bullet and the Spells section need to be internally consistent. More critically, **Guiding Bolt** should be described as succeeding in hitting but missing due to Mage Armor — but Mage Armor sets AC, it does not "deflect" spells. A Guiding Bolt that misses an AC 15 (or 17 per the resume doc) target would simply miss, not be "deflected entirely." The Summary's language ("magical defenses deflected it entirely") implies a magical defense like *counterspell* or *shield*, not an AC miss.

**Evidence:** The resume doc sets A'lai's AC at 17 (XMM Archmage chassis). Mage Armor is the source of that AC. Guiding Bolt misses on a failed attack roll against AC — the phrasing "deflected entirely" suggests a magical reaction, but A'lai does not use Counterspell on a Guiding Bolt (he saves it for Earthen Grasp per the Spells section). The Spells section says "the bolt failed to penetrate his mage armor and had no effect," which is the mechanically accurate description (missed the AC), but the Summary and Scenes language of "magical defenses deflected it entirely" overstates this as a magical deflection.

**Suggested fix:** Revise the Summary and Scenes language to "the bolt went wide / failed to connect, turned by A'lai's hardened magical defenses [i.e., his Mage Armor]" rather than "deflected entirely," which implies a counter-spell reaction. Or accept the flavor language as stylistic and note the mechanical distinction in a GM note.

---

### 5. NPC Spelling Inconsistency: "A'lai Avainmore" vs. canonical "A'lai Aivenmore"

**Location:** Summary (all three paragraphs); Scenes → Confrontation at the High Tower; NPCs → A'lai Avainmore; Spells section (multiple entries)

**Issue:** Throughout the recap, the NPC is consistently spelled **"A'lai Avainmore."** The canonical spelling in every campaign document is **A'lai Aivenmore**.

**Evidence:** The entity registry lists the canonical name as **A'lai Aivenmore** (with aliases Aivenmore, A'lai). The VTT corrections glossary gives "Ally Avonmore, Alai Ivanmore… A'lai Avonmore, A'lai Ivanmore…" as wrong forms, and the correct form as **A'lai Aivenmore**. The campaign_state, world_state, and party.md all use "Aivenmore." The resume doc also uses "Aivenmore" throughout.

**Suggested fix:** Replace every instance of "A'lai Avainmore" with **A'lai Aivenmore** throughout the recap.

---

### 6. NPC Status Ambiguity: Bookwyrm described as murdered in this session

**Location:** NPCs → Bookwyrm ("brutally murdered — her throat torn apart by Moziqodo's claws")

**Issue:** The NPCs section describes Bookwyrm as having been "brutally murdered — her throat torn apart by Moziqodo's claws." However, per campaign_state and world_state, **Bookwyrm (First Reader) is alive** as of Chapter 62. The murdered NPC whose throat was torn out is **not Bookwyrm** — it is an unnamed victim, or this is a confusion with the discovery of a dead Watcher on the walkway. The campaign documents confirm Bookwyrm is a green dragonborn who is alive and was manipulating the investigation.

**Evidence:** Campaign_state NPC table: "Bookwyrm (First Reader) — Alive." World_state §4: "Bookwyrm (First Reader) — Alive — Manipulative, self-preserving." The Janussi murder reconstruction names Alkrist as the one who killed Janussi (poisoned/cleaver blow), not Moziqodo. The entity registry confirms Bookwyrm is a green dragonborn First Reader. The party NPC tracker also lists Bookwyrm as alive. The victim whose throat was torn apart by Moziqodo's claws was a **different character** — context from world_state indicates Moziqodo killed **Bookwyrm**, but this flatly contradicts Bookwyrm's "alive" status in campaign_state (Chapter 62 is after Chapter 60).

**Clarification needed:** Cross-referencing more carefully — the world_state §4 (Candlekeep NPCs) states: "Bookwyrm (First Reader) — Alive." But the NPCs section of this recap says Bookwyrm was killed by Moziqodo. If this happened *in* Chapter 60 and the campaign_state reflects a post-Chapter-60 update, then Bookwyrm should be listed as **dead** in the campaign_state — but she is not. This is a direct contradiction.

**Suggested fix:** Clarify whether Bookwyrm was actually killed in this session. If she was killed in Chapter 60, the campaign_state (which lists her as alive and notes her status is "unconfirmed post-key-seizure") needs updating. If she was not killed — and the campaign_state's "alive" status is authoritative through Chapter 62 — then the NPCs section of this recap incorrectly attributes her murder to this session, and the "brutally murdered" description belongs to a different NPC (possibly the Watcher killed on the walkway, or an error).

---

### 7. Item Continuity: "Real High Tower Key" held by Grygum — second key or one of two keys?

**Location:** Items → Real High Tower Key; Summary (paragraph 3: "Grygum now held both the real High Tower key and the artifact")

**Issue:** The recap states Grygum holds "the real High Tower key." The campaign context consistently refers to **two** High Tower keys being required (the party's key and the key Moziqodo was bringing). The Summary's phrasing "both the real High Tower key and the sapphire" implies Grygum holds one key (singular), but the resume doc confirms: "⭐ Holds **the real High Tower key #2 AND the sapphire**." The recap's Items section says "recovered from Tadric after the battle with Moziqodo" — meaning this is key #2 (the one Tadric was unknowingly holding). Key #1 was the one A'lai seized from Bookwyrm. This distinction is not clearly made in the recap.

**Evidence:** World_state: "A'lai holds the first Hightower key in the High Tower awaiting Moziqodo with the second." Resume doc: "Holds the real High Tower key #2 AND the sapphire." The campaign_state describes "the inert key Daz carries" as a separate key — actually the decoy. There are thus three keys in play: the decoy (previously with Daz), key #1 (A'lai seized from Bookwyrm), and key #2 (recovered from Tadric, now with Grygum).

**Suggested fix:** Clarify in the Items section that Grygum holds **High Tower key #2** (recovered from Tadric), not the only key. A'lai Aivenmore still holds key #1. This distinction is critical for future sessions.

---

### 8. Ambiguous Claim: "Thorin delivering the killing blow" on Moziqodo — in what session?

**Location:** NPCs → Moziqodo ("He was slain by the party in the north gallery rotunda, with Thorin delivering the killing blow using Dawnbringer.")

**Issue:** This claim is consistent with the session's own narrative, but it is worth flagging that the campaign_state does not record who specifically delivered the killing blow on Moziqodo — it only records that Moziqodo was fought in the rotunda. This is a minor documentation point but could cause confusion if future consistency checks compare this against the campaign_state.

**Evidence:** Campaign_state: "North Gallery Rotunda — A domed chamber in the northern galleries where the party fought and killed Moziqodo." No attribution of the killing blow to Thorin in the campaign_state or world_state. Dawnbringer's entry in world_state notes she "delivered the killing blow that slew the abyssal spawn," which is consistent with this recap.

**Suggested fix:** No error, just note for the record: the world_state's Dawnbringer entry independently corroborates Thorin/Dawnbringer delivering the killing blow on Moziqodo, so this is consistent.

---

### 9. Character Ability Ambiguity: Daz's "telekinesis" to seize the sapphire

**Location:** Spells → Telekinesis; Scenes → Confrontation at the High Tower

**Issue:** The recap attributes the sapphire-seizure to **Telekinesis** (a 5th-level spell). The party.md and world_state list Daz's abilities as including **"Telekinetic"** (the Telekinetic feat, which grants a *mage hand* cantrip enhanced with a bonus-action shove) — not necessarily the *Telekinesis* spell (5th level). The Telekinetic feat does not allow seizing an object from a creature's grasp against a Strength save. The *Telekinesis* spell does allow this (contested Strength check). If the GM ran it as the spell (5th-level slot), this is correct. If it was the feat, it is mechanically incorrect as described.

**Evidence:** World_state: "Daz — Abilities: Evoker (Fireball, Scorching Ray, Sculpt Spells), Fey Touched, Warcaster, Misty Step, Shape Water, Magic Missile, Maximilian's Earthen Grasp, Hypnotic Pattern, **Telekinetic**." The Telekinetic feat and the *Telekinesis* spell are distinct. The Spells section names it as "Telekinesis" (the spell) and describes "the wizard failed his strength saving throw," which matches the *Telekinesis* spell mechanic, not the Telekinetic feat.

**Suggested fix:** If Daz used the *Telekinesis* spell (5th-level slot), verify he has it prepared/known as an Evoker (it is not on the standard Wizard Evoker spell list per the ability description in party.md, but Wizards can learn any spell). If the intent was the Telekinetic feat, the mechanical description (Strength saving throw, object seized from grip) does not match — the feat only allows a 5-foot shove. Clarify which was used and ensure it is consistent with Daz's sheet.

---

### 10. Timeline/Continuity: "Darrl nearly killed" — unidentified character name

**Location:** Summary (paragraph 2): "Bookworm dead, Darrl nearly killed, Janussi gone, guards slain"

**Issue:** The name "Darrl" appears in A'lai's monologue as quoted in the Summary. This appears to be a transcription variant of **Daral** (Daral Yashenti). However, "Darrl" does not appear in the VTT corrections glossary, the entity registry, or any campaign document. The VTT glossary lists "Daryl, Jarl, Droll, Darrell, And Daryl, Dural, Gal" as wrong forms of **Daral**.

**Evidence:** VTT corrections: "Daryl, Jarl, Droll, Darrell, And Daryl, Dural, Gal" → **Daral**. Entity registry: **Daral Yashenti**. The only "Darrl" in any document is this recap.

**Suggested fix:** Change "Darrl" to **Daral** in A'lai's quoted monologue in the Summary.

---

### Summary of Issues by Severity

| # | Issue | Severity |
|---|---|---|
| 5 | "A'lai Avainmore" should be "A'lai Aivenmore" (consistent throughout) | **High** — wrong canonical name, will propagate |
| 6 | Bookwyrm listed as murdered — contradicts campaign_state (alive through Ch62) | **High** — direct factual contradiction |
| 1 | "Bookworm" should be "Bookwyrm" | **Medium** — confirmed live landmine per glossary |
| 7 | Grygum's key not identified as key #2; key #1 still with A'lai | **Medium** — ambiguity will confuse future sessions |
| 2 | "Sylvyr" should be "Sylvira" | **Low** — isolated typo, one occurrence |
| 3 | "bow" should be "crossbow" | **Low** — internal inconsistency within the recap |
| 4 | "deflected entirely" misrepresents Mage Armor as a magical deflection | **Low** — flavor vs. mechanics; flagged for GM awareness |
| 9 | "Telekinesis" (spell) vs. "Telekinetic" (feat) — ability identity unclear | **Low** — needs sheet verification |
| 10 | "Darrl" should be "Daral" | **Low** — transcription variant |
| 8 | Thorin killing blow attribution | **None** — consistent with world_state |