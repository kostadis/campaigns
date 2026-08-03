## Consistency Report — New Chapter 3 (2025-05-28 Dwarven Excavation Session)

---

### CRITICAL — Character Identity / Class Errors

**Location:** Summary, Memorable Moments, Scenes, Spells

**Issue:** The tortle character is called **"Sema"** throughout, and is described as **"the tortle barbarian."**

**Evidence:** All campaign documents (world_state.md, party.md, campaign_state.md) name this character **Soma**, not Sema. The VTT corrections table explicitly lists "Sema → Soma." More critically, **Soma is a Druid (Circle of the Moon)**, not a Barbarian. The Barbarian is **Brewbarry** (Goliath). Soma using she/her pronouns (party.md: "She is patient, maternal…") — the recap uses "him/his" for her throughout.

**Suggested fix:** Replace all instances of "Sema" with "Soma." Remove "tortle barbarian" label; she is the "tortle druid." Correct pronouns to she/her. The rage, fury, and crushing fist blow attributed to the "tortle barbarian" in the Summary likely belong to Brewbarry and should be re-attributed accordingly.

---

### CRITICAL — NPC Name Error (Recurring)

**Location:** Summary, Scenes, NPCs section, Items section, Spells section

**Issue:** One of the two dwarf archaeologists is called **"Dazzleglim"** throughout the recap. This name does not exist in the campaign.

**Evidence:** campaign_state.md: "Warning delivered to **Dazlyn Grayshard** and Norbus Ironrune." NPC table: "**Dazlyn Grayshard** | Alive | Ancient dwarven ruins SW of Phandalin." entity_registry.yaml: "**Dazlyn Grayshard** — Shield dwarf prospector and business partner of Norbus; forthright and honest to a fault." The VTT corrections table maps "Dazzlyn, Dazzlin, Dazzledan, Dazzlen, Dazlin → Dazlyn." "Dazzleglim" is not a misspelling variant — it is a different invented name.

**Suggested fix:** Replace every instance of "Dazzleglim" with "Dazlyn Grayshard" (or "Dazlyn" for short). Per campaign_state.md, it is specifically Dazlyn who offered the sending stones.

---

### HIGH — Invented NPC / Wrong Quote Attribution

**Location:** Memorable Moments

**Issue:** The quote `"We found 10." — Felkur` is attributed to a character named **"Felkur,"** who does not appear anywhere in the campaign documents.

**Evidence:** The Summary states: "**Valfine** quietly suggested they had found only ten." No NPC or PC named Felkur exists in campaign_state.md, world_state.md, party.md, or entity_registry.yaml.

**Suggested fix:** Attribute the quote to **Valphine** (correcting the spelling from Valfine). Remove "Felkur" entirely.

---

### HIGH — Chapter Number Mismatch

**Location:** Recap header / campaign timeline

**Issue:** The recap is labeled **"New Chapter 3,"** but the campaign state places the Dwarven Excavation at **Chapter 2**.

**Evidence:** campaign_state.md NPC entry: "Dazlyn and Norbus were present at the Dwarven Excavation **(ch2)**." The canon events timeline lists Ch03 as "Gnomengarde; King Korboz's madness. Shapeshifter incidents" — a completely different session.

**Suggested fix:** Relabel the session **Chapter 2** to match campaign_state.md. Verify against session transcripts before committing.

---

### HIGH — Spell Misattribution (Thunderwave)

**Location:** Scenes ("Battle with the Ochre Jellies"), Spells section

**Issue:** **Thunderwave** is attributed to **Vukadin (Vukradin)**.

**Evidence:** world_state.md lists Thunderwave explicitly under **Valphine's** key spells: "Sacred Flame, Fairy Fire, Spirit Guardians, Guiding Bolt, Daylight, Doom Sphere, Zone of Truth, **Thunderwave**." Vukradin's key spells are listed as "Bardic Inspiration, Vicious Mockery, Universal Speech, Command, Hold Person, Silence, Spray of Cards" — Thunderwave is absent. While Thunderwave is technically on the Bard list, the campaign's own documented spell attribution puts it on Valphine.

**Suggested fix:** Re-attribute Thunderwave to **Valphine**. Verify against session transcript before changing.

---

### HIGH — Mechanical Error (Dissonant Whispers vs. Ochre Jelly)

**Location:** Summary, Scenes ("Battle with the Ochre Jellies"), Spells section

**Issue:** Dissonant Whispers is described as forcing an ochre jelly to "recoil in psychic agony and flee." This is mechanically impossible under standard 5e rules.

**Evidence:** Ochre Jellies (Monster Manual) have condition immunity to **Frightened**, among other conditions. Dissonant Whispers works by imposing the frightened condition and forcing movement. An ooze with frightened immunity cannot be affected. Either the GM ruled differently (which should be noted), or the spell used was something else.

