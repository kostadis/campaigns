# Consistency Report — Session 2026-08-17 (Chapter 64) Recap

---

### 1. Kalan Strongbranch present at the investigator's office — status contradiction

- **Location**: Summary (¶3), Scenes → "Deciphering the Vault Riddles", NPCs → Kalan Strongbranch, Locations → Investigator's Office, Items → Vault Cryptogram, Memorable Moments
- **Issue**: The recap has Kalan Strongbranch physically present, transcribing the cryptogram from photographic memory and later arriving "huffing and puffing." Both `campaign_state.md` and `world_state.md` record Kalan as **fled — "to the wind"**, whereabouts unknown, after admitting the fake-key deception. The recap also has him doing two contradictory things in the same scene: transcribing the cryptogram at the start *and* arriving late after the party had already solved it.
- **Evidence**: `campaign_state.md` NPC table: "Kalan Strongbranch | Alive — **fled, 'to the wind'** | Whereabouts unknown." `world_state.md` §4: "admitted the deception when confronted, then ran. 'Kalan is to the wind.'" `20260810_race_to_the_vile_door.md` frames his return as an *optional branch* ("If the party sent Tadric… he arrives with him… If they didn't — he turns up on his own at the Jewel of the Styx"). The prep also notes Kalan returning is a **−1 Track** event, i.e. a scene the GM plays deliberately, not a default.
- **Suggested fix**: Two separate problems. (a) If Kalan did return this session, add one clause noting it explicitly ("Kalan Strongbranch, returned from his flight, …") and update `campaign_state.md`/`world_state.md` to reflect he is no longer at large. (b) Resolve the double-arrival: either someone *else* transcribed the cryptogram at the start, or Kalan's late arrival is a separate later beat — as written the same NPC both opens and interrupts the scene.

---

### 2. Kalan Strongbranch attributed a "photographic memory" — likely wrong character

- **Location**: Summary (¶3), Scenes → "Deciphering the Vault Riddles", NPCs → A'lai Aivenmore
- **Issue**: The recap gives Kalan "photographic memory" allowing him to transcribe the cryptogram in full — but the recap's own **A'lai Aivenmore** NPC entry also says "Has a photographic memory." One of these is a misattribution.
- **Evidence**: No context document attributes photographic memory to Kalan. `entity_registry.yaml` describes Kalan as "Gatewarden; archmage." A'lai is the one who "spent years quietly researching" the cryptogram and knows two of its answers — the memorized-cryptogram capability fits A'lai's established arc. Prep (`candlekeep_murders_arc.md` S6 Beat 4) has the cryptogram book itself in an indestructible glass case with Daz transcribing it (DC 10 Arcana) — no photographic-memory NPC involved.
- **Suggested fix**: Confirm which character has the ability against the transcript, and remove it from the other. If A'lai memorized it, the recap should say so and drop the claim from Kalan's entry.

---

### 3. Kalan Strongbranch called "head of Candlekeep's guard"

- **Location**: NPCs → Kalan Strongbranch
- **Issue**: Title is imprecise and mixes two offices.
- **Evidence**: The **AUTHORITATIVE CANON** registry lists Kalan Strongbranch as "**Gatewarden**; archmage," with a separate faction entry for "The Watchers" and Tadric as "Watcher (Kalan's lieutenant)." `world_state.md` calls him "Reinstated Head of the Avowed" — an internal inconsistency in that generated doc, since the Avowed are the senior scholars, not the guard. Canon's Gatewarden title should win over both.
- **Suggested fix**: "Kalan Strongbranch, **Gatewarden** of Candlekeep, who has deputized the party."

---

### 4. Manshoon described as "the legendary wizard" arriving — simulacrum vs. person

- **Location**: Scenes → "The Aftermath at the High Tower" (scene heading), Summary (¶1)
- **Issue**: The scene heading says the party "witnesses the arrival of the legendary wizard Manshoon," while the bullets and the NPC entry correctly identify a **simulacrum**. The recap is internally inconsistent about what walked in.
- **Evidence**: `campaign_state.md`, `world_state.md`, and the registry all identify the Candlekeep breach as **Manshoon's simulacrum** (registry: "appears as **Manshoon's Simulacrum**"). `20260810_race_to_the_vile_door.md` notes the CR-12 "real man, depleted" block is for the *Vault* encounter and explicitly confirms "It remains **correct for the ch63 Candlekeep breach**, which was the simulacrum (GM ruling, 2026-08-19)."
- **Suggested fix**: Change the scene heading to "…witnesses the arrival of **Manshoon's simulacrum**."

---

### 5. Manshoon "breaching the inner sanctum" — the door he shattered is the Security Control Room

- **Location**: Summary (¶1), Scenes → "The Aftermath at the High Tower", Locations → High Tower, NPCs → Manshoon
- **Issue**: The recap repeatedly calls the shattered door the entrance to the "inner sanctum." Campaign docs name the specific room: the **Security Control Room**, which held the ward-governing artifacts behind the two-key door. "Inner sanctum" is an ambiguous coinage that could be confused with the Vault.
- **Evidence**: `campaign_state.md`: "Manshoon's simulacrum then breached the keep, shattering the **security-control-room door** with a `wall of force`." `world_state.md` §4 Locations: "**Security Control Room** — held the artifacts governing Candlekeep's wards behind a door requiring both keys; **Manshoon shattered it with `wall of force`**."
- **Suggested fix**: Replace "inner sanctum" with "the security control room" throughout, or note the equivalence once on first use.

---

### 6. Manshoon's target described only as "something of extraordinary value in a room nobody knew existed"

