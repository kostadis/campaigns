# Consistency Report — Chapter 9 Recap ("Tower of Storms: Heart, Sharks, and Salvage")

**Verdict: multiple errors found.** Two are canonical name errors that will propagate badly if uncorrected (one is an active glossary landmine); several are attribution errors that contradict the authoritative chapter narrative and campaign_state.

---

## Critical — Name Errors (canon-backed)

### 1. "Meryl" is wrong everywhere — the sea elf spirit is **Miraal**
- **Location**: Summary, Memorable Moments, Scenes ("The Spirit's Departure…"), NPCs ("Meryl"), Items ("Opalescent Conch"), Locations ("Leilon")
- **Issue**: The recap names the sea elf spirit "Meryl" throughout. This rests on the **AUTHORITATIVE CANON** entity registry: the banshee of the Tower of Storms is **Miraal** ("Sea elf slain by Moesko; her spirit haunts the Haunted Cave as a banshee, seeking return of her opalescent conch"). This is not merely a spelling drift — it is a **fusion landmine**:
  - The VTT glossary maps `meryl, Merrill, Mariel → **Meril**` — and **Meril is a different entity**: Soma's dead druid mentor (registry: "Meril", "Meril's Staff"). A future spell pass applying the glossary to this recap would silently convert the banshee into Soma's mentor.
  - Canon explicitly marks the pair as distinct: `rejected_aliases` contains `[Meril, Miral]`. Two entities canon marks as confirmed distinct must never be merged.
- **Evidence**: Canon registry (Miraal entry; Meril entry; rejected_aliases). Corroborated by campaign_state ("Banshee Miraal Encounter (area T1): Opalescent conch returned; Miraal's spirit laid to rest").
- **Suggested fix**: Replace every "Meryl" with **Miraal**. Rename the NPC entry. Do this before any glossary-driven cleanup touches this file.

### 2. "Starchloros Lover" → **Star-Crossed Lover**
- **Location**: Summary, Scenes ("Salvage in the Shark-Infested Depths"), Locations ("Shipwreck Waters"), Items ("Plus One Halberd")
- **Issue**: The shipwreck name is a known transcription garble. Rests on **AUTHORITATIVE CANON**: registry entry "Star-Crossed Lover — Sunken shipwreck (area T10) holding a +1 weapon in the grip of the captain's skeleton." The glossary explicitly lists `Starchloros Lover → Star-Crossed Lover`. Note the ch11 narrative doc *shares* this error ("Star Crossed Lover" and, in ch09 prose per the memory index, "Starchloros") — canon is the tiebreaker, not majority agreement among generated documents.
- **Suggested fix**: "Star-Crossed Lover" in all four places.

---

## High — Attribution Errors

### 3. Who destroyed the heart: **Vukradin**, not "Valphine and Vukradin"
- **Location**: Summary ("together they struck it down"; "the party agreed it had to go"), Scenes ("Valphine and Vukradin attack and destroy the beating heart")
- **Issue**: campaign_state states flatly: "Moesko's Heart Destruction (area T9): **Vukradin destroyed the heart**." The ch11 narrative agrees — Vukradin alone strikes it ("my offhand strike landed. The second swing connected, and the heart… was destroyed"), while **Valphine argued against destroying it at all** ("I don't see why we should destroy it. I mean, it's serving a useful purpose"). The recap's own Memorable Moment quote framing ("Defending her decision to leave Moesko's… heart") contradicts the scene bullet putting her among the attackers. "The party agreed" also overstates — Valphine dissented.
- **Suggested fix**: Credit Vukradin with the destruction; note Valphine's dissent rather than her participation.

### 4. Light spell: cast by **Vukradin**, not Valphine
- **Location**: Summary ("Valphine conjured a soft light"), Scenes, Spells ("Light — Cast by Valphine")
- **Evidence**: Ch11, Vukradin POV: "I then cast a light spell to temporarily illuminate the beacon, as a symbol of our intent."
- **Suggested fix**: Attribute Light to Vukradin.

### 5. Lightning rod: ch11 says **Vukradin** smashed it, not Brewbarry
- **Location**: Summary ("Brewbarry wasted no time and set about smashing it"), Scenes ("Brewbarry begins smashing the lightning rod")
- **Evidence**: Ch11, Vukradin POV: "I wasted no time… I descended to the lightning rod and smashed it." No document attributes this to Brewbarry. (Chapter docs are the authoritative tier; the recap is the outlier.)
- **Suggested fix**: Attribute the rod's destruction to Vukradin, or verify against the ch09 transcript before locking either version.

