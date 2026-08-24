# Consistency Report — "New Chapter 4" (session 2025-06-03)

This recap is early-campaign backfill material (orc attack at the excavation canyon → first ogre → Phandalin → second ogre cliffhanger). Checked against AUTHORITATIVE CANON (entity registry), campaign_state, world_state, party doc, and the adjacent narrative chapters 3–5.

---

## 1. "Valpine" and "Valfina" are the same character, spelled two different wrong ways

- **Location:** Summary, Memorable Moments, Scenes, Spells (throughout)
- **Issue:** The cleric appears as **"Valpine"** (heals Vukradin, mace, hand crossbow) and **"Valfina"** (knocked out by Ice Knife, "turtle elf" target) — two divergent garbles of one PC. A future reader could parse them as two different characters, one of whom knocked the other out.
- **Evidence:** **AUTHORITATIVE CANON:** the registry's canonical entry is **Valphine** (aliases "Valphine Sotorra/Sortorra"). The VTT corrections glossary lists both "Valpine" and "Valfina" as known wrong-forms → Valphine.
- **Suggested fix:** Normalize every instance to **Valphine**.

## 2. "Brewberry" → Brewbarry

- **Location:** Summary, Scenes, Items (throughout)
- **Issue:** The goliath's name is misspelled consistently.
- **Evidence:** **AUTHORITATIVE CANON:** registry entry is **Brewbarry**. Glossary lists "Brewberry" as a wrong-form.
- **Suggested fix:** Global replace with **Brewbarry**.

## 3. "Dazlin" → Dazlyn (Grayshard)

- **Location:** Summary, Scenes, Locations, NPCs
- **Issue:** Dwarf's name misspelled; also both dwarves are described as "miners."
- **Evidence:** **AUTHORITATIVE CANON:** registry has **Dazlyn Grayshard** ("shield dwarf **prospector**") and **Norbus Ironrune** ("prospector"). Glossary: "Dazlin" is a wrong-form. ("Norbus" is spelled correctly.)
- **Suggested fix:** "Dazlyn" everywhere; prefer "prospectors" over "miners."

## 4. Chapter number / date does not fit the existing chapter sequence

- **Location:** Title ("New Chapter 4") and date line (2025-06-03)
- **Issue:** This recap's content ends mid-fight with the mountain-pass ogre — exactly where the existing `chapter_03_to_find_a_shapeshifter.md` **opens** (§03.01: ogre prone, flees, killed by Vukradin, whistle/coins/key looted). So these events *precede* chapter 3's narrative, yet the recap is labeled Chapter 4 — and a chapter 4 already exists ("The Bard, the Kings, and the Carver") covering entirely different events (mimic fight, the two kings, bandits). The date is also suspect: the corrections log dates the chapter-3 session to **2025-05-28**, and the registry's "Orcanese" entry places "Do you speak Orcanese?" (which fits this recap's orc parley) in that 2025-05-28 session.
- **Evidence:** chapter_03 §03.01–03.02; chapter_04 contents; entity registry "Orcanese" note; vtt_known_additions 2026-08-02 entry.
- **Suggested fix:** Human checkpoint before this recap is filed: verify against `summaries/` which session this transcript actually is, and renumber/redate so it slots *before* the existing chapter 3 content rather than colliding with chapter 4.

## 5. Spells section conflates the two ogres

- **Location:** Spells (Sacred Flame, Thorn Whip, Mold Earth)
- **Issue:**
  - **Sacred Flame** — "later used against the **whistling ogre** while it was incapacitated." The whistling ogre was never incapacitated; the *Hungry Ogre* in the mountain pass was (walloping ammo + Command).
  - **Mold Earth** — entry says the rockfall attempt happened "during the **mountain pass** ogre fight," but the Scenes section places it in the **whistling ogre** fight ("Soma attempts to use magic to loosen the terrain… settles for another blast of toxic mist").
  - **Thorn Whip** — "used again to attempt to pull the whistling ogre across the battlefield" appears in no scene bullet; likely conflation.
- **Evidence:** Recap-internal contradiction between Scenes and Spells sections.
- **Suggested fix:** Verify against transcript; align each spell entry with the correct ogre encounter.

## 6. First-ogre placement conflicts with campaign_state (probably campaign_state's drift, not the recap's)

