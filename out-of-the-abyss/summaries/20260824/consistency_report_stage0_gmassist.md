# Consistency Report — Session 2026-08-24 Recap

## 1. Sentinel Worm / "Miriam" — two canon-level name errors in one phrase

- **Location**: Summary (¶1); Scenes → *Decoding the Cryptogram* (beat 2); NPCs → Silvara Savicas
- **Issue**: The recap gives the guardian's title as "**Sentinel Worm**" and her true name as "**Miriam**." Both are ASR garblings, not canon.
- **Evidence**: The **AUTHORITATIVE CANON** registry lists `Miirym, the Sentinel Wyrm` — "translucent ghost-dragon guardian of Candlekeep (encountered 'Underneath Candlekeep')." The VTT corrections glossary independently confirms both: `Miriam` → **Miirym**, and `sentinel worm` → **Sentinel Wyrm** (flagged there as "Miirym's title; homophone the ASR cannot resolve"). Prep (`20260824_worth_two_faces.md`) uses **Miirym** throughout and gives her true name as **Vydykyq**.
- **Suggested fix**: "…provided the true name of the Sentinel Wyrm, **Vydykyq**…" — and note the separate issue below: *Miirym* is the guardian's **name**, not the answer to the riddle.

## 2. The riddle-1 answer is almost certainly **Vydykyq**, not the dragon's common name

- **Location**: Summary (¶1); Scenes → *Decoding the Cryptogram*; NPCs → Silvara Savicas
- **Issue**: The recap presents "Miriam" as *the true name* Sylvira supplied. Canon and prep both treat **Miirym** as the guardian's ordinary/public name and **Vydykyq** as her *true* name — the thing that has power.
- **Evidence**: Prep `20260824_worth_two_faces.md`, Clever Play #3: *"Sylvira handed them a dragon's true name and they filed it as a riddle answer… **Say Vydykyq.**"* `candlekeep_day_four.md` Beat 2 clue table: clue **1 = Vydykyq**, location Drakonoikos/catacombs, *"Sylvira freebie."*
- **Suggested fix**: Record the answer as **Vydykyq**, with Miirym named as the wyrm it belongs to. This matters for the next session, where speaking Vydykyq is a live mechanical key.

## 3. "Silvara Savicas" — wrong spelling of an established NPC

- **Location**: Summary (¶1); Scenes; NPCs (heading and body)
- **Issue**: Consistently spelled "Silvara Savicas."
- **Evidence**: **AUTHORITATIVE CANON**: `Sylvira Savikas` (aliases: *Savikas*, *Sylvira*). `campaign_state.md` and `world_state.md` both use **Sylvira Savikas**. The VTT glossary explicitly lists `Silvara`, `Silvira Savica`, `Silvira Savika` → **Sylvira Savikas**.
- **Suggested fix**: Replace all instances with **Sylvira Savikas**.

## 4. "Ally Evanmore" — wrong name; this is **A'lai Aivenmore**, and he is a prisoner, not a helper

