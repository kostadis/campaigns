I need no preamble — here is the consistency report.

---

## Consistency Report — Chapter 47: Neverwinter, Never a Dull Moment

---

### ISSUE 1 — Lord Cassian identified as Elara's **brother**; campaign state identifies him as her **cousin**

- **Location:** Summary (multiple occurrences), Scenes ("Meeting Lord Cassian"), NPCs ("Lord Cassian Meliamne"), Items ("Meliamne Family Statue")
- **Issue:** The recap repeatedly calls Cassian "Elara's brother" (e.g., "She directed the party to Lord Cassian, Elara's brother"; "the grieving brother of the late Lady Elara"). The scene transcript confirms this framing as well.
- **Evidence:** `campaign_state.md` NPC table lists Cassian as: *"Elara's cousin; carries her anti-Margaster case; active contact for mermaid statue and necklace provenance."* The entity registry entry for Cassian reads: *"NPC who gives the party a description of Bimble Nackle that will make players assume it is KP"* — no "brother" framing. `neverwinter_network.md` explicitly: *"Sea elf, Elara's **cousin**…"* The Moonstone Mask staff member's dialogue as quoted in the Scenes section says *"even if her **brother** did want to raise her"* — this is either a misattribution (Cassian is cousin, not brother) or the staff member was mistaken in-fiction. The active obligations bullet in `campaign_state.md` states: *"Return mermaid statue to Lord Cassian Meliamne (Elara Meliamne's **cousin**…)"*
- **Suggested fix:** Replace "brother" with "cousin" throughout the recap (Summary, all Scene sections, NPCs section, Items section). If the staff member said "brother" in the VTT, note that as an in-world ambiguity or staff error rather than canon — Cassian's correct relationship per campaign state is cousin.

---

### ISSUE 2 — Planar Manifold referred to inconsistently as "Planar Manifold," "displacement manifold," and "Planar Manifold"

- **Location:** Summary, Scene "The Return of the Meliamne Statue and a New Quest," NPCs ("Lady Elara Meliamne"), Locations ("Neverwinter Docks")
- **Issue:** The device is called "the Planar Manifold" in the Summary and NPCs section, but "displacement manifold" in the Scenes section. The entity registry uses **Displacement Manifold** as the canonical name.
- **Evidence:** `entity_registry.yaml` entry: *name: Displacement Manifold, type: location, note: "Planar routing device built and operated by the Commission at Neverwinter's docks…"* The `vtt_transcription_corrections.md` and `neverwinter_network.md` also use "Displacement Manifold." The `gm-assist.md` for this same session uses "displacement manifold" in scene text and "Planar Manifold" in the Summary — this inconsistency originates in the gm-assist itself.
- **Suggested fix:** Standardize to **Displacement Manifold** throughout the recap, consistent with the entity registry. The Summary and NPCs sections should be updated; the Scenes section is already correct.

---

### ISSUE 3 — "Brewberry" used throughout instead of "Brewbarry"

- **Location:** Summary (multiple), Memorable Moments, Scenes (multiple), NPCs ("Moonstone Mask Staff Member")
- **Issue:** The recap consistently spells the character's name as "Brewberry." The canonical spelling is **Brewbarry**.
- **Evidence:** `vtt_transcription_corrections.md` explicitly lists "Brewberry" as a **wrong** transcription form and maps it to **Brewbarry**. The party document, character sheet, and entity registry all use Brewbarry. The player's character is Brewbarry Root Smasher Ogalakadu.
- **Suggested fix:** Global find-and-replace "Brewberry" → "Brewbarry" throughout the document. (Note: the gm-assist.md source also uses "Brewberry" — this error propagated from there.)

---

### ISSUE 4 — Autograph name spelled "Alducia" in Memorable Moments, contradicts "Aldusia" in VTT corrections