- **Location:** Summary ¶3 / Scene "The Whistling Ogre"
- **Issue:** The recap puts the first (whistling) ogre on the road **to Phandalin**, *before* the Gnomengarde quest was even received. `campaign_state.md` labels it "**Frozen** Ogre Encounter (**en route to Gnomengarde**, first ogre)."
- **Evidence:** The recap's internal ordering (ogre → Phandalin → quests → Gnomengarde road) is coherent, and chapter_03 §03.01 corroborates the recap's second-ogre details (fled, killed by Vukradin, whistle/coins/key — matching campaign_state's *second*-ogre entry). Note also the "Frozen Ogre" label fits neither ogre in the recap — the only "frozen" ogre is the second one (frozen by Command). campaign_state is a generated/hand-edited grounding doc; the recap derives from the session itself.
- **Suggested fix:** Don't alter the recap's geography without checking the transcript; if the recap holds up, correct campaign_state's "en route to Gnomengarde / Frozen" labeling on the first ogre instead.

## 7. "Killed his brother" vs. "one of its kind"

- **Location:** Memorable Moments vs. Summary ¶5 / Scene "Ambush in the Mountain Pass"
- **Issue:** The Memorable Moment says Vukradin boasted they had killed the ogre's **brother**; the Summary and Scene say he claimed they had slain "one of its kind" / "another ogre recently." Internal inconsistency — "brother" is a stronger, unverified claim.
- **Suggested fix:** Verify the actual line; standardize on one phrasing.

## 8. "I eat turtle elf" glossed as "specifically targeting Valfina"

- **Location:** Memorable Moments
- **Issue:** The gloss attributes the threat to Valphine alone. But **Soma is the tortle** and Valphine is the (drow) elf — "turtle elf" most naturally points at Soma, or at both PCs as a mashup. Attributing it to Valphine alone is a precision/attribution risk.
- **Evidence:** party.md (Soma: Tortle Druid; Valphine: Drow Elf Cleric).
- **Suggested fix:** Verify against transcript; reword the gloss (e.g., "apparently referring to Soma and/or Valphine").

## 9. Sending Stones "moral provenance" claim is suspect

- **Location:** Items — Sending Stones
- **Issue:** Entry says Vukradin "debates whether they could have been obtained through dishonorable means." The stones were the dwarves' legitimate reward for the excavation quest, and shortly after this session Vukradin proudly cites them as his wealth — no shame attached.
- **Evidence:** campaign_state ("Dazlyn offered sending stones in lieu of monetary payment… delivered as the reward"); chapter_04 §04.02 ("I am rich! I have sending stones!"). His blood-money concerns in this session were about the **orc loot**.
- **Suggested fix:** Verify transcript; likely reassign the moral-provenance debate to the orc loot and describe the stones simply as the dwarves' reward.

## 10. Clarinet and trumpet are unattested; recap contradicts itself on the instrument

- **Location:** Summary ¶1/¶4, Memorable Moments, Items — Clarinet; vs. Scene "Return to the Excavation Site"
- **Issue:** The recap has Vukradin owning a clarinet and a trumpet and performing on clarinet at the Stonehill Inn — but the Scenes section has him playing a **flute** for the dwarves, and every grounding doc attributes only **lute/flute** to him. Not impossible early-campaign, but internally inconsistent and unattested elsewhere.
- **Evidence:** world_state/party.md ("Lute/flute"; "Flute (instrument)").
- **Suggested fix:** Check the transcript for what was actually said in the "reeded instrument or brass" line and at the inn; reconcile the Items entry with the excavation flute scene.

## 11. Harbin's quote is garbled

- **Location:** Memorable Moments
- **Issue:** "I'm far too thin **and body** to make a good meal" is not English — almost certainly a transcription garble of "too thin **and bony**."
- **Suggested fix:** "…far too thin and bony to make a good meal."

## 12. Command's caster is never named

- **Location:** Summary ¶5, Scenes, Spells — Command
- **Issue:** "A divine command/decree" halts the ogre, caster unattributed. Both candidates exist: Valphine (the divine caster, present in the fight) and Vukradin (world_state lists Command among his signature spells). Leaving it ambiguous invites future misattribution.
- **Suggested fix:** Name the caster after checking the transcript (context — "divine," alongside her walloping-bolt shot — suggests Valphine).

## 13. Gnomengarde quest purpose understated

- **Location:** Scene "Return to Phandalin"
- **Issue:** Quest described as "investigating rock gnomes at Gnomengarde." The actual commission was to obtain a magical device/item to use against the dragon.
- **Evidence:** campaign_state ("Gnomengarde Quest — obtain magic item(s) from gnomes"); chapter_03 §03.03 ("the mayor is looking for some kind of magical device that can help fight against the threat of the dragon").
- **Suggested fix:** "…retrieving a magical device from the rock gnomes of Gnomengarde to help against the dragon."

## 14. Linene's trade-route disruption — possible anachronism (verify)

- **Location:** Summary ¶4, Locations/NPCs — Lionshield Coster / Linene
- **Issue:** The Lionshield supply-chain disruption is first documented at ch17 in the canon timeline; if the transcript for this early session doesn't actually contain it, this is later knowledge bleeding backward into an early recap.
- **Evidence:** world_state Canon Events Timeline ("Ch17 | Lionshield Coster's interdimensional supply chain noted as disrupted").
- **Suggested fix:** Verify against the session transcript. If Linene did say it, keep it (it would be a legitimately early seed of the Manifold thread); if not, cut it.

---

## Minor notes

- **Linene "proprietor"** (NPCs): canon describes her as *master of the Lionshield Coster's Phandalin post* — she manages the outpost of the Yartar-based Lionshields, she doesn't own it. (Registry — AUTHORITATIVE CANON.)
- **Greataxes vs. battle axes:** orcs attack with greataxes in the scenes, but the loot list says "battle axes." Verify which was looted.
- **Norbus "encouraging":** registry characterizes him as "gruff and excessively cautious." Not a contradiction of fact, but note the tonal drift if his portrayal matters later.
- **"Each time pulled back… by Valpine's divine healing":** the scenes show only one Healing Word; the second recovery is unshown. Confirm whether both revivals were hers.
- **Starry Wisp (Vukradin):** appears in no grounding doc. Plausible for a low-level Eloquence bard and the docs' spell lists are late-campaign, so not flagged as an error — but worth a transcript spot-check since "luminous magical projectile" is doing the identification work.

## Clean

Harbin Wester (50 gp reward, cowardice, "his lordship" = Neverember), Toblen Stonehill, the walloping ammunition's provenance (first ogre) and use (Valphine's hand crossbow), the Ice Knife friendly-fire incident (corroborated by Valphine dodging Soma's Ice Knife range in chapter_03 §03.06), the E1 canyon setting for the orc attack, and the open-ended cliffhanger (ogre incapacitated, not killed — correctly *not* claiming the kill that happens in chapter 3) all check out against canon and the grounding docs.