- **Location**: Summary (¶1); Scenes → *Decoding the Cryptogram*; NPCs → Ally Evanmore; Items → Key to the Inner Sanctum
- **Issue**: Two problems. (a) The name is a garbling. (b) The characterisation — a broken man volunteering his photographic memory to help — omits that he is the arc's **antagonist**, Manshoon's inside man of eleven years, currently **bound in the party's custody** and bargaining for a null-magic cell.
- **Evidence**: **AUTHORITATIVE CANON**: `A'lai Aivenmore` (aliases *Aivenmore*, *A'lai*) — "Great Reader; main antagonist; Manshoon's inside man." VTT glossary lists `Ally Avanmore`, `Ally Evan more`, `Alai Evanmore` → **A'lai Aivenmore**. `campaign_state.md`: *"A'lai Aivenmore — Alive, captured, bound, in the party's custody… Broken; bargaining for a magic-nullifying cell."* Prep Scene 1 has him trading cryptogram lines from captivity.
- **Suggested fix**: Rename to **A'lai Aivenmore** throughout and state his status (bound prisoner, trading information for a null cell) in the NPC entry. A future session reading this recap would otherwise treat him as a friendly scholar.

## 5. "Kaylin Strongbranch" — wrong first name, and his presence contradicts campaign state

- **Location**: Summary (¶1); Scenes → *Decoding the Cryptogram*; NPCs → Kaylin Strongbranch
- **Issue**: (a) Name is **Kalan**, not Kaylin. (b) More seriously, campaign state has Kalan **fled Candlekeep** — "to the wind" — after admitting the fake-key deception. His casual arrival "huffing and puffing" to help with a cipher is unexplained.
- **Evidence**: **AUTHORITATIVE CANON**: `Kalan Strongbranch` (aliases *Strongbranch*, *Kalan*) — "Gatewarden; archmage." VTT glossary records exactly this session's ruling: *"`Kaylin` vs `Kalan` Strongbranch: the registry won. Both transcriptions said *Kaylin*; the module, `entity_registry.yaml`, and the 20260817 VTT all say **Kalan**."* `campaign_state.md`: *"Kalan Strongbranch — Alive — **fled, 'to the wind'** — Whereabouts unknown."* Prep (`20260810_race_to_the_vile_door.md`, Scene 2 branch) treats his return as a **designed beat** requiring a trigger, arriving mid-race.
- **Suggested fix**: Rename to **Kalan Strongbranch**, and add one line establishing his return (did he come back on his own? was Tadric sent? was this a GM ruling?). Otherwise the next prep pass will not know whether the fugitive thread is closed.

## 6. "House of Mechanis" / "Dust of Mechanis" — should be **Mechanus**

- **Location**: Summary (¶3); Scenes → *Gathering the Components*; Locations → House of Mechanis; Items → Dust of Mechanis; NPCs → Spanner
- **Issue**: The plane, the building, and the dust are all spelled *Mechanis*.
- **Evidence**: **AUTHORITATIVE CANON** lists the location `House of Mechanus` and the concept `Mechanus` ("lawful plane, modrons' home"). VTT glossary: `Mechanis, Mechanists, Machinus, methanus` → **Mechanus**. Prep and `candlekeep_day_four.md` Beat 3 both say *"dust of Mechanus."*
- **Suggested fix**: **House of Mechanus**, **Dust of Mechanus**, and "a perfect lubricant from the plane of **Mechanus**."

## 7. The Dust of Mechanus was **not obtained** — the Items entry contradicts the recap's own scene text

- **Location**: Items → Dust of Mechanis ("The party obtained it via the tools lent by Spanner"); Summary (¶3, "the party still needed one final ingredient: the Dust of Mechanis")
- **Issue**: The Items block asserts the party has the dust. The Scenes block says Spanner refused (only a dead modron yields it) and lent **tools instead**. Internal contradiction, and the Items version is the wrong one.
- **Evidence**: `vtt_known_additions.md`, **Modron tool** entry: *"In-session substitution for the riddle's stated component: the cryptogram calls for **dust of Mechanus**, which the party never obtained… The GM ruled the tool an acceptable alternative. This is what the party is carrying into the Vault."* Prep `20260824_worth_two_faces.md` carry-forward table: *"Dust of Mechanus — **The dust does not exist yet**."*
- **Suggested fix**: Rewrite the Items entry: the dust was **not** obtained; the party carries Spanner's **mechanist tools** as a GM-ruled substitute. This is load-bearing for riddle line 4.

## 8. Riddle line 3 (the prophecy) is never mentioned — the recap loses the reason the trap fired

- **Location**: Summary (¶4); Scenes → *The Descent and the Trap*
- **Issue**: The recap presents the staircase trap as an unmotivated ambush ("Without warning, a ten-foot section of the staircase hinged open"). Prep is explicit that the trap fired **because the party skipped riddle line 3** — *"utter the original prophecy to unseen ears."*
- **Evidence**: `20260824_worth_two_faces.md`: *"⭐ **The riddle is two-sixths done, and the party does not know that.** … 3 | Utter the original prophecy to unseen ears | ❌ **skipped** … They skipped step 3 and the stair told them so."* The riddle text itself is in `candlekeep_day_four.md` Beat 3.
- **Suggested fix**: This may be deliberate (the players genuinely don't know yet). But flag it: if the recap is the future session's memory, a note in the Scenes block — even "the party does not yet know why the stair opened" — prevents next session's prep from re-deriving it.

## 9. Fall distances are internally inconsistent (500 ft vs 1,500 ft vs "1,500 ft" in Memorable Moments)

- **Location**: Summary (¶5); Scenes → *The Long Descent*; Memorable Moments (Dawnbringer quote annotation)
- **Issue**: Zalthir catches Thorin at ~500 ft; the party lands ~1,500 ft down; the Memorable Moments annotation says Thorin "plummets 1,500 feet." The shaft is canonically **1,000 ft**.
- **Evidence**: `candlekeep_day_four.md` Beat 5: *"**`Feather fall` shaft, 1000 ft.**"* `20260810_race_to_the_vile_door.md`, Scene 3: *"it's a 1,000-ft `feather fall` shaft."* Prep `20260824_worth_two_faces.md` cold open describes "a thousand feet" and an alcove "at the four-hundred-foot mark."
- **Suggested fix**: Reconcile against the transcript. If play established 1,500 ft, note it as a GM revision; otherwise correct to ~1,000 ft. As written, the three figures cannot all be right.

## 10. "Aloando" — should be **Alaundo**

- **Location**: Throughout — Summary (¶1, ¶2, ¶4); Scenes; Locations → House of Aloando, Keepers' Grove; Items → Statue of Aloando
- **Issue**: The seer's name is spelled *Aloando* everywhere.
- **Evidence**: **AUTHORITATIVE CANON**: `Alaundo the Seer` (alias *Alaundo*) — "the historical prophet whose 99 prophecies the Endless Chant recites"; location `The House of Alaundo`. VTT glossary: `Aluando, Alando, Alwando, Alondo, Luando, Al Londo, Elando, Londo, Orlando, **Aloando**, Aluander` → **Alaundo**.
- **Suggested fix**: Replace all with **Alaundo** / **House of Alaundo** / **Statue of Alaundo**.

## 11. "Founder's Court" — canon is **Founders Court**

- **Location**: Summary (¶1); Scenes; Locations → Founder's Court; NPCs → Kaylin Strongbranch; Items → Statue of Aloando
- **Issue**: Apostrophe placement.
- **Evidence**: **AUTHORITATIVE CANON** location: `Founders Court`. VTT glossary explicitly: `Founder's Court` → **Founders Court**.
- **Suggested fix**: **Founders Court** throughout.

## 12. "Orrey of the Astronomicon" — should be **Orrery**

- **Location**: Summary (¶1); Scenes → *Decoding the Cryptogram*; NPCs → Silvara Savicas
- **Issue**: "Orrey" (twice), and the standalone reference "seen inside the Orrey."
- **Evidence**: **AUTHORITATIVE CANON**: `The Astronomicon` — "contains **The Orrery** and Stargazer." VTT glossary: `Ori` → **Orrery**; `Astronomicron` → **Astronomicon** (with a note that the module spelling outranked both transcriptions).
- **Suggested fix**: **Orrery of the Astronomicon**.

## 13. Limniz is described only as "a star" — the constellation is missing

- **Location**: Summary (¶1); Scenes; NPCs → Silvara Savicas
- **Issue**: The recap says Sylvira "identified the star Limniz from the charts." Canon ties Limniz specifically to **Mystra's Mantle**.
- **Evidence**: `vtt_known_additions.md`, **Limniz** entry: *"identified the eastern light of **Mystra's Mantle**, Limniz… the easternmost star of the **Mystra's Mantle** constellation, looked up in the Orrery of the Astronomicon."* Same entry warns the transcripts said "Mystara's"/"Mistara's" and both were corrected to **Mystra**.
- **Suggested fix**: "…identified **Limniz**, the easternmost star of **Mystra's Mantle**, from the charts of the Orrery of the Astronomicon."

## 14. "Edvaldo Sedanur" recognises "early Candlekeep architecture" — and is treated as reliable

- **Location**: Summary (¶6); Scenes → *The Lava Chamber and the Obsidian Tower*; NPCs → Edvaldo Sedanur
- **Issue**: The recap describes Edvaldo as "An **Avowed** scholar specializing in the history of Candlekeep" who "provided key historical data." Prep flags this scholar as a **doppelganger** whose entire cover is unverifiable local-history expertise, and the recap states his credentials as fact.
- **Evidence**: `20260824_worth_two_faces.md`, *The Scholar*: *"**The party hired a doppelganger…** He is **unnamed on tape.** Nothing to violate, nothing to retcon."* And: *"⛔ Do not tip this."* Separately, `vtt_known_additions.md` confirms **Edvaldo Sedanur** as GM-approved new canon (spelling from the second transcription; this VTT rendered *Cedanur*) — so the **name is right**, but nothing attests "Avowed" or "specializing in the history of Candlekeep" as verified fact.
- **Suggested fix**: Keep the name. Soften the NPC entry to what the party *observed* — a scholar who says he specialises in Candlekeep history — rather than asserting his affiliation. Also note that the height figure ("over 500 feet") is his claim, not confirmed.

## 15. Manshoon is described as the man himself; canon has him as a **simulacrum**

- **Location**: Summary (¶9–11); Scenes → *The Vault of Dangerous Secrets*; NPCs → Manshoon
- **Issue**: The recap calls him "the legendary wizard Manshoon" and "Manshoon himself," with no indication he is a construct.
- **Evidence**: **AUTHORITATIVE CANON**: `Manshoon` — "appears as **Manshoon's Simulacrum**." `campaign_state.md`: *"**Manshoon's simulacrum then breached the keep**, shattering the security-control-room door with a `wall of force`."* Prep `20260824_worth_two_faces.md` is built entirely around **two simulacra** ("Worth Two Faces"), and notes Daz has field-perception on the *not-quite-there* nature of a simulacrum.
- **Suggested fix**: Note explicitly that this is (or is believed to be) **a simulacrum**, not the man. Whether the party has realised it yet is a separate question worth recording — it changes how the next session's fight reads.

## 16. The dragon guardian is unnamed in the recap despite being the same NPC as issue #1

- **Location**: Summary (¶8); Scenes → *The Spectral Silver Dragon's Trial*; Locations → The Lava Cavern; NPCs → Spectral Silver Dragon; Memorable Moments
- **Issue**: The "spectral silver dragon" is described as an anonymous guardian — while, six paragraphs earlier, the recap has Sylvira supplying "the true name of the Sentinel Worm." These are the same creature (**Miirym / Vydykyq**), and the recap never connects them.
- **Evidence**: **AUTHORITATIVE CANON**: `Miirym, the Sentinel Wyrm` — "translucent ghost-dragon guardian of Candlekeep (encountered 'Underneath Candlekeep')." Prep Scene 3 is titled *"Vydykyq, the Last Guardian of Knowledge"* and describes exactly this encounter: a spectral silver dragon on the bridge, lava glow passing through her, verifying the Reader's claims (riddle line 5).
- **Suggested fix**: Identify her as **Miirym, the Sentinel Wyrm** (true name **Vydykyq**) in the NPC block. This is the single most consequential fix in the report — the party is holding her true name and may not know it.

## 17. The riddle-5 "verification" framing is lost

- **Location**: Scenes → *The Spectral Silver Dragon's Trial*; Summary (¶8)
- **Issue**: The recap frames the dragon encounter as her "testing their knowledge" and offering a boon. Canon frames it as **riddle line 5** — *"One last guardian of knowledge remains to verify the chosen Reader's claims"* — a procedural gate, not an optional trial.
- **Evidence**: `candlekeep_day_four.md` Beat 3 riddle text; `20260824_worth_two_faces.md` Scene 3 heading: *"⭐ **Riddle line 5.**"* Daz identifying himself as "the Reader" is precisely this mechanic.
- **Suggested fix**: Note that this satisfied riddle line 5 and that Daz is now the **verified Reader** — a status with mechanical consequences (asking the vault for things; Manshoon by contrast is unverified and, by the keep's own law, a thief).

## 18. Two guardian chambers are conflated — "a previous owlbear statue lay destroyed on the floor"

- **Location**: Summary (¶7); Scenes → *The Spectral Silver Dragon's Trial* (last beat); NPCs → Iron Owlbear Guardian
- **Issue**: The recap has the party pass a *living* iron owlbear's riddles, and then notice *"a previous owlbear statue lay destroyed on the floor."* Canon places the destroyed owlbear on the **lava-chamber threshold**, killed by Manshoon before the party arrived — not as a second statue inside.
- **Evidence**: `candlekeep_day_four.md` Beat 6 and `20260810_race_to_the_vile_door.md` Scene 3: *"On the threshold lies the Iron Owlbear's corpse — beak intact, three skull-frame screws sheared."* Verbatim trophy plant: *"The owlbear's iron beak is intact… It would come away with one good wrench."* Prep `20260824_worth_two_faces.md` assigns the kill to **Simulacrum B**.
- **Suggested fix**: Clarify where the destroyed owlbear was found (threshold vs. interior), and whether the beak was claimed — it is a designed trophy and a future session will look for it.

## 19. Counterspell: the Scenes block and the Spells block flatly contradict each other

- **Location**: Scenes → *The Vault of Dangerous Secrets* ("Manshoon uses his counterspell to attempt to nullify the attack, but Daz's spell still partially takes effect"); Spells → Counterspell ("Manshoon briefly considered using this… but ultimately chose not to burn it")
- **Issue**: One says he cast it and it partly failed; the other says he declined to cast it. These cannot both be true.
- **Evidence**: Internal contradiction within the recap. Prep treats his slot economy as load-bearing (`20260810_race_to_the_vile_door.md`: *"Counterspelled twice → professional insult; he leaves if he can"*; and for simulacra, *"⛔ Simulacra can never regain slots — ever"*), so which slots he has spent matters mechanically next session.
- **Suggested fix**: Resolve against the transcript and record a single version. If he did *not* counterspell, that is a slot still in hand.

## 20. "Phantasmal Killer" resisted "through sheer force of will… but the attack still found purchase"

- **Location**: Summary (¶11); Scenes; NPCs → Manshoon; Spells → Phantasmal Killer
- **Issue**: Mechanically muddled. *Phantasmal Killer* deals no damage on a successful save; a successful save ends nothing "partially." "Resisted the full brunt but still suffered psychic damage" describes no standard outcome.
- **Evidence**: Standard 5e spell behaviour. Prep notes Manshoon has **Magic Resistance** (advantage on saves vs. spells) and **Legendary Resistance 3/day** (shared across the pair) — either of which could produce a narrated "resisted through sheer will," but both result in *no* effect, not partial.
- **Suggested fix**: State plainly what happened — saved outright, failed and took damage, or burned a Legendary Resistance. **If a Legendary Resistance was spent, that must be recorded**: prep says the pair share only three, and *"the shape of this fight is Zalthir burning all three resistances and then the fourth Stunning Strike landing."*

## 21. Only **one** Manshoon is described — the second body is unaccounted for

- **Location**: Summary (¶9–11); Scenes → *The Vault of Dangerous Secrets*; NPCs → Manshoon
- **Issue**: The recap tracks a single Manshoon from the vault desk down to the duel. Prep's central structural element is **two simulacra**, with B hidden in the stacks and stepping out when A drops or when the party turns for the riddle door.
- **Evidence**: `20260824_worth_two_faces.md`: *"**Two bodies. That is the twist and it is the title of this document.**"* Statblock deltas: A at HP 95 / AC 19 (robe + staff), B at HP 95 / AC 15, shared slot pool, 3 shared Legendary Resistances, 2 shared legendary actions.
- **Suggested fix**: Verify against the transcript whether B was revealed, spotted, or is still concealed. If concealed, the recap is fine as written but should not imply the fight is a single-opponent encounter — next session's prep depends on knowing whether the party knows.

## 22. "Grygum named the holy triumvirate that patroned the great library" — check the phrasing, not the facts

- **Location**: Summary (¶7); Scenes → *Riddles of the Iron Guardian*; canon check
- **Issue**: Not an error — **Oghma, Deneir, Milil** are all canon deities in the registry, and Candlekeep's traditional patrons. Flagging only that "patroned" and "holy triumvirate" are the recap's own phrasing, not attested canon terminology.
- **Evidence**: **AUTHORITATIVE CANON** deities: `Oghma`, `Deneir`, `Milil`. No registry entry for "holy triumvirate."
- **Suggested fix**: Optional. Keep the three names; consider "the three gods who patronise the library" unless the transcript uses "triumvirate" verbatim.

## 23. "Key to the Inner Sanctum" — an Items entry describing a *prior* session's event

- **Location**: Items → Key to the Inner Sanctum
- **Issue**: This item is described as "stripped from Ally Evanmore after the battle in the high tower and given to Glabbagool for safekeeping" — an event from Ch62–63, not this session. It appears in a Ch64/65 recap with no indication it is a carry-forward, and it uses the wrong name (see #4).
- **Evidence**: `campaign_state.md`: *"The party later stripped that key from A'lai and hid it inside Glabbagool."* Note also the naming: canon and campaign docs call these **High Tower keys**, not "key to the Inner Sanctum" — the VTT glossary lists `Hightower Keys` → **High Tower Keys**.
- **Suggested fix**: Either drop the entry (it is not a this-session item) or relabel it **A'lai Aivenmore's High Tower key**, carried forward from Ch62–63.

## 24. Level: recap implies status quo; party levelled

- **Location**: Not stated anywhere in the recap
- **Issue**: No mention of levelling, but the party document is known-stale and prep records a level change.
- **Evidence**: `20260824_worth_two_faces.md`: *"**Party level** | 9 | 9 ✓ — `party.md` still says 8, it is stale, ignore it"* and Decision §4: *"**Level 10 at the cut** — after the choice, not before."* `party.md` in context lists all four PCs at level 8.
- **Suggested fix**: Note the party's current level in the recap if it changed this session, and flag `party.md` as needing a hand-update — it is two levels behind by the time this arc closes.

## 25. Minor: "the grove where Candlekeep's keepers of tomes are buried"

- **Location**: Summary (¶2); Scenes; Locations → Keepers' Grove
- **Issue**: The recap coins "Keepers' Grove." Canon has a location simply called **The Grove**.
- **Evidence**: **AUTHORITATIVE CANON** location: `The Grove`. No registry entry for "Keepers' Grove."
- **Suggested fix**: Use **The Grove** unless the transcript establishes the longer name; otherwise a coined place-name will propagate.

---

## Summary of highest-priority fixes

| Priority | Fix |
|---|---|
| **Critical** | #1/#2/#16 — **Miirym, the Sentinel Wyrm**; true name **Vydykyq**; she is the spectral silver dragon |
| **Critical** | #4 — **A'lai Aivenmore**, and he is a *bound prisoner*, not a helpful scholar |
| **Critical** | #7 — the party does **not** have the Dust of Mechanus; they have Spanner's tools as a GM-ruled substitute |
| **High** | #5 — **Kalan** Strongbranch, and explain how a fugitive is back in the room |
| **High** | #15/#21 — Manshoon is a **simulacrum**, and there may be **two** |
| **High** | #19/#20 — resolve the counterspell contradiction and the Phantasmal Killer mechanics (Legendary Resistance count is load-bearing) |
| **Medium** | #3, #6, #10, #11, #12 — spelling: Sylvira Savikas, Mechanus, Alaundo, Founders Court, Orrery |
| **Medium** | #9 — reconcile the three different fall distances |
| **Medium** | #14 — do not assert Edvaldo's credentials as verified fact |