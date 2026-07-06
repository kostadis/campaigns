# Consistency Report — Session 2026-06-22

## Critical Issues

### 1. Looted magic items duplicate gear the party already holds
- **Location:** Summary; Scene "Looting the Water Temple"; Items (Ring of Free Action, Mace of Smiting)
- **Issue:** The recap has the party recover a **mace of smiting** and a **ring of free action** "from Belsornig's corpse." Both items are already in the party's possession, looted from Lareth — they cannot be looted a second time.
- **Evidence:** world_state Party Equipment: "Mace of Smiting (Calmer, looted from Lareth)" and "Ring of Free Action (from Lareth)." party.md lists Mace of Smiting under Calmer's items and Ring of Free Action in party inventory. campaign_state confirms Lareth's loot was already taken (Ch13).
- **Suggested fix:** Remove the mace of smiting and ring of free action from Belsornig's loot. If new magic items were found, name different ones.

### 2. Half-plate +1 from Belsornig — possible confusion with Lareth's plate
- **Location:** Summary; Items (Half-Plate +1)
- **Issue:** "Half-plate +1 recovered from Belsornig's corpse." The party already carries magical plate mail looted from Lareth (and Calmer wears +1 Plate Mail). Half-plate is a distinct item type, so this *may* be new, but it closely echoes existing gear.
- **Evidence:** world_state: "Magical plate mail (looted from Lareth; fits no party member)." party.md, Calmer: "+1 Plate Mail (AC 20 with shield)."
- **Suggested fix:** Confirm this is genuinely a new medium-armor item and not a restatement of Lareth's plate; if uncertain, cut it.

### 3. "Barkinar" and the troll contract — unknown NPC and non-existent prior quest
- **Location:** Summary; Scene "An Unexpected Petitioner"; NPCs
- **Issue:** The recap twice states the trolls were something "the party had already been assigned by Barkinar to deal with." No NPC named **Barkinar** appears in any context document, and no troll contract or prior troll assignment exists in the quest log.
- **Evidence:** The party's Earth Temple superiors are Romag (dead) and Hartsch. campaign_state's completed/active quest lists contain no troll assignment. No "Barkinar" in any NPC table.
- **Suggested fix:** Verify the name (possible mis-transcription of Hartsch/Romag?) and drop or correct the claim of a pre-existing troll assignment. Treat the unsigned troll contract as new information introduced this session, not a prior party task.

### 4. Belsornig treated as dead/conquered — contradicts campaign state
- **Location:** Summary; NPCs (Belsornig); Locations (Canon Belsornig's Chambers)
- **Issue:** The recap presents the party as "the new masters of the Upper Temple," looting Belsornig's corpse and chambers as "the deceased Prophet of Water." Per current context Belsornig is alive, in the Water Temple, under Fire Temple assault, and never directly confronted by the party. Notably, the recap's combat is only against gargoyles and the Juggernaut — Belsornig's death is never actually depicted.
- **Evidence:** campaign_state: "Belsornig (Water Temple, area 215) — Confrontation Unresolved... Not directly confronted by the party. Thread open." NPC table: "Belsornig — Alive — Water Temple — Hostile; currently under Fire Temple assault." world_state matches.
- **Suggested fix:** Reconcile with campaign_state — either this is an uncaptured forward session and the state documents need updating to reflect Belsornig's death and the party's conquest, or the "Belsornig's corpse" framing is erroneous (see Issue #1, which stands regardless). Flag for human resolution before either doc is trusted downstream.

## Internal Contradiction

### 5. Who offered the larger share of Dren's tribute
- **Location:** Summary vs. Scene "Belsornig's Hidden Cache"
- **Issue:** The Summary says **Calmer** "magnanimously offered to contribute the largest portion" of Dren's tribute. The later scene says **Zephyr, as leader,** "offers to pay the bigger share," with Calmer merely calling it "an excellent idea." Same event, two different actors.
- **Evidence:** Both passages describe the same tribute-division moment.
- **Suggested fix:** Determine which character made the offer and make both passages agree.

## Tier-2 / Clarity Issues

### 6. Temple terminology muddle (Earth / Water / Upper / Lower)
- **Location:** Summary; Scene "An Unexpected Petitioner"; NPCs (Calmer)
- **Issue:** The recap interchangeably calls the conquered Water Temple the "Upper Temple," has the cleric pledge loyalty to "the new leadership of the Earth Temple and of the Lower Temple," and calls Calmer "now leader of the Earth/Upper Temple." Calmer being "leader of the Earth Temple" conflicts with Hartsch, the Earth Temple's Supreme Prophet. This is likely in-fiction flattery, but it risks confusing future sessions about which temple the party actually holds and who leads the Earth Temple.
- **Evidence:** world_state: Hartsch is "self-declared Supreme Prophet of the Earth Temple." The Water Temple is a distinct elemental temple; the party operates under Earth Temple cover as the Obsidian Edge.
- **Suggested fix:** Standardize: the party took the **Water Temple**; Calmer is being flattered as its new figurehead. Keep Hartsch as Earth Temple leader; avoid labeling Calmer "leader of the Earth Temple."

### 7. Treasure-split figures don't reconcile
- **Location:** Scene "Belsornig's Hidden Cache"; Summary
- **Issue:** The cache is described as "three thousand gold pieces" but also "1,250 gold each" (which for four PCs implies ~5,000), while Dren's "ten percent share (about 1,000 gold, 250 each)" implies a ~10,000 gp base. The numbers don't add up to a single pot.
- **Evidence:** Internal to the recap.
- **Suggested fix:** State one total and derive the per-share and 10% tribute figures from it consistently.

## Low-Confidence / Verify Only

- **Party level:** "The party (level 8)... rolling up to 8d8" — party.md lists Calmer as Cleric 6. party.md is a working reference and the campaign has advanced many chapters, so level 8 is plausible. Verify against current character sheets; not treated as a hard error.
- **"Protective Zone" radius:** described as "roughly sixty feet in range." The 3d8-damage/slow effect reads as Spirit Guardians (15-ft radius). Low-confidence mechanical note only — worth a glance, not a firm correction.

## Confirmed NOT Errors (do not flag)
- **Zinnia referred to as "he/him"** in the recap is **correct** and should be preserved.
- **Sequoia casting Jump and Silvery Barbs** is legitimate (Arcane Trickster); not an error.
- **Dren** = Dren Halveth, Broken Blades captain and party ally — correct.
- **Zephyr's pistol** = the custom hand crossbow pistol looted from Krell — correct.