### 6. The +1 halberd was recovered by **Soma**; Brewbarry is the eventual holder
- **Location**: Summary ("It was Brewbarry who found the first prize"), Scenes ("Brewbarry discovers a magical halberd"), NPCs ("the magical halberd Brewbarry had pulled from the deep")
- **Evidence**: Ch11, Soma POV: "As I swam towards the first shipwreck, the Star Crossed Lover, my eyes fell upon something gleaming… a +1 halberd… **I swiftly secured it**." The crab scene in Vukradin's POV then shows the halberd in Brewbarry's hands — so Soma recovered it and it ended up with Brewbarry (matching campaign_state's holdings: "+1 Halberd… — Brewbarry").
- **Suggested fix**: Soma recovered it from the wreck; it passed to Brewbarry.

### 7. The starfish-covered Sea Urchin chest was ferried by **Soma**, not Brewbarry
- **Location**: Scenes ("Brewbarry recovers a locked chest covered in starfish from the Sea Urchin and ferries it to the shore")
- **Evidence**: Ch11, Soma POV: "I found another locked chest clinging with starfish from the Sea Urchin and, in another wreck, yet a third locked chest. **I ferried them all to shore**." Note the pattern: issues 6–7 (and the shark "lunged at Brewbarry" beat, unattested in ch11) systematically shift Soma's underwater actions onto Brewbarry. Also consistent with campaign_state's later note that "Soma did the diving" for the mermaid statue.
- **Suggested fix**: Attribute chest recovery/ferrying to Soma.

### 8. Soma's "blood money" line was a private thought, not a spoken quote
- **Location**: Memorable Moments (quote: "All money is blood money until proven otherwise." — Soma, "Cutting through the party's moral debate")
- **Evidence**: Ch11, Soma POV: "I think all money is blood money until proven otherwise, **but I kept that thought to myself**."
- **Suggested fix**: Either drop the quote or reframe it as internal narration; do not record it as table dialogue Vukradin heard.

---

## Medium — Lore / Provenance

### 9. Wand of Secrets and spellbook came from the **Orca** — the recap names only three of five wrecks
- **Location**: Scenes ("Salvaging the Wrecks"), Locations ("Shipwreck Waters"), Items ("Wand of Secrets")
- **Issue**: Rests on **AUTHORITATIVE CANON**: "Orca — Sunken shipwreck (area T14) containing a wand of secrets and a wizard spellbook"; "Wand of Secrets — found in the locked chest aboard the Orca." The recap's "other wrecks" hides this; the location entry lists only Star-Crossed Lover, Sea Urchin, and Vainglory though it counts five wrecks (canon and campaign_state add **Golden Gull** and **Orca**).
- **Suggested fix**: Name all five wrecks; source the wand/spellbook chest to the Orca.

### 10. Leilon: "a town to the south" and "the party's next destination" — both questionable
- **Location**: Locations ("Leilon"), Scenes (final bullet)
- **Issue**: (a) Canon places Leilon "on the High Road being rebuilt… in service of Neverwinter's Lord Protector" — i.e., between Neverwinter and the Phandalin region, **north** of the Tower of Storms along the coast; no document attests "south." (b) "Next destination" is overstated and could confuse future sessions: per campaign_state the party went on to the Whispering Wood arc and the entire Icespire campaign; as of ch47 Leilon is still *future* ("The Leilon arc is next, not past"). Miraal's warning is a long-range hook, not an itinerary.
- **Suggested fix**: "A town on the High Road to the north" and "foreshadowed as a future destination," not "next destination."

### 11. Cloak and crab should use canonical names
- **Location**: Items ("Color-Changing Cloak"), NPCs ("Giant Crab", "Hunter Sharks")
- **Issue**: Rests on **AUTHORITATIVE CANON**: the cloak on the Vainglory captain's skeleton is the **Cloak of Many Fashions**; the giant crab is named **Crabby** (party-given, ch07: speaks Common, intelligence gifted by Miraal); the meanest of the three sharks is the named NPC **Daggermaw** (campaign_state: "Daggermaw Hunter Shark Encounter").
- **Suggested fix**: Add the canonical names so future passes link these entities correctly.

---

## Minor

### 12. Octopus-hide armor: internal contradiction
- **Location**: Scenes ("debates taking Moesko's octopus-hide armor") vs. Items ("The party recovered it from his body")
- **Evidence**: Ch11 records only Vukradin dismissing it as useless splint-mail-equivalent; no confirmation it was taken. No later document lists it in party holdings.
- **Suggested fix**: Pick one; "debated, disposition unconfirmed" is the defensible record.

### 13. Grapple attribution reversed in NPC entry
- **Location**: NPCs ("Hunter Sharks… attempting to grapple their prey")
- **Evidence**: Ch11: **Soma** attempted the grapple ("the creature managed to elude my grappling attempt"). The recap's own scene bullet has it right; the NPC entry reverses it.

### 14. Conch resting place inconsistent within the recap
- **Location**: Summary ("Beneath his armor… they found an opalescent conch") vs. Items/Scenes ("resting on Moesko's lap")
- **Evidence**: Ch11 says only "resting nearby." Harmonize to one description.

### 15. Mechanics nits in the Spells section
- **Location**: Spells ("Prayer of Healing… granting the benefits of a short rest"; "Healing Word — Readied by Valphine as a bonus action")
- **Issue**: Prayer of Healing heals but does not grant short-rest benefits; bonus actions cannot be "readied" in 5e. Neither claim is attested in the session docs.
- **Suggested fix**: Trim both embellishments.

### 16. "Human heart" of a half-orc
- **Location**: Summary, Items ("Moesko's Heart")
- **Issue**: Canon registry has Moesko as a **half-orc** anchorite. "Human heart" does match the ch11 narration, so this may be deliberate in-fiction description — flagging only so nobody later infers Moesko was human.

---

## Notes on the *context documents* (not the recap)

- **world_state, "Leilon Hook" section, spells the banshee "Miral"** — per canon this is a wrong-form (glossary: `Miral → Miraal`) and, worse, sits one keystroke from **Meril** the mentor. Correct the doc, not canon.
- **The ch11 narrative doc's chapter number (11) disagrees with campaign_state's timeline**, which places the Tower of Storms events at **Ch08–09**. The recap's "Chapter 9" matches campaign_state; the narrative doc's numbering appears to be its own drift. No recap change needed.
- The recap's date (2025-08-22) and the ch09 attribution are corroborated by the VTT-additions log ("Bill Krabby", "Sharky" — both ch09) — no issue there.