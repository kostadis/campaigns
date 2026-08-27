# Consistency Report — Session 2026-08-17 Recap

## HIGH CONFIDENCE ISSUES

**1. Location: Summary (¶1), Scenes → "The Aftermath at the High Tower", NPCs → Manshoon**
- **Issue**: The recap repeatedly identifies the arriving wizard as "the legendary wizard Manshoon" himself, arriving in person. Campaign state and world state consistently record the entity that breached Candlekeep as **Manshoon's simulacrum**, not Manshoon.
- **Evidence**: `campaign_state.md`: "**Manshoon's simulacrum then breached the keep**, shattering the security-control-room door with a `wall of force`." `world_state.md` §1: "**MANSHOON'S SIMULACRUM IS INSIDE CANDLEKEEP.**" The AUTHORITATIVE CANON registry entry for Manshoon reads: "appears as **Manshoon's Simulacrum**." The prep doc `20260810_race_to_the_vile_door.md` note 8 explicitly scopes this: the CR-6 simulacrum block "remains **correct for the ch63 Candlekeep breach**, which was the simulacrum (GM ruling, 2026-08-19)."
- **Suggested fix**: Replace "Manshoon" with "Manshoon's simulacrum" (or "a simulacrum of Manshoon") in the breach narration, and note in the NPC entry that the figure in the keep is a simulacrum. The recap's read that it is the man himself is a live GM decision point, not established canon.

**2. Location: Summary (¶2), Scenes → "Deciphering the Vault Riddles", NPCs → Kalan Strongbranch, Memorable Moments**
- **Issue**: Kalan Strongbranch is described as present, cooperative, transcribing the cryptogram from memory and arriving late at the investigator's office. Per campaign state as of Ch.63, Kalan has **fled** Candlekeep after admitting the fake-key deception; his whereabouts are unknown.
- **Evidence**: `campaign_state.md` NPC table: "Kalan Strongbranch | Alive — **fled, 'to the wind'** | Whereabouts unknown." `world_state.md` §4: "admitted it when confronted, then ran. 'Kalan is to the wind.'" `party.md`: "Alive, **fled** after admitting he handed them a fake key."
- **Suggested fix**: Either (a) the session depicts Kalan's return — in which case the recap should say so explicitly ("Kalan Strongbranch, returned from wherever he had fled…") and campaign_state needs updating, or (b) this is the wrong NPC and the transcriber should verify who actually transcribed the cryptogram. The prep doc anticipates a mid-race Kalan return (`20260810_race_to_the_vile_door.md`, Scene 2 branch: "he turns up on his own"), so (a) is plausible — but the recap must not silently assume it.

**3. Location: Summary (¶2), Scenes → "Deciphering the Vault Riddles", NPCs → Kalan Strongbranch**
- **Issue**: Kalan Strongbranch is given two mutually contradictory roles in the *same* session: he transcribes the cryptogram in full at the investigator's office (¶2, sentence 1) *and* he "arrived huffing and puffing moments later" with a clue, "only to find the party had already cracked the entire cipher" (¶2, final sentence; also a Memorable Moment). He cannot both be the one who spread the riddles across the floor and the one who arrived late to find them already solved.
- **Evidence**: Internal to the recap; both claims appear in the Summary and are duplicated in Scenes and Memorable Moments.
- **Suggested fix**: Determine which NPC did which. It is likely one of these is a different Candlekeep figure (Tadric? Fembris Lancer?) — verify against the transcript.

**4. Location: Summary (¶2), Scenes → "Deciphering the Vault Riddles", NPCs → Sylvira Savikas**
- **Issue**: Sylvira Savikas is described as arriving under her own power and being physically present ("Sylvira Savikas arrived shortly after," "when she passed [the Orrery]"). Campaign state records her as **bedridden and dying of abyssal plague**.
- **Evidence**: `campaign_state.md`: "Sylvira Savikas | Alive, dying of abyssal plague | **Bedridden, Candlekeep**." `world_state.md` §4: "Curator of the Infernal Fortress (tiefling)… **Bedridden.**"
- **Suggested fix**: If she rose from her sickbed for this crisis, say so — it is a character beat worth recording, and campaign_state's "bedridden" should be updated. If the recap simply assumed mobility, correct it.

