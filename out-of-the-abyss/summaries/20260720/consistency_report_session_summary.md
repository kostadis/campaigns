# Consistency Report — Chapter 59: The Key Is Secured

---

## Issue 1 — Helmed Horror Count (Internal Inconsistency + Campaign State Contradiction)

**Location:** Summary, Chaos in Deneir's Sanctum scene, NPCs (Helmed Horrors), vs. Locations (Deneir's Sanctum)

**Issue:** The Summary, Scenes, and NPCs sections consistently say **three** helmed horrors attacked ("three towering helmed horrors," "Three helmed horrors smashed through the windows and doors"). The Locations section of this same recap contradicts that: "site of the helmed-horror ambush (two ruined suits of armor, one inert key remain)." The campaign_state (Completed Encounters #19) also says "Two helmed horrors came through the windows" and its current-situation paragraph reads "Two ruined helmed horrors."

**Evidence:** Campaign_state §Completed Encounters #19: *"Two helmed horrors came through the windows targeting the inert High Tower key in Daz's pocket; both destroyed."* Current Situation: *"Two ruined helmed horrors and one inert key on the floor with them."* vs. the GM planning doc (20260712): *"the party has just destroyed all three helmed horrors."*

**Suggested Fix:** The GM planning doc and all narrative sections agree on three; the Locations section and campaign_state say two. If three is correct (consistent with planning doc), update the Locations section to "three ruined suits of armor" and flag the campaign_state entry #19 for correction to "Three helmed horrors." If two is correct, revise all narrative references to match. Resolve before the campaign_state is next regenerated.

---

## Issue 2 — Moziqodo's Creature Type (Major Lore Error)

**Location:** Summary, Memorable Moments, Battle in the Domed Rotunda scene, NPCs (Moziqodo), throughout

**Issue:** The recap repeatedly calls Moziqodo a "pit fiend." Pit fiends are CR 20 lawful-evil Baatorian **devils** from the Nine Hells. Moziqodo is described across all campaign documents as Sylvira's **demonspawn son** — a demon from the **Abyss**. The terms are not interchangeable: different planes, different creature types, different alignments, and a CR gap of roughly 15. The GM planning doc explicitly stat-blocks Moziqodo at CR5, AC 15, HP 85 — nothing like a pit fiend. The NPCs section compounds the error by calling him a "pit fiend" while simultaneously describing "abyssal demon resistances," which is self-contradictory (abyssal = Abyss = demon; pit fiend = Nine Hells = devil).

**Evidence:** Entity registry: *"Moziqodo: 'The Beast of Candlekeep'; Sylvira's demonspawn son."* Candlekeep_avowed.md: *"her demonspawn son Moziqodo — the Beast of Candlekeep."* Planning doc (20260712): CR5, AC 15, HP 85 — incompatible with a pit fiend (CR 20).

**Suggested Fix:** Replace all instances of "pit fiend" with the correct creature designation. The recap's own language is closer to the truth when it calls him "the beast," "Sylvira's abyssal spawn son," or "the creature." A neutral descriptor such as "abyssal demonspawn" or simply "the beast" is appropriate and consistent with campaign docs. Remove the phrase "abyssal demon resistances (immune to fire)" from the NPCs section or replace it with a description matching the actual stat block used.

---

## Issue 3 — Who Frightened Moziqodo (Internal Inconsistency)

**Location:** Summary and Memorable Moments vs. Battle in the Domed Rotunda scene

**Issue:** The Summary attributes Moziqodo's frightened condition to Zalthir: *"fixing the pit fiend with such a terrifying display of focused violence that the demon recoiled in fear, unable to advance."* Memorable Moments repeats this: *"first frightening the pit fiend and then stunning it completely."* The Scenes section contradicts this: it is Thorin who lands a **Menacing Attack** (Battle Master maneuver, DC 15 Wis save, which the fiend fails on a 13) that imposes the frightened condition. Zalthir's contribution is the subsequent **Stunning Strike** (ki point), not the fear.

**Evidence:** Battle in the Domed Rotunda scene: *"Thorin adds a Hill Strike attempt… then lands a Menacing Attack — the fiend fails a DC 15 Wisdom save (rolled 13) and is frightened, unable to advance… Zalthir launches a brutal assault… spends a ki point to stun the creature."*

**Suggested Fix:** Correct the Summary and Memorable Moments to attribute the frightened condition to Thorin's Menacing Attack and the stunned condition to Zalthir's Stunning Strike. One suggested revision: *"Thorin's Menacing Attack forced the demon to recoil in fear while Zalthir's Stunning Strike left it helpless."*

---

## Issue 4 — Daz Using Fire Inside Candlekeep (Mechanical Contradiction)

**Location:** Chaos in Deneir's Sanctum scene

**Issue:** The Scenes section states "Daz hurled magical fire and force" during the helmed horror battle in Deneir's Sanctum. Candlekeep's fire-suppression ward is confirmed **active** in this same session — fire erupts and immediately evaporates (confirmed by the Thaumaturgy/fire test later in the session). If the ward prevents fire from burning, Daz's fire spells should have evaporated on cast, producing no damage.

**Evidence:** Locations (Candlekeep): *"Its primary defense is a magical ward that prevents teleportation and suppresses fire within its walls — fire spells erupt briefly then evaporate instantly."* Death of Bookwyrm scene: ward confirmed still active via the fire test.

**Suggested Fix:** Revise to *"magical force"* only (Magic Missile, which is confirmed in the rotunda fight scene). The fire component appears to be an error; Daz's primary damage output in the sanctum fight would have been force-based given the ward.

---

## Issue 5 — "Natural 1 Rescued into a 26" (Mechanically Misleading)

**Location:** The Death of Bookwyrm scene

**Issue:** The recap states Daz "botches it with a natural 1, then with Grygum's help reaches a 26." In 5e, the Help action grants advantage — a reroll from scratch, not an addition to the 1. Guidance (1d4) added to a natural 1 can produce at most ~12. Neither mechanism produces 26 from a 1. The description implies the 1 was retained and transformed, which is mechanically impossible through standard means.

**Evidence:** D&D 5e PHB: Help action grants advantage (new roll); Guidance adds 1d4 to one roll; neither converts a 1 into a 26. No ability on Grygum's sheet or Daz's sheet in party.md enables this.

**Suggested Fix:** Revise the description to reflect the actual mechanic: *"Daz botches an initial attempt (natural 1), but Grygum's Help action lets him reroll — his second attempt comes up strong, totaling 26."* The result (26) is likely correct; the framing is not.

---

## Issue 6 — Thaumaturgy Producing Fire (Wrong Spell)

**Location:** The Death of Bookwyrm scene (Scenes) and Spells section

**Issue:** The Scenes section reads "Grygum casts Thaumaturgy onto a piece of paper; the flame erupts." Thaumaturgy is a cleric cantrip that produces minor sensory/environmental effects (sounds, visual effects, tremors, odors, etc.) — it cannot produce fire. The Spells section hedges with "Thaumaturgy / Firebolt," but Fire Bolt is a wizard/sorcerer cantrip, not a cleric one. Grygum (Life Domain Cleric 8) does not have Fire Bolt in his accessible spell list.

**Evidence:** Party.md: *"Grygum — Cleric 8 (Life Domain)."* PHB Thaumaturgy description: minor effects, no fire production. Fire Bolt is not on the Cleric spell list.

**Suggested Fix:** Replace "Thaumaturgy" with a spell Grygum can access. Sacred Flame (radiant, not fire) won't test the ward. A more likely candidate is a fire-capable item Grygum carries, or the narration should credit a different character (Daz) with testing fire. Alternatively, if the DM ruled Thaumaturgy could produce a small flame for testing purposes, note it as a ruling rather than stating it as the spell's standard function.

---

## Issue 7 — Grygum "Radiating Holy Light That Seared Two Horrors" (Domain Mismatch)

**Location:** Chaos in Deneir's Sanctum scene

**Issue:** The Scenes section states "Grygum radiated holy light that seared two horrors." This reads as an AoE radiant-damage effect against multiple constructs. Life Domain's Channel Divinity is Preserve Life (healing, not damage). Radiance of the Dawn (AoE radiant damage via Channel Divinity) is a **Light Domain** feature, not Life Domain. Turn Undead affects undead only; helmed horrors are constructs and are immune to it.

**Evidence:** Party.md: *"Grygum — Cleric 8 (Life Domain)."* PHB Life Domain: Channel Divinity is Preserve Life; no AoE damage feature listed. Radiance of the Dawn is exclusive to Light Domain.

**Suggested Fix:** Clarify what Grygum actually used. If he cast Sacred Flame twice (one per round), the description should say so. If the DM improvised a domain feature, note it as a table ruling. Revise to avoid implying a Life Domain cleric has AoE radiant Channel Divinity.

---

## Issue 8 — "Bookwyrm's Tower" as an Item in the Sanctum (Ambiguous Reference)

**Location:** The Aftermath of the Sanctum Attack scene, Scroll of Detect Magic item entry, multiple references

**Issue:** The recap repeatedly refers to "Bookwyrm's tower" glowing brightly under Detect Magic in Deneir's Sanctum, with the note it is "even brighter than usual." The Detect Magic scroll was used in Deneir's Sanctum — not in Bookwyrm's actual tower. "Bookwyrm's tower" must therefore refer to a portable magical item (a staff, rod, or focus), but no such item is defined anywhere in party.md, campaign_state, or world_state. This reference is opaque and will confuse future sessions.

**Evidence:** No entry for a "Bookwyrm's tower" item exists in entity_registry.yaml or party.md. Campaign_state and world_state list Bookwyrm's possessions without naming this item.

**Suggested Fix:** Identify what "Bookwyrm's tower" actually is (a staff? a focus Daral was carrying from her office?), and name it explicitly. If it is a building rather than an item, clarify why it registered on a Detect Magic scan in a different room. Add it to the items section with a description.

---

## Issue 9 — Moziqodo's Containment Status (Inaccurate Present Tense)

**Location:** The Death of Bookwyrm scene (Summary and Scenes)

**Issue:** Daz is described as recalling "Sylvira's abyssal spawn son — a creature she keeps locked in a magical sanctuary." The present-tense "keeps locked" implies Moziqodo is still contained at the time of this session. Per the GM planning doc (20260712), Moziqodo had **already escaped** Sylvira's Mordenkainen's Mansion containment before this session opened — his escape is part of A'lai's long-game setup. By this session he is already loose and actively attacking Tadric.

**Evidence:** Planning doc (20260712): *"A'lai orchestrated Moziqodo's escape from Sylvira's Mordenkainen's-Mansion containment from the start — not opportunism, a long game."* Candlekeep_avowed.md: *"her demonspawn son Moziqodo — escaped the Mordenkainen's mansion she'd trapped him in and now stalks rooftops at night."*

**Suggested Fix:** Revise to past tense: *"a creature she had struggled to keep contained"* or *"a creature who had recently escaped the magical sanctuary she'd built to hold him."*

---

## Issue 10 — A'lai Described as Sole "Mastermind" (Incomplete Characterization)

**Location:** Summary (final paragraph), NPCs (A'lai Aivenmore)

**Issue:** The recap describes A'lai as "the architect behind it all," "the suspected mastermind," and states his "likely aim is opening the high tower to obtain a magical artifact of ineffable power." Campaign documents establish A'lai as **Manshoon's inside man** — a highly capable agent, but not the top of the conspiracy chain. Labeling him as the ultimate mastermind in the session document may anchor future prep incorrectly.

**Evidence:** Entity registry: *"A'lai Aivenmore: Great Reader; main antagonist; Manshoon's inside man."* Planning doc (20260712): *"A'lai orchestrated Moziqodo's escape… Manshoon likely ends the night with both keys."*

**Suggested Fix:** This is accurate from the party's in-session perspective (they don't know about Manshoon). Add a GM-note qualifier in the recap or NPCs section, e.g.: *"Suspicion now turned heavily toward A'lai as the architect of this phase of the conspiracy"* — leaving room for the larger principal to surface in Chapter 60+. The specific claim that his aim is "a magical artifact of ineffable power" should also be flagged as party speculation rather than confirmed fact, since campaign docs don't specify this motivation.

---

## Document-Level Note (Campaign State, Not Recap Error)

**Location:** campaign_state.md NPC Current States table

**Issue:** Bookwyrm is listed as *"Alive; Hostile-concealed; performs cooperation, steered investigators wrong"* and the Active Quests section still describes Kalan planning a Zone of Truth challenge against her at the naming ceremony. After Chapter 59, Bookwyrm is dead. The campaign_state claims to be *"Current as of Chapter 61"* but has not been updated to reflect her death or the new key situation (party now holds a fake key + the real key from Tadric).

**Suggested Fix:** Regenerate campaign_state.md post-Chapter 59. Bookwyrm should be moved to the dead NPC table. The Active Quest for the naming ceremony should be updated or closed. The Current Situation should note the party holds both the inert decoy key and the real key secured from Tadric.