- **Location:** Memorable Moments ("Aldus's invented daughter"), Summary ("stammered out 'Aldusia'")
- **Issue:** The Summary text says Aldus invented the name *"Aldusia"* while the Memorable Moments section spells it *"Alducia."* The VTT corrections document lists "Aldousia" as a wrong form and maps it to **Alducia**.
- **Evidence:** `vtt_transcription_corrections.md`: *"Aldousia → Alducia."* The NPCs section spells it "Alducia." The Items section ("Vukradin's Autograph") says *"To Alducia."* The Summary body text says *"Aldusia."* The gm-assist.md Summary also uses "Aldusia."
- **Suggested fix:** The canonical form per the VTT corrections table is **Alducia**. Correct the Summary's single instance of "Aldusia" to "Alducia" to match the rest of the document and the corrections table.

---

### ISSUE 5 — Prutha described as "a former party member" who has departed; campaign state confirms departure but specifies destination and consequence

- **Location:** NPCs ("Prutha"), Summary ("Prutha is confirmed to have departed on a crusade to convert orcs")
- **Issue:** This is correct but incomplete in a way that could confuse future sessions. The recap says Prutha "departed on a crusade to convert orcs" and is "no longer traveling with the group." Campaign state places Prutha specifically at **Icespire Hold** on a missionary mission to convert Vorga's orcs to Valphine's Lathanderite faith — he is not wandering, he has a named mission and location.
- **Evidence:** `campaign_state.md` NPC table: *"Prutha (orc Lathandrite) | Alive | With party at Woodland Manse"* — note this is the ch45 state. The Party Current Situation bullet: *"Prutha and five orc converts also present [at Icespire Hold], on a missionary campaign to convert Vorga's orcs to Valphine's Lathanderite faith."* `world_state.md` also places him at Icespire Hold as of ch46.
- **Suggested fix:** Clarify the NPCs entry: Prutha is not merely "on a crusade" in an unspecified direction — he is at **Icespire Hold** with five orc converts, on a mission to convert Vorga's tribe. The Summary's scene note ("that will have consequences") is accurate and can be retained.

---

### ISSUE 6 — Party described as arriving with Cryovain hoard obligation unmentioned; "Vukradin insisted no payment necessary" matches existing characterization but the stat on the reward is ambiguous

- **Location:** Scenes ("The Return of the Meliamne Statue and a New Quest"), NPCs ("Lord Cassian Meliamne")
- **Issue:** Lord Cassian rewards the party with *"50 gold pieces each."* The gm-assist.md says only *"gold pieces each"* without specifying 50. The recap specifies 50 gp per companion. This is not directly contradicted but also not confirmed by any campaign state document — it is a session-generated detail. If this number is wrong it will affect party finances going forward.
- **Evidence:** No grounding document specifies the reward amount. The gm-assist.md summary does not give a figure.
- **Suggested fix:** Flag as **unverified detail** — confirm the 50 gp figure against the VTT transcript before it enters party finances tracking. Not necessarily wrong, just not confirmed by any existing document.

---

### ISSUE 7 — Inviting the crowd to "the Church of Lathander" vs. "Spire of the Morninglord"

- **Location:** Scenes ("Meeting Lord Cassian and a Musical Performance"), Summary
- **Issue:** In the Scenes section the party invites the crowd to *"a future performance and sermon at the Church of Lathander,"* but everywhere else in the recap (Summary, Locations, Memorable Moments) the temple is consistently called *"the Spire of the Morninglord."* These appear to be the same location, but the naming is inconsistent within the document. The Scenes text likely reflects a VTT transcription rendering.
- **Evidence:** The Locations section entry is titled "Spire of the Morninglord" — a Lathander temple in Neverwinter. The Summary, Memorable Moments, and Summons scene all use "Spire of the Morninglord." "Church of Lathander" does not appear in any campaign grounding document as a named Neverwinter location.
- **Suggested fix:** Change "Church of Lathander" in the Scenes section to **"Spire of the Morninglord"** to match the established name used throughout the rest of the recap and the Locations entry.

---

### ISSUE 8 — Character levels listed inconsistently between party document and recap framing