**5. Location: Summary (¶3), Scenes → "The Grave of Alaundo and the House of Mechanus", Locations → The Grove**
- **Issue**: The recap states the party learned Alaundo "died at the age of ninety-seven" from his grave in the Grove. The 97 is canonically the number of *steps*, derived from the riddle's "tread as many steps as he lived in years" — but the recap presents the grave as the *source* of the number, which is a substantive factual claim about Alaundo's lifespan.
- **Evidence**: `world_state.md` §4 Locations: "**The Vault** (beneath the House of Alaundo, via **97 steps** and a lava chamber)." `candlekeep_day_four.md` Beat 3: "**97 steps:** Inda the half-orc librarian knows from devotion." The prep material sources the number from **Inda**, not from a grave inscription. Whether Alaundo's actual age at death is 97 (vs. the step count coinciding by design) is not attested anywhere in context.
- **Suggested fix**: Verify against transcript. If the grave scene happened, it is new canon and fine — but flag that the prep docs assigned this knowledge to Inda, who does not appear anywhere in this recap despite being the House of Alaundo's designated NPC.

**6. Location: Scenes → "The Statue of Alaundo", NPCs (absent)**
- **Issue**: **Inda** does not appear anywhere in the recap, despite being the canonical House of Alaundo NPC who fills the inkpot and knows the 97 steps. The recap has the party borrowing ink from unnamed "assembled scholars."
- **Evidence**: AUTHORITATIVE CANON registry: "Inda | npc | House of Alaundo; half-orc, secretly worships Alaundo as a deity." `candlekeep_day_four.md` Beat 5: "**Inda fills the inkpot.** Statue slides." `candlekeep_vault_session.md` Beat 4: "**Inda** emerges. *'You are going to the Vault. The Seer foresaw you. May I walk you to the inkpot?'*"
- **Suggested fix**: Confirm whether Inda was present at the table. If she was and was omitted, add her. If she was genuinely skipped, note it — it is a live thread (she also seals the staircase in the finale script).

**7. Location: Summary (¶3), Scenes, NPCs → Spanner**
- **Issue**: Spanner is called "the gnome librarian." The `vtt_known_additions.md` entry from *this very session* records him as a **modron** librarian.
- **Evidence**: `vtt_known_additions.md`: "**Spanner** — 20260817 — 'Under the direction of Spanner, the librarian' — 2026-08-21 — **modron librarian**, House of Mechanus; both transcriptions agree." AUTHORITATIVE CANON registry is neutral: "Spanner | npc | House of Mechanus librarian; directs the 13 modrons." Note the registry says he *directs* the modrons, which reads more naturally as a non-modron overseer — but "gnome" is attested nowhere.
- **Suggested fix**: Resolve Spanner's species against the transcript. "Gnome" appears to be an unsourced addition; either the additions-file note or the recap is wrong. Do not let "gnome librarian Spanner" enter canon unverified.

**8. Location: Summary (¶3), Scenes → "The Grave of Alaundo and the House of Mechanus"**
- **Issue**: The recap says the party "persuaded Spanner to lend them the tools" and that obtaining the dust requires killing a modron or using specialized tools. The prep script says the dust is **given freely under siege**.
- **Evidence**: `candlekeep_day_four.md` Beat 3: "**Mechanus dust:** Spanner gives a bag freely under siege."
- **Suggested fix**: Not an error if the table played it differently — GM prerogative — but flag that this diverges from prep and that the "kill a modron or use tools" framing is new canon requiring no further verification only if the transcript supports it.

## MEDIUM CONFIDENCE ISSUES

**9. Location: Summary (¶1), Scenes → "The Aftermath at the High Tower", Locations → High Tower**
- **Issue**: The recap says Manshoon "shattered the magically protected door… breaching the inner sanctum" and repeatedly calls the target "the inner sanctum." Canon names this room the **Security Control Room**.
- **Evidence**: `world_state.md` §4 Locations: "**Security Control Room** — held the artifacts governing Candlekeep's wards behind a door requiring both keys; **Manshoon shattered it with `wall of force`**." `campaign_state.md` uses "security-control-room door" throughout. "Inner sanctum" is not an attested Candlekeep location in the registry.
- **Suggested fix**: Replace "inner sanctum" with "Security Control Room" throughout, or note it as an in-fiction descriptive phrase rather than a place name.