**Suggested fix:** If this was a GM ruling, add a note clarifying it was a house rule. If the spell was misidentified, review the transcript to determine what was actually cast.

---

### MEDIUM — Recurring PC Name Misspellings

**Location:** Summary, Scenes, Spells (multiple instances)

**Issue:** Three PC names are misspelled throughout the recap.

**Evidence:**
- "Vukadin" → correct name is **Vukradin** (VTT corrections: "Vukadin → Vukradin")
- "Valfine" → correct name is **Valphine** (VTT corrections: extensive alias list)
- "Brewberry" → correct name is **Brewbarry** (VTT corrections: "Brewberry → Brewbarry")

**Suggested fix:** Global search-and-replace: Vukadin → Vukradin, Valfine → Valphine, Brewberry → Brewbarry.

---

### MEDIUM — Wrong Pronoun for Brewbarry

**Location:** Summary ("Brewberry swung her halberd")

**Issue:** The recap uses **"her"** for Brewbarry.

**Evidence:** party.md uses he/him pronouns throughout Brewbarry's entry: "He measures everything in contests… He does not experience his exile as injustice." Brewbarry is male.

**Suggested fix:** Change "Brewberry swung her halberd" to "Brewbarry swung his halberd."

---

### MEDIUM — Wrong Pronoun for Soma

**Location:** Summary, Scenes, Memorable Moments ("Sema withdraws into his shell," "revive him," etc.)

**Issue:** The recap uses **"him/his"** for Soma throughout.

**Evidence:** party.md: "By tortle standards, Soma is old. **She** is patient, maternal, dry-witted."

**Suggested fix:** Replace he/him/his with she/her when referring to Soma.

---

### MEDIUM — Internal Contradiction (Who Shouted the Archaeological Warning)

**Location:** Memorable Moments vs. NPCs section

**Issue:** The archaeological preservation warning quote is attributed to **"Norbus"** in Memorable Moments, but the NPCs section says **"Dazzleglim"** (Dazlyn) shouted the same type of warning during combat.

**Evidence:** Memorable Moments: `"Could you not use such damaging spells?" — Norbus`. NPCs section (Dazzleglim): "He shouted warnings during the battle, urging the party not to damage the interior of the archaeological site." These describe the same behavior but assign it to different dwarves.

**Suggested fix:** Assign the quote to one dwarf consistently. The entity registry describes Dazlyn as "forthright and honest to a fault" and Norbus as "gruff and excessively cautious" — review the transcript to confirm the speaker, then correct either the Memorable Moments attribution or the NPCs section description.

---

### LOW — Spell Not in Vukradin's Documented Kit (Starry Wisp)

**Location:** Spells section

**Issue:** **Starry Wisp** is attributed to Vukradin ("Vukradin"). It is not listed among his key spells in any campaign document.

**Evidence:** world_state.md lists Vukradin's key spells as "Bardic Inspiration, Vicious Mockery, Universal Speech, Command, Hold Person, Silence, Spray of Cards." Starry Wisp (2024 PHB) does not appear. While it is on the Bard list, its use has not been previously documented for this character.

**Suggested fix:** Verify against the session transcript. If confirmed, add Starry Wisp to Vukradin's documented spell list; if it was actually Valphine's Sacred Flame, correct the attribution.

---

### LOW — Vukradin's Weapon (Daggers)

**Location:** Summary, Memorable Moments, Scenes

**Issue:** Vukradin kills two jellies with a "swift double-dagger strike." Daggers are not listed among his items in any campaign document.

**Evidence:** world_state.md lists Vukradin's items as: "Lute/flute, rapier, sending stones, Boots of Elvenkind…" party.md confirms: rapier, flute, no daggers. Because this is Chapter 2/3 and the party documents reflect Chapter 45 state, item loadout may have changed — but daggers as a combat signature is inconsistently supported.

**Suggested fix:** Flag for GM verification. If Vukradin had daggers at this point in the campaign, note it. If the killing blows were made with his rapier, correct the weapon description.

---

### LOW — Ambiguous Gem Attribution at Hall of Greed

**Location:** Locations ("Hall of Greed"), Scenes, Items

**Issue:** The recap describes the gem in the statue's hands as either "a priceless emerald or an elaborate piece of glass" — value left unresolved. The entity_registry entry flags the Hall as "containing a **trapped** statue," but no trap is described or triggered.

**Evidence:** entity_registry.yaml (E11): "Sealed chamber containing a **trapped** statue of a horned dwarf holding a glowing green gem." campaign_state.md: "Hall of Greed trap NOT FOUND IN SUMMARIES."

**Suggested fix:** Add a GM note to confirm whether the trap was bypassed, disarmed, or omitted from the session. This affects whether future sessions can assume the statue trap has been dealt with.