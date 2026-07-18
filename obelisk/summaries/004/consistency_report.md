# Continuity Report — *Ambush in Phandalin: The Redbrand Reckoning*

---

## ISSUE 1 — Wrong character name for the tiefling sidekick

**Location:** Summary (multiple references); Scenes — Return to Phandalin, Breakfast, Redbrand Ambush; NPCs — Vera; Spells — Magic Missile; Memorable Moments

**Issue:** The tiefling spellcaster sidekick is called **"Vera"** throughout the recap.

**Evidence:** Both `world_state` and `campaign_state` consistently name her **"Veyra"** — the party roster, NPC table, timeline, and mechanics notes all use "Veyra" without exception.

**Suggested fix:** Replace every instance of "Vera" with **"Veyra"** across all sections.

---

## ISSUE 2 — Wrong proprietor name for the Stonehill Inn

**Location:** Summary; Scenes — Return to Phandalin; NPCs — Toblin Stonehill; Locations — Stonehill Inn

**Issue:** The innkeeper is called **"Toblin Stonehill"** in the NPCs section but **"Toblin Stonehill"** is also used in the Summary — however, the recap alternates and the NPC table header reads "Toblin" correctly in one place. More critically, the `world_state` and `campaign_state` spell the name **"Toblen Stonehill"** (with an *e*), not "Toblin."

**Evidence:** `world_state` NPC list: *"Toblen Stonehill — Owner, Stonehill Tavern."* `campaign_state` NPC table: *"Toblen Stonehill | Alive | Stonehill Tavern, Phandalin."*

**Suggested fix:** Correct all instances of "Toblin" to **"Toblen"** throughout the recap.

---

## ISSUE 3 — "Elmar the barkeep" is an unattested name; the bartender is Elsa

**Location:** Summary ("Elmar the barkeep poured out celebratory ale"); Scenes — Return to Phandalin ("Elmar the barkeep provides ale"); NPCs — Elmar

**Issue:** The recap introduces **"Elmar"** as the barkeep at the Stonehill Inn. No character by this name appears in either context document. The bartender at the Stonehill Tavern is **Elsa**.

**Evidence:** `world_state` Key NPCs: *"Elsa — Bartender, Stonehill Tavern; sharp-eyed. Has a scholar sister in Neverwinter. Recommended Daran Edermath as a local source."* `campaign_state` NPC table: *"Elsa | Alive | Stonehill Tavern, Phandalin | Friendly."*

**Suggested fix:** Replace "Elmar the barkeep" with **"Elsa"** in all sections, and remove or correct the "Elmar" NPC entry accordingly.

---

## ISSUE 4 — Tuck described as an adult; he is a 9-year-old child

**Location:** Summary ("a local named Tuck sprinted across the room to throw his arms around Zenvon in a tearful embrace"); Scenes — Return to Phandalin; NPCs — Tuck

**Issue:** The recap presents Tuck as an undifferentiated "local," which implies an adult. The embrace and emotional display are framed as peer-level interaction. In fact, Tuck is a young child.

**Evidence:** `world_state` Key NPCs: *"Tuck — 9-year-old son of Toblen; offered to guide the party to a tunnel into the woods."* `campaign_state` NPC table lists him under Phandalin with no faction note, consistent with a child townsfolk NPC.

**Suggested fix:** Identify Tuck as **Toblen's 9-year-old son** in the NPCs section and adjust the Summary framing to reflect that the embrace is from a child, not an adult peer.

---

## ISSUE 5 — Sildar described as "a member of the Lords' Alliance" without his rank; minor but potentially misleading

**Location:** NPCs — Sildar Hallwinter ("A member of the Lords' Alliance")

**Issue:** Not technically wrong, but the campaign documents consistently identify Sildar as a **Lords' Alliance agent** (intelligence/field operative role), not merely a generic member. The distinction matters because he is explicitly tasked with field investigation, not policy. The recap's Summary also calls him a "wealthy Lords' Alliance man," which overstates his apparent resources — he is described in `world_state` as an agent who "recovered enough to walk and negotiate but cites lingering wounds," with no indication of personal wealth.

**Evidence:** `world_state`: *"Sildar Hallwinter — Lord's Alliance agent."* `campaign_state`: *"Sildar Hallwinter | Alive | Traveling with party to Phandalin | Ally (paying escort)."*

**Suggested fix:** Refer to Sildar as a **Lords' Alliance agent** in the NPCs section. Remove or soften the implication that he is personally wealthy in the Summary.

---

## ISSUE 6 — Phandelver Pact described as destroyed by "bandits and evil mercenary wizards"; source text says bandits and a catastrophic spell battle

**Location:** Scenes — Breakfast, Revelations, and Negotiations ("bandits and evil mercenary wizards attacked, destroying much of the cavern"); Locations — Wave Echo Cave ("a great magical battle 500 years ago")

**Issue:** The Scenes section attributes the destruction to "evil mercenary wizards," which is a meaningful embellishment not present in the campaign documents. The Locations section describes it more accurately as "a great magical battle." The two descriptions within the same recap are inconsistent with each other, and the Scenes version adds a faction ("evil mercenary wizards") that has no support in the context documents.