**10. Location: Summary (¶2), Scenes, Memorable Moments, NPCs → Batbayar**
- **Issue**: The bard's name is rendered **Batbayar**. The VTT corrections glossary maps the mis-hearings "Bathayar, Pfaffayar" to **Bauthoyar** — but the AUTHORITATIVE CANON registry has **Batbayar**.
- **Evidence**: AUTHORITATIVE CANON registry: "Batbayar | npc | legendary halfling bard whose statue dominates the School of Drama." `vtt_transcription_corrections.md`: "| Bathayar, Pfaffayar | **Bauthoyar** |".
- **Suggested fix**: **Canon wins — the recap's "Batbayar" is correct.** The error is in `vtt_transcription_corrections.md`, which should be updated to map the mis-hearings to **Batbayar**, not "Bauthoyar." Flagging the glossary, not the recap. This finding rests on the AUTHORITATIVE CANON section.

**11. Location: Locations → School of the Drama Library, Summary (¶2)**
- **Issue**: The venue is called "the School of the Drama Library." Canon names it **The School of Drama**.
- **Evidence**: AUTHORITATIVE CANON registry: "The School of Drama | location." Registry note on Batbayar: "whose statue dominates the **School of Drama**." `candlekeep_day_four.md` clue table: "School of Drama (Batbayar)."
- **Suggested fix**: "School of Drama." This finding rests on the AUTHORITATIVE CANON section.

**12. Location: Locations → Founders' Court, Summary (¶3)**
- **Issue**: Rendered "Founders' Court" (with apostrophe). Canon registry has **Founders Court** (no apostrophe). The `vtt_known_additions.md` file notes the transcript itself was inconsistent ("Zoom wrote Founder's/Founders").
- **Evidence**: AUTHORITATIVE CANON registry: "Founders Court | location." `vtt_known_additions.md`: "**Founders' Court** — 20260817 — … Candlekeep location; Zoom wrote Founder's/Founders."
- **Suggested fix**: Use **Founders Court** per canon. Low stakes but worth normalizing before it forks. This finding rests on the AUTHORITATIVE CANON section.

**13. Location: NPCs → Miirym, Summary (¶2)**
- **Issue**: Miirym is described as "the sentinel worm and dragon guardian of Candlekeep" and referred to as "Her." Canon calls her **Miirym, the Sentinel Wyrm** — *wyrm*, not *worm*. The recap's "sentinel worm" appears twice.
- **Evidence**: AUTHORITATIVE CANON registry: "Miirym, the Sentinel **Wyrm** | npc | translucent ghost-dragon guardian of Candlekeep." `vtt_transcription_corrections.md` maps "Miriam → **Miirym**" but does not cover the wyrm/worm split.
- **Suggested fix**: "Miirym, the Sentinel Wyrm." "Worm" is a homophone error that would badly confuse future sessions given the Underdark's actual purple worms. This finding rests on the AUTHORITATIVE CANON section. Also add a `worm → wyrm` row to the VTT glossary.

**14. Location: Locations → Orrery of the Astronomicon, Summary (¶2)**
- **Issue**: Rendered as one compound location, "the Orrery of the Astronomicon." Canon treats **The Astronomicon** as the location, which *contains* **The Orrery**.
- **Evidence**: AUTHORITATIVE CANON registry: "The Astronomicon | location | aliases: Astronomicon | note: contains **The Orrery** and **Stargazer**."
- **Suggested fix**: "the Orrery, in the Astronomicon" — a minor phrasing fix, but keeps the containment relationship legible.

**15. Location: Items → Sapphire Gem**
- **Issue**: The recap says the sapphire "had long since passed to Grygum's possession." Campaign state confirms Grygum holds it — but the recap describes this as though it were established *this session*, when it is prior-session state (Ch.62–63), and the sentence attributes the assassin's search to "A'lai's assassin" in past tense within a Memorable Moment that appears to be recapping *last* session's events, not this one.
- **Evidence**: `campaign_state.md` Key resources: "**Grygum: the real High Tower key, the fake key, and the stolen sapphire** — smashing the sapphire recalls a key to the holder's hand, which is why the Zhentarim assassin went for Daz and found nothing." The assassin is dead (killed by Thorin, Ch.63).
- **Suggested fix**: The fact is correct; the *placement* is the problem. The first Memorable Moment quote ("Took your time. I've been in the room…") and its context both describe the **previous** session's assassin encounter, not this one. Move or remove — a future reader will think an assassin attacked this session.