- **Location:** (Background context issue, not in recap body, but relevant to continuity)
- **Issue:** The `party.md` document lists characters at **level 7** (Barbarian 6, Druid 6, Cleric 6, Bard 6 in the character sheet entries — but the co-GM prep doc `20260623_neverwinter_vukradin_present.md` explicitly states *"Player level: 7."*) The campaign state and party doc show Level 6 in the character sheets. The Phandalin CLAUDE.md lists all characters as **Bard 5 / Druid 5 / Cleric 5 / Barbarian 5**. This is not a recap error per se, but the recap does not mention levels — however if any mechanical claims are added, they may hit the wrong level.
- **Evidence:** `CLAUDE.md` (Phandalin): *"Vukradin | Bard 5 / Aasimar"*, *"Soma | Druid 5 / Tortle"*, etc. `party.md` character sheets show Barbarian 6, Cleric 6, Druid 6, Bard 6. Prep doc says level 7. Three different numbers in three different documents.
- **Suggested fix:** Reconcile the level discrepancy in the grounding documents. The party.md sheet entries (level 6) are most recently updated; the CLAUDE.md appears to be out of date (pre-leveling). Flag for the GM to confirm current level before any mechanical session prep relies on it.

---

### ISSUE 9 — Recap describes Valphine's insight revealing audience reaction; attributes this to *Valphine's eyes glowing with Lathander's light*, but perception check mechanism is ambiguous

- **Location:** Summary ("Valphine — her eyes now glowing with the golden light of Lathander — could see through the polished veneer"), Scenes (Valphine's insight check)
- **Issue:** Minor flag. The recap frames Valphine's social perception as tied to her glowing eyes (a Lathander manifestation), while the Scenes section correctly notes it was an **Insight check** roll. These are not contradictory, but the Summary's framing implies divine sight rather than a skill check, which could set a precedent for future sessions that this is a passive ability rather than a rolled one.
- **Evidence:** `world_state.md` Valphine's stat block does not list any passive golden-eye divine-insight feature. Her spells include Insight expertise (+10 from party.md) — this was almost certainly a skill check. The Scenes section correctly notes "Valphine's insight check."
- **Suggested fix:** Clarify in the Summary that the golden-eyed perception is narrative flavor on top of a **rolled Insight check**, not a new passive divine ability. Low priority but worth noting for voice consistency.

---

### NO ISSUE FOUND

The following elements in the recap are consistent with campaign documentation:
- Elara Meliamne's death (confirmed canon, `campaign_state.md` NPC table, `entity_registry.yaml`)
- House Margaster's involvement in Elara's death (confirmed canon, `neverwinter_network.md`)
- The Displacement Manifold going dark approximately seven weeks prior (consistent with campaign state)
- Cullen Sharpe's name, faction, and behavior (confirmed canon, `neverwinter_network.md`, ch47 canon status)
- Aldus as a steward of Lord Neverember (consistent with prep docs; Aldus Hern is the name in the prep doc — recap uses "Aldus" alone, which is acceptable)
- The Moonstone Mask's description (earthmote, moonstone masks, staff dress) matches entity registry and prep docs
- The Spellplague of 1385 as the origin of the earthmotes (confirmed, entity registry)
- Boney's presence with the party and the fact that he "doesn't poop" / need stabling (consistent with party.md and world_state.md)
- Vukradin's fame being for early work rather than current exploits (consistent with prep docs)
- The Candlekeep Report reference and dragon-comparison framing for Neverember's concerns (consistent with prep docs)
- Lord Neverember's title (Lord Protector of Neverwinter) (confirmed, entity registry)
- The Common Chord as a former low-end venue now Neverwinter's most exclusive (consistent with prep docs)
- The Lionshield Coster as primary client of the Displacement Manifold (confirmed, campaign state)
- The gnome technician described but unnamed (consistent with `neverwinter_network.md`'s Bimble Nackle guardrail — name withheld correctly)
- Cassian's "She was 12 when she last saw this" quote (consistent with gm-assist.md)
- The 200 gp bribe paid by Cassian to Cullen Sharpe (consistent with gm-assist.md)
- The party's planned next stop being the counting house with a letter of recommendation (consistent with campaign state active obligations)