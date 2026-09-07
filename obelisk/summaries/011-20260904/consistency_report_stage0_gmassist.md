# Consistency Report — Chapter 11 "Look who came to dinner"

## High-priority findings

### 1. "Brugor Axe-Biter" — canonical spelling is **Brughor Axe-Biter** (recap-wide)
- **Location**: Summary, Memorable Moments (Gog's quote and the assassination beat), Scenes (Battle Against Gog), NPCs (Brugor Axe-Biter, Gog entries)
- **Issue**: The orc chief is spelled "Brugor" throughout — roughly a dozen occurrences, including inside a section heading and a quoted line.
- **Evidence**: **AUTHORITATIVE CANON** — the NPC entry is "**Brughor Axe-Biter** / **Brughor**," and the Wyvern Tor location entry names "orc chief Brughor Axe-Biter" as the roster lead. Additionally, `vtt_transcription_corrections.md` explicitly lists "Brugor" as a known ASR garble ("Brugor, Brugort, Rukor → **Brughor**"), so this is a documented transcription error that leaked into the recap, not a variant. This is exactly the transposed/dropped-letter class of error the campaign's name rules exist to catch.
- **Suggested fix**: Brugor → **Brughor** everywhere, including the quote "You killed Brughor! Brughor!" and the NPC entry title.

### 2. Bugbear headcount: five total vs. canon's four
- **Location**: Summary ("four bugbears, a hulking ogre, and a single orc" inside, *after* the sentry was killed outside); Scouting the Cave scene
- **Issue**: One sentry killed outside + four bugbears inside = five bugbears. Canon's roster is four bugbears total.
- **Evidence**: **AUTHORITATIVE CANON** — Wyvern Tor entry: "Its module roster is orc chief Brughor Axe-Biter, **four bugbears**, and the ogre Gog." The Ch. 11 prep doc names exactly four bugbears (Hul the sentry, Skarn, Gorra, Muk).
- **Suggested fix**: Inside count should be **three** bugbears (the sentry was the fourth) — unless the GM added a fifth at the table, in which case verify against the VTT and note the deviation deliberately.

### 3. "Warden" as the apprentice's personal name
- **Location**: Summary, Memorable Moments (the dinner quote), NPCs (Warden entry), Dinner with the Red Wizard scene
- **Issue**: The recap treats "Warden" as the name of Hamun's undead former apprentice. Per the GM's working docs, "Warden" is the *collective title* of Hamun's twelve zombies (the **Kost Wardens**); the apprentice/acolyte zombie is **Warden Holl**, and **Warden Dreth** (a different zombie) leads them. As written, "Warden" is ambiguous between two distinct entities and will confuse future sessions.
- **Evidence**: This rests on generated/working docs, **not** the authoritative registry: `hamun_kost_strategy.md` ("One of them is his acolyte... **Warden Holl** is a Red Wizard acolyte in a singed robe — 'the Kost Warden who never learned he was dead'") and the Ch. 11 prep cast list, both deferring to `docs/background/monsters_phase2_descriptions.md` §4.1 as the authority.
- **Suggested fix**: Rename to **Warden Holl** in the NPC entry and prose — or, if the GM genuinely renamed him "Warden" at the table, record that as a deliberate ruling so Dreth/Holl don't collide with it later.

### 4. The route to Cragmaw Castle — the session's payoff is missing from the recap
- **Location**: Summary (final paragraph), Dinner with the Red Wizard scene
- **Issue**: The entire quid pro quo of the Wyvern Tor job was Hamun paying, on delivery, with **the route to Cragmaw Castle**. The recap records the delivery (threat "extinguished"), the dinner, and the party "planning to head toward Cragmaw Castle" — but never records whether Hamun handed over the route. Campaign state's live blocker is "the party has the name and no route"; the next session needs to know whether that blocker fell.
- **Evidence**: Pip's quest log: "**Hamun Kost knows the way, and has agreed to tell us**"; Ch. 11 prep doc scope line: "Closes in Hamun Kost's tent at Old Owl Well **with the route to Cragmaw Castle in hand**" and "He pays on delivery... He gives up the route to Cragmaw Castle."
- **Suggested fix**: Add an explicit line to the Summary and the dinner scene stating whether the route was delivered (and, if not, why Hamun withheld it).

## Medium-priority findings

### 5. Talon described as "forged with diamonds and precious stones"
- **Location**: Items (Talon entry)
- **Issue**: Unattested and likely a misattribution. Canon describes Talon as a +1 longsword; the "precious stones" detail belongs to **Zenvon's ornate short sword** ("semi-precious stones," from the Redbrand armory).
- **Evidence**: **AUTHORITATIVE CANON** — Talon: "+1 longsword belonging to the slain knight Aldith Tresendar." world_state: "a finely made +1 longsword"; Zenvon's combat profile: "ornate short sword... semi-precious stones."
- **Suggested fix**: "A finely made magical longsword carried by Pip..." — drop the gemstone description or move it to the correct weapon.

### 6. True Strike is not on Zenvon's documented spell list
- **Location**: Spells (True Strike entry), Battle Against Gog scene ("Zenvon uses magical precision")
- **Issue**: Every context document lists Zenvon's Arcane Trickster spells as exactly *Mage Hand*, *Minor Illusion*, and *Thunderwave* (DC 12). True Strike appears nowhere.
- **Evidence**: campaign_state ("Zenvon took the Arcane Trickster archetype: *Mage Hand*, *Minor Illusion*, and *Thunderwave*"); world_state and party.md agree.
- **Suggested fix**: Verify against the VTT/character sheet. If Zenvon legitimately knows True Strike (e.g., a cantrip pick not yet recorded), the sheet and grounding docs need updating; if not, the recap invented an ability.

### 7. Charcoal drawing attributed only to "descriptions from Sildar"
- **Location**: Secrets in the Charcoal scene ("referencing notes from what Sildar had told them"); Items (Charcoal Drawing: "strange goblins encountered by Sildar")
- **Issue**: Understates/misattributes the party's own evidence. The party *directly found two dead elongated-skull goblins* under Tresendar Manor (Ch. 6 — Veyra rolled the Investigation), in addition to the live one at the ambush who spoke to Sildar. Framing it as secondhand only will distort future recall.
- **Evidence**: world_state ("Two dead goblins with elongated skulls... found in the hideout caverns in Ch. 6"); both player quest logs ("Two more dead in the caverns under the manor... They were here first").
- **Suggested fix**: "...similar to the elongated-skull goblins the party found dead beneath Tresendar Manor and the one that confronted Sildar on the Triboar Trail."

### 8. Completed contracts on the same marauders go unmentioned
- **Location**: Summary / Dinner scene; NPCs (Hamun Kost: "tasked the party with clearing out the raiders")
- **Issue**: The recap credits the Wyvern Tor job solely to Hamun. **Harbin Wester's 120 gp contract** on these exact marauders (accepted in Ch. 5) was also just completed, and per the prep doc, Daran Edermath's Old Owl Well job is effectively done too. If the recap is silent, future sessions may forget the money owed in Phandalin.
- **Evidence**: campaign_state ("Wyvern Tor (120 gp, Harbin Wester)... accepted"); Ch. 11 prep ("this job is already paid for twice"; "Owed in Phandalin, whenever they go back: Harbin's 120 gp... and Daran Edermath's boots").
- **Suggested fix**: Note in the recap that Harbin's 120 gp bounty is now collectible, and that Hamun was the *second* employer for the same clear.

## Low-priority / minor findings

### 9. Internal inconsistency: when the bugbears flee
- **Location**: Summary vs. Scenes
- **Issue**: The Summary has all bugbears bolt immediately after Brughor's death, before the Gog fight ("The party let them go. What remained was Gog"). The Battle Against Gog scene then has "the remaining bugbears" fleeing "one by one" mid-fight. Also, the Ambush scene calls the interior bugbears "sentries," which they were not.
- **Suggested fix**: Pick one timeline (mid-fight flight matches the scene beats) and align the Summary; drop "sentries" for the interior bugbears.

### 10. Maela's NPC blurb contradicts her scenes
- **Location**: NPCs (Sister Maela Dawnforge)
- **Issue**: The blurb says she shows "cold pragmatism when dealing with dangerous monsters," but the recap's own Memorable Moments have her expressing *sadness* over the slain sentry and chiding Zenvon for being "remarkably cold" toward the dying Gog.
- **Suggested fix**: Rewrite the blurb to match the played beats — she mourned the sentry and pushed back on Zenvon's coldness. (Her cold-pragmatism side is real per party.md — the Rondar execution — but it is not what this session showed.)

### 11. The sentry may have a name: Hul
- **Location**: NPCs (Bugbear Sentry), Scenes
- **Issue**: The prep doc carries the bugbear **Hul** (milky eye, salvaged pike — exactly the features the recap describes) as table-canon features, with sentry-assignment marked as cuttable overlay. If the GM used the name at the table, the recap should record it.
- **Suggested fix**: Check the VTT; if "Hul" was spoken, name the sentry.

### 12. Minor Illusion producing a bugbear image
- **Location**: Spells (Minor Illusion), Ambush Inside the Cave scene
- **Issue**: Minor Illusion creates the image of an *object*, not a creature, by RAW. A stationary bugbear image is a common table ruling, not an error per se — but worth confirming it was a deliberate ruling so it doesn't silently expand the cantrip in future sessions.
- **Suggested fix**: None required if the GM ruled it; consider a mechanics note.

## Non-findings (checked, clean)

- **Chapter 10 → 11 continuity**: campaign_state and world_state still list Old Owl Well as "not started" and don't know Hamun Kost exists — this is *not* a contradiction. The Ch. 11 prep doc explicitly warns those docs are stale through Ch. 10; no flags were issued on that basis.
- **Treasure** (silver, electrum, three vials of perfume) matches the module's 180 sp / 15 ep / 3 perfume vials.
- **Gog fighting until slain while the bugbears rout on Brughor's death** matches canon exactly.
- **Talon's provenance reveal** (Aldith Tresendar, the Black Hawk) is correctly *new* information this session — canon records the party knew only the name as of Ch. 10. Spellings "Aldith Tresendar" and "Black Hawk" are correct per canon and glossary. (The "black armor and billowing cape" detail is unattested embellishment but contradicts nothing.)
- **Hamun's behavior** (freezing at the crystal-goblin description, Netherese expertise, offering identification services, paying attention to the obelisk mention) tracks the strategy doc's contingencies precisely.
- Names **Zenvon, Veyra, Sister Maela Dawnforge, Pip Thistlewick, Hamun Kost, Old Owl Well, Wyvern Tor, Cragmaw Castle, Netheril** all resolve cleanly against canon.