## LOW CONFIDENCE / VERIFY

**16. Location: Scenes → "The Descent into the Vault"**
- **Issue**: Two contradictory accounts of who caught themselves. The Summary says "Zalthir seized the stable stone and scrambled to safety, and Grygum managed to hold on." The Scene bullets say "Zalthir uses his strength to hold on and scrambles to safety" and separately "Grygum manages to scramble to safety." Minor, but the verbs are swapped between the two passes.
- **Suggested fix**: Pick one rendering and use it in both places.

**17. Location: Scenes → "The Descent into the Vault"**
- **Issue**: "Daz attempts to use magic to seize the collapsing stairs and halt the fall" — this is not listed in the Summary and reads like Maximilian's Earthen Grasp or Telekinetic. Daz does have both on his sheet, so this is mechanically valid, but the recap does not name the spell.
- **Evidence**: `world_state.md` §2 Daz: "Maximilian's Earthen Grasp… Telekinetic." `party.md` confirms.
- **Suggested fix**: Name the spell if the transcript does; otherwise this is fine.

**18. Location: Items → Potion of Flying**
- **Issue**: Listed as "in the party's possession… noted as a potential resource for Daz." The potion is specifically **concealed inside Glabbagool**, who is fused to **Zalthir's** forearm — so retrieving it for Daz is a non-trivial action, not a simple hand-off.
- **Evidence**: `world_state.md` §2 Zalthir key items: "Potion of Flying (concealed in Glabbagool)." `party.md`: "a Potion of Flying concealed inside Glabbagool."
- **Suggested fix**: Note the custody chain, or drop the item entry if it was only discussed and not used.

**19. Location: Scenes → "The Prisoner's Bargain", NPCs → Tadric**
- **Issue**: Tadric is described as taking A'lai into custody and marching him to the prison. Campaign state has Tadric "holding the ward lattice by hand" — he is the single point of failure keeping Candlekeep's wards up.
- **Evidence**: `campaign_state.md`: "Tadric | Alive | Candlekeep — **holding the ward lattice by hand**." `world_state.md` §4: "Now hand-holding the failing ward lattice." The prep doc explicitly notes Tadric "has not slept in a day and a half and is hand-holding the ward lattice. He genuinely does not have a free hour."
- **Suggested fix**: Not an error if the GM moved him — but flag that Tadric leaving his post has ward consequences, and the prep doc used his immobility as a deliberate fuse-holding device for the Sylvira/Moziqodo reveal. If Tadric is now mobile and escorting prisoners, **the Sylvira fuse is exposed** (he is the only living person who knows Moziqodo was her son). This is a downstream GM decision worth surfacing.

**20. Location: Summary (¶1), Scenes → "The Aftermath at the High Tower"**
- **Issue**: "After eleven years of service, he had not even been worth the effort of a single spell" / "he was not even worth the spell slot." Canon has A'lai as Manshoon's inside man for eleven years and **31 years at Candlekeep** — the recap's eleven-year figure is correct for the Manshoon relationship. No error, but the phrasing "eleven years of service" could be misread as tenure at Candlekeep.
- **Evidence**: `world_state.md` §4: "**Manshoon's inside man for eleven years** — 31 years at Candlekeep."
- **Suggested fix**: "After eleven years serving Manshoon…" for clarity.

## NOTES ON THINGS THAT ARE CORRECT

- **House Baenre** as A'lai's deduction is correctly recorded as *his* inference, not established fact. Good. (Prep doc: he is **wrong** — the patron is Vizeran DeVir — and the DeVir name must not surface at Candlekeep.) The recap's framing ("concluded with quiet certainty") preserves this correctly.
- **A'lai's request for the null magic prison**, the withheld depository contents, and the Glabbagool key-storage are all consistent with campaign_state.
- **"Fustilugs"** spelling matches the VTT glossary correction (`Fustelugs → Fustilugs`).
- **A'lai Aivenmore**, **Zalthir**, **Grygum**, **Thorin**, **Daz**, **Glabbagool**, **Manshoon**, **Alaundo** all spelled per canon.
- **Thirteen modrons** matches the registry note on Spanner ("directs the 13 modrons").