- **Location**: NPCs → Manshoon
- **Issue**: Vague where the campaign docs are specific, and risks future confusion about what Manshoon is racing for.
- **Evidence**: `campaign_state.md` Active Quests: "he is working toward the **Book of Vile Darkness** in the Vault beneath the House of Alaundo." `world_state.md` §4: "Wants the **Book of Vile Darkness**." Also note the framing contradiction: the recap says "a room nobody knew existed," but A'lai and Manshoon both knew of the depository, and `campaign_state.md` records that A'lai "**withheld the depository's true contents** from Manshoon — his last card," i.e. Manshoon knows the room exists but not what's in it.
- **Suggested fix**: "…seeking the **Book of Vile Darkness** in the Vault beneath the House of Alaundo — though A'lai withheld the depository's true contents from him."

---

### 7. Sylvira Savikas's illness left unnamed; "weakened by illness" understates it

- **Location**: Summary (¶3), Scenes → "Deciphering the Vault Riddles", NPCs → Sylvira Savikas
- **Issue**: Referred to only as "her illness." The condition is named, plot-relevant, and connected to Moziqodo.
- **Evidence**: `campaign_state.md`: "Sylvira Savikas | Alive, **dying of abyssal plague**." `world_state.md` §4 same. The registry has a dedicated event entry: "**Sylvira's Abyssal Plague** — Abyss-born plague afflicting Sylvira, **given to her by her son**; disclosed during Daz's ch60 interview."
- **Suggested fix**: Name it — "too weak from the abyssal plague to act herself." The son-transmission link is worth a clause given the Moziqodo thread running underneath the scene.

---

### 8. Sylvira called "a powerful and knowledgeable scholar" — title and role omitted