**Evidence:** `world_state` and `campaign_state` both describe the loss of Wave Echo Cave as resulting from "a devastating bandit assault and a catastrophic spell battle" with no reference to mercenary wizards as a named faction.

**Suggested fix:** Standardize the description to **"a bandit assault and a catastrophic spell battle"** in both the Scenes and Locations sections. Remove "evil mercenary wizards" as an unsupported addition.

---

## ISSUE 7 — Sildar stated to pay 50 gp for escort in Scenes but this conflicts with the 100 gp negotiation outcome

**Location:** Scenes — Breakfast, Revelations, and Negotiations ("Sildar pays the party the promised 50 gold pieces for escorting him safely to Phandalin" and "securing 100 gold pieces upfront")

**Issue:** Within the same scene description, Sildar is said to first pay the 50 gp escort fee owed from the original agreement, and then separately to pay 100 gp upfront for the new tasks. This is internally consistent and matches the campaign documents — however, the Summary only mentions the 100 gp negotiation and omits the 50 gp escort payment, creating a gap between Summary and Scenes. A future reader relying on the Summary alone would not know the 50 gp was collected.

**Evidence:** `campaign_state` Active obligations: *"Escort Sildar Hallwinter safely to Phandalin (owed 50 gp on delivery)."* The Scenes section correctly records both payments; the Summary omits the 50 gp delivery payment.

**Suggested fix:** Add a line to the **Summary** noting that Sildar paid the promised **50 gp escort fee** at breakfast in addition to the negotiated 100 gp advance for the new tasks.

---

## ISSUE 8 — Zenvon's weapons in combat described as "dagger and scimitar"; his build uses scimitar and short sword as the primary Nick pair

**Location:** Scenes — The Redbrand Ambush ("striking with his dagger and scimitar before repositioning")

**Issue:** The recap has Zenvon fight with a dagger and scimitar. Per his combat profile, his Nick mastery build uses **scimitar + short sword** as the primary dual-wield pair. He does carry a dagger, but the Nick property (which is the mechanical core of his Level 2 build) applies to the scimitar + short sword combination. Using "dagger and scimitar" is not impossible, but it misrepresents his established fighting style and the weapon masteries he took at Level 2.

**Evidence:** `world_state` Zenvon combat profile: *"Weapons: Scimitar (Nick mastery), Short Sword, Dagger, Javelin... Nick property lets the second light-weapon attack land without spending the bonus action."* The Nick build is explicitly scimitar + short sword.

**Suggested fix:** Change the combat description to **"scimitar and short sword"** to reflect his actual weapon mastery build. The dagger can be noted as a backup weapon but should not be his primary off-hand in a combat sequence.

---

## ISSUE 9 — Magic Missile attributed to "Vera" is consistent with Veyra's spell list, but the Spells section does not note this is a sidekick spell

**Location:** Spells — Magic Missile

**Issue:** This is a minor documentation concern rather than an error: the Spells section records Magic Missile as cast by "Vera" (already flagged as the wrong name — see Issue 1). Once the name is corrected to Veyra, the spell attribution is accurate. However, future session notes should be aware that Magic Missile is on **Veyra's** spell list, not available to any other party member, so attributing it correctly to Veyra (not Zenvon, Pip, or Maela) is important for ongoing continuity.

**Evidence:** `world_state` party roster: *"Veyra — Tiefling spellcaster | Firebolt, Magic Missile."* No other party member has access to this spell.

**Suggested fix:** Correct the name to **Veyra** (see Issue 1). No further change needed once the name is fixed.

---

## ISSUE 10 — "Sister Maela Dawnforge" surname not attested in campaign documents

**Location:** NPCs — Sister Maela Dawnforge

**Issue:** The recap gives Sister Maela the surname **"Dawnforge,"** which does not appear anywhere in the campaign documents. The character is referred to throughout both context documents simply as **"Sister Maela"** or **"Maela."**

**Evidence:** `world_state` party roster and throughout: *"Sister Maela — Sidekick (DM-run) | Dwarf cleric."* No surname is given in any context document.

**Suggested fix:** Either confirm "Dawnforge" as an established surname with the DM, or remove it and refer to the character as **"Sister Maela"** until a surname is canonically established.

---

## SUMMARY OF ISSUES

| # | Severity | Section | Issue |
|---|---|---|---|
| 1 | **High** | All | "Vera" should be "Veyra" throughout |
| 2 | **Medium** | All | "Toblin" should be "Toblen" throughout |
| 3 | **High** | Summary, Scenes, NPCs | "Elmar the barkeep" should be "Elsa" |
| 4 | **Medium** | Summary, NPCs | Tuck presented as adult; he is Toblen's 9-year-old son |
| 5 | **Low** | Summary, NPCs | Sildar's role and apparent wealth slightly overstated |
| 6 | **Medium** | Scenes, Locations | "Evil mercenary wizards" is unsupported; internal inconsistency on the Pact's destruction |
| 7 | **Low** | Summary | 50 gp escort payment omitted from Summary; present in Scenes |
| 8 | **Medium** | Scenes | Zenvon fights with dagger+scimitar; should be scimitar+short sword (Nick build) |
| 9 | **Low** | Spells | Name fix only; spell attribution itself is correct once name is corrected |
| 10 | **Low** | NPCs | "Dawnforge" surname for Maela is unattested; confirm or remove |