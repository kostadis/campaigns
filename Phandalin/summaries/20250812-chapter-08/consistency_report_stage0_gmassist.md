# Consistency Report — Chapter 8 Recap ("Tower of Storms")

## Canon errors (rest on the AUTHORITATIVE entity registry)

**1. Moesko is a half-orc, not an orc**
- **Location**: Summary (throughout), Memorable Moments ("lone orc anchorite," "the orc's final hit point"), Scenes ("Showdown with Moesko"), NPCs, Items ("Octopus Hide Armor"), Locations
- **Issue**: The recap calls Moesko an "orc anchorite" at least six times.
- **Evidence**: AUTHORITATIVE CANON — `entity_registry.yaml`: "Moesko — **Half-orc** anchorite of Talos who guards the Tower of Storms lighthouse." (The registry also confirms this for the parallel anchorites: Grannoc is "half-orc"; the Anchorites of Talos are half-orc worshippers per the Neverwinter Wood location note.)
- **Suggested fix**: Replace "orc" with "half-orc" in every reference to Moesko.

**2. "Myral" should be "Miraal" — and must not drift to "Meril"**
- **Location**: Summary ("stolen from a sea elf named Myral"), Items ("originally taken from Myral the Sea Elf")
- **Issue**: Wrong spelling of the sea elf's name.
- **Evidence**: AUTHORITATIVE CANON — `entity_registry.yaml`: "Miraal — Sea elf slain by Moesko; her spirit haunts the Haunted Cave as a banshee, seeking return of her opalescent conch." The VTT glossary confirms Mirelle/Mirale/Miral/etc. are known garbles of **Miraal**. Note that `world_state.md` itself carries the variant "Miral" in two places (ch09 timeline, Leilon thread) — per trust tiering, that is world_state's error, not license for the recap. Also note the registry's `rejected_aliases` explicitly separates **Meril** (Soma's mentor) from **Miral** — a corrector must not "fix" Myral toward Meril.
- **Suggested fix**: "Myral" → "Miraal" in both places.

**3. Shipwrecks attributed to the harpies; canon attributes them to Moesko's beacon**
- **Location**: Summary ("the graveyard of ships the harpies had lured to their doom"), Scenes ("wrecks of ships lured to their doom by the harpies")
- **Issue**: The recap makes the harpies the cause of the ship graveyard.
- **Evidence**: AUTHORITATIVE CANON — `entity_registry.yaml`: Moesko "guards the Tower of Storms lighthouse, **using the beacon to wreck ships**." `campaign_state.md` corroborates: destroying Moesko's heart "extinguished" the "corrupted green beacon" and "the Tower's curse ended." The harpies charm individual sailors, but the wrecking engine is the beacon — the recap's framing could mislead the ch9 heart-destruction payoff.
- **Suggested fix**: Reword to something like "the graveyard of ships wrecked beneath the tower's corrupted beacon" (harpies may still be described as preying on survivors/sailors).

## Contradictions against campaign context

**4. Who killed Moesko — Brewbarry (recap) vs. Soma (campaign_state)**
- **Location**: Summary (final paragraph), Memorable Moments ("Brewbarry delivers the killing blow on Moesko"), Scenes ("Brewbarry delivers the final, crushing blow")
- **Issue**: The recap credits Brewbarry with the killing blow; the campaign state credits Soma.
- **Evidence**: `campaign_state.md`, Completed Encounters: "Tower of Storms — Moesko the Anchorite Encounter (area T7): Moesko killed; **Soma delivered final blow**." The canon registry is silent on the killer, so this is recap-vs-grounding-doc, not recap-vs-canon. Note the recap builds a whole narrative beat on Brewbarry's kill ("who had spent much of the night missing everything in sight… delivered a single, decisive blow"), so if campaign_state is right, three sections of the recap are wrong; if the recap is right, campaign_state needs a correction.
- **Suggested fix**: Verify against the session VTT/transcript (the authoritative tier) and correct whichever document is wrong. Do not let both attributions persist.

**5. Soma's pronoun — "his"**
- **Location**: Spells ("Wild Shape — Soma used **his** druidic power to transform")
- **Issue**: Wrong pronoun for Soma.
- **Evidence**: `party.md` ("She is patient, maternal…"), `world_state.md` ("Declared an honorary citizen of Phandalin so **she** could qualify"; "glows to detect… **she** was able to keep it"). Both grounding docs consistently use she/her; the registry does not contradict.
- **Suggested fix**: "his" → "her."

## Internal inconsistencies within the recap

**6. Harpy kill count doesn't reconcile between Summary and Scenes**
- **Location**: Summary (paragraph 4) vs. Scenes ("The Harpy's End")
- **Issue**: The Summary accounts for the three harpy deaths as: one felled by Valphine's bolts, one by Vicious Mockery — leaving the third unexplained, and explicitly paints Brewbarry as hitting nothing all night. The scene list, however, credits Brewbarry a lethal halberd blow on one harpy ("Brewbarry delivers a final, lethal blow with his halberd to one of the harpies"). The Memorable Moment "Brewbarry delivers the killing blow on Moesko… After a session full of missed attacks… finally lands the decisive strike" also contradicts the scene-level harpy kill.
- **Evidence**: Internal to the recap; `campaign_state.md` says only "All three harpies defeated" with no attribution.
- **Suggested fix**: Reconcile: either add Brewbarry's harpy kill to the Summary (and soften "missing everything in sight"), or remove it from the scene list if it didn't happen — check the transcript.

**7. Player quote laundered into an in-fiction character beat**
- **Location**: Summary (paragraph 3) vs. Memorable Moments quote
- **Issue**: The Summary says "one party member muttering that Vukradin had a talent for failing upward," but the quote block attributes "He's failing upward" to **David** — who is Vukradin's *own player* (David Mendenhall, per the party doc). An out-of-character table comment by the character's own player has been rendered as an in-fiction remark by a companion. No party member said it in-fiction.
- **Suggested fix**: Either drop the "one party member muttering" framing from the Summary, or verify a different player/character actually said it in-fiction.

## Mechanics vs. character sheets

**8. Self-targeted Bardic Inspiration**
- **Location**: Summary, Memorable Moments, Scenes, Spells ("Vukradin granted himself bardic inspiration, allowing him to turn a failed wisdom saving throw… into a success")
- **Issue**: Bardic Inspiration targets "one creature other than yourself"; nothing on Vukradin's sheet (Bardic Inspiration ×4/SR, Font of Inspiration, Unfailing Inspiration, Silver Tongue per `party.md`) permits self-inspiration or retroactive save conversion on himself.
- **Evidence**: `party.md` Vukradin stat block and feature list.
- **Suggested fix**: Verify against the transcript what actually happened (e.g., a house ruling, or an inspiration die he'd been holding from another source). If it was a table ruling, keep the beat but annotate it as such so future sessions don't cite it as a repeatable ability.

**9. Two cantrips in one strike**
- **Location**: Summary ("Soma struck first with a lash of thorns **and** a cloud of toxic gas"), Scenes ("a whip of thorns and a spray of poison")
- **Issue**: Thorn Whip and Poison Spray are both action-cast cantrips; they cannot both land in a single turn. Almost certainly two consecutive rounds compressed into one sentence.
- **Suggested fix**: Reword to sequence them ("opened with a whip of thorns, then followed with a spray of poison") so the recap doesn't imply a double-cantrip turn.

## Minor notes

**10. "Spells" section includes non-spells** — Wild Shape and Bardic Inspiration are class features, not spells. Harmless in a recap, but consider a "Spells & Abilities" heading.

**11. Silence scope** — Scene 1 says the sphere "deafen[s] the party **and the harpies**"; Silence only deafens creatures inside the 20-ft sphere, and the harpies were airborne outside it. The Spells section states it correctly ("Everyone within the sphere was deafened"). Align the scene bullet.

**12. "Disrupted its concentration"** — a harpy's Luring Song is not a concentration effect (damage grants charmed targets a repeat save). Loose narration, repeated for both Valphine's crit and Vukradin's blast; fine as color, but don't let "concentration" harden into the grounding docs.

## Verified as consistent (no action)

- Chapter placement: Tower of Storms at ch8 matches the canon timeline ("Ch08–09 | Tower of Storms: Moesko defeated"), and the party's prior knowledge of the conch's origin is supported by the ch7 Crabby encounter (registry: Crabby "was gifted intelligence by the sea elf Miraal… in exchange for laying Miraal's spirit to rest").
- Tower described atop an ~80-ft rocky outcropping — matches registry.
- Potion of Water Breathing found in the harpy nest (T5) — matches registry and campaign_state.
- All three harpies defeated; Silence neutralizing the songs — matches campaign_state.
- Soma's wolf-spider and brown-bear forms — match her documented wild shapes.
- Valphine's mace + hand crossbow — match her item list.
- Opalescent conch in Moesko's possession, taken from the sea elf, party intends to investigate — matches registry (name spelling aside, see #2).
- Thunderwave's 10-foot push, the Shrine of Talos frescoes, and the lightning-rod altar all match the registry's T4/T8 notes.