- **Location**: NPCs → Sylvira Savikas
- **Issue**: Understates her rank and omits her curatorial post, which is her stated basis for knowing Miirym's true name and the Mystra's Mantle star.
- **Evidence**: **AUTHORITATIVE CANON** registry: "Sylvira Savikas — **Great Reader; curator, Infernal Fortress**." `world_state.md` §4: "Curator of the Infernal Fortress (tiefling)." Her demonic-possession/true-names expertise (cited in the recap's own bullet) follows from the Infernal Fortress post.
- **Suggested fix**: "**Great Reader** Sylvira Savikas, curator of the Infernal Fortress…"

---

### 9. A'lai Aivenmore called "a high-ranking scholar" — title omitted; species omitted

- **Location**: NPCs → A'lai Aivenmore
- **Issue**: Vague where canon is specific, and omits that he is a drow — relevant given the scene where he speculates about a Menzoberranzan house.
- **Evidence**: **AUTHORITATIVE CANON** registry: "A'lai Aivenmore — **Great Reader**; main antagonist; Manshoon's inside man." `world_state.md` §4: "**Drow scholar** (ex-Council of Twelve)… 31 years at Candlekeep with no house, family or country, only his chair."
- **Suggested fix**: "**Great Reader** A'lai Aivenmore, a drow scholar who turned traitor…"

---

### 10. "Eleven years of service" vs. "31 years at Candlekeep" — check the figure

- **Location**: Summary (¶1), Memorable Moments, NPCs → A'lai Aivenmore
- **Issue**: Not an error, but a number that can be misread. The recap consistently uses eleven years, which is correct for the *Manshoon relationship*, not his tenure.
- **Evidence**: `world_state.md` §4: "**Manshoon's inside man for eleven years** — 31 years at Candlekeep." `campaign_state.md`: "A'lai's patron for 11 years."
- **Suggested fix**: No change required, but consider "After eleven years serving Manshoon" rather than bare "eleven years of service," so a future reader doesn't take it as his time at the keep.

---

### 11. Miirym described as "dragon guardian of Candlekeep… who lives in the castle"

- **Location**: Summary (¶3), NPCs → Miirym
- **Issue**: Miirym is a **ghost**, not a living dragon; the recap's phrasing ("dragon who lives in the castle") reads as a living resident.
- **Evidence**: **AUTHORITATIVE CANON** registry: "Miirym, the Sentinel Wyrm — **translucent ghost-dragon** guardian of Candlekeep (encountered 'Underneath Candlekeep')." Note also the riddle text the recap itself quotes — "the true name of **she who serves in spirit**" — which is consistent with the ghost reading.
- **Suggested fix**: "Miirym, the Sentinel Wyrm — the translucent ghost-dragon guardian of Candlekeep."

---

### 12. "School of the Drama Library" — name divergence

- **Location**: Summary (¶2), Scenes → "The Prisoner's Bargain", Locations → School of the Drama Library, NPCs → Batbayar
- **Issue**: The location is named "School of the Drama Library" three times. Canon names it **The School of Drama**.
- **Evidence**: **AUTHORITATIVE CANON** registry, location: "**The School of Drama**." Registry NPC entry: "Batbayar — legendary halfling bard whose statue dominates **the School of Drama**." `candlekeep_murders_arc.md` clue table: "School of Drama (Batbayar statue)." The recap's form appears to trace to in-transcript speech ("the entry hall of the School of the Drama Library") rather than canon.
- **Suggested fix**: Use **The School of Drama** in section headings and prose; the verbatim quote may retain the spoken form.

---

### 13. Batbayar's statue location described inconsistently

- **Location**: Locations → School of the Drama Library, NPCs → Batbayar
- **Issue**: Recap says the statue "dominates the entry hall." The registry says it dominates the School of Drama generally; not a contradiction, but the recap asserts an interior detail that no context doc attests. Low-confidence detail worth flagging for a transcript check.
- **Evidence**: **AUTHORITATIVE CANON** registry: "legendary halfling bard whose statue dominates the School of Drama." The "entry hall" detail comes from A'lai's in-scene dialogue in the recap itself, so it is probably fine — flagging only so a future session doesn't treat it as independently confirmed.
- **Suggested fix**: No change needed; it is quoted from A'lai. Note in world_state if promoted to canon.

---

### 14. Astronomicon / Orrery relationship inverted

- **Location**: Summary (¶3), Locations → Orrery of the Astronomicon, NPCs → Sylvira Savikas
- **Issue**: The recap treats "Orrery of the Astronomicon" as a chamber containing star charts and, in the Sylvira bullet, says she "passed the Astronomicon" and saw people "inside." The registry structure is: **The Astronomicon** is the building, and **The Orrery** is a sub-location within it (alongside **Stargazer**). The recap's compound name is fine as prose, but the "three people inside the Orrery" vs. "inside the Astronomicon" alternation is ambiguous about which space is under observation.
- **Evidence**: **AUTHORITATIVE CANON** registry, location: "The Astronomicon (aliases: Astronomicon) — contains **The Orrery** and **Stargazer**." VTT corrections glossary also has "Ori → **Orrery**" and "Mistra's Mantle → **Mystra's Mantle**," confirming both terms are live campaign names.
- **Suggested fix**: State it once: "the **Orrery**, within the Astronomicon" — and pick one for the intruder sighting (the transcript quote is "when she passed the Astronomicon, she noticed three people inside").

---

### 15. "House of Momentous Deeds" — name divergence

- **Location**: Summary (¶4), Scenes → "The Statue of Alaundo", Locations → House of Momentous Deeds
- **Issue**: Recap names it the "House of Momentous Deeds" (three occurrences). Canon names it **The Hall of Momentous Deeds**.
- **Evidence**: **AUTHORITATIVE CANON** registry, location: "**The Hall of Momentous Deeds** — contains **The Whispering Dome**." `candlekeep_murders_arc.md` S7 Beat 3 corroborates: "research at the **Hall of Momentous Deeds**." Note this is a house-vs-hall distinction in a keep full of "House of X" buildings (House of Alaundo, House of Mechanus, House of Records), so the drift is easy and worth correcting explicitly.
- **Suggested fix**: **Hall of Momentous Deeds** in all three places.

---

### 16. Founders Court described as containing the House of Mechanus and the Immortal Chambers

- **Location**: Locations → Founders Court
- **Issue**: "A central area in Candlekeep where the House of Alaundo is located, also **near** the House of Mechanus and the Immortal Chambers." The recap's own House of Mechanus entry says that building is "situated **between** the Immortal Chambers and Founders Court" — i.e. adjacent to, not in, Founders Court. Minor, but the two entries phrase adjacency differently.
- **Evidence**: `vtt_known_additions.md`: "**Immortal Chambers** — 'It sits between the Immortal Chambers and Founders Court'"; "**Founders' Court** — 'The House of Alaundo stands in the middle of Founders' Court.'" Registry lists Founders Court, The Immortal Chambers, and House of Mechanus as three separate locations.
- **Suggested fix**: "Founders Court — a central court where the House of Alaundo stands; the House of Mechanus lies between it and the Immortal Chambers."

---

### 17. Alaundo's grave in "the grove where Candlekeep's keepers of tomes were buried"

- **Location**: Summary (¶4), Scenes → "The Grave of Alaundo…", Locations → The Grove
- **Issue**: Alaundo is described as buried among the **Keepers of Tomes**. Alaundo is the prophet the institution is founded on, not a Keeper of Tomes. Whether the grove is exclusively Keepers' or a general Avowed cemetery is unclear from context docs.
- **Evidence**: Registry: "Alaundo the Seer — the historical prophet whose 99 prophecies the Endless Chant recites"; listed as a distinct NPC from any office-holder. `candlekeep_murders_arc.md` S7 Beat 3 puts his tombstone in "the **Grove cemetery**" without restricting it to Keepers. The Grove is a registry location in its own right.
- **Suggested fix**: "the Grove, Candlekeep's burial ground" — drop the "keepers of tomes were buried" qualifier unless the transcript states it, in which case attribute it to the in-scene speaker.

---

### 18. Alaundo's age at death — 97 vs. the 99 prophecies

- **Location**: Summary (¶4, ¶6), Scenes, Locations → The Grove, Memorable Moments
- **Issue**: Not an error — flagging only because 97 and 99 are adjacent numbers attached to the same figure and a future session could conflate them.
- **Evidence**: `candlekeep_murders_arc.md` S7 Beat 3: "**97 steps:** Alaundo's age at death." Registry: "Alaundo the Seer — the historical prophet whose **99 prophecies** the Endless Chant recites." Both figures are correct and distinct.
- **Suggested fix**: No change. Consider a parenthetical in world_state when promoting: "died aged 97 (distinct from his 99 prophecies)."

---

### 19. Spanner described as overseeing thirteen modrons — species confirmed, but note prior error

- **Location**: Scenes, Locations → House of Mechanus, NPCs → Spanner
- **Issue**: None — the recap correctly says **gnome** librarian. Flagging as a *confirmed-correct* item because a known prior error exists in the pipeline.
- **Evidence**: **AUTHORITATIVE CANON** registry: "Spanner — House of Mechanus librarian; directs the 13 modrons." `vtt_known_additions.md` explicitly records the correction: "**gnome** librarian… *Corrected 2026-08-20 by `/staged-consistency` stage 0: originally filed here as 'modron librarian', which was wrong — the tape says gnome twice.*" The recap is right.
- **Suggested fix**: None. Consider promoting Spanner to `entity_registry.yaml` proper (the additions file notes he is "not yet promoted").

---

### 20. Modron dust mechanism — two incompatible explanations given

- **Location**: Items → Dust of Mechanus, NPCs → Modrons
- **Issue**: The Items entry says the dust "could be dust from the plane itself **or** the remains of a slain modron, which turn to dust when they die **on the Prime Material**." The Modrons NPC entry states flatly "When they die they turn to dust, which is why killing one would yield Dust of Mechanus." The Prime-Material qualifier appears in one place and not the other, and no context document attests either version.
- **Evidence**: Registry has Mechanus as a concept ("lawful plane, modrons' home, source of the Maze Engine") but no dust mechanics. `candlekeep_murders_arc.md` S7 Beat 3 has only: "**Mechanus dust:** Spanner… has a basket of 'spent gear-dust' from his 13 modrons. **He gives it freely** under siege." Note the prep version has Spanner giving dust freely with no tools and no negotiation — the recap's tools/collateral/symmetry-study negotiation is a table divergence from prep, which is fine but should be recorded as the new canon.
- **Suggested fix**: Pick one formulation from the transcript and use it in both entries. Also record in world_state that the party obtained **modron tools on loan** (not a free basket of dust), since the loan creates an outstanding obligation.

---

### 21. Zalthir + Glabbagool owe Spanner an interview — obligation not surfaced as an open thread

- **Location**: Scenes → "The Grave of Alaundo and the House of Mechanus", NPCs → Spanner, Glabbagool, Items → Modron Tools
- **Issue**: The party incurred two live obligations this session — a deferred symmetry-study interview with Spanner, and borrowed tools that presumably must be returned — but neither is flagged as an open thread.
- **Evidence**: `campaign_state.md` maintains an "Active obligations & outstanding debts" list (Dawnbringer's therapy, Fembris Lancer, etc.). Nothing in the recap flags these for promotion.
- **Suggested fix**: Add to the recap's carry-forward (or note for `campaign_state.md`): "Owe Spanner a symmetry study/interview of Zalthir and Glabbagool, deferred until after the descent; modron tools on loan."

---

### 22. Glabbagool called "an intelligent gelatinous cube"

- **Location**: NPCs → Glabbagool, Summary (¶1)
- **Issue**: `world_state.md` describes Glabbagool as a "sentient **grey ooze** (formerly gelatinous cube)" bonded to Zalthir's forearm — not a free-standing cube.
- **Evidence**: `world_state.md` §3: "**Glabbagool — sentient grey ooze (formerly gelatinous cube).** **Bonded to Zalthir's left forearm**, functioning as a semi-autonomous extension of his body." `campaign_state.md` NPC table: "Glabbagool | Alive | **Bonded to Zalthir's forearm**." The registry entry ("sentient ooze companion") is consistent with grey ooze. Note the recap's own quoted GM line — "standing just a little bit taller with pride" — is table flavor and doesn't establish an independent body.
- **Suggested fix**: "Glabbagool — a sentient ooze bonded to Zalthir's left forearm." Flag also that `world_state.md` contains a self-noted reconciliation warning ("One dossier places Glabbagool on Grygum's arm; the authoritative bond is **with Zalthir**") — the recap correctly has Zalthir, so no error there.

---

### 23. Grygum called "a cleric" implicitly; species not stated — minor

- **Location**: Throughout (Grygum has no NPC entry, being a PC)
- **Issue**: No error. Noting only that the recap's "Grygum, on the storage arrangement: 'It's a little weird to store things inside our NPCs, but I'll allow it'" is a player-voice/OOC line attributed as if in-character. Future readers may mistake it for Grygum's in-world dialogue.
- **Evidence**: `party.md`: Grygum — Cleric 8 (Life Domain), Orc, player Ben Pfaff. The quoted line is table-speak about NPC handling, not diegetic.
- **Suggested fix**: Mark OOC lines as such, as the recap already does elsewhere ("Thorin, out of character: 'I'm not ready to cop to what we did'").

---

### 24. "Grygum pouring 44 points of healing into Zalthir" — check against sheet

- **Location**: Summary (¶6), Scenes → "The Descent into the Vault"
- **Issue**: 44 HP in a single act, with the text noting Zalthir was "short 27 hit points" and the healing was "overkill." No spell or resource is named. Worth verifying against Grygum's sheet that a 44-point heal is available at his level.
- **Evidence**: `party.md`: Grygum — Cleric 8 (Life Domain). `world_state.md` lists his abilities: "Revivify, Divine Healing, Guiding Bolt, Spirit Guardians, Inflict Wounds, Glyph of Warding, Dust of Suleiman." Life Domain's Disciple of Life bonus plus a 4th-level Cure Wounds could plausibly reach 44, and he holds "fourth-level spell gems" per `party.md` — so this is likely fine, but the spell is unnamed in the recap.
- **Suggested fix**: Name the spell/resource used, so a future session can track slot expenditure.

---

### 25. Daz's Telekinesis — verify against sheet

- **Location**: Summary (¶6), Scenes → "The Descent into the Vault", Memorable Moments
- **Issue**: Daz casts **Telekinesis** (5th level). `party.md` lists Daz as **Wizard 8 (Evoker)**, which grants 4th-level slots at most. `world_state.md` lists his abilities as "Evoker (Fireball, Scorching Ray, Sculpt Spells), Fey Touched, Warcaster, Misty Step, Shape Water, Magic Missile, Maximilian's Earthen Grasp, Hypnotic Pattern, **Telekinetic**" — note **Telekinetic** (the feat) is listed, not **Telekinesis** (the 5th-level spell). These are different things and the recap may have conflated them.
- **Evidence**: `party.md` Daz section: "Wizard 8 (Evoker)." `world_state.md` §2 Daz: "**Telekinetic**." Note also that `party.md` states "**Party levels to 9 before the next fight**" and `campaign_state.md` records level-9 as pending — if the party leveled this session, 5th-level slots become available and the cast is legal.
- **Suggested fix**: Confirm from the transcript whether Daz cast the **spell** Telekinesis or used the **Telekinetic** feat's shove. If the spell, confirm the level-up to 9 occurred and record it; if the feat, correct the recap and the two places it names the spell in bold.

---

### 26. Trap trigger range — "between the 93rd and 102nd steps" vs. "positioned themselves on the 97th step"

- **Location**: Summary (¶6), Scenes → "The Descent into the Vault", Locations → The Hidden Staircase, Memorable Moments
- **Issue**: The Scenes bullets and Locations entry say the hinge caught "anyone standing between steps 93 and 102," and separately that Grygum went "down 97 steps" with Zalthir joining him. But the Memorable Moments entry says "The party had carefully positioned themselves **on the 97th step**" — singular, all of them. These describe different tactical pictures, and the recap also states Daz was "safely above" while Grygum was on 97 (i.e. within the trap range).
- **Evidence**: Internal to the recap. `candlekeep_murders_arc.md` S7 Beat 5 has the trap at "step 93 (or wherever)," so the exact range is a table detail with no external authority.
- **Suggested fix**: Reconcile to one description. Given the Dexterity saves and per-character outcomes described, "the party spread across steps 93–102, with Daz above the hinge" appears to be the accurate picture; correct the Memorable Moments framing.

---

### 27. Thorin's fall resolution left unresolved — flag explicitly for next session

- **Location**: Scenes → "The Descent into the Vault"
- **Issue**: The recap records "rolling a 2, then a 5 on a luck reroll, then invoking a second reroll at +8 ('you must use the new roll'), **the result of which is left unresolved as the GM calls the night**." This is correct to record but should be surfaced as a hard open item, not buried in a bullet — the next session opens on an unresolved die.
- **Evidence**: Internal. `party.md` Thorin: Fighter 8 (Battle Master), Dwarf (Giant Foundling) — no Lucky feat is listed in `party.md` or `world_state.md`, so the "luck reroll" and "second reroll at +8" mechanics should be checked against the sheet.
- **Suggested fix**: Add an explicit open-thread line: "⚠️ **Unresolved:** Thorin's final reroll on the fall was not resolved before the session ended." Also verify the reroll source against his sheet.

---

### 28. "Zalthir joins him on 97, noting he can hover" — ability unattested

- **Location**: Scenes → "The Descent into the Vault"
- **Issue**: Zalthir is described as able to **hover**. No context document attributes hovering to Zalthir.
- **Evidence**: `party.md` Zalthir — Monk 8 (Warrior of Shadow), Bronze Dragonborn. Items: Eldritch Claw Tattoo, spider-silk cloak, **Potion of Flying** (in Glabbagool), ice mirror. `world_state.md` abilities: Darkness, Shadow Step, Stunning Strike, Eldritch Claw Tattoo, Minor Illusion. No hover/fly feature. The recap's own Items section notes the Potion of Flying was "**raised as one of Zalthir's options** during the positioning discussion" — i.e. discussed, not necessarily drunk.
- **Suggested fix**: Clarify whether Zalthir hovered (potion consumed — a resource expenditure to record), *could* hover conditionally (potion available), or whether this is a Zalthir-player claim not yet mechanically resolved. If the potion was drunk, remove it from the party's held-items list.

---

### 29. Zalthir "can grab the other two and open my wings" — wings unattested

- **Location**: Scenes → "The Descent into the Vault"
- **Issue**: Zalthir refers to "my wings." Bronze dragonborn in standard 5e do not have wings; no context document grants Zalthir flight.
- **Evidence**: `party.md`: "Zalthir — Monk 8 (Warrior of Shadow) · **Bronze Dragonborn**." No wing/flight feature in `party.md` or `world_state.md`. This may be a Potion-of-Flying reference, a homebrew feature, or table banter.
- **Suggested fix**: Resolve against the character sheet. If Zalthir has no wings, mark the line clearly as an in-character proposal that did not resolve, so a future session doesn't grant him flight on the strength of this recap.

---

### 30. "44 points of healing… to prepare **them**" — recipient ambiguity

- **Location**: Summary (¶6)
- **Issue**: "Grygum pouring 44 points of healing into Zalthir to prepare **them** for whatever lay ahead" — ambiguous whether "them" is Zalthir or the party. The Scenes bullet clarifies it was Zalthir alone (short 27 HP), so the Summary reads as if the whole party was healed.
- **Evidence**: Internal to the recap; Scenes bullet is the more specific statement.
- **Suggested fix**: "…pouring 44 points of healing into Zalthir, who was down 27 hit points with no short rest taken."

---

### 31. "Daz recalls the letter from the librarian in Milo's book" — unclear referent

- **Location**: Scenes → "The Grave of Alaundo and the House of Mechanus"
- **Issue**: "the letter from the librarian in Milo's book" is opaque and will not be reconstructible in six months. Which librarian, which volume?
- **Evidence**: Registry: "**Account of the War of the Dragons** — Milo Goodbarrel's multi-volume book (Volumes 1-3), sold at Rishaal's Pageturners." `candlekeep_day_four.md` carry-forward: "⭐ **Daz's *Milo Goodbarrel's account* Volumes 1–3** (Rishaal the Pageturner edition)… Daz reads from Volumes 1–3 throughout the OOTA back half. Mike's character beat." No librarian-letter is recorded in any context doc.
- **Suggested fix**: Expand with volume and the librarian's name if the transcript gives them; otherwise flag as "an unspecified passage from Milo Goodbarrel's *Account of the War of the Dragons*."

---

### 32. "every scholar in Castle Ward knows this one by heart"

- **Location**: Scenes → "The Grave of Alaundo and the House of Mechanus"
- **Issue**: **Castle Ward is a district of Waterdeep, not part of Candlekeep.** The scene is set at Candlekeep, and the scholars in question are Candlekeep's Avowed. This is almost certainly a transcription artifact.
- **Evidence**: `vtt_known_additions.md`: "**Castle Ward** — Waterdeep district; Stroud-statue…; Rishaal's bookshop; Bahamut chapter." Critically, `vtt_transcription_corrections.md` contains an existing glossary row for exactly this drift: "**Kendall Keep → Castle Ward**" — indicating the ASR confuses these terms in this campaign. The likely intended word here is "Candlekeep."
- **Suggested fix**: Change to "every scholar in **Candlekeep** knows this one by heart." Worth adding a note to the VTT corrections file that the Castle Ward↔Candlekeep confusion runs in both directions.

---

### 33. "Fustilugs… magically enchanted centuries ago under one of the oversized black marble chess pieces"

- **Location**: Summary (¶2), Scenes, Locations → Philosopher's Court, Items → Black Marble Knight
- **Issue**: The Summary says "one of the oversized black marble chess pieces"; the Items and Locations entries correctly specify the **knight**. The Summary is vaguer than the rest of the recap and than the answer requires.
- **Evidence**: `candlekeep_murders_arc.md` clue table: "**Fustilugs** | Philosopher's Court (under the **black marble knight**)." The recap's own quoted A'lai line refers to "the knight is never replaced." Also note the recap's verb drift: Summary says "magically **enchanted**," the transcript quote says "magically **enched**" (a garble), and the Locations/Items entries say "magically **etched**." Etched is almost certainly correct.
- **Suggested fix**: Summary → "under the oversized black marble **knight**"; standardize on "**etched**" throughout.

---

### 34. "Fustilugs" spelling — confirmed correct, flagging the known trap

- **Location**: Throughout
- **Issue**: None. Flagging as confirmed-correct because the VTT corrections file records this as a known garble.
- **Evidence**: `vtt_transcription_corrections.md`, Real-world/table section: "Fustelugs → **Fustilugs**." The recap uses **Fustilugs** consistently. Correct.
- **Suggested fix**: None.

---

### 35. "Batbayar" spelling — confirmed correct, flagging a documented prior canon error

- **Location**: Throughout
- **Issue**: None — the recap uses **Batbayar**, which matches canon. Flagging because this name was recently and specifically corrected in the pipeline and a regression would be easy to miss.
- **Evidence**: **AUTHORITATIVE CANON** registry: "**Batbayar** — legendary halfling bard whose statue dominates the School of Drama." `vtt_transcription_corrections.md` glossary row: "Bathayar, Pfaffayar, Bauthoyar → **Batbayar**," plus a lengthy post-mortem: "**`Bathayar/Pfaffayar → Bauthoyar` was wrong for four days; the canonical is `Batbayar`.**… Caught by `/staged-consistency` stage 0 on 2026-08-20." The recap is correct.
- **Suggested fix**: None.

---

### 36. "Manshoon on square one, the party on square zero" vs. "box one / box zero"

- **Location**: Summary (¶1), Scenes → "The Aftermath at the High Tower"
- **Issue**: The Summary says "square"; the Scenes bullet says "box." Trivial, but the prep document uses a specific term.
- **Evidence**: `20260810_race_to_the_vile_door.md`, "The Manshoon Track": "**Six boxes. He starts on box 1**… | **≤3** | **4–5** | **6** |." The prep's term is **box**.
- **Suggested fix**: Standardize on "box" to match the GM-side track terminology.

---

### 37. Manshoon "currently one square ahead of the party in the race to the vault" — check against prep track

- **Location**: NPCs → Manshoon
- **Issue**: Stated as settled fact. Per prep, the Track advances and reduces during play (A'lai's two bought clue lines are −1 each; Sylvira's freebies −1; running clue scenes +1). The recap describes the party buying A'lai's two lines *and* receiving Sylvira's two answers, which per prep would move the Track. "One square ahead" may be stale as of session end.
- **Evidence**: `20260810_race_to_the_vile_door.md`: "**Reduce −1 for each:** A'lai's two cryptogram lines (bought); Sylvira's two freebies (Vydykyq + Limniz)…" and "**Carry the Manshoon Track across the break** at whatever it read when you cut. **Write it down**; don't reconstruct it from memory next week."
- **Suggested fix**: Record the **actual Track value at session end** in the recap or a GM note, per the prep's own explicit instruction. "One square ahead" without a number is not sufficient to resume from.

---

### 38. Sylvira's clue answers vs. prep's expected answers — verify

- **Location**: Summary (¶3), Scenes
- **Issue**: The recap has Sylvira supplying (a) Miirym's true name for riddle 1 and (b) the Eastern Light of Mystra's Mantle as an Orrery star. Prep expects Sylvira's two freebies to be the **answers** — **Vydykyq** (riddle 1) and **Limniz** (riddle 2). The recap never states the actual answer words, only what they refer to.
- **Evidence**: `20260810_race_to_the_vile_door.md`: "**Sylvira's two freebies (Vydykyq + Limniz)**"; `candlekeep_murders_arc.md` clue table: "1 | **Vydykyq** | catacombs (Sentinel Wyrm Miirym)… 2 | **Limniz** | Astronomicon Orrery." So Vydykyq *is* Miirym's true name and Limniz *is* the star.
- **Suggested fix**: Record the answer words themselves — **Vydykyq** and **Limniz** — since they are the cipher inputs the party now holds. Without them the recap doesn't capture what was actually gained.

---

### 39. The riddle text order differs from prep

- **Location**: Summary (¶3), Scenes → "Deciphering the Vault Riddles"
- **Issue**: The recap's decoded riddle runs: feed the quill / tread as many steps / **sprinkle dust of Mechanus** / **utter the original prophecy** / obsidian door. Prep's canonical riddle runs: feed the quill / tread as many steps / **utter the original prophecy** / **sprinkle dust of Mechanus** / one last guardian / verify the chosen Reader's claims / obsidian door. Lines 3 and 4 are swapped, and two lines are missing entirely.
- **Evidence**: `candlekeep_day_four.md` Beat 3 and `candlekeep_murders_arc.md` S7 Beat 3, verbatim:
  > *Feed the quill of Alaundo the Seer / Tread as many steps as he lived in years / **Utter the original prophecy to unseen ears** / **Sprinkle dust of Mechanus on dormant gears** / **One last guardian of knowledge remains** / **To verify the chosen Reader's claims** / But those well versed in Candlekeep's lore / May fearlessly pass the Obsidian Door*
- **Suggested fix**: Two issues. (a) The ordering: the recap's own quoted table-line — Grygum supplying the missed line and Thorin saying *"Okay, that rhymes with years"* — indicates "unseen ears" belongs adjacent to "years," i.e. prep's order is right and the recap's summary reordered it. (b) The **two missing lines about the guardian who verifies the chosen Reader's claims** are load-bearing for the next session and should be restored. This matters: the party may believe they have the full text when they are two lines short.

---

### 40. The party's descent count vs. the missing "guardian" step

- **Location**: Summary (¶6), Scenes → "The Descent into the Vault"
- **Issue**: The party descended "counting each step carefully toward the ninety-seventh" and hit the trap at 93–102. Per prep, the correct procedure is to speak the first prophecy *at* the right step, which triggers the hinge as a **feather-fall shaft**, not a hazard. The recap presents the hinge as an unanticipated trap and Thorin's fall as a disaster, with no mention of the prophecy being spoken.
- **Evidence**: `candlekeep_day_four.md` Beat 5: "Count steps. At step 93 or so, party speaks the first prophecy aloud. **Step hinges open. `Feather fall` shaft, 1000 ft.**" `candlekeep_murders_arc.md` S7 Beat 5 identical. The recap earlier notes "With the prophecy provided by the scholars who knew it by heart" — so they *had* the prophecy — but never records them speaking it.
- **Suggested fix**: Clarify whether the prophecy was spoken. If not, the fall may be a genuine hazard rather than the intended feather-fall descent, and that distinction determines whether Thorin is falling 1,000 ft with magical protection or without. This is the single most consequential ambiguity in the recap for the next session.

---

### 41. "Kalan Strongbranch — whose photographic memory allowed him to transcribe the cryptogram in full — spread the riddles across the floor"

- **Location**: Summary (¶3)
- **Issue**: Per the recap's own Scenes section, it was **A'lai** who suggested going to the investigator's office specifically to "put these notes on the floor and bring all of our best minds to see what we can do." The Summary attributes the floor-spreading to Kalan.
- **Evidence**: Internal to the recap: Scenes → "Deciphering the Vault Riddles", first bullet: "A'lai suggests the venue: 'I think I can help you, but I suggest we go to the investigator's office, where we can put these notes on the floor…'"
- **Suggested fix**: Attribute the venue and the floor-layout suggestion to A'lai; keep Kalan's role (whatever it resolves to per Issue 2) separate.

---

### 42. "Thorin appealed to the Watcher Tadric, invoking… their deputization by Kalan Strongbranch"

- **Location**: Summary (¶2), Scenes → "The Prisoner's Bargain", NPCs → Kalan Strongbranch
- **Issue**: The party's deputization is attributed to Kalan Strongbranch. But per `campaign_state.md`, the party was **conscripted by Bookwyrm** (the First Reader), and Kalan was *removed from the investigation* before subsequently betraying them with a fake key. Whether Kalan ever deputized them needs checking.
- **Evidence**: `world_state.md` §1: "secretly summoned by acting-head **Bookwyrm** to investigate the murder." `candlekeep_murders_arc.md` S2 Beat 1: "Bookwyrm publicly: 1. **Removes Kalan from the investigation.** 2. **Conscripts the party.**" `candlekeep_arc_flowchart_v2.md` has Kalan reinstated as Gatewarden only at the *end* of the arc. Note the recap's transcript quote does support Thorin *saying* this — so it may be Thorin's rhetorical framing rather than a fact.
- **Suggested fix**: If this is Thorin's in-character argument, mark it as such ("invoking what Thorin characterized as their deputization by Kalan Strongbranch"). Do not record it in world_state as established institutional fact without corroboration.

---

### 43. "Grygum: 'He only has 2? Oh, well, send him off to the jail then.'" — placement

- **Location**: Scenes → "The Prisoner's Bargain", final bullet
- **Issue**: This line is placed as the closing beat of Tadric taking A'lai into custody, but reads as a reaction to A'lai only knowing **two** riddle answers — i.e. it belongs earlier, at the reveal, not at the handover.
- **Evidence**: Internal. The bullet immediately above it is A'lai's "I suppose" to Tadric; the two are sequenced as if Grygum's line follows the custody transfer.
- **Suggested fix**: Reorder so the "only has 2" reaction sits with the two-answers reveal.

---

### 44. Fembris Lancer, Daral Yashenti, Spiderbait, Dawnbringer — companions unaccounted for

- **Location**: Recap-wide
- **Issue**: The recap never mentions four attached companions who, per campaign docs, are with or held by the party. Dawnbringer in particular has an active obligation (continued therapy, refuses to leave Candlekeep) and Thorin — who just fell down a shaft — is her wielder.
- **Evidence**: `campaign_state.md` NPC table: Dawnbringer "With Thorin, at Candlekeep"; Spiderbait "Traveling with party"; Daral Yashenti "With party, Candlekeep"; Fembris Lancer "Imprisoned | Deneir's Sanctum (party's captive)." `party.md`: "Attached companions: **Glabbagool**, **Dawnbringer**, **Spiderbait**, **Daral Yashenti**, and captive **Fembris Lancer**."
- **Suggested fix**: Not necessarily an error — they may simply have been offscreen. But note their whereabouts for continuity, especially Dawnbringer, who is presumably falling with Thorin.

---

### 45. Moziqodo / Sylvira fuse — correctly handled, flagging as a standing hazard

- **Location**: Summary (¶3), Scenes, NPCs → Sylvira Savikas, Memorable Moments
- **Issue**: None — the recap correctly and repeatedly notes Sylvira does not know her son is dead, and Thorin's "I do what I can for those that I can" is correctly framed. Flagging as **confirmed-correct** because this is the single most fragile continuity item in the campaign and the recap handled it well.
- **Evidence**: `campaign_state.md`: "⚠️ **Does not know her son Moziqodo is dead, or that the party killed him**." `20260810_race_to_the_vile_door.md`: "⏳ **Fuse length: banked for Gauntlgrym** (ruling 2026-08-10)… **You have to keep a straight face for two sessions.**" Also note the prep's warning that **Tadric is the leak risk** — and Tadric was on screen this session and marched A'lai off. Worth confirming he still hasn't told her.
- **Suggested fix**: None to the recap. Confirm in a GM note that Tadric did not tell Sylvira this session, per the fuse-management ruling.

---

### 46. "the same 'null magic prisms' the party first encountered when they wanted to imprison a drow at the start of this adventure"

- **Location**: Locations → Null Magic Prison
- **Issue**: "prisms" is a transcription garble of "**prisons**" (A'lai's quoted line has "null magic prism," clearly a mishearing). The recap propagates the garble into a Locations entry. Additionally, the back-reference to "the start of this adventure" and an attempted drow imprisonment is not attested in any context document.
- **Evidence**: `world_state.md` §4 Locations: "**Candlekeep Prison** — nullifies all spellcasting; A'lai is desperate to be put in it." `campaign_state.md` uses "magic-nullifying cell." The registry has no "null magic prism." No context doc records an early attempt to imprison a drow at Candlekeep — the captured **House T'sarran spy** is held inside Glabbagool, not in a cell.
- **Suggested fix**: Correct "prisms" → "prisons" in the Locations entry (leave the verbatim quote). Verify the drow-imprisonment back-reference against the transcript before it enters world_state; it may be a conflation with the T'sarran spy.

---

### 47. "the investigator's office, where we can put these notes on the floor" — office proximity claim

- **Location**: Scenes → "Deciphering the Vault Riddles", Locations → Investigator's Office, Null Magic Prison
- **Issue**: The recap asserts twice that the investigator's office is "conveniently near the prison." No context doc places these adjacently.
- **Evidence**: `candlekeep_murders_arc.md` S2 Beat 3: "Bookwyrm gives them an office in **Exaltation**." The registry lists **Exaltation** as a location; the prison is unlocated relative to it. `world_state.md` mentions the Bell Tower having cells.
- **Suggested fix**: Attribute to A'lai's in-scene claim rather than stating as geography, unless the transcript has the GM confirming it.

---

### 48. `world_state.md` internal error — Kalan's title (flag against the grounding doc, not the recap)

- **Location**: N/A — context document defect
- **Issue**: `world_state.md` §4 calls Kalan Strongbranch "Reinstated **Head of the Avowed**," and `campaign_state.md` repeats "Kalan Strongbranch reinstated as **Head of the Avowed**." Per **AUTHORITATIVE CANON**, Kalan is the **Gatewarden**. The Avowed are Candlekeep's senior scholars as a body; "Head of the Avowed" conflates the guard command with the scholarly leadership (which is the First Reader / Keeper of Tomes line).
- **Evidence**: **AUTHORITATIVE CANON** registry: "Kalan Strongbranch — **Gatewarden**; archmage." Registry faction: "The Avowed." `candlekeep_arc_flowchart_v2.md` and `candlekeep_vault_session.md` both use "**Gatewarden**" consistently: "♻️ **Kalan, reinstated** — vindicated." `candlekeep_murders_arc.md` likewise: "**Tadric:** acting Gatewarden."
- **Suggested fix**: Correct `campaign_state.md` and `world_state.md` to **Gatewarden**. This finding rests on the AUTHORITATIVE CANON section overriding the generated grounding docs.

---

### 49. `world_state.md` internal error — A'lai as "ex-Council of Twelve"

- **Location**: N/A — context document defect
- **Issue**: `world_state.md` §4 describes A'lai as "**Drow scholar** (ex-Council of Twelve)." No Council of Twelve exists in the registry or in any Candlekeep prep document. Candlekeep's governing body is the Avowed, with the **Great Readers** as the senior council.
- **Evidence**: **AUTHORITATIVE CANON** registry: "A'lai Aivenmore — **Great Reader**; main antagonist." Registry factions include "Great Readers," "The Avowed," "Keepers of Secrets," "Loremasters," etc. — no Council of Twelve. `candlekeep_murders_arc.md` refers to the "Council of Great Readers" convening in Exaltation. The registry does contain a "**Council of Spiders**" (drow wizards) and a "**Council of Savants**" (Gracklstugh derro) — possible source of the drift.
- **Suggested fix**: Correct `world_state.md` to "Great Reader" or "Council of Great Readers." Flagging against the grounding doc; the recap does not repeat this error.

---

## Summary of priority

**Blocking for next session:**
- **#40** — was the prophecy spoken before the hinge opened? Determines whether Thorin is in a feather-fall shaft or a lethal drop.
- **#39** — two riddle lines are missing from the decoded text ("one last guardian of knowledge remains / to verify the chosen Reader's claims").
- **#27** — Thorin's final reroll is unresolved.
- **#37** — the Manshoon Track value at session end is not recorded, contrary to explicit prep instruction.

**Character-sheet verification needed:** #25 (Telekinesis vs. Telekinetic), #28 (Zalthir hovering), #29 (Zalthir's wings), #24 (44-point heal), #27 (Thorin's reroll source).

**Canon-name corrections:** #12 (School of Drama), #15 (Hall of Momentous Deeds), #32 (Candlekeep not Castle Ward), #46 (prisons not prisms).

**Grounding-doc corrections (canon overrides generated docs):** #48 (Kalan = Gatewarden), #49 (A'lai = Great Reader, no Council of Twelve).

**Largest single risk:** #1 — Kalan Strongbranch is recorded as fled in both grounding docs but is fully present and active in this recap, in two contradictory capacities